# Agent Kit project instructions

Read [team policy](docs/team-policy.md) for authority and safety. Use [team workflow](docs/team-workflow.md) as the single delivery workflow. Skills, examples and role documents do not add approval rounds or competing lifecycles.

## Start the assigned work

Read the assigned task and only the current project context, decisions, code and tests needed to understand it. Use verified project commands. Fresh templates contain no inherited approval.

Name one delivery owner. The main session normally owns the task from scope through implementation and handoff; a separate Coordinator or team is not required. Propose bounded ownership in chat if it is unassigned. Shared records have one explicitly assigned writer. Preserve other work.

Propose the outcome, scope, important design choices and acceptance before execution. Planning is read-only and stays in chat until writes are approved. Direct human approval covers routine implementation, local checks and repairs in its stated scope. Do not ask again per file, function, bug or phase.

## Deliver without repeated stops

Implement a complete usable change across its actual callers and layers. Write meaningful regression tests and run focused checks while coding. Submit a completed coherent change for review and configured CI on a concrete source revision. Demonstrate/accept usable flows at meaningful milestones. Release only under its actual authority.

Pause affected work for a material missing decision/expanded scope, a failure that makes dependent work incorrect or unsafe, or an action needing release/real-data authority. Always honor a human stop. Continue independent authorized work; when none remains, report the blocker and wait without inventing verification work.

Use one [task record](docs/tasks/README.md); the [templates](docs/agent-coordination-templates.md) are optional field guides. Routine repairs need diagnosis and relevant rechecks, not another plan document, review chain or approval round. Do not hide failed assertions, weaken protection or manufacture PASS.

## Skills and optional delegation

Select only relevant skills from the [catalog](docs/skills-catalog.md) and read their actual entrypoints. Technical guidance and conditional checklists apply to the task, not every edit. Keep existing stack, contracts and domain rules.

Optional native kit-explorer, kit-implementer and kit-reviewer roles follow the [role documents](docs/roles/coordinator.md) and [model routing](docs/model-routing.md). Delegate only when authorized and useful; assign inputs, files, checks, acceptance and handoff. Children do not delegate again. Explorer/reviewer return evidence without application implementation or deployment. Runtime permissions and task authority govern tools; roles do not force sandbox profiles. Disclose self-review when no independent reviewer ran.

## Explain and hand off

Use [TechNote](docs/technote.md) for meaningful updates and requested explanation levels. English is default; an explicit language request takes precedence. State the result, remaining problem, evidence/limits and next action. Do not narrate unchanged checks or copy full templates into chat.

Keep source completion, verified behavior, human acceptance and release distinct. PASS needs observed evidence; applicable unrun checks are NOT_RUN with a reason. At handoff update the owned task record, review the final diff and report actual checks and remaining work. No automatic commit/push, publication, global configuration, production operation or destructive cleanup.
