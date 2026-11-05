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

Start from the operational question the changed instrumentation must answer. Reuse existing incidents, runbooks or requirements; a small diagnostic change does not need a new planning document:

- [ ] The affected operational question is clear; capture it only where review or handoff needs durable context
- [ ] Each selected or changed signal helps answer that question
- [ ] Each question is matched to the right signal type: metrics say **that** something is wrong, traces say **where**, logs say **why**

## Structured Logging

- [ ] Changed events follow the established structured format and stable event naming
- [ ] Request-scoped events carry the correlation/request context needed to diagnose the affected flow
- [ ] Relevant outbound/async boundaries preserve correlation context (HTTP headers, queue metadata)
- [ ] Where the same flow has multiple entry points (scheduler, replay, manual run), events distinguish their origin when needed for diagnosis
- [ ] Levels and routing follow the project convention; retain appropriate production verbosity and avoid changing unrelated levels
- [ ] No secrets, tokens, passwords, or unredacted PII in any log line (hard rule from `security-and-hardening`)
- [ ] Fields are allowlisted — no whole request/response bodies, no auth headers
- [ ] External service calls logged with metadata only: endpoint, status, latency, attempt count, sanitized identifiers
- [ ] Actual log output spot-checked: structured fields, not `[object Object]`

## Metrics

- [ ] Where request health needs metrics, **RED** covers the affected endpoints/dependencies: Rate, Errors, Duration
- [ ] Where resource health needs metrics, **USE** covers the affected resources: Utilization, Saturation, Errors
- [ ] Where tail latency is the question, a histogram or equivalent distribution exposes the needed percentiles; an average alone is insufficient
- [ ] All labels come from small, fixed sets (route template, status class, provider name)
- [ ] No unbounded label values: no user IDs, tenant IDs, emails, raw URLs, request IDs, or error message text
- [ ] Status labels use the project's bounded grouping (for example `5xx`); do not migrate a valid existing schema for this example
- [ ] Queue depth and processing duration cover workers/queues selected by the operational requirement

## Distributed Tracing

- [ ] When tracing is changed, initialization follows the existing SDK/client requirements
- [ ] Existing auto-instrumentation covers the affected client boundary where needed; no unrelated tracing platform setup
- [ ] The affected cross-service path propagates/extracts trace context using the established protocol
- [ ] Context survives async boundaries — queue messages carry trace metadata
- [ ] Manual spans only around meaningful internal units of work, with the attributes on-call will filter by
- [ ] No secrets or PII as span attributes
- [ ] Sampling follows the project's cost/privacy/diagnosis requirements; inspect the changed path without requiring a new sampling system

## Alerting

- [ ] A changed alert identifies an actionable service symptom or justified operational risk, consistent with the established paging policy
- [ ] A changed alert has a useful action; propose removal of noisy alerts only when evidence and scope justify it
- [ ] A new/changed alert points to the needed meaning, first diagnostic and escalation owner; reuse the existing runbook
- [ ] Thresholds and durations justified by an SLO or historical data, not guesses
- [ ] Severity names, levels and routing follow the established project scheme and the affected alert's intended urgency; **page** and **ticket** are response examples, not required field values or a limit on the number of levels
- [ ] When delivery validation is required and authorized, check the changed alert's routing/runbook; do not notify people incidentally
- [ ] Check observed noise for the affected alert when relevant; unrelated alert cleanup remains separate

## Dashboards

- [ ] If a dashboard is required/changed, it shows the health signals needed for the affected question
- [ ] Include dependency health only where it helps the affected diagnosis
- [ ] Dashboard answers the on-call questions from the top of this checklist — not "everything except the answer"
- [ ] The selected time range fits the diagnosis or operational question

## Verify the Telemetry

Verify only the instrumentation changed, in an authorized environment. The following are options, not requirements to induce failures, install tools or notify people:

- [ ] For an authorized error-path check, locate the observed event by correlation ID
- [ ] For affected metrics, use authorized traffic or existing observations to inspect expected labels and values
- [ ] For changed trace propagation, follow an authorized representative request across the affected boundaries
- [ ] Where diagnosis is the acceptance claim, assess whether the available telemetry answers the stated question; inducing a failure is optional and needs authority

## Pre-Launch Gate

This heading is retained for existing links. The project release criteria determine which observations below apply; this reference creates no universal pre-launch gate:

- [ ] If log aggregation is required, the affected structured events reach the existing sink
- [ ] If request-health metrics are required, the affected endpoint/dependency signals are visible
- [ ] If an alert is required or changed, it has an owner/runbook and authorized delivery evidence
- [ ] If cross-service tracing is required or changed, the affected path preserves trace context
- [ ] Relevant operators can find any changed runbook

Do not add an aggregator, dashboard, alert or tracing service merely to fill a row. An unmet actual release criterion stays open with an owner; source completion and release readiness remain distinct. Use the project's existing release/runbook instructions and [team workflow](../../docs/team-workflow.md#acceptance-and-release) for release sequencing and recovery decisions.
