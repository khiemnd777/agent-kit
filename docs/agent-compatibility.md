# Runtime compatibility

**Status: authored configuration and static validation only. Native discovery, invocation, effective model/permission behavior and two-machine checks are NOT_RUN.** Check [verification results](verification-results.md) for the actual package evidence.

## Runtime adapters

| Capability | Codex | Claude Code |
| --- | --- | --- |
| Shared project instructions | AGENTS.md | CLAUDE.md with literal @AGENTS.md import |
| Repository skills | .agents/skills | .claude/skills |
| Native custom agents | .codex/agents/*.toml | .claude/agents/*.md |
| Default model intent | Omit model and model_reasoning_effort in native definitions | model: inherit; omit effort |
| Read-only role intent | Read-only sandbox plus role restrictions | Explicit Read, Glob, Grep tool list plus role restrictions |

The literal import in CLAUDE.md is outside a code block. Claude's current AGENTS.md support has client/version and settings conditions; the import keeps one policy source without copying its body.

Codex project-layer loading depends on project trust and client support. Managed settings and live parent permissions can affect the result. A read-only sandbox concerns local execution; inherited connectors and parent overrides still require an effective-permissions check. Claude's read-only agents have no shell, write/edit or connector tools in their declared allowlist.

A written role playbook is not a native registered agent. Coordinator is the main session role and does not automatically become a native subagent or replace the client's main system prompt.

## Discovery and overrides

Inspect the client's available repository skills and custom agents, including effective source paths. Identify personal/managed/plugin duplicates instead of assuming the repository copy is active. Do not change global configuration to make a test pass.

Record client version, account/provider availability and observed settings without exposing credentials. Supported effort levels and model aliases vary. Do not infer runtime model identity from what the language model says about itself.

Fresh sessions from a completed checkout are preferred for initial discovery checks. Reload/restart only if the client requires it after a definition changes; do not claim universal hot reload. If delegation is unavailable, apply roles sequentially and mark native checks NOT_RUN.

Models, tools and context are local to each runtime. Cross-tool continuation uses [shared Git documents](team-workflow.md), not native messages or shared chat history. TOML/YAML adapters require semantic review; checksum equality is only for skill mirrors.

## Official sources

Source review date: 2026-10-12. These references establish authoring mechanisms, not successful execution of this kit.

- [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)
- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
- [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Claude shared instructions](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools)
- [Claude skills](https://code.claude.com/docs/en/skills)
- [Claude custom agents](https://code.claude.com/docs/en/sub-agents)
- [Claude models](https://code.claude.com/docs/en/model-config)

Verify these mechanisms against the client versions used in your two-machine run before claiming compatibility.
