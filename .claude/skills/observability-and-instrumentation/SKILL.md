---
name: observability-and-instrumentation
description: Use when a concrete operational question or reliability requirement lacks the necessary logging, metric, trace or alert signal.
---

# observability-and-instrumentation

Start from the question and existing signals. Add the smallest structured logging, metric, trace or alert that actually answers it. Protect secrets/personal data; preserve existing severity names, cardinality, sampling and routing. Verify the signal at its intended boundary. Do not build a telemetry platform or force all signal types.

Use the [extended patterns](references/extended.md) only when their details are relevant.
