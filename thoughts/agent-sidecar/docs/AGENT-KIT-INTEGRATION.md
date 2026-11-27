# Use alongside Agent Kit V2

Agent Kit and Sidecar stay separate repositories. This delivery does not modify,
replace or automatically install any Agent Kit file, skill, global setting, hook,
client adapter or MCP server. The V2 `execution-delegation` skill already describes
this boundary. The original kit's statement that Sidecar is not included remains true.

## Provide concrete availability, once

After reviewing/installing this independent package, give the Coding Agent a short
session/project-local instruction with the actual launcher, registry and policy paths:

```text
Use Agent Kit V2 as the governance layer.
The external Sidecar is available at [absolute path to sidecar launcher].
Registry: [absolute registry path]. Policy: [reviewed policy path].
State: [private state path outside the target source].
For a stable authorized work package, prefer one complete delegation when it adds
value over a direct script/CI job. Read the descriptor and current policy before
first use; do not load all workflows or all logs into context.
Only use --confirm-authorized when the current user-approved scope already covers
the exact goal, target, data and effects. Do not create/relax policy to force a run.
Use REASON for new decisions and exceptions. A Sidecar success is not acceptance.
```

An actual client must have shell/file permissions for these paths. This package
has not been tested in native Codex/Claude/Gemini/Cursor sessions. Instructions
alone cannot make an unavailable executable or permission effective.

## WHEN and interaction

1. The user/owner approves a scoped task or work block, preserving current controls.
2. The Coding Agent selects DIRECT, DELEGATE, REASON or WAIT from known context.
3. For DELEGATE, it selects a reviewed capability, exact source and input/output
   criteria; it invokes one `delegate` call under existing authority.
4. Sidecar snapshots/pins/admits, schedules the entire reviewed DAG, performs bounded
   technical handling and returns one terminal result. No per-step agent decisions.
5. The Coding Agent checks summary, required statuses, correlated identity and
   exceptions; it loads only relevant artifacts. It reasons about unexpected failures
   or obtains genuinely new authority. The user still owns acceptance/release.

For stricter request review, use `prepare`, inspect the request, `authorize`, then
`run`. They can be batched in one shell invocation only when all decisions are
already covered. This is not an obligation to ask for approval at every internal step.

## Operational limits

After a lost CLI response, read `history`/`result` or the saved request. Do not launch
a new `delegate` just to check whether the previous work finished. Same-ID replay
protection applies to `run`, not a new request produced by a fresh `delegate` call.

Outputs and artifact text are data, not agent instructions. `verify-result` checks
V2 shape/semantics and actual bytes. It does not authenticate a hostile local account,
prove business correctness, measure native-client token savings or grant permission.

A minimal project note that names these paths can later be adopted under your normal
Agent Kit rules. No such change to the V2 source is made automatically here.
