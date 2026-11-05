# Definition of Done

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

A focused result may need only the diff, relevant checks and short handoff. Use one checkpoint for long/resumed/coordinated work when useful; no mandatory additional record.

## Requested self-test handoff

For a human-requested CODE_COMPLETE_UNTESTED handoff, complete required code/callers and provide actual prerequisites, commands/manual steps and known blockers. Tests/runtime remain NOT_RUN and availability Unknown until observed. Honor stopped testing and distinguish source completion from acceptance/release.
