# Definition of Done

The project has a shared quality standard. The checks needed to demonstrate that standard depend on the agreed deliverable, changed behavior and actual risk. This Agent Kit adaptation follows [verification scope and completion](../../docs/team-policy.md#verification-scope-and-completion); it does not impose runtime, full-suite, documentation or Git work on every edit.

## Acceptance criteria and completion claims

Acceptance criteria describe the required result. The Definition of Done guides the applicable quality and evidence checks for that result. Neither creates new scope, authority or application behavior.

| Claimed result | Evidence needed |
| --- | --- |
| Documentation or instruction update | Reviewed content, relevant references and package consistency |
| Code integration | Required implementation plus actual imports/callers/routes/UI/commands and source review |
| Verified behavior | Relevant authorized checks, including runtime when the claim depends on runtime behavior |
| Human acceptance | The authorized human's acceptance of the delivered result |
| Release readiness | Applicable project release/security/data/operational gates and explicit delivery authority |

A passing check supports only its observed scope. Code integration is not runtime readiness. A build or mock does not prove live integration, UI behavior, production or human acceptance. Do not claim universal absence of regressions.

## Select applicable checks

Use the task's existing record to identify relevant checks and limits. Do not create a new checklist or gate for every edit.

- **Correctness:** required criteria, invariants, edge/error paths and actual integration seams. Behavior changes or bug fixes need meaningful regression coverage where appropriate and permitted.
- **Quality:** focused source review and relevant formatting/lint/type/build checks. Preserve other work; avoid unrelated cleanup and unsupported abstractions.
- **Integration and data:** affected contracts, authorization, compatibility, transactions, migrations/configuration and concurrency where relevant.
- **Documentation:** changed public behavior, contracts, decisions or operating instructions when users or maintainers need them.
- **Release:** security, observability, recovery and deployment controls appropriate to the actual release. Merge/deploy requires explicit authority; a code handoff does not authorize release.

Run relevant checks at coherent slice, integration or handoff boundaries. Reuse evidence while relevant code, inputs, environment and conclusions remain valid. Recheck only affected scope when evidence is invalidated or a finding remains unresolved. A stage, receipt or unrelated edit does not invalidate every check.

## Errors and unavailable verification

For an API/UI/library error in implementation, runtime or UAT, pause the affected flow, preserve evidence and plan the specific repair before editing. Name the observed condition, cause/hypothesis, affected files/consumers and repair check. Classify the repair against valid approval; material approach/control/scope changes require a revised Approved plan.

If a harness fails, identify the missing proof and a bounded next action with expected observations and a stopping condition. Equivalent verification must demonstrate the same criterion within existing authority and required controls. Do not blindly retry, weaken tests, rebaseline unexplained integrity failures or create another admission/receipt/reviewer chain. Continue independent authorized work; required unproved criteria stay open.

Use PASS for observed success, FAIL for observed failure and NOT_RUN for an applicable check that did not run, with its reason. A check that does not apply is not a failure or an unrun mandatory gate. Record material applicability decisions where they affect the conclusion; trivial edits need no extra ceremony.

## Human-requested self-test handoff

If the human requests code delivery and will perform testing, complete the required implementation and actual caller/route/UI/command wiring, review source and provide configured URLs, startup prerequisites, required roles without secrets, manual steps and known blockers. Missing required code or callers remains incomplete.

Use CODE_COMPLETE_UNTESTED when that is the agreed handoff. Keep tests/runtime NOT_RUN and unobserved availability Unknown. Do not claim Verified, Accepted or release readiness from source completion. Do not reopen stopped tests or harnesses to satisfy an upstream checklist. Retain Auth, data protection, file validation, privacy and necessary runtime integrity controls.

The user may later authorize startup, a focused repair or a specific check. That authority covers the identified action; it does not automatically reopen the old verification program. Keep the current boundary and record results separately from historical evidence.
