---
name: test-driven-development
description: Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code works, when a bug report arrives, or when you're about to modify existing functionality.
---

# Test-Driven Development

Use [team workflow](../../../docs/team-workflow.md#testing-layers) for delivery. Developer-owned tests provide fast feedback while coding; they are not a separate approval phase or a reason to run a full suite after every edit.

## Trigger and inputs

Use for changed logic, state/permission rules, error paths or a bug needing regression coverage. Documentation/static content without behavioral impact does not need a business test. Read existing source/tests and discover the actual framework, checked-in wrappers, focused command and integration/CI conventions before choosing commands. Do not assume npm or install a runner as a side effect.

## Focused loop

1. Define the observable behavior or defect and a test that distinguishes correct output from the plausible regression.
2. For new logic or a reproducible bug, observe the relevant failure before the fix where practical. Distinguish the expected assertion from an unrelated setup/import failure.
3. Implement the behavior through the real owning seam and run its focused checks.
4. Refactor while preserving those assertions. Add important boundary, denied/error/repeated/concurrent cases when the changed rules need them.
5. At a completed coherent change, include the tests/results with the implementation for normal review/configured CI. Broader integration suites run for affected seams or actual project rules.

Keep tests deterministic, isolated and about behavior. Use representative authorized synthetic data. Mock external boundaries when useful, but test database transactions, contract mappings and integration semantics at their actual boundary when those are the claim. A unit test or mock alone cannot prove live integration or rendered UI.

## Test levels and evidence

Prefer the fastest check that exposes the defect. Use integration/contract tests for affected consumers/data and a small set of acceptance tests for important user journeys. Manual/exploratory acceptance checks usable flows at milestones. Do not defer all tests until the project is complete or require every level for each change.

Reuse valid results until relevant source, inputs, environment or findings change. No rerun merely for a new session/stage or reassurance. A developer repairs tests/config broken by their own change inside valid scope; independent shared infrastructure faults go to their maintenance owner. Follow [failure handling](../../../docs/team-workflow.md#failures-and-blockers) without inventing new harness/orchestration or retrying until green.

## Output

Report the behavior covered, actual command/result and meaningful limits in the same task. Keep assertions strong; do not disable failing tests, loosen expectations or rebaseline unexplained mismatches. Required unproved criteria remain open with FAIL/NOT_RUN. A human-requested untested source handoff retains its explicit limits; no acceptance or release is inferred.

Use the existing [testing patterns](../../references/testing-patterns.md) only when the project's framework matches their examples. They are techniques, not a required toolchain or another workflow.
