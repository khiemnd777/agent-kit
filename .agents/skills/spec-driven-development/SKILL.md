---
name: spec-driven-development
description: "Clarify unclear requirements, domain rules, interfaces or acceptance for a significant change. Use when a material product or design decision is needed before implementation."
---

# Spec-Driven Development

Use the [lean operating core](../../../AGENTS.md). Resolve the uncertainty that prevents correct implementation. A clear contained fix needs a short plan and approval, but not a separate specification document.

## Define only the needed decisions

Read existing requirements and relevant code/tests. Reuse accepted decisions instead of restating them. Identify the outcome, scope and observable acceptance. Examine actors/permissions, states, data invariants, interfaces and error or concurrent behavior only where the change affects them.

Separate confirmed requirements, inspected behavior, assumptions and open questions. An existing defect is not a business rule. Preserve the chosen stack and contracts unless changing them is part of the task.

For several distinct capabilities, sketch their responsibilities and real dependencies. Elaborate only the boundary needed for implementation; do not create a recursive hierarchy of specifications or a document for each module.

## Resolve material choices

Approval of the current plan covers routine work inside its scope. For complex tasks investigate risks/alternatives and discuss the proposal first; UI plans include an ASCII mockup. A direct implementation request does not itself approve a plan. Ask about a material missing product/design decision or additional authority when evidence cannot resolve it. Present a concrete recommendation and its tradeoff. Continue independent authorized work. A planning-only request stays within planning; saving a proposed artifact follows that request's scope.

Keep a short decision in chat for focused work. Use an existing spec/tracker or one checkpoint when a durable decision or handoff needs it. No mandatory SPEC.md, owner-naming ceremony or new approval receipt.

## Hand off to implementation

Provide the agreed behavior, affected contracts/callers and sufficient acceptance/checks to start. Stop specifying when those are clear. Routine bugs do not restart the specification process. A written requirement is not implementation, observed behavior, human acceptance or release authority.
