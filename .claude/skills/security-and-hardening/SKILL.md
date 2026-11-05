---
name: security-and-hardening
description: Address affected trust boundaries in authorization, untrusted input, sensitive data, dependencies and external integrations, or perform an explicitly scoped security audit.
---

# Security and Hardening

Use the [lean operating core](../../../AGENTS.md). Identify the assets and trust boundaries affected by the task, including existing callers and controls. Reuse a relevant established threat model. A local validator repair does not require a whole-project audit, but an evidenced security defect affecting the agreed behavior remains in scope.

## Preserve applicable protections

- Treat externally controlled values and model output as untrusted, regardless of whether they arrive through HTTP, files, queues, tools or another process. Validate allowed shape and limits before use; parameterize queries, avoid shell interpolation and encode output in its destination context.
- Enforce authentication and resource/tenant authorization on protected operations. Shape validation or a hidden UI control is not authorization. Retain denied-access coverage relevant to the change.
- Protect credentials, secrets and personal data in source, responses, telemetry and external calls. Keep session, CSRF, transport and rate-limit controls aligned with the project's security policy.
- For user-influenced server fetches, uploads or destructive paths, retain the appropriate network, content, containment and ownership checks. Do not broaden a rejected target as a fallback.
- For dependencies or install-policy changes, inspect the authoritative lockfile, relevant scripts and advisory reachability using the existing manager. An audit pass is not proof of package trust. Do not install tools, execute unreviewed dependency scripts or force upgrades incidentally.

## Apply authority at the actual boundary

Approval of the task plan covers routine in-scope security work. Every new task first needs planning and approval, including small security fixes. Ask only when evidence requires a material new use of sensitive data, elevated access, weaker protection, external sharing or another authority not granted. Continue unaffected work. Runtime approval mechanisms and required project review/release controls remain binding.

Preserve the project's data purpose, retention and export/deletion requirements. Do not invent consent, legal conclusions or approval from a template. Handle an exposed secret through authorized incident procedures; source cleanup alone does not revoke it.

## Verify and finish

Select relevant abuse and denied-access cases, then inspect or test the changed boundary with authorized tools and data. Check that defenses remain effective at the actual enforcement point and that error handling does not expose internals. Reuse evidence for untouched controls. Dependency audits apply to relevant changes and actual project release requirements, not every local edit.

Stop when the scoped protections and acceptance have sufficient evidence. State required proof that could not run; do not claim security certification from source checks.

Read [detailed techniques](references/detailed-guide.md) for a selected threat, [hardening examples](references/hardening-patterns.md) for its implementation, or the [security reference](../../references/security-checklist.md) for applicable verification.
