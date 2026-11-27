---
name: execution-delegation
description: "Decide WHEN to hand a complete stable work block to a real external executor, or use direct tools/reasoning instead."
---

# Execution Delegation

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Trigger
Use when a repeatable block is known at task entry or during a mixed task and
external execution may add value. Do not invoke for every edit or just because a
task is long. No additional LLM router or full catalog scan is required.

## Decide and hand off
Prefer an adequate existing command/script/CI. Otherwise confirm real capability
availability/review/version, approved target/snapshot, side effects, constraints
and required evidence. Send one complete outcome-level request. Do not send the
whole chat or micromanage internal steps. The owner keeps product decisions,
authority and acceptance; the executor owns execution within the contract.

## Interpret and stop
Read a compact result, validate request/snapshot/evidence binding and inspect
only the detail relevant to a finding or acceptance. Reason on unknown failures;
seek the actual human authority for expanded scope. Reconcile uncertain effects
before replay. Preserve unaffected evidence. A PASS is not human acceptance.

## Missing Sidecar
This V2 package contains no Sidecar/runtime connector. Use an equivalent authorized
DIRECT route or report the missing prerequisite. Do not install, implement,
simulate or poll an unavailable executor. Draft contract examples are not results.
Consult the [WHEN policy](../../../docs/execution/when.md),
[delegation detail](../../../docs/execution/delegation-policy.md) and
[draft contract](../../../contracts/README.md) only for the actual decision.
