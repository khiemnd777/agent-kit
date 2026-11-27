---
name: frontend-ui-engineering
description: "Build or repair the approved UI using real data wiring, accessible controls, responsive layout and relevant visual evidence."
---

# Frontend UI Engineering

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Preview and preserve the design
Inspect the affected screen/components/styles/data path. Reuse supported design
patterns. Present a proportional ASCII preview in the UI plan and obtain approval
before coding. Complete approved UI/data/caller wiring before tests/rendered checks.
A spacing/text fix does not need a new visual-research phase or state library.

## Implement the real experience
Prefer clear ownership, local state and explicit props where adequate. Add shared
state or extraction only for demonstrated coupling, not a line-count rule. Wire
real routes/consumers; a disconnected mock is not a completed feature. Preserve
semantic structure, accessible names, keyboard reachability, focus and meaningful
feedback. Handle affected loading/empty/error/success/permission states.

Keep supported sizes and realistic content usable, including nested containers.
Preserve agreed template structure, navigation/action order, controls, behavior
and approved differences. See [template notes](../../references/template-application.md)
when fidelity is part of acceptance; inspiration does not replace that contract.

## Verify and finish
Use relevant rendered, interaction, breakpoint and accessibility checks; reuse
unaffected evidence. Classify new and baseline defects. Do not demand a warning-free
entire site or install an audit platform incidentally. A blocked required flow
remains unverified. Build/source success does not establish visual fidelity.
