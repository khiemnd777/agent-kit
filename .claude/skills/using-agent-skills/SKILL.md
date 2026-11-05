---
name: using-agent-skills
description: Use only when deciding among relevant skills is unclear; do not run this meta-skill at every session start.
---

# Using Agent Skills

[Team workflow](../../../docs/team-workflow.md) owns delivery. Skills are optional technical aids, not mandatory lifecycle hops, approval gates or reasons to create agents.

## Select relevant material

When choosing a skill is genuinely uncertain, read the assigned outcome and relevant project sources. Choose only skills whose techniques help the actual task from the [catalog](../../../docs/skills-catalog.md), read their entrypoints and relevant references, then return to the work. Do not preload all skills, run a catalogue-wide sequence or route through missing skills/invented slash commands.

| Need | Aid |
| --- | --- |
| Clarify requirements | spec-driven-development |
| Organize coherent changes | planning-and-task-breakdown |
| Implement through real layers/callers | incremental-implementation |
| Refresh relevant context | context-engineering |
| Test behavior or regression | test-driven-development |
| Diagnose a concrete failure | debugging-and-error-recovery |
| Review a completed change | code-review-and-quality |
| Simplify while preserving behavior | code-simplification |
| API/UI/security/performance/observability/source research/documentation | Matching technical skill in the catalog |
| Explain results | technote |

## Authority and result

Preserve the current stack, ownership and authority. Planning-only requests stay read-only; a direct implementation request covers local edits/checks inside valid scope. Existing approval covers routine phases/checks/repairs within valid scope; a skill adds no approval round. Pause only affected material decisions, unsafe dependencies or actions needing unavailable authority, and always respect human stops. Continue independent work or hand off the waiting state.

Identify effective sources when names collide; do not silently substitute or edit global settings. The output is the user's result or an evidence-backed answer, not completion of a skill sequence. Report checks and limits without inferring runtime, acceptance or release from static evidence.
