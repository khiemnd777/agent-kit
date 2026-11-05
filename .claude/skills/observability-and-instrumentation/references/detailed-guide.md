# Observability and Instrumentation: detailed techniques

Read the section that resolves the current technical question. The [skill entrypoint](../SKILL.md) sets scope and completion; examples here do not select a stack, authorize side effects or add delivery gates. Preserve the project's actual security and release requirements.

## Contents

- [Select a signal](#select-a-signal)
- [Signal choices](#signal-choices)
- [Relevant warning signs](#relevant-warning-signs)
- [Verification](#verification)

## Select a signal

### Define the operational question

Identify the concrete operational question not answered by existing telemetry. The current task may already state it; no separate document or fixed number of questions is required. For example:

```
FEATURE: checkout payment retry
QUESTIONS ON-CALL WILL ASK:
1. What fraction of payments succeed on first attempt vs after retry?
2. When a payment fails permanently, why? (provider error? timeout? validation?)
3. Is the payment provider slower than usual?
→ Every signal below must help answer one of these.
```

If no diagnostic gap or applicable requirement remains, adding telemetry is unnecessary scope.

### Pick the signal needed for the question

| Signal | Answers | Cost profile | Example |
|---|---|---|---|
| **Structured log** | "What happened in this specific case?" | Per-event; grows with traffic | `payment_failed` with provider error code |
| **Metric** | "How often / how fast, in aggregate?" | Fixed per series; cheap to query | p99 latency of provider calls |
| **Trace** | "Where did time go across services?" | Per-request; usually sampled | One slow checkout, broken down by hop |

Rule of thumb: metrics tell you **that** something is wrong, traces tell you **where**, logs tell you **why**.

### Structured logging

For changed logs that need aggregation or correlation, use stable events and machine-readable fields in the project's existing logger. JSON is one common encoding; do not migrate unrelated logging to match this example:

```typescript
// BAD: string interpolation — unqueryable, inconsistent
logger.info(`Payment ${id} failed for user ${userId} after ${n} retries`);

// GOOD: stable event name + structured fields
logger.warn({
  event: 'payment_failed',
  paymentId: id,
  provider: 'stripe',
  errorCode: err.code,
  attempt: n,
}, 'payment failed');
```

**Log levels — follow the project's existing scheme.** These are illustrative meanings, not a new required taxonomy:

| Level | Meaning | On-call action |
|---|---|---|
| `error` | Invariant broken; someone may need to act | Investigate |
| `warn` | Degraded but handled (retry succeeded, fallback used) | Watch for trends |
| `info` | Significant business event (order placed, job finished) | None |
| `debug` | Diagnostic detail | Off in production by default |

**Preserve correlation when the diagnostic question needs it.** Use a validated request or job identifier across the affected operation and intended downstream boundaries. Reuse existing context; do not add IDs to unrelated messages merely to satisfy a checklist. For example:

```typescript
// Express: child logger per request, ID propagated downstream
app.use((req, res, next) => {
  // Use the project's validation/length rules before accepting an external ID.
  req.id = validatedRequestId(req.headers['x-request-id']) ?? crypto.randomUUID();
  req.log = logger.child({ requestId: req.id });
  res.setHeader('x-request-id', req.id);
  next();
});
```

**When several entry points write to one log, name the entry point.** A correlation ID identifies a run; it does not say which code path started it. The same job reached by a scheduler, by a replay endpoint, and by a manual CLI run produces interchangeable lines in one sink, so attributing a line falls back to elimination — cross-reading the scheduler's history, the process table, a deploy log — and that argument holds only as long as those external records happen to still exist. Stamp the entry point where the run starts, next to the correlation ID, and propagate both the same way:

```typescript
// One helper for every entry point: the run's own logger carries both fields.
// `entryPoint`, not `source` — ECS reserves `source.*` for network fields.
export const runLog = (entryPoint: 'scheduler' | 'replay_endpoint' | 'cli', runId: string) =>
  logger.child({ entryPoint, requestId: runId });

// scheduler tick        -> runLog('scheduler', crypto.randomUUID())
// POST /jobs/:id/replay -> runLog('replay_endpoint', req.id)
// CLI invocation        -> runLog('cli', process.env.RUN_ID ?? crypto.randomUUID())
```

When downstream attribution is required, propagate validated entry-point and correlation fields through the relevant queue or HTTP boundary, subject to the project's trust and privacy rules. A field that merely correlates with an entry point is a hint, not an attribution: anything that can invoke the job can reproduce it.

**Never emit credentials, tokens, passwords or unredacted sensitive personal data.** Allowlist the fields needed for the question; do not log whole request bodies. This protection applies directly and does not require loading another skill.

### Metrics

When request health is the question, use existing or scoped **RED** signals for the affected endpoints/dependencies: **R**ate, **E**rrors and **D**uration. When resource saturation is the question, consider **USE**: **U**tilization, **S**aturation and **E**rrors. Do not instrument every endpoint/resource merely to complete this list.

Reuse the existing metrics API. OpenTelemetry and Prometheus are possible implementations; the `prom-client` example below does not authorize adding a package or backend. Bound the label cardinality whichever implementation is used.

```typescript
import { Histogram } from 'prom-client';

const httpDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration',
  labelNames: ['method', 'route', 'status_class'],  // '2xx', not '200'
  buckets: [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5],
});
```

**Cardinality is the failure mode.** Every unique label combination is a separate time series. Labels must come from small, fixed sets (route template, status class, provider name). Never use user IDs, raw URLs, error messages, or other unbounded values as labels — that belongs in logs and traces.

```
OK as label:    route="/api/tasks/:id"   status_class="5xx"   provider="stripe"
NEVER a label:  user_id, email, request_id, full URL, error message text
```

When tail latency is the question, inspect an appropriate distribution or percentile; a mean alone can hide slow requests. Keep other aggregates when they answer the actual operational question. Do not add a full percentile set to every metric.

### Distributed tracing

When an approved cross-service diagnostic question needs tracing, reuse the project's tracing stack. OpenTelemetry is one option if its setup is within scope; this example is not a requirement to add a tracing platform:

```typescript
// tracing.ts — must be imported before anything else
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';

const sdk = new NodeSDK({
  serviceName: 'checkout-service',
  instrumentations: [getNodeAutoInstrumentations()],
});
sdk.start();
```

Add manual spans only for the missing unit of work that the question needs. Preserve validated context across the affected async boundaries and emit allowlisted attributes. Follow the project's sampling, volume and retention policy; this example does not mandate tracing every request or retaining all errors.

### Alerting

Prefer signals that explain user impact or a justified impending failure. Select symptoms or leading indicators from the project's operational requirements; these examples illustrate different uses:

```
SYMPTOM (page-worthy):           CAUSE (dashboard, not a page):
error rate > 1% for 5 min        CPU at 85%
p99 latency > 2s                 one pod restarted
queue age > 10 min               disk at 70%
```

A cause signal can be useful for diagnosis or prevention, but it needs an actionable interpretation. Match urgency to impact and evidence rather than paging on every resource fluctuation.

Rules for every alert you create:

1. **It must be actionable.** If the proposed alert has no useful response, revise or omit it. Do not remove unrelated existing alerts without their scope and owner.
2. **It links to useful response guidance** — reuse an existing runbook or add the missing meaning, first check and escalation path in the project's normal location.
3. **It has a threshold and duration** justified by the SLO or by historical data, not by a guess.
4. Use the project's established severity names, levels and routing. Match the alert's intended urgency to that scheme. **Page** (immediate response) and **ticket** (deferred follow-up) illustrate response urgency; they are not mandatory severity-field values or a two-level limit. A local alert addition/change does not require migrating the existing schema, routing or runbooks to match these examples. If no convention exists, choose a minimal useful scheme for the actual operational needs within the approved scope.

#### Writing Runbooks

For a new or changed alert, response guidance should explain what is happening, what to check first and who owns escalation. Reuse the project's runbook location and existing guidance; `docs/runbooks/` is an example when no convention exists, not a requirement for one file per alert.

**Minimum viable runbook (three lines):**

```markdown
# Runbook: High Error Rate on /api/tasks
**Means:** DB connection pool likely exhausted, or a bad deploy.
**First check:** `SELECT count(*) FROM pg_stat_activity WHERE backend_type = 'client backend';`
  — if count > pool limit, see Step 2. (Swap in the equivalent for your database.)
**Escalate to:** #db-oncall or engineering on-call rotation.
```

**When to expand beyond three lines:** add steps only when the first check alone isn't enough to decide. A five-step runbook that covers the three most common causes is better than a twenty-step document that covers every edge case and gets skimmed.

**Correct relevant runbook errors.** When this task changes an alert or reveals a misleading recovery step, update the affected guidance or record its owner. Incident closure follows the actual incident process; this skill does not add a new documentation gate.

### Verify the changed telemetry

Verify the instrumentation actually changed, using available authorized environments. Select only applicable observations below; do not induce staging/production failures, send alert notifications or provision platforms without authority. Missing required evidence remains explicit:

- Use a safe local fixture or authorized test request to observe the changed log fields and relevant correlation.
- If metrics changed, use available controlled traffic to confirm expected series, labels and values.
- If tracing changed, follow the affected request path with the existing tracing tools where authorized.
- If alert delivery is an acceptance criterion, use the approved test mechanism and destination. Do not lower live thresholds or send real notifications without that authority; record unavailable delivery proof.

## Signal choices

More telemetry is useful only when it answers a question or meets a concrete requirement. Reuse queryable events, existing dashboards and supported sampling. New tracing, metrics, alerts and platforms are separate choices; adding one does not require the others.

## Relevant warning signs

- A changed retry, queue or external call leaves an operational question unanswered.
- The changed operation needs correlation or launch attribution but loses that context.
- A new metric label contains an unbounded identifier, raw URL or error message.
- A changed alert has no actionable owner or meaningful response guidance.
- A new field exposes credentials or sensitive personal data.
- Claimed telemetry behavior has no observed output at the relevant boundary.

Investigate these signals where they affect the task; do not audit every endpoint or migrate all existing telemetry.

## Verification

For the instrumentation changed in this task:

- [ ] Each added/changed signal answers a concrete operational question or project requirement
- [ ] Changed logs use structured fields and relevant correlation/entry-point context
- [ ] Changed telemetry does not expose secrets, tokens or unredacted personal data
- [ ] Selected metrics use bounded labels and an appropriate latency distribution
- [ ] If tracing changed, the affected path preserves trace context
- [ ] If an alert changed, it is actionable, has an owner/runbook and was checked within authorized scope
- [ ] Actual output was observed where tools/authority allow; required unavailable observations remain NOT_RUN

The [checklist](../../../references/observability-checklist.md) is a menu of applicable checks. Only the project's actual release requirements can make a telemetry item a release gate; this skill adds none.
