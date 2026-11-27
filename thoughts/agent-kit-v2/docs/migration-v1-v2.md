# V1 -> V2 migration

## Source baseline

Agent Kit V1.0.0, commit `df3b058a52acc9ea10a7556733baae44ac12d1f2`.
V2 is a curated standalone rebuild from inspected source, not a byte-for-byte
V1 checkout. No remote repository was changed and no application was migrated.

## Deliberate changes

- Replace repetitive LLM step orchestration with an outcome-level delegation
  policy usable at task entry and at stable intermediate blocks.
- Keep direct tools and reasoning available when no external executor exists.
- Replace compulsory WHAT/skills-percentage/journal/visual forms for every task
  with proportional evidence reporting. Useful multi-part WHAT and UI evidence
  remain; honest actual skill descriptions are allowed without percentages.
- Centralize authority in the core; shorten mirrored role instructions.
- Retain the 17 technical skill identities, adapting their guidance to V2;
  add one execution-delegation skill. Consolidate optional engineering references
  into scoped V2 references rather than copying all V1 long-form guides.
- Add draft JSON contracts and offline consistency checks, not a runtime.
- Refresh templates; do not carry V1 maintenance approvals or test success into
  new application records. Historical V1 tasks remain in the pinned source.

## Preserved boundaries

Plan approval before implementation; no repeated approval for covered steps;
roadmap acceptance stops; latest human stop; no implicit publish/merge/deploy;
privacy and data controls; one delivery owner; bounded child ownership;
long/complex/UI code-and-wiring-before-tests order; UI preview before coding;
source/verified/accepted/released distinctions; relevant evidence reuse;
MIT attribution and inherited upstream notice; existing client-role identities.

## Before applying to an existing project

Inspect its current instruction hierarchy, local modifications, skill overrides,
records and runtime restrictions. Agree a scoped adoption plan. Reconcile rather
than overwrite project rules. Copy only reviewed sources/mirrors/adapters, then
run package checks. Do not replace application records with these empty templates.
A fresh client session can be used for an authorized discovery test; this package
does not prove native loading by static checks.

## Source layout changes

V1 expanded detailed guides and historical task/journal records are not reproduced
as active V2 instructions. Their provenance is retained through the pinned source;
compact references serve the current V2 skills. No claim is made that every V1
reference byte or historical example is bundled. Grok export is regenerated from
the actual V2 source, excluding delivery approvals, task history and examples.

## Rollback and comparison

Keep the actual prior project revision or backup before adoption. Rollback is an
explicit operation under its real authority, not an automatic action of this kit.
Compare V1, V2 using existing tools, and only later V2 with a real Sidecar as
separate configurations. See [benchmark plan](benchmark-plan.md).
