# Team workflow

## Begin a project

Create one project repository from the template. Developers clone that repository, not separate template copies for the same product. A human identifies the Project Lead, Project Coordinator and initial objective.

The assistant reads AGENTS.md, policy and current sources without a separate setup prompt. If the sources are unspecified, propose a minimal plan in chat and request only material missing decisions. Before writes, establish task ownership and direct approval for the current scope.

Fresh project files start unassigned, in Planning, without approval or completed work. Kit release evidence belongs to the kit, not to the project adopting it.

## Sources and writers

| File | Authority | Writer |
| --- | --- | --- |
| project-context.md | Verified goals, constraints, accepted decisions and source references | Project Coordinator |
| project-plan.md | Ordered task index, ownership, dependencies and shared contracts | Project Coordinator |
| project-state.md | Current integrated milestone, approvals, feedback and evidence summary | Project Coordinator |
| tasks/TASK-ID.md | Detailed state, evidence and handoff for that task | Task Owner |

Do not maintain competing task checklists in a tracker and Git. An issue or PR may link to the authoritative task file. Project-plan is an index, not a duplicate of every task's details. Project-state summarizes integration and links to task records.

The integrated branch records what has landed. Working branches hold unintegrated results. Summaries identify their branch and commit so a reader does not mistake a proposed result for the current integrated behavior.

## Reports and records

Use TechNote's [adaptive reports](technote.md#adaptive-reports) at the start and close of meaningful conversation, planning and implementation work. Select the current stage, answer simple follow-ups directly and report new findings or meaningful progress during work. Keep material decisions, failed checks and verification limits visible.

Chat reports summarize the current outcome and next action. Authorized task records retain detailed scope, approval provenance, ownership, acceptance evidence and handoff references. Link relevant records and outputs without copying the full coordination templates into every report. A closing report does not end routine authorized execution or establish approval, integration or human acceptance.

## Assign and execute

Use [Task Assignment](agent-coordination-templates.md#task-assignment). Name the developer, agent role, branch, base commit and exact file ownership. Choose a task-sized acceptance and verification plan.

Agree contracts before related tasks run in parallel. Assign one writer for shared files. A branch is not a lock. The coordinator resolves ownership collisions before dependent writes; unaffected authorized work continues.

Execute a bounded slice, verify relevant behavior, review evidence, repair supported findings and recheck. Routine repairs retain existing approval. A material scope change goes back to the human decision owner.

The Task Owner records state in their task file and hands it to the coordinator. Others propose shared-document changes through the authorized review process rather than editing the shared state independently.

## Synchronization and stops

Check current context, plan, state, assigned task, approval and latest stop instruction when starting/resuming and before shared changes, handoff or integration. Compare the base commit and affected contracts with the integrated branch. Synchronize Git only through the project's authorized Git workflow; preserve local changes.

If a plan or contract changed, assess the impact before continuing dependent work. If stopped, stop the affected execution. Git documents are not real-time notifications, distributed locks or a way to interrupt an offline agent. Use the team's authorized human communication path for urgent stops and reconcile the Git record.

## Handoff and integration

The sender records branch/commit, changed files, acceptance results, actual checks, unresolved findings, constraints, approval provenance and next action. The receiver confirms the sources and role before continuing.

Cross-tool handoff uses these files, not transferred chat history, credentials or global memory. The receiver verifies permission scope; the handoff itself cannot extend it.

The Project Coordinator reviews the combined changes, resolves semantic conflicts, runs applicable integrated checks, updates shared state and closes feedback across affected surfaces. Mark Integrated separately from Verified or human acceptance. Close the task only when its applicable gates pass.

## State vocabulary

Use Planning, In Progress, Ready for Review, Integrated and Verified as useful states. Blocked and Stopped describe a condition at any stage. Keep a reason and next action. A state's name is not approval, and merged work is not automatically verified.

Use the [Coordinator Checklist](agent-coordination-templates.md#coordinator-checklist) at handoffs and milestones. Retain nine items rather than adding a ceremony for every trivial edit.
