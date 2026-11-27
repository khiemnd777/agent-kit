# WHEN to use the Sidecar

| WHEN | Decision owner | Action |
| --- | --- | --- |
| A new task contains a stable, reviewed source-inspection block | Coding Agent under Agent Kit | DELEGATE `repo.prepare` before reasoning that needs those facts |
| A mixed task reaches another stable multi-step block | Coding Agent | Delegate the whole block once, not one call per command |
| One existing shell command/script/CI job is sufficient | Coding Agent | DIRECT; avoid Sidecar overhead |
| Requirements, architecture or unknown root cause need judgment | Coding Agent/user | REASON; Sidecar does not replace this work |
| Scope, current authority, capability or environment is missing | Coding Agent / admission guard | WAIT or structured blocked result |
| Independent DAG dependencies are ready | Sidecar | Start within the concurrency cap, with no LLM decision |
| A dependency failed | Sidecar | Dependent success-only checks remain NOT_RUN; independently allowed steps continue |
| A step declares `when: always` and its dependencies have terminated | Sidecar | Run the approved step, unless the whole request was stopped/expired |
| A reviewed safe-read-only step returns an explicitly listed transient exit code | Sidecar | Retry within the attempt and time budgets |
| A product assertion returns failure, effects are unknown, or a new decision is needed | Sidecar -> Coding Agent | Return FAIL/escalation; no unapproved repair or retry-until-green |
| The user/host sends SIGINT/SIGTERM or the budget expires | Sidecar | Stop dispatch, terminate in-flight process groups and report uncertainty honestly |
| The workflow passes | Coding Agent -> User | Interpret evidence; do not equate execution success with human acceptance |

## Before-coding example

User approves examining a repository before deciding a change. The Coding Agent
uses the existing `repo.prepare` capability in one `delegate` call. Sidecar snapshots
the actual dirty/untracked source, inventories the selected paths, reads declared
entrypoints, and returns a compact result. The agent then reasons from the relevant
artifacts. No model is asked to schedule inventory vs manifest extraction.

## Verification example

After a coherent approved change, the agent delegates `agentkit.verify`. Sidecar
runs sync and export checks independently, then package verification, then the test
suite. A package failure prevents dependent regression from being presented as PASS.
The agent reads the failure evidence rather than orchestrating each command.

## Do not generalize these examples

A small inventory can be cheaper as one script. Existing CI should not be duplicated
just to use a new framework. Compare equivalent work/evidence, include first-time setup
and policy maintenance, and use native-client usage telemetry for token claims.
