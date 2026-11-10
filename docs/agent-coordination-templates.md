# Coordination templates

Optional field guides under the [lean core](../AGENTS.md). Use an existing tracker/checkpoint when continuation or coordination benefits; a focused task needs no new file. Omit fields that add no information. The main session owns delivery by default, and a shared record has one writer when edited.

## Task Assignment

```text
Outcome / acceptance:
Scope, ownership and relevant inputs:
Material decisions, authority limits or latest stop:
Relevant checks / result to return:
```

A short message can carry this assignment. Include enough detail for material design/data/permission decisions; reference approval of the parent plan before implementation; do not create repeated approvals for covered work. Include task type/risks, ASCII UI preview where applicable and selected skills/reasons in planning. Delegation is optional and children do not delegate.

## Conversation WHAT table

Follow [the core rule](../AGENTS.md#show-what-in-the-conversation) when presenting an implementation plan and the completed-work report. Render the table in the conversation, even if it also exists in a task file. Localize labels/statuses to the conversation language.

| Name | Purpose | Location | Status | Reason if undone/ignored |
| --- | --- | --- | --- | --- |
| W01 | Intended outcome | Affected file or component | Actual planning/approval or result status | Required for undone/ignored work; otherwise — |

Reuse item names between plan and result. This template adds no separate tracker or task-file requirement; retain the skills table and next-step options.

## Project / Task State

Use project-state.md as the single live summary and link detailed task/decision history. The delivery owner proactively updates affected state/task entries within authorized writes. For a real interruption or handoff, keep one concise checkpoint:

```text
Goal / scope / acceptance:
Done / remaining work:
Decisions / current authority limits / latest stop:
Source revision or working-tree inputs:
Actual checks: evidence -> PASS / FAIL / NOT_RUN + meaningful limits
Blocker and owner / next useful action, if any:
```

Update at meaningful milestones. A project summary links tasks instead of copying their checklists. Reuse unaffected evidence when resuming. Routing metadata belongs here only when needed to investigate model/permission behavior; unobserved values are Unknown. Model/session/agent identities never become application startup conditions.

A waiting review does not create work: continue independent authorized tasks or hand off the waiting state. No field or technical PASS grants permission or proves human acceptance.

## Coordinator Checklist

This heading remains for existing links. These optional handoff questions do not require a Coordinator or another review cycle:

- Is the requested output complete, including necessary callers and data paths?
- Do actual checks support the claim, with missing proof and review independence stated accurately?
- Are material limits, unresolved defects and any next action clear?

Close planning/implementation with actual skills (Skill | Source | Actual contribution | Estimated participation %) and 1–3 concrete next-step options with conditions/authority. Save authorized journal records first; children propose records to the owner. Unapproved/read-only planning stays in chat.

Stop when scoped acceptance and sufficient verification are met. Keep Source complete, Behavior verified, Human accepted and Released distinct. Optional polish does not extend completion.
