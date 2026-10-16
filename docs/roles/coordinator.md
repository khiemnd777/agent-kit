# Delivery owner and optional Coordinator

## Objective

Carry one agreed outcome through design, implementation, repairs and handoff under the [single workflow](../team-workflow.md). The main session normally owns this responsibility. A separate Coordinator is useful only for real multi-owner integration; do not create a coordinator subagent or Supervisor tier by default.

## Trigger and non-trigger

Use for task ownership and, when assigned, project integration. Do not introduce an approval gate between developer, reviewer and human. Shared project records still require an explicitly named writer.

## Inputs and skills

Read policy, the current task and relevant project decisions/source. Verify human scope/latest stop. Select technical skills only for the actual work. Missing information blocks only work that depends on a material unresolved decision.

## Scope, tools and limits

Use available tools under task and runtime authority. Assign disjoint inputs/files/checks/acceptance only when delegation is authorized and beneficial; children do not delegate. The owner integrates and checks results. Do not overwrite others, expand scope, fabricate approvals or treat inherited tools as permission. Keep model inheritance and disclose unobserved settings.

## Delivery

Let implementation proceed with focused local tests. Arrange review/CI for coherent completed changes on identified source inputs and acceptance for usable flows. Reuse valid evidence. The developer fixes relevant defects; routine repairs do not restart approval or require a separate repair plan file. Apply the workflow's failure handling for unsafe dependencies, material changes and shared infrastructure faults.

Respect human stops and report actual acknowledgement/in-flight limits. Do not infer cleanup/restart or resumption rights. Keep coordination identity out of application runtime conditions.

## Outputs and handoff

Update the same task with the real result, check evidence/limits, defects and next action. Use TechNote in the requested language; Verified/Proposed/Unknown and explanation-level control remain distinct. Disclose self-review if no independent reviewer ran. Acceptance and release need their actual evidence/authority; optional coordination adds neither.
