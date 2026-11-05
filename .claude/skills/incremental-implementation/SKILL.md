---
name: incremental-implementation
description: "Implement a larger feature as coherent usable changes through its real layers and callers. Use when dependency order or unfinished behavior needs careful staging."
---

# Incremental Implementation

Use the [lean operating core](../../../AGENTS.md). Implement only after approval of the task plan, including for small changes. Do not add an unnecessary slicing exercise. Approval covers routine local edits, focused checks and evidenced repairs within the plan; material scope/solution changes need amended approval.

## Deliver usable increments

1. Read the relevant requirement, contracts, source and tests. Identify the actual caller or user flow that will exercise the change.
2. Implement that behavior through the necessary UI/routes/services/data/commands. Include the real integration; an unused helper or disconnected screen is not a complete feature.
3. Add or update meaningful regression coverage for changed logic and risky seams. For long/complex/UI tasks complete all approved production files and real integration before writing/updating tests, then run relevant existing checks; do not add tests that merely mirror trivial edits.
4. Diagnose evidenced defects and repair within scope. Inspect the coherent diff and report actual checks for normal project review/CI when applicable.

Prefer complete capabilities over arbitrary file batches. A technical prerequisite can stand alone when it has a real consumer. Preserve authorization, data invariants, module boundaries and stack conventions. Keep unrelated cleanup outside the task.

Use existing isolation for unfinished behavior when needed; do not introduce feature-flag or deployment infrastructure automatically. Migration recovery must reflect actual data reversibility. For template-based UI, consult the [template reference](../../references/template-application.md) when rendered fidelity is part of acceptance.

## Control effort and finish

Reuse unaffected evidence; rerun checks for changed inputs or findings. Continue repair while a concrete hypothesis, useful progress and reasonable cost justify it. Escalate material changes or unavailable authority; pause unsafe dependent work and honor human stops. New runners, receipts or review orchestration are separate outcomes.

For long/resumed work keep one useful checkpoint, not a record after each edit. Stop when scoped implementation, caller integration and appropriate checks are complete with no relevant blocker. Report remaining required FAIL/NOT_RUN honestly; optional polish is not unfinished delivery. Git, acceptance and release retain their actual authority. Consult the [completion reference](../../references/definition-of-done.md) only if the claim is unclear.
