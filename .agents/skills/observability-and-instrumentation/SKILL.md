---
name: observability-and-instrumentation
description: Add or review logs, metrics, traces or alerts for a concrete diagnostic gap or operational requirement using the project's existing telemetry.
---

# Observability and Instrumentation

Use the [lean operating core](../../../AGENTS.md). Begin with the operational question and inspect existing signals for the affected behavior. Reuse telemetry that already answers it. A production feature does not automatically require all signal types, a new dashboard or an observability platform.

## Select a useful signal

Use structured events for what happened in a specific operation, bounded metrics for aggregate rates or latency, and tracing when a cross-service path cannot otherwise be explained. Choose the minimum signal that resolves the gap. Match existing naming, log levels, units, sampling and routing rather than introducing a parallel schema.

For a request or job that must be followed across boundaries, preserve relevant correlation context. Identify the entry point when multiple launch paths share one stream and attribution matters. Validate externally supplied identifiers and propagate only information appropriate to each boundary. A simple local diagnostic need not add an ID to every unrelated message.

## Keep cost and data exposure bounded

- Allowlist emitted fields. Exclude credentials, tokens, raw sensitive payloads and unnecessary personal data from logs, traces and metrics.
- Keep metric labels bounded. Prefer route templates or known categories to user IDs, raw URLs and error text. Match histogram buckets and units to the actual question.
- Consider signal volume, sampling and retention. Extra detail that cannot change an operational decision creates cost without resolving the gap.
- For a new or changed alert, establish its actionable meaning, owner, threshold and response guidance using the project's severity and runbook conventions. Reuse an existing runbook where it fits.

New services, paid platforms, notifications and staging/production experiments retain their actual authority boundaries. Existing deployment or release controls remain binding; this skill adds no mandatory rollout.

## Verify and finish

Observe the changed telemetry with a safe fixture, existing focused test or other authorized environment. Check the actual fields, correlation, bounded series or routing needed for the claim. Alert delivery and cross-service propagation require relevant observed evidence; a configuration diff alone does not prove either.

Stop when the operational question is answerable with sufficient evidence. Do not expand into instrumenting every endpoint or resolving unrelated incident debt. Report unavailable observations and their effect on any required criterion.

Read [detailed techniques](references/detailed-guide.md) for the selected logging, metrics, tracing or alerting pattern. Consult the [telemetry checklist](../../references/observability-checklist.md) only for applicable checks.
