# Skills catalog

Seventeen optional technical skills are available. The [lean core](../AGENTS.md) governs delivery; skills do not grant authority or replace the required planning → approval → implementation workflow. Choose only the skill whose techniques resolve a **current** need; do not preload a catalog or start every session with a meta-skill.

| Need | Skill |
| --- | --- |
| Important requirements or design choice unclear | spec-driven-development |
| Real dependencies need task ordering | planning-and-task-breakdown |
| A change benefits from vertical slices | incremental-implementation |
| Missing context on resume | context-engineering |
| Changed behavior needs regression coverage | test-driven-development |
| A concrete defect or blocker | debugging-and-error-recovery |
| A coherent completed diff needs review | code-review-and-quality |
| Evidence-backed simplification | code-simplification |
| Material API/contract choice | api-and-interface-design |
| UI behavior, accessibility or approved visual fidelity | frontend-ui-engineering |
| Unfamiliar/version-sensitive external interface | source-driven-development |
| Actual trust/data/permission boundary | security-and-hardening |
| Measured performance issue or explicit target | performance-optimization |
| Missing signal for an operational question | observability-and-instrumentation |
| Material architecture/contract/operations documentation | documentation-and-adrs |
| Requested TechNote medium or substantive explanation | technote |
| Help selecting a skill | using-agent-skills |

During planning, select the minimum sufficient skills for task type, boundaries, risks and outcome; state brief reasons. Read selected `SKILL.md` files before applying them, then only the relevant reference sections. Close planning and implementation with actual contributions and compact source labels (Personal / Repo / UNKNOWN), estimates totaling 100% among applied skills, and the [authorized journal record](engineering/skill-usage/README.md). No skill used means say so; reading alone is not contribution. Estimates are not effectiveness scores or measured resource use. A file count or session start alone does not trigger a skill. The project determines stack, checks and permissions. See [runtime compatibility](agent-compatibility.md).

**Maintainers:** [provenance, upstream pin and historical adaptations](skills-provenance.md), [manifest](skills-manifest.json), [verification guide](verification-guide.md).

## Provenance

Maintenance history, the pinned upstream source and adaptation details are in [skill provenance](skills-provenance.md); they are not required context for application tasks.
