---
name: performance-optimization
description: "Measure a concrete bottleneck and verify a scoped optimization against comparable conditions and correctness."
---

# Performance Optimization

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Establish evidence
Identify the slow operation, workload, outcome, revision, data/cache state and
environment. Use an existing profiler/query plan/benchmark or authorized field
signal. Large files or unfamiliar patterns are not evidence of a bottleneck.
A controlled local result is not automatically a user-facing improvement.

## Change the supported cause
Inspect where time/resources are spent; test a concrete hypothesis. Batching,
indexes, bounded queries, caching, code splitting and render changes are options,
not a checklist. Preserve permissions and correctness. Account for write/storage
cost and cache scope/invalidation/freshness, especially tenant, auth and monetary
data. Do not remove necessary work to improve a metric.

## Compare and stop
Measure under comparable conditions and report variance; an improvement within
noise is inconclusive. Reuse required correctness evidence. Classify a red check
before reverting/reimplementing and avoid full-suite reassurance loops. Remove
task-owned complexity whose performance rationale was not observed, preserving
other work. Keep a useful command/finding in the existing record, not a new ledger.
For Agent Kit optimization, separate governance changes from future executor
benefits; byte counts are not token savings. See [benchmark](../../../docs/benchmark-plan.md).
