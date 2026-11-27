# V2 delivery workflow

## Understand, plan and approve

Read the task and the relevant source, not the entire kit. Establish the desired
outcome, boundaries, acceptance and actual risk. Resolve material choices and
obtain approval of the current implementation scope. Preserve agreed roadmap
packages; do not split by arbitrary file counts or create artificial handoffs.
For UI tasks, preview the agreed design in ASCII before coding.

## Select the route when a work block is known

Use the [WHEN policy](execution/when.md). The route is part of the owner's
ordinary decision, not a mandatory extra LLM call, metadata form or registry
scan. Reuse a known route while its assumptions remain valid.

| Work | Route |
| --- | --- |
| One adequate existing command/script/CI job | DIRECT |
| Stable multi-step block with suitable authorized external executor | DELEGATE |
| Unresolved requirements, design, implementation or unexplained failure | REASON |
| Missing permission, material decision or unsafe prerequisite | WAIT |

A novel feature can use REASON for implementation and DIRECT/DELEGATE for
repeatable repository inventory, fixture preparation or verification. Sidecar is
not confined to the end of the task. Do not force a novel task into a recipe.

## Complete the approved package

The owner remains accountable. Delegate whole outcomes, not individual tool
calls separated by LLM decisions. Existing automation wins over a new abstraction
when it meets the need. Children are optional and require useful bounded work.

For long, complex or UI packages, complete approved production code and real
callers/wiring before writing or updating tests, then run them. Existing source
and tests may be read during investigation. A material unsafe dependency blocks
its affected work even before testing. Do not hide incomplete wiring with mocks.

Use focused tests and existing required review/CI. A new session, phase or agent
does not invalidate unchanged evidence. Recheck changed dependencies, inputs,
environment, policy or source, not everything by habit.

## Interpret results and handle exceptions

Read a compact result, then evidence required for acceptance or a finding.
Validate its identity and source binding. Mechanical success is not business
correctness; preserve semantic review where needed. Resume reasoning when the
result exposes an unknown cause or decision, not after each successful step.

Repair evidenced in-scope defects. Retry only when justified by changed inputs
or a concrete transient cause and safe replay semantics. No retry-until-green,
weakened assertion, automatic broadened scan or incidental tooling rebuild.
Continue while new evidence justifies the effort; otherwise report the blocker.

## Handoff and stop

Use [proportional handoff](handoff-templates.md). Record the actual result,
revision/snapshot, checks, unresolved work and pending human decision. A small
task needs no mandatory task file, skills-percentage table or technical image.
Multi-part work benefits from a WHAT table and observable checklist. UI/fidelity
claims require relevant visual evidence, not a decorative diagram.

Keep the sole live state in `docs/project-state.md` when persistent state is
useful. Detailed approval/evidence stays in the existing task record. Stop at the
agreed acceptance boundary and before separately unauthorized work or release.
