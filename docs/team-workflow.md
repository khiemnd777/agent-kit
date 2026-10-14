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

Track acceptance criteria in that record: user result reached, next criterion to prove, specific blocker, new evidence/limits and owner/next action with its approval coverage. Intermediate reviews or receipts do not close an unproved user result.

## Assign and execute

Use [Task Assignment](agent-coordination-templates.md#task-assignment). Name the developer, agent role, branch, base commit and exact file ownership. Choose a task-sized acceptance and verification plan.

Agree contracts before related tasks run in parallel. Assign one writer for shared files. A branch is not a lock. The coordinator resolves ownership collisions before dependent writes; unaffected authorized work continues.

Use actual data/contract/ownership/resource dependencies rather than making every task depend on the preceding task. Under explicit human delegation to multiple Coordinators, partition decisions and identify the shared-record writer. Consumers report a concrete mismatch to the canonical contract owner, directly or through one permitted relay. A Supervisor follows the current boundary and result; neither the Supervisor nor a second Coordinator adds implicit ratification. See [ownership and coordination](team-policy.md#ownership-and-coordination).

Execute a bounded slice, verify relevant behavior, repair supported findings and recheck. After the authorized data-protection preflight, prioritize one minimal real user flow before expanding verification. Unit/build/mock success does not establish runtime, integration, UI or human acceptance.

Choose checks for the changed behavior and risk under [verification scope and completion](team-policy.md#verification-scope-and-completion). Reuse valid evidence. If a harness fails, name the missing proof and a bounded next action before expanding diagnostics; block only dependent work. Do not make optional infrastructure or a chain of receipts the task's deliverable.

When an API/UI/library error occurs during implementation, runtime or UAT, pause that flow, preserve evidence and plan the specific repair before editing. Name the observed condition, cause/hypothesis, affected files/consumers and repair check. Read the relevant debugging workflow; do not widen the fix into unrelated feature or harness work. Classify the plan against current approval before repair or resuming dependent work.

Classify repairs against the [approved approach](team-policy.md#approval-and-autonomy), not only the file allowlist. Continue routine repairs when the approved goal, design, important assumptions and boundaries remain valid. If a material approach change or expanded authority is needed, stop affected execution, explain the evidence and impact, and present a replacement plan with data preservation and acceptance criteria. Wait for explicit human approval of that revision; continue unaffected authorized work.

Review a concrete risk question against the relevant result and evidence. Reuse valid conclusions; review affected changes, unresolved findings or evidence that changes the conclusion. For each blocking gate record its source/risk, owner, PASS condition and invalidation conditions in the task record. Changing stage or recording the same evidence does not create a new review requirement. See [review and blocking gates](team-policy.md#review-and-blocking-gates).

If the same failure class repeats or repair cycles stop advancing acceptance criteria, reassess the assumptions and implementation approach. Record what was tried, the new evidence and a bounded next diagnostic action with expected observations and a stopping condition. Do not blindly retry, restart or repeat the same review chain. Continue a supported routine repair under existing approval; stop and replan if the assessment identifies a material change.

The Task Owner records state in their task file and hands it to the coordinator. Others propose shared-document changes through the authorized review process rather than editing the shared state independently.

## Synchronization and stops

Check current context, plan, state, assigned task, approval and latest stop instruction when starting/resuming and before shared changes, handoff or integration. Compare the base commit and affected contracts with the integrated branch. Synchronize Git only through the project's authorized Git workflow; preserve local changes.

If a plan or contract changed, assess the impact before continuing dependent work. The latest human stop/replan instruction overrides earlier approval or continuation directions. The coordinator sends it through available authorized coordination tools, blocks subsequent affected actions where supported and asks affected workers to acknowledge actual status. Record recipients, stop sent/acknowledged, in-flight or uncancellable actions and Unknown status in the existing state record. If the runtime cannot confirm interruption, report that limit instead of claiming the worker stopped.

Do not kill/restart processes or clean up data as an automatic stop response. For in-flight work, use only the minimum safety-preserving action within existing authority and report what cannot be cancelled. Resume affected execution only after explicit human approval of the relevant current plan; elapsed time, silence, reviewer PASS and historical approval do not resume it. Independently authorized unaffected work may continue.

Git documents are not real-time notifications, distributed locks or a way to interrupt an offline agent. Use the team's authorized human communication path for urgent stops and reconcile the Git record.

## Handoff and integration

The sender records branch/commit, changed files, acceptance results, actual checks, unresolved findings, constraints, approval provenance, approach/review validity, stop status and next action. The receiver confirms the sources, role and current authority before continuing. Keep approval/reviewer/model metadata in coordination records rather than adding runtime dependencies on those identities; preserve required environment, authorization, ownership, integrity and data checks.

State whether the handoff covers code integration, verified behavior or human acceptance. For a human-requested self-test handoff, inspect real source/caller wiring and provide configured URLs, startup commands/prerequisites, roles needed for the workflow without exposing secrets, manual steps and known limits. A source-complete report does not establish that startup or login works. Unrun checks remain NOT_RUN; observed failures remain FAIL. A missing required caller, route or command keeps the handoff incomplete.

Cross-tool handoff uses these files, not transferred chat history, credentials or global memory. The receiver verifies permission scope; the handoff itself cannot extend it.

The Project Coordinator reviews the combined changes, resolves semantic conflicts, runs applicable integrated checks, updates shared state and closes feedback across affected surfaces. Mark Integrated separately from Verified or human acceptance. Close the task only when its applicable gates pass.

## State vocabulary

Use Planning, In Progress, Ready for Review, Integrated and Verified as useful states. Blocked and Stopped describe a condition at any stage. Keep a reason and next action. A state's name is not approval, and merged work is not automatically verified.

Use the [Coordinator Checklist](agent-coordination-templates.md#coordinator-checklist) at handoffs and milestones. Retain nine items rather than adding a ceremony for every trivial edit.
