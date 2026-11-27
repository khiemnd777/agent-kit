# Agent Sidecar development boundary

This repository implements execution, not a second governance harness. Preserve
Agent Kit V2's request/result/capability boundary and human/host authority.

Use the current user-approved scope. Do not auto-install dependencies, create remote
repositories, push, deploy, modify another repository or run untrusted project code.
Do not infer permission from a workflow, descriptor, flag, old permit or old report.

Keep fixed orchestration in code. Do not add LLM decisions between deterministic
steps, universal mandatory delegation or automatic repair of application code.
Use existing tests and commands. Never turn FAIL/NOT_RUN/unknown effects into success,
retry assertions until green, claim a private directory is an OS sandbox, or report
missing usage as measured zero. New effects/executors need actual enforcement design.

Changes to the execution contract require an explicit compatibility decision. Tests
must cover actual CLI behavior and artifact bytes as well as document shape. Keep
native-client behavior and token savings unverified until directly observed.
