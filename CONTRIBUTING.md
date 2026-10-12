# Contributing

Keep Agent Kit portable, understandable and honest about its verification limits.

## Scope and workflow

Read [AGENTS.md](AGENTS.md), [team policy](docs/team-policy.md) and the [team workflow](docs/team-workflow.md). Agree the change scope, ownership, acceptance criteria and actual human approval before execution. Preserve existing work.

Make a focused branch and describe the resulting behavior and verification in your PR. A project may use its own authorized Git workflow. Do not infer commit, push, merge or repository administration authority from the kit.

## Sources of truth

- Edit skills, shared references and the upstream license in `.agents/`.
- Produce byte-identical copies in `.claude/`; never edit a mirrored skill first.
- Keep the sixteen upstream skills and their 26 source files unchanged at the recorded commit. A deliberate upstream upgrade is a separately reviewed change to the pin, provenance and all affected files.
- Edit common role behavior in `docs/roles/`. Native TOML and YAML adapters reference those roles and use their respective runtime schemas. They are not identical copies.
- Edit the complete explanation method in [TechNote](docs/technote.md). Its skill routes there instead of repeating the method.
- Keep policy, templates, role definitions and kit documentation in English. Project data and exact labels may retain their original language.

## Integrity inventory

[skills-manifest.json](docs/skills-manifest.json) records the upstream pin, 17 logical skills, all mirror pairs, native role bindings and checksums.

After an intentional change, review the expected diff before updating its recorded hashes. Copy canonical changes to their mapped mirrors, then recompute SHA-256 for the affected manifest entries. Never update hashes just to hide an unexplained difference.

Mutable project context, plan, state and task records are excluded from the kit checksum inventory. Normal project work can update those records without changing the kit's release manifest. Package-verification reports are also excluded to avoid a self-referential checksum cycle.

Use the reproducible [integrity check](docs/verification-guide.md#package-integrity) and the required static/runtime checks. Confirm that policy and role links still resolve, model pins were not introduced accidentally and read-only roles did not gain tools or permissions.

## Verification reporting

Report Written, Discovered, Invoked and Verified separately. Use PASS, FAIL or NOT_RUN for each actual check. Metadata discovery and agent self-reports do not prove effective model inheritance or permissions.

Keep observations tied to the kit version, commit, OS, client and date. Do not turn a single client result into support for all versions or operating systems. Do not place fixture approvals or kit verification results into fresh project state.

Examples must use synthetic data. Do not commit secrets, personal machine paths, account configuration, customer data or conversation history.

## Licensing

New contributions are supplied under the repository's MIT license. Preserve upstream copyright and license notices. Review provenance and rights before introducing another source package or executable resource.
