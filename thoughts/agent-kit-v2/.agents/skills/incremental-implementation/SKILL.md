---
name: incremental-implementation
description: "Deliver coherent approved capabilities through real callers/layers without artificial file-by-file handoffs."
---

# Incremental Implementation

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Implement a usable capability
Read the outcome, contracts and relevant source/tests. Identify the actual flow
that consumes the change. Implement through its necessary UI/routes/services/data
or commands; include real integration and preserve authorization/data invariants.
An unused helper or disconnected screen does not complete a capability.

For long/complex/UI work, complete the approved production scope and wiring before
writing/updating tests, then run them. Add meaningful regressions for changed
behavior and risky seams, not tests that restate trivial internals. Prefer usable
increments over arbitrary file batches; a prerequisite needs a real consumer.

Stable subproblems can use existing direct tools or an available executor under
the delegation policy. Do not hand over evolving product decisions or build a
runner as incidental feature work. Feature flags/migration recovery need actual
scope and data constraints, not default infrastructure.

## Complete and hand off
Repair evidenced defects within approval and recheck invalidated evidence. Honor
stops and preserve other work. One checkpoint may support long/resumed tasks;
no record after every edit. Stop with coherent source, relevant evidence and
explicit FAIL/NOT_RUN limits. Optional polish, Git publication and release do not
silently become part of the package.
