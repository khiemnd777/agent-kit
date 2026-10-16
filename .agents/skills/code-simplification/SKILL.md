---
name: code-simplification
description: Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be. Use when reviewing code that has accumulated unnecessary complexity.
---

# Code Simplification

Simplify relevant code while preserving confirmed behavior under the [single team workflow](../../../docs/team-workflow.md). Avoid unsolicited cleanup, extra approval chains and a suite run after every small edit.

## Trigger and inputs

Use for real duplication, tangled control flow, unclear boundaries or needless indirection obstructing current work. Read callers/tests and understand why the code exists. Skip a separate simplification pass when code is clear or behavior is not understood.

## Preserve behavior and reduce concepts

Preserve outputs, errors, side effects/order, permissions, data and contracts. Existing bugs are not approved requirements; distinguish behavior fixes from refactoring.

Collapse duplicate branches, name a domain concept, make types explicit, move feature logic to its owning module, reuse a canonical helper or remove a needless pass-through. Prefer fewer concepts over moving the same complexity into more files. Follow existing idioms/conventions.

## Coherent implementation

Keep unrelated refactoring separate and the diff reviewable. Run focused checks during edits and relevant integration checks at completed-change boundaries. Reuse unaffected evidence. No fixed line/file budgets, automatic codemod installation or full suite after each rename/helper.

Repair defects caused by the change within scope. Shared environment faults follow workflow ownership. Do not reset/revert others, commit or delete uncertain code automatically. Material behavior/design changes need the relevant human decision.

## Handoff

Confirm reduced complexity and preserved behavior with applicable evidence, without weakened assertions. Report the structural improvement, checks and FAIL/NOT_RUN limits. Submit for normal review/CI, not another simplification gate. Source completion is not runtime readiness or human acceptance.
