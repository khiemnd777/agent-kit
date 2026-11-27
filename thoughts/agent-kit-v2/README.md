# Agent Kit V2

## Decision & Governance

**Decide the work. Authorize its scope. Delegate repeatable execution. Reason about exceptions.**

Agent Kit is a repository-local operating kit for coding agents. V2 separates
engineering decisions from mechanical execution without embedding an execution
engine. The independent Sidecar is a future project, **not included or required**.

```text
User / Product Owner
       | goals, approval, acceptance
Coding agent following Agent Kit V2
       | decision, scope, authority, acceptance criteria
       +-- DIRECT ----> existing command / script / configured CI
       +-- REASON ----> investigation / implementation / interpretation
       +-- DELEGATE --> external Sidecar [NOT IMPLEMENTED HERE]
       |                complete work package -> evidence / exceptions
       +-- WAIT ------> missing decision, authority, prerequisite or human stop
```

**Version:** 2.0.0 source candidate. Package checks are described in
[verification results](docs/verification-results.md). Native client behavior,
Sidecar interoperability and token savings are not established by those checks.

## Start here

Open this directory in your coding client. The agent reads `AGENTS.md`; existing
project instructions must be reconciled, not overwritten blindly.

```text
Use Agent Kit V2 for [project/task]. Inspect relevant source and propose the
scope, acceptance and checks. Preserve existing project rules and my approval
boundaries. Use existing tools for repeatable work; no Sidecar is installed.
Do not create a repository, publish, deploy, or add a runtime without approval.
```

For a new application, initialize its own context/plan/state from the templates.
The kit's delivery records are **not** the application's approval or test evidence.
For Vietnamese onboarding, read [Bắt đầu](docs/START-HERE.vi.md).

## What changed

| V1 pattern | V2 behavior |
| --- | --- |
| Agent repeatedly coordinates known tool steps | Delegate a complete stable block, or batch existing direct tools |
| Verification is the main automation example | Consider repeatable work at task entry and at any stable block |
| Mandatory WHAT/skills percentages/visual handoffs for all tasks | Proportional reporting; no fabricated participation percentages |
| Governance repeated across roles/skills | One operating core; focused on-demand guidance |
| Runtime integration is unspecified | Versioned draft request/result/capability contracts with offline checks |
| Historical records can dominate context | Fresh adopter records, one live checkpoint, focused evidence reuse |

Approval, data safety, human stops and roadmap acceptance boundaries remain.
See the complete [migration guide](docs/migration-v1-v2.md).

## Included

- A lean governance core and decision/authority/delegation policies.
- Seventeen adapted technical skills plus one new `execution-delegation` skill.
- Canonical `.agents/` sources and byte-matched `.claude/` mirrors.
- Optional explorer, implementer and reviewer adapters for Codex, Claude,
  Gemini and Cursor; a generated manual Grok reference.
- Draft execution contracts, synthetic examples and offline validation tools.
- Package tests, source provenance, acceptance scenarios and a benchmark plan.

## Not included

No Sidecar implementation, workflow registry service, DAG runner, tool executor,
scheduler, event listener, runtime connector, LLM gateway, account configuration
or automatic installation. The maintenance scripts validate and generate kit
files; they do not execute user tasks. No Swamp source is included.

## Verify this package

Python 3.11+ is needed only for maintenance, not for using the instructions.
Install the development requirements in your own environment when authorized;
the checker does not install anything automatically.

```sh
python3 scripts/sync_assets.py --check
python3 scripts/export_grok.py --check
python3 scripts/verify_package.py
python3 -m unittest discover -s tests -v
```

`verify_package.py` requires the libraries listed in `requirements-dev.txt`.
Missing required dependencies produce a nonzero exit, never a false PASS.
See [verification guide](docs/verification-guide.md) for scope and limitations.

## Read only what you need

| Need | Document |
| --- | --- |
| Approval and risk | [Policy](docs/team-policy.md) |
| WHEN to route and return control | [Invocation timing](docs/execution/when.md) |
| Delegate a complete block | [Delegation policy](docs/execution/delegation-policy.md) |
| Future executor boundary | [Execution contracts](contracts/README.md) |
| Results and escalation | [Evidence policy](docs/execution/evidence-policy.md) |
| Delivery and handoff | [Workflow](docs/team-workflow.md), [handoff](docs/handoff-templates.md) |
| Choose a focused skill | [Skill catalog](docs/skills-catalog.md) |
| Native adapters and known limits | [Compatibility](docs/agent-compatibility.md) |
| Adopt V2 / compare savings | [Migration](docs/migration-v1-v2.md), [benchmark](docs/benchmark-plan.md) |
| Review this delivery | [Build record](docs/delivery/V2-BUILD.md) |

## Source and license

This is a curated V2 rebuild from `khiemnd777/agent-kit` at
`df3b058a52acc9ea10a7556733baae44ac12d1f2`, not a full V1 archive or a new remote
repository. MIT license; upstream notices and traceability are retained in
[provenance](docs/skills-provenance.md) and [third-party notices](THIRD_PARTY_NOTICES.md).
