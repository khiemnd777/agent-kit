# Team workflow

This is Agent Kit's single delivery workflow. [Policy](team-policy.md) governs authority and safety. Skills explain techniques; roles assign responsibilities. Neither creates another lifecycle. The flow below describes the life of a coherent change, not six approval gates after every edit.

## Start and agree once

Main session owns delivery by default. Read relevant project decisions and the minimum source/tests. Derive outcome, scope and observable acceptance from the request; record a checkpoint only when coordination or continuation benefits. A clear implementation request permits necessary local edits and checks; planning-only requests remain read-only.

A small well-understood fix can proceed directly with relevant checks and a short explanation, without a separate plan, approval round or task file. A material architecture/data/permission decision needs a reviewable design. Once the current scope is approved, the owner continues routine implementation and repairs without asking at each file, bug or stage. Clarify only decisions that cannot be resolved safely from the available evidence.

## Continuous delivery flow

| Moment | Responsible role | Result / next action |
| --- | --- | --- |
| Requirement | Human + delivery owner | Agree observable behavior, scope, constraints and acceptance |
| Design | Delivery owner | Identify affected layers/contracts, error/data behavior and checks; resolve material choices |
| Development | One implementation owner | Complete a usable change through its real layers and callers; write regression tests and run focused checks while coding |
| Review and CI | Reviewer + configured CI | Evaluate the completed coherent change and relevant checks against the same concrete source revision; owner repairs evidenced defects |
| Acceptance | QA role or authorized human | Demonstrate a usable flow at a meaningful milestone and check actual behavior, permissions/data and important edge states |
| Release | Authorized release owner | Release the verified candidate under project controls, then check operation and recovery readiness |

A role is a responsibility, not a mandatory extra agent. The delivery owner can design, implement, diagnose and hand off. Review should be independent when the risk/project requires it; disclose sequential self-review when independent review did not run. QA can be the human. A separate Coordinator/Supervisor is not the default.

Work in small, complete changes. Include actual imports, routes, callers and data paths; do not hand off an unused API or disconnected UI as complete. Keep branches short-lived when Git work is authorized. A workflow approval is not permission to commit, push, merge or deploy.

## Development and local feedback

The developer owns both implementation and its tests. Use existing project commands for fast focused feedback during coding. Integration/contract checks belong close to changes that affect those seams. Do not invoke a formal reviewer, acceptance cycle or human approval after every function, file or small edit.

The owner repairs product defects and tests/configuration broken by their own change inside valid scope. Diagnose before changing code; a routine repair does not need a new plan document or approval receipt. Escalate when evidence changes a material design, data/permission boundary or required authority.

If the project cannot start or run a basic test, make minimal environment readiness an explicit setup task. Its outcome is a running application/basic check and usable documented commands. Do not retrofit a comprehensive test platform before product work begins. Retained data and real environments still need their actual protections and authority.

## Testing layers

| Layer | When | Scope |
| --- | --- | --- |
| Focused local feedback | While coding | Fast unit/regression checks for the changed logic; relevant integration/contract checks |
| Configured CI | When a coherent revision is submitted, and integration as configured | Project lint/type/build/unit/integration checks; fast feedback target about ten minutes, with expensive jobs separated |
| Acceptance and release checks | Usable user-flow milestones / release candidate | Real running behavior, relevant roles/data/edge states and the project's release/security/operational requirements |

These are check locations, not a universal all-items checklist. A documentation edit does not need an application run; a behavior claim needs the relevant runtime evidence. Do not leave all testing to the end or run an entire suite after each edit. Use broader suites when the affected integration or actual project release rules call for them.

Reuse valid evidence across sessions, reviewers and stages. Recheck when relevant code, inputs, environment or a finding changes the result. An unrelated edit, new chat or stale coordination receipt alone does not invalidate all checks. Tests are maintained to distinguish intended behavior from actual defects; do not weaken assertions or rebaseline unexplained integrity mismatches to obtain green results.

## Review and CI

Submit one coherent, reviewable result with intent, relevant diff, actual checks and known limits. Identify its source revision: use a commit/PR revision when available, or a clearly described working-tree snapshot when Git writes are excluded. Review and check results apply to those inputs; no custom receipt/approval framework is needed.

A reviewer examines correctness, domain/contracts, maintainability and actual security/data/performance risks. Return concrete findings with location, trigger, impact and expected correction. Do not edit application code for mutation tests or repairs. Style preferences and optional polish do not block progress. Required project protections and unresolved relevant defects do.

The implementation owner fixes findings and reruns affected checks. The reviewer rechecks the affected diff/finding; unchanged conclusions remain valid. A new stage does not trigger another reviewer chain. While review/CI waits, continue independent authorized work with non-conflicting ownership. If none remains, hand off the waiting state; do not invent harness work to fill the wait.

## Acceptance and release

Present a usable flow with prerequisites, actual URL/commands, needed roles without secrets, steps and expected results. Acceptance checks happen when the flow is usable, not after every small edit. For an internal change without a user-facing flow, use its observable technical acceptance criteria.

QA/human reports a defect with reproduction, actual/expected behavior and evidence. The developer repairs it and verifies the affected flow. A material product/design change returns to the human; a routine bug does not restart the whole specification/approval cycle.

Release only under explicit scope and the project's required controls. Use the tested candidate, check application operation after release and retain an appropriate recovery path. Passing local checks or finishing code is not deployment, production verification or human acceptance.

## Failures and blockers

Pause only affected work for these delivery reasons:

1. A material decision is missing or the next action expands approved scope/authority.
2. A concrete failure makes dependent work incorrect, unsafe or destructive to data.
3. The next release/real-data action needs authority that has not been granted.

Always honor a direct human stop/replan, including its resumption boundary. These rules do not authorize process termination, data cleanup or bypassing runtime controls.

| Failure | Owner and response |
| --- | --- |
| Product code or business assertion fails | Developer diagnoses the supported cause, fixes it within scope and runs the affected checks |
| The developer's change breaks its tests/configuration | The same developer repairs the evidenced cause within scope, then checks whether the original blocked check reaches its intended assertion or usable-flow checkpoint; apply the tooling stop below if it still cannot |
| Shared runner/environment fails independently of the feature | Name a maintenance owner/task for that problem; keep dependent verification blocked and continue independent product work |
| Same command fails again without changed inputs or new evidence | Stop repeating it; report the actual error, attempted change and one specific next diagnostic action or decision |
| Review/CI/acceptance cannot run within available tools or authority | State the missing proof and owner/next action; required criteria remain open and the affected result is not releasable |

A harness is tooling that launches or collects checks. Repair a supported small test/config defect within the task's authority. Building a new runner, selector/admission/receipt system or review orchestration is a separate engineering outcome, not an automatic response to a failed check. Do not start one as a side effect. A failing business assertion cannot be dismissed as a tooling issue. Never retry merely until a flaky check happens to turn green.

For a tooling repair, identify the original blocked check and its required assertion/usable-flow checkpoint. Make focused evidenced repairs and rerun that check while each attempt provides useful progress, remains proportionate and stays inside scope. A new error alone neither proves progress nor forces a stop. Stop or change strategy when attempts add no useful evidence, the work becomes unrelated infrastructure, or additional authority is required. Report original blocker, repairs, current proof and owner/next action. Continue unaffected work and keep dependent proof open. A now-reachable failing business assertion is a product defect, not a tooling excuse.

## Applying an approved template

Preserve the human-approved template's structure, hierarchy, workflow, controls and responsive behavior. Identify its source/version and approved differences in the same task record. Use the [template reference](../.agents/references/template-application.md) and [acceptance selection guide](template-application-acceptance.md) for relevant rendered/interaction criteria.

Use a representative rendered screen early when an unresolved design choice would otherwise be replicated. Check that choice before copying an unproved approach across dependent screens. This is developer feedback within the approved task, not a mandatory Coordinator/human gate for each screen or edit. Continue independent wiring and other unaffected code. At a usable-flow milestone, verify the affected desktop/mobile behavior and relevant states. Build/source alone does not prove UI fidelity.

## Synchronization and stops

Use one current checkpoint for long/resumed or coordinated work when useful; a focused fix needs no task record. Existing project context/plan/state are shared summaries only when useful; read/update relevant decisions at start/resume and integration, not before every action. Their named writer owns shared changes. Others send concrete proposed updates to that owner. Git records are not live messages or locks.

For authorized parallel work, agree a shared contract and separate ownership. Block only a real incompatible dependency, file collision or resource conflict. Delegation is optional, children do not delegate, and the assigning owner integrates outputs. When a human stops running work, transmit the stop with available authorized tools and report actual acknowledgement/in-flight limits; a status label cannot resume it.

## Handoff and completion

Stop when scoped acceptance, required implementation/callers and proportionate verification are complete. Do not turn optional refactoring, speculative edge cases or polish into new completion criteria.


| Claim | Required evidence |
| --- | --- |
| Source complete | Required implementation, real caller/route/data wiring, source review and usable handoff instructions |
| Behavior verified | Relevant observed checks, including runtime for runtime claims; open required failures/NOT_RUN stay explicit |
| Human accepted | The authorized human's actual acceptance |
| Released | Authorized release plus its actual operating evidence |

A human-requested self-test handoff may be CODE_COMPLETE_UNTESTED: code/callers must be complete, but tests/runtime stay NOT_RUN and availability Unknown until observed. Do not reopen stopped testing to claim readiness. A missing required implementation is incomplete, not a known limitation used to close the task.

When a task record/checkpoint is useful, update it with result, checks/source revision, defects or blockers and next action. For a focused fix the diff, checks and handoff may suffice. Report what changed and why, actual commands/results and meaningful limits. Do not fabricate review independence or attach application startup to agent/session/model/effort/review receipts.

## State vocabulary

Use Agreed, In Development, In Review, Ready for Acceptance, Accepted and Released as useful descriptions. Blocked/Stopped applies only to affected work with a reason and next action. Existing project labels can be retained. States describe progress; they are not approval gates or permission grants.

## Engineering basis

This workflow adapts small complete changes, rapid developer feedback and review that supports forward progress. It is a project operating choice, not a certification claim or proof of measured speed.

- [DORA: test automation](https://dora.dev/capabilities/test-automation/)
- [DORA: continuous integration](https://dora.dev/capabilities/continuous-integration/)
- [Google: small changes](https://google.github.io/eng-practices/review/developer/small-cls.html)
- [Google: code review standard](https://google.github.io/eng-practices/review/reviewer/standard.html)
