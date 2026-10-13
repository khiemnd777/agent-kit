# Kit verification results

**Version:** 0.1.0 preview
**Package verification date:** 2026-10-12
**Claim boundary:** static package validation and independent source review. Native behavior and two-machine compatibility are **NOT_RUN**.

The baseline sections below record the 2026-10-12 checks. Later maintenance has separate dated records; it does not turn an earlier observation into a new runtime result.

## Environment

The package checks ran on macOS 26.6.2 with Python 3.13.3 and the existing system Ruby/Psych 3.1.0 YAML parser. No global configuration or dependencies were installed or changed for these checks.

No Codex or Claude Code client was started against this checkout. No native kit agent was invoked. Requested/effective native models and permissions are therefore Unknown.

## Completed package checks

| Check | Result | Observed evidence and limit |
| --- | --- | --- |
| Source provenance | PASS | All 26 original upstream Git blob hashes match the pinned commit metadata; source files remain unchanged |
| Skill distribution | PASS | 17 entrypoints per runtime root; 27 canonical/mirror pairs match byte for byte, including references and original MIT notice |
| Manifest integrity | PASS | 78 maintained kit files have matching SHA-256 entries; mutable project state and reports are deliberately excluded |
| Metadata syntax | PASS | Ruby/Psych parsed 34 skill frontmatters and three Claude native definitions; Python tomllib parsed three Codex definitions |
| Required fields/defaults | PASS | Expected names, descriptions, Codex instructions, omitted Codex model/effort, Claude inherit and read-only intent checked structurally |
| Relative references | PASS | 179 local Markdown links/anchors resolve, including the TechNote reference from both roots |
| Fresh template state | PASS | Planning, unassigned owners, no human approval, no execution scope or fixture task records |
| Coordination templates | PASS | Three templates and nine checklist items; shared state has one designated writer |
| Package text checks | PASS | New kit content reviewed in English; whitespace and targeted private-path/credential-pattern checks found no issue |
| Preservation | PASS | Source checkout status/tracked diff, 26 import-source files and five selected global configuration file hashes unchanged |
| Independent source review | PASS after repair | One path-safety finding was corrected and re-reviewed; no additional actionable finding identified |

The metadata checks validate structure and intent, not installed-client discovery, sandbox enforcement, tool access or language-model behavior. The text pattern scan is not a complete security audit.

## Reproducible integrity command

The exact Python code block in `verification-guide.md` was extracted and executed from the repository root:

```text
PASS: inventory hashes, mirror bytes and 17 skills per root
```

Its shared resolver checks the manifest, inventory, mirror entries and skill directories before reads. It rejects absolute paths, parent traversal, escaped resolved paths and symlink components.

## Owned negative fixtures

The published integrity recipe was exercised against isolated copies under the ignored local verification workspace. Only synthetic copies were changed. No application, client, global configuration or project approval was used or modified.

| Fixture | Expected exit | Result |
| --- | --- | --- |
| Unchanged package | 0 | PASS |
| Changed mirror content | Nonzero: hash/mirror mismatch | PASS |
| Missing mirror file | Nonzero: missing path | PASS |
| Absolute mirror path | Nonzero: unsafe path | PASS |
| Parent-traversal mirror path | Nonzero: unsafe path | PASS |
| Symlink mirror file | Nonzero: unsafe path | PASS |
| Symlink manifest | Nonzero before reading the manifest | PASS |
| Symlink parent directory | Nonzero: unsafe path | PASS |
| Absolute inventory path | Nonzero: unsafe path | PASS |

Nine checks completed: one positive and eight expected-rejection cases. These establish the recipe's tested integrity/path boundaries on this host, not native runtime or cross-machine behavior.

## Review and repair history

The independent read-only reviewer identified that the initial integrity recipe checked inventory paths but not mirror paths or the manifest itself. No unsafe input was used against private data. The coordinator replaced those reads with one bounded resolver, reran the published recipe and performed the negative checks above. The reviewer then inspected the final repair, confirmed the guide checksum and reran the clean recipe without writing files.

This was an independent package source review, not an invocation of `kit-reviewer` through either client. A final whitespace scan flagged Markdown hard-break spaces in this report. Those spaces were removed and the scan was repeated.

## Checks not run

| Check | Status | Reason |
| --- | --- | --- |
| skill-creator quick_validate | NOT_RUN / prerequisite failed | Attempts with system and bundled Python stopped at import because PyYAML is absent. No installation attempted. Ruby/Psych parsing and independent metadata checks completed instead |
| V02 native skill/agent discovery | NOT_RUN | No client session against the completed checkout |
| V03-V10 startup, authorization, session continuity, TechNote and duplicate handling | NOT_RUN | No real client behavioral run |
| V11-V15 parallel ownership, handoff, stale context and integration | NOT_RUN | Two developers on two physical machines were not available in this execution |
| V16-V17 effective model inheritance/overrides | NOT_RUN | No native invocation or runtime model observation |
| V18 effective read-only permissions | NOT_RUN | Authored restrictions and static fields do not prove enforcement |
| V19 unsupported-delegation behavior | NOT_RUN | No client fallback behavior exercised |
| Two-machine round 1 and round 2 | NOT_RUN | Independent machine/client matrix remains pending |

Application-specific builds, business-rule tests, deployment and production acceptance are outside this instruction-only package. Publishing the preview is authorized despite the explicit NOT_RUN items; it is not a verified compatibility release.

These results apply to this kit version. They do not grant approval or imply completed work in projects created from the template.

## Adaptive reporting update — 2026-10-13

**Task:** KIT-REPORTING-001. **Owner:** main session for this bounded kit maintenance update. **Branch / base:** `main` / `22c2a20359072dcb510f3329b97161b16f947fb2`.

**Approval provenance:** Khiêm gave direct human Approved in the current chat on 2026-10-13 for the six adaptive reporting formats and their consistent application to related Agent Kit instructions. That approval covers documentation, package checks and in-scope repairs. On the same date, Khiêm separately authorized committing all reporting updates and pushing them to `origin/main`. Global configuration, application changes and publication beyond the requested repository push remain outside this scope. No later stop instruction was received.

**Result:** The canonical TechNote document now defines before-and-after reports and illustrative examples for conversation, planning and implementation. AGENTS.md, README, policy, workflow, all four common roles, skills catalog and the existing coordination checklist route to that source. Claude's literal AGENTS.md import and both TechNote skill routes remain intact. The three coordination templates still hold detailed records.

**Acceptance:** All six minimum formats match the approved proposal. Reports retain material decisions, blockers, actual verification and limits. Simple follow-ups remain direct, and reports add no approval gate inside existing authorization. Fresh project context, plan, state and task inventory retain their unassigned, unapproved values.

| Check | Result | Evidence and limit |
| --- | --- | --- |
| Published package-integrity recipe | PASS | Extracted the exact Python recipe from verification-guide.md and executed it from the repository root; 78 inventory hashes, 27 mirror pairs and 17 skills per root remain valid |
| Local Markdown references | PASS | Read-only Python scan resolved 189 local links/anchors across 76 Markdown files; external URLs were not fetched |
| Source and template preservation | PASS | SHA-1 Git blob checks preserve all 26 canonical upstream sources and their mirrors; comparison with the base commit preserves fresh project files, task inventory, native adapters and model/tool settings |
| Coordination structure | PASS | Source inspection retains three coordination templates and nine checklist items; detailed handoff requirements remain in place |
| Whitespace | PASS | `git diff --check` returned exit code 0 |
| Independent source review | PASS | Bounded kit-reviewer subagent inspected the assigned guidance diff and found no actionable issue; its guidance whitespace check returned exit code 0. This was source review, not native client discovery or a V20 behavioral run |
| V20 runtime reporting behavior | NOT_RUN | Six formats and edge scenarios are documented in the verification guide; fresh native client sessions and the two-machine matrix were not exercised |

**Current state / next action:** The approved guidance update, source review and applicable package checks are complete. Delivery to `origin/main` is authorized; actual commit and remote synchronization evidence belongs to Git history and the delivery report. V20 remains the next runtime check when a client verification scope is authorized. Native discovery, runtime reporting consistency and reading-time improvement remain Unknown. The reviewer performed read-only inspection; effective runtime sandbox enforcement was not verified. This record is kit maintenance evidence, not inherited project approval or an application task record.
