# Acceptance handoff templates

Use these templates directly in the conversation under the [core](../AGENTS.md). Localize prose, labels and controls to the user's conversation language. Bracketed fields are placeholders, not evidence. The templates add no runtime harness, universal test checklist or execution authority.

## Classification

At the start of every plan, including small tasks, state directly in chat:

```text
Delivery type: One handoff / Roadmap
Rationale: Why the result can be accepted together or needs separate rounds
Parent roadmap: Name/ID and current package if applicable, or None
```

The user/Product Owner approves classification with the plan; do not add a separate approval round. Classify by how the result can be accepted, not by file count, lines of code or estimated duration. Apply these criteria in order:

1. **Parent roadmap first.** Work belonging to an agreed roadmap retains roadmap delivery, its overall position and its acceptance stops, even when the current package is small. Do not silently reclassify it as standalone work to bypass a stop. Covered repairs stay within the current package rather than inventing a new package.
2. **Separate acceptance rounds.** Use roadmap delivery when distinct workflows, user groups or outcomes need separate review, or acceptance/decisions in an earlier result affect later work. Multiple files or modules alone do not justify splitting. Define the meaningful packages, their outcomes, dependencies and observable acceptance before implementation.
3. **One complete assessment.** Use one handoff when the work is outside a parent roadmap, scope is clear, its checklist is focused and the complete result can be assessed together in one review. Do not invent phases to fill a template.

If evidence is insufficient, continue authorized read-only investigation and present the classification with its rationale before implementation. Material scope growth requires an amended plan/classification before expanding work; do not silently change delivery type to cross an acceptance stop.

Risk is a separate axis. A small permission fix may use one handoff and still require authorization/security checks. Neither type grants publication, migration or real-data authority.

| Example | Delivery type | Rationale |
| --- | --- | --- |
| Correct a login error message outside a roadmap | One handoff | The result and affected flow can be assessed together |
| Records, bulk import and approvals requiring separate acceptance | Roadmap | Distinct results need planned acceptance rounds |
| A small package already inside an agreed roadmap | Roadmap | Retain the parent picture and stops regardless of size |
| A bounded permission fix outside a roadmap | One handoff | One assessment; relevant permission checks remain required |

Examples illustrate classification only; they are not approved product scope or observed agent behavior.

## Common evidence and presentation rules

- Keep the main handoff concise; link detailed files, logs and checks instead of pasting them. Retain the core WHAT and skills tables and 1–3 concrete next-step options with conditions/authority.
- Both types show an **actual result image or a technical diagram grounded in delivered work** directly in chat. Use images for observed UI/output and diagrams for actual structure, data or processing, including documentation tasks. Prefer short labels and a wordless presentation while retaining essential annotations.
- Caption the visual with the delivered revision/snapshot, relevant source, evidence status and limits. Without Git, identify the task/package and document version; never invent a commit. Mark **Verified**, **Proposed** and **Unknown** content accurately. A visual may contain more than one evidence status.
- Images must be actually observed results; diagrams must be checked against current source, documents or observations. Mockups and AI images are not runtime evidence. Redact sensitive data.
- If the required actual visual is unavailable, state **UNAVAILABLE** with a reason. Do not fabricate a substitute or claim full acceptance readiness while required evidence is missing.
- Prefer 3–5 focused acceptance checks, adjusted to risk. Each names an action/observation and expected result. Images alone do not prove permissions, isolation, transactions or other hidden properties; use appropriate technical evidence.
- Distinguish source completion, behavior verification, human acceptance and release. Explain FAIL/NOT_RUN and its impact; technical PASS does not mean human acceptance.

## 1. Roadmap delivery: one meaningful package at a time

Keep preplanned package IDs/names/order and plan revision in [project-context](project-context.md), detailed intended outcomes/dependencies/acceptance in [project-plan](project-plan.md) and the sole live summary in [project-state](project-state.md). Do not create a new package B only after completing A. Unconfirmed work has an explicit decision point and is not authorized for implementation; material changes require plan approval.

Packages represent usable outcomes or coherent flows, not individual files or disconnected UI/API/database layers. Within each approved package, complete production code and real wiring before writing/updating and running tests, then verify and hand off. This does not mean writing the whole roadmap before testing its first package.

### [Package ID / name / delivered revision]

**Overall picture: names only, from the agreed plan**

```text
Accepted:            [Names actually accepted by the user/Product Owner]
Awaiting acceptance: [Current package name]
Next:                [Next preplanned package name]
Later:               [Remaining preplanned names in order]
```

Identify in-progress/blocked work accurately rather than calling it accepted. Do not infer completion percentage from package count; packages can differ in size.

**Actual result image / technical diagram**

[Render the visual here. Caption: revision/snapshot, source, Verified/Proposed/Unknown content and limits.]

**Outline**

- Result: [Completed capability/flow].
- Components: [Relevant UI/API/data/integrations or documents].
- Rules and limits: [Key invariants, omissions and unverified parts].

**Acceptance checklist**

- [ ] [Action/observation] -> [Expected result].
- [ ] [Important exception] -> [Expected result].
- [ ] [Connection to earlier work] -> [Expected result].

**Technical evidence**

| Check / command / snapshot / environment | Actual result and limits | Evidence |
| --- | --- | --- |
| [Check] | [PASS / FAIL / NOT_RUN, with reasons for missing evidence] | [Link] |

**WHAT**

| Name | Purpose | Location | Status | Reason if undone/ignored |
| --- | --- | --- | --- | --- |
| [Stable task item] | [Outcome] | [File/view/module] | [Actual status] | [Reason or em dash] |

**Skills:** [Core skills table derived from the authorized saved journal; disclose chat-only planning when applicable].

**User/Product Owner decision:** [Accept / Changes requested / Stop].

**Next-step options:** [1–3 concrete choices, expected outcomes and required authority; the next roadmap package must already be in the agreed plan].

**Stop:** repair defects within current authorized package scope. Do not open the next package until the user/Product Owner accepts the current result **and** authorizes continuing. One explicit instruction may cover both; silence and overall-roadmap approval do not replace it. Optional checkpoints do not replace this acceptance stop.

## 2. One handoff: standalone bounded work

Omit the overall-picture block and artificial phases. Next-step options are not permission to start another task.

### [Task name / delivered revision]

**Outline**

- Result: [Change and problem addressed].
- Scope: [Affected components].
- Limits: [Missing or unverified parts, if any].

**Actual result image / technical diagram**

[Render the visual here. Caption: revision/snapshot, source, Verified/Proposed/Unknown content and limits.]

**Acceptance checklist**

- [ ] [Action/observation] -> [Expected result].
- [ ] [Related impact] -> [Expected result].

**Technical evidence**

| Check / command / snapshot / environment | Actual result and limits | Evidence |
| --- | --- | --- |
| [Check] | [PASS / FAIL / NOT_RUN, with reasons for missing evidence] | [Link] |

**WHAT**

| Name | Purpose | Location | Status | Reason if undone/ignored |
| --- | --- | --- | --- | --- |
| [Stable task item] | [Outcome] | [File/view/module] | [Actual status] | [Reason or em dash] |

**Skills:** [Core skills table derived from the authorized saved journal; disclose chat-only planning when applicable].

**Next-step options:** [1–3 concrete choices with outcomes and required authority; when complete, reviewing/accepting the result can be the single next option].
