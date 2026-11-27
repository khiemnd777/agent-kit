"""Reviewed, digest-pinned workflows; the registry does not grant authority."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .contract import shape_errors, validate_schema_document, validate_with_schema
from .io import SidecarError, ID_RE, digest_bytes, structured, safe_relative

BUILTINS = {"inventory", "entrypoints", "manifest", "mirrors", "json-files"}
SCHEMA: dict[str, Any] = {
    "type": "object", "additionalProperties": False,
    "required": ["format", "id", "version", "description", "lifecycle", "review_ref",
                 "effects", "replay_policy", "input_schema", "steps"],
    "properties": {
        "format": {"const": "sidecar.workflow/v1"},
        "id": {"type": "string", "pattern": "^[a-z][a-z0-9._-]{0,63}$"},
        "version": {"type": "string", "minLength": 1, "maxLength": 64},
        "description": {"type": "string", "minLength": 1, "maxLength": 2048},
        "lifecycle": {"enum": ["draft", "reviewed"]},
        "review_ref": {"type": ["string", "null"], "maxLength": 512},
        "effects": {"type": "array", "minItems": 1, "uniqueItems": True,
                    "items": {"enum": ["read_source", "write_scratch"]}},
        "replay_policy": {"enum": ["safe_read_only", "never"]},
        "input_schema": {"type": "object"},
        "steps": {"type": "array", "minItems": 1, "maxItems": 64, "items": {
            "type": "object", "additionalProperties": False,
            "required": ["id", "executor", "needs", "criterion", "timeout_seconds"],
            "properties": {
                "id": {"type": "string", "pattern": "^[a-z][a-z0-9._-]{0,47}$"},
                "executor": {"enum": ["builtin", "process"]},
                "operation": {"type": "string"},
                "needs": {"type": "array", "maxItems": 64, "uniqueItems": True,
                          "items": {"type": "string"}},
                "criterion": {"type": "string", "minLength": 1, "maxLength": 1024},
                "timeout_seconds": {"type": "number", "minimum": 0.05, "maximum": 3600},
                "when": {"enum": ["success", "always"]},
                "argv": {"type": "array", "minItems": 1, "maxItems": 64,
                         "items": {"type": "string", "minLength": 1, "maxLength": 4096}},
                "cwd": {"type": "string", "maxLength": 512},
                "env": {"type": "object", "maxProperties": 32,
                        "additionalProperties": {"type": "string", "maxLength": 4096}},
                "retry_exit_codes": {"type": "array", "maxItems": 8, "uniqueItems": True,
                                     "items": {"type": "integer", "minimum": 2, "maximum": 125}},
                "retry_delay_seconds": {"type": "number", "minimum": 0.05, "maximum": 10},
            }
        }}
    }
}


@dataclass(frozen=True)
class Workflow:
    path: Path
    data: dict[str, Any]
    digest: str

    @property
    def descriptor(self) -> dict[str, Any]:
        d = self.data
        return {"schema_version": "0.1.0", "kind": "capability_descriptor",
                "capability": {"id": d["id"], "version": d["version"], "digest": self.digest},
                "contract_version": "0.1.0", "description": d["description"],
                "lifecycle": d["lifecycle"], "effects": d["effects"],
                "input_schema": d["input_schema"], "output_schema": "execution-result.schema.json",
                "replay_policy": d["replay_policy"], "review_ref": d["review_ref"]}

    @property
    def has_process(self) -> bool:
        return any(s["executor"] == "process" for s in self.data["steps"])


def load_workflow(path: Path) -> Workflow:
    data, raw = structured(path)
    errors = validate_with_schema(SCHEMA, data)
    if errors:
        raise SidecarError("invalid_workflow", "; ".join(errors[:8]))
    steps = {s["id"]: s for s in data["steps"]}
    if len(steps) != len(data["steps"]):
        raise SidecarError("duplicate_step", "Workflow contains duplicate step IDs")
    if data["lifecycle"] == "reviewed" and not data["review_ref"]:
        raise SidecarError("missing_review", "Reviewed workflows need a review reference")
    if data["input_schema"].get("type") != "object" or data["input_schema"].get("additionalProperties") is not False:
        raise SidecarError("input_schema", "Inputs require a closed object schema")
    errors = validate_schema_document(data["input_schema"])
    if errors:
        raise SidecarError("input_schema", "; ".join(errors[:8]))
    for s in steps.values():
        if any(n not in steps for n in s["needs"]):
            raise SidecarError("missing_dependency", "Dependency names an absent step")
        if s["executor"] == "builtin":
            if s.get("operation") not in BUILTINS or any(k in s for k in ("argv", "env", "cwd", "retry_exit_codes")):
                raise SidecarError("invalid_builtin", "Builtin step must name a supported operation only")
        else:
            if not s.get("argv") or "operation" in s:
                raise SidecarError("invalid_process", "Process step needs argv, not operation")
            if not safe_relative(s.get("cwd", "."), allow_dot=True):
                raise SidecarError("invalid_cwd", "Working directory must stay inside the private copy")
            if "{{" in s["argv"][0] or "/" in s["argv"][0] or "\\" in s["argv"][0]:
                raise SidecarError("invalid_executable", "Executable is a policy-pinned tool name, not a path or template")
            if s.get("retry_exit_codes") and data["replay_policy"] != "safe_read_only":
                raise SidecarError("unsafe_retry", "Retry requires reviewed safe_read_only replay semantics")
            for key in s.get("env", {}):
                if not key.startswith("SC_INPUT_"):
                    raise SidecarError("unsafe_environment", "Workflow env keys must start SC_INPUT_")
    # Kahn's algorithm also rejects self-dependencies; file order has no scheduling semantics.
    remaining = set(steps)
    done: set[str] = set()
    while remaining:
        ready = {k for k in remaining if set(steps[k]["needs"]) <= done}
        if not ready:
            raise SidecarError("dependency_cycle", "Workflow dependencies form a cycle")
        done |= ready
        remaining -= ready
    wf = Workflow(path.resolve(), data, digest_bytes(raw))
    if shape_errors(wf.descriptor, "capability_descriptor"):
        raise SidecarError("invalid_capability", "Workflow descriptor violates Agent Kit V2 contract")
    return wf


def load_registry(root: Path) -> dict[str, Workflow]:
    if not root.is_dir():
        raise SidecarError("missing_registry", "Registry directory is unavailable", "fix_environment")
    result: dict[str, Workflow] = {}
    for path in sorted(root.iterdir()):
        if path.suffix.lower() not in {".yaml", ".yml", ".json"}:
            continue
        wf = load_workflow(path)
        if wf.data["id"] in result:
            raise SidecarError("duplicate_capability", "Registry has duplicate capability IDs")
        result[wf.data["id"]] = wf
    return result
