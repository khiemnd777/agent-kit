---
name: code-review-and-quality
description: "Review a diff or coherent change for concrete correctness, contract, security and maintainability defects. Use for requested PR/code review or required project review."
---

# Code Review and Quality

Use the [lean operating core](../../../AGENTS.md). Review a coherent result at the appropriate project milestone. Do not introduce a reviewer after every edit or a multi-model approval chain.

## Read the relevant evidence

Read the requested behavior/acceptance, diff and revision, affected callers/data path and existing check results. A described working-tree snapshot is sufficient when no commit exists. No clean-worktree or custom receipt prerequisite is needed solely for review.

Inspect the risks the change actually creates:

- Correctness/domain: changed invariants, boundaries, errors and relevant denied/repeated/concurrent actions.
- Contracts/data: consumers, compatibility, authorization/tenant/resource scope, transactions and invalidation.
- Maintainability: clear control flow/types, sensible ownership and no unnecessary abstractions or unrelated cleanup.
- Security/performance: affected trust boundaries, secret/input handling, query/payload bounds and evidence for any performance claim.

Prioritize defects with a credible trigger and concrete impact. Do not invent a risk or latency estimate. Source inspection is not runtime evidence.

## Evaluate coverage and findings

Check whether assertions distinguish intended behavior from plausible regressions. Reuse valid test/build/rendered evidence. Rerun or broaden checks only to resolve a concrete uncertainty or actual required gate. For template fidelity claims, consult the relevant [template criteria](../../references/template-application.md).

Review-only authority does not permit application edits, mutation testing or repairs. Return a proposed experiment to the implementation owner if needed.

Each actionable finding states location, trigger, impact, severity and expected correction. Required behavior, actual correctness/security/data defects and evidenced quality regressions can block completion. Preferences, speculative improvements and polish remain optional.

## Conclude

Return findings, or state no actionable finding was found within the reviewed scope, with actual checks and limits. Disclose self-review versus independent review. The owner repairs findings; recheck the changed finding while retaining unaffected conclusions. A new session or stage alone does not justify a fresh review chain. Review does not grant human acceptance, Git or release authority.
