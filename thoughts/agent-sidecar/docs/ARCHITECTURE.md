# Architecture and implementation decisions

## Accepted boundary

**Agent Kit — Decision & Governance -> Sidecar — Execution & Optimization.**
Two repositories; a contract connects them. Agent Kit remains instructions/skills
executed by a Coding Agent. Sidecar is an actual execution runtime. It never decides
business scope, obtains new authority from metadata, marks human acceptance, rewrites
application code after failures, or asks an LLM how to schedule each DAG step.

## Components

| Module | Responsibility |
| --- | --- |
| `cli.py` | One-call `delegate` and separate prepare/authorize/run; structured terminal return |
| `registry.py` | Workflow schemas, exact pins, input schemas and DAG validation |
| `snapshots.py` | Bounded local snapshot and private working-copy creation |
| `policy.py` | Policy/permit admission, expiry, executable and runtime fingerprints |
| `executors.py` | Pure builtin checks or explicitly trusted host subprocesses |
| `engine.py` | DAG scheduling, deadline/cancellation, evidence, claims and terminal result |
| `contract.py` + `contracts/` | V2's draft schemas and semantic checker |
| `io.py` | Strict bounded parsing, path containment, hashes and atomic local writes |

The registry is a directory, not a server. State is a private directory, not Redis,
a database service or daemon. No application knows Sidecar's internal Python modules;
the stable boundary for this release is the CLI and the supported V2 draft profile.

## Author once; execute repeatedly

A maintainer writes/reviews a workflow and its input/check definitions once. The
owner selects/pins it in a local policy. Every request supplies a goal and inputs,
not a freshly generated DAG or the full agent conversation. The engine uses code to
run fixed dependencies, retries and result aggregation. New reasoning is needed
only for choosing the work block, resolving exceptions or interpreting acceptance.

The tool does not promise universal token savings. The useful unit is a stable work
package, not a file edit. `repo.prepare` demonstrates delegation *before coding*;
`agentkit.verify` demonstrates independent checks followed by dependent verification.

## Implementation choice

Python 3.11+ was chosen for this release. The already-delivered V2 contract defines
its digest using Python JSON serialization and includes a Python semantic validator.
Reusing that MIT contract boundary avoids a new canonicalization dialect or a bespoke
partial JSON Schema engine. PyYAML and jsonschema use the same exact versions listed
by V2. Go was an earlier proposal, not an accepted stack constraint. A future Go
runtime must prove the same semantics and canonicalization rather than silently
switch profiles. No Go runtime or build is claimed here.

## Evidence/availability boundaries

The source contracts were draft/design-only in V2. This Sidecar implements a documented
subset and has actual local interoperability tests; it does not retroactively make
all possible V2 contract combinations, coding clients or host permission models verified.

Execution optimization in this release is code-driven DAG scheduling, concurrency,
bounded output, safe transient retries and duplicate delivery protection. No general
cross-run cache, hidden agent, history mining or measured token optimization is claimed.
