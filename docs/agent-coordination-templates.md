# Coordination templates

Optional field guides for the [single team workflow](team-workflow.md), not additional documents or approval gates. Use the existing task/issue and omit fields that do not affect the task. One task has one delivery owner; each shared record has one assigned writer. Keep detailed evidence here rather than repeat it in chat.

## Task Assignment

```text
Task / owner:
Outcome and acceptance:
Relevant decisions / source revision:
Approved scope / human approval source / latest stop:
Owned files and any real dependencies:
Approach and applicable checks:
Result to hand off:
```

For a small fix this can be a short paragraph in the existing issue. For material design/data/permission decisions, include enough detail for review before execution. Do not create a second plan or fill generic placeholders as product copy.

## Project / Task State

```text
Task / writer / source revision:
Current result and stage:
Authority / restrictions / latest stop:
Checks: criterion -> actual command/evidence -> PASS / FAIL / NOT_RUN + limits
Open defect or dependency: impact -> owner -> next action
Next delivery / acceptance action:
```

A project summary links existing tasks and shared decisions; it does not duplicate their checklists. Keep requested/observed model metadata only when relevant to routing evidence; Unknown for unobserved values. Model/session/agent details never become application startup conditions.

A waiting review is a state. Continue independent authorized work; if none exists, hand off and wait. A state field or technical PASS cannot grant permission or establish human acceptance.

## Coordinator Checklist

This heading is retained for existing links. These are the delivery owner's handoff questions, not a mandatory nine-step ceremony or a requirement to create a Coordinator role:

- Is the actual output complete for the agreed outcome, including its real callers/data path?
- Do the recorded checks support the claim, with failed/unrun criteria and review independence stated accurately?
- Are material feedback, current scope/stop restrictions, blockers, owner and next action clear?

Use at a meaningful handoff. Do not ask for per-file/phase approvals, restart unchanged checks or build a receipt chain to fill these fields. Keep Source complete, Behavior verified, Human accepted and Released distinct.
