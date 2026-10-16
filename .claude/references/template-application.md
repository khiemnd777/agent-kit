# Applying an approved template

Use only for a human-approved internal/user-supplied template. Follow the [single team workflow](../../docs/team-workflow.md#applying-an-approved-template). This reference defines fidelity evidence, not another lifecycle.

## Source and scope

Record source/version or identifying hash, retained structure/hierarchy/workflow/controls, prototype removals and approved differences in the existing task. External inspiration does not replace an approved template. Resolve material discrepancies before changing the agreed design.

## Developer feedback

Wire real controller/data/callers. Compare a representative rendered screen early when an uncertain choice would otherwise be replicated. Check that choice before copying it to dependent screens, and continue unaffected code. No mandatory Coordinator confirmation or human gate follows each screen/edit.

## Usable-flow acceptance

Choose relevant rows from the [acceptance guide](../../docs/template-application-acceptance.md). Compare rendered source/implementation at matched desktop/mobile viewports. Check structure, tabs/action order, controls, interactions and applicable populated/empty/loading/error/permission states. Check navigation/unsaved-state continuity, disabled/busy feedback and preview identity when the approved flow has them.

Inspect keyboard focus and controls inside clipped/scrollable containers. Page-level no-overflow does not prove nested control visibility; screenshots do not prove a sequence or authorization. Do not create data or execute data-changing actions outside scope.

Record actual PASS/FAIL/NOT_RUN, evidence and missing prerequisite/owner/next action. One screen's evidence does not prove another screen; reuse genuinely shared evidence without transferring an unobserved conclusion. Check usable-flow milestones, not every state after every edit.

## Claims

Source complete requires real wiring/review. Verified UI needs relevant rendered/interaction evidence; human acceptance needs the human. CODE_COMPLETE_UNTESTED is a requested self-test source handoff. Missing code stays incomplete and unrun runtime stays NOT_RUN. None grants release or proves native agent behavior.
