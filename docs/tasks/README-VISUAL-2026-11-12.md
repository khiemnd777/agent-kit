# README visual redesign — plan v1

Status: HUMAN ACCEPTED — integrated README 1.0.0. No Git publication authorized.

## Intent and source
User requests a visual, explicit, easy-to-understand README based on supplied JevEval reference: centered identity, short promise, factual badges, navigation, benefits and an early workflow diagram.
Current README.md and docs/handoff-templates.md inspected. README currently uses English; propose retaining that product language. Conversation remains Vietnamese.

## Proposed scope
- README.md: centered hero, short value proposition, factual status/license badges and anchor navigation; Why Agent Kit; early How it works; included components; two copyable onboarding prompts; compact documentation/limits/license.
- Optional repo-local SVG workflow asset under docs/assets/, with text/alt equivalent and readable light/dark presentation.
- Synchronize README integrity metadata in docs/skills-manifest.json after approved edits. Verify links/anchors, package integrity and rendered readability where tools permit; report any missing render verification.
- Preserve planning/approval, verification limits, provenance and license; no new agent behavior, client support claims or publication.

## Acceptance
- Reader can identify purpose, value and first action from the opening sections.
- Workflow diagram accurately shows investigation/plan -> human approval -> implementation -> verification -> handoff.
- Existing new-project and existing-project prompts remain accessible and copyable.
- Factual claims, local paths/anchors and manifest agree with current source; preview and runtime evidence remain distinct.

## Concurrent work and authority
Existing multi-client changes and project-state.md are owned by another active task. Do not overwrite them or infer final supported-client status from in-progress artifacts. Reconcile approved source at implementation time.
At initial planning handoff only this planning record and phase journal were saved. Plan approval is recorded below. No Git publication/external writes authorized.

## Approval and implementation — 2026-11-12

Khiêm approved plan v1 with “Duyệt” in this chat. Local README, optional SVG assets, integrity metadata and relevant verification are authorized. No Git publication, external writes or deployment.

Implemented the approved layout with local badge/workflow SVGs, early benefits and workflow, collapsible verbatim onboarding prompts, included components, client entrypoint table and compact documentation/status/attribution. Retained the concurrent multi-client source distinctions; no adapter or exporter changes. Verification in progress; human acceptance pending.

## Implementation handoff — revision v1

Source complete; human acceptance PENDING. README and two self-contained local SVGs implemented. README hash plus asset inventory entries synchronized without resetting concurrent multi-client changes.

### Actual verification
- PASS: 38 README local paths/applicable anchors; both onboarding prompt bodies preserved verbatim from the multi-client working snapshot.
- PASS: two SVG XML documents, titles and no external visual resources.
- PASS: documented package integrity recipe; Grok export --check; git diff --check.
- PASS: local Chrome preview at 1440 px and 390 px plus dark background; no document horizontal overflow, both images loaded, both disclosure prompts expanded, all internal navigation anchors resolved. Three tables rendered.
- Preview generated in /tmp using installed Ruby RDoc with local HTML/table/anchor adaptation; CSS approximates GitHub, not an observed GitHub render. Initial headless attempt inside sandbox aborted and local bind was denied; approved escalated localhost checks succeeded. Preview renderer anchor/table handling corrected before final evidence. No product defect or gate weakened.
- NOT_RUN: actual GitHub rendering and native client behavior; no publication, deployment or source upload.
- On narrow screens SVG text scales down; the five numbered text steps preserve readable workflow content.

### Evidence
See the adjacent README-VISUAL-2026-11-12/ directory for desktop/mobile/dark/full screenshots, browser-check.json, package-check.txt and content-check.txt. Temporary local preview: http://127.0.0.1:18763/ (session-local server; not published).

### Review
Compared delivered workflow to AGENTS.md and team workflow. Preserved approval/acceptance boundaries, source-versus-runtime limits, client distinctions, MIT attribution and upstream pin. Reviewed content against multi-client working snapshot; no adapters, exporter, skills or agent rules changed in this task. Self-review only; no independent agent review claimed.

## v1 acceptance and v2 request — 2026-11-12

Khiêm explicitly accepted v1: “nghiệm thu v1. mở v2: tôi muốn thêm vào mục Support: Claude, Codex, Gemini, Cursor, Grok.” v1 human evaluation recorded separately, preserving the original handoff journal. No publication authority granted.

### v2 proposed plan
Delivery: One handoff. Rationale: one bounded README presentation update reviewed together. Parent roadmap: None; v2 is a standalone revision of accepted README v1, not a new roadmap.

- Add a concise Support line in the centered introduction with the requested visible labels/order: Claude, Codex, Gemini, Cursor, Grok. Link to the Support section.
- Promote existing Choose your client subsection to standalone Support, reusing its table rather than creating another technical matrix. Order clients as requested and display Claude (Claude Code), Codex, Gemini (Gemini CLI), Cursor, Grok (web/app). Preserve source/runtime and manual-reference distinctions.
- Synchronize README hash only; update current task/state/journal and local preview evidence. Check links/anchors, package integrity and desktop/narrow rendering. No runtime/adapter/skill changes, new client claims, Git publication or external writes.
- Acceptance: all five names visible near the top, Support anchor resolves, corresponding client rows remain accurate, v1 layout and copyable prompts preserved.

Implementation not yet authorized: request opens v2, while AGENTS.md requires approval of the presented plan before implementation. README/assets/manifest remain unchanged in this planning turn.

## v2 approval — 2026-11-12

Khiêm approved the presented layout with “Duyệt bố cục v2.” This authorizes the scoped local Support presentation, README hash, records and checks. No Git publication or external changes. Implemented the hero Support line linking to #support and promoted/reordered the existing table, preserving client setup details and source/runtime limits. Verification in progress.

## v2 implementation handoff — 2026-11-12

Implemented the approved hero Support line with Claude, Codex, Gemini, Cursor and Grok linking to #support; promoted existing client table to Support and ordered its five rows accordingly. Claude Code, Gemini CLI and manual Grok web/app scope remain explicit. Only README hash changed in the manifest for this revision. v1 prompt bodies and SVG assets preserved.

PASS: 39 local README paths/anchors; exact requested labels/order; both v1 prompts unchanged; documented package integrity; Grok export --check; git diff --check. Local Chrome checks PASS at 1440 px, 390 px and dark setting: images loaded, prompts expanded, internal anchors resolved and no page horizontal overflow. Local preview reviewed visually at desktop and narrow widths. Evidence: README-VISUAL-2026-11-12/v2/. Previous session localhost processes had stopped; restarted for verification.

Source self-review complete. Local preview is an approximation of GitHub using the existing temporary renderer, not an actual GitHub observation. Actual GitHub rendering and native runtime NOT_RUN. Human v2 acceptance PENDING. No publication/deploy. Local preview http://127.0.0.1:18763/.

## v2 scoped feedback repair — revision 2, 2026-11-12

Khiêm requested “Bỏ nội dung NOT_RUN đi.” Applied as a bounded presentation adjustment to current approved v2: removed the two NOT_RUN sentences from README Status and limits; retained the preview version and a short link to verification guide/results. Existing detailed evidence documents remain historical source records. README hash synchronized and temporary preview regenerated.

PASS: no NOT_RUN text in README; replacement document targets exist; documented package integrity; diff whitespace; desktop/narrow/dark browser checks. Updated full screenshot and browser evidence in v2-revision2/. Human acceptance of revised v2 pending; no publication.

## Prompt simplification proposal — 2026-11-12

User requested simplification of new-project and existing-codebase commands/prompts. One handoff; no parent roadmap. Scope: replace only the two copyable prompt bodies, synchronize README hash and recheck content/links/package/preview. This revises the prior verbatim-prompt acceptance condition, so plan approval is pending. Publication remains unauthorized.

Proposed new-project prompt:

```text
Create [project name] for [target users] to [goal] using https://github.com/khiemnd777/agent-kit.
Inspect the template, propose a plan, and wait for my approval before setup.
After approval, start with fresh project records and verify the app runs.
```

Proposed existing-codebase prompt:

```text
Integrate https://github.com/khiemnd777/agent-kit into this codebase.
Inspect the project and propose a minimal plan. Preserve existing rules, stack, records, and current work.
Wait for my approval, then apply the plan and verify the integration.
```

Keep approval before setup/integration; fresh records for new projects; existing rules/stack/records/current work preserved for integration. Detailed operating rules remain in the kit source. No README implementation yet.

## Prompt simplification approval and implementation — 2026-11-12

Khiêm approved both exact drafts: “Duyệt 2 hai prompts trên, cập nhật README và preview để tôi xem.” Replaced only the two text prompt bodies with the approved three-line versions and synchronized README hash. Local preview refresh and scoped checks authorized; no publication. Verification in progress.

## Simplified prompts handoff — 2026-11-12

Both approved three-line prompt bodies are implemented exactly. README hash synchronized. PASS: exact prompt content assertion; documented package integrity recipe; diff whitespace; local browser checks at 1440 px, 390 px and dark setting (images, prompt expansion, internal navigation, no document horizontal overflow). Visual check confirms both expanded prompts show the new text; screenshot and browser results saved under simplified-prompts/. Self-review complete. No changes to Support, instructions, adapters or SVGs. Actual GitHub rendering unverified; no publication. User review pending. Local preview http://127.0.0.1:18763/#quick-start.

## Copy button proposal — 2026-11-12

User asks for a Copy button. One handoff; no parent roadmap. Official GitHub source confirms built-in Markdown code block copy buttons: https://github.blog/news-insights/product-news/whats-new-from-github-changelog-may-2021-recap/ . Current README already uses fenced text blocks. Local preview renderer has no copy control.

Propose adding a semantic Copy button for each of the two prompt blocks in the local preview. ASCII mockup: prompt title [Copy], followed by the unchanged prompt text. Copy exact prompt text including line breaks, success label Copied!, failure feedback if clipboard permission/API fails. Keep keyboard focus and narrow-screen usability. No content, README hash, Git publication or GitHub customization changes needed. Scope: existing temporary preview renderer and local task/state/journal/evidence. Acceptance: two buttons, exact clipboard content for each, accurate success/failure feedback and desktop/narrow usability. UI plan approval pending under AGENTS.md and frontend-ui-engineering preview rule.

## Copy controls approval — 2026-11-12

Khiêm approved the two-button UI plan with “Duyệt.” Scope: existing temporary local preview renderer, Copy controls, real clipboard checks, scoped task/state/journal/evidence. No README content or package-source change, publication or global settings. Implemented semantic buttons with exact-text copy, asynchronous success/error feedback, polite status region, visible keyboard focus and narrow-screen touch targets. Verification follows completed wiring.

## Copy controls implementation handoff — 2026-11-12

Two real Copy buttons implemented in temporary localhost preview, with async Clipboard API, exact prompt text, Copied! feedback, honest error fallback, polite status regions, keyboard focus and 44 px narrow-screen targets. README and manifest unchanged in this package; GitHub rendering is not customized. Local renderer/CSS/JS snapshots and browser evidence saved in copy-controls/.

PASS: actual clipboard write/read text equals each README prompt at desktop 1440 px, narrow 390 px and dark setting; trusted Enter and mouse activation, success feedback, two controls, accessible labels/status regions, target sizes and reachability. PASS: injected Clipboard API rejection shows error instead of success, and restored API retry copies the exact prompt. This error-branch check uses controlled rejection, not proof of native permission-denial behavior. Native browser clipboard was used for all successful text comparisons.

Initial keyboard test sent Enter without the character payload and did not activate native button behavior; corrected the test input (not the product or assertion), after which exact clipboard comparisons passed. A native CDP clipboard-write permission denial did not cause the expected API rejection under the test activation; that expectation was not treated as product failure. Replaced only that error trigger with explicit API rejection and retained the honest-error/retry assertions; this limit is recorded.

Self-review and visual inspection complete on desktop/narrow screenshots. No README/agent/runtime changes or publication. Human acceptance pending. Preview http://127.0.0.1:18763/#quick-start.

## Copy acceptance and review-strengths proposal — 2026-11-12

Khiêm explicitly accepted Copy controls: “Nghiệm thu nút copy.” Separate human evaluation saved; publication remains unauthorized.

New request: showcase Agent Kit strengths beyond the current workflow: WHAT at planning/done handoffs, participating Skills table, and handoff/acceptance records. Delivery: One handoff; all three belong to one README explanation reviewed together. Parent roadmap: None. Proposal only; implementation awaits plan approval.

### Proposed bounded outcome
- Update Why Agent Kit bullets to name scope visibility (WHAT), visible skill contributions and evidence-led handoff/human acceptance.
- Add a compact See what you are approving section after How it works and before Quick start, with three source-grounded examples using one consistently labeled illustrative task.
- WHAT: show planning and completion tables with stable item names and exact canonical columns Name, Purpose, Location, Status, Reason if undone/ignored. Distinguish scope status from behavior verified and human acceptance.
- Skills: show Skill, Source, Actual contribution, Estimated participation %, using Repo/Personal labels; percentages are subjective participation estimates, not measured savings, runtime or effectiveness. Include only actually applied skills in real task reports. Illustrative example not evidence of an actual task.
- Handoff/acceptance: show a compact record naming revision/result, preview or diagram, acceptance checklist, check evidence/limits, human decision and next step. It is a review aid; no automatic human acceptance or release. Link authoritative handoff templates.
- Include anchors in hero navigation as needed, existing source links, README hash synchronization and preview rendering. Preserve accepted Support, short prompts and local Copy controls; change no operating rules, skills, adapters, workflows or publication scope.

### Acceptance and verification
All three strengths can be understood from concise explanations and examples; WHAT covers both planning/done; Skills fields/estimates align with source; handoff separates technical evidence and human acceptance. README examples explicitly illustrative, not claims of runtime output. Verify local paths/anchors, manifest integrity, prompt/Copy regression and desktop/narrow preview.

### Sources inspected
AGENTS.md Show WHAT / Select and report skills / Finish and hand off; docs/handoff-templates.md; docs/engineering/skill-usage/README.md. Documentation-and-adrs skill applied to source grounding and compact information architecture. No README/preview change in this planning turn.

## Review strengths approval with Planning/triage/discussion — 2026-11-12

Khiêm approved the preceding scope and added: “Duyệt scope trên, nhưng tôi muốn thêm cơ chế Planning/triage/discussion, đặt trước Handoff & acceptance.” This approves the amended four-part README explanation in one handoff, with no parent roadmap: WHAT, Skills, Planning/triage/discussion, Handoff & acceptance. Local content, README hash, preview and checks authorized; no kit-rule changes or publication.

Implemented named benefit bullets and See what you are approving after workflow. One explicitly illustrative Copy-controls example spans planning/completion WHAT tables, Skills table, triage/discussion/plan narrative and review record. Canonical sources linked. Exact accepted onboarding prompts, Support and local Copy implementation retained. Skill files read for triage/planning/discussion were content sources, not additional execution skills. Verification in progress.

## Review strengths implementation handoff — revision 1, 2026-11-12

Completed the approved four-part explanation: WHAT (planning/completion), Skills contributions, Planning/triage/discussion immediately before Handoff & acceptance. Why Agent Kit now names these strengths; hero navigation links Review outputs. Examples consistently use an explicitly illustrative Copy-controls task, not fabricated execution evidence. Source rules, skills and adapters unchanged.

### Acceptance and actual checks
- PASS: both WHAT tables retain Name/Purpose/Location/Status/Reason columns and stable Copy controls identity.
- PASS: Skills fields and source labels match current journal policy; subjective estimate caveat and no-skill behavior included.
- PASS: requested Planning/triage/discussion placement; source ownership vs verified cause, facts/proposals/open questions, plan approval and bounded planning notes explained from current sources.
- PASS: handoff record contains revision/result/visual, acceptance observations, actual checks/limits, WHAT/Skills, human decision and next action; release/acceptance distinct.
- PASS: 48 local README paths/anchors; accepted onboarding prompt bodies and Support section unchanged; README has no NOT_RUN text; hash synchronized.
- PASS: documented package integrity, Grok export --check, git diff --check.
- PASS: local preview 1440 px/390 px/dark, six tables, images, prompt disclosures, internal navigation, no page horizontal overflow. Narrow tables use horizontal scrolling.
- PASS: Copy regression at all three settings: actual clipboard equals each unchanged prompt, Enter/mouse activation and success feedback. Controlled API rejection/retry PASS; native denial behavior remains outside the claim.
- Self-review and actual screenshot inspection complete. Exact GitHub rendering not observed; local renderer approximates GitHub. No independent review claimed, no publication/deploy.

Evidence saved in review-strengths/. Preview http://127.0.0.1:18763/#see-what-youre-approving. Human acceptance pending for this content package.

## Review-strengths scoped ASCII correction — 2026-11-12

Khiêm identified missing ASCII mockups in both Planning/triage/discussion and Handoff/acceptance. Applied as a bounded correction inside the approved README explanation package. Added a proposed UI mockup with placement, exact-copy action, pending/success/error states and approval decision; replaced the plain handoff record with a boxed ASCII layout/review record showing both controls, evidence fields, review observations, limits, WHAT/Skills and human decision.

UI pre-approval ASCII requirement grounded in AGENTS.md/team-workflow; handoff ASCII is explicitly a summary and does not replace actual result images or claim execution evidence. No new rule requiring ASCII-only handoff, no agent/skill changes. README hash updated; verification in progress.

## ASCII correction handoff — review strengths revision 2, 2026-11-12

Both requested ASCII mockups implemented and reviewed visually: Planning shows the proposed prompt/control layout plus placement, action, success/error and approval; Handoff shows both controls and a boxed evidence/checklist/decision record for comparison with the agreed mockup. Frame borders aligned at 58 columns. Mockups remain explicitly illustrative; actual result-image evidence is still required for UI delivery.

PASS: required sections and distinctions; accepted onboarding prompt bodies unchanged; six actual Markdown tables and four code blocks render intact; documented package integrity; whitespace; localhost desktop/narrow/dark navigation/images/disclosures/no document overflow. Narrow code blocks scroll horizontally. Local preview renderer originally misread ASCII pipe lines as Markdown table rows; fixed fence tracking in the temporary renderer and retained the six-table assertion. This was a preview-rendering defect, not a source-rule change. Previous unaffected Copy behavior checks retained; Copy source unchanged. Evidence: ascii-mockups/. Actual GitHub rendering unverified; human content acceptance pending; no publication.

## User correction: distinguish authoring instructions from README copy — 2026-11-12

Khiêm rejected the literal interpretation of “mockup as ASCII”: it was explanatory direction to the agent, not text/artifacts to reproduce verbatim in the README. Prior ASCII correction is superseded. Removed both added ASCII blocks and literal implementation-oriented wording. Rewrote the content as reader benefits: picture/agree on the proposed solution before coding; compare delivered result against the accepted design with evidence and a real human decision. No instruction/rule change or publication.

Reader-facing correction verified: removed literal ASCII blocks/terminology; the two onboarding prompts remain the only code blocks. Package integrity and diff whitespace PASS; desktop/narrow/dark preview PASS with six tables, images, disclosures, anchors and no page overflow. Screenshot reviewed. Supersedes the prior ASCII delivery; user acceptance pending.

## Version 1.0.0 and SME positioning — 2026-11-12

Khiêm requested: “Nâng lên Version 1.0.0, bỏ preview, ghi là thực chiến qua nhiều SME Projects.” Applied as a scoped README/package-metadata revision: README version/alt text and local badge now 1.0.0 without product preview designation; hero states “Field-tested across multiple SME projects.” Manifest kit_version and release_status updated, with maintained README/badge hashes synchronized. Statement provenance is Khiêm's explicit maintainer instruction, not a new independently measured runtime finding. No client names, customer identities, counts or performance claims added. Historical verification observations retain their original version/date; local visual preview terminology still means a view of the README, not the product status. No Git tag, publication, release or deployment authorized/performed. Verification in progress.

Version/positioning checks PASS: README and badge show 1.0.0 without product preview designation; manifest kit_version/release_status match; SME statement present; valid SVG. Package integrity, Grok export --check and diff whitespace PASS. Local desktop/narrow/dark preview PASS, images/links/disclosures/six tables/no page overflow; screenshots reviewed. Maintainer statement is user-provided, not independently audited. Historical verification records retain original versions. Evidence saved under version-1.0.0/. Local source complete; user acceptance pending; no tag, remote release or deployment.

## Final integrated README 1.0.0 human acceptance — 2026-11-12

Khiêm replied “Nghiệm thu.” after the latest README 1.0.0 handoff. Current integrated README accepted, including approved Support, short prompts, review-strengths presentation after wording correction, 1.0.0/badge/metadata and SME positioning. Copy controls were separately accepted earlier. Latest technical evidence retained without rerunning unchanged checks. No commit/push, Git tag, remote release or deployment authorized by acceptance alone.
