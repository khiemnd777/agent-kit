# Verification — Agent Sidecar 0.1.0

Date: 2026-11-17. This is observed local evidence, not human acceptance or release.

| Check | Observed result | Evidence |
| --- | --- | --- |
| Sidecar regression suite | PASS — 105 tests, 0 failures, 0 errors, 0 skipped | [Raw log](evidence/tests.log), [machine record](evidence/verification.json) |
| Three V2 schemas unchanged | PASS — byte-identical | [Interop record](evidence/interop.json) |
| `repo.prepare` actual execution | PASS | [Result](evidence/runs/repo.prepare/result.json) |
| `agentkit.integrity` actual execution | PASS | [Result](evidence/runs/agentkit.integrity/result.json) |
| `agentkit.verify` actual execution | PASS — 4 checks; 77 V2 regression tests observed | [Result](evidence/runs/agentkit.verify/result.json), [V2 test output](evidence/runs/agentkit.verify/logs/regression.log) |
| ORIGINAL V2 semantic validator on all 3 real result sets | PASS | Each evidence run's `agentkit-validator.log` |
| Source Agent Kit V2 before vs after | PASS — unchanged | [Interop record](evidence/interop.json) |
| Wheel build; bundled schemas; installed-wheel CLI | PASS | [Build log](evidence/build-wheel.log), [CLI output](evidence/wheel-smoke.log) |
| Native Codex/Claude/Gemini/Cursor integration | NOT_RUN | No client launched |
| macOS / Windows / Python 3.11 runtime matrix | NOT_RUN | Actual test host below |
| Hard OS/network sandbox | NOT_IMPLEMENTED | Trusted-process opt-in is not isolation |
| Native-client token/cost savings | NOT_MEASURED | No invented savings percentage |

Actual host: `Linux-6.18.57-x86_64-with-glibc2.41`; Python `3.13.5`;
jsonschema `4.26.0`; PyYAML `6.0.3`.
The package declares Python 3.11+ based on used APIs; only the above runtime was observed.

## What the tests exercise

Strict JSON/YAML/schema boundaries, registry pins, cycles and dependency failure,
concurrency (instrumented unit probe), expiry and request-bound permits, null-permit
rejection, content snapshots and tampering, paths/symlinks, required evidence,
actual subprocess execution, environment stripping, isolated copies, bounded output,
SIGINT/cancellation, global/step timeouts, transient retries, failure/no-retry,
background-child handling, duplicate/in-flight/stranded requests, actual artifact
hash verification, CLI lifecycle and one-call delegation.

Some tests deliberately use synthetic workflows/mocked worker outcomes to exercise
scheduler and failure branches. That is unit evidence, not a real application benchmark.
The three interoperability runs and the 77-test V2 suite did execute actual local code.
Original V2 validation establishes document consistency; the Sidecar verifier additionally
checks actual artifact bytes. Neither proves hostile-code isolation or human approval.

The retained request/approval references identify local implementation test fixtures.
They are **not authority to execute later tasks**. Historic result fingerprints name
the runtime/snapshots used for that run; do not modify them to fit another environment.

## Reproduce

```sh
python3 tools/verify.py --out /tmp/new-sidecar-evidence
python3 tools/interop.py --agent-kit /path/to/agent-kit-v2 \
  --out /tmp/new-sidecar-interop --confirm-trusted-code
```

Use a fresh interoperability output directory. No checker auto-installs dependencies.
Self-review is not independent security review. Archive integrity/round-trip evidence
for the final ZIP is reported separately at delivery; no ZIP can contain its own hash.
