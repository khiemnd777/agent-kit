# Task records and checkpoints

Every task requires a plan and explicit user/Product Owner approval before implementation, even a short fix. A concise chat plan is sufficient for small work; a separate task file is optional unless project rules or useful coordination require one. A proposal is planning-only, and historical approvals do not authorize another task.

## Planning notes

The delivery owner may save bounded local planning documentation from task start under the [core rule](../../AGENTS.md#planning-only-documentation), before approval to implement. Reuse the existing `docs/tasks/<TASK-ID>.md` or assigned task record. A short task still needs no mandatory new file when there is no useful durable planning content; create a concise task record when meaningful notes or decisions need preservation, not an empty tracker per message.

Save concise updates after meaningful requirement clarifications, revisions, decisions, approvals, newly identified open questions and before a real interruption/handoff. Do not wait until planning ends or ask permission for each note. Do not dump the full conversation, logs or secrets. The record should distinguish:

| Content | Record |
| --- | --- |
| Requirement or discussion note | Relevant source, concise content, proposal/confirmed/unknown status |
| Revision | What changed, why, affected scope and superseded item |
| Decision / approval | Stable ID when useful, exact decision, actual human/source and known date; preserve history and never invent approval/timestamps |
| Open question | Unresolved point, impact and next decision needed |

Reuse current task/decision IDs. Mark an old decision superseded and link its replacement rather than silently erasing history. Approved stable design goes to project-context, intended outcomes to project-plan and current position/stop/next action to project-state, with links back to the task. Do not copy all notes into those summaries or create a second live tracker. Significant architecture choices may use the existing ADR location; this rule creates no compulsory ADR or new note hierarchy.

This is documentation permission only: a saved proposal is not implementation approval. Explicit read-only/no-file requests, human stops, assigned read-only roles, shared-record ownership and runtime restrictions take precedence. In those cases keep notes in chat and disclose unsaved status. Do not use the exception to change application code, runnable prototypes, tests, dependencies, runtime configuration, migrations, agent rules/skills or perform Git publication/external/real-data actions.

Keep durable rules in AGENTS.md, stable design in project-context.md, intended outcomes in project-plan.md and the single current-state summary in project-state.md. Detailed approvals, decisions and evidence belong in the relevant task. The delivery owner proactively maintains affected entries within authorized writes at approval/scope changes, meaningful results, blockers/stops and before handoff; children propose shared changes to the owner.

When a real interruption or handoff needs it, maintain **one concise checkpoint**: outcome/acceptance/scope, done/todo, decisions/latest stop, revision, actual PASS/FAIL/NOT_RUN checks/limits, blocker/owner and next action. Resume remaining work and reuse valid evidence. Do not create artificial pauses or checkpoints per file/function.

Record skill use at authorized planning/implementation handoffs under the [journal guide](../engineering/skill-usage/README.md). This is not a command log or second live task tracker. Bounded planning records are allowed by the core rule; explicitly read-only/no-file work must not save them. Preserve history and avoid duplicate usage on resume.

TASK-001 through TASK-007 describe historical kit maintenance, not adoption authority. [TASK-008](TASK-008.md) records the approved workflow/journal maintenance; its authorization also does not transfer to an adopting project.

[TASK-009](TASK-009.md) records approved DL01–DL04 source-location guidance in debugging; no separate skill or publication.

[TASK-009](TASK-009.md) — DL01–DL04 HUMAN ACCEPTED / CLOSED on 2026-11-06; no new scope or native pilot. Closure publication authorized on 2026-11-09; see task publication records.
