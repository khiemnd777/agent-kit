---
name: planning-and-task-breakdown
description: "Organize a task whose dependencies, scope or delivery order are unclear. Use for a larger change, real parallel work or a requested implementation plan."
---

# Planning and Task Breakdown

Use the [lean operating core](../../../AGENTS.md). Organize work only as far as needed to execute it. Every task requires planning and explicit approval before implementation; small tasks can use a short chat plan without a separate document.

## Make the next change executable

- State the outcome, boundaries and observable acceptance. Include permission, invalid-input, error or concurrent behavior where relevant.
- Identify affected callers, layers, data and material design choices from source. For complex tasks investigate risks and alternatives, discuss a concrete proposal and obtain approval. For UI tasks preview an ASCII text mockup before approval/coding. Combined cases apply all relevant preparation.
- Select minimum sufficient skills with brief reasons. Report actual planning contributions and compact source labels using the journal policy.
- Plan dependency order within the approved scope. Long/complex/UI tasks complete all production code and real wiring before writing/updating and running unit or other tests; avoid per-file/function code/test cycles and artificial handoffs. Split independently approved outcomes only when actual scope/dependencies require it. File/line counts are estimates, not split or review gates.
- The main session owns delivery by default. Delegate only when the benefit exceeds coordination cost and task/runtime authority permits it; define interfaces and non-conflicting ownership.
- Choose focused checks for changed behavior and affected seams. Include existing project review/CI/release requirements at the appropriate milestone, not after every step.

A long task may need one short [checkpoint](../../../docs/tasks/README.md). Reuse an existing tracker where useful or required; do not duplicate its state or overwrite another writer's work. A planning-only task stays in chat unless its scope includes a saved artifact.

For an approved template, retain its identity and agreed differences; consult the [template reference](../../references/template-application.md) when fidelity decisions need detail.

## Finish planning

Return the first coherent change, intended checks and any material unresolved decision. Once these are clear and authorized, implement without per-step confirmation. Revise the plan when evidence changes a dependency or acceptance, not simply because a phase or session ended.
