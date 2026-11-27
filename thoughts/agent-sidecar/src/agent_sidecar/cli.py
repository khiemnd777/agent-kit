"""Synchronous CLI: no daemon, hidden polling, automatic installation or LLM calls."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import signal
import sys
import threading
from typing import Any

from . import __version__
from .contract import canonical_digest
from .engine import execute, verify_result
from .io import SidecarError, atomic_json, contained, read_json
from .policy import authorize, environment, load_policy, make_policy, prepare_request
from .registry import load_registry, load_workflow
from .snapshots import create_snapshot, initialize_state, verify_snapshot


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--version", action="version", version="sidecar " + __version__)
    sub = p.add_subparsers(dest="command", required=True)

    def registry_arg(s: argparse.ArgumentParser) -> None:
        s.add_argument("--registry", type=Path, default=Path("workflows"))

    def state_arg(s: argparse.ArgumentParser) -> None:
        s.add_argument("--state", type=Path, required=True, help="Private directory OUTSIDE the source root (mode 0700)")

    s = sub.add_parser("capabilities", help="List workflow identities; does not authorize them")
    registry_arg(s); s.add_argument("--id")
    s = sub.add_parser("validate-workflow", help="Validate schema, types and DAG")
    s.add_argument("path", type=Path)
    s = sub.add_parser("snapshot", help="Copy source including uncommitted/untracked non-excluded files")
    state_arg(s); s.add_argument("--source", type=Path, required=True)
    s.add_argument("--repository"); s.add_argument("--output", type=Path, required=True)
    s = sub.add_parser("policy", help="Write a bounded local policy; not a run permit")
    registry_arg(s); s.add_argument("--workflow", action="append", required=True)
    s.add_argument("--repository", action="append", required=True)
    s.add_argument("--tool", action="append", default=[], metavar="NAME=/absolute/executable")
    s.add_argument("--allow-trusted-process", action="store_true",
                   help="Acknowledge: trusted code only, no OS filesystem/network sandbox")
    s.add_argument("--output", type=Path, required=True)
    for name in ("prepare", "delegate"):
        s = sub.add_parser(name, help=("Pin without executing" if name == "prepare" else
            "One authorized call: snapshot, pin, record caller authorization, execute DAG, return evidence"))
        registry_arg(s); state_arg(s)
        group = s.add_mutually_exclusive_group(required=True)
        group.add_argument("--source", type=Path); group.add_argument("--snapshot", type=Path)
        s.add_argument("--repository"); s.add_argument("--workflow", required=True)
        s.add_argument("--policy", type=Path, required=True); s.add_argument("--inputs", type=Path)
        s.add_argument("--objective", required=True); s.add_argument("--scope-id", required=True)
        s.add_argument("--decision-ref", required=True); s.add_argument("--ttl", type=int, default=1800)
        s.add_argument("--output", type=Path, required=name == "prepare")
        if name == "delegate":
            s.add_argument("--confirm-authorized", action="store_true",
                help="Caller already has real authority for this work package; not a new approval decision")
    s = sub.add_parser("authorize", help="Explicit caller attestation for one exact request; not human identity proof")
    registry_arg(s); s.add_argument("--request", type=Path, required=True)
    s.add_argument("--policy", type=Path, required=True); s.add_argument("--output", type=Path, required=True)
    s.add_argument("--confirm", action="store_true", help="Caller has actual authority for this exact request")
    s = sub.add_parser("run", help="Execute and return a single evidence-bound terminal result")
    registry_arg(s); state_arg(s); s.add_argument("--request", type=Path, required=True)
    s.add_argument("--policy", type=Path, required=True); s.add_argument("--permit", type=Path, required=True)
    s.add_argument("--output", type=Path)
    s = sub.add_parser("verify-result", help="Check V2 semantics AND actual artifact hashes")
    s.add_argument("--request", type=Path, required=True); s.add_argument("--result", type=Path, required=True)
    s.add_argument("--run-dir", type=Path, required=True); s.add_argument("--capability", type=Path)
    s = sub.add_parser("history", help="List recent runs without loading logs or prompting a model")
    state_arg(s); s.add_argument("--limit", type=int, default=20)
    s = sub.add_parser("result", help="Read one completed result; never resumes/replays it")
    state_arg(s); s.add_argument("--run-id", required=True)
    return p


def _workflow(registry: Path, identity: str):
    items = load_registry(registry)
    if identity not in items:
        raise SidecarError("capability_unavailable", "Requested capability does not exist in this registry", "fix_environment")
    return items[identity]


def dispatch(args: argparse.Namespace) -> tuple[Any, int]:
    cmd = args.command
    if cmd == "capabilities":
        items = load_registry(args.registry)
        if args.id:
            return _workflow(args.registry, args.id).descriptor, 0
        return {"capabilities": [{"capability": w.descriptor["capability"], "description": w.data["description"],
                                  "lifecycle": w.data["lifecycle"], "process_execution": w.has_process,
                                  "checks": [s["id"] for s in w.data["steps"]]} for w in items.values()]}, 0
    if cmd == "validate-workflow":
        wf = load_workflow(args.path)
        return {"valid": True, "capability": wf.descriptor["capability"], "execution_performed": False}, 0
    if cmd == "snapshot":
        snap = create_snapshot(args.source, args.state, args.repository)
        atomic_json(args.output, snap, exclusive=True)
        return snap, 0
    if cmd == "policy":
        workflows = [_workflow(args.registry, name) for name in args.workflow]
        tools = {}
        for item in args.tool:
            name, sep, path = item.partition("=")
            if not sep or name in tools:
                raise SidecarError("tool_option", "Use one NAME=/path for each tool")
            tools[name] = path
        policy = make_policy(workflows, args.repository, tools, args.allow_trusted_process)
        atomic_json(args.output, policy, exclusive=True)
        return {"policy_digest": canonical_digest(policy), "output": str(args.output),
                "run_authorized": False, "process_execution": policy["allow_trusted_process"]}, 0
    if cmd in {"prepare", "delegate"}:
        if cmd == "delegate" and not args.confirm_authorized:
            raise SidecarError("confirmation_required", "Delegate requires --confirm-authorized under actual existing authority", "authorize")
        if args.output and args.output.exists():
            raise SidecarError("output_exists", "Output exists; choose a new path")
        policy = load_policy(args.policy)
        wf = _workflow(args.registry, args.workflow)
        if args.source:
            snap = create_snapshot(args.source, args.state, args.repository)
        else:
            snap = read_json(args.snapshot)
            verify_snapshot(initialize_state(args.state), snap["snapshot"]["value"])
        request = prepare_request(wf, policy, snap, read_json(args.inputs) if args.inputs else {},
                                  args.objective, args.scope_id, args.decision_ref, args.ttl)
        if cmd == "delegate":
            permit = authorize(request, wf, policy)
            state = initialize_state(args.state)
            atomic_json(state / "requests" / (request["request_id"] + ".request.json"), request, exclusive=True)
            atomic_json(state / "requests" / (request["request_id"] + ".permit.json"), permit, exclusive=True)
            result = run_with_signals(request, wf, policy, permit, state)
            if args.output: atomic_json(args.output, result, exclusive=True)
            return result, status_code(result)
        atomic_json(args.output, request, exclusive=True)
        return {"request_id": request["request_id"], "request_digest": canonical_digest(request),
                "output": str(args.output), "execution_performed": False,
                "checks": [c["id"] for c in request["checks"]]}, 0
    if cmd == "authorize":
        if not args.confirm:
            raise SidecarError("confirmation_required", "Use --confirm only under actual user/host authorization", "authorize")
        request = read_json(args.request); policy = load_policy(args.policy)
        wf = _workflow(args.registry, request["capability"]["id"])
        permit = authorize(request, wf, policy)
        atomic_json(args.output, permit, exclusive=True)
        return {"permit_written": str(args.output), "request_id": request["request_id"],
                "scope": "single-user local caller attestation; not a signed/human-identity credential"}, 0
    if cmd == "run":
        if args.output and args.output.exists():
            raise SidecarError("output_exists", "Result output exists; choose a new path before running")
        request = read_json(args.request); policy = load_policy(args.policy); permit = read_json(args.permit)
        wf = _workflow(args.registry, request["capability"]["id"])
        result = run_with_signals(request, wf, policy, permit, args.state)
        if args.output: atomic_json(args.output, result, exclusive=True)
        return result, status_code(result)
    if cmd == "verify-result":
        request, result = read_json(args.request), read_json(args.result)
        verify_result(request, result, args.run_dir, read_json(args.capability) if args.capability else None)
        return {"valid": True, "artifact_bytes_verified": True, "human_acceptance": False}, 0
    if cmd in {"history", "result"}:
        state = initialize_state(args.state)
        if cmd == "result":
            run_root = contained(state / "runs", args.run_id)
            if not (run_root / "result.json").exists():
                raise SidecarError("no_terminal_result", "Run is active/interrupted; reconcile, do not blindly replay", "reconcile")
            result = read_json(contained(run_root, "result.json"))
            verify_result(read_json(contained(run_root, "request.json")), result, run_root,
                          read_json(contained(run_root, "capability.json")))
            return result, 0
        if not 1 <= args.limit <= 100:
            raise SidecarError("invalid_limit", "History limit must be between 1 and 100")
        paths = sorted((state / "runs").iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
        output = []
        for path in paths[:args.limit]:
            run_root = contained(state / "runs", path.name)
            metadata = read_json(contained(run_root, "state.json"))
            output.append(metadata)
        return {"runs": output, "resume_supported": False, "limits": "No automatic crash recovery or replay"}, 0
    raise SidecarError("unknown_command", "Unknown command")


def status_code(result: dict[str, Any]) -> int:
    return {"succeeded": 0, "failed": 1, "blocked": 2, "escalated": 3,
            "cancelled": 130, "timed_out": 124}[result["status"]]


def run_with_signals(request, workflow, policy, permit, state):
    event = threading.Event()
    originals = {}
    if threading.current_thread() is threading.main_thread():
        for sig in (signal.SIGINT, signal.SIGTERM):
            originals[sig] = signal.signal(sig, lambda *_: event.set())
    try:
        return execute(request, workflow, policy, permit, state, event)
    finally:
        for sig, handler in originals.items():
            signal.signal(sig, handler)


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        output, code = dispatch(args)
    except (SidecarError, OSError, ValueError, KeyError, TypeError, RuntimeError, ImportError) as exc:
        # Do not print raw JSON/request values or subprocess output on errors.
        error = {"error": getattr(exc, "code", "input_or_environment_error"),
                 "message": exc.message if isinstance(exc, SidecarError) else type(exc).__name__,
                 "next_action": getattr(exc, "action", "fix_environment"),
                 "execution_outcome": "No terminal outcome established; inspect state before any replay"}
        print(json.dumps(error, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
