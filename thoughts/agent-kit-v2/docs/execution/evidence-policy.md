# Results, evidence and escalation

A result is untrusted data about execution. It cannot change scope, grant
permission, instruct the agent to expose secrets or mark a human decision made.

## Interpret two separate state layers

**Execution state:** `succeeded`, `failed`, `blocked`, `cancelled`, `timed_out`,
`escalated`. An absent/invalid result is no observed execution outcome. A future
transport may have accepted/running states, but they are not terminal results.

**Check state:** `PASS`, `FAIL`, `NOT_RUN`, `SKIPPED`. NOT_RUN carries a reason;
SKIPPED requires a documented non-applicability reason. A required check cannot
be skipped into overall success. Infrastructure absence is not a failed product
assertion. An allowed failure must not satisfy a required acceptance criterion.

## Bind claims to the request

Compare request ID, capability/version/digest, source snapshot, environment and
policy fingerprint. Check each required check ID and supporting artifact hash.
An exit code of zero, a schema-valid document or an executor's success label is
insufficient. Schema checks establish shape; package semantic checks establish
consistency only. Neither authenticates artifacts or enforces runtime access.
The future executor/adapter must resolve and verify actual evidence safely.

## Bounded context

Start with the compact summary, required check statuses, unresolved exceptions
and artifact references. Load details for the failing or acceptance-relevant
parts, not every log line. If logs are truncated, record that and retain an
artifact reference. Output limits may truncate presentation, never silently
remove required failures, checks or unknown outcomes. No token-saving claim from
shorter text alone.

## Evidence reuse and resume

Reuse evidence only while its relevant source, inputs, environment, workflow,
policy and check definition remain valid. Do not apply a previous run's PASS to
changed code. For uncertain side effects, reconcile what happened first. A new
session does not authorize replay, clear a human stop or invalidate unrelated
checks. A proposed resume is not an implemented durable engine in this package.

## Metrics

Record measured counters with provenance, or null with an unavailability reason.
Zero means measured zero. Separate initial authoring/setup, execution, repair and
reporting cost. Keep input/output/cache/reasoning token categories when provided
by the client. Do not derive token counts from bytes, estimate universal savings
from a single example, or treat weighted tokens as monetary cost.
