---
name: code-review-and-quality
description: Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. Use when asked to review a diff or a pull request, even when the diff is pasted inline.
---

# Code Review and Quality

Review a completed coherent change under [team workflow](../../../docs/team-workflow.md#review-and-ci). Improve code health while allowing progress; do not create per-edit gates or a multi-model chain.

## Inputs

Read agreed behavior/scope/acceptance, source revision/diff, relevant callers/data path and existing check results. Use a described working-tree snapshot when Git writes are excluded. A new receipt framework, commit or clean worktree is not needed solely for review.

## Inspect real risks

- Correctness/domain: requirements, state/invariants, boundaries, errors, denied/repeated/concurrent actions when affected.
- Contracts/data: consumers, mappings, compatibility, authorization/tenant/resource scope, transactions/history and invalidation.
- Maintainability: ownership/dependency direction, clear types/control flow, useful abstractions and no unrelated cleanup or feature logic leaking into general modules.
- Security: affected trust boundaries, inputs/outputs, secrets, dependency/upload risk.
- Performance: affected query/payload bounds, N+1, complexity and evidence for measurement claims.

Prioritize high-confidence defects with triggers and impact. Do not invent risk/latency numbers. Inspection does not prove runtime behavior.

## Evaluate tests/evidence

Check whether assertions distinguish intended behavior from plausible defects; report meaningful missing cases. Do not edit application code for mutation testing or repairs. Return a proposed experiment to the authorized owner if useful.

Assess relevant test/build/rendered evidence for its inputs and reuse valid conclusions. No full suite or repeated test is required merely to finish review. For approved templates use the [template reference](../../references/template-application.md): preserve structure/workflow/controls and require relevant rendered evidence for UI claims. Missing required proof remains open.

## Findings and follow-up

Each actionable finding names severity, location, condition, impact and expected correction. Block on unmet requirements, actual correctness/security/data defects or evidenced quality regressions. Preferences/polish are optional.

The implementation owner repairs findings. Recheck the affected diff/finding and retain unchanged conclusions. Stage/session/receipt changes alone do not need a new reviewer. Shared environment faults go to their owner without another review chain.

## Output

Return findings or state no actionable finding was found, with source/review scope, actual checks and limits. Disclose self-review versus independent review. Review is not authority expansion, human acceptance or release. Honor task/runtime limits and human stops; use TechNote in the requested language.
