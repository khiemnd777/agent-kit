---
name: documentation-and-adrs
description: "Update a changed contract or usage instruction, or record a significant architecture decision without inventing approval history."
---

# Documentation and ADRs

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Choose the smallest useful record
Identify the audience and decision/question. Update the existing relevant source
rather than duplicating policy across README, spec, ADR and task files. Use an ADR
for a significant choice whose rationale/consequences matter, not every code edit.
Distinguish proposal, accepted architecture, authorized implementation and observed
behavior. Do not reconstruct fictional approval history.

## Explain the changed behavior
Derive commands and examples from real supported tools. An example grants no
installation or publication authority. Document inputs, outputs, failure modes,
compatibility and important constraints. Comments should explain reasons, not
repeat syntax. Link sanitized evidence rather than copy logs/credentials.

Keep durable rules in the core, stable design in context, intended outcomes in
plan and one live state summary. No mandatory journal or percentage table per
phase. Planning notes stay inside their actual authority and shared ownership.

## Verify and finish
Check affected links and the agreement between prose, examples and implementation.
Separate reviewed syntax from executed commands. Mark future Sidecar contracts
as draft and unavailable runtime as NOT_RUN. Stop when the requested audience can
use or review the changed result; unrelated documentation debt is separate scope.
