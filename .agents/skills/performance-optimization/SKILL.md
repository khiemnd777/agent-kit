---
name: performance-optimization
description: Diagnose a measured or suspected performance regression, then verify a scoped optimization against a comparable baseline and relevant correctness checks.
---

# Performance Optimization

Use the [lean operating core](../../../AGENTS.md). Identify the slow operation, affected workload and required outcome. A large file, unfamiliar framework pattern or merely possible bottleneck does not justify unrelated optimization.

## Measure the relevant behavior

Use an existing profiler, query plan, repeatable benchmark or authorized field evidence. Capture the source revision and conditions that matter: workload, data, cache state, environment and measurement budget. A controlled result can support a local performance claim; it does not prove an improvement for real users without relevant field evidence.

Find where time or resources are actually spent. Inspect the affected query, render path, network waterfall or contention point. Select one supported hypothesis at a time where practical; isolate effects sufficiently to understand the result. Do not add RUM, a CI platform or monitoring infrastructure just to complete local performance work.

## Change the supported cause

Use the existing stack and constrain the change to the measured bottleneck. Query batching, bounded fetching, indexes, caching, code splitting or render changes are options, not a checklist to apply together.

Preserve correctness and security. An index has write and storage costs. A cache must account for tenant, viewer and other response inputs, invalidation and acceptable staleness; do not hide fresh authorization or money/inventory requirements behind stale values. Retain required validation and work instead of removing them to improve a metric.

## Decide from evidence and finish

Measure again under comparable conditions and consider variance. Repeat when it can resolve a concrete uncertainty; stop an experiment that is no longer yielding useful evidence. A result within noise is inconclusive, not a verified win. Remove task-owned complexity whose only justification was an unobserved performance benefit; preserve other work.

Run relevant correctness/regression checks and reuse unaffected evidence. If a check is red or unavailable, distinguish a change-induced regression from an existing product or tooling issue before deciding what to retain. Do not enter a revert, reimplement and full-suite loop. Follow the core's progress and scope rules for further diagnosis.

Use an existing suitable regression guard or record the reproducible measurement command. Keep useful failed hypotheses in the current checkpoint or handoff when they would prevent repeated work; no separate experiment ledger is required. Finish when the agreed performance outcome and appropriate correctness evidence are met, or hand off the specific blocker and limits.

Read [detailed techniques](references/detailed-guide.md) for measurement and interpretation, [optimization examples](references/optimization-patterns.md) for a selected bottleneck, or the [performance reference](../../references/performance-checklist.md) for an applicable check.
