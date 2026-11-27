---
name: security-and-hardening
description: "Protect affected trust, data and authorization boundaries with scoped verification and real runtime controls."
---

# Security and Hardening

Use the [V2 operating core](../../../AGENTS.md); skills do not grant authority.

## Identify the affected boundary
Inspect assets, callers and existing protections. Reuse a relevant threat model;
a local validator fix does not require a whole-project audit. Treat HTTP/files/
queues/tools/model output as untrusted. Validate shape and limits, parameterize
queries, avoid shell interpolation and encode for the destination context.

Authentication and resource/tenant authorization belong at the protected boundary;
a hidden button or valid JSON is not authorization. Preserve session/CSRF,
transport/rate-limit controls and denied-access cases relevant to the change.
Protect secrets and personal data in source, output, telemetry and external calls.

## Constrain effects
For uploads, user-influenced fetches and destructive paths, retain containment,
network/content and ownership controls. Do not broaden rejected targets. Inspect
lockfiles/scripts and relevant dependency advisories when that scope changes;
audit success is not trust proof or permission to install/upgrade.

An external execution contract only describes permissions. The future host must
enforce filesystem, network, secret, process and cancellation controls; a separate
clone is not a sandbox. Reconcile unknown effects before retry. Do not invent
consent/legal conclusions or bypass runtime restrictions to finish a checklist.

## Verify and stop
Use relevant abuse/denied-access cases and authorized synthetic data. Confirm
protection at the actual boundary; source checks are not security certification.
Incident cleanup does not revoke exposed secrets. Report required missing proof
and stop at scoped acceptance. See [security notes](../../references/engineering-notes.md#security).
