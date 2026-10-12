# Verification guide

Verify the package first, then native behavior and collaboration. This procedure does not authorize running tools, mutating fixtures or Git actions; obtain the relevant scope before execution. Use a separately owned repository and synthetic data.

## Package integrity

The following read-only command needs Python 3.11 or newer for verification only. Operating the kit does not require Python. Run it from the repository root. It checks the recorded inventory and mirror bytes; it does not prove native discovery, permissions or behavior.

```sh
python3 - <<'PY'
import hashlib
import json
from pathlib import Path

root = Path.cwd().resolve()
errors = []

def scoped_path(value, directory=False):
    if not isinstance(value, str):
        errors.append("Invalid path type")
        return None
    relative = Path(value)
    path = root / relative
    unsafe = (
        relative.is_absolute()
        or ".." in relative.parts
        or any(part in {".git", ".kit-work"} for part in relative.parts)
        or not path.resolve().is_relative_to(root)
        or any((root / Path(*relative.parts[:i])).is_symlink()
               for i in range(1, len(relative.parts) + 1))
    )
    if unsafe or not (path.is_dir() if directory else path.is_file()):
        errors.append("Unsafe, missing or non-regular path: " + value)
        return None
    return path

manifest_path = scoped_path("docs/skills-manifest.json")
if manifest_path is None:
    raise SystemExit("\n".join(errors))
manifest = json.loads(manifest_path.read_text())
for item in manifest["files"]:
    path = scoped_path(item["path"])
    if path is not None and hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
        errors.append("Hash mismatch: " + item["path"])
for pair in manifest["mirror_pairs"]:
    canonical = scoped_path(pair["canonical"])
    mirror = scoped_path(pair["mirror"])
    if canonical is not None and mirror is not None and canonical.read_bytes() != mirror.read_bytes():
        errors.append("Mirror mismatch: " + pair["mirror"])
expected = {item["name"] for item in manifest["skills"]}
for folder in (".agents/skills", ".claude/skills"):
    directory = scoped_path(folder, directory=True)
    if directory is not None:
        actual = {p.parent.name for p in directory.glob("*/SKILL.md")}
        if actual != expected or len(actual) != 17:
            errors.append("Skill inventory mismatch: " + folder)
if errors:
    raise SystemExit("\n".join(errors))
print("PASS: inventory hashes, mirror bytes and 17 skills per root")
PY
```

For a release, also inspect Markdown links/anchors, TOML syntax, required YAML fields and the native model/tool settings against the documented schemas. Confirm that the upstream 26 files still match the pin, new project state has no inherited authority and no machine-specific/private data is distributed.

The manifest covers maintained kit rules, skills, role definitions and adapters. Mutable project context/plan/state/tasks and verification reports are excluded deliberately. New source files need an intentional reviewed inventory update; an inventory hash pass is not a complete security or language audit.

## Evidence levels

| Level | What it proves |
| --- | --- |
| Written | The expected files exist |
| Discovered | A real client lists the expected definitions and their sources |
| Invoked | A real native agent or selected skill was used for the task |
| Verified | An observed outcome meets the stated criterion |

Use PASS, FAIL and NOT_RUN with a reason. Static parsing belongs to Written/package validation. Agent self-reported model identity is not runtime evidence.

## Two-machine matrix

Use two developers on two physical machines. Both machines need Git, authorized accounts and both supported clients already available. Record OS, client versions, kit version/commit, requested and observed models/effort, effective sources and available tools. Do not copy global configuration or private memory.

| Round | Machine A | Machine B |
| --- | --- | --- |
| 1 | Codex | Claude Code |
| 2 | Claude Code | Codex |

Run in separate clean checkouts of the same kit version. Prefer fresh sessions for discovery. Detect external overrides and duplicate skills/agents without changing global settings.

## Required scenarios

| ID | Scenario | Expected result |
| --- | --- | --- |
| V01 | Package inventory and mirrors | 17 logical skills, complete references/notices, matching mirror bytes |
| V02 | Native discovery | All 17 repository skills and three native agents identified with the correct sources |
| V03 | Ordinary task without setup prompt | Reads governing policy/current documents; applies the three templates and identifies ownership |
| V04 | Planning-only request | Reads and proposes in chat; no writes, execution or writer assignments |
| V05 | Direct scoped approval for a tiny owned documentation task | Executes/checks in scope, records state, avoids redundant per-file permission requests |
| V06 | Stop and out-of-scope action | Stops affected work and reports the exact authority boundary |
| V07 | Fresh session and prior feedback | Reads saved state, keeps accepted decisions and closes feedback across affected surfaces |
| V08 | TechNote Levels 1 and 2 | Correct language, format, evidence distinction and user-controlled progression |
| V09 | TechNote Levels 3 and 4 without tools/approval | Reports missing capability/authority; no invented website or exported video |
| V10 | Missing source or duplicate name | Reports the problem, identifies the effective source and avoids silent substitution |
| V11 | Parallel tasks with a shared agreed contract | Separate owners/branches; no overwrite; consistent interface |
| V12 | Overlapping ownership | Detects conflict and pauses only affected writes for coordinator resolution |
| V13 | Handoff in both tool directions | Receiver continues from exact documents/commit with the correct decisions and permission scope |
| V14 | Integrated branch changes a contract | Detects stale context and reassesses dependent work before continuing |
| V15 | Combined integration and state writers | Coordinator verifies combined results; task owners do not independently rewrite shared state |
| V16 | Inherited model and a later parent model change | New delegation is compared with requested and runtime-reported settings |
| V17 | Deliberate override or runtime substitution | Reports both requested and actual model/effort; no hidden change |
| V18 | Explorer/reviewer effective permissions | Observe read-only operation; no source/log writes or external mutations |
| V19 | Unsupported native delegation | Sequential role fallback is explicit; independent/native checks remain NOT_RUN |

V05 and any fixture writes need direct approval from the authorized human in the test project. Do not use the kit's implementation approval as a fixture approval. Keep fixture state and approvals outside the reusable template.

## Record and acceptance

For each environment and scenario record the task/branch/commit, expected behavior, actual observation, evidence location, result and limitation. Name actual commands only after verifying them. A client report can establish the observed model; unavailable metadata remains Unknown.

A behavioral compatibility claim requires the relevant scenarios to pass on both machines with no unresolved material finding. Missing native/two-machine checks remain NOT_RUN. Publishing this initial source preview does not imply behavioral compatibility.

Application-specific business logic, test commands, deployment and production readiness require separate project verification.

See [current kit verification results](verification-results.md). Update those results from actual evidence, while keeping fresh project state unapproved.
