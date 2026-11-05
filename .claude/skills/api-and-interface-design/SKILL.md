---
name: api-and-interface-design
description: Design or change API, module and component contracts, including compatibility, validation, errors and safe retries.
---

# API and Interface Design

Use the [lean operating core](../../../AGENTS.md). Work on the contract affected by the request and its real consumers. A small interface repair still requires a short plan and approval, but not a separate specification or API-wide audit. Covered repairs inside an already-approved plan do not need repeated approval.

## Establish the affected contract

Inspect the existing definition, implementation and relevant callers before changing a signature. Identify observable inputs, outputs, error behavior, ownership and compatibility constraints. Preserve the project's naming, transport and versioning conventions. Define a new contract only when the task needs one; types, examples or existing tests may already express it adequately.

Prefer a compatible extension when it satisfies the outcome. A field removal, required-field addition, changed meaning or altered failure response can break consumers. Account for actual callers and an agreed transition when a breaking change is necessary; do not create a parallel API version merely to avoid inspecting those callers.

## Preserve boundary behavior

- Validate untrusted input and external service responses at the relevant trust boundary. Keep resource/tenant authorization distinct from shape validation. Avoid duplicate validation only where an established internal contract makes it redundant.
- Preserve predictable error shapes and the distinction between absence, denial, invalid input and server failure. Keep sensitive implementation details out of responses.
- For collections that can grow, retain appropriate limits, stable ordering and the project's pagination contract. A bounded existing interface need not be redesigned for an unrelated change.
- For partial updates, distinguish omitted fields from explicit clearing and retain concurrency protections where competing writes are possible.

For retriable side effects, establish what one user intent means. A stable idempotency key needs a durable atomic claim, payload matching, deliberate in-flight duplicate behavior and retention covering the supported retry window. A timeout leaves an unknown outcome; do not repeat a charge or other irreversible effect merely because a response was lost. This guidance does not authorize payment or production operations.

## Verify and finish

Check the changed contract through its actual caller or an existing focused contract/regression test. Include the failure or duplicate/concurrency case that motivated the change when relevant. Reuse unaffected evidence and retain project-required integration checks. Update the affected types or API documentation alongside the implementation, without backfilling unrelated endpoints.

Finish when the requested contract, consumers and relevant evidence agree. Report incompatible changes, unresolved assumptions and checks that could not run.

Read [detailed techniques](references/detailed-guide.md) only for contract examples, REST/TypeScript patterns or the idempotency mechanism needed by this task.
