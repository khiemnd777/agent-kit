# Agent Kit — lean operating core

Read the assigned task and relevant source first. This is the default instruction entrypoint; consult [policy](docs/team-policy.md), [workflow](docs/team-workflow.md), [skill catalog](docs/skills-catalog.md) or role detail **only when the current task needs it**. Links are not mandatory reading or additional gates.

## Authority and autonomy

A clear request to implement/fix authorizes necessary local investigation, edits and focused checks within its scope and runtime permissions. A planning-only or review request does **not** authorize implementation. Main session owns delivery by default; no repeated approval for each file, bug or phase.

Ask for a material missing decision, expanded scope or an operation needing additional authority. Git commits/push/PR, deployment, production/real-data changes, paid, destructive and external operations retain their actual permission boundaries. Respect human stops and others' work; tools and records never grant authority.

## Proportionate delivery

- **Focused:** clear contained low-risk change. Implement directly, inspect diff, run relevant checks and hand off concisely. No mandatory task file or extra agent.
- **Standard:** feature/bug crossing meaningful seams. Complete callers/integration, use targeted regression checks and a checkpoint if continuation needs it.
- **Sensitive:** authorization, private data, payments, migrations, production or irreversible changes. Preserve actual risk-boundary checks and project-required review.

Risk—not number of files or task duration—determines effort. Preserve project domain rules, stack, contracts, existing data and security.

## Continue, stop and hand off

Use existing project commands and tests relevant to the change. Fix evidenced defects within scope, recheck affected inputs and reuse unaffected evidence. Never weaken assertions, invent PASS, or create a runner/review orchestration project incidentally.

Continue diagnostics only while a concrete hypothesis, evidence and progress justify the cost. If attempts stop helping, change strategy or hand off a blocker. **Stop once required acceptance and appropriate verification are met; optional polish/refactors are separate.**

For long/delegated work keep [one checkpoint](docs/tasks/README.md) only when useful: outcome, done/todo, decisions, revision, checks/limits and next action. Resume rather than restart unaffected work. Skills and delegation are optional; children do not delegate.

Report result, observed checks, limits and next action if any. Use concise [TechNote Level 1](docs/technote.md) by default. Distinguish source complete, behavior verified, human accepted and released. Required unrun checks are NOT_RUN; no automatic publication or release.
