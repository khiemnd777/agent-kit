---
name: debugging-and-error-recovery
description: "Locate and diagnose an evidenced failure, repair its supported cause, and stop when further attempts have no useful basis."
---

# Debugging and Error Recovery

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Locate ownership before claiming cause
Start from exact error/UI text, route, endpoint, symbol or field. Use scoped
`rg`/file searches or the available equivalent. A screenshot suggests a source
location but does not prove it. Trace callers, registrations and consumers in the
actual architecture; do not assume a fixed layer chain. Distinguish a text match,
confirmed owner and verified cause. Reuse the source map without a new ceremony.

## Diagnose
Capture actual/expected behavior, reproduction, revision and data/authority limits.
Classify product logic, contract, authorization/data, test/config, shared environment
and external service failures. Choose an observation that distinguishes a concrete
hypothesis. A business assertion is not a tooling fault to dismiss. A setup/import
failure is not proof that a regression test detected the original bug.

A stable existing diagnostic bundle can be DIRECT/DELEGATE. Unknown-cause reasoning
stays with the owner; do not automatically repair source inside a mechanical executor.

## Repair, verify and stop
Preserve valid assertions, business rules and data. Make evidenced in-scope repairs
and rerun affected checks, including the original flow for runtime claims. Continue
only while new evidence and reasonable cost justify it; a different error alone is
not progress. Do not retry unchanged work until green, rebuild infrastructure,
install tools, reset data or restart services without authority. Report the specific
blocker when progress stalls. Explorer/reviewer roles return findings, not repairs.
