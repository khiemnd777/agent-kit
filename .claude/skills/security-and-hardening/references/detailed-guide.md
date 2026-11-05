# Security and Hardening: detailed techniques

Read the section that resolves the current technical question. The [skill entrypoint](../SKILL.md) sets scope and completion; examples here do not select a stack, authorize side effects or add delivery gates. Preserve the project's actual security and release requirements.

## Contents

- [Understand the affected trust boundary](#understand-the-affected-trust-boundary)
- [Controls for affected surfaces](#controls-for-affected-surfaces)
- [Hardening Controls](#hardening-controls)
- [Review Checklist](#review-checklist)
- [Security decisions](#security-decisions)
- [Relevant warning signs](#relevant-warning-signs)
- [Verification](#verification)

## Understand the affected trust boundary

Identify the assets, actors and existing controls relevant to the requested change. Reuse an established threat model; a small repair does not need a fresh formal document or a timed exercise. For an unfamiliar or changed boundary, consider:

1. **Map the affected trust boundaries.** Where does untrusted data cross into the changed operation? HTTP requests, form fields, file uploads, webhooks, third-party APIs, message queues, and **LLM output** — plus the local values that look internal because the OS handed them to you: another process's command line or environment, filenames on a shared volume, a path in a job payload. Trust follows who *wrote* a value, not which channel delivered it. Every boundary is attack surface.
2. **Name the assets.** What's worth stealing or breaking? Credentials, PII, payment data, admin actions, money movement.
3. **Use an applicable threat lens** when it helps identify a missing protection. STRIDE offers these questions; selecting one does not require a complete matrix for every handler:

| Threat | Ask | Typical mitigation |
|---|---|---|
| **S**poofing | Can someone impersonate a user/service? | Authentication, signature verification |
| **T**ampering | Can data be altered in transit or at rest? | Integrity checks, parameterized queries, HTTPS |
| **R**epudiation | Can an action be denied later? | Audit logging of security events |
| **I**nformation disclosure | Can data leak? | Encryption, field allowlists, generic errors |
| **D**enial of service | Can it be overwhelmed? | Rate limiting, input size caps, timeouts |
| **E**levation of privilege | Can a user gain rights they shouldn't? | Authorization checks, least privilege |

4. **Select relevant abuse cases.** Check the denied-access, malformed-input or misuse case that could invalidate the changed protection. Reuse existing coverage and add a meaningful regression assertion where needed.

If the affected trust boundary remains unknown, resolve that uncertainty before claiming the protection is verified. Continue independent authorized work while the dependent security decision is unresolved.

## Controls for affected surfaces

### Preserve applicable protections

- **Validate untrusted input** at the affected system boundary, including its allowed shape and limits
- **Parameterize all database queries** — never concatenate user input into SQL
- **Encode output** to prevent XSS (use framework auto-escaping, don't bypass it)
- **Protect external communication** with HTTPS or the project's appropriate authenticated encrypted transport; do not weaken existing transport controls
- **Hash passwords** with bcrypt/scrypt/argon2 (never store plaintext)
- **Preserve applicable browser security headers** such as CSP, HSTS and anti-framing/content-type controls when the changed surface serves browser content
- **Preserve session and CSRF controls**, including appropriate httpOnly, secure and sameSite settings for cookie-based sessions
- **Use dependency audit and install-policy checks** for relevant dependency changes or actual project release requirements; an unrelated source edit adds no audit gate

### Apply existing approval; ask only for a missing security decision

The changes below need a confirmed security/data boundary. If the current human-approved scope already covers that boundary, implement and verify without asking again per handler, file or phase. Ask only for an unapproved material change, such as new sensitive-data use, external sharing, elevated access or weaker protection. Continue unaffected authorized work.

- Adding new authentication flows or changing auth logic
- Storing new categories of sensitive data (PII, payment info)
- Adding new external service integrations
- Changing CORS configuration
- Adding file upload handlers
- Modifying rate limiting or throttling
- Granting elevated permissions or roles

### Do not take unsafe shortcuts

- **Never commit secrets** to version control (API keys, passwords, tokens)
- **Never log sensitive data** (passwords, tokens, full credit card numbers)
- **Never trust client-side validation** as a security boundary
- **Never disable security headers** for convenience
- **Never use `eval()` or `innerHTML`** with user-provided data
- **Never store sessions in client-accessible storage** (localStorage for auth tokens)
- **Never expose stack traces** or internal error details to users

## Hardening Controls

The controls below are technical options for the affected threat, not another workflow. Worked implementations are in [hardening-patterns.md](hardening-patterns.md). Open only the relevant section and retain the project's actual contracts and protections.

### Injection, XSS, and access control

- Parameterize every query. Never build SQL, NoSQL, or shell commands from input strings.
- Encode output through the framework's auto-escaping. If raw HTML is unavoidable, sanitize with an allowlist sanitizer first.
- Check **authorization** on every request, not just authentication: the authenticated user must own, or be permitted on, the specific resource (A01, IDOR).

Patterns: [Injection](hardening-patterns.md#injection), [XSS](hardening-patterns.md#cross-site-scripting-xss), [Access control](hardening-patterns.md#broken-access-control).

### Authentication and sessions

- Use the approved password-hashing library and project work-factor parameters (for example bcrypt, scrypt or argon2), never plaintext or a fast general-purpose digest. Load the session secret from the approved secret source, never hardcode it.
- Preserve the established session/CSRF policy, including `httpOnly`, `secure`, suitable `sameSite` behavior and bounded lifetime for cookie sessions. SameSite is part of the protection, not proof that all CSRF risks are covered. Select `'lax'` or `'strict'` according to the required flow; a cross-site flow using `'none'` needs its explicitly established secure-cookie and CSRF protections. An approved `'strict'` setting does not fail because an example uses `'lax'`; do not migrate a protected flow to match an example.

Pattern: [Authentication](hardening-patterns.md#broken-authentication).

### Headers, CORS, and responses

- Preserve the established security-header and CSP policy on affected browser responses. For a new browser surface, choose appropriate controls within its agreed security scope; the examples do not mandate migrating unrelated responses or adding a new package.
- For private/credentialed APIs, restrict CORS to the approved origins. Preserve an intentionally public unauthenticated resource policy; never use `*` with credentials or treat CORS as authorization.
- Strip sensitive fields (`passwordHash`, reset tokens) before any response. Error bodies are generic; internals go to server logs only.

Patterns: [Misconfiguration](hardening-patterns.md#security-misconfiguration), [Sensitive data exposure](hardening-patterns.md#sensitive-data-exposure).

### Input validation and uploads

- Validate at the boundary with allowlisted shape, lengths, enums and formats. Use the project's validation-error contract (422 is one possible response) and pass parsed values downstream; keep sensitive details out of errors.
- Uploads: allowlist MIME types, cap size, verify content (magic bytes) when it matters. The extension proves nothing.

Patterns: [Schema validation](hardening-patterns.md#schema-validation-at-boundaries), [File upload](hardening-patterns.md#file-upload-safety).

### Server-side fetches (SSRF)

Any URL the user influences — webhooks, import-from-URL, image proxies, link previews — can be aimed at internal services. Allowlist scheme and host, resolve **all** DNS records and reject any private or reserved address (loopback, link-local `169.254.169.254`, private, unique-local, for IPv4 and IPv6), and forbid redirects. That check still has a DNS-rebinding TOCTOU gap: for high-risk surfaces, pin the resolved IP or put a filtering agent in front.

Pattern: [SSRF](hardening-patterns.md#server-side-request-forgery-ssrf).

### Destructive operations on derived paths

A delete, move, or overwrite is only as safe as the value naming its target, and trust follows who *wrote* that value, not which channel delivered it: another process's command line is as attacker-controlled as a form field. A shape check proves well-formedness, not authorization. Before the call, require all three: the resolved target (symlinks resolved) sits under an **allowlisted root**; it is at least one level **below** that root; and it carries **ownership evidence read before the operation**. On refusal, log the rejected target and stop; never fall back to a broader default path.

Why the check is weaker than it reads (marker self-attestation, check/use races): [Destructive paths](hardening-patterns.md#destructive-operations-on-derived-paths). Worked code: `../../../references/security-checklist.md`.

### Rate limiting

Preserve or define limits appropriate to the affected abuse case and existing policy. Authentication attempts usually need stronger protection than ordinary reads, but this reference does not prescribe one numeric limit. If enforcement must span multiple processes, account for their aggregate traffic; an isolated in-memory counter cannot establish a global bound. A topology change may require shared enforcement within its actual scope.

Pattern: [Rate limiting](hardening-patterns.md#rate-limiting).

### Secrets

Use the project's secret manager or environment boundary; do not hardcode credentials. If setup changes need an example file, include placeholders only and preserve ignore rules for real secrets. Inspect the relevant diff, including what will be committed when Git work is authorized. **Treat an exposed secret as compromised:** involve the authorized incident owner for revocation/rotation and cleanup. Removing source text alone does not revoke access; history rewriting and production operations retain their own authority.

Pattern: [Secrets management](hardening-patterns.md#secrets-management).

### Dependencies and supply chain

1. **Find the affected installation boundary and manager.** Use the workspace root that owns the authoritative lockfile, or an independent nested project when appropriate. Resolve relevant metadata/CI conflicts before executing dependency changes; continue independent source work. Preserve the project's manager/version policy rather than changing it incidentally.
2. **Block dependency scripts before first execution.** Within authorized installation scope, bootstrap with scripts disabled or a documented fail-closed policy, inspect the pending script source, allow only the minimum and persist the policy in the working tree before a clean frozen/immutable verification. A commit is not a prerequisite for local verification; stage/commit/push only with explicit Git authority. Never blanket-approve.
3. **Run relevant dependency checks using the existing manager when dependencies or install policy change, or when the project requires them for release.** Triage findings by reachability in runtime, build, test and deploy paths, impact and fix availability. Never apply forced remediation (`npm audit fix --force` or equivalent) automatically; review and verify the actual upgrade. Record required unresolved findings and their owner under the project's deferral policy. Missing unrelated audit infrastructure does not create new setup work.
4. **Audits only match known advisories.** They do not catch a newly malicious or typosquatted package (`cross-env` vs `crossenv`). Review new dependencies, lockfile diffs, and script-policy changes together: ownership, maintenance, release age, provenance, transitive graph. Verify registry signatures where supported (`npm audit signatures`, `pnpm audit signatures`) and treat their absence as a signal to investigate, not automatic proof of compromise (A06, LLM03).

Triage decision tree: [Dependency audit triage](hardening-patterns.md#dependency-audit-triage). Manager matrix and install-script gate: `../../../references/security-checklist.md`.

### Personal data and privacy

Hardening asks "can an attacker read it?" Privacy asks "should *we* hold it at all, and for how long?" The cheapest data to protect, breach, and comply over is the data you never collected; treat personal data as a liability to minimize.

- **Classify fields as you add them** (non-personal, PII, sensitive) and handle each class accordingly. You cannot protect, or honor a deletion request for, data you cannot find.
- **Collect only against a stated purpose.** "Might be useful later" is latent breach scope, not a purpose. Keep PII out of telemetry (the `observability-and-instrumentation` skill makes the same point from the ops side).
- **Apply the established retention and deletion requirements** to affected stores, caches, indexes, analytics and backup lifecycles. Identify where the changed data goes; do not invent a universal TTL or destroy retained data to satisfy an example.
- **Support the data-subject rights your jurisdiction requires** (GDPR, CCPA, and kin): export, correct, delete. Design the schema so a user's data is findable and erasable, not smeared irreversibly across systems.
- **Use the project's approved basis and controls for collection and sharing.** Sending personal data to an analytics, ad or LLM vendor is an external disclosure. Resolve missing consent, contractual or regional requirements with the appropriate owner before introducing that use; this skill does not determine legal compliance.

Classification examples: [Data classification](hardening-patterns.md#data-classification). Handle an actual privacy incident through the project's incident and privacy owners; applicable notification and investigation requirements need their own evidence and authority.

### AI / LLM features

Calling an LLM — chatbots, summarizers, agents, RAG — adds a new attack surface; map it to the [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/):

- **Model output is untrusted input** (LLM05). Never into `eval`, SQL, a shell, `innerHTML`, or a file path; parse defensively, validate against a schema, then encode.
- **Prompts can be hijacked** (LLM01). Untrusted text in the context — a user message, a fetched page, a PDF — can carry instructions. The system prompt is not a security boundary; enforce permissions in code.
- **Keep secrets, other tenants' data, and the full system prompt out of the context window** (LLM02, LLM07); scope tool permissions, validate tool arguments, and enforce the granted scope and runtime approvals for destructive actions (LLM06); cap tokens, request rate, and recursion depth (LLM10); partition RAG embeddings per tenant and validate documents before indexing (LLM08).

Pattern: [LLM output handling](hardening-patterns.md#llm-output-handling).

## Review Checklist

If a changed protection needs more detailed verification guidance, select the relevant part of `../../../references/security-checklist.md`; loading it is not a prerequisite for every local edit. Review the changed behavior and any evidenced security impact on its callers; this is not a full-project audit for every local change. Dependency audit/install-policy checks apply when dependencies or that policy change, or when actual release requirements call for them. Missing unrelated CI/audit infrastructure does not create setup work or block source completion; an unmet required release criterion stays open with its owner.

## Security decisions

Internal deployment or framework defaults do not establish that a changed boundary is protected. Verify the enforcement point and the relevant denied case. An audit pass covers known advisory checks, not every supply-chain threat. Likewise, text produced by an LLM is still untrusted before use in queries, commands, HTML or file operations.

Keep personal data use tied to its approved purpose and lifecycle. A template, source comment or skill cannot grant access, establish consent or declare legal compliance.

## Relevant warning signs

- Untrusted input or model output reaches a query, shell, DOM or destructive target without its applicable protection.
- A changed protected path loses resource/tenant authorization or relevant denied-access coverage.
- Credentials or private data appear in source, errors, telemetry or an unauthorized external context.
- A changed URL fetch can reach unintended internal addresses, or an upload bypasses content/size restrictions.
- Dependency execution bypasses the authoritative lockfile or reviewed script policy.
- A changed personal-data flow lacks its approved purpose, retention, sharing or deletion requirements.

Inspect these risks on the affected behavior and its actual callers. An explicitly requested audit can cover a wider agreed surface; an ordinary local edit does not silently become that audit.

## Verification

Select checks for the changed behavior and actual task/release criteria. Reuse valid evidence for untouched controls:

- [ ] The relevant diff/artifacts introduce no exposed secrets; a discovered exposure is handled under the project's incident authority
- [ ] Changed input boundaries validate untrusted values; changed error responses conceal internal details
- [ ] Affected protected paths retain authentication, resource/tenant authorization and denied-access coverage
- [ ] If destructive filesystem behavior changes, target containment and ownership protections remain verified
- [ ] If headers, sessions, auth throttling or deployment topology change, their affected protections are checked
- [ ] If server fetches or AI/LLM behavior change, the affected URL/output trust boundaries are checked
- [ ] If personal-data collection, retention, sharing or export/deletion behavior changes, the affected lifecycle and stores are checked
- [ ] If dependencies/install policy change, or release scope requires it, audit reachability and script/lockfile controls have appropriate evidence; required missing proof stays open

A local validator fix does not require a whole-history scan, audit-tool installation or new CI policy merely to finish this checklist. Do not dismiss an evidenced security defect affecting the agreed behavior as unrelated debt. Mandatory project release/security controls remain binding at their actual boundary.
