---
name: test-driven-development
description: "Design meaningful tests after the approved code/wiring scope; preserve the project code-first order rather than imposing red-green cycles."
---

# Regression and Verification (historical skill ID)

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Historical name, actual project sequence
The `test-driven-development` identifier is retained for compatibility, not as a
mandate for test-first development. For long/complex/UI packages complete approved
production code and real wiring before writing/updating tests, then run them.
Existing tests/reproduction evidence may be inspected during investigation.

## Choose assertions that matter
Use the project's actual framework/wrappers. Identify an observable requirement
and plausible regression, not incidental implementation details. A setup/import
failure is not a regression assertion detecting the bug. Include affected bounds,
denied/error, duplicate or concurrent behavior. Use isolated authorized synthetic
data and appropriate mocks; mocked units do not prove live integration or rendering.

Stable check bundles may run DIRECT/DELEGATE. Choose relevant checks once, consume
bounded evidence and rerun only invalidated parts. Do not run every layer or the
full suite by habit. Missing tooling is NOT_RUN, not PASS or proof of a product defect.

## Handle failures
Preserve valid assertions; change expectations only for confirmed changed behavior
or an evidenced test defect. Retire obsolete/duplicate tests only with needed
coverage retained. No retry-until-green, incidental test platform or automatic
new runner. Report observed results and missing required checks separately from
acceptance/release. See [testing notes](../../references/engineering-notes.md#testing).
