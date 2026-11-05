---
name: frontend-ui-engineering
description: Build or repair UI components, layouts and interactions while preserving the project's design, accessibility, responsive behavior and real data wiring.
---

# Frontend UI Engineering

Use the [lean operating core](../../../AGENTS.md). Inspect the affected screen, components, styles and data path. Reuse the project's design system and supported interaction patterns. A text or spacing fix does not require a new visual research phase, component architecture or state-management library.

## Preview before implementation

Every UI task includes an ASCII text mockup in the plan for discussion/preview and explicit approval before coding, even a small change. Scale the mockup to the affected control/state. Complex UI also needs risk/alternative investigation. Complete all approved UI/data/caller wiring before writing/updating and running tests or rendered verification.

## Implement the requested experience

Keep components and state ownership understandable. Prefer local state and explicit props when they work; introduce shared state or extraction to solve a demonstrated coupling problem, not a line-count or tree-depth rule. Wire the real route, controller and data rather than presenting an isolated mock as a completed feature.

Preserve semantic structure, accessible names, keyboard reachability, visible focus and meaningful feedback on changed controls. Consider loading, empty, error, success and permission states where the change affects them. Keep layout usable at the project's supported sizes and with realistic content; page-level overflow checks alone do not prove that controls inside nested containers are reachable.

Follow existing tokens and hierarchy. Obtain visual references only when a material design question remains unresolved; an established supported pattern can be reused directly. Reference examples do not require a particular palette, framework, animation style or new design document.

## Apply an approved template

For an approved internal or supplied template, retain its agreed structure, navigation/action order, controls, interactions and responsive behavior. Use its identified source and approved differences. Resolve uncertain choices in the ASCII planning preview and obtain approval before coding. Rendered/interaction verification follows completed approved code and wiring; do not add a gate per screen.

Read the [template reference](../../references/template-application.md) and [acceptance selection guide](../../../docs/template-application-acceptance.md) when template fidelity is part of acceptance. At a usable-flow milestone, compare relevant desktop/mobile views and interactions with the approved template. An external inspiration image does not override that contract.

## Verify and finish

Select representative rendered and interaction checks for the changed behavior, relevant breakpoint boundaries and affected accessibility requirements. Reuse unaffected evidence. Classify new findings and relevant baseline defects; do not require a warning-free entire site or install an audit platform for every edit. A required flow blocked by a baseline defect remains unverified.

Stop when the requested flow is usable and its relevant checks are sufficient. State any missing rendered evidence; source or build success alone does not prove visual fidelity.

Use [detailed techniques](references/detailed-guide.md) for component, state or layout examples. Use the [accessibility reference](../../references/accessibility-checklist.md) for the affected accessibility question; neither is a mandatory whole-site checklist.
