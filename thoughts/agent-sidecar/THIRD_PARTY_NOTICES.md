# Sources, provenance and licenses

## Agent Kit V2 boundary

Source: user-provided `agent-kit-v2.0.0.zip` in this conversation.
SHA-256: `f4551605d75561be67375c75acd9db99f5b26aaa107d547889712ce778e957e4`.
That V2 package records its V1 source as `khiemnd777/agent-kit` commit
`df3b058a52acc9ea10a7556733baae44ac12d1f2`.

The three JSON Schemas are copied unchanged under MIT. The source
`scripts/check_contract.py` is included as `agent_sidecar/contract.py`, changing
only the package-root lookup to locate the bundled schemas. The inherited MIT
copyright/permission notice is retained in LICENSE. Original V2 files remain unchanged.

The runner, registry, admission/policy, snapshotting, CLI, executors, tests and
integration documentation are new implementation for this delivery. No code,
workflow definition or skill was copied from Swamp. No Swamp API/client/binary is
linked or required, and no compatibility with Swamp YAML is claimed.

## Runtime dependencies (not vendored)

- jsonschema 4.26.0 — MIT; JSON Schema validation, also used by V2.
- PyYAML 6.0.3 — MIT; safe YAML parsing with additional strictness in Sidecar.

Installed dependency licenses remain with their distributions. Python's standard
library supplies subprocess/filesystem/concurrency functionality. No dependency is
downloaded or installed by the runtime. A lock on direct versions is not a fully
hermetic OS/transitive dependency/environment claim.
