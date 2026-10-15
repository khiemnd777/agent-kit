# TASK-005 — Approved template application workflow

## Assignment and authority

- Task: KIT-TEMPLATE-APPLICATION-001 v1. Direct human approval: Khiêm's “Approved KIT-TEMPLATE-APPLICATION-001 v1” instruction in the current chat on 2026-10-15.
- Developer owner: Khiêm. Task Owner and sole writer: this Codex desktop main session. Work and review are sequential; no independent native reviewer is assigned.
- Branch / source base HEAD: `main` / `8fedcd0b08b256b08e50cfbcd12b3ccc80ed267c`. Initial worktree and index were clean.
- Goal: make approved-template application preserve agreed structure, hierarchy, interaction and responsive behavior, with a representative rendered screen before dependent expansion.
- Scope: team workflow and coordination templates; four named canonical skills and matching Claude copies; one new byte-identical reference pair; shared acceptance checklist; needed catalog, manifest and verification guidance/results; this task record.
- Latest restriction: no Pinky Lamb or other application changes/execution, CMS environment, new skill or harness, native agent/model/permission changes, global configuration, commit/push, publication or deployment. No later stop instruction was received.
- Model routing: inherit developer selection; no override. Runtime-observed model and effort: Unknown.
- Shared project context, plan and state remain unassigned templates. This task does not grant project-wide coordinator ownership.

## Accepted approach and criteria

1. Trigger this guidance only for a task applying a user-supplied or internal template that the human approved. Distinguish an external design reference used as selection evidence.
2. Before broad implementation, record template source/version/hash, retained structure, removed prototype material, approved differences, representative screen and observable criteria, plus runtime/login/data/tool/permission prerequisites. Report unavailable prerequisites early; do not invent data or change access.
3. Complete and connect one representative screen to real controller/data, compare rendered desktop/mobile views at matched viewports, and exercise primary interactions and applicable states. Coordinator records evidence against criteria before dependent expansion; no per-step human approval is added within valid scope.
4. Use the shared checklist with criterion, screen, role, data state, viewport, expected result, evidence, PASS/FAIL/NOT_RUN and owner. Cover structure, order, controls, focus, responsive behavior, preview identity, clipping/occlusion and relevant states. Page-level no-overflow alone cannot prove controls are visible or reachable.
5. Keep Code integrated, verified behavior/UI and human accepted separate. `CODE_COMPLETE_UNTESTED` is limited to a human-requested source handoff for self-testing and cannot close a verified-template objective.
6. Preserve 17 skills, existing approval and permission rules, historical verification results and upstream provenance. Run package/content checks only; source walkthrough is not native behavioral PASS.

## Planned checks and handoff

- Run the published package integrity recipe for inventory hashes, mirror bytes, skill count and provenance; parse metadata and resolve local links; inspect source diff and protected-file scope; run `git diff --check`.
- Review the four counterexamples from the approval against the actual instruction text. Record source-review conclusions separately from native or rendered behavior.
- Record final changed files, actual check results, limits, source base HEAD, diff/patch reference and necessary checksums here. Handoff to Khiêm for review of the uncommitted package changes.

## Actual verification and source review

| Check | Result | Evidence and limit |
| --- | --- | --- |
| Published package-integrity recipe, extracted from `docs/verification-guide.md` and run with `python3` | PASS | 81 inventory hashes, 28 mirror byte/hash pairs, 17 skills per root; 20 original and six adapted upstream canonical files. The recipe also checks each recorded pair hash. |
| Ruby/Psych frontmatter parse and Python JSON parse | PASS | 34 skill entrypoints have required name/description fields; manifest syntax valid. This is metadata inspection, not native discovery. |
| Local Markdown links/anchors | PASS | 56 local links/anchors in 17 changed Markdown files resolved. External URLs were not fetched. |
| Provenance and protected project state | PASS | Original upstream origin metadata retained; fresh `project-context.md`, `project-plan.md` and `project-state.md` byte-identical to source base HEAD. |
| Scope and whitespace | PASS | Exactly 18 approved files changed or added. `git diff --check` and new-file trailing-whitespace scan returned no issue. Index remains empty. |
| Native/runtime/rendered UI behavior | NOT_RUN | Documentation/package task; no application or CMS environment was run and no native agent behavior was exercised. |
| Independent review or human product acceptance | NOT_RUN | Sequential main-session source self-review only; no independent native reviewer or product acceptance claimed. |

The source review tested the four specified counterexamples against the written guidance:

| Counterexample | Written instruction result | Behavioral result |
| --- | --- | --- |
| Colors/components match, but tabs or action order differ | Structure/hierarchy and workflow-order checklist rows cannot PASS; review skill names this failure. | NOT_RUN |
| Build PASS without rendered UI | Build supports Code integrated only; representative rendered desktop/mobile rows stay NOT_RUN. | NOT_RUN |
| Empty screen without populated-data evidence | Populated-data structure and control rows stay NOT_RUN; an empty state cannot substitute. | NOT_RUN |
| Page has no overflow but a nested button is clipped | Container-level clipping, visibility and focus/reachability rows cannot PASS. | NOT_RUN |

The manifest's two existing mirror-pair checksum fields for `definition-of-done.md` and `using-agent-skills/SKILL.md` were stale at source base HEAD while their file inventory hashes were correct. They were refreshed, and the existing published recipe now verifies every mirror-pair checksum. No source content for those files changed.

## Retro cross-check — 2026-10-15

Read-only comparison with the retro turn in Codex thread `01a13b73-294b-7461-bd95-4de864be7f09` confirmed the Kit/Pinky Lamb split. The existing Kit edits already covered template identity, representative rendered verification, evidence levels and nested clipping. General gaps remained: the retro called for an explicit template-element-to-target-position/behavior/evidence map; applicable state checks for navigation continuity, selection, unsaved changes, disabled/busy controls and preview source identity; and separate evidence for each screen or content group after expansion. The reference, workflow and checklist now state these checks without importing CMS-specific names, counts, ports, data or approvals. Data-changing actions outside the adopting task's authority remain NOT_RUN.

The retro's CMS layout, content groups, actions, roles, retained data and adoption steps remain project-specific and are not implemented by this Kit package. This comparison was source self-review, not a replay of that application or a native behavior check. It remained within the approved v1 maintenance scope and changed no additional file paths.

## Current state and handoff

- State: locally verified for the approved documentation/package scope. The 18-file diff remains uncommitted and unstaged on `main` at source base HEAD `8fedcd0b08b256b08e50cfbcd12b3ccc80ed267c`.
- Changed scope: four canonical skills and four Claude mirrors; two new reference mirrors; workflow, coordination templates, shared checklist, catalog, manifest, verification guide/results and this task record.
- Core SHA-256: `.agents/references/template-application.md` and its Claude mirror `417c2f9ac2d50407e2ce438abe05ccf0730f10f27e8a0b59489b7d4ac8035b6c`; `docs/template-application-acceptance.md` `e11d640c7b9150120c10098d7c97f18a2d055b0d8ff9f9cf1b211435885069c4`.
- Handoff patch: `/private/tmp/KIT-TEMPLATE-APPLICATION-001-v1.patch`, with a matching `.sha256` sidecar. The patch covers the full 18-file working diff, including new files. Its checksum is reported in the final chat after generation to avoid a circular patch checksum inside this record.
- Receiver: Khiêm. Next action: review or apply the patch in an adopting project under that project's own task approval; obtain actual rendered evidence there before claiming template fidelity. No Git delivery or application behavior is asserted here.

Coordinator checklist applied to this bounded task: approval and latest restrictions confirmed; accepted approach and file ownership preserved; counterexamples and evidence limits reviewed; feedback closed across workflow, skills and checklist; current task record and handoff updated. Shared project authority is unchanged. No material decision remains open within this maintenance scope.

## Git delivery authority — 2026-10-15

Khiêm directly instructed “commit and push” in the current chat after reviewing the KIT-TEMPLATE-APPLICATION-001 v1 result and retro cross-check. This authorizes staging, committing and ordinary pushing of the current 18 task-owned files on `main` to its configured upstream `origin/main`, plus staged-diff, SHA/divergence and final worktree checks. It supersedes the earlier no-commit/push restriction only for this delivery. No other file, branch operation, history rewrite, force push, publication or deployment is included.

Preflight: local `main` HEAD and remote `origin/main` both resolve to `8fedcd0b08b256b08e50cfbcd12b3ccc80ed267c`; index is empty; the worktree contains exactly the 18 owned files listed by this task scope, with no unrelated changes. The package/content checks above remain applicable; native behavior and rendered application UI remain NOT_RUN. The handoff patch and checksum must be refreshed after this authority record is added.

The resulting commit, remote SHA/divergence and final worktree status will be reported in the closing chat. This authority record is not proof that delivery has occurred.
