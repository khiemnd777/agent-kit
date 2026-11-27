#!/usr/bin/env python3
"""Offline draft-contract checks. Never executes, authorizes or authenticates a job."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parent
MAX_DOCUMENT_BYTES = 2 * 1024 * 1024
SCHEMAS = {
    "execution_request": "execution-request.schema.json",
    "execution_result": "execution-result.schema.json",
    "capability_descriptor": "capability.schema.json",
}


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _no_constant(value: str) -> None:
    raise ValueError(f"Non-finite JSON constant is not supported: {value}")


def load_json(path: Path) -> Any:
    """Read bounded UTF-8 JSON, rejecting ambiguous/nonstandard input."""
    with path.open("rb") as stream:
        raw = stream.read(MAX_DOCUMENT_BYTES + 1)
    if len(raw) > MAX_DOCUMENT_BYTES:
        raise ValueError("JSON document exceeds the 2 MiB offline-check limit")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_object,
                           parse_constant=_no_constant)
    except RecursionError as exc:
        raise ValueError("JSON nesting is too deep") from exc
    stack = [(value, 0)]
    while stack:
        node, depth = stack.pop()
        if depth > 64:
            raise ValueError("JSON nesting exceeds 64 levels")
        if isinstance(node, float) and not math.isfinite(node):
            raise ValueError("Non-finite JSON number is unsupported")
        if isinstance(node, dict):
            stack.extend((child, depth + 1) for child in node.values())
        elif isinstance(node, list):
            stack.extend((child, depth + 1) for child in node)
    return value


def canonical_digest(value: Any) -> str:
    # Local draft profile, not RFC 8785 or an authentication mechanism.
    data = json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _validator_class() -> Any:
    try:
        from jsonschema import Draft202012Validator
    except ImportError as exc:
        raise RuntimeError("NOT_RUN: jsonschema is unavailable; no dependency is auto-installed") from exc
    return Draft202012Validator


def _local_schema_errors(schema: dict[str, Any]) -> list[str]:
    """No schema lookup may cause a network read, including via nested references."""
    errors: list[str] = []
    stack: list[Any] = [schema]
    while stack:
        item = stack.pop()
        if isinstance(item, dict):
            for key, value in item.items():
                if key in {"$ref", "$dynamicRef"} and (
                        not isinstance(value, str) or not value.startswith("#")):
                    errors.append("Only local fragment schema references are supported offline")
                if key == "$id":
                    errors.append("Embedded $id is unsupported in this local draft checker")
                stack.append(value)
        elif isinstance(item, list):
            stack.extend(item)
    return errors


def validate_schema_document(schema: dict[str, Any]) -> list[str]:
    errors = _local_schema_errors(schema)
    if errors:
        return errors
    validator = _validator_class()
    try:
        validator.check_schema(schema)
    except Exception as exc:
        return [f"Invalid JSON Schema: {type(exc).__name__}"]
    return []


def validate_with_schema(schema: dict[str, Any], value: Any) -> list[str]:
    errors = validate_schema_document(schema)
    if errors:
        return errors
    validator = _validator_class()
    from referencing import Registry
    from referencing.exceptions import NoSuchResource

    def refuse_remote(uri: str) -> Any:
        raise NoSuchResource(ref=uri)

    try:
        instance = validator(schema, format_checker=validator.FORMAT_CHECKER,
                             registry=Registry(retrieve=refuse_remote))
        for error in sorted(instance.iter_errors(value), key=lambda e: str(list(e.path))):
            # Do not print input values: they could contain private data.
            location = "/".join(str(part) for part in error.path) or "<root>"
            errors.append(f"{location}: violates {error.validator}")
    except Exception as exc:
        errors.append(f"Schema evaluation failed safely: {type(exc).__name__}")
    return errors


def shape_errors(value: Any, expected_kind: str, root: Path = ROOT) -> list[str]:
    schema = load_json(root / "contracts" / SCHEMAS[expected_kind])
    return validate_with_schema(schema, value)


def _duplicates(items: list[str]) -> bool:
    return len(items) != len(set(items))


def _safe_relative_path(path: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,255}", path)) and all(
        part not in {"", ".", ".."} for part in path.split("/"))


def _safe_logical_path(path: str) -> bool:
    match = re.fullmatch(r"(source|scratch):/(.*)", path)
    if not match:
        return False
    tail = match.group(2)
    return not tail or _safe_relative_path(tail)


def request_errors(request: Any, capability: Any | None = None,
                   root: Path = ROOT) -> list[str]:
    errors = shape_errors(request, "execution_request", root)
    if errors:
        return errors
    try:
        canonical_digest(request)
    except (TypeError, ValueError):
        return ["Request must contain finite, JSON-serializable values"]
    ids = [check["id"] for check in request["checks"]]
    if _duplicates(ids):
        errors.append("Duplicate requested check IDs")
    if not any(check["required"] for check in request["checks"]):
        errors.append("At least one observable required check is needed")
    auth = request["authorization"]
    if any(not _safe_logical_path(path) for path in auth["allowed_paths"]):
        errors.append("Invalid logical path: only contained source:/ or scratch:/ paths are supported")
    network = "network" in auth["allowed_effects"]
    if network != bool(auth["network_hosts"]):
        errors.append("Network effect and explicit network host allowlist must agree")
    if capability is not None:
        cap_errors = shape_errors(capability, "capability_descriptor", root)
        if cap_errors:
            return errors + ["capability: " + error for error in cap_errors]
        if capability["capability"] != request["capability"]:
            errors.append("Capability identity/version/digest mismatch")
        if not set(capability["effects"]).issubset(auth["allowed_effects"]):
            errors.append("Capability effects exceed the declared authorization bounds")
        if capability["lifecycle"] == "reviewed" and not capability["review_ref"]:
            errors.append("Reviewed capability needs a review reference (not proof of trust)")
        if capability["replay_policy"] != "safe_read_only" and request["limits"]["max_attempts"] > 1:
            errors.append("This draft requires one attempt unless replay is declared safe_read_only")
        if capability["replay_policy"] == "safe_read_only" and "write_source" in capability["effects"]:
            errors.append("safe_read_only conflicts with write_source")
        input_schema = capability["input_schema"]
        if input_schema.get("type") != "object" or input_schema.get("additionalProperties") is not False:
            errors.append("Capability inputs need an explicit object schema and unknown-field rejection")
        errors.extend("inputs: " + error for error in validate_with_schema(input_schema, request["inputs"]))
    # Deliberately no live expiry/authority/availability check here.
    return errors


def result_errors(request: Any, result: Any, capability: Any | None = None,
                  root: Path = ROOT) -> list[str]:
    errors = request_errors(request, capability, root)
    errors.extend(shape_errors(result, "execution_result", root))
    if errors:
        return errors
    for key in ("request_id", "capability", "target"):
        if result[key] != request[key]:
            errors.append(f"Result {key} does not match the request")
    if result["request_digest"] != canonical_digest(request):
        errors.append("Result request_digest does not match the complete request")
    expected = {item["id"]: item for item in request["checks"]}
    observed = [item["id"] for item in result["checks"]]
    if _duplicates(observed):
        errors.append("Duplicate result check IDs")
    if set(observed) != set(expected):
        errors.append("Terminal result must account for exactly the requested check IDs")
    artifact_ids = [item["id"] for item in result["artifacts"]]
    artifact_paths = [item["relative_path"] for item in result["artifacts"]]
    if _duplicates(artifact_ids) or _duplicates(artifact_paths):
        errors.append("Artifact IDs and paths must be unique")
    known_artifacts = set(artifact_ids)
    if any(not _safe_relative_path(path) for path in artifact_paths):
        errors.append("Unsafe artifact relative path")
    for check in result["checks"]:
        if not set(check["evidence_ids"]).issubset(known_artifacts):
            errors.append(f"{check['id']}: references an undeclared artifact")
        if check["status"] in {"PASS", "FAIL"} and not check["evidence_ids"]:
            errors.append(f"{check['id']}: observed PASS/FAIL needs evidence references")
        if not check["detail"].strip():
            errors.append(f"{check['id']}: outcome/reason cannot be whitespace")
    for exception in result["exceptions"]:
        if exception["related_check"] is not None and exception["related_check"] not in expected:
            errors.append("Exception refers to an unknown check")
    if result["logs_truncated"] and not result["artifacts"]:
        errors.append("Truncated logs require retained artifact references")
    limits = request["limits"]
    if len(result["summary"].encode("utf-8")) > limits["max_summary_bytes"]:
        errors.append("Summary exceeds the requested UTF-8 byte budget")
    if sum(item["size_bytes"] for item in result["artifacts"]) > limits["max_evidence_bytes"]:
        errors.append("Declared evidence exceeds the requested byte budget")
    metrics = result["metrics"]
    if metrics["attempts"] > limits["max_attempts"]:
        errors.append("Attempt count exceeds the requested limit")
    if result["started_at"] is not None:
        try:
            start = datetime.fromisoformat(result["started_at"].replace("Z", "+00:00"))
            end = datetime.fromisoformat(result["finished_at"].replace("Z", "+00:00"))
            if end < start:
                errors.append("finished_at is earlier than started_at")
        except ValueError:
            errors.append("Timestamp is outside this checker's supported datetime profile")
    usage = metrics["usage"]
    counters = [usage[key] for key in ("input_tokens", "output_tokens", "cache_read_tokens",
                                      "cache_write_tokens", "reasoning_tokens")]
    if any(value is None for value in counters) and not usage["unavailable_reason"]:
        errors.append("Unavailable usage counters need a reason")
    if any(value is not None for value in counters) and not usage["source"]:
        errors.append("Measured usage counters, including zero, need provenance")
    if result["status"] == "succeeded":
        if result["run_id"] is None or result["started_at"] is None or metrics["attempts"] < 1:
            errors.append("Success requires an observed run/start and at least one attempt")
        if result["effects_state"] == "unknown" or result["exceptions"]:
            errors.append("Success cannot contain unknown effects or unresolved exceptions")
        for check in result["checks"]:
            if check["status"] == "FAIL":
                errors.append("Success cannot contain a failed check")
            if expected.get(check["id"], {}).get("required") and check["status"] != "PASS":
                errors.append(f"{check['id']}: required check must PASS for success")
        if metrics["duration_seconds"] is not None and metrics["duration_seconds"] > limits["max_duration_seconds"]:
            errors.append("Successful duration exceeds the requested limit")
    elif not result["exceptions"]:
        errors.append("Non-success requires an actionable exception/reason")
    if result["effects_state"] == "unknown" and not any(
            item["next_action"] == "reconcile" for item in result["exceptions"]):
        errors.append("Unknown effects require reconciliation, not automatic replay")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--capability", type=Path)
    args = parser.parse_args(argv)
    try:
        request = load_json(args.request)
        capability = load_json(args.capability) if args.capability else None
        errors = (result_errors(request, load_json(args.result), capability) if args.result
                  else request_errors(request, capability))
    except (OSError, ValueError, RuntimeError, UnicodeError) as exc:
        print(f"NOT_VALIDATED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"valid": not errors, "scope": "offline document consistency only",
                      "execution_performed": False, "authority_verified": False,
                      "errors": errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
