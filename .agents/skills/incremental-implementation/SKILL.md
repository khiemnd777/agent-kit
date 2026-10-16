---
name: incremental-implementation
description: Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the next task from a plan. Use when rolling a change out behind a feature flag, when you're about to write a large amount of code at once, or when a task feels too big to land in one step.
---

# Incremental Implementation

Follow the [single team workflow](../../../docs/team-workflow.md). Deliver small complete changes, not arbitrary file/line batches or a mandatory review after each edit.

## Inputs

Read the task, approved ownership, relevant domain/contracts/source/tests and real dependencies. Implement an already-small coherent change directly.

## Developer-owned loop

1. Implement the agreed behavior through real UI/routes/services/data/commands and callers as applicable.
2. Write meaningful regression tests and run focused checks while coding; use integration/contract checks for affected seams.
3. Diagnose and repair product defects and tests/config broken by the change within valid scope.
4. At a completed coherent change, self-review the diff and submit the result/evidence for normal review and configured CI.
5. Hand off usable flows for acceptance at meaningful milestones. Continue independent authorized work while waiting; do not invent harness work.

No formal reviewer/approval is required after every function or file. Reuse valid evidence and rerun affected inputs/findings. Broader suites need an integration or actual project requirement.

## Slicing and safeguards

Prefer vertical capabilities with the layers each needs. A technical prerequisite can be separate when it has a real consumer/dependency. Keep unrelated refactoring separate. Preserve module ownership, authorization, data invariants and stack conventions.

Use existing isolation for unfinished features when needed; do not automatically add a flag/deployment framework. Recovery for migrations must reflect actual data reversibility, not an unconditional rollback promise. For approved templates use the [template reference](../../references/template-application.md); resolve uncertain replicated choices early and verify usable flows without a Coordinator gate.

## Failure and handoff

Apply [failure handling](../../../docs/team-workflow.md#failures-and-blockers): pause unsafe dependent work, escalate material changes and respect human stops. Small test/config repairs remain developer work; independent shared infrastructure faults need an owner. New runners/receipts/orchestration are not incidental work.

Complete required source/callers before claiming source completion. Report actual checks and FAIL/NOT_RUN, prerequisites, manual steps and defects using the [Definition of Done](../../references/definition-of-done.md). Acceptance/release/Git need their actual authority. No automatic commit, reset or revert.
