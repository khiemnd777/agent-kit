"""Bounded builtin and opt-in trusted-process executors.

A private copy is not a sandbox. Only reviewed trusted code may use process mode.
No inherited credentials, implicit shell, source writes or LLM integration.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import threading
import time
import tomllib
from typing import Any

from .io import SidecarError, contained, digest_bytes, read_bytes, read_json, now
from .snapshots import MAX_FILE, _files, private_copy


class Interrupted(Exception):
    def __init__(self, status: str) -> None:
        super().__init__(status)
        self.status = status


@dataclass
class Control:
    cancelled: threading.Event
    deadline: float

    def check(self, step_deadline: float | None = None) -> None:
        if self.cancelled.is_set():
            raise Interrupted("cancelled")
        if time.monotonic() >= min(self.deadline, step_deadline or self.deadline):
            raise Interrupted("timed_out")


@dataclass
class Outcome:
    check_status: str = "NOT_RUN"
    detail: str = "Not started"
    terminal: str | None = None
    action: str = "reason"
    effects_unknown: bool = False
    attempts: int = 0
    log: bytes = b""
    truncated: bool = False
    payload: Any = None
    receipts: list[dict[str, Any]] = field(default_factory=list)


def _inventory(source: Path, inputs: dict[str, Any], control: Control,
               deadline: float) -> tuple[bool, dict[str, Any]]:
    records, missing, seen = [], [], set()
    for rel in inputs.get("include", ["."]):
        control.check(deadline)
        try:
            path = contained(source, rel, allow_dot=True)
        except FileNotFoundError:
            missing.append(rel); continue
        files = _files(path, filtering=False)[0] if path.is_dir() else [path]
        for file in files:
            control.check(deadline)
            name = file.relative_to(source).as_posix()
            if name in seen: continue
            seen.add(name)
            data = read_bytes(file, MAX_FILE)
            records.append({"path": name, "size_bytes": len(data), "digest": digest_bytes(data)})
    return not missing, {"files": sorted(records, key=lambda x: x["path"]), "missing": missing,
                         "count": len(records), "byte_count": sum(r["size_bytes"] for r in records)}


def _entrypoints(source: Path, _: dict[str, Any], control: Control,
                 deadline: float) -> tuple[bool, dict[str, Any]]:
    found = []
    for filename in ("package.json", "pyproject.toml"):
        control.check(deadline)
        if not (source / filename).exists(): continue
        path = contained(source, filename)
        if filename.endswith(".json"):
            doc = read_json(path)
            scripts = doc.get("scripts", {}) if isinstance(doc, dict) else None
        else:
            doc = tomllib.loads(read_bytes(path).decode("utf-8"))
            scripts = doc.get("project", {}).get("scripts", {})
        if not isinstance(scripts, dict) or any(not isinstance(v, str) for v in scripts.values()):
            return False, {"invalid_manifest": filename}
        found.append({"source": filename, "declared_scripts": scripts})
    return True, {"manifests": found, "commands_executed": False,
                  "note": "Only explicitly declared scripts are reported; commands are never inferred."}


def _manifest(source: Path, _: dict[str, Any], control: Control,
              deadline: float) -> tuple[bool, dict[str, Any]]:
    path = contained(source, "docs/package-manifest.json")
    manifest = read_json(path)
    if not isinstance(manifest, dict) or not isinstance(manifest.get("files"), dict) or not manifest["files"]:
        return False, {"reason": "Expected Agent Kit V2 file-hash manifest"}
    mismatches = []; count = 0
    for rel, digest in manifest["files"].items():
        control.check(deadline)
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            return False, {"reason": "Invalid manifest digest"}
        try:
            actual = digest_bytes(read_bytes(contained(source, rel), MAX_FILE)).split(":")[1]
            if actual != digest: mismatches.append(rel)
        except FileNotFoundError:
            mismatches.append(rel)
        count += 1
    return not mismatches, {"checked": count, "mismatches": mismatches,
                            "scope": "Declared file hashes only; not acceptance, full verification or authentication"}


def _mirrors(source: Path, _: dict[str, Any], control: Control,
             deadline: float) -> tuple[bool, dict[str, Any]]:
    canonical = contained(source, ".agents/skills")
    mirrors = contained(source, ".claude/skills")
    left = _files(canonical, filtering=False)[0]; right = _files(mirrors, filtering=False)[0]
    lnames = {p.relative_to(canonical).as_posix() for p in left}
    rnames = {p.relative_to(mirrors).as_posix() for p in right}
    mismatches = sorted(lnames ^ rnames)
    if not lnames:
        return False, {"reason": "Canonical skill inventory is empty"}
    for rel in sorted(lnames & rnames):
        control.check(deadline)
        if read_bytes(contained(canonical, rel), MAX_FILE) != read_bytes(contained(mirrors, rel), MAX_FILE):
            mismatches.append(rel)
    return not mismatches, {"files_compared": len(lnames & rnames), "mismatches": mismatches,
                            "scope": "Byte equality only, not native skill discovery"}


def _json_files(source: Path, inputs: dict[str, Any], control: Control,
                deadline: float) -> tuple[bool, dict[str, Any]]:
    paths = inputs.get("paths", [])
    if not paths:
        return False, {"reason": "No JSON paths requested"}
    invalid = []
    for rel in paths:
        control.check(deadline)
        try:
            read_json(contained(source, rel))
        except (FileNotFoundError, SidecarError) as exc:
            invalid.append({"path": rel, "code": getattr(exc, "code", "missing_file")})
    return not invalid, {"checked": len(paths), "invalid": invalid}


OPERATIONS = {"inventory": _inventory, "entrypoints": _entrypoints,
              "manifest": _manifest, "mirrors": _mirrors, "json-files": _json_files}


def builtin(step: dict[str, Any], source: Path, inputs: dict[str, Any],
            control: Control) -> Outcome:
    start = time.monotonic(); deadline = start + step["timeout_seconds"]
    try:
        control.check(deadline)
        passed, payload = OPERATIONS[step["operation"]](source, inputs, control, deadline)
        control.check(deadline)
        return Outcome("PASS" if passed else "FAIL",
                       "Builtin check passed" if passed else "Builtin assertion failed",
                       None if passed else "failed", attempts=1, payload=payload,
                       receipts=[{"executor": "builtin", "duration_seconds": time.monotonic()-start}])
    except Interrupted as exc:
        return Outcome(detail="Builtin interrupted", terminal=exc.status, attempts=1)
    except FileNotFoundError:
        return Outcome(detail="Required source input is absent", terminal="blocked", action="fix_environment", attempts=1)
    except (SidecarError, ValueError, UnicodeError, tomllib.TOMLDecodeError) as exc:
        return Outcome(detail="Builtin could not interpret its bounded input: " + getattr(exc, "code", type(exc).__name__),
                       terminal="escalated", action="reason", attempts=1)


def expand(value: str, inputs: dict[str, Any], source: Path, scratch: Path) -> str:
    if value == "{{source}}": return str(source)
    if value == "{{scratch}}": return str(scratch)
    match = re.fullmatch(r"\{\{inputs\.([A-Za-z][A-Za-z0-9_]*)\}\}", value)
    if match:
        item = inputs.get(match.group(1))
        if not isinstance(item, (str, int, bool)):
            raise SidecarError("template_input", "Template input must be a scalar")
        return str(item)
    if "{{" in value or "}}" in value:
        raise SidecarError("template_syntax", "Only whole argv/env-value templates are supported")
    if "\0" in value:
        raise SidecarError("nul_argument", "NUL is not permitted in arguments")
    return value


def _kill_group(proc: subprocess.Popen[bytes]) -> None:
    try: os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError: pass
    try: proc.wait(timeout=0.3)
    except subprocess.TimeoutExpired: pass
    # Kill the group even if its original leader exited; children may hold stdout open.
    try: os.killpg(proc.pid, signal.SIGKILL)
    except ProcessLookupError: pass
    try: proc.wait(timeout=1)
    except subprocess.TimeoutExpired: pass


def process(step: dict[str, Any], source: Path, scratch: Path, inputs: dict[str, Any],
            policy: dict[str, Any], control: Control, max_attempts: int, log_limit: int) -> Outcome:
    outcome = Outcome()
    start = time.monotonic(); deadline = start + step["timeout_seconds"]
    all_log = bytearray()
    try:
        work = private_copy(source, scratch / "work")
        home = scratch / "home"; home.mkdir(mode=0o700)
        temp = scratch / "tmp"; temp.mkdir(mode=0o700)
        cwd = contained(work, step.get("cwd", "."), allow_dot=True)
        if not cwd.is_dir():
            raise SidecarError("invalid_cwd", "Working directory is not a directory")
        command = step["argv"]
        executable = policy["tools"][command[0]]["path"]
        argv = [executable] + [expand(v, inputs, work, scratch) for v in command[1:]]
        env = {"PATH": os.defpath, "HOME": str(home), "TMPDIR": str(temp), "TMP": str(temp),
               "TEMP": str(temp), "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC",
               "PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1",
               "GIT_TERMINAL_PROMPT": "0", "CI": "true"}
        env.update({k: expand(v, inputs, work, scratch) for k, v in step.get("env", {}).items()})
        for attempt in range(1, max_attempts + 1):
            control.check(deadline)
            attempt_start = time.monotonic()
            attempt_started_at = now()
            overflow = threading.Event()
            proc = subprocess.Popen(argv, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    start_new_session=True, close_fds=True, bufsize=0)
            outcome.attempts = attempt
            assert proc.stdout is not None

            def drain() -> None:
                try:
                    while True:
                        chunk = proc.stdout.read(8192)
                        if not chunk: break
                        remaining = max(0, log_limit - len(all_log))
                        all_log.extend(chunk[:remaining])
                        if len(chunk) > remaining:
                            overflow.set()
                except (OSError, ValueError):
                    pass

            reader = threading.Thread(target=drain, name="sidecar-output", daemon=True)
            reader.start()
            interruption: str | None = None
            try:
                while proc.poll() is None:
                    control.check(deadline)
                    if overflow.is_set():
                        interruption = "output_limit"; break
                    time.sleep(0.01)
            except Interrupted as exc:
                interruption = exc.status
            finally:
                if interruption:
                    _kill_group(proc)
                else:
                    # Do not let background descendants outlive a successful parent.
                    try:
                        os.killpg(proc.pid, 0)
                        interruption = "background_children"
                        _kill_group(proc)
                    except ProcessLookupError:
                        pass
                reader.join(timeout=1)
                if reader.is_alive():
                    interruption = interruption or "unsettled_output"
                    _kill_group(proc)
                    # A malicious process that escapes its group is outside this trusted-host model.
                else:
                    proc.stdout.close()
            code = proc.poll()
            outcome.receipts.append({"attempt": attempt, "exit_code": code,
                                     "duration_seconds": time.monotonic() - attempt_start,
                                     "started_at": attempt_started_at, "finished_at": now(),
                                     "interruption": interruption})
            outcome.log = bytes(all_log)
            outcome.truncated = overflow.is_set()
            if interruption or overflow.is_set():
                reason = interruption or "output_limit"
                outcome.terminal = reason if reason in {"cancelled", "timed_out"} else "escalated"
                outcome.detail = "Process interrupted: " + reason
                outcome.effects_unknown = True
                outcome.action = "reconcile"
                return outcome
            control.check(deadline)
            if code is not None and code < 0:
                outcome.terminal = "escalated"
                outcome.detail = "Process was terminated by a signal; effects require reconciliation"
                outcome.effects_unknown = True
                outcome.action = "reconcile"
                return outcome
            if code == 0:
                outcome.check_status = "PASS"; outcome.detail = "Process completed with exit code 0"
                return outcome
            outcome.check_status = "FAIL"
            outcome.detail = "Process assertion failed with exit code " + str(code)
            outcome.terminal = "failed"
            if code not in step.get("retry_exit_codes", []) or attempt >= max_attempts:
                return outcome
            # Only explicitly enumerated transient exit codes on reviewed safe replay workflows.
            until = time.monotonic() + step.get("retry_delay_seconds", 0.1)
            while time.monotonic() < until:
                control.check(deadline); time.sleep(0.01)
            outcome.check_status = "NOT_RUN"; outcome.terminal = None
        return outcome
    except Interrupted as exc:
        outcome.terminal = exc.status
        outcome.check_status = "NOT_RUN"
        outcome.detail = "Execution stopped at its deadline/cancellation boundary"
        outcome.effects_unknown = outcome.attempts > 0
        outcome.action = "reconcile" if outcome.effects_unknown else "reason"
        outcome.log = bytes(all_log)
        return outcome
    except (OSError, SidecarError) as exc:
        outcome.terminal = "blocked" if outcome.attempts == 0 else "escalated"
        outcome.detail = "Process prerequisite failed: " + getattr(exc, "code", type(exc).__name__)
        outcome.action = "fix_environment" if outcome.attempts == 0 else "reconcile"
        outcome.effects_unknown = outcome.attempts > 0
        outcome.log = bytes(all_log)
        return outcome
