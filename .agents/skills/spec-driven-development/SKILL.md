---
name: spec-driven-development
description: Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when drafting a PRD or requirements document with objectives and scope, or when requirements are unclear, ambiguous, or only exist as a vague idea. Use when a single requirement spans several independently testable capabilities and needs decomposing into a capability map of modules before specifying.
---

# Spec-Driven Development

Clarify meaningful requirements under the [single team workflow](../../../docs/team-workflow.md). Specifications support implementation; they are not a mandatory Specify/Plan/Tasks/Implement approval hierarchy.

## Trigger and inputs

Use when actors, rules, data/state, interfaces or acceptance are unclear for a significant change. A well-understood small fix can use a short explanation in its existing task. Reuse an accepted specification.

## Define the requirement

Record the outcome/scope, actors/permissions, states/invariants, happy/error/denied/repeated/concurrent behavior and observable acceptance where relevant. Identify material architecture/data choices, verified sources, assumptions and unknowns. Preserve the stack and confirmed domain rules.

For distinct capabilities, sketch responsibilities and actual dependencies. Organize coherent changes with consumers rather than a fixed file budget or recursive specification hierarchy. Elaborate a module only when it helps implementation.

## Approval and storage

Planning stays read-only and in chat until corresponding writes/execution are approved. Present the scope and material choices before dependent execution. Valid approval continues across routine phases and repairs; do not force a turn to end, a spec to be saved or approval to repeat solely because a phase ended.

Use the existing authorized spec/task/tracker and writer. Do not automatically create SPEC.md, a tasks directory or competing checklists. Keep material decisions current without copying chat history.

## Handoff

Identify the first complete change, affected layers/callers, acceptance and checks. Use planning-and-task-breakdown only if organization is still needed. Developer tests accompany code; review/CI evaluates completed changes; QA/human checks usable flows. Apply [failure handling](../../../docs/team-workflow.md#failures-and-blockers) for material missing decisions or unsafe dependencies. Routine bugs do not restart specification.

Return an agreed requirement or a concrete decision with impact/recommendation. A written spec is not implementation, runtime proof, human acceptance or release authority.
