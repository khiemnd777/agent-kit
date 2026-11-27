# Verification results — Agent Kit V2

Date: 2026-11-17. Version: 2.0.0 source candidate.
Baseline: `df3b058a52acc9ea10a7556733baae44ac12d1f2`.

## Observed local results

| Check | Result | Evidence scope |
| --- | --- | --- |
| Canonical/Claude skill and reference mirrors | PASS | Byte equality |
| 12 optional native role adapter sources | PASS | Generated equality, TOML/YAML fields; not native invocation |
| Maintained source inventory / inherited license notices | PASS | Local hashes and exact inherited notice blobs |
| Local Markdown links / anchors | PASS | Package-local references |
| 3 draft JSON Schemas and 8 synthetic contract examples | PASS | Shape and semantic consistency only |
| Manual Grok reference freshness | PASS | Explicit source allowlist; no upload |
| Python regression suite | PASS — 77 tests | Actual local unittest run |

Raw local output is retained in [checks.log](delivery/checks.log); machine-readable
context is in [verification.json](delivery/verification.json). Output-evidence files
are named manifest exclusions to avoid a circular inventory/report dependency.

Tests cover contradictory success claims, missing/unknown evidence, correlation
and source/policy/environment mismatch, path traversal and symlink ancestors,
unknown input/permission fields, replay/usage/output bounds, duplicate keys,
frontmatter ambiguity, stale generated assets and absent validation dependencies.
They do not execute any workload or access the example artifact paths.

## Not observed

Native client discovery, invocation, effective permissions and governance compliance:
**NOT_RUN**. Sidecar interoperability, isolation, scheduling, durable execution and
cancellation: **NOT_RUN**; no Sidecar is present. Token/latency A/B or B/C benchmark:
**NOT_RUN**. Human acceptance of this source delivery: pending. Remote publication:
not performed. Self-review is not independent review.

The source is a curated V2 rebuild, not a full V1 archive. Smaller instruction text
is not measured token savings. A valid schema or package PASS is not runtime
security enforcement, artifact authenticity, business correctness or acceptance.

## Reproduce

Run the four maintenance commands in README from the extracted package root.
Python 3.11+ and the explicitly listed development libraries are required for full
checks; no script auto-installs dependencies or configures a coding client.

## Archive round-trip

PASS: ZIP CRC/duplicate-entry checks, extraction into a separate temporary directory,
all four README maintenance commands (including 77 unit tests) on that extracted
copy, and maintained-file hash comparison. Hidden client directories are included.
The final archive contains 119 files; no `.git`, virtual environment, cache or credentials.
