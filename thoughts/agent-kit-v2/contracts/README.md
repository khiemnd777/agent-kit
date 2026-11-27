# Execution boundary — contract draft 0.1.0

Status: **DRAFT / DESIGN-ONLY**. Agent Kit V2 is usable without these contracts.
No executor, transport, adapter, CLI, registry or Sidecar is implemented here.
The independent Sidecar will need its own implementation and interoperability
review. Contract shapes below are a V2 design, not Swamp syntax.

## Contract files

- `execution-request.schema.json`: outcome, pinned capability, target/snapshot,
  authorization reference, required evidence and resource/output bounds.
- `execution-result.schema.json`: terminal execution state, check observations,
  correlation, artifact references, exceptions and measured-or-unknown metrics.
- `capability.schema.json`: declared inputs/effects/replay semantics. A descriptor
  does not establish availability, approval, trust or runtime enforcement.

Schemas use JSON Schema Draft 2020-12. All top-level/defined objects reject
unknown properties. Capability-specific `inputs` are validated against the
capability's input schema, not guessed from the task text. This draft supports
source/scratch/network effects; financial/production effect protocols are not
implicitly included and would need separately designed controls.

## Request semantics

The request describes one complete stable work block, not a list of prompts to
ask an LLM. The owner pins the capability/version/digest, repository snapshot,
environment and policy. `content_digest` denotes an independently prepared
snapshot that includes relevant uncommitted/untracked inputs; a Git HEAD cannot
stand in for uncommitted work. Snapshot creation/isolation is not implemented here.

`authorization` records a reference to actual authorization, allowed effects,
logical path roots and expiry. It is **not** a token, signature or proof of
permission. `source:/` and `scratch:/...` are symbolic mounts; the future host
must resolve, contain and enforce them with real filesystem/network controls.
Network hosts are not permission to bypass DNS, redirects or network policy.
The future executor must reject a draft/unreviewed capability for live use.

## Result semantics

Request/result identity must match, including capability, snapshot and environment.
`request_digest` is SHA-256 of UTF-8 JSON encoded with sorted keys, no insignificant
whitespace and `ensure_ascii=False`, prefixed `sha256:`. This is a local draft
canonicalization profile, **not RFC 8785**, not a digital signature and not
cross-language interoperability proof. A production transport must settle its
canonicalization/authentication contract before adoption. Do not include secrets.

All required checks must be present and PASS for `succeeded`. A FAIL anywhere,
unresolved exception or unknown effect state prevents success. PASS/FAIL check
claims need artifact references. Referenced artifacts must be known; safe relative
paths and digests are declarations to verify at the runtime boundary, not files
proven to exist by schema validation. Do not automatically fetch arbitrary paths.

`blocked` may have no run ID and no start time. Cancelled/timed-out effects may be
unknown; reconcile before replay. Non-success results require actionable exception
information. `NOT_RUN` and `SKIPPED` need meaningful reasons. No field represents
human acceptance, release or newly granted permission.

Summary and evidence limits must not hide required checks, failures or uncertain
effects. Truncated log presentation retains a referenced evidence artifact.
Usage counters are null with a reason when unavailable; zero is measured zero.
Timestamps/usage in `examples/` are synthetic and prove no execution.

## Offline checks shipped with the kit

`python3 scripts/check_contract.py --request contracts/examples/request-inventory.json
--result contracts/examples/result-success.json --capability
contracts/examples/capability-inventory.json` (one shell command).

The tool validates document shape and consistency. It deliberately accepts a
draft synthetic descriptor for **offline design checks only**, does not authorize
a run, access artifact files, inspect credentials, execute a command, call an API,
start an LLM or validate expiry against the current clock. Live integration must
perform those independent trust, consent, freshness and environment checks.

Examples must never be copied into project state as observed evidence or approval.
The future Sidecar has not run these examples. No protocol compatibility is claimed.
