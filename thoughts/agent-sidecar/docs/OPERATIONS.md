# Local operations

## Paths and lifecycle

Use separate directories for Agent Kit, Sidecar, target project and private Sidecar
state. State must be owned by the local user with POSIX mode 0700. Do not place state
inside the snapshot source. Never commit runtime snapshots, logs or working copies.

```text
state/
  snapshots/<content sha>/manifest.json + source/
  requests/req-*.request.json + req-*.permit.json       # one-call delegate records
  claims/req-*.json                                  # exclusive request delivery claim
  runs/run-*/
    request.json capability.json workflow.json policy.json permit.json
    state.json result.json
    evidence/ logs/ scratch/<step>/work home tmp
```

Run records are atomic files. An abrupt kill before terminal commit leaves a claim
and an unfinished state; it does not become success on the next invocation. Inspect
what ran, reconcile possible effects and authorize a new intent only when safe.
No automatic claim deletion, restart/resume, result rebaseline or process re-launch.

## Inspect without rerunning

```sh
python3 sidecar history --state /private/sidecar-state --limit 10
python3 sidecar result --state /private/sidecar-state --run-id run-EXACT_ID
python3 sidecar verify-result \
  --request /private/sidecar-state/runs/run-EXACT_ID/request.json \
  --result /private/sidecar-state/runs/run-EXACT_ID/result.json \
  --capability /private/sidecar-state/runs/run-EXACT_ID/capability.json \
  --run-dir /private/sidecar-state/runs/run-EXACT_ID
```

Use the actual run ID; the placeholder is not an existing run. History reads metadata,
not full logs. `result` verifies the retained artifact bytes before returning its claim.

## Stop

Foreground execution handles Ctrl-C/SIGINT and SIGTERM. It stops new dispatch and
terminates in-flight process groups. Timeout uses the same bounded settlement path.
Trusted processes can escape their groups; uncertain effects require reconciliation.
Do not interpret a stopped CLI as a rollback of external writes.

## Exit codes

`0` succeeded; `1` failed check; `2` blocked/admission/input error;
`3` escalated; `124` timed out; `130` cancelled. A valid terminal result is JSON on
stdout. Admission/parse failures without a result emit a structured diagnostic on
stderr and exit nonzero. Detailed child stdout/stderr are stored as evidence, not
mixed into the returned JSON stream.

## Retention and budgets

There is no automatic retention daemon. State can grow; review artifacts and delete
only your own inactive run/snapshot directories under actual authority. Do not delete
claims blindly to rerun uncertain work. Source snapshots omit common secrets/caches
but are not secret-scanned. Treat the whole state directory as private source data.

Snapshot hard limits: 10000 files, 8 MiB/file, 64 MiB total. Every process step copies
the snapshot separately. Request limits bound concurrency, wall time and retained
evidence, **not** total child CPU/memory/disk usage. Choose narrow source roots and
conservative budgets. Use a host sandbox for hard isolation; this release supplies none.

## Upgrade

Source/dependency/tool changes alter environment fingerprints. Re-review affected
workflows/policy, prepare new requests and keep old records as historical evidence.
Do not edit old result files to make them match a new runtime. No auto-updater runs.
