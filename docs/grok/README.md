# Grok web/app — manual use

This adapter targets consumer Grok on grok.com and the xAI mobile apps, not Grok Build, the API or a Grok model inside Cursor. It supplies a reference attachment and a bootstrap prompt; it does not register native agents/skills, read a local checkout or execute local commands. Native capability parity is not claimed.

## Prepare and use

1. From the kit root, run `python3 scripts/export_grok.py --check` with Python 3.11+. If stale, review the source changes and regenerate locally with `python3 scripts/export_grok.py`. No network or upload occurs. The export embeds source hashes, policy, 17 skills, technical references, role playbooks, blank context/plan templates and license notices. Local prose links are rewritten; task history, approvals, journals and current state are excluded.
2. Review [agent-kit-reference.md](agent-kit-reference.md) and the project material you intend to share. Attach the reference manually to a new Grok chat when authorized to send that content. The kit does not upload anything or alter account/global instructions. File/context limits depend on the actual client/account; no universal size limit or automatic import is assumed.
3. Supply the bounded task and only authorized project evidence, then use [bootstrap.md](bootstrap.md). For a Project with an available instructions field, the same bootstrap can be pasted manually, but that UI and persistence have not been verified. A fresh chat attachment is the baseline path.
4. Review the plan and approve it before requesting implementation proposals. If local write/command tools are unavailable, Grok returns proposed patches/check commands and unsaved state/journal notes. A human or authorized coding client applies changes and reports actual results. Conversational role changes are not native delegation or independent review.

The export uses a SHA-256 source snapshot rather than a Git HEAD, so source edits invalidate it even before commit. Regenerate after shared policy/skill/reference/role changes, verify with `--check`, and replace older attachments in the next working session. A stale attachment cannot update itself. Confirm content use through a bounded task that cites the applicable section; do not treat an assistant's claim that it “loaded” the kit as discovery proof. If a client rejects or cannot use the full reference, stop and record that limit; do not claim coverage from a partial upload.

## Evidence and sources

Local generation and freshness can be verified without a Grok account. Upload, retrieval, instructions persistence, role adherence and tool access remain **NOT_RUN** until observed separately. No account changes, source upload or external writes are authorized by this guide.

[Official Grok FAQ](https://docs.x.ai/grok/faq) documents web/app uploads including Markdown. It does not establish automatic repo discovery, local `@AGENTS.md` expansion or registration of native local skills/subagents on consumer Grok. Source review: 2026-11-12.
