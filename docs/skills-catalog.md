# Skills catalog

The package has 17 logical skills, each with a canonical `.agents/skills/` entrypoint and byte-identical `.claude/skills/` copy. [Team workflow](team-workflow.md) is the only delivery process; skills supply technical help on demand. They do not create approval rounds, required agents or universal checklists.

| Skill | Use when |
| --- | --- |
| using-agent-skills | Select the minimum useful available aid |
| spec-driven-development | Clarify significant requirements and material choices |
| planning-and-task-breakdown | Organize coherent changes and real dependencies |
| incremental-implementation | Implement a complete change with developer feedback |
| context-engineering | Load/resume relevant context without restarting delivery |
| test-driven-development | Test changed behavior and meaningful regressions |
| debugging-and-error-recovery | Diagnose and repair a concrete defect |
| code-review-and-quality | Review a completed coherent result |
| code-simplification | Reduce relevant complexity while preserving behavior |
| api-and-interface-design | Design contracts and module interfaces |
| frontend-ui-engineering | Implement accessible/responsive UI and approved-template fidelity |
| source-driven-development | Verify a version-sensitive/unfamiliar approach with primary sources |
| security-and-hardening | Address relevant trust boundaries and permission/data risks |
| performance-optimization | Measure and improve an actual performance problem |
| observability-and-instrumentation | Instrument behavior needed for diagnosis/operation |
| documentation-and-adrs | Record decisions, changed contracts and operations |
| technote | Explain outcomes/evidence and requested presentation levels |

## Read and route

Read the chosen entrypoint and only relevant references. Do not preload all skills or follow a lifecycle chain. Existing stack, commands, business rules and authority come from the project. Identify effective sources when names collide; do not silently substitute or change global settings. See [runtime compatibility](agent-compatibility.md).

## Provenance

The sixteen engineering skills derive from 26 instruction-only files at [addyosmani/agent-skills commit 1401c8b8030e023baeebb31781a6653fe8e93026](https://github.com/addyosmani/agent-skills/tree/1401c8b8030e023baeebb31781a6653fe8e93026). Twenty-three canonical upstream files are adapted: all sixteen entrypoints plus definition-of-done, orchestration-patterns and the accessibility, observability, performance, security and testing references. Three upstream files retain original bytes: the MIT notice and the hardening/optimization pattern references. Original origin/pin/blob metadata remains in the manifest; adaptation means maintained local content, not byte equality with the original blob.

### Local adaptations

Current authority and maintenance evidence: [KIT-CONTINUOUS-WORKFLOW-001 v1 / TASK-007](tasks/TASK-007.md). Nine process-oriented skills were rewritten as focused aids, seven technical entrypoints route to the same workflow, and shared completion/orchestration/template references align with continuous delivery. Developer-owned fast tests, completed-change review/CI and usable-flow acceptance replace per-edit approval/review cycles. Normal in-scope test/config repairs remain developer work; shared infrastructure faults have an owner. No new harness is part of this task.

The approved eight-finding correction in the same task adds a tooling stop when a focused repair cannot restore the original blocked checkpoint, even if errors/configuration change. It removes blanket framework research/preference questions, repeated security approval, mandatory RUM/CI/telemetry platform setup, line-count refactors, commit prerequisites and routing to absent skills. Source-driven and observability discovery descriptions now match those narrower purposes. Actual project security, correctness and release requirements remain binding; source checks do not prove agent behavior or speed.

The subsequent approved seven-finding correction scopes local security checks, UI viewports/warnings and documentation to the affected change. It removes the invalid standalone axe-core command and the automatic three-level props refactor, classifies red checks before undoing a performance change, and permits retiring tests only for evidenced obsolescence/duplication with required coverage preserved. Existing release requirements and the earlier tooling stop remain unchanged. The same task records this correction and its actual verification limits; no additional workflow or harness is introduced.

The approved two-conflict follow-up aligns the security checklist with the skill's supported Lax/Strict cookie choices under the established session/CSRF policy. Observability now inherits project severity names, levels and routing; page/ticket illustrate urgency rather than mandate a two-level schema. An approved Strict cookie or existing alert scheme does not require a configuration migration to satisfy these references. Scope, release requirements and the earlier tooling stop remain unchanged.

Earlier changes in TASK-004, TASK-005 and TASK-006 are historical provenance. Their former workflow/four-boundary wording is superseded by the current workflow, not an additional set of instructions. Approved-template fidelity criteria remain relevant under that workflow. TechNote and template-application are kit-owned content with matching mirrors.

[The manifest](skills-manifest.json) records sources/digests/mirrors. Written/structurally checked files do not prove native discovery, invocation or workflow compliance; see [verification results](verification-results.md).
