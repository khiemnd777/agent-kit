# Agent Kit V2 contract compatibility profile

## Source and status

The three `src/agent_sidecar/contracts/*.schema.json` files are byte-for-byte copies
from the delivered Agent Kit V2.0.0 archive (SHA-256 recorded in provenance).
`contract.py` reuses its MIT semantic validator with only its package-root lookup
adapted. The contract version remains **0.1.0**. It was a draft in V2; this runtime
implements the profile below, not every shape potentially admitted by its schemas.
No statement in an old design-only schema description is changed into runtime proof.

## Supported profile

- Local synchronous invocation, UTF-8 JSON; requests/results/capability descriptors
  retain the unchanged V2 shape. CLI diagnostics are separate, not fake terminal results.
- `content_digest` snapshots only. No unverified Git HEAD snapshot, implicit clone,
  branch checkout, source upload or remote source fetch.
- Exactly `read_source` + `write_scratch`, logical roots `source:/` + `scratch:/`,
  and an empty network-host list. Narrower logical-root grants, network and source
  writes are refused rather than silently widened.
- Reviewed fixed workflows. Capability digest = SHA-256 of the exact workflow file
  bytes. The runtime implementation is separately pinned in `environment_digest`.
- `checks` exactly match the pinned workflow's step IDs and criteria; every check
  is required in this release. An owner cannot rename a criterion into business
  acceptance while retaining the same implementation.
- `input_schema` is a closed object schema. Only local schema fragments are allowed;
  remote references, embedded schema IDs, unknown request fields and ambiguous data
  are refused.
- Limits: max wall time, max concurrency, summary bytes and total declared evidence
  bytes are enforced. Reserve at least 8192 bytes of evidence per step. Snapshot hard
  caps are 10000 files, 8 MiB/file and 64 MiB total. No CPU/RAM/disk cgroup claims.
- `max_attempts` bounds attempts per step; `metrics.attempts` reports the highest
  per-step attempt count (zero if none started). Per-step receipts contain every
  attempted execution and exit code. This is explicit local profile semantics;
  consumers must not interpret it as total process launches or whole-DAG reruns.
- `when: always` waits for upstream terminal states but never bypasses a stopped,
  cancelled or expired request. There are no general expression/LLM conditions.

## Canonical identity and environment

Request/manifest/policy digests use V2's local Python profile:
`json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)`
encoded UTF-8 and hashed with SHA-256. This is **not RFC 8785**, a signature or a
cross-language guarantee. Nonfinite numbers, duplicate keys, invalid Unicode and
excessive nesting/size are rejected.

Environment identity includes the Sidecar source/schema hashes, Python version and
executable digest, platform, exact dependency versions and pinned top-level tools.
It is deliberately **not a hermetic build identity**: it does not capture every
shared library, kernel state or program invoked by trusted child code. No general
cache reuse across different requests is implemented on the strength of this hash.

## Terminal outcomes

| State | Meaning |
| --- | --- |
| `succeeded` | Every required check PASS, complete retained evidence, settled declared effects |
| `failed` | Observed assertion/command failure; dependent checks remain NOT_RUN |
| `blocked` | Missing/currently unauthorized prerequisite; may be before any run |
| `cancelled` | Cancellation was observed; inspect unknown effects before replay |
| `timed_out` | A step, request or authorization deadline was reached |
| `escalated` | Unknown effects, incomplete evidence, changed boundary or unexpected condition |

An invalid request/registry can fail before a contract-compatible result exists.
The CLI returns an error and nonzero status, not a fabricated successful result.
A blocked result produced for valid request data accounts for every requested check.

Detailed evidence is stored under a run root. PASS/FAIL need actual artifact
references; artifact bytes are checked before writing the terminal result.
Exceeding an output/evidence budget does not produce success: a bounded retained
record identifies the omission, keeps any known FAIL, and requires owner handling.

Builtin-only usage counters are zero with a no-model provenance statement. Process
usage counters are null with a reason because arbitrary child programs are not
instrumented. Neither says how many tokens the Coding Agent used around the call.

## Authorization and replay

`policy` creates a selected, pinned allowlist but no execution permit. `prepare`
pins one request. `authorize --confirm` records the current local caller's actual
authority for that request. `run` verifies the permit. `delegate --confirm-authorized`
batches those operations under already-existing authority; it is not self-approval.

Permits bind complete request digest, policy, approval reference and expiry. They
are not remote credentials or a multi-user authorization system. Policy changes,
expired authority, changed runtime or snapshot corruption fail closed. Null/malformed
permits are refused. Mid-run snapshot/runtime changes prevent a success result.

A request ID is claimed with exclusive file creation. Reusing its identical completed
request returns previously verified evidence. A different request under that ID,
an active claim or an interrupted claim never starts duplicate work. A fresh request
ID is a new intent: it needs current authority; the owner must reconcile previous
unknown effects. No automatic crash resume, exactly-once external effects or automatic
replay across new IDs is claimed.
