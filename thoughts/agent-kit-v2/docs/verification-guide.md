# Package verification

These checks validate this kit's source and draft document contracts. They do
not run a Sidecar, native coding client, application or benchmark.

## Prerequisites and commands

Python 3.11+; development libraries listed in `requirements-dev.txt`. Using the
instructions alone has no Python/library runtime dependency. Install development
tools only under actual authority; none of the scripts auto-installs packages.

Run from the package root:

```sh
python3 scripts/sync_assets.py --check
python3 scripts/export_grok.py --check
python3 scripts/verify_package.py
python3 -m unittest discover -s tests -v
```

After an authorized, reviewed canonical source change, regenerate the assets and
manual reference without `--check`, then run `verify_package.py --update-manifest`
and recheck. Hash refresh is not code review or authorization.

## What is checked

The maintained inventory detects changed/missing/unexpected source files.
Canonical skill/reference mirrors and optional native role bodies are generated
from one source and checked byte for byte. Frontmatter/TOML fields, license notices,
source pin, fresh adopter templates and local links/anchors are checked.

All three draft JSON Schemas and synthetic examples receive shape and semantic
checks. Negative unit tests exercise mismatched revisions/identities, incomplete
or contradictory evidence, unsafe paths, missing metric provenance, out-of-bounds
claims and unsupported input. Files are never executed as workflows.

The Grok reference is generated from an explicit source allowlist. No upload,
account configuration, global skill installation or runtime discovery occurs.

## Evidence boundaries

- Package PASS: those source/doc/script consistency checks passed.
- Native discovery/invocation/permissions: NOT_RUN until observed in that client.
- Agent compliance with governance scenarios: NOT_RUN until actually exercised.
- Future Sidecar interoperability, isolation, retries and cancellation: NOT_RUN.
- Token/latency savings and human acceptance: require their own real evidence.

The manifest excludes its own file and the named mutable output-evidence files
listed inside it. ZIP transport checksums are separate. Neither is a signature or
security attestation. All example run metrics and artifacts are synthetic; no
artifact bytes at their example paths are claimed to exist.
