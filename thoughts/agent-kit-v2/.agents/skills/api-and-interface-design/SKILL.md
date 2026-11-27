---
name: api-and-interface-design
description: "Design changed API/module contracts with real callers, compatible data shapes, meaningful failures and safe replay semantics."
---

# API and Interface Design

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Establish the affected contract
Read its definition, implementation and real consumers. Preserve established
naming, transport and versioning unless the approved outcome requires a change.
A field removal, newly required field or changed error meaning can break callers;
a compatible extension is preferable when sufficient. Do not create a second
API just to avoid inspecting consumers.

## Preserve boundary behavior
Validate untrusted input and responses without confusing shape with resource or
tenant authorization. Retain meaningful absence/denial/invalid-input/server-error
distinctions and protect sensitive internals. Bound growing collections with
appropriate ordering/pagination. Distinguish an omitted update from explicit
clearing and preserve concurrent-write protections.

For retriable effects, define one intent, payload matching, atomic claiming,
in-flight duplicates and retention. A lost response does not prove a write failed;
reconcile unknown effects before replay. This does not authorize financial or
production operations. An execution contract is likewise not a permission token.

## Verify and finish
Check changed behavior through its actual consumers and relevant failure,
duplicate/concurrency cases. Reuse unaffected evidence. Update changed types/docs
alongside code. Report compatibility limits and NOT_RUN checks. Read the
[API notes](../../references/engineering-notes.md#api-and-data) only when needed.
