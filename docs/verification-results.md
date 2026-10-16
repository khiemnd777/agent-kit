# Kit verification results

**Version:** 0.1.0 preview
**Package verification date:** 2026-10-12
**Claim boundary:** static package validation and independent source review. Native behavior and two-machine compatibility are **NOT_RUN**.

The baseline sections below record the 2026-10-12 checks. Later maintenance has separate dated records; it does not turn an earlier observation into a new runtime result.

## Environment

The package checks ran on macOS 26.6.2 with Python 3.13.3 and the existing system Ruby/Psych 3.1.0 YAML parser. No global configuration or dependencies were installed or changed for these checks.

No Codex or Claude Code client was started against this checkout. No native kit agent was invoked. Requested/effective native models and permissions are therefore Unknown.

## Completed package checks

| Check | Result | Observed evidence and limit |
| --- | --- | --- |
| Source provenance | PASS | All 26 original upstream Git blob hashes match the pinned commit metadata; source files remain unchanged |
| Skill distribution | PASS | 17 entrypoints per runtime root; 27 canonical/mirror pairs match byte for byte, including references and original MIT notice |
| Manifest integrity | PASS | 78 maintained kit files have matching SHA-256 entries; mutable project state and reports are deliberately excluded |
| Metadata syntax | PASS | Ruby/Psych parsed 34 skill frontmatters and three Claude native definitions; Python tomllib parsed three Codex definitions |
| Required fields/defaults | PASS | Expected names, descriptions, Codex instructions, omitted Codex model/effort, Claude inherit and read-only intent checked structurally |
| Relative references | PASS | 179 local Markdown links/anchors resolve, including the TechNote reference from both roots |
| Fresh template state | PASS | Planning, unassigned owners, no human approval, no execution scope or fixture task records |
| Coordination templates | PASS | Three templates and nine checklist items; shared state has one designated writer |
| Package text checks | PASS | New kit content reviewed in English; whitespace and targeted private-path/credential-pattern checks found no issue |
| Preservation | PASS | Source checkout status/tracked diff, 26 import-source files and five selected global configuration file hashes unchanged |
| Independent source review | PASS after repair | One path-safety finding was corrected and re-reviewed; no additional actionable finding identified |

The metadata checks validate structure and intent, not installed-client discovery, sandbox enforcement, tool access or language-model behavior. The text pattern scan is not a complete security audit.

## Reproducible integrity command

The exact Python code block in `verification-guide.md` was extracted and executed from the repository root:

```text
PASS: inventory hashes, mirror bytes and 17 skills per root
```

Its shared resolver checks the manifest, inventory, mirror entries and skill directories before reads. It rejects absolute paths, parent traversal, escaped resolved paths and symlink components.

## Owned negative fixtures

The published integrity recipe was exercised against isolated copies under the ignored local verification workspace. Only synthetic copies were changed. No application, client, global configuration or project approval was used or modified.

| Fixture | Expected exit | Result |
| --- | --- | --- |
| Unchanged package | 0 | PASS |
| Changed mirror content | Nonzero: hash/mirror mismatch | PASS |
| Missing mirror file | Nonzero: missing path | PASS |
| Absolute mirror path | Nonzero: unsafe path | PASS |
| Parent-traversal mirror path | Nonzero: unsafe path | PASS |
| Symlink mirror file | Nonzero: unsafe path | PASS |
| Symlink manifest | Nonzero before reading the manifest | PASS |
| Symlink parent directory | Nonzero: unsafe path | PASS |
| Absolute inventory path | Nonzero: unsafe path | PASS |

Nine checks completed: one positive and eight expected-rejection cases. These establish the recipe's tested integrity/path boundaries on this host, not native runtime or cross-machine behavior.

## Review and repair history

The independent read-only reviewer identified that the initial integrity recipe checked inventory paths but not mirror paths or the manifest itself. No unsafe input was used against private data. The coordinator replaced those reads with one bounded resolver, reran the published recipe and performed the negative checks above. The reviewer then inspected the final repair, confirmed the guide checksum and reran the clean recipe without writing files.

This was an independent package source review, not an invocation of `kit-reviewer` through either client. A final whitespace scan flagged Markdown hard-break spaces in this report. Those spaces were removed and the scan was repeated.

## Checks not run

| Check | Status | Reason |
| --- | --- | --- |
| skill-creator quick_validate | NOT_RUN / prerequisite failed | Attempts with system and bundled Python stopped at import because PyYAML is absent. No installation attempted. Ruby/Psych parsing and independent metadata checks completed instead |
| V02 native skill/agent discovery | NOT_RUN | No client session against the completed checkout |
| V03-V10 startup, authorization, session continuity, TechNote and duplicate handling | NOT_RUN | No real client behavioral run |
| V11-V15 parallel ownership, handoff, stale context and integration | NOT_RUN | Two developers on two physical machines were not available in this execution |
| V16-V17 effective model inheritance/overrides | NOT_RUN | No native invocation or runtime model observation |
| V18 effective read-only permissions | NOT_RUN | Authored restrictions and static fields do not prove enforcement |
| V19 unsupported-delegation behavior | NOT_RUN | No client fallback behavior exercised |
| Two-machine round 1 and round 2 | NOT_RUN | Independent machine/client matrix remains pending |

Application-specific builds, business-rule tests, deployment and production acceptance are outside this instruction-only package. Publishing the preview is authorized despite the explicit NOT_RUN items; it is not a verified compatibility release.

These results apply to this kit version. They do not grant approval or imply completed work in projects created from the template.

## Adaptive reporting update — 2026-10-13

**Task:** KIT-REPORTING-001. **Owner:** main session for this bounded kit maintenance update. **Branch / base:** `main` / `22c2a20359072dcb510f3329b97161b16f947fb2`.

**Approval provenance:** Khiêm gave direct human Approved in the current chat on 2026-10-13 for the six adaptive reporting formats and their consistent application to related Agent Kit instructions. That approval covers documentation, package checks and in-scope repairs. On the same date, Khiêm separately authorized committing all reporting updates and pushing them to `origin/main`. Global configuration, application changes and publication beyond the requested repository push remain outside this scope. No later stop instruction was received.

**Result:** The canonical TechNote document now defines before-and-after reports and illustrative examples for conversation, planning and implementation. AGENTS.md, README, policy, workflow, all four common roles, skills catalog and the existing coordination checklist route to that source. Claude's literal AGENTS.md import and both TechNote skill routes remain intact. The three coordination templates still hold detailed records.

**Acceptance:** All six minimum formats match the approved proposal. Reports retain material decisions, blockers, actual verification and limits. Simple follow-ups remain direct, and reports add no approval gate inside existing authorization. Fresh project context, plan, state and task inventory retain their unassigned, unapproved values.

| Check | Result | Evidence and limit |
| --- | --- | --- |
| Published package-integrity recipe | PASS | Extracted the exact Python recipe from verification-guide.md and executed it from the repository root; 78 inventory hashes, 27 mirror pairs and 17 skills per root remain valid |
| Local Markdown references | PASS | Read-only Python scan resolved 189 local links/anchors across 76 Markdown files; external URLs were not fetched |
| Source and template preservation | PASS | SHA-1 Git blob checks preserve all 26 canonical upstream sources and their mirrors; comparison with the base commit preserves fresh project files, task inventory, native adapters and model/tool settings |
| Coordination structure | PASS | Source inspection retains three coordination templates and nine checklist items; detailed handoff requirements remain in place |
| Whitespace | PASS | `git diff --check` returned exit code 0 |
| Independent source review | PASS | Bounded kit-reviewer subagent inspected the assigned guidance diff and found no actionable issue; its guidance whitespace check returned exit code 0. This was source review, not native client discovery or a V20 behavioral run |
| V20 runtime reporting behavior | NOT_RUN | Six formats and edge scenarios are documented in the verification guide; fresh native client sessions and the two-machine matrix were not exercised |

**Current state / next action:** The approved guidance update, source review and applicable package checks are complete. Delivery to `origin/main` is authorized; actual commit and remote synchronization evidence belongs to Git history and the delivery report. V20 remains the next runtime check when a client verification scope is authorized. Native discovery, runtime reporting consistency and reading-time improvement remain Unknown. The reviewer performed read-only inspection; effective runtime sandbox enforcement was not verified. This record is kit maintenance evidence, not inherited project approval or an application task record.

## Recovery retro guidance update — 2026-10-13

**Task / plan:** KIT-RETRO-001 / P2, superseding the unapproved P1 proposal. **Owner:** main session, designated coordinator and sole writer for this bounded kit maintenance task. **Branch / base:** `main` / `8b70cd4ba02b63a8ef8c723564ee32df2c4147f5`.

**Approval provenance:** Khiêm gave direct human “Approved P2 / KIT-RETRO-001” in the current chat on 2026-10-13 for the presented documentation and static-verification plan. This approval covers routine work and repairs within P2. The earlier KIT-REPORTING-001 approval grants no authority to this task. The initial P2 restriction excluded commit/push. Later in the same chat on 2026-10-13, Khiêm explicitly authorized committing and pushing the ten P2 files, with remote and final worktree verification, while retaining native/fixture NOT_RUN. That instruction covers ordinary Git delivery on the existing `main` branch to `origin/main`. **Latest restriction:** native behavior and fixtures remain NOT_RUN. If the approach changes materially, stop affected execution and present a revised plan for human review and explicit approval. This approval does not resume stopped work in another project.

**Owned scope:** `docs/team-policy.md`, `docs/team-workflow.md`, `docs/agent-coordination-templates.md`, `docs/verification-guide.md`, `docs/roles/coordinator.md`, `docs/roles/implementer.md`, `docs/roles/reviewer.md`, `docs/technote.md`, this maintenance section and affected hashes in `docs/skills-manifest.json`. The subsequent Git instruction authorizes staging/committing these ten files and pushing to `origin/main`, with remote/worktree checks. Pinky Lamb application/data/CMS ledgers, global configuration, model routing, sandbox/permissions, dependency installation, unrelated Git writes, publication beyond the requested repository push and deployment are excluded.

**Goal / accepted decisions:** Distinguish routine repairs under a still-valid approved approach from material changes that require stopping and replanning, even with the same file allowlist. Make stop acknowledgement explicit, reuse valid reviews, justify blocking gates, separate coordination metadata from runtime checks and track the next user acceptance criterion. Preserve approval, data protection and required quality gates. Retain the existing templates and one current maintenance record.

**Sources / limits:** The human-supplied CMS-RECOVERY-001 v1 retro is investigation context; its application/runtime claims have not been independently reproduced here. Current policy, workflow, templates, guide, role instructions, reporting guidance and kit state were inspected. Fresh project context/plan/state remain unassigned and unapproved. Model routing stays inherited; resolved model/effort and effective native agent permissions are Unknown. No native agent or fixture is part of this task.

**Result / acceptance:** The ten owned files now implement P2's guidance and evidence updates. Policy, workflow, templates and the three affected roles distinguish valid routine repairs from material approach changes within the same allowlist. Stops have sent/acknowledged/in-flight/Unknown states and require explicit relevant approval to resume. Review reuse, blocking-gate justification, runtime separation, early real-flow evidence and specific progress reporting agree across the sources. A–G extend V05/V06 and add V21–V25, each with setup, expected behavior, failure signals, evidence and limits. The three templates, nine checklist items, historical evidence and fresh project authority state are preserved. These are documentation/static acceptance results, not observed native behavior or human product acceptance.

| Actual check | Result | Evidence and limit |
| --- | --- | --- |
| Guidance traceability and final source review | PASS | Coordinator inspected `git diff --` for all owned guidance and mapped repair/material-change/stop, review/gate, runtime, preservation and reporting requirements to policy/workflow/templates/roles/scenarios. A routine wording repair retained independent review where warranted in the existing checklist and clarified the material-change boundary; no material approach change or unresolved source finding remains. This was coordinator self-review, not independent/native review |
| Scenario structure | Written / static PASS | Read-only inline `python3` inspection confirms A–G each contain the five required fields. Scenario content includes failure cases, preserved-data boundaries and capability/approval limits; it does not establish behavioral PASS |
| Published package-integrity recipe | PASS | Read-only inline `python3` extracted and executed the exact recipe from verification-guide.md; comparison with the base confirms the recipe is unchanged. Output: `PASS: inventory hashes, mirror bytes and 17 skills per root`. All 78 inventory entries and 27 mirror pairs remain valid; only eight owned source hashes changed |
| Local Markdown references | PASS | Read-only inline `python3` scan of `git ls-files '*.md'` resolved 198 local links/anchors across 76 tracked Markdown files, excluding fenced examples. External URLs were not fetched |
| Upstream provenance | PASS | Read-only inline `python3` calculated Git blob SHA-1 values for all 26 canonical upstream sources and 26 mirrored sources; each matches its recorded pinned origin |
| Scope, history and protected-file preservation | PASS | Read-only inline `python3` used `git diff --name-only 8b70cd4ba02b63a8ef8c723564ee32df2c4147f5` and byte comparisons with `git show` at that base. Exactly ten approved files changed; all 74 other tracked files, fresh project sources/task inventory, native adapters, model routing and upstream skills remain byte-identical. This report retains its complete historical prefix. Manifest metadata/inventory/mirror definitions are unchanged apart from eight approved source digests |
| Coordination structure and added text | PASS | Read-only inline `python3` counted three templates and nine checklist items and scanned added text for private absolute paths, credential patterns and retro-specific implementation literals. No issue found; the text scan is not a complete security audit |
| Pre-delivery whitespace and Git state | PASS | `git diff --check` returned exit code 0. Before Git delivery, `git status --short --branch` and read-only HEAD/index checks confirmed ten unstaged owned changes, unchanged HEAD, no staged/untracked files and no commit/push |
| A–G native/fixture behavior and two-machine matrix | NOT_RUN | Explicit P2 restriction; no native client, worker fixture, application or two-machine behavioral run was performed. Writing scenarios and checking their source cannot prove behavior |
| Independent review and effective runtime permissions | NOT_RUN / Unknown | Coordinator performed source review sequentially. No independent native reviewer ran, and effective sandbox, stop enforcement, model/effort and application behavior were not observed |

**Current state / handoff:** Complete for the approved documentation and static-verification scope, with Git delivery separately authorized. The resulting commit, remote SHA/divergence comparison and final worktree status are delivery evidence in Git history and the delivery report; authorization alone does not establish push success. The current record is this KIT-RETRO-001 section; prior dated records remain historical. The coordinator checklist was applied to P2 authority, ownership, acceptance, final diff, evidence limits and this handoff. No writer was delegated, no later stop instruction was received and no material decision is outstanding.

**Feedback / next action:** P2 closes the planning feedback about same-allowlist material changes and stop precedence. No documentation work remains; the approved delivery covers only these ten files and requires remote/worktree confirmation in the delivery report. Native scenarios remain excluded; the next behavioral verification would require a separately identified client/fixture scope and direct human approval. Kit maintenance evidence does not grant authority to projects adopting the template or resume Pinky Lamb recovery.

## Explorer and Reviewer responsibility correction — 2026-10-13

Current maintenance record: [TASK-003](tasks/TASK-003.md). Khiêm directly approved correcting the adapters and docs so Explorer and Reviewer do not change application code or implement solutions, while permissions follow the runtime and task scope.

This correction supersedes the earlier role-based read-only configuration and V18 expectation. Earlier rows about read-only intent or enforcement describe the previous configuration; they remain historical evidence. Current adapters omit Codex sandbox overrides and Claude tool/permission overrides. Investigation and review instructions permit authorized checks and evidence capture while prohibiting application code changes, implementation and deployment.

Local verification results and handoff are maintained in TASK-003. Native discovery, invocation, effective permissions, V18 behavior and two-machine checks remain NOT_RUN. Package validation does not establish those outcomes.

## Proportionate verification and M3 coordination retrospective — 2026-10-14

Current maintenance record: [TASK-004](tasks/TASK-004.md). Khiêm directly approved P2.1 for exactly 21 Agent Kit files and local checks, excluding Pinky Lamb writes, a new harness and commit/push. The earlier pause/planning-only instruction is superseded only within this scope.

Policy, coordination templates/roles and the adapted workflows now select checks by claim, changed behavior and risk; bound failed verification without another admission/receipt chain; partition explicitly delegated Coordinator decisions; and separate code integration, verified behavior and human acceptance. An API/UI/library error during implementation/runtime/UAT pauses the affected flow for a focused repair plan before edits. Routine covered repair authority and material-change approval remain distinct. Auth, data preservation and necessary integrity controls are retained.

Current provenance: 22 of the 26 canonical upstream files still match the original pin; `using-agent-skills`, `planning-and-task-breakdown`, `incremental-implementation` and `definition-of-done.md` are explicit Agent Kit adaptations with matching Claude copies and retained original origin metadata/license. Earlier rows asserting all 26 unchanged describe their original observation dates; they are not current claims.

| Actual check | Result | Evidence and limit |
| --- | --- | --- |
| Published package recipe via inline `python3` | PASS | 78 inventory hashes, 27 content/provenance mirror pairs, 17 skills per root; 22 original/four adapted canonical upstream sources |
| Metadata via `ruby -rpsych`, JSON and `tomllib` | PASS | 37 YAML frontmatters and three unchanged Codex adapters; six adapted entrypoints also passed equivalent name/description/scaffold checks |
| Bundled skill-creator quick_validate.py | NOT_RUN / prerequisite failed | One attempt exited 1 because PyYAML is absent, before validation. No dependency installed; existing Ruby/Psych checks provide separate evidence |
| Changed-source links, scope and preservation | PASS | Final inline `python3` resolved 83 local links/anchors across 20 changed Markdown files and confirmed exactly 21 owned changes, 67 protected tracked files unchanged, historical report prefix/original provenance retained, HEAD unchanged and index empty. `git diff --check` exited 0; no commit/push |
| V26–V30 | Written / reviewed | Scenario-based self-review covers proportional checks, harness failure, delegated coordination, untested handoff and focused error repair. No behavioral PASS is inferred |
| Native behavior, independent native review and two-machine compatibility | NOT_RUN | No client/agent/fixture/application run or new harness; effective native behavior remains Unknown |

The exact approval, external retrospective evidence, file ownership, checks and final handoff live in TASK-004. No other repository or fresh-project authority is changed. Local package validation does not prove that native agents follow the new guidance or that Pinky Lamb works.

## Approved-template application guidance — 2026-10-15

**Task:** [KIT-TEMPLATE-APPLICATION-001 v1 / TASK-005](tasks/TASK-005.md). **Source base HEAD:** `8fedcd0b08b256b08e50cfbcd12b3ccc80ed267c`. Khiêm directly approved the scoped workflow, four skills and mirrors, one reference pair, checklist and necessary package documentation in the current chat. Commit/push, application/CMS execution and native behavioral verification are excluded.

The approved-template path now requires template identity and prerequisites before broad implementation, then an evidence-backed representative screen connected to real controller/data at matched desktop/mobile viewports before dependent expansion. The external design reference rule stays limited to external inspiration. The acceptance checklist uses criterion, screen, role, data state, viewport, expected result, evidence, PASS/FAIL/NOT_RUN and owner. Code integrated, verified behavior/UI and Human accepted remain separate; `CODE_COMPLETE_UNTESTED` is limited to a human-requested self-test source handoff.

| Actual check | Result | Evidence and limit |
| --- | --- | --- |
| Published package-integrity recipe | PASS | 81 inventory hashes, 28 mirror byte/hash pairs and 17 skills per root; 20 original and six adapted canonical upstream files. The existing recipe now checks each pair's recorded hash as well as bytes. |
| Skill metadata and manifest syntax | PASS | Ruby/Psych parsed 34 skill frontmatters with name/description; Python parsed manifest JSON. No native client discovery is implied. |
| Changed Markdown links/anchors | PASS | Read-only scan resolved 56 local links/anchors across 17 changed Markdown files, including new files. External URLs were not fetched. |
| Provenance and protected project files | PASS | Source comparison retained each previous inventory origin; project context, plan and state remain byte-identical to HEAD. Original upstream blob metadata remains pinned. |
| Four counterexamples | Written / source self-review PASS | The reference, skills, workflow and checklist reject color-only structural drift, build-only UI claims, empty-only layout evidence and page-level no-overflow with a clipped nested control. This checks instruction coverage, not agent behavior. |
| Retro cross-check | Written / source self-review PASS | Compared with the source retro in Codex thread `01a13b73-294b-7461-bd95-4de864be7f09`; added explicit template-element mapping, navigation/selection/dirty state, disabled/busy controls, approved preview-source identity and separate per-screen/group evidence after expansion. CMS-specific adoption and product verification remain separate. |
| Whitespace and scoped diff | PASS | `git diff --check` returned 0. Final file scope and handoff patch are recorded in TASK-005. |
| Native agent behavior and rendered application UI | NOT_RUN | No native agent, application or CMS environment was run. Source walkthrough does not establish behavioral PASS. |
| Independent review and human product acceptance | NOT_RUN | The main session performed sequential source self-review; no independent native reviewer or product acceptance was requested or claimed. |

Historical verification sections above retain their original observations. This maintenance result establishes local package and instruction consistency only; adopting projects must gather their own rendered evidence under their own approval.


## Four feature / verification-infrastructure boundaries — 2026-10-16

Current maintenance record: [KIT-HARNESS-BOUNDARIES-001 v1 / TASK-006](tasks/TASK-006.md). Khiêm directly approved the four boundaries and six skills plus Claude mirrors, excluding Pinky Lamb changes, a new harness and commit/push. This maintenance task does not change fresh project context/plan/state or grant authority to an adopting project.

Policy, workflow and task assignment guidance distinguish business tests using the existing runner from verification-infrastructure implementation. Harness start/collection failures stop that attempt without harness repair/replacement/replay under feature approval. Source changes invalidate affected evidence instead of creating a new generation/namespace/review chain solely for a stale receipt. Application startup and requests retain necessary runtime protections while keeping agent/session/model/effort/coordination receipts outside operating conditions.

The six adapted skills are debugging-and-error-recovery, test-driven-development, code-review-and-quality, code-simplification, context-engineering and spec-driven-development. Their Claude copies match the canonical content. Universal full-suite-per-implementation/refactor-step instructions, reviewer mutation edits, session/task-based reruns and per-phase human reapproval were removed. Failed business assertions, initial/material-change approval and required unproved acceptance criteria remain binding.

The original upstream pin, origin metadata and license remain intact. Five canonical upstream entrypoints are newly marked as local adaptations; code-review-and-quality retains its earlier template adaptation and adds this approved change. Current total: 15 original / 11 adapted of 26 upstream canonical files. Historical observations above remain historical.

Initial local checks: published package-integrity recipe PASS; 12 entrypoint frontmatters/name/description/scaffold checks via existing Ruby/Psych PASS; git diff --check PASS. The bundled quick_validate.py is NOT_RUN because its PyYAML dependency is absent; no installation or retry occurred. Final scope/link/preservation/package evidence and the reviewed handoff are recorded in TASK-006.

Native discovery/compliance with the four boundaries, effective model/permission behavior, two-machine compatibility, application/runtime behavior and independent native review remain NOT_RUN/Unknown. No new runner, fixture or harness was created. This record establishes instruction/package changes and local checks, not a Pinky Lamb repair or a measured reduction in tokens/time. Commit/push remains excluded.


## Continuous workflow remake — 2026-10-17

Current maintenance: [KIT-CONTINUOUS-WORKFLOW-001 v1 / TASK-007](tasks/TASK-007.md). Khiêm directly approved replacing old workflow instructions and synchronizing Claude, excluding Pinky Lamb, a new harness and commit/push. Prior records remain historical; TASK-006's four-boundary wording is superseded as active guidance by the continuous workflow.

The single workflow now owns delivery. Developer tests accompany implementation; review/CI evaluates completed coherent changes; acceptance checks usable flows at milestones. One delivery owner is the default. Routine in-scope product/test/config repairs continue without new approval documents, while independent shared infrastructure faults have an owner. No per-edit reviewer, phase approval, default Supervisor/Coordinator or mandatory native scenario campaign is introduced.

Nine process aids, seven technical skill routing notes, shared references, entrypoints/roles/native instruction bodies and onboarding/summary guidance align with that workflow. Original skill metadata, upstream origins/pin/license, native schema/model/permission intent and historical evidence are retained. Current local check results and exact scope are in TASK-007.

Native discovery/workflow compliance, effective runtime settings, independent native review, two-machine collaboration, application behavior and measured delivery-speed/token improvements remain NOT_RUN/Unknown. Source/package consistency is not behavioral proof, human acceptance or a repair to Pinky Lamb. No new harness, installation, application execution or Git write is part of this maintenance.


Final local result for TASK-007: PASS for the existing package recipe (81 entries, 28 mirror pairs, 17 skills/root, 8 original / 18 adapted upstream files), 37 YAML frontmatters and three TOML definitions, 275 local links/anchors, exact 67-file remake scope and preservation of 27 other starting files, plus whitespace and unchanged HEAD/empty index. All 34 skill frontmatters and original upstream origins/license are retained. quick_validate.py remains NOT_RUN because PyYAML is absent; existing Ruby/Psych provides separate metadata evidence. Sequential source review is complete; native behavior, independent review, two-machine operation and measured speed/token improvements remain unverified. The exact current evidence and next action are in TASK-007; no commit/push occurred.

## Eight-finding correction to the remake — 2026-10-17

Current maintenance remains [TASK-007](tasks/TASK-007.md#approved-eight-finding-correction--2026-10-17). Khiêm approved fixing exactly the eight subsequent review findings, P1 first, with Claude synchronization and no Pinky Lamb changes, new harness or commit/push. That review superseded the initial self-review's no-unresolved-finding conclusion; the earlier observations above are preserved.

The correction adds a tooling stop based on restoring the original blocked check and valid result, scopes source research and security approval to actual missing decisions, removes mandatory RUM/CI/observability platform setup, line-count splits and commit prerequisites, and replaces missing-skill routes. Actual security/data protections, business assertions and project release requirements remain binding. Seven skill pairs, three reference pairs, workflow and package/evidence records are affected. Original upstream metadata remains intact; current adaptation counts are 21 adapted / 5 original. Source-driven and observability descriptions are narrowed; the skill inventory and native adapters are unchanged.

Current local result: PASS for the existing package recipe (81 entries, 28 mirror pairs, 17 skills/root, 21 adapted / 5 original upstream files), Ruby/Psych parsing of 37 YAML frontmatters, 144 affected local links/anchors, exact 25-file follow-up scope with 69 other source files byte-identical, historical prefixes/provenance preservation and whitespace/unchanged HEAD/empty index. No source file was added/deleted. The full commands, eight source-review cases and limits are recorded in TASK-007. The bundled quick validator remains NOT_RUN because PyYAML is absent; Ruby/Psych is separate evidence.

No native/application/independent behavioral review or speed/token experiment is part of this correction. Static package/source checks cannot prove that an agent will comply or that delivery is faster. Source corrections and Claude synchronization are complete; human acceptance, commit/push and runtime claims are not inferred.

## Seven remaining instruction conflicts corrected — 2026-10-17

Current maintenance remains [TASK-007](tasks/TASK-007.md#approved-seven-finding-correction--2026-10-17). Khiêm approved fixing exactly the seven subsequent review findings with Claude synchronization and no Pinky Lamb changes, new harness or commit/push. Prior observations remain historical.

The correction scopes local security checks, UI evidence and documentation to the affected change; removes the invalid standalone axe-core command and automatic props-depth refactor; classifies failures before undoing performance work; and preserves valid assertions when retiring tests. Actual security/release criteria, approved-template fidelity and the existing tooling stop remain binding. Four skill pairs, two reference pairs and package/evidence records are affected. All frontmatter and original upstream metadata are retained; current adaptation counts are 23 adapted / 3 original.

Current local result: PASS for the existing package recipe (81 entries, 28 mirror pairs, 17 skills/root, 23 adapted / 3 original upstream files), Ruby/Psych parsing of 37 YAML frontmatters, 102 affected local links/anchors, exact 16-file follow-up scope with 78 other files byte-identical, historical prefix/provenance/frontmatter preservation and whitespace/unchanged HEAD/empty index. No source file was added/deleted. Actual commands, seven source cases and limits are recorded in TASK-007. The bundled quick validator remains NOT_RUN because PyYAML is absent; Ruby/Psych is separate evidence.

The seven approved source corrections and Claude synchronization are complete. No native/application/independent behavioral review or speed/token experiment is included. Source/package checks do not prove agent compliance, runtime improvement or human acceptance. No new harness, installation, Pinky Lamb change or Git mutation occurred; commit/push remains excluded.

## Cookie and severity instruction conflicts corrected — 2026-10-17

Current maintenance remains [TASK-007](tasks/TASK-007.md#approved-two-conflict-correction--2026-10-17). Khiêm approved correcting exactly the two remaining review findings and synchronizing Claude, excluding Pinky Lamb, a new harness and commit/push. Previous observations remain historical.

Security skill/checklist now agree on Lax/Strict cookie choices under the established project session/CSRF policy. Observability skill/checklist preserve project severity names, level count and routing; page/ticket are urgency examples. Neither correction changes application configuration or introduces another approval/review stage. Frontmatter, inventory, native adapters, workflow/P1 stop and upstream origins/pin/license remain intact; adaptation counts remain 23 adapted / 3 original.

Current local result: PASS for the existing package recipe (81 entries, 28 mirror pairs, 17 skills/root, unchanged 23 adapted / 3 original upstream files), Ruby/Psych parsing of 37 YAML frontmatters, 97 local links/anchors, exact 12-file follow-up scope with 82 other files byte-identical, historical prefix/frontmatter/provenance preservation, whitespace and unchanged HEAD/empty index. No source file was added/deleted. Actual checks, cases and limits are in TASK-007. The bundled quick validator remains NOT_RUN because PyYAML is absent; Ruby/Psych is separate evidence.

The two source corrections and Claude synchronization are complete. Native/application cookie/auth/alert behavior, independent review, effective runtime settings, two-machine operation and speed/token effects remain NOT_RUN/Unknown. No application configuration, Pinky Lamb source, new harness, dependency, global setting or Git state was changed; commit/push remains excluded. Source/package checks do not establish runtime success or human acceptance.
