---
name: test-driven-development
description: "Design and run meaningful regression, unit and integration tests after the approved code scope is complete. Preserve the project code-first sequence; avoid per-file/function red-green cycles."
---

# Test-Driven Development

Use the [lean operating core](../../../AGENTS.md). The historical skill identifier does not impose test-first development. For long/complex/UI tasks complete all approved production files and real wiring before writing/updating unit or other tests, then run them. Tests provide developer feedback in that phase. Match their depth to the behavior and risk; a documentation, cosmetic or trivial reversible change does not automatically need a new test.

## Choose the useful assertion

Read the affected source and existing tests. Use the project's framework, checked-in wrappers and focused commands. Identify the observable requirement and a plausible regression that the test should catch. Avoid tests that merely repeat the implementation or assert incidental internals.

Investigate existing source/tests and reproduction evidence during planning. During the test phase, make regression assertions distinguish intended behavior from the original defect using available evidence; do not start per-file/function red-green cycles or reverse the approved code-first order. A missing dependency or import error is setup failure, not proof that the regression test detected the bug. If reproduction is unavailable, state that limit.

## Implement and verify

Implement the behavior through its owning seam, then run the focused check. Add boundary, denied/error, repeated or concurrent cases when the changed rules require them. Refactor only when it supports the task while retaining those assertions.

Prefer deterministic isolated tests and authorized synthetic data. Mock external boundaries where useful. Exercise transactions, contract mappings, rendering or live integration at their actual boundary when that is the claim; a mocked unit result cannot establish it.

Broaden testing when changed dependencies, an observed failure or real project requirements warrant it. Reuse unaffected evidence across edits, sessions and review. Do not run the full suite merely for reassurance or require every test level for every change.

## Handle failures and stop

Repair product and related test/config defects within scope while evidence and useful progress justify the cost. Independent infrastructure faults need their owner; keep dependent proof open and continue unaffected work. Do not build a new runner or repeat a flaky check until green.

Keep valid assertions strong. Change expectations only for a confirmed requirement change or demonstrated test defect; retire obsolete/duplicate tests only with required coverage preserved. Stop when scoped behavior has sufficient evidence, unless an actual project gate remains.

Report covered behavior, actual command/result and meaningful FAIL/NOT_RUN limits. Use [testing patterns](../../references/testing-patterns.md) only when the chosen technique and framework need them. A source handoff does not imply acceptance or release.
