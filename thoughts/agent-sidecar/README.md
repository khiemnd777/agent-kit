# Agent Sidecar

**Independent execution for Agent Kit V2. Version 0.1.0 — source release candidate.**

Agent Kit decides the goal, scope, authority and acceptance. Sidecar executes a
reviewed repeatable work package, runs its fixed steps without LLM orchestration,
and returns bounded results and verifiable evidence. It is not an agent harness.

```text
User's actual approval / host permissions
                    |
Coding Agent following Agent Kit V2
  DIRECT | REASON | WAIT | DELEGATE
                            |
       sidecar delegate --confirm-authorized ...
                            |
      Admission -> fixed snapshot -> reviewed DAG
                     /                  \
            independent step       independent step
                     \                  /
                  dependent steps
                            |
       one result + artifacts, or actionable exceptions
                            |
          Coding Agent interprets; user accepts
```

No Swamp dependency, LLM API, subscription, external account, daemon, webhook,
Git write or automatic installation. Agent Kit V2 stays unchanged in a separate
repository. **Read [SECURITY.md](SECURITY.md) before enabling process execution.**

## Start

Python **3.11+** is the implementation runtime. The earlier Go stack suggestion
was not a fixed implementation constraint. This release uses the V2 Python JSON
canonicalization and validator directly instead of inventing a second profile.
Dependencies are pinned: `jsonschema==4.26.0`, `PyYAML==6.0.3`.

From this source directory, in an environment you authorize:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
sidecar --version
sidecar capabilities --registry ./workflows
```

Alternatively, after installing `requirements.txt`, use `python3 sidecar ...`.
The source launcher does not install anything. Installation needs normal package
access; runtime builtin execution uses only local data. Workflows are supplied
in this source tree; always pass their registry path when running elsewhere.

Vietnamese guide: **[Bắt đầu](docs/START-HERE.vi.md)**.

## A real one-call delegation, before coding

This demo only reads the included synthetic source; it never executes its code.
Choose an empty private working directory **outside the source being inspected**.
Policy setup happens once after reviewing the selected workflow, not every step.

```sh
WORK="$(mktemp -d)"
SOURCE="$(pwd)/examples/demo-project"

python3 sidecar policy --registry ./workflows \
  --workflow repo.prepare --repository "$SOURCE" \
  --output "$WORK/policy.json"

# Only after the current scope actually authorizes this work package:
python3 sidecar delegate --registry ./workflows \
  --workflow repo.prepare --source "$SOURCE" \
  --state "$WORK/state" --policy "$WORK/policy.json" \
  --inputs ./examples/prepare-inputs.json \
  --scope-id demo-source-inspection \
  --decision-ref 'local-user-approved:demo-read-only-inspection' \
  --objective 'Inventory selected paths and extract declared entrypoints' \
  --confirm-authorized --output "$WORK/result.json"
```

The command pins the snapshot/workflow/runtime, records the caller's existing
request-scoped authorization, executes both independent steps, and returns **one
terminal result**. It does not ask a model which command to run next. The approval
reference above is an example: it must identify a real authorization in actual use.
The flag is an attestation, **not** human identity authentication or a new permission.

The result uses the unchanged Agent Kit V2 `0.1.0` draft shape. Detailed source
inventory and entrypoints live in hashed artifacts, not the agent's initial
context. Request/permit records are retained under `state/requests/`; completed
runs also retain their request, capability, policy, workflow and evidence.

Use `prepare -> authorize -> run` instead when the request needs separate review
or a stable ID for retrying transport delivery. Reissuing `delegate` creates a
**new** request. After a lost response, inspect history; do not blindly issue a
new delegation. Repeated `run` with the same completed request returns the verified
previous result without rerunning it. Interrupted/in-flight claims block replay.

## Included workflows

| Capability | WHEN | Execution |
| --- | --- | --- |
| `repo.prepare` | Before investigation/planning, or before another stable source-inspection block | Inventory/hashes and source-declared entrypoints; builtin only |
| `agentkit.integrity` | Repeated V2 package integrity inspection | Manifest hashes + skill mirrors; builtin only; not the full kit verification |
| `agentkit.verify` | At an approved coherent verification point | The four V2 maintenance commands in private copies; explicit trusted-process permission |

Do not use Sidecar merely to wrap a single adequate command. Architecture,
unknown bug diagnosis, requirement decisions and semantic acceptance stay with
the Coding Agent and user. See [WHEN and use cases](docs/WHEN.md).

## Implemented

- Strict bounded YAML/JSON workflows; duplicate-key, alias, cycle and unknown-field rejection.
- Local registry with exact byte digests; only reviewed and policy-pinned capabilities run.
- Content-addressed snapshots including uncommitted/untracked non-excluded inputs.
- DAG scheduling, bounded concurrency, success/always dependency conditions.
- Builtin read-only checks; optional trusted POSIX process executor with argv (no implicit shell).
- Request/global and step deadlines, SIGINT/SIGTERM handling, process-group termination.
- Explicit transient-exit-code retries, never unconditional retry-until-green.
- Request-bound local permits, expiry and runtime/policy/snapshot mismatch rejection.
- Exactly-accounted required checks, bounded evidence, artifact hashes and terminal states.
- Atomic run records, history and duplicate-request protection. No unsafe automatic resume.
- Compact machine-readable return; detailed artifacts remain local and are read on demand.

## Deliberate limits

**No OS/container/network sandbox.** Builtins do not run repository code. Process
mode is disabled unless explicitly enabled for trusted code. A private copy,
minimal environment and executable pin do not constrain a malicious child process.
Do not use this release to execute untrusted PRs or production commands. Network
and source-write effects are not supported; in trusted-process mode their absence
is a policy obligation, not kernel-enforced isolation.

No multi-user authentication, signed remote permits, scheduler, distributed workers,
LLM reasoning, workflow generation, conversation-history mining, automatic release,
resume after crash, general result cache or CPU/memory/disk cgroups. Workspaces are
private **per step**; steps do not share writable build output. Dependency ordering
and evidence aggregation work; a multi-step mutable build pipeline needs a separately
reviewed workspace design. Only `content_digest` snapshots are supported in this release.

There are no measured native-client token savings. Builtin-only runs invoke no
models; usage for arbitrary process steps is unknown, not fabricated zero.

## Verify

```sh
python3 tools/verify.py --out /tmp/sidecar-test-evidence

# Optional: execute trusted local V2 maintenance scripts in copies, then call
# the ORIGINAL V2 contract validator on actual Sidecar results.
python3 tools/interop.py \
  --agent-kit /absolute/path/to/agent-kit-v2 \
  --out /tmp/sidecar-v2-interop \
  --confirm-trusted-code
```

Use fresh output directories for interoperabilty runs. Full observed evidence and
limitations are in [verification](docs/VERIFICATION.md) and [handoff](HANDOFF.vi.md).

## Documentation

[Architecture](docs/ARCHITECTURE.md) · [Contract profile](docs/CONTRACT.md) ·
[Agent Kit integration](docs/AGENT-KIT-INTEGRATION.md) ·
[Workflow authoring](docs/WORKFLOWS.md) · [Security](SECURITY.md) ·
[Operations](docs/OPERATIONS.md) · [Sources / license](THIRD_PARTY_NOTICES.md)

MIT. No remote repository has been created or changed as part of this delivery.
