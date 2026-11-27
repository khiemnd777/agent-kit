# Optional roles and model selection

One delivery owner is sufficient. Delegate to explorer, implementer or reviewer
only when bounded work and coordination benefit justify it under actual authority.
Children do not redelegate and do not acquire broader permissions through a role.

Generated adapters retain V1 role identities. Codex adapters omit model/effort and
sandbox overrides. Markdown adapters for Claude/Gemini/Cursor use `model: inherit`
as in the inspected source and omit tool/MCP/permission overrides. This records
source intent, not verified effective model or permission behavior.

Client defaults, managed configuration and host restrictions remain authoritative.
Do not infer effective model identity from the LLM's self-report. The supplied
adapters must be observed in their actual client before native behavior is claimed.
