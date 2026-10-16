---
name: using-agent-skills
description: Discovers and invokes agent skills. Use when starting a session, or when you need to decide which skill or workflow applies to the piece of work at hand. This is the meta-skill that governs how all other skills are discovered and invoked.
---

# Using Agent Skills

[Team workflow](../../../docs/team-workflow.md) owns delivery. Skills are optional technical aids, not mandatory lifecycle hops, approval gates or reasons to create agents.

## Select relevant material

Read the assigned outcome and relevant project sources. Choose only skills whose techniques help the actual task from the [catalog](../../../docs/skills-catalog.md), read their entrypoints and relevant references, then return to the work. Do not preload all skills, run a catalogue-wide sequence or route through missing skills/invented slash commands.

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

Preserve the current stack, ownership and authority. Planning stays in chat until writes are approved. Existing approval covers routine phases/checks/repairs within valid scope; a skill adds no approval round. Pause only affected material decisions, unsafe dependencies or actions needing unavailable authority, and always respect human stops. Continue independent work or hand off the waiting state.

Identify effective sources when names collide; do not silently substitute or edit global settings. The output is the user's result or an evidence-backed answer, not completion of a skill sequence. Report checks and limits without inferring runtime, acceptance or release from static evidence.
