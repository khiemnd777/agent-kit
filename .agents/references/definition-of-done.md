# Definition of Done

The [single team workflow](../../docs/team-workflow.md#handoff-and-completion) defines delivery/completion. Select evidence for the agreed claim; this is not another gate or all-items checklist.

## Match evidence to the result

| Claim | Evidence |
| --- | --- |
| Documentation/instruction change | Reviewed content, relevant links/metadata and package consistency |
| Source complete | Required implementation, real imports/callers/routes/UI/data/commands, source review and usable instructions |
| Behavior verified | Applicable observed checks, including runtime for running-behavior claims |
| Human accepted | Actual authorized human acceptance |
| Released | Authorized release and operating evidence |

Builds, mocks, reviews and source handoffs support only observed scope. Missing required code is incomplete. Required FAIL/NOT_RUN keeps the affected claim open.

## Applicable checks

Use focused tests during implementation and project CI/review for completed changes. Check domain correctness, affected contracts/data/permissions, maintainability and relevant lint/type/build/documentation. Release security/recovery requirements apply at release, not every edit. Preserve data and others' work; do not weaken assertions.

Reuse valid evidence; recheck affected code/inputs/environment/findings, not every session/stage/unrelated edit. Routine repairs need no new approval/document chain. Developer-owned test/config repairs stay in scope; unrelated shared infrastructure faults have their own owner. Follow [failure handling](../../docs/team-workflow.md#failures-and-blockers).

## Requested self-test handoff

Complete required code/callers and provide actual startup/prerequisites/URL/manual steps and known blockers. CODE_COMPLETE_UNTESTED is a human-requested source handoff: tests/runtime stay NOT_RUN and availability Unknown until observed. Do not reopen stopped testing or infer acceptance/release. A later action needs its actual scope, not reopening every historical check.
