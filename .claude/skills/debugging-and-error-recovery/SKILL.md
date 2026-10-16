---
name: debugging-and-error-recovery
description: Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday broke, behavior doesn't match expectations, or you encounter any unexpected error. Use when you need to figure out what broke and why — a systematic approach to finding and fixing the root cause rather than guessing.
---

# Debugging and Error Recovery

Diagnose failures under [team workflow](../../../docs/team-workflow.md#failures-and-blockers). The implementation owner fixes routine defects in the current task; a bug alone does not create a plan, approval or review phase.

## Inputs and scope

Capture actual/expected behavior, reproduction/error evidence, affected source revision and authority/data limits. Pause unsafe or incorrect dependent work and continue independent authorized work. Always honor human stops.

## Find the cause

1. Reproduce using existing commands/direct flow where permitted. State unavailable reproduction rather than manufacture certainty.
2. Localize product logic, API/contracts, data/permissions, test/config, shared environment or external service.
3. Form a supported hypothesis and choose evidence that distinguishes alternatives. Do not repeat unchanged commands or guess at more patches without new evidence.
4. Fix the cause and add meaningful regression coverage where appropriate. Preserve domain rules, authorization and data.
5. Run affected checks and inspect the original flow when the claim needs runtime. Reuse unaffected results; broader suites need an integration/project reason.

A routine diagnosis can be short in the existing task/chat. A separate plan document is needed only for a material design, recovery, data/permission or authority change requiring human review.

## Failure ownership

- Product defect/business assertion: developer repairs behavior; do not call it tooling to dismiss failure.
- Tests/config broken by the change: the same developer repairs the evidenced cause inside valid scope. Identify the original blocked check and its intended assertion/usable-flow checkpoint and valid result, make the focused repair and rerun that check. If tooling still prevents reaching the checkpoint or reporting its valid result, stop tooling edits in the product task and hand off the maintenance blocker; a changed error/configuration, agent or session does not restart repair attempts. Continue independent product work with dependent proof open. If the check reports a failing business assertion, fix that product defect under the existing scope.
- Independent shared runner/environment fault: identify a maintenance owner/task, keep dependent proof open and continue independent code.
- Missing environment from the start: a minimal setup task should deliver a running app/basic test, not a comprehensive harness.

New runners, selectors/admissions/receipts and review orchestration are separate engineering outcomes, not automatic repairs. No blind retries, weakened assertions, unexplained integrity rebaseline, process cleanup, seed/reset or restart without authority. Do not repeat an unchanged failed action. The tooling stopping condition above also applies when inputs or errors change without restoring the blocked checkpoint. Further tooling repair requires explicit maintenance scope; report the original blocker, attempted repair, current evidence and specific next action/owner in the same task.

## Verification and handoff

Use actual focused test/build commands. Keep FAIL/applicable NOT_RUN with reasons and required unproved criteria open. Return the cause/hypothesis, repair, checks and remaining defect to the same task/owner. A build/mock is not end-to-end proof. Explorer/reviewer return findings without implementing the repair; do not infer acceptance or release.
