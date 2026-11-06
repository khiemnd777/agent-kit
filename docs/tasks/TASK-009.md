# TASK-009 — source location in debugging

## Authority and scope

On 2026-11-06 Khiêm approved DL01–DL04 in the current chat: supplement debugging-and-error-recovery in the original Agent Kit, keep scope narrow, do not create fast-triage, do not commit/push. This record is kit maintenance, not adoption authority. No worktree, subagent or application change.

## WHAT

| Name | Purpose | Location | Status | Reason if undone/ignored |
| --- | --- | --- | --- | --- |
| DL01 | Add bounded source-location guidance, preserve trigger and cause distinction | Canonical debugging SKILL.md and Claude mirror | done | — |
| DL02 | Synchronize package provenance and hashes | docs/skills-provenance.md; docs/skills-manifest.json | done | — |
| DL03 | Verify package, mirror, links and source boundaries | Existing docs/verification-guide.md recipe; scoped diff | done | — |
| DL04 | Record authority, evidence and actual skill contributions | This task; task index; project-state maintenance pointer; skill journal | done | — |
| DL05 | Separate fast-triage skill | Skill roots | ignored | User explicitly rejected this option |
| DL06 | Expand routing or install elsewhere | Catalog, adopters, global skills | ignored | Outside approved narrow scope |
| DL07 | Publication, runtime pilot or application change | Git remote/runtime/application | ignored | No commit/push or other execution authorized |

## Verification and limits

PASS: existing package-integrity recipe (17 skills/root, mirror bytes, hashes/provenance; 3 original / 23 adapted upstream files); scoped diff whitespace; unchanged frontmatter and pre-existing skill body; affected local file links; source review for Noah-specific rules and scope. No harness or dependency installation.

Unavailable: host skill-creator quick_validate.py exited 1 because Python lacks yaml. Equivalent structural evidence above passed; this is not a PASS of that validator. It is optional here, not an outstanding required package gate.

The adopting-project state remains an uninitialized template; only a kit-maintenance pointer was added. Actual contribution record: [implementation journal](../engineering/skill-usage/records/TASK-009/source-location-implementation-1.json). Source review is delivery-owner self-review, not independent review. Native discovery/invocation and measured speed/token improvements NOT_RUN; human implementation acceptance PENDING_REVIEW.

## Scoped publication — 2026-11-06

Khiêm explicitly requested commit/push of DL01–DL04 and related records only in the original agent-kit. This supersedes the earlier no-publication restriction only for this scope; no application, native pilot or unrelated edits. Human implementation acceptance remains PENDING_REVIEW; publication authorization is not acceptance.

Allowlist: canonical/mirror debugging skill, manifest/provenance, task index, TASK-009, project-state maintenance pointer and TASK-009 journal. Before publication, fetched main/origin/main divergence 0/0. Full existing package recipe and diff whitespace PASS. Content publication VERIFIED: commit 34973ea (8 allowlisted files), push exit 0; post-push main/origin/main divergence 0/0. No unrelated changes included. Receipt metadata is committed/pushed separately after this result; it does not claim its own commit hash.

| Name | Purpose | Location | Status | Reason if undone/ignored |
| --- | --- | --- | --- | --- |
| DP01 | Publish DL01–DL04 and related records | main → origin/main, content 34973ea | done | — |
| DP02 | Record result and publication skill use | TASK-009/state/publication journal | done | — |
| DP03 | Unrelated changes/runtime/deployment | Other source/runtime | ignored | Outside authorization |
