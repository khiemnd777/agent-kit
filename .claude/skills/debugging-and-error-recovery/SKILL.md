---
name: debugging-and-error-recovery
description: "Diagnose a concrete failure or unexpected behavior and repair its supported cause. Use for reproducible bugs, failed checks or blocked execution with useful evidence."
---

# Debugging and Error Recovery

Use the [lean operating core](../../../AGENTS.md). A new defect task requires a plan and approval, even if small. Evidenced repairs covered by an already-approved plan do not create another approval/review chain. For long/complex/UI tasks finish approved production code before writing/updating and running tests; use existing evidence during investigation.

## Locate the relevant source

Start with the most specific available signal: error or UI text, route, endpoint, symbol or field. Prefer `rg` and `rg --files`, then narrow searches as evidence identifies the relevant area. For screenshots, search visible text and other observable clues; visual identification remains a hypothesis until source confirms it.

Trace callers, registrations or consumers far enough to establish ownership in the actual project structure. If evidence suggests a contract mismatch, inspect the relevant sides; do not assume a fixed layer sequence. Distinguish a matching file, confirmed ownership and a verified cause. An owner match alone does not establish causality; report unresolved ownership rather than selecting the first plausible match.

Reuse this source map in diagnosis and repair. It does not require a separate triage report, checkpoint or approval round. Keep the requested outcome: locating source alone does not complete an approved bug-fix task or authorize additional work.

## Find the cause

Capture actual/expected behavior, error or reproduction evidence, relevant revision and data/authority limits. Reproduce through an existing command or direct flow where permitted. If unavailable, distinguish a supported hypothesis from a verified cause.

Locate the failing boundary: product logic, contract, authorization/data, test/configuration, shared environment or external service. Choose a concrete hypothesis and the observation that would distinguish it from alternatives. Fix the supported cause and add meaningful regression coverage where appropriate. Preserve domain rules, valid assertions, permissions and retained data.

Run affected checks, including the original user flow when a runtime claim needs it. Reuse unaffected evidence. A business assertion failure is a product/test-contract question, not a tooling failure to dismiss.

## Keep repair proportionate

For blocked tooling, identify the original check and the assertion or usable result it must reach. A related test/config repair can take several justified edits inside scope. After an attempt, assess what changed: new evidence, reduced uncertainty, progress toward that checkpoint, and remaining cost.

Continue while the next diagnostic or repair has a concrete basis and reasonable cost within the task. A changed error alone neither proves progress nor resets unlimited attempts. An unchanged failure with no new hypothesis calls for a different approach or handoff, not repetition. Stop when useful progress stalls, repair becomes a separate infrastructure outcome, or further work needs unavailable scope/authority. Report attempted repairs, current evidence and a specific next action/owner; keep dependent proof open.

Independent shared infrastructure faults belong to their maintenance owner. Missing initial setup may need a minimal running-app/basic-test task, not a comprehensive test platform. New runners, selectors, receipts and review orchestration are not incidental repairs.

## Finish safely

Pause unsafe dependent work, continue independent authorized work and honor human stops. Do not reset data, clean up processes, install tooling or restart services without applicable authority. Explorer/reviewer roles return findings without implementing repairs.

Stop when the defect and relevant regression are resolved. Report cause or hypothesis, repair, actual checks and remaining limits. Broader testing needs a concrete risk or project requirement; a build/mock is not end-to-end proof, acceptance or release.
