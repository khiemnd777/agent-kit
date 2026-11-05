# Local skill contribution journal

The delivery owner records actual skill participation at planning and implementation handoff, automatically as part of authorized task work rather than waiting for a reminder. This is a repository-local document convention: no service, scheduler, daemon, telemetry collector, database or new harness. It supplies inspectable evidence for retrospectives, not proof of native loading or causal effectiveness.

## Write boundary and presentation

Save a phase record before reporting within the approved write scope and derive the skills table from that same record. Unapproved/read-only planning stays in chat; never claim that an unsaved record exists. Once writes are authorized, a current-task planning record may be saved with its actual recording time and known source identities. Do not invent earlier timestamps, versions or records for past tasks/pilots.

Use one table: **Skill | Source | Actual contribution | Estimated participation %**. Include applied skills only: merely selecting or reading one is insufficient. Use **Repo** for an effective skill inside the target repository, **Personal** for an external personal/host/plugin skill, and **UNKNOWN** if its effective source cannot be verified. These labels describe effective location, not authorship/upstream origin. Do not duplicate a display label in storage or migrate history just to add the column. Keep paths, packages, versions and fingerprints in records, not the table. Localize labels to the user's requested language without changing their meaning.

Estimates total 100% among applied skills. They are subjective shares of contribution, not measured time, tokens, quality, efficiency or causal credit. If no skill was applied, use an empty skills array and state that explicitly; do not fabricate a skill to reach 100%.

## Storage and identities

Use `records/<task-id>/<event-id>.json` below this directory. Use stable task/scope identities and phase/handoff identifiers, for example `TASK-008/workflow-journal/implementation/1`. A resumed chat continues that same identity: it does not create another usage event. Multiple genuine handoffs may use a new index without pretending they are new tasks.

Create each event exclusively (for example file mode `x`), preserving existing files. If the logical event already exists, reuse it; an ID collision with different content is an error, not permission to overwrite. Corrections and evaluations are new linked events. Children return proposed records/state updates; the delivery owner writes shared records. No secrets, raw prompts/logs, customer data, access-bearing URLs or machine configuration belong here. Use repo-relative/logical skill paths and safe evidence references, not home-directory dumps.

## Event format — schema_version 1

All JSON events contain:

| Field | Meaning |
| --- | --- |
| schema_version | `1` |
| event_id | Unique stable event identity |
| event_type | `phase_handoff`, `evaluation` or `correction` |
| task_id / scope_id | Stable task and bounded approved outcome |
| recorded_at | Actual recording time, ISO 8601 with timezone |
| reported_by | Role or safe logical reporter identity |
| source_kind | For example `agent_self_report`, `human_feedback`, `independent_review` |

A `phase_handoff` additionally contains:

- `phase`: `planning` or `implementation`; `handoff_index`: positive integer.
- `classification`: task size, complexity and whether UI is involved. Describe the actual task; combined requirements apply together.
- `authority`: approval source and authorized scope, including publication limits. A proposed plan or historical approval is not permission.
- `skills`: entries with `skill_id`, `contribution_summary`, `contribution_percent_estimate`, `estimate_source`, and `source_identity`.
- `source_identity`: `kind` (`repository`, `host_skill` or `plugin`, or `unknown`), `path` (repo-relative or logical), `version` (nullable), `sha256` (nullable) and `fingerprint_basis` (actual observation or reason missing). Plugins may include a safe package identity. Capture the bytes actually used; do not attribute a later fingerprint to earlier use. External host/plugin sources map to Personal in the table.
- `outcome`: `delivery_status` (`COMPLETED`, `INCOMPLETE`, `BLOCKED`, `STOPPED`), `verification_level`, `human_acceptance` (`PENDING_REVIEW`, `ACCEPTED`, `CHANGES_REQUESTED`, `NOT_APPLICABLE`) and `limitations`. Phase completion is not completion or human acceptance of the whole task.
- `measurements`: counters below, plus nullable `client`, `model` and `effort` with evidence/reasons. Record only observed values.
- `evidence_refs`: safe local references or public commit identifiers supporting the result.

For each of `elapsed_seconds`, `tool_calls`, `input_tokens`, `output_tokens`, `cached_input_tokens`, `reasoning_output_tokens`, use an object with `value` (number or null), `source_ref` (reference or null) and `missing_reason` (reason when unavailable). Preserve units and scope. Null is not zero. Do not estimate tokens from text length, contribution percentages or configuration placeholders. File hashes, model self-report and package checks are not evidence of native discovery/invocation or measured savings.

An `evaluation` contains `subject_event_id`, `assessment_source` (`human`, `independent_reviewer`, `agent_self_review`), positive `review_attempt`, `decision` (`ACCEPTED`, `CHANGES_REQUESTED`, `PASS`, `FAIL`, `PENDING`), `findings` and evidence references. Technical PASS is not human ACCEPTED. Each finding names its confirmed category (`IMPLEMENTATION_DEFECT`, `REQUIREMENT_CHANGE`, `ENVIRONMENT`, `TEST_DEFECT`, `UNKNOWN`), description, evidence and nullable `skill_attribution`. Attribute a defect only with evidence; co-usage is not blame.

A `correction` contains `supersedes_event_id`, a reason and a complete corrected event payload in `replacement` (the same event type and logical task/scope/phase identity, with no nested correction). Preserve the original. Link later evaluations to the corrected event. Reject missing targets, cycles, competing correction heads or mismatched identities as invalid; do not silently pick a winner. Retro uses the latest unambiguous logical version, not both versions. Evaluations/corrections never count as additional skill use.

## Retrospective interpretation

Validate required fields/types, identities, estimate totals and links before including a record. Exclude invalid/partial/conflicting records with a reported reason; do not silently repair or drop errors. No automated scorer is required by this guide.

- Count unique implementation task+scope outcomes, not planning+implementation as two tasks. A resume or linked evaluation is not another task.
- Human first-review acceptance rate: accepted at first human decision / reviewed implementation task+scopes with a first decision of ACCEPTED or CHANGES_REQUESTED. Exclude pending/unreviewed outcomes; show numerator, denominator and exclusions.
- Separate confirmed implementation rework from changed requirements, environment issues and test defects. Preserve evaluator source, attempts, evidence and missing attribution.
- Compare observed resource costs only for comparable task classes, versions and measurement scopes. Show sample size and missingness; do not turn missing costs into zero or infer causality from shared skill usage.
- Present contribution estimates separately from verified outcomes and measured overhead. Do not produce an automatic total skill effectiveness score.

The first records here describe this kit-maintenance task only. Adopters initialize their own task/state records; no approval or historical outcome transfers with this template.
