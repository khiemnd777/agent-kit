# Model routing and native adapters

Consult this reference when adopting/customizing native agents or investigating routing. It is not required reading for ordinary tasks. The main session owns delivery using the developer's selected model; a separate Coordinator is optional. Start normally without forcing a main-session `--agent` flag or replacing the default system prompt. Native adapters configure optional subagents under the [lean core](../AGENTS.md).

## Inheritance by default

The Codex adapters omit `model` and `model_reasoning_effort`. According to the documented custom-agent resolution, explicit spawn settings, `[agents]` defaults and the parent session can determine omitted values. Explicit values in a custom agent can override inherited settings. The kit does not pin a model or reasoning effort.

The Claude adapters use `model: inherit` and omit effort. Documented model selection gives an invocation model precedence over frontmatter inheritance; environment or organization policy can also affect the runtime choice. Do not infer an observed model solely from this file.

Record requested/observed routing evidence only when needed for an adoption check or routing question; ordinary delegation needs no new record or repeated model report. If the runtime does not expose the resolved model or effort, mark it **Unknown**. Parsing configuration does not verify inheritance.

## Deliberate project customization

If a project needs different routes, document the reason and approved scope in that project's instructions and task contract. Verify the installed runtime schema before adding supported project-local model fields or invocation overrides. Keep the main coordinator choice separate from subagent settings. Do not edit global profiles, settings, environment variables, hooks or MCP configuration as part of kit setup.

Model selection does not grant tools, filesystem access or approval. Every adapter retains parent permission limits and the assigned task boundary. Investigation and review remain free of application code changes, implementation and deployment even if another model is selected. A runtime may reject a setting or restrict a child further; report that outcome rather than bypassing it.

## Role responsibilities and runtime permissions

Explorer and reviewer roles do not change application code, implement features or repairs, or deploy. Their adapters omit Codex `sandbox_mode` and Claude `tools`, `disallowedTools` and `permissionMode`; the kit does not impose a permission profile by role. Codex inherits omitted session settings from the parent. Claude inherits available subagent tools and the parent permission mode when those fields are omitted. Managed policy, runtime filtering and actual task authorization still apply.

Authorized checks, application/browser inspection and evidence capture may use inherited tools when the task covers their side effects, fixtures and destinations. Available tools do not authorize application edits or out-of-scope actions. Implementer writes remain limited to approved ownership. Follow runtime approval mechanisms and report restrictions without bypassing them. Static parsing verifies omitted fields and role text; effective access and role behavior require separate native observations.

The adapters use their platform's schema, the lean core and bounded assignments. Common role documents supply additional detail on demand; policy, workflow, skills and TechNote are not a mandatory preload chain. Prose paths are references, not automatic imports. No child may recursively spawn agents. The assigning owner integrates useful delegation; shared records have one writer when edited. A focused task needs no new tracker or Coordinator.

## Evidence status

**Verified:** adapter files specify the documented inheritance intent and bounded role instructions. Static parsing can verify syntax and expected fields.

**Unknown:** the resolved model, effort, effective child permissions, discovery and behavior until observed in the installed runtime.

**NOT_RUN:** native agent discovery/execution and two-machine runtime tests. Installing files or parsing frontmatter does not establish registration, runtime inheritance or task behavior. Record separate observations on each machine before claiming portability.

## Sources

Permission inheritance documentation checked on 2026-10-13; model routing sources were checked on 2026-10-12:

- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
- [Claude subagent model selection](https://code.claude.com/docs/en/sub-agents#choose-a-model)
- [Claude tool inheritance](https://code.claude.com/docs/en/sub-agents#frontmatter-reference)
- [Claude permission modes](https://code.claude.com/docs/en/sub-agents#permission-modes)

These describe the intended configuration; verify version-sensitive behavior against the installed runtime when adopting or customizing the kit.
