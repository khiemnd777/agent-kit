# Model routing and native adapters

The Project Coordinator is the main session using the developer's selected model. Start the main session normally. Do not force a main-session `--agent` flag or replace the default system prompt to use this kit. The role documents describe responsibilities; native adapters configure optional subagents.

## Inheritance by default

The Codex adapters omit `model` and `model_reasoning_effort`. According to the documented custom-agent resolution, explicit spawn settings, `[agents]` defaults and the parent session can determine omitted values. Explicit values in a custom agent can override inherited settings. The kit does not pin a model or reasoning effort.

The Claude adapters use `model: inherit` and omit effort. Documented model selection gives an invocation model precedence over frontmatter inheritance; environment or organization policy can also affect the runtime choice. Do not infer an observed model solely from this file.

For each delegated task, report the requested route and the runtime-observed model when the tool exposes it. If the runtime does not expose the resolved model or effort, mark the value **Unknown**. Do not claim inheritance was verified from a successful configuration parse.

## Deliberate project customization

If a project needs different routes, document the reason and approved scope in that project's instructions and task contract. Verify the installed runtime schema before adding supported project-local model fields or invocation overrides. Keep the main coordinator choice separate from subagent settings. Do not edit global profiles, settings, environment variables, hooks or MCP configuration as part of kit setup.

Model selection does not grant tools, filesystem access or approval. Every adapter retains parent permission limits and the assigned task boundary. Read-only work must remain read-only even if another model is selected. A runtime may reject a setting or restrict a child further; report that outcome rather than bypassing it.

## Permission adapters

Codex explorer and reviewer adapters request `sandbox_mode = "read-only"`. Confirm the installed runtime accepts and actually applies that field before relying on the restriction. A parse check alone does not verify an effective sandbox override. Claude explorer and reviewer adapters allow only `Read`, `Glob` and `Grep`; they omit shell, editing and mutation connector tools. Implementers inherit available tools and permissions, while instructions limit writes to approved ownership. This inherited access is not an additional grant.

The adapters use their platform's schema and explicit instructions to read common role documents. Paths in prose are instructions to read files; they are not an automatic import mechanism. No child may recursively spawn agents. The Project Coordinator alone assigns delegated work and updates shared coordination documents.

## Evidence status

**Verified:** adapter files specify the documented inheritance intent and bounded role instructions. Static parsing can verify syntax and expected fields.

**Unknown:** the resolved model, effort, effective child permissions, discovery and behavior until observed in the installed runtime.

**NOT_RUN:** native agent discovery/execution and two-machine runtime tests. Installing files or parsing frontmatter does not establish registration, runtime inheritance or task behavior. Record separate observations on each machine before claiming portability.

## Sources

Official documentation checked on 2026-10-12:

- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
- [Claude subagent model selection](https://code.claude.com/docs/en/sub-agents#choose-a-model)

These describe the intended configuration; verify version-sensitive behavior against the installed runtime when adopting or customizing the kit.
