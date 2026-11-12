# Multi-client support — plan v1

Delivery owner: main session. Delivery type: proposed one handoff; no parent roadmap. Source baseline: 8161bfe. Status and authority live in docs/project-state.md. This is planning-only documentation, not adapter/skill implementation approval.

## Confirmed request and assumption

- Khiêm requests additional Gemini, Grok and Cursor support.
- Khiêm explicitly selected Grok web/app of xAI in the current conversation.
- Proposed Gemini target: Gemini CLI. Gemini consumer web/Gems are not included unless requested.
- Preserve existing Codex and Claude behavior, shared AGENTS.md, 17 canonical skills and three role responsibilities.

## Proposed complete outcome

1. Gemini CLI: GEMINI.md imports @AGENTS.md; use existing .agents/skills without another mirror; add three native role adapters in .gemini/agents using documented Markdown/YAML schema and inherited model intent. Preserve parent permission boundaries and disclose effective permission uncertainty.
2. Cursor: use root AGENTS.md and .agents/skills; add three native role adapters in .cursor/agents. Avoid another instructions/skill copy. Inspect duplicate skill discovery from existing .claude/skills; source preference is not yet proven in a live client. Do not change existing mirror layout merely to avoid duplicates. Keep role/tool permission intent aligned, without introducing a new role permission profile.
3. Grok web/app: add a local manual-use guide/bootstrap and a self-contained uploadable Markdown reference assembled from shared policy and canonical skills/references (with provenance/license as needed). Do not rely on local relative links or @ imports being expanded by Grok. Describe planner/implementer/reviewer as conversational roles, not registered native subagents. No claim of automatic repo discovery or local command execution. Define source revision and refresh instructions to prevent stale exports. Exact web/app settings/UI, limits and automatic skill loading are unverified; manual chat attachment is the documented baseline.
4. Update README, compatibility/adoption/model-routing/verification/provenance documentation as affected, manifest and integrity recipe where necessary, plus task/journal/state. No global configuration, client installation, external upload/account changes, API integration, Git publication or deploy.

## Acceptance and checks

- One shared policy source and unchanged canonical skill semantics; export content must match approved sources and preserve required references/licenses.
- Three corresponding role identities and bodies stay semantically aligned across native adapters; valid client-specific YAML fields and inherited model intent, no invented config keys.
- Existing package-integrity recipe passes after scoped manifest additions; check affected relative links, adapter metadata, inventories and whitespace.
- Explicit capability matrix separates authored/static-checked from discovered/invoked/behavior-verified; native client tests and Grok upload stay NOT_RUN unless actually authorized and observed. No new dependency installation to make a gate pass.
- No regressions to existing Codex/Claude source adapters or mirror integrity. Actual runtime duplicate-skill resolution remains a documented limit until observed.

## Evidence read on 2026-11-12

- https://geminicli.com/docs/cli/gemini-md/ — @file import.
- https://geminicli.com/docs/cli/skills/ — workspace .agents/skills alias; precedence over .gemini/skills at same tier.
- https://geminicli.com/docs/core/subagents/ — .gemini/agents Markdown/YAML and inherited model/tools fields.
- https://cursor.com/docs/rules — AGENTS.md support.
- https://cursor.com/docs/skills — .agents/skills and Claude compatibility discovery.
- https://cursor.com/docs/subagents — .cursor/agents schema and model inheritance.
- https://docs.x.ai/grok/faq — web/mobile uploads including Markdown. Does not establish repo-file discovery or native local subagents on consumer web/app.

## Open decisions

User approval of plan v1 including Gemini CLI assumption and manual Grok support. Live loading and behavior depend on actual installed client versions/accounts; no account/source upload is authorized by this plan.

## Approval — 2026-11-12

Khiêm replied “Duyệt” after the Gemini CLI explanation and plan-v1 handoff. This approves plan v1 including Gemini CLI, Cursor and manual Grok web/app support as one handoff with no parent roadmap. Implement local adapters/export/docs and checks. No install, external upload/account write, Git publication or deployment. Earlier proposal/unknown entries above are historical; the Gemini target and implementation approval are now resolved.

## Local implementation handoff — 2026-11-12

Source/package complete on the working tree based on 8161bfe; no commit created. Added GEMINI.md import, six Markdown native adapters (three per Gemini/Cursor), manual Grok guide/bootstrap/reference, deterministic local exporter and four regression tests. Updated README adoption, compatibility/model-routing/provenance/contributor/verification guidance and 112-entry manifest. No skill content changes or extra skill mirrors.

### Acceptance observations

- PASS: shared import and three role identities/bodies match across all four native clients; 9 YAML frontmatters parsed with existing Ruby/Psych and three existing TOMLs parsed with Python.
- PASS: published integrity recipe verifies 112 inventory entries, 35 byte-identical mirror pairs and 17 skills per root; upstream metadata unchanged.
- PASS: 78 protected core/Codex/Claude/canonical/mirror files unchanged against 8161bfe.
- PASS: 279 applicable local links/anchors across nine affected documentation files; Python syntax; four exporter tests; source freshness and deterministic reference reproduction.
- PASS: self-review of approved coherent change; no remaining actionable findings. This is not independent review. An initial test exposed a false rejection of macOS /var temporary-directory ancestry; fixed by checking path components inside the source root, and affected tests reran PASS.
- NOT_RUN: native discovery/invocation/effective models/permissions, Cursor duplicate skill resolution, Grok upload/retrieval/instructions persistence, two-machine behavior. No client install, account/external write or publication performed.

Detailed results: [validation.json](KIT-MULTI-CLIENT-2026-11-12/validation.json). Commands: published Python recipe in verification-guide.md; `python3 -m unittest discover -s tests -p 'test_export_grok.py'`; `python3 scripts/export_grok.py --check`; Ruby/Psych YAML parsing; inline Python adapter/link/preservation checks; `git diff --check`.

The Grok reference is approximately 324 KB. Account/context acceptance remains unobserved; a static export does not establish actual attachment usability. The export embeds source policy/skills/playbooks and license notices, rewrites local prose links and excludes maintenance task footers, approvals, journals and current state. Original content hashes identify source bytes; prose link rewriting and omission of the historical tasks-README footer are deliberate export transformations.

Concurrent work: README-VISUAL-2026-11-12 planning task/journal appeared during this task and was left untouched. README changes here only describe approved additional clients; future README visual work must preserve them. No worker/subagent was spawned.

Implementation journal: [implementation-1.json](../engineering/skill-usage/records/KIT-MULTI-CLIENT-2026-11-12/implementation-1.json). Human acceptance of delivered source remains pending; plan approval is not acceptance. Next options: review/accept this source package, or authorize a bounded native-client check with available accounts/clients; any Grok upload requires explicit content-sharing scope. Git publication remains a separate authorization.
