# Applying an approved template

Use this reference only when a human-approved task applies an internal or user-supplied template to an application. It does not authorize implementation, fixture data, permission changes or runtime access. Follow the project's approved scope and [team workflow](../../docs/team-workflow.md#applying-an-approved-template).

## Classify the source

| Source | Use |
| --- | --- |
| Internal or user-supplied template approved for the task | Preserve the agreed structure, information hierarchy, workflow order, controls, interactions and responsive behavior. Change only prototype material and differences explicitly approved for this task. |
| External design used for inspiration | Treat it as evidence for a design choice. Do not copy protected branding/content or treat its layout as an approved product requirement. |

The external-reference rule does not override fidelity to an approved template. A color or component match does not compensate for missing tabs, a changed action order or absent states.

## Before broad implementation

In the owned task record, identify:

1. Template source, version/revision and content hash; the exact screen or artifact used for comparison.
2. Map each retained template element to its target screen and position, expected behavior and acceptance evidence. Include required structure and hierarchy, navigation and action order, controls, interactions, responsive behavior and relevant states.
3. Prototype-only content or behavior to remove, and each approved difference. Resolve a material discrepancy with the human before changing the approved approach.
4. One representative screen and observable acceptance criteria using the [shared checklist](../../docs/template-application-acceptance.md).
5. Required runtime URL or route, login role, data states, inspection tools, permission scope and evidence destination. If a condition is unavailable, record NOT_RUN, owner and next action early. Do not invent data or change access to make a check pass.

## Representative screen boundary

Connect the representative screen to its real controller and data path. Compare the template and rendered implementation at the same desktop and mobile viewport sizes. Inspect the full interaction sequence and applicable populated, empty, loading, error and permission states. When the approved workflow requires it, verify that navigation retains entered data, selection and unsaved-change state; controls reflect role, disabled and busy states; and preview identifies the approved source version, whether saved, snapshot or draft. Confirm that every required control is visible and reachable with pointer and keyboard focus, including controls inside scrollable or clipped containers. A page without horizontal overflow can still hide a button inside a card, panel or modal. Do not run a data-changing action outside the task's authority; leave its criterion NOT_RUN with the reason and owner.

Record each criterion as PASS, FAIL or NOT_RUN with the evidence and owner. The Coordinator confirms the representative screen from that evidence before dependent screens or components expand. After expansion, record separate checklist rows for each affected screen or content group; representative PASS does not transfer to them automatically. This confirmation is part of the approved task's verification; it is not a new human approval gate. Independent authorized work may continue. If the template or authority boundary changes materially, follow the team's approval policy.

## Completion claims

- **Code integrated:** Required source, controller/data path and callers are connected. A build or source walkthrough may support this claim.
- **Behavior/UI verified:** Rendered desktop/mobile and interaction evidence meets the applicable checklist criteria.
- **Human accepted:** The human explicitly accepts the result.

Use `CODE_COMPLETE_UNTESTED` only for a human-requested source handoff for self-testing. It does not close a task whose goal is an applied and verified template. Keep missing checks as NOT_RUN with the reason and next owner/action. Source review of these instructions does not prove native agent behavior or an application's rendered result.
