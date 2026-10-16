# TASK-006 — Four boundaries for feature work and verification infrastructure

## Assignment and authority

- Plan: KIT-HARNESS-BOUNDARIES-001 v1, approved in the current chat on 2026-10-16.
- Direct human approval: Khiêm wrote “Approved. Áp dụng bốn ranh giới này vào Agent Kit và sửa đồng bộ sáu skill cùng bản Claude. Không sửa Pinky Lamb, không mở harness mới, chưa commit/push. Báo rõ đã sửa gì và phần nào chưa kiểm chứng.”
- Task Owner: this Codex desktop main session; sequential implementation and self-review. No subagent or independent reviewer is assigned.
- Branch / base HEAD: `main` / `919ce6b8d84c8ac5ad4ce473ad6e6c2c9973d2ac`. Initial worktree and index: clean.
- Covered actions: the instruction/document changes below and local source/package consistency checks. Latest restrictions: no Pinky Lamb changes or execution, new harness, commit/push, global configuration, dependencies, application/native/fixture runs or external publication.
- Shared project context/plan/state remain fresh templates. This maintenance assignment grants no project-wide Coordinator ownership.
- Model: inherit the developer selection; no override. Runtime-observed model/effort: Unknown.
- Work state: complete for the approved instruction/package-maintenance scope; local checks PASS with the validator prerequisite limitation below. Native behavior and human acceptance are not claimed. Changes remain uncommitted.

## Exact file ownership

Canonical entrypoints and their byte-identical `.claude/skills/` copies (12 files):

1. `.agents/skills/debugging-and-error-recovery/SKILL.md`
2. `.agents/skills/test-driven-development/SKILL.md`
3. `.agents/skills/code-review-and-quality/SKILL.md`
4. `.agents/skills/code-simplification/SKILL.md`
5. `.agents/skills/context-engineering/SKILL.md`
6. `.agents/skills/spec-driven-development/SKILL.md`

Supporting policy, packaging and evidence records (9 files):

7. `docs/team-policy.md`
8. `docs/team-workflow.md`
9. `docs/agent-coordination-templates.md`
10. `CONTRIBUTING.md`
11. `docs/skills-catalog.md`
12. `docs/skills-manifest.json`
13. `docs/verification-guide.md`
14. `docs/verification-results.md`
15. `docs/tasks/TASK-006.md`

## Accepted change and acceptance criteria

1. Feature approval permits business code and regression tests using the existing runner; verification-framework/selector/admission/receipt/orchestration implementation needs its own directly approved task.
2. When a harness cannot start or collect results, stop the attempt and report its error and missing criterion. Do not repair, replace or replay it under feature approval. Continue independent authorized code work. A failing business assertion still requires product repair; required unproved criteria remain open.
3. Source changes lead to affected-diff review and rechecks of invalidated evidence, not a new generation, namespace or review chain solely because a review receipt is stale. Preserve historical evidence and real integrity checks.
4. Application startup and requests retain environment, authenticated actor, authorization, ownership, data protection and necessary integrity checks; agent/session/model/effort/coordination receipts are not operating conditions.
5. The six skills no longer impose universal full-suite runs per implementation/refactor step, reviewer mutation edits, session/task-based evidence invalidation or per-phase human reapproval within valid scope. Initial and material-change approvals remain.
6. Preserve skill inventory/frontmatter, upstream pin/original origins/license, template-application guidance, native adapters, other skills, shared project templates and historical reports/tasks. Mark five newly adapted upstream files and the further review adaptation; maintain matching mirrors and valid manifest hashes.
7. Finish through source review and existing local package checks only. No new harness or native behavior claim is part of this task.

## Work and verification

Selected workflows: using-agent-skills, TechNote, skill-creator, documentation-and-adrs and code-review-and-quality. Git-workflow is used only for read-only status/diff checks. Repository instructions remain in English; user-facing reports are in Vietnamese as requested.

Planned checks: final diff and four-boundary source review; published package-integrity recipe; existing skill metadata validator if its dependencies are available, otherwise report the prerequisite and use available equivalent structural checks; affected local links/anchors; scope/history/provenance preservation; `git diff --check` and final read-only HEAD/index/worktree checks. Recheck only evidence invalidated by an actual subsequent correction.

No task-specific runner, fixture, selector, admission or receipt will be added. Native discovery, model/permission behavior, two-machine compatibility, application behavior and independent native review remain NOT_RUN. Static checks cannot prove agent compliance or repair another project.

### Actual checks and source review

| Check | Actual result | What it proves / limits |
| --- | --- | --- |
| Published integrity recipe extracted from `docs/verification-guide.md` and executed with inline `python3` | PASS for initial source set | Inventory hashes, mirror bytes/provenance, 17 skills per root, 15 original and 11 adapted upstream files. A later template wording correction changes its hash; final package recheck follows |
| `PYTHONDONTWRITEBYTECODE=1 python3` dependency preflight for the bundled `quick_validate.py` | NOT_RUN: validator prerequisite unavailable | PyYAML is absent. The validator was not invoked, no dependency was installed and no retry was made |
| Existing `ruby -rpsych` inline metadata checks | PASS | All 12 changed entrypoints: YAML dictionary/allowed fields, matching names, valid name/description shape and no unfinished scaffold outside fenced examples. This is separate structural evidence, not a PASS from quick_validate.py |
| `git diff --check` | PASS for initial source set | No whitespace error at that point; final evidence records will be checked at handoff |

Sequential self-review inspected the changed policy, six canonical skill diffs and supporting guidance against the four cases in the verification guide. Business tests use the existing runner; unavailable harnesses cannot be repaired/replaced/replayed under feature approval; stale receipts do not create successor generations; startup/request checks keep coordination metadata separate from authenticated actor and protection checks. The review also checked that failed business assertions and required unproved criteria remain open, and that routine product repair/initial approval/material-change rules remain present. Reviewer mutation and unconditional full-suite/per-phase instructions were replaced at their actual call sites, including checklist examples. A small wording correction clarified affected evidence invalidation in the assignment template. No independent agent or native behavior ran.

### Final local result

- PASS: the published integrity recipe, rechecked after the template wording/digest correction, validates 81 inventory entries, 28 mirror pairs, 17 skills per root, and 15 original / 11 adapted upstream files. The unchanged skill-metadata result remains valid; no validator retry occurred.
- PASS: inline `python3` scope/history/provenance/link inspection confirms exactly the 21 owned files changed, 72 other tracked files byte-identical to base, original origin metadata/pin/license/inventory retained, five newly adapted canonical files, six skill frontmatters unchanged and the historical verification-report prefix preserved.
- PASS: 69 local links/anchors across all 20 changed Markdown files resolve. External URLs were not fetched. Final evidence text adds no link target or source instruction and does not invalidate package/metadata evidence.
- PASS: `git diff --check` after the template and report changes. The new task's `git diff --no-index --check -- /dev/null docs/tasks/TASK-006.md` produced no whitespace diagnostics; exit 1 denotes the added-file difference. Final handoff checks tracked whitespace and this task's lines after the record update.
- NOT_RUN: quick_validate.py (PyYAML absent), native discovery/compliance, effective model/permissions, application/runtime behavior, independent native review and two-machine compatibility. No claim of measured time/token savings or Pinky Lamb recovery is made.
- Delivery boundary: HEAD remains the base above, index empty, no Git write/commit/push or new runner/fixture/script. No Pinky Lamb command or change occurred during this implementation task. Native adapters, model routing, other skills, shared project templates and previous task records remain unchanged.

The coordinator checklist was applied sequentially to this maintenance assignment: verified human approval/restrictions, exact ownership and acceptance; inspected source/evidence and closed conflicting clauses across the six skills/mirrors; preserved prior work and recorded the final result/limits here. This does not claim independent review, runtime behavior or project-wide Coordinator authority.

## Feedback and next action

The four approved boundaries and their conflicting skill clauses are now corrected within this scope. The earlier general plan was rejected; it is not the authority for this work. No required source correction remains from this self-review. Next option: review/accept the current diff for the instruction/package scope. Commit/push, native behavioral verification and repairs in an adopting project each require their own explicit scope; none is started by this handoff.
