"""Single-user local authorization boundary; metadata is not identity authentication."""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
import importlib.metadata
import os
from pathlib import Path
import platform
import shutil
import sys
import uuid
from typing import Any

from . import __version__
from .contract import canonical_digest, request_errors, validate_with_schema
from .io import SidecarError, atomic_json, digest_bytes, instant, now, read_bytes, read_json
from .registry import Workflow

DEFAULT_LIMITS = {"max_duration_seconds": 300, "max_attempts": 1, "max_concurrency": 4,
                  "max_summary_bytes": 4096, "max_evidence_bytes": 2 * 1024 * 1024}
LIMITS_SCHEMA = read_json(Path(__file__).parent / "contracts/execution-request.schema.json")["properties"]["limits"]
POLICY_SCHEMA: dict[str, Any] = {
    "type": "object", "additionalProperties": False,
    "required": ["format", "repositories", "capabilities", "limits", "max_authorization_seconds",
                 "allow_trusted_process", "process_risk_acknowledgement", "tools"],
    "properties": {
        "format": {"const": "sidecar.policy/v1"},
        "repositories": {"type": "array", "minItems": 1, "maxItems": 64, "uniqueItems": True,
                         "items": {"type": "string", "minLength": 1, "maxLength": 256}},
        "capabilities": {"type": "array", "minItems": 1, "maxItems": 64, "items": {
            "type": "object", "additionalProperties": False, "required": ["id", "version", "digest"],
            "properties": {"id": {"type": "string"}, "version": {"type": "string"},
                           "digest": {"type": "string", "pattern": "^sha256:[0-9a-f]{64}$"}}}},
        "limits": LIMITS_SCHEMA,
        "max_authorization_seconds": {"type": "integer", "minimum": 1, "maximum": 86400},
        "allow_trusted_process": {"type": "boolean"},
        "process_risk_acknowledgement": {"enum": [None, "trusted-code-only-no-os-sandbox"]},
        "tools": {"type": "object", "maxProperties": 32, "additionalProperties": {
            "type": "object", "required": ["path", "digest"], "additionalProperties": False,
            "properties": {"path": {"type": "string", "minLength": 1, "maxLength": 1024},
                           "digest": {"type": "string", "pattern": "^sha256:[0-9a-f]{64}$"}}}}
    }
}


def load_policy(path: Path) -> dict[str, Any]:
    data = read_json(path)
    errors = validate_with_schema(POLICY_SCHEMA, data)
    if errors:
        raise SidecarError("invalid_policy", "; ".join(errors[:8]), "authorize")
    if data["allow_trusted_process"] != (data["process_risk_acknowledgement"] == "trusted-code-only-no-os-sandbox"):
        raise SidecarError("process_risk", "Trusted host execution needs explicit unconfined-process acknowledgement", "authorize")
    ids = [v["id"] for v in data["capabilities"]]
    if len(set(ids)) != len(ids):
        raise SidecarError("invalid_policy", "Duplicate capability identities", "authorize")
    return data


def tool_identity(path: Path) -> dict[str, str]:
    path = path.resolve(strict=True)
    if not path.is_file() or not os.access(path, os.X_OK):
        raise SidecarError("tool_unavailable", "Pinned tool is not executable", "fix_environment")
    return {"path": str(path), "digest": digest_bytes(read_bytes(path, 128 * 1024 * 1024))}


def make_policy(workflows: list[Workflow], repositories: list[str], tools: dict[str, str],
                trusted_process: bool = False) -> dict[str, Any]:
    if not workflows:
        raise SidecarError("empty_policy", "Explicitly select at least one reviewed workflow", "authorize")
    if any(w.data["lifecycle"] != "reviewed" for w in workflows):
        raise SidecarError("unreviewed", "A draft workflow cannot enter a live policy", "authorize")
    if any(w.has_process for w in workflows) and not trusted_process:
        raise SidecarError("process_disabled", "Selected workflow executes code; explicit trusted-process opt-in is required", "authorize")
    resolved = {}
    for name, path in tools.items():
        if not name or "/" in name or "\\" in name:
            raise SidecarError("invalid_tool", "Tool name must be a bare name")
        resolved[name] = tool_identity(Path(path))
    needed = {s["argv"][0] for w in workflows for s in w.data["steps"] if s["executor"] == "process"}
    if not needed <= set(resolved):
        raise SidecarError("missing_tool", "Every process executable must be explicitly pinned", "fix_environment")
    return {"format": "sidecar.policy/v1", "repositories": repositories,
            "capabilities": [w.descriptor["capability"] for w in workflows],
            "limits": dict(DEFAULT_LIMITS), "max_authorization_seconds": 3600,
            "allow_trusted_process": trusted_process,
            "process_risk_acknowledgement": "trusted-code-only-no-os-sandbox" if trusted_process else None,
            "tools": resolved}


def environment(policy: dict[str, Any]) -> dict[str, Any]:
    package = Path(__file__).parent
    engine_files = []
    for path in sorted(package.rglob("*")):
        if path.suffix in {".py", ".json"} and "__pycache__" not in path.parts:
            engine_files.append({"path": path.relative_to(package).as_posix(),
                                 "digest": digest_bytes(read_bytes(path))})
    tools = {}
    for name, pinned in policy["tools"].items():
        actual = tool_identity(Path(pinned["path"]))
        if actual != pinned:
            raise SidecarError("tool_changed", "Executable bytes differ from the policy pin", "fix_environment")
        tools[name] = actual
    return {"profile": "local-runtime-fingerprint/v1", "sidecar": __version__,
            "python": sys.version, "python_executable": tool_identity(Path(sys.executable)),
            "system": platform.system(), "machine": platform.machine(), "release": platform.release(),
            "engine_digest": canonical_digest(engine_files), "tools": tools,
            "dependencies": {p: importlib.metadata.version(p) for p in ("jsonschema", "PyYAML")},
            "process_environment_profile": "minimal-v1"}


def checks_for(wf: Workflow) -> list[dict[str, Any]]:
    return [{"id": s["id"], "required": True, "criterion": s["criterion"]} for s in wf.data["steps"]]


def prepare_request(wf: Workflow, policy: dict[str, Any], snapshot: dict[str, Any],
                    inputs: dict[str, Any], objective: str, scope: str, decision_ref: str,
                    ttl: int = 1800) -> dict[str, Any]:
    if ttl < 1 or ttl > policy["max_authorization_seconds"]:
        raise SidecarError("ttl_limit", "Authorization window exceeds the policy")
    request = {"schema_version": "0.1.0", "kind": "execution_request",
               "request_id": "req-" + uuid.uuid4().hex, "objective": objective,
               "capability": wf.descriptor["capability"],
               "target": {"repository": snapshot["repository"], "snapshot": snapshot["snapshot"],
                          "environment_digest": canonical_digest(environment(policy)),
                          "policy_digest": canonical_digest(policy)},
               "inputs": inputs,
               "authorization": {"scope_id": scope, "decision_ref": decision_ref,
                                 "allowed_effects": ["read_source", "write_scratch"],
                                 "allowed_paths": ["source:/", "scratch:/"], "network_hosts": [],
                                 "expires_at": (datetime.now(timezone.utc) + timedelta(seconds=ttl)).isoformat()},
               "checks": checks_for(wf), "limits": dict(policy["limits"])}
    admit(request, wf, policy)
    return request


def admit(request: dict[str, Any], wf: Workflow, policy: dict[str, Any],
          permit: dict[str, Any] | None = None) -> None:
    errors = request_errors(request, wf.descriptor)
    if errors:
        raise SidecarError("request_rejected", "; ".join(errors[:8]))
    if wf.data["lifecycle"] != "reviewed" or request["capability"] not in policy["capabilities"]:
        raise SidecarError("untrusted_capability", "Workflow is unreviewed or not pinned in the supplied policy", "authorize")
    target = request["target"]
    if target["repository"] not in policy["repositories"]:
        raise SidecarError("target_not_authorized", "Repository is outside the supplied policy", "authorize")
    if target["snapshot"]["kind"] != "content_digest":
        raise SidecarError("snapshot_profile", "This release accepts content snapshots, not unverified Git HEAD values")
    if target["policy_digest"] != canonical_digest(policy):
        raise SidecarError("policy_changed", "Policy fingerprint differs from the request", "authorize")
    if target["environment_digest"] != canonical_digest(environment(policy)):
        raise SidecarError("environment_changed", "Runtime fingerprint differs; prepare a new request", "fix_environment")
    if request["checks"] != checks_for(wf):
        raise SidecarError("check_mismatch", "Requested check IDs/criteria must match the pinned workflow")
    auth = request["authorization"]
    if (set(auth["allowed_effects"]) != {"read_source", "write_scratch"}
            or set(auth["allowed_paths"]) != {"source:/", "scratch:/"} or auth["network_hosts"]):
        raise SidecarError("unsupported_authority", "V1 only accepts source read and private scratch write; no network/source writes", "authorize")
    until = instant(auth["expires_at"])
    left = (until - datetime.now(timezone.utc)).total_seconds()
    if left <= 0:
        raise SidecarError("authorization_expired", "Authorization has expired", "authorize")
    if left > policy["max_authorization_seconds"] + 1:
        raise SidecarError("authorization_window", "Authorization lifetime exceeds the policy", "authorize")
    if any(request["limits"][k] > v for k, v in policy["limits"].items()):
        raise SidecarError("budget_exceeded", "Request exceeds a policy resource/output ceiling", "authorize")
    if request["limits"]["max_evidence_bytes"] < len(wf.data["steps"]) * 8192:
        raise SidecarError("evidence_budget", "Reserve at least 8192 evidence bytes per workflow step")
    if wf.has_process:
        if os.name != "posix":
            raise SidecarError("platform_unsupported", "Process executor is supported on POSIX only", "fix_environment")
        if not policy["allow_trusted_process"]:
            raise SidecarError("process_disabled", "Trusted host execution is disabled", "authorize")
        for step in wf.data["steps"]:
            if step["executor"] == "process" and step["argv"][0] not in policy["tools"]:
                raise SidecarError("tool_not_pinned", "Workflow executable is absent from policy", "authorize")
    if permit is not None:
        expected = {"format", "request_id", "request_digest", "policy_digest", "decision_ref", "expires_at", "approved_at"}
        if not isinstance(permit, dict) or set(permit) != expected:
            raise SidecarError("invalid_permit", "Invalid permit shape", "authorize")
        if (permit["format"] != "sidecar.local-permit/v1" or permit["request_id"] != request["request_id"]
                or permit["request_digest"] != canonical_digest(request)
                or permit["policy_digest"] != target["policy_digest"]
                or permit["decision_ref"] != auth["decision_ref"] or permit["expires_at"] != auth["expires_at"]):
            raise SidecarError("permit_mismatch", "Local permit does not authorize this exact request", "authorize")
        try:
            approved = instant(permit["approved_at"])
            if approved > datetime.now(timezone.utc) or approved >= until:
                raise ValueError()
        except (TypeError, ValueError):
            raise SidecarError("invalid_permit", "Permit approval timestamp is invalid", "authorize")


def authorize(request: dict[str, Any], wf: Workflow, policy: dict[str, Any]) -> dict[str, Any]:
    admit(request, wf, policy)
    return {"format": "sidecar.local-permit/v1", "request_id": request["request_id"],
            "request_digest": canonical_digest(request), "policy_digest": canonical_digest(policy),
            "decision_ref": request["authorization"]["decision_ref"],
            "expires_at": request["authorization"]["expires_at"], "approved_at": now()}
