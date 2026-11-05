# Definition of Done

For long/complex/UI tasks, complete all approved production files and real wiring before writing/updating unit or other tests, then run tests. Do not alternate code/test per file/function. Repair evidenced defects during the test phase and rerun affected checks.
Use the [lean operating core](../../AGENTS.md). Completion means the requested result and sufficient evidence for its risk, with no unresolved blocker to that claim. Stop there; optional polish, broader audits and unrelated refactoring are separate work.

## Match evidence to the result

| Claim | Evidence |
| --- | --- |
| Documentation/instruction change | Reviewed content and relevant links, metadata or package consistency |
| Source complete | Required implementation, real callers/routes/data/commands, source review and usable handoff instructions |
| Behavior verified | Applicable observed checks, including runtime evidence for running-behavior claims |
| Human accepted | Actual authorized human acceptance |
| Released | Authorized release and operating evidence |

Builds, mocks and source reviews support only their observed scope. Missing required implementation is incomplete. Required FAIL/NOT_RUN keeps the affected claim open; an unselected optional check does not become a blocker.

## Select sufficient checks

Use meaningful focused tests for changed behavior and relevant contract/integration checks for affected seams. Keep actual project review, CI, security and release requirements. A simple documentation or cosmetic edit does not imply an application run, new test or full-suite gate.

Reuse valid evidence. Recheck when relevant source, inputs, environment or findings change, not merely for a new session/stage. Routine repairs stay within task authority while evidence, progress and cost justify them; use [failure guidance](../../docs/team-workflow.md#failures-and-blockers) if ownership or next scope is unclear. Do not weaken assertions or build a harness to fill a gap.

A focused task can use a short approved chat plan, diff and relevant checks. Close planning/implementation with actual skill contributions and 1–3 concrete next-step options; the owner saves the authorized phase journal record before reporting. Keep one checkpoint only for a real interruption/handoff, not per file/function. Unapproved/read-only planning remains in chat.

## Requested self-test handoff

For a human-requested CODE_COMPLETE_UNTESTED handoff, complete required code/callers and provide actual prerequisites, commands/manual steps and known blockers. Tests/runtime remain NOT_RUN and availability Unknown until observed. Honor stopped testing and distinguish source completion from acceptance/release.
