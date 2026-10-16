---
name: planning-and-task-breakdown
description: Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel work is possible.
---

# Planning and Task Breakdown

Follow the [single team workflow](../../../docs/team-workflow.md). This skill organizes work; it does not create another tracker, checkpoints or approval rounds.

## Trigger and inputs

Use when dependencies or acceptance need clarification. Skip a separate planning exercise if the current approved task already answers them. Read the outcome, relevant source/design decisions, actual constraints and authority.

## Make an executable plan

- State behavior and observable acceptance, including relevant permission, invalid-input, repeated/concurrent action and error cases.
- Identify affected layers/callers/data and material design choices. Resolve important missing decisions before dependent work.
- Split large work into small complete capabilities or coherent technical changes with real consumers. File/line counts are estimates, not mandatory split/review gates.
- Name one delivery owner and only real contract, ownership or resource dependencies. Optional parallel work needs agreed interfaces and disjoint files, not a default Coordinator/Supervisor team.
- Select focused developer tests, configured CI and acceptance of usable flows at meaningful milestones. No gate after every file or phase.
- Identify release/real-data actions needing separate authority; routine repairs remain within valid task scope.

## Record once

Planning stays in chat. With write authority use the existing task/spec/tracker and its writer. Do not create a second plan or overwrite another unfinished task. The [field guide](../../../docs/agent-coordination-templates.md#task-assignment) is optional.

For an approved template, record its identity, retained structure and approved differences; use the [template reference](../../references/template-application.md) for relevant rendered criteria. Uncertain replicated design choices may need early developer feedback, not a gate after every edit.

## Output

Identify the first complete change, its acceptance/checks and material missing decisions. Once the current scope is approved, continue covered work without per-step approval. Update the same task with results, blockers and next action.
