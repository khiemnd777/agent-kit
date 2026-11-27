# Contributing

Use the operating core and the actual task authority. Keep governance separate
from execution. Do not add a runtime, scheduler, hidden installer or mandatory
Sidecar dependency as incidental package maintenance.

Edit canonical skills in `.agents/skills/` and roles in `docs/roles/`; generate
mirrors/adapters with `python3 scripts/sync_assets.py`. Regenerate the manual
reference with `python3 scripts/export_grok.py`. Update the maintained inventory
using `python3 scripts/verify_package.py --update-manifest` only after reviewing
the intended changes, then run all checks and tests. Refreshing hashes is not
proof that a change is safe or authorized.

Preserve MIT notices and precise provenance. Do not copy Swamp source into this
package. Contract changes require examples, semantic/negative tests and a version
decision; draft compatibility is not an implementation claim. Keep all missing
native/integration/token evidence explicit. Never commit credentials, user
conversation histories, virtual environments or local runtime data.
