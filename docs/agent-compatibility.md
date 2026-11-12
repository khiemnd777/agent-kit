# Runtime compatibility

**Status: authored configuration and static validation only. Native discovery, invocation, effective model/permission behavior and two-machine checks are NOT_RUN.** Check [verification results](verification-results.md) for the actual package evidence.

## Runtime adapters

| Capability | Codex | Claude Code | Gemini CLI | Cursor | Grok web/app |
| --- | --- | --- | --- | --- | --- |
| Shared instructions | AGENTS.md | CLAUDE.md imports @AGENTS.md | GEMINI.md imports @AGENTS.md | Root AGENTS.md | Manual reference attachment |
| Skills | .agents/skills | .claude/skills | .agents/skills | .agents/skills; compatibility discovery also sees .claude/skills | Embedded reference sections, not registered skills |
| Native custom agents | .codex/agents/*.toml | .claude/agents/*.md | .gemini/agents/*.md | .cursor/agents/*.md | Not supplied; conversational roles only |
| Model intent | Omit model/effort | model: inherit; omit effort | model: inherit; omit tuning overrides | model: inherit; omit tuning overrides | Human's selection; no routing config |
| Role/permission intent | Bounded role text; omit sandbox override | Bounded role text; omit tool/permission overrides | Same role text; omit tools/MCP overrides | Same role text; omit readonly/background overrides | No local access or execution inferred from attachment |

### Gemini CLI and Cursor adoption

The three new adapters per client preserve the existing role names, descriptions and instruction bodies. Gemini uses the documented Markdown/YAML custom-agent schema; omitted tool fields inherit parent-session availability according to the documentation. Cursor native `.cursor/agents/` definitions take precedence over same-name Claude/Codex compatibility definitions. Neither configuration establishes effective permissions or actual model identity without observation. No global settings or client feature toggles are shipped; check the installed version if discovery fails.

Gemini discovers `.agents/skills/` as the workspace alias, with precedence over `.gemini/skills/` at the same tier. Cursor documents both `.agents/skills/` and `.claude/skills/` discovery, so this kit's existing Claude mirror may produce same-name candidates. They remain byte-identical; **effective skill source/deduplication is Unknown** until inspected in Cursor. Do not report 34 distinct skills or add another `.cursor/skills/` mirror. Check the selected path, preserve Claude support and report a loading issue rather than changing global config or deleting mirrors.

For Gemini, inspect `/memory show` and `/skills list` in an authorized native check to confirm imported core and canonical skills. For Cursor, inspect the available skills and native roles/effective sources in the actual client. Those commands/UI observations have **NOT_RUN** here; official documentation is authoring evidence only.

### Grok consumer web/app

Use the [manual guide](grok/README.md), [bootstrap](grok/bootstrap.md) and generated [reference](grok/agent-kit-reference.md). The export embeds shared policy, skill/reference content, playbooks and licenses so uploaded prose does not depend on local relative paths. It deliberately excludes maintenance approvals, task records, journals and current state. Its source snapshot hash and read-only freshness check detect stale exports. Local generation never uploads anything. File acceptance, retrieval, custom-instructions UI/persistence and workflow behavior remain **NOT_RUN**. Do not infer local repo access, native skill activation/subagents or shell execution from consumer chat attachments.

The literal import in CLAUDE.md is outside a code block. Claude's current AGENTS.md support has client/version and settings conditions; the import keeps one policy source without copying its body.

Codex project-layer loading depends on project trust and client support. Managed settings and live parent permissions can affect the result. Codex inherits omitted sandbox settings; Claude inherits available subagent tools and the parent permission mode when the corresponding fields are omitted. The kit does not force a permission profile by role. Runtime filtering and the approved task scope still govern tool use. Authorized checks and evidence capture do not grant application code changes, implementation or deployment. Observe effective permissions and role behavior separately.

A written role playbook is not a native registered agent. The main session normally owns delivery; a separate Coordinator is optional and does not replace the client's system prompt. All roles/skills use the lean AGENTS.md core; they consult policy/workflow detail only when relevant and follow the required planning → approval → implementation boundary without inventing extra per-file approvals.

## Discovery and overrides

Use these checks for initial adoption, a changed adapter or a concrete discovery/override problem. An ordinary task or new workflow stage does not require a compatibility audit. Inspect the client's available repository skills and custom agents, including effective source paths. Identify personal/managed/plugin duplicates instead of assuming the repository copy is active. Do not change global configuration to make a test pass.

Record client version, account/provider availability and observed settings without exposing credentials. Supported effort levels and model aliases vary. Do not infer runtime model identity from what the language model says about itself.

Fresh sessions from a completed checkout are preferred for initial discovery checks. Reload/restart only if the client requires it after a definition changes; do not claim universal hot reload. If delegation is unavailable, the main session can carry the task without a role ceremony; disclose self-review when relevant and keep native checks NOT_RUN.

Models, tools and context are local to each runtime. Cross-tool continuation uses the relevant source and one useful [checkpoint](tasks/README.md); runtimes do not share live messages or chat history. TOML/YAML adapters require semantic review; checksum equality is only for skill mirrors.

## Official sources

Source review date: 2026-10-12; permission/tool inheritance rechecked on 2026-10-13. These references establish authoring mechanisms, not successful execution of this kit. Gemini CLI, Cursor and Grok sources below were reviewed on 2026-11-12.

- [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)
- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
- [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Claude shared instructions](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools)
- [Claude skills](https://code.claude.com/docs/en/skills)
- [Claude custom agents](https://code.claude.com/docs/en/sub-agents)
- [Claude models](https://code.claude.com/docs/en/model-config)

Verify these mechanisms against the client versions under evaluation before claiming compatibility. A two-machine portability claim requires observations on both machines; it is not a prerequisite for a local source change.

- [Gemini context imports](https://geminicli.com/docs/cli/gemini-md/)
- [Gemini skill discovery](https://geminicli.com/docs/cli/skills/)
- [Gemini custom agents and schema](https://geminicli.com/docs/core/subagents/)
- [Cursor project instructions](https://cursor.com/docs/rules)
- [Cursor skill discovery](https://cursor.com/docs/skills)
- [Cursor custom agents, precedence and schema](https://cursor.com/docs/subagents)
- [Grok web/app file uploads](https://docs.x.ai/grok/faq)
