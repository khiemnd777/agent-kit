# Observability Checklist

Select checks for the instrumentation changed and the actual operational requirements, alongside the `observability-and-instrumentation` skill. The sections are alternatives by signal type, not an all-items gate. Reuse existing telemetry; do not create a monitoring platform to complete this checklist. Unselected items are not required checks; missing actual project requirements remain open.

## Table of Contents

- [On-Call Questions (Start Here)](#on-call-questions-start-here)
- [Structured Logging](#structured-logging)
- [Metrics](#metrics)
- [Distributed Tracing](#distributed-tracing)
- [Alerting](#alerting)
- [Dashboards](#dashboards)
- [Verify the Telemetry](#verify-the-telemetry)
- [Pre-Launch Gate](#pre-launch-gate)

## On-Call Questions (Start Here)

Telemetry without a question is noise. Before instrumenting anything:

- [ ] 2–4 questions an on-call engineer will ask about this feature are written down
- [ ] Every signal below maps to one of those questions
- [ ] Each question is matched to the right signal type: metrics say **that** something is wrong, traces say **where**, logs say **why**

## Structured Logging

- [ ] Logs are structured (JSON) with stable event names — not free-form strings
- [ ] Every log line carries a correlation/request ID, generated or accepted at the system boundary
- [ ] Correlation ID is propagated on every outbound call and async boundary (HTTP headers, queue metadata)
- [ ] Any log stream written by more than one entry point (scheduler, replay endpoint, manual run) carries an entry-point field, set where the run starts and propagated alongside the correlation ID
- [ ] Log levels are consistent: `error` = invariant broken, someone may act; `warn` = degraded but handled; `info` = significant business event; `debug` = off in production
- [ ] No secrets, tokens, passwords, or unredacted PII in any log line (hard rule from `security-and-hardening`)
- [ ] Fields are allowlisted — no whole request/response bodies, no auth headers
- [ ] External service calls logged with metadata only: endpoint, status, latency, attempt count, sanitized identifiers
- [ ] Actual log output spot-checked: structured fields, not `[object Object]`

## Metrics

- [ ] Where request health needs metrics, **RED** covers the affected endpoints/dependencies: Rate, Errors, Duration
- [ ] Where resource health needs metrics, **USE** covers the affected resources: Utilization, Saturation, Errors
- [ ] Latency is a histogram; p50/p95/p99 queryable — never an average
- [ ] All labels come from small, fixed sets (route template, status class, provider name)
- [ ] No unbounded label values: no user IDs, tenant IDs, emails, raw URLs, request IDs, or error message text
- [ ] Status codes grouped by class (`5xx`, not `503`)
- [ ] Queue depth and processing duration cover workers/queues selected by the operational requirement

## Distributed Tracing

- [ ] OpenTelemetry (or equivalent) initialized at service startup, before other imports
- [ ] Auto-instrumentation enabled for HTTP, gRPC, and DB clients
- [ ] Trace context propagated on every outbound call (W3C `traceparent`/`tracestate`) and extracted from every inbound request
- [ ] Context survives async boundaries — queue messages carry trace metadata
- [ ] Manual spans only around meaningful internal units of work, with the attributes on-call will filter by
- [ ] No secrets or PII as span attributes
- [ ] Head-based sampling at a low default rate; 100% of errors kept if tail sampling is available

## Alerting

- [ ] Every alert is symptom-based (error rate, p99 latency, queue age) — causes (CPU, disk, restarts) go to dashboards, not pagers
- [ ] Every alert is actionable; "ignore it, it self-heals" alerts are deleted
- [ ] Every alert links to a runbook — minimum three lines: what it means, first query to run, escalation path
- [ ] Thresholds and durations justified by an SLO or historical data, not guesses
- [ ] Severity names, levels and routing follow the established project scheme and the affected alert's intended urgency; **page** and **ticket** are response examples, not required field values or a limit on the number of levels
- [ ] Each new alert test-fired once: it reached the right channel and the runbook link works
- [ ] No alerts that fire daily and get acknowledged without action

## Dashboards

- [ ] Service health dashboard exists: error rate, latency p99, traffic, saturation
- [ ] Dependency health panel shows per-service error rates and latency
- [ ] Dashboard answers the on-call questions from the top of this checklist — not "everything except the answer"
- [ ] Default time range is sensible (1h–6h, not 30d)

## Verify the Telemetry

Verify only the instrumentation changed, in an authorized environment. The following are options, not requirements to induce failures, install tools or notify people:

- [ ] Forced an error in staging → found it in the logs by correlation ID
- [ ] Sent test traffic → metric series appear with expected labels and sane values
- [ ] Followed one request end-to-end in the tracing UI → no broken spans
- [ ] An induced failure was diagnosed from telemetry alone, without reading the source

## Pre-Launch Gate

This heading is retained for existing links. The project release criteria determine which observations below apply; this reference creates no universal pre-launch gate:

- [ ] If log aggregation is required, the affected structured events reach the existing sink
- [ ] If request-health metrics are required, the affected endpoint/dependency signals are visible
- [ ] If an alert is required or changed, it has an owner/runbook and authorized delivery evidence
- [ ] If cross-service tracing is required or changed, the affected path preserves trace context
- [ ] Relevant operators can find any changed runbook

Do not add an aggregator, dashboard, alert or tracing service merely to fill a row. An unmet actual release criterion stays open with an owner; source completion and release readiness remain distinct. Use the project's existing release/runbook instructions and [team workflow](../../docs/team-workflow.md#acceptance-and-release) for release sequencing and recovery decisions.
