# Benchmark plan — not yet executed

## Separate the causes

A: current V1 operating kit, using its actual source.
B: V2 with the same available direct scripts/tools and no Sidecar.
C: V2 plus an independently implemented, authorized Sidecar (future; out of scope).

A/B isolates governance/reporting changes. B/C isolates the executor's incremental
benefit. Do not attribute A/B savings to a Sidecar that does not exist.

Use matched source snapshot, task, acceptance, client/model/effort, permissions,
dependency state and environment. Run independent sessions without leaking the
other variant's solution. Alternate order when practical and report small samples
as descriptive, not universal. Correctness and scope/permission preservation win
before latency or cost.

## Cases

A contained approved fix; a real repeatable multi-step job; a mixed novel feature
with a stable subproblem; and a resume/exception case. Use actual workload when
authorized. Do not build a benchmark harness or artificial fault platform merely
to fill metrics. A shell-script baseline is required where it already meets the
same job; compare against competent batching, not deliberately inefficient agents.

## Record

Source/snapshot; task and approval; real loaded instructions/skills; client/model;
first useful action; total elapsed/setup/waits; LLM turns; tool calls; repeated
unchanged checks; measured input/output/cache/reasoning tokens or null with reason;
correctness, security/scope outcomes; repair and recipe maintenance costs.

No percentage savings claimed until measured. Fewer Markdown bytes is only a
source-size observation. Workflow authoring and repairs belong in amortized cost;
one-time work can be cheaper through direct tools. Missing counters are not zero.

## State

Native A/B: NOT_RUN. Sidecar B/C: NOT_RUN and not possible from this package alone.
