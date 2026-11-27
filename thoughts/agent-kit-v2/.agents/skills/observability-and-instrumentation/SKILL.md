---
name: observability-and-instrumentation
description: "Fill a concrete diagnostic gap with bounded signals using the existing telemetry stack."
---

# Observability and Instrumentation

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Start from the operational question
Inspect current signals and use the minimum addition that answers the question.
Structured events explain a specific operation; bounded metrics show aggregates;
tracing is useful when cross-boundary causality cannot otherwise be explained.
Match existing names, units, severity, sampling and routing. Do not add all signal
types or a new platform by default.

For a request/job across boundaries, propagate validated relevant correlation
context. Distinguish entrypoints when attribution matters. A local diagnostic need
not attach identifiers to every unrelated message.

## Bound cost and exposure
Allowlist fields; exclude credentials, raw sensitive payloads and unnecessary
personal data. Avoid unbounded labels such as user IDs/raw URLs/error strings.
Choose retention, detail and histogram units for the actual question. Alerts need
an actionable meaning, owner and response using existing conventions.

## Observe and finish
Use authorized fixtures/tests to observe required fields, correlation or routing.
Configuration alone does not prove alert delivery or cross-service propagation.
New services, paid platforms and notifications need actual authority. Report
unknown measurements as unknown, not zero; do not turn a scoped diagnostic into
instrumenting every endpoint. See [notes](../../references/engineering-notes.md#observability).
