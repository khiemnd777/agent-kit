# WHEN — decision, delegation and return of control

These are Agent Kit policies, not hooks or background monitoring. No runtime
in this repository observes the user's IDE, Git events or conversation history.

| Moment | Owner action | Executor action | Return to owner |
| --- | --- | --- | --- |
| A request arrives | Understand outcome; identify known block; confirm scope/authority | None before invocation | Not applicable |
| An approved repeatable block is ready | Choose smallest adequate route; hand off the whole block | Execute within fixed contract if available | One compact completed/blocked/exception result |
| A novel feature exposes a stable subproblem | Reuse an existing recipe or command without handing over product decisions | Execute that subproblem | When its outcome is ready or needs a decision |
| Inputs or constraints change materially | Re-evaluate only affected route/evidence | Do not silently reinterpret the old intent | Escalate incompatible changes |
| Expected technical failure occurs | No step-by-step involvement if safe handling was predeclared | Apply bounded safe retry/cleanup | Report attempts and final outcome |
| Assertion fails, authority is missing, or effects are uncertain | Reason or ask the actual decision maker | Stop dependent work; preserve evidence | Failure, escalation or blocked result |
| User stops | Respect stop; request supported cancellation if a real executor exists | Acknowledge and settle if supported | Report confirmed versus unknown in-flight effects |
| Required evidence is sufficient | Interpret and hand off | No new work | Human acceptance remains separate |

## Example A — repeatable work at task entry

The user requests an authorized inventory of 15 repositories. The owner already
knows a reviewed capability that reads metadata, detects stack/test commands and
produces a bounded report. It sends one request for the fixed repository snapshots.
The executor handles its internal fan-out and aggregation. The owner reads the
summary and only investigates anomalies. No LLM chooses the next command for
each repository. This is a future DELEGATE path, not a runnable V2 feature.

Without that executor, an adequate existing batch script is DIRECT. Do not build
Sidecar to complete the inventory incidentally or claim that direct tool use is
already Sidecar execution.

## Example B — new feature with repeatable blocks

The owner reasons about the feature and approval. At a suitable boundary it can
hand off a stable source inventory or fixture-validation block, continue novel
implementation, and later hand off a verification bundle. Each handoff covers an
outcome, not a single command. Long/complex/UI code-before-tests ordering and
existing project requirements remain binding.

## Example C — exception, not an automatic reasoning loop

A verification result contains one assertion failure and successful independent
checks. The owner reads the failing evidence, diagnoses and repairs within scope.
Only invalidated checks run again. Do not reopen every passed check just because
another block failed. A missing runtime/dependency is NOT_RUN/BLOCKED, not an
assertion failure. A timeout with unknown side effects is not a safe retry signal.

## Example D — Sidecar does not exist yet

This package has no external executor installed. The owner does not poll a
fictional registry, create a placeholder success report or invoke a made-up CLI.
It uses existing tools under the same scope or states the unmet prerequisite.
The contract examples are design/test fixtures, not integration results.

## Never trigger by these facts alone

A file was edited; a message arrived; a commit exists; an agent changed; the
context was compacted; a timer elapsed; a workflow once passed. None proves
readiness, authority, invalidated evidence, task completion or human acceptance.
