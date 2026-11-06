# Skill provenance and historical maintenance

This is for kit maintainers, not required reading for application tasks.

## Provenance

The sixteen engineering skills derive from 26 instruction-only files at [addyosmani/agent-skills commit 1401c8b8030e023baeebb31781a6653fe8e93026](https://github.com/addyosmani/agent-skills/tree/1401c8b8030e023baeebb31781a6653fe8e93026). Twenty-three canonical upstream files are adapted: all sixteen entrypoints plus definition-of-done, orchestration-patterns and the accessibility, observability, performance, security and testing references. Three upstream files retain original bytes: the MIT notice and the hardening/optimization pattern references. Original origin/pin/blob metadata remains in the manifest; adaptation means maintained local content, not byte equality with the original blob.

### Historical adaptations

Historical authority and maintenance evidence: [KIT-CONTINUOUS-WORKFLOW-001 v1 / TASK-007](tasks/TASK-007.md). Nine process-oriented skills were rewritten as focused aids, seven technical entrypoints route to the same workflow, and shared completion/orchestration/template references align with continuous delivery. Developer-owned fast tests, completed-change review/CI and usable-flow acceptance replace per-edit approval/review cycles. Normal in-scope test/config repairs remain developer work; shared infrastructure faults have an owner. No new harness is part of this task.

The approved eight-finding correction in the same task adds a tooling stop when a focused repair cannot restore the original blocked checkpoint, even if errors/configuration change. It removes blanket framework research/preference questions, repeated security approval, mandatory RUM/CI/telemetry platform setup, line-count refactors, commit prerequisites and routing to absent skills. Source-driven and observability discovery descriptions now match those narrower purposes. Actual project security, correctness and release requirements remain binding; source checks do not prove agent behavior or speed.

The subsequent approved seven-finding correction scopes local security checks, UI viewports/warnings and documentation to the affected change. It removes the invalid standalone axe-core command and the automatic three-level props refactor, classifies red checks before undoing a performance change, and permits retiring tests only for evidenced obsolescence/duplication with required coverage preserved. Existing release requirements and the earlier tooling stop remain unchanged. The same task records this correction and its actual verification limits; no additional workflow or harness is introduced.

The approved two-conflict follow-up aligns the security checklist with the skill's supported Lax/Strict cookie choices under the established session/CSRF policy. Observability now inherits project severity names, levels and routing; page/ticket illustrate urgency rather than mandate a two-level schema. An approved Strict cookie or existing alert scheme does not require a configuration migration to satisfy these references. Scope, release requirements and the earlier tooling stop remain unchanged.

All task records above describe historical maintenance. Their tooling cutoff and compulsory workflow wording are superseded by the lean core. Earlier changes in TASK-004, TASK-005 and TASK-006 are historical provenance. Their former workflow/four-boundary wording is superseded by the current workflow, not an additional set of instructions. Approved-template fidelity criteria remain relevant under that workflow. TechNote and template-application are kit-owned content with matching mirrors.

[The manifest](skills-manifest.json) records sources/digests/mirrors. Written/structurally checked files do not prove native discovery, invocation or workflow compliance; see [verification results](verification-results.md).

## Lean refactor — 2026-11-05

The owner approved source refactoring, package checks, a separate branch and review PR, plus preparation of a Codex pilot. Merge, adoption in other projects and native pilot execution are outside this task. The current [core](../AGENTS.md) and workflow replace historical mandatory preload/records and the one-repair cutoff with proportionate effort, relevant evidence and progress-based stopping.

Seven long technical entrypoints now route to optional detailed guides. Those guides are derived from the corresponding pinned upstream entrypoint, with local scope/wording adaptations; their manifest `origin.derived_from` preserves the original repository, commit, path and blob identity. They are additional local splits, not new upstream files. The original 26 upstream identities remain 23 adapted and 3 byte-original; no upstream version bump is implied. Canonical and Claude mirrors share the same bytes and provenance.

The catalog now routes skills without maintenance history. TechNote defaults to a short explanation; its extended media guidance is optional. Native model/tool/permission inheritance is retained. [Verification results](verification-results.md) record actual source/package evidence; [pilot handoff](codex-pilot-handoff.md) specifies the unrun runtime comparison. Smaller source entrypoints are not measured token or elapsed-time savings.

## Approved workflow and journal overlay — 2026-11-05

[TASK-008](tasks/TASK-008.md) records approval of the generalized reverse-port. The current operating core supersedes the lean refactor's direct-implementation exception: all tasks require planning and explicit approval, with concise chat plans for small work. Long/complex/UI tasks finish the approved production code and wiring before writing/updating and running tests; complex tasks investigate risks/alternatives, and UI tasks preview an ASCII mockup before approval/coding. Covered repairs retain progress-based diagnostics without repeated approval.

Skill selection is task-specific; planning/implementation report actual contributions and compact effective-source labels from authorized local journal records. Durable rules, stable context, intended outcomes and the single current-state summary are separate. The owner proactively maintains authorized records, without a scheduler/harness. Original upstream pin/blob/license identities, native fields/model/permission inheritance and fresh adoption authority are preserved. No project-specific permissions, data or historical skill usage is ported. Source/package evidence does not prove native loading, workflow compliance or improved time/token use.

## TASK-009 — source location in debugging, 2026-11-06

Approved DL01–DL04 adds a concise source-location technique to debugging-and-error-recovery: exact signals, screenshot evidence, scoped search, ownership tracing and separation of matches from causes. The technique is informed by the personal noah-fast-triage skill without importing Noah paths, identity contracts, architectural layers or approval rules. Trigger/description, 17-skill inventory, upstream pin and licenses are unchanged. Canonical and Claude mirror remain byte-identical. No separate fast-triage skill, adopter update, native pilot or Git publication is authorized. See [task/evidence](tasks/TASK-009.md).
