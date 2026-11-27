# Workflow authoring

A workflow is reviewed reusable code/configuration, **not** generated anew per task.
The format is `sidecar.workflow/v1`; it is not Swamp YAML. Both JSON and unambiguous
YAML are supported. Aliases/anchors, merge keys, duplicates and unknown properties
are refused. The existing three workflows are runnable examples.

## Builtin-only example

```yaml
format: sidecar.workflow/v1
id: my.json-check
version: 1.0.0
description: Check named JSON files in a fixed source snapshot.
lifecycle: draft
review_ref: null
effects: [read_source, write_scratch]
replay_policy: safe_read_only
input_schema:
  type: object
  properties:
    paths:
      type: array
      items: {type: string, minLength: 1, maxLength: 256}
      minItems: 1
      maxItems: 64
  required: [paths]
  additionalProperties: false
steps:
  - id: json-valid
    executor: builtin
    operation: json-files
    needs: []
    criterion: Every named JSON file parses without ambiguous or nonstandard data.
    timeout_seconds: 20
```

This sample remains draft and **cannot run** until actually reviewed and its exact
reviewed file digest selected in a policy. Merely changing the lifecycle field is
not a substitute for real review/authority. `validate-workflow` checks structure,
not safety, business correctness or operational readiness.

## Steps and dependencies

Each step supplies `id`, `executor`, `needs`, `criterion`, `timeout_seconds` and one
executor's fields. IDs are unique and dependencies must form a DAG. The file order
does not imply dependencies. A step defaults to `when: success`; `when: always`
means after all named dependencies terminate, even if they fail. Cancellation and
request deadlines still stop new dispatch. There is no per-step LLM or auto-repair.

Builtin operations: `inventory`, `entrypoints`, `manifest`, `mirrors`, `json-files`.
They are fixed code in `executors.py`, not dynamically loaded target plugins.

## Trusted process steps

Process steps specify `argv`, optional contained `cwd`, optional `SC_INPUT_*` env
values and optional transient `retry_exit_codes`/`retry_delay_seconds`. The first
argv element is a policy-pinned bare executable name; no dynamic executable template.
Values may be literal or whole-value `{{inputs.key}}`, `{{source}}`, `{{scratch}}`.
There is no partial interpolation or implicit shell. Explicit shell executables
are possible only under an explicitly reviewed trusted-process policy.

`{{source}}` in process mode points at that step's private writable source copy,
not the original repository. Every process step gets a separate copy. Dependencies
order work, but do not implicitly transfer build outputs or mutable files. The
builtin source snapshot is never modified by a builtin executor.

Only retry codes 2..125 can be listed; assertion code 1 is never configurable as a
transient retry. Retries require `safe_read_only`, remain within request attempt/time
ceilings and do not retry after unknown effects, cancellation or timeout. That label
is a maintainer assertion to review, not a guarantee from repeatability alone.

## Pin and re-review

Any workflow byte change changes its digest. New capability semantics require review,
policy update and a new request; old permits never silently authorize the change.
Changing a registry file does not modify the Agent Kit repository.
