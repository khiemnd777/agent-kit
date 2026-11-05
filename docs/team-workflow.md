# Team workflow

Use the [lean core](../AGENTS.md) for routine work and this detail when delivery decisions need it. [Policy](team-policy.md) governs authority. Skills and roles support this one workflow.

## Start and agree once

Read the request, relevant decisions and the minimum source/tests. Derive the outcome, scope and observable acceptance. The main session owns delivery; a clear implementation request already covers necessary local work and focused checks. Planning-only work stays read-only.

Proceed directly on a clear contained fix. Explain or resolve a material architecture, contract, data or permission decision before dependent work. Do not create a plan, task file or approval round merely because work is starting.

## Proportionate effort

| Effort | Use when | Useful work |
| --- | --- | --- |
| Focused | Clear, contained, low-risk change | Edit, inspect the diff, check relevant behavior, give a short handoff |
| Standard | Feature/bug crosses meaningful seams | Complete callers/integration, cover regressions and use a checkpoint if useful |
| Sensitive | Authorization, private data, money, migrations, production or irreversible effects | Examine affected failure/abuse cases and retain required review, data and release controls |

These are effort choices within one workflow. Duration and file count do not determine risk. Escalate detail when evidence exposes real uncertainty; a long ordinary task does not acquire every sensitive-task check.

## Continuous delivery flow

Clarify what is needed, implement a complete usable change, obtain relevant verification/review, and hand off. Human acceptance and release occur only when part of the task and under their actual authority.

A role is a responsibility, not a required extra agent. The owner can design, implement and diagnose. Independent review is useful or required according to risk/project rules; disclose self-review when applicable. Git actions require their actual scope.

## Development and local feedback

Use existing commands and meaningful tests while changing behavior. Cover actual imports, routes, consumers and data paths; an unused API or disconnected UI is incomplete. A regression check should distinguish the reported defect from correct behavior. Do not add tests that merely restate implementation or an unrelated platform for a documentation edit.

Repair defects caused by the change within valid scope. If basic setup blocks progress, diagnose the concrete missing capability and establish only the necessary readiness under existing authority. Do not turn product work into an incidental runner, selector, admission or review system.

## Testing layers

| Layer | Select when | Evidence |
| --- | --- | --- |
| Focused local checks | Changed logic, contract or UI behavior | Relevant unit/regression, integration or rendered checks |
| Configured CI | Coherent submitted revision and project-required integration | The project's actual checks |
| Acceptance/release | Usable milestone or authorized release | Observed flow, permissions/data and operational criteria appropriate to risk |

No layer is a universal all-items checklist. Documentation/source claims need source evidence; runtime claims need runtime evidence. Broaden checks only for an affected integration risk or required project gate.

Reuse checks and review conclusions while their relevant code, inputs and environment remain valid. Recheck affected evidence after a change or finding. A new chat, phase, reviewer or unrelated edit alone does not invalidate everything. Never weaken assertions or rebaseline unexplained failures to get green.

## Review and CI

Submit a coherent result with intent, diff, source revision, checks and limits. Use a commit/PR when available or identify the working snapshot when Git writes are excluded; no custom receipt framework is needed.

Review findings identify location, trigger, impact and expected correction. Preferences and optional cleanup do not block completion. The owner fixes relevant defects and reruns affected checks; the reviewer rechecks changed findings and retains unaffected conclusions. No per-file review chain is required.

During waits, continue independent authorized work with separate ownership. If none remains, report the waiting state without inventing verification work.

## Acceptance and release

Demonstrate requested usable behavior with prerequisites, commands/URL, safe roles/data, steps and expected results where applicable. An internal change can use observable technical criteria. Routine defects are repaired under existing scope; changed product requirements return to the user.

Release only if authorized and under project controls, using the checked candidate and an appropriate recovery path. Code completion and local checks do not imply human acceptance, deployment or production readiness.

## Failures and blockers

Pause affected work for a material unresolved decision, expanded authority, an unsafe/incorrect dependency, or a direct human stop. Continue independent authorized work.

For a failing check, identify whether it reached the intended assertion or was blocked by tooling. Diagnose a supported cause, make an in-scope repair and recheck the affected result. Continue while a concrete hypothesis and new evidence show useful progress at proportionate cost. There is no fixed one-repair cutoff or automatic retry allowance.

Stop repeating an unchanged command without changed inputs or new evidence. If repairs stop making progress, change diagnostic strategy or hand off the blocker with what was tried and one useful next action. A different error, agent or session is not itself progress. Conversely, reaching a new evidenced cause can justify another small repair without a new approval ritual.

A shared environment fault or substantial tooling rebuild is separate maintenance scope when it exceeds the task. Keep dependent proof open and continue unaffected work. Do not install tools, retry until a flaky check turns green, dismiss a business assertion as tooling, or create a new harness to fill a wait.

## Applying an approved template

Preserve the approved source/version, hierarchy, workflow, controls and responsive behavior. Use the [template reference](../.agents/references/template-application.md) and [acceptance selection guide](template-application-acceptance.md) only for relevant UI work.

Check a representative rendered screen early if an unresolved choice would otherwise spread across dependent screens. Check relevant desktop/mobile states at a usable milestone. This is local feedback, not a gate per screen; source/build alone does not establish visual fidelity.

## Synchronization and stops

For long, resumed or coordinated work, maintain [one checkpoint](tasks/README.md) when useful. Prefer the existing issue/task; do not duplicate plan/state/approval ledgers. Update at meaningful milestones, handoff or a blocker.

Capture outcome/scope/acceptance, done/todo, decisions and latest stop, revision, checks/limits and next action. At resume read that checkpoint and affected source, then continue; do not restart completed work or rerun unaffected checks just because the session changed.

Separate parallel ownership and agree contracts at real dependencies. Git is not a live lock or message channel. The assigning owner integrates children; a sent stop is not proof a worker stopped.

## Handoff and completion

Finish when required implementation/callers and scoped acceptance are satisfied, appropriate verification is complete, and no in-scope blocker remains. Optional polish, wider audits or unrelated refactors are separate work.

| Claim | Evidence |
| --- | --- |
| Source complete | Required implementation and real wiring, reviewed diff, usable handoff |
| Behavior verified | Relevant observed checks; required failures/NOT_RUN remain explicit |
| Human accepted | Actual authorized human acceptance |
| Released | Authorized release and observed operation |

A requested source-only self-test handoff may be CODE_COMPLETE_UNTESTED: implementation is complete but runtime/tests stay NOT_RUN and availability Unknown. Do not reopen stopped tests or hide missing implementation as a limitation.

## State vocabulary

Use project labels, or Agreed, In Development, In Review, Ready for Acceptance, Accepted and Released, only when useful. Blocked/Stopped names the affected work, reason and next action. Labels describe progress; they grant no authority.

## Engineering basis

This is a project operating choice, not proof of measured speed. It draws on [DORA test automation](https://dora.dev/capabilities/test-automation/), [continuous integration](https://dora.dev/capabilities/continuous-integration/), and Google's guidance on [small changes](https://google.github.io/eng-practices/review/developer/small-cls.html) and [review standards](https://google.github.io/eng-practices/review/reviewer/standard.html).
