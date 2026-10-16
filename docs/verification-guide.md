# Verification guide

This guide checks the kit package and records evidence. [Team workflow](team-workflow.md) owns product testing/review/acceptance. An instruction edit does not require a native behavioral campaign, new runner, fixture or harness.

## Package integrity

For package changes, review the intended diff, update explained source/mirror hashes, then use the existing read-only recipe below from the repository root with Python 3.11+. Python is a verification tool, not a requirement to operate the kit. This validates inventory/mirrors/provenance, not client behavior.

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
inventory = {item['path']: item for item in manifest['files']}
for item in manifest["files"]:
    path = scoped_path(item["path"])
    if path is not None and hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
        errors.append("Hash mismatch: " + item["path"])
    origin = item.get('origin', {})
    if path is not None and origin.get('repository') == manifest['upstream']['repository']:
        if origin.get('commit') != manifest['upstream']['commit']:
            errors.append('Upstream pin mismatch: ' + item['path'])
        adaptation = item.get('adaptation')
        if adaptation is None:
            data = path.read_bytes()
            blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            if blob != origin.get('git_blob_sha'):
                errors.append('Unmarked upstream change: ' + item['path'])
        elif not isinstance(adaptation, dict) or not adaptation.get('source') or not adaptation.get('reason'):
            errors.append('Invalid adaptation metadata: ' + item['path'])
        else:
            scoped_path(adaptation.get('record'))
canonical_upstream = [item for item in manifest['files']
                      if item['path'].startswith('.agents/')
                      and item.get('origin', {}).get('repository') == manifest['upstream']['repository']]
adapted = sum(item.get('adaptation') is not None for item in canonical_upstream)
if (len(canonical_upstream) != manifest['upstream']['file_count']
        or adapted != manifest['upstream']['adapted_file_count']
        or len(canonical_upstream) - adapted != manifest['upstream']['unchanged_file_count']):
    errors.append('Upstream adaptation counts mismatch')
for pair in manifest["mirror_pairs"]:
    canonical = scoped_path(pair["canonical"])
    mirror = scoped_path(pair["mirror"])
    if canonical is not None and mirror is not None and canonical.read_bytes() != mirror.read_bytes():
        errors.append("Mirror mismatch: " + pair["mirror"])
    if canonical is not None and hashlib.sha256(canonical.read_bytes()).hexdigest() != pair.get('sha256'):
        errors.append("Mirror pair hash mismatch: " + pair["canonical"])
    canonical_item = inventory.get(pair['canonical'], {})
    mirror_item = inventory.get(pair['mirror'], {})
    if (canonical_item.get('origin') != mirror_item.get('origin')
            or canonical_item.get('adaptation') != mirror_item.get('adaptation')):
        errors.append('Mirror provenance mismatch: ' + pair['mirror'])
expected = {item["name"] for item in manifest["skills"]}
for folder in (".agents/skills", ".claude/skills"):
    directory = scoped_path(folder, directory=True)
    if directory is not None:
        actual = {p.parent.name for p in directory.glob("*/SKILL.md")}
        if actual != expected or len(actual) != 17:
            errors.append("Skill inventory mismatch: " + folder)
if errors:
    raise SystemExit("\n".join(errors))
print("PASS: inventory hashes, mirror bytes, 17 skills per root; "
      + str(len(canonical_upstream) - adapted) + " original / " + str(adapted) + " adapted upstream files")
PY
```

Also check affected local links/anchors and changed metadata using available tools. Preserve upstream pin/original origins/license, native schema/model/permission intent and fresh project authority. Do not install missing tools merely to complete a checklist. Equivalent structural evidence must be reported separately from an unavailable validator.

The manifest contains maintained rules/skills/roles/adapters. Mutable project/task/evidence records are excluded. New maintained sources need an intentional inventory update; hashes are not a security or language audit. Recheck only evidence invalidated by actual later changes.

## Evidence levels

- Written: source files exist.
- Discovered: an actual client identifies the definitions and effective sources.
- Invoked: the actual selected skill/native agent is used for the stated task.
- Verified: observed behavior meets its stated criterion.

Use PASS, FAIL and applicable NOT_RUN with reasons. A check that does not apply is not a failed/unrun mandatory gate. Parsing and model self-report do not prove effective runtime behavior.

## Source review for workflow changes

Inspect actual instructions and their callers/entrypoints. Confirm that one owner can proceed through implementation with focused tests, review/CI targets coherent completed changes, and acceptance targets usable flows. Check that routine repairs do not add approval/documents or per-edit review gates.

Consider these concrete cases without executing a behavioral harness:

- A small approved fix: the owner implements/tests directly, without a separate spec/checkpoint/reviewer per file.
- Tests/config broken by that fix: the same developer diagnoses/repairs within scope.
- Shared runner failure independent of the feature: a maintenance owner is named, dependent proof stays blocked and independent code work continues.
- Review waits or a command fails unchanged: continue independent authorized work or hand off the blocker; do not invent verification/orchestration to fill the wait.
- Source/session/stage changes: retain valid checks/reviews and recheck affected inputs/findings only.
- Material missing decision, unsafe dependency or release/data authority missing: pause the affected work and request the needed decision. A direct human stop always applies.
- Source-only self-test handoff: code/callers must be complete; tests/runtime remain NOT_RUN and acceptance/release are not inferred.
- Approved-template flow: preserve its fidelity criteria, use relevant rendered evidence at usable-flow milestones and no Coordinator gate per edit.

These questions are content review, not native behavioral PASS. Do not turn them into another required fixture/runner chain.

## Two-machine matrix

Only a separately authorized compatibility task uses actual installed clients/machines. Record client/OS/kit revision, effective sources, supported tools and observed model/permissions. Observe discovery, one bounded task/handoff and required authority/stop behavior using existing capabilities and synthetic data. Do not change global settings or import another project's approvals/data.

## Required scenarios

There is no universal V01-V31 runlist for every edit. Older scenario numbers in historical task/results records describe the previous workflow. Select actual cases for the current behavioral claim and task authority; excluded/unavailable runs stay NOT_RUN. Do not restart old campaigns to complete source maintenance.

## Recovery and approval scenarios

Historical A-G scenario references remain evidence of earlier maintenance only. Current repair, stop and decision behavior is defined by [failure handling](team-workflow.md#failures-and-blockers) and [policy](team-policy.md#approval-and-autonomy), not a successor generation or review ledger. Do not rewrite past approvals or their recorded results.

## Record and acceptance

Record source revision, actual command/observation, result and limits in the same authorized task. Source/package checks support instruction consistency, not runtime compliance, token/time improvement, an adopting project's recovery or human acceptance. Keep historical observations and mark the current outcome clearly.
