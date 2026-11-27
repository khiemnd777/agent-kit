"""One request -> autonomous DAG execution -> one evidence-bound terminal result."""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, Future
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import threading
import time
import uuid
from typing import Any

from .contract import canonical_digest, request_errors, result_errors, shape_errors
from .executors import Control, Interrupted, Outcome, builtin, process
from .io import (SidecarError, atomic_json, contained, digest_bytes, instant, now,
                 read_bytes, read_json, utf8_prefix)
from .policy import admit, environment
from .registry import Workflow
from .snapshots import initialize_state, verify_snapshot


def usage(processes: bool) -> dict[str, Any]:
    fields = ("input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens")
    return {**{key: None if processes else 0 for key in fields},
            "source": None if processes else "Sidecar builtins only; no model API or subprocess invocation",
            "unavailable_reason": "External subprocess token usage is not instrumented" if processes else None}


def base_result(request: dict[str, Any]) -> dict[str, Any]:
    return {"schema_version": "0.1.0", "kind": "execution_result", "request_id": request["request_id"],
            "request_digest": canonical_digest(request), "run_id": None,
            "capability": request["capability"], "target": request["target"], "status": "blocked",
            "summary": "Execution did not start", "started_at": None, "finished_at": now(),
            "effects_state": "none", "checks": [{"id": c["id"], "status": "NOT_RUN",
                "detail": "Execution did not start", "evidence_ids": []} for c in request["checks"]],
            "artifacts": [], "exceptions": [], "logs_truncated": False,
            "metrics": {"duration_seconds": 0, "attempts": 0, "usage": usage(False)}}


def blocked_result(request: dict[str, Any], error: SidecarError) -> dict[str, Any]:
    result = base_result(request)
    result["summary"] = utf8_prefix("BLOCKED: " + error.message, request["limits"]["max_summary_bytes"])
    result["exceptions"] = [{"code": error.code, "message": error.message[:2048],
                             "next_action": error.action, "related_check": None}]
    return result


def verify_result(request: dict[str, Any], result: dict[str, Any], root: Path,
                  capability: dict[str, Any] | None = None) -> None:
    errors = result_errors(request, result, capability)
    if errors:
        raise SidecarError("invalid_result", "; ".join(errors[:8]))
    for item in result["artifacts"]:
        try:
            path = contained(root, item["relative_path"])
            data = read_bytes(path, min(item["size_bytes"] + 1, request["limits"]["max_evidence_bytes"] + 1))
        except (OSError, SidecarError) as exc:
            raise SidecarError("missing_evidence", "Artifact is missing, unsafe or unreadable") from exc
        if len(data) != item["size_bytes"] or digest_bytes(data) != item["digest"]:
            raise SidecarError("evidence_mismatch", "Artifact content does not match its declared bytes")


def _write_artifact(run_root: Path, artifact_id: str, relative: str, content: bytes,
                    media_type: str) -> dict[str, Any]:
    path = run_root / relative
    path.parent.mkdir(exist_ok=True, mode=0o700)
    path = contained(run_root, relative, must_exist=False)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as stream:
        stream.write(content); stream.flush(); os.fsync(stream.fileno())
    return {"id": artifact_id, "relative_path": relative, "digest": digest_bytes(content),
            "media_type": media_type, "size_bytes": len(content)}


def _persist_outcome(step: dict[str, Any], outcome: Outcome, run_root: Path,
                     allowance: int) -> tuple[list[dict[str, Any]], list[str]]:
    artifacts, ids = [], []
    receipt = {"format": "sidecar.step-evidence/v1", "step": step["id"],
               "check_status": outcome.check_status, "detail": outcome.detail,
               "attempts": outcome.attempts, "attempt_records": outcome.receipts,
               "payload": outcome.payload, "logs_truncated": outcome.truncated,
               "effects_unknown": outcome.effects_unknown}
    content = (json.dumps(receipt, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    if len(content) + len(outcome.log) > allowance:
        original_size = len(content)
        receipt["payload"] = {"omitted": True, "reason": "evidence_budget_exceeded", "original_receipt_bytes": original_size}
        outcome.terminal = "escalated"
        outcome.detail = "Evidence budget exceeded; retained record is incomplete"
        receipt["original_observed_status"] = outcome.check_status
        receipt["original_detail"] = receipt["detail"]
        if outcome.check_status != "FAIL":
            outcome.check_status = "NOT_RUN"
        outcome.action = "reconcile" if outcome.effects_unknown else "reason"
        outcome.truncated = True
        receipt.update(check_status=outcome.check_status, detail=outcome.detail, logs_truncated=True)
        content = (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        outcome.log = outcome.log[:max(0, allowance - len(content))]
    if len(content) > allowance:
        raise SidecarError("internal_evidence_budget", "Minimal step evidence cannot fit its reserved budget")
    if outcome.log:
        artifact_id = step["id"] + ".log"
        artifacts.append(_write_artifact(run_root, artifact_id, "logs/" + artifact_id,
                                         outcome.log, "application/octet-stream"))
        ids.append(artifact_id)
    artifact_id = step["id"] + ".receipt"
    artifacts.append(_write_artifact(run_root, artifact_id, "evidence/" + step["id"] + ".json",
                                     content, "application/json"))
    ids.append(artifact_id)
    return artifacts, ids


def execute(request: dict[str, Any], wf: Workflow, policy: dict[str, Any], permit: dict[str, Any],
            state: Path, cancelled: threading.Event | None = None) -> dict[str, Any]:
    basic = request_errors(request)
    if basic:
        raise SidecarError("invalid_request", "; ".join(basic[:8]))
    state = initialize_state(state)
    try:
        if not isinstance(permit, dict):
            raise SidecarError("invalid_permit", "A concrete request-bound permit is required", "authorize")
        admit(request, wf, policy, permit)
        source, _ = verify_snapshot(state, request["target"]["snapshot"]["value"])
    except SidecarError as exc:
        return blocked_result(request, exc)
    except FileNotFoundError:
        return blocked_result(request, SidecarError("missing_snapshot", "Prepare the content snapshot first", "fix_environment"))
    claim_path = state / "claims" / (request["request_id"] + ".json")
    request_digest = canonical_digest(request)
    run_id = "run-" + uuid.uuid4().hex
    claim = {"format": "sidecar.claim/v1", "request_digest": request_digest,
             "run_id": run_id, "pid": os.getpid(), "state": "running", "created_at": now()}
    try:
        atomic_json(claim_path, claim, exclusive=True)
    except FileExistsError:
        old = read_json(claim_path)
        if old.get("request_digest") != request_digest:
            return blocked_result(request, SidecarError("request_id_conflict", "Request ID already binds different content"))
        if not (state / "runs" / old["run_id"]).exists():
            return blocked_result(request, SidecarError("inflight_or_interrupted",
                "Request has a live/stranded claim; do not replay", "reconcile"))
        run_root = contained(state / "runs", old["run_id"])
        if (run_root / "result.json").exists():
            prior = read_json(contained(run_root, "result.json"))
            verify_result(request, prior, run_root, wf.descriptor)
            return prior
        return blocked_result(request, SidecarError("inflight_or_interrupted",
            "Request is active or interrupted without terminal evidence; inspect and reconcile, never auto-replay", "reconcile"))
    run_root = state / "runs" / run_id
    run_root.mkdir(mode=0o700)
    atomic_json(run_root / "request.json", request)
    atomic_json(run_root / "capability.json", wf.descriptor)
    atomic_json(run_root / "workflow.json", wf.data)
    atomic_json(run_root / "policy.json", policy)
    atomic_json(run_root / "permit.json", permit)
    atomic_json(run_root / "state.json", {"state": "running", "run_id": run_id, "request_digest": request_digest})
    result = base_result(request)
    result["run_id"] = run_id; result["started_at"] = now()
    start = time.monotonic()
    seconds_left = (instant(request["authorization"]["expires_at"]) - datetime.now(timezone.utc)).total_seconds()
    control = Control(cancelled or threading.Event(), start + min(request["limits"]["max_duration_seconds"], seconds_left))
    steps = wf.data["steps"]
    pending = {s["id"]: s for s in steps}
    completed: dict[str, Outcome] = {}
    running: dict[Future[Outcome], dict[str, Any]] = {}
    artifacts_by_step: dict[str, list[dict[str, Any]]] = {}
    evidence_by_step: dict[str, list[str]] = {}
    allowance = request["limits"]["max_evidence_bytes"] // len(steps)
    concurrency = request["limits"]["max_concurrency"]
    stopped: str | None = None

    def work(step: dict[str, Any]) -> Outcome:
        try:
            if step["executor"] == "builtin":
                return builtin(step, source, request["inputs"], control)
            scratch = run_root / "scratch" / step["id"]
            scratch.mkdir(parents=True, mode=0o700)
            return process(step, source, scratch, request["inputs"], policy, control,
                           request["limits"]["max_attempts"], max(0, allowance - 4096))
        except Exception as exc:
            # Source/command output is untrusted; do not dump exception values to context.
            return Outcome(detail="Unexpected executor error: " + type(exc).__name__, terminal="escalated",
                           effects_unknown=step["executor"] == "process",
                           action="reconcile" if step["executor"] == "process" else "reason")

    with ThreadPoolExecutor(max_workers=concurrency, thread_name_prefix="sidecar") as pool:
        while pending or running:
            try:
                control.check()
            except Interrupted as exc:
                stopped = exc.status
            for sid, step in list(pending.items()):
                if stopped:
                    completed[sid] = Outcome(detail="Not started: run " + stopped)
                    del pending[sid]; continue
                if not set(step["needs"]) <= set(completed): continue
                if step.get("when", "success") == "success" and any(completed[n].check_status != "PASS" for n in step["needs"]):
                    completed[sid] = Outcome(detail="Not started: upstream check did not PASS")
                    del pending[sid]; continue
                if len(running) >= concurrency: break
                running[pool.submit(work, step)] = step
                del pending[sid]
            if not running:
                if pending:
                    raise SidecarError("scheduler_stuck", "No runnable step; workflow invariant failed")
                break
            ready, _ = wait(running, timeout=0.05, return_when=FIRST_COMPLETED)
            for future in ready:
                step = running.pop(future); outcome = future.result()
                arts, ids = _persist_outcome(step, outcome, run_root, allowance)
                artifacts_by_step[step["id"]] = arts; evidence_by_step[step["id"]] = ids
                completed[step["id"]] = outcome
    boundary_changed = False
    try:
        verify_snapshot(state, request["target"]["snapshot"]["value"])
        if canonical_digest(environment(policy)) != request["target"]["environment_digest"]:
            boundary_changed = True
    except (SidecarError, OSError, ValueError):
        boundary_changed = True
    statuses = {o.terminal for o in completed.values() if o.terminal}
    if boundary_changed:
        statuses.add("escalated")
    if stopped: statuses.add(stopped)
    missing = any(o.check_status != "PASS" for o in completed.values())
    result["status"] = next((s for s in ("cancelled", "timed_out", "escalated", "failed", "blocked") if s in statuses),
                            "failed" if missing else "succeeded")
    result["checks"] = []
    for step in steps:
        outcome = completed[step["id"]]
        result["checks"].append({"id": step["id"], "status": outcome.check_status, "detail": outcome.detail,
                                  "evidence_ids": evidence_by_step.get(step["id"], [])})
        result["artifacts"].extend(artifacts_by_step.get(step["id"], []))
        result["logs_truncated"] |= outcome.truncated
        if outcome.terminal:
            result["exceptions"].append({"code": "step_" + outcome.terminal, "message": outcome.detail,
                                           "next_action": outcome.action, "related_check": step["id"]})
    result["effects_state"] = "unknown" if boundary_changed or any(o.effects_unknown for o in completed.values()) else "known"
    if boundary_changed:
        result["exceptions"].append({"code": "execution_boundary_changed",
            "message": "Snapshot or runtime identity changed during execution; do not accept the result as current proof",
            "next_action": "reconcile", "related_check": None})
    if result["status"] != "succeeded" and not result["exceptions"]:
        result["exceptions"] = [{"code": "run_incomplete", "message": "Run stopped or required evidence is incomplete",
                                  "next_action": "reason", "related_check": None}]
    if len(result["exceptions"]) > 64:
        result["exceptions"] = result["exceptions"][:63] + [{"code": "multiple_failures",
            "message": "Additional failure details remain in check evidence; reconciliation is required",
            "next_action": "reconcile", "related_check": None}]
    result["finished_at"] = now()
    duration = time.monotonic() - start
    if result["status"] == "succeeded" and (duration > request["limits"]["max_duration_seconds"] or time.monotonic() >= control.deadline):
        result["status"] = "timed_out"
        result["exceptions"] = [{"code": "run_deadline", "message": "Finalization exceeded the execution deadline",
                                  "next_action": "reason", "related_check": None}]
    result["metrics"] = {"duration_seconds": duration,
                         "attempts": max((o.attempts for o in completed.values()), default=0),
                         "usage": usage(wf.has_process)}
    counts = {s: sum(c["status"] == s for c in result["checks"]) for s in ("PASS", "FAIL", "NOT_RUN", "SKIPPED")}
    result["summary"] = utf8_prefix(f"{result['status'].upper()}: " + ", ".join(f"{n} {s}" for s, n in counts.items())
                                   + ". Evidence is execution evidence, not human acceptance.",
                                   request["limits"]["max_summary_bytes"])
    # Validate actual artifact bytes and V2 semantics before committing any success label.
    verify_result(request, result, run_root, wf.descriptor)
    atomic_json(run_root / "result.json", result)
    atomic_json(run_root / "state.json", {"state": result["status"], "run_id": run_id,
                                           "request_digest": request_digest, "finished_at": result["finished_at"]})
    atomic_json(claim_path, {**claim, "state": result["status"], "finished_at": result["finished_at"]})
    return result
