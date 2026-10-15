# Coordination templates

The coordinator fills and maintains these three templates. Humans decide goals, material requirements and acceptance. Fields in angle brackets are template inputs, not literal product text.

Use the same state template for the project and individual tasks. Only the Project Coordinator writes shared state; each Task Owner writes their task record. See [team workflow](team-workflow.md).

These three templates are detailed coordination records. For user-facing chat, use TechNote's [adaptive reports](technote.md#adaptive-reports) for the current conversation, planning or implementation stage. Preserve required evidence and authority in the authorized record; keep material limits visible in the short report.

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
<Concrete output and completion level: code integration, verified behavior
or human acceptance; an early sample if direction is uncertain>

Sources and decisions to preserve:
<Relevant requirements, code, accepted approach, important assumptions,
data/permission boundaries, protective controls, labels and selected skills.
For an approved-template application: template source/version/hash, retained
structure/hierarchy/workflow/interaction/responsive rules, prototype material
to remove and human-approved differences. External references are selection
evidence, not authority to alter the approved template.>

Authorization:
<Direct human approval source, approver, plan revision and covered actions;
latest stop/replan or restriction and actual acknowledgement status.
No approval is the default for a new task. An unchanged allowlist is not
proof that a materially changed approach is approved.>

Scope and ownership:
<Owned files/modules, permitted tools/checks and preserved data/work>

Dependencies and contracts:
<Actual data/contract/ownership/resource dependencies and canonical owner;
decision owner per Coordinator scope and one shared-record writer when delegated.
No whole-team freeze or Supervisor ratification without a real requirement.>

Model routing:
<Inherit by default; Explicit only by an intentional approved project choice.
Record requested and runtime-reported model/effort; Unknown if unobserved.>

Acceptance criteria:
- <Observable condition>
- <Important boundary or counterexample>

Verification:
<Checks that prove the criteria, check owner and evidence location;
minimal real flow after authorized data preflight when applicable.
For an approved-template application: representative screen and observable
criteria; runtime/login/data/tool/permission prerequisites; rendered desktop
and mobile comparison at matching viewports, real controller/data path,
interaction and applicable states. Use template-application-acceptance.md;
record unavailable prerequisites as NOT_RUN before dependent expansion.
For reviews: question, result/evidence scope, risk reason and validity.
For blocking gates: source/risk, owner, PASS and invalidation conditions.
For a failed harness: missing proof, affected work, bounded next action
and stopping condition. Reuse valid evidence; no universal harness per edit.
For self-test handoff: actual callers/routes/commands, prerequisites,
manual steps and NOT_RUN/runtime-availability limits.>

Handoff to coordinator:
<Branch/commit, outputs/files, actual check results, findings,
assumptions, limits and next action>

Coordination limits:
Preserve and accommodate other developers' changes.
Explorers and reviewers do not change application code, implement features or repairs, or deploy.
Permissions follow the runtime and approved task scope; no sandbox/tool profile is imposed by role.
Authorized checks and evidence capture must stay within assigned side effects, fixtures and destinations.
Children do not delegate again.
Escalate material missing decisions; continue unaffected authorized work.
Continue routine repairs while the approved approach remains valid.
Stop affected execution for material approach changes or human stop;
report actual status and await explicit approval of the current plan.
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
<Confirmed user result, priority and next acceptance criterion to prove>

Mode / state:
<Planning or Executing; stage plus Blocked/Stopped reason when applicable>

Current authority:
- Approval source / approver / revision: <none unless verified>
- Covered actions: <specific scope>
- Latest stop or restriction: <reference, affected work/recipients,
  sent/acknowledged status, in-flight/uncancellable work and Unknowns>

Accepted decisions:
<Approved approach and assumptions/boundaries that must remain valid;
evidence/impact of any material change and required replacement plan.
Distinguish decisions, proposals and Unknowns; the same scope does not
authorize a material approach change.>

Reference sample:
<Accepted sample and qualities to retain, or None. For approved-template
application: source/version/hash, representative screen, required structure,
prototype removals and approved differences.>

Work:
<Task ID -> owner -> branch/commit -> result reached / specific blocker
-> next action and whether current approval covers it>

Integration:
<Integrated commit/results; identify unintegrated branch results separately>

Model / capability evidence:
<Requested and observed model/effort, overrides, effective capabilities;
Unknown for unobserved values>

Verification evidence:
<Criterion -> PASS / FAIL / NOT_RUN -> command/evidence/date and limits;
for an approved-template task, link checklist rows with screen, role, data
state, viewport, expected result and owner. Record representative rendered
desktop/mobile and interaction evidence before dependent expansion; source
or build PASS does not prove UI fidelity. Distinguish Code integrated,
verified behavior/UI and Human accepted; CODE_COMPLETE_UNTESTED is only a
human-requested self-test source handoff, not verified-template completion.
review question/scope/risk and reused result with validity conditions;
blocking gate source/risk, owner, PASS and invalidation conditions.
When an API/UI/library error appears in implementation/runtime/UAT:
affected flow paused, evidence, cause/hypothesis, focused repair plan,
affected files/consumers, repair check and approval coverage before edits.
When debugging repeats: attempts, new evidence, reassessed assumptions
and bounded next diagnostic action with expected result/stop condition.>

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
[ ] Preserve the approved approach; check important assumptions/boundaries, ownership and contracts; replan material changes even within the same allowlist.
[ ] Define acceptance, counterexamples and checks; for approved-template application, identify the source/hash, representative screen, prerequisites and rendered criteria before broad work; send the stage's opening report.

BEFORE HUMAN REVIEW
[ ] Inspect the actual output and evidence limits; for approved-template application, compare the representative rendered desktop/mobile screen, primary interactions and relevant states against the accepted template; check roles, routing and capabilities.
[ ] Integrate and repair under a valid approved approach; reuse valid reviews and review relevant changes/findings/evidence by risk; use independent review where warranted; justify blocking gates.
[ ] Close earlier feedback across affected surfaces with evidence.

AT HANDOFF / MILESTONE
[ ] Update owned state, source revisions and current-output links; reconcile old pending items.
[ ] Use the stage's closing report; retain material evidence/limits and the decision or next action, with relevant record links.
[ ] Continue authorized routine work; expand template-dependent work only after representative criteria pass, without a new per-step human approval; stop/replan material changes or expanded authority; transmit and confirm human stop status before explicit approved resumption.
```

If a checklist item fails, the coordinator repairs only what existing approval covers while the approach remains valid. Stop affected execution for a material change or human stop and present the concrete issue and replacement recommendation for explicit approval. Checklist items do not create per-action gates or authorize process/data cleanup.
