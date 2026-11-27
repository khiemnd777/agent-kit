---
name: spec-driven-development
description: "Resolve material requirement/domain/interface uncertainty without manufacturing a specification hierarchy."
---

# Spec-Driven Development

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Define needed decisions
Read accepted requirements and relevant code/tests. State outcome, scope and
observable acceptance. Inspect actors/permissions, states, invariants, interfaces
and error/concurrency cases only where affected. Separate confirmed requirements,
observed behavior, assumptions and unknowns. An existing bug is not a business rule.

Preserve chosen stack/contracts unless changing them is authorized. For distinct
capabilities, identify responsibilities and real dependencies without creating
a spec document for every module. Distinguish product decisions from a repeatable
execution block that may later be delegated.

## Resolve material choices
Reuse accepted decisions. Discuss concrete alternatives/tradeoffs for complex
work and preview UI in ASCII. Ask only for material choices/authority that evidence
cannot resolve. Continue unaffected authorized work. Planning-only requests remain
planning-only; saved notes do not approve implementation.

## Handoff
Provide agreed behavior, affected consumers and sufficient acceptance/checks.
A clear small fix can use a short approved chat plan. Stop specifying when those
are sufficient; routine in-scope repair does not restart specification. Written
requirements are not implementation, observed behavior or human acceptance.
