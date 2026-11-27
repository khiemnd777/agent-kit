# Client compatibility and evidence limits

Status: **authored source and static package validation only**. No native client
session, account change, installation or permission test was performed for V2.

| Client | Entry / skills | Optional roles | Runtime evidence |
| --- | --- | --- | --- |
| Codex | AGENTS.md / .agents/skills | .codex/agents/*.toml | NOT_RUN |
| Claude Code | CLAUDE.md imports AGENTS.md / .claude/skills | .claude/agents/*.md | NOT_RUN |
| Gemini CLI | GEMINI.md imports AGENTS.md / canonical skills | .gemini/agents/*.md | NOT_RUN |
| Cursor | AGENTS.md / canonical and compatibility discovery | .cursor/agents/*.md | NOT_RUN |
| Grok web/app | Manual generated reference | No native repository runtime supplied | NOT_RUN |

Formats/identities follow inspected V1 adapters; current effective client behavior
must be verified in an authorized real session. Source equality is not discovery,
invocation, deduplication, model identity or access-control proof. Client-specific
settings and versions can affect discovery. Do not delete Claude mirrors or change
global settings to force a pass. Inspect personal/managed/plugin source collisions.

When adoption or a concrete discovery issue warrants it, observe effective loaded
paths, selected roles and actual permissions. Source and static tests are separate
from native behavior. The kit supplies no installers, hooks, account configuration,
startup scans or automatic integrations. Chat-only file attachment does not grant
shell access, registered skills, native subagents or a Sidecar.

Upstream adapter baseline: Agent Kit commit
`df3b058a52acc9ea10a7556733baae44ac12d1f2`. An official Codex skills source was
consulted during package preparation: https://learn.chatgpt.com/docs/build-skills .
This establishes documentation guidance, not a successful native V2 invocation.
