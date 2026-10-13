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
