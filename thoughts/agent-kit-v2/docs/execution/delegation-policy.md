# Delegation policy

## Delegate an outcome, not a sequence of LLM tool decisions

A candidate block has stable inputs, verifiable outputs, understood side effects
and useful reuse. Repeatability does not require identical results and does not
make an operation idempotent. Code review can include a fixed collection/checking
block while semantic review still needs reasoning.

Prefer DIRECT when one existing command, script or configured CI job is adequate.
Use DELEGATE only when an already available, reviewed external executor adds
useful coordination, isolation, resumability or evidence aggregation. A large
command count is not sufficient by itself. No numeric score is an authority gate.

## Admission decision by the owner

Before invocation, establish all of the following from real evidence:

1. The user-approved scope covers the goal, target, data, side effects and budget.
2. The capability exists, its version/digest and contract are known, and its
   declared effects fit that scope. A file containing metadata does not prove
   native availability or trust.
3. Inputs identify the intended immutable snapshot, including uncommitted and
   relevant untracked files when they are part of the change. HEAD is not a
   substitute for that snapshot. Relevant environment/policy identities are known.
4. Required checks, output limits, time limits, retries and escalation conditions
   are explicit enough to execute without repeated owner decisions.
5. There is a safe way to receive the result and honor cancellation. Runtime
   permission/isolation enforcement belongs to the executor and host, not this kit.

If a prerequisite is unknown, do not silently broaden the target or pick a more
powerful workflow. Choose an equivalent authorized direct route or report WAIT.

## Handoff

Use the [draft contract](../../contracts/README.md) when a future compatible
adapter is actually installed. Send the goal and allowed bounds, not the entire
chat, all skills, credentials or an LLM-generated DAG. Pin capability identity.
Selecting an executor's internal workflow must not change authorized effects.

One request covers one complete work block. Acknowledge only observed delivery;
no transport/adapter is included in V2. Do not synthesize events or repeatedly
poll a job to consume time. Use the real executor's completion mechanism and
report what can actually be observed in the current client.

## Return conditions

Success with complete evidence -> interpret and hand off.
Known safe technical handling -> executor stays within agreed bounds.
Unexplained failure, material decision, policy change or unsafe replay -> owner
reasoning/approval. Cancellation/timeout -> distinguish settled versus unknown
effects before any rerun. Missing or mismatched evidence -> reject the claim,
not silently mark success or automatically execute again.

## Workflow lifecycle

Discover/select reviewed existing automation first. Propose creation of a new
recipe only when repeated work and maintenance cost justify it. Recipe authoring
is separate approved implementation work; V2 does not author a workflow for every
request. Human approval of a recipe is not perpetual authorization to run it.
When the recipe, source, policy or environment changes, invalidate only affected
evidence and re-review the affected boundary.
