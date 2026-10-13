# Agent Kit

Shared instructions, 17 skills and three native agents for software teams using Codex and Claude Code.

Agent Kit keeps project decisions, ownership and handoffs in Git so developers can continue work without repeating the conversation. It does not choose an application stack.

**Version:** 0.1.0 preview. Static package checks are recorded in [verification results](docs/verification-results.md). Native discovery, effective model/permission behavior and two-machine collaboration are **NOT_RUN**. The package is designed for both tools; runtime compatibility is not yet verified.

## Quick start

1. Select **Use this template** on GitHub and create **one repository for your project**.
2. Each developer clones that repository and opens its root in Codex or Claude Code.
3. Give the assistant your actual project goal or task. No separate setup prompt is required by the kit. The intended startup behavior must still be verified on your client.
4. Review the proposed scope, owners and acceptance criteria. Give a direct human **Approved** for the scope you want executed.
5. The designated Project Coordinator maintains shared documents. Task Owners maintain their own task records and branches.

For an existing project, review the kit's instructions against the project's current rules before adoption. Integrate relevant rules rather than overwrite existing instructions.

Codex uses [AGENTS.md](AGENTS.md), `.agents/skills/` and `.codex/agents/`. Claude Code uses [CLAUDE.md](CLAUDE.md), `.claude/skills/` and `.claude/agents/`. Both read the same project policy and role documents. Account access, project trust, managed policies and available tools still affect loading and behavior.

## What is included

- Sixteen pinned [engineering skills](docs/skills-catalog.md) plus the new TechNote skill.
- The [four-level TechNote method](docs/technote.md), including [adaptive before-and-after reports](docs/technote.md#adaptive-reports) for conversation, planning and implementation.
- Three [coordination templates](docs/agent-coordination-templates.md): Task Assignment, Project/Task State and a nine-item Coordinator Checklist.
- [Team workflow](docs/team-workflow.md), file ownership, shared state and cross-tool handoffs.
- Native `kit-explorer`, `kit-implementer` and `kit-reviewer` definitions for each runtime.
- [Model routing](docs/model-routing.md) that defaults to the developer's selected model.
- A [verification guide](docs/verification-guide.md), manifest and explicit evidence limits.

## Project sources

| Source | Purpose | Writer |
| --- | --- | --- |
| [Project context](docs/project-context.md) | Goals, constraints, decisions and sources | Project Coordinator |
| [Project plan](docs/project-plan.md) | Task index, ownership, dependencies and contracts | Project Coordinator |
| [Project state](docs/project-state.md) | Current integrated status, approval references, feedback and evidence | Project Coordinator |
| [Task records](docs/tasks/README.md) | Task-specific state and handoff | Assigned Task Owner |

The initial documents are intentionally unassigned and in Planning mode. They contain no approval, completed project work or copied test results. Replace unspecified fields only with verified project information or clearly identified proposals.

## Two-developer example

**Example, not an approved project:** Developer A uses Codex on a bounded documentation task. Developer B uses Claude Code on a separate task. The Project Coordinator agrees ownership and a shared interface first. Each owner records the branch, base commit, acceptance evidence and next action. The coordinator reviews and verifies the combined result before marking it integrated.

The tools do not share chat history or automatically control each other. Cross-developer coordination uses Git documents and the team's authorized review process. Git state is not a real-time message or distributed lock.

## Defaults and limits

Documentation and explanations default to English. An explicit user language request takes precedence for that request. Preserve exact project labels and identifiers.

The coordinator is the main session, not a subagent registered by its name. Native child agents inherit model selection intent; runtime overrides can change the effective model. Report requested and observed settings separately.

Reviewers and explorers remain read-only. Model selection does not grant execution, Git, publication or production permission. Planning does not write files or assign writers.

The kit includes no application dependencies, model/provider credentials, hooks, automatic installers, MCP services or global configuration. Extra presentation tools for TechNote Levels 3 and 4 are not bundled.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). New kit content is MIT licensed under [LICENSE](LICENSE).

The sixteen engineering skills and their references come from [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills/tree/1401c8b8030e023baeebb31781a6653fe8e93026), pinned without source edits. Their original MIT copyright and permission notice are retained in [.agents/ADDY-AGENT-SKILLS-LICENSE](.agents/ADDY-AGENT-SKILLS-LICENSE) and its Claude mirror. Original upstream examples are governed by the kit's [policy overlay](docs/team-policy.md#upstream-workflow-overlay).
