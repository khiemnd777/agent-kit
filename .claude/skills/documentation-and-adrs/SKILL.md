---
name: documentation-and-adrs
description: Update changed contracts and usage instructions, or record the rationale for a significant architecture decision in the project's existing documentation.
---

# Documentation and ADRs

Use the [lean operating core](../../../AGENTS.md). Produce documentation that helps someone use, maintain or resume the affected work. A code change does not automatically need an ADR, changelog entry or new task record.

## Choose the smallest useful record

Identify the reader and the question the document should answer. Inspect the existing relevant instructions or decision record, then update that location. Prefer one maintained source over parallel explanations in a README, spec, ADR and task file.

Use an ADR for a significant choice whose constraints, alternatives or consequences would otherwise be lost, especially when reversal is expensive or the project requires a decision record. For a routine local fix, an explanatory comment, updated example or concise handoff may be sufficient. Do not reconstruct old decisions or invent approval history to populate a template.

When an ADR is appropriate, follow the established directory, format, numbering and status convention. Capture the actual problem, decision, important alternatives and consequences. Distinguish a proposal from an accepted decision. Preserve superseded decisions as history and link the replacement where the project expects it; historical records are not current instructions.

## Document the changed behavior

- Update setup or operating commands only when the task changes them. Derive commands from the project and state prerequisites; example commands are not permission to install, configure or deploy.
- Keep changed public contracts understandable: inputs, outputs, meaningful errors, constraints and compatibility effects. Use the project's existing types or documentation tooling.
- Explain non-obvious reasons and constraints near the relevant code. Avoid comments that repeat syntax or promise behavior the implementation does not provide.
- Update agent-facing rules only when the requested work intentionally changes a convention. Preserve domain and permission boundaries.
- Record a gotcha or recovery instruction where a future reader will need it. Link existing evidence rather than copying logs or secrets into the document.

## Maintain rules, state and skill evidence

Keep durable rules in AGENTS.md, stable design in project-context.md, outcomes in project-plan.md and the single live summary in project-state.md; link detailed task/decision history. Within authorized writes the owner proactively updates affected entries at approval/scope changes, results, blockers/stops and handoff, without a reminder or scheduler. Save actual phase contributions using the [journal](../../../docs/engineering/skill-usage/README.md); do not save unapproved/read-only planning or invent measurements/approvals.

## Verify and finish

Compare the changed explanation with the implementation or other actual evidence. Check affected links, examples and commands to the extent relevant and authorized; distinguish reviewed syntax from commands actually executed. Do not claim a runtime result merely because documentation describes one.

Stop when the requested audience can understand the changed behavior or decision and relevant contradictions are resolved. Unrelated documentation debt is separate work. A long task may reuse its existing checkpoint; this skill adds no reporting cycle.

Read [detailed techniques and examples](references/detailed-guide.md) for ADR, API, README or changelog formats only when one is needed.
