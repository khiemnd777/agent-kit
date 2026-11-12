# Contributing

Keep Agent Kit portable, concise and honest about evidence. The [lean core](AGENTS.md) governs routine work; [workflow](docs/team-workflow.md) and [policy](docs/team-policy.md) provide detail when needed. Skills and roles must not introduce competing approval or per-edit verification lifecycles.

## Sources of truth

Edit canonical skills/references in `.agents/`, then copy affected content byte for byte to `.claude/`. Preserve supported frontmatter, inventory, original upstream pin/origin metadata and license. Record approved local adaptations in [provenance](docs/skills-provenance.md) and the manifest; an upstream upgrade needs its actual reviewed scope.

Gemini CLI and Cursor use `.agents/skills/` directly; do not create extra skill mirrors. Keep all four native adapter sets aligned in role identity and body, using each runtime schema. Regenerate the manual Grok reference with `python3 scripts/export_grok.py` after its sources change, and verify with `--check`. The exporter embeds license notices and source fingerprints, never task approvals or private project state.

Common role behavior is in `docs/roles/`. Native adapters route to it using their existing schemas; do not pin models, add tool/sandbox overrides or change global settings as a side effect. Keep project docs/skills in English; user-facing explanations honor explicit language requests.

Use one checkpoint when useful for continuation or required by the project; give shared summaries one writer when edited. Preserve existing work and historical decisions/reports. Do not infer Git mutations, publication or release from an instruction update.

## Package changes

Review the actual intended diff, update affected mirrors and only explained inventory hashes. Do not rebaseline unexplained differences. Add new maintained sources intentionally; mutable task/project/evidence records stay outside package hashes.

Use the existing [package check](docs/verification-guide.md#package-integrity), affected links and metadata checks. These checks do not require a new runner or native/fixture campaign. Native behavior remains NOT_RUN unless observed under its own authorized scope. Recheck only evidence invalidated by a subsequent change.

## Handoff and license

Report the concrete changes, actual check commands/results/limits, unresolved defects and next action. Disclose self-review versus independent review. Do not store credentials, customer data, machine configuration or private conversation history. New kit content is MIT; retain upstream notices and rights.
