---
name: code-review-and-quality
description: "Review a coherent diff for concrete correctness, contract, security and maintainability defects; distinguish evidence from preference."
---

# Code Review and Quality

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Inspect the relevant evidence
Read acceptance, diff/snapshot, affected callers/data paths and existing results.
A described working snapshot can be sufficient; review does not require a new
commit or clean-worktree ceremony. Inspect changed invariants, denied/error or
concurrent actions, ownership/tenant boundaries, contracts, transactions,
invalidation, input/secret handling and bounded performance only where affected.

Known collection/checking steps can be DIRECT or DELEGATE; semantic correctness
still needs review. Do not treat an executor's green result as code-review proof.

## Report actionable findings
Each finding identifies location, trigger, impact, severity and expected correction.
Prioritize actual defects and missing required evidence. Preferences, speculative
risk and unrelated polish do not block completion. Check that assertions would
catch plausible regressions. Source inspection is not observed runtime behavior.

Review-only authority does not allow code edits, mutation tests, repairs or deploys.
Return proposed experiments to the implementation owner. Recheck changed findings
and retain unaffected conclusions; do not introduce per-edit or multi-model review
chains. Disclose self-review versus independent review and the review limits.
