---
name: code-simplification
description: "Reduce evidenced duplication, tangled control flow or needless indirection without silently changing behavior."
---

# Code Simplification

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Preserve the contract
Inspect callers/tests for outputs, errors, side-effect order, authorization/data
invariants and compatibility. Separate a bug fix from a behavior-preserving
refactor. Do not simplify code whose relevant behavior is unknown.

Collapse duplicate branches, name a domain concept, clarify types/control flow,
move behavior to its owner or remove a needless pass-through. Prefer fewer
concepts, not the same complexity redistributed across extra files. Follow the
project's idioms; line count alone is not a refactoring requirement.

## Verify and stop
Keep a coherent diff and checks that detect the affected regression. Reuse
unaffected evidence; a rename is not a reason for a full audit. Repair regressions
within scope and preserve other people's work. Do not install a codemod, reset,
revert or commit automatically. Finish at the requested improvement, reporting
actual evidence and any required missing check.
