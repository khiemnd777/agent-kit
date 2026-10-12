# Coordination templates

The coordinator fills and maintains these three templates. Humans decide goals, material requirements and acceptance. Fields in angle brackets are template inputs, not literal product text.

Use the same state template for the project and individual tasks. Only the Project Coordinator writes shared state; each Task Owner writes their task record. See [team workflow](team-workflow.md).

## Task Assignment

```text
TASK ASSIGNMENT: <task ID - short title>
Plan: <reference and revision>
Developer owner: <assigned person>
Agent role / runtime: <role, client and version>
Branch / base commit: <branch and starting commit>

Goal:
<Who needs which observable result?>

Deliverable:
<Concrete output; an early representative sample if direction is uncertain>

Sources and decisions to preserve:
<Relevant requirements, code, accepted decisions, labels and selected skills>

Authorization:
<Direct human approval source, approver, plan revision and covered actions;
latest stop or restriction. No approval is the default for a new task.>

Scope and ownership:
<Owned files/modules, permitted tools/checks and preserved data/work>

Dependencies and contracts:
<Required inputs, agreed shared interfaces and sequential work>

Model routing:
<Inherit by default; Explicit only by an intentional approved project choice.
Record requested and runtime-reported model/effort; Unknown if unobserved.>

Acceptance criteria:
- <Observable condition>
- <Important boundary or counterexample>

Verification:
<Checks that prove the criteria, check owner and evidence location>

Handoff to coordinator:
<Branch/commit, outputs/files, actual check results, findings,
assumptions, limits and next action>

Coordination limits:
Preserve and accommodate other developers' changes.
Explorers and reviewers are read-only.
Children do not delegate again.
Escalate material missing decisions; continue unaffected authorized work.
```

Agent completion is an input to integrated verification, not its replacement.

## Project / Task State

```text
STATE: <project or task ID>
Updated: <timestamp>
Writer / owner: <designated coordinator or task owner>
Plan revision / source commit: <current references>
Runtime / role: <client/version and actual role, if relevant>

Current goal:
<Confirmed result and priority>

Mode / state:
<Planning or Executing; stage plus Blocked/Stopped reason when applicable>

Current authority:
- Approval source / approver / revision: <none unless verified>
- Covered actions: <specific scope>
- Latest stop or restriction: <reference and affected work>

Accepted decisions:
<Decisions to preserve; distinguish proposals and unknowns>

Reference sample:
<Accepted sample and qualities to retain, or None>

Work:
<Task ID -> owner -> branch/commit -> next action>

Integration:
<Integrated commit/results; identify unintegrated branch results separately>

Model / capability evidence:
<Requested and observed model/effort, overrides, effective capabilities;
Unknown for unobserved values>

Verification evidence:
<Criterion -> PASS / FAIL / NOT_RUN -> command/evidence/date and limits>

Latest feedback:
<Requested repair -> affected surfaces -> resolution -> closing evidence>

Human decisions needed:
<Only material unresolved decisions with impact and recommendation, or None>

Next action / handoff:
<Concrete action, receiver, dependency and whether current authority covers it>
```

An approval field written by an agent, or an Integrated/Verified label, does not create authority.

## Coordinator Checklist

```text
BEFORE EXECUTION / ASSIGNMENT
[ ] Read the current plan, human approval and latest stop; the action is covered.
[ ] Preserve decisions; resolve material assumptions, ownership and contracts.
[ ] Define acceptance, counterexamples and checks; use an early sample if useful.

BEFORE HUMAN REVIEW
[ ] Inspect the actual output and evidence limits; check roles, routing and capabilities.
[ ] Integrate and repair in-scope findings; use independent review where warranted.
[ ] Close earlier feedback across affected surfaces with evidence.

AT HANDOFF / MILESTONE
[ ] Update owned state, source revisions and current-output links; reconcile old pending items.
[ ] Report result -> evidence -> limits -> material human decision or next action.
[ ] Continue authorized work; escalate expanded scope and stop the affected work when requested.
```

If a checklist item fails, the coordinator repairs what is already authorized before presenting the milestone. A human decision request should identify the concrete issue and recommendation.
