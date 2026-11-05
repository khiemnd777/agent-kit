---
name: code-simplification
description: "Reduce concrete duplication, tangled control flow or needless indirection while preserving behavior. Use for requested refactoring or complexity obstructing the current task."
---

# Code Simplification

Use the [lean operating core](../../../AGENTS.md). Simplify relevant code only. If the code is already clear or its behavior is unknown, do not create an extra cleanup pass.

## Preserve the contract

Read callers and existing tests to understand outputs, errors, side effects/order, permission/data invariants and compatibility. An existing bug is not an approved requirement; identify behavior changes separately from refactoring.

Collapse duplicate branches, name a domain concept, clarify types/control flow, move logic to its actual owner, reuse an existing helper or remove a needless pass-through. Prefer fewer concepts over redistributing the same complexity across more files. Follow project idioms.

## Verify the affected behavior

Keep a coherent diff and run checks that can detect the relevant regression. Use integration checks when an affected seam warrants them. Reuse unaffected evidence; a rename/helper extraction does not require a full suite or new test platform by default.

Repair regressions caused by the change within scope. Preserve others' work and uncertain code. Resolve material behavior/design changes through the existing task authority. Do not install a codemod, reset, revert or commit automatically.

## Stop at the requested improvement

Finish when the scoped complexity is reduced, required behavior is preserved and appropriate verification is sufficient. Optional broader cleanup does not extend the task. Report the structural improvement, actual checks and FAIL/NOT_RUN limits. Source completion is not runtime readiness or human acceptance.
