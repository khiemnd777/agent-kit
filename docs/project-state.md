# Project state

The single current-state summary for an adopting project; link task records rather than duplicate their checklists. These values are not the status of Agent Kit's own release.

| Field | Current value |
| --- | --- |
| Updated | Not initialized |
| shared-record owner | Unassigned |
| Current goal | Unspecified |
| Current plan revision | Unspecified |
| Mode | Planning |
| State | Awaiting project definition |
| Human approval source | None |
| Authorized execution scope | None |
| Latest stop or restriction | No execution authorized |
| Accepted decisions | None |
| Accepted reference sample | None |
| Active tasks / owners | None |
| Integrated project result | None |
| Verification evidence | None |
| Latest feedback | None |
| Next action | Propose the project goal, roles and bounded plan in chat |

The delivery owner proactively updates this summary and affected tasks within authorized writes after approval/scope changes, meaningful results, blockers/stops and before handoff. Keep stable design in project-context.md, intended outcomes in project-plan.md and history in tasks/decisions. This fresh template grants no authority and is not Agent Kit maintenance status. No scheduler or daemon is implied. Distinguish integrated commits from branch results, and agent checks from human acceptance. Verify approval provenance before continuing from another session.

## Kit maintenance pointer — 2026-11-06

[TASK-009](tasks/TASK-009.md) records approved DL01–DL04 source-location guidance in debugging. Source/mirror and metadata complete; package and scoped source checks PASS, journal saved. Optional host validator unavailable (missing yaml); native behavior NOT_RUN; DL01–DL04 HUMAN ACCEPTED / TASK-009 CLOSED by Khiêm on 2026-11-06. Scoped content commit 34973ea pushed to origin/main (exit 0; divergence 0/0); receipt metadata published separately. No native pilot or adopter update. Adoption template values above remain uninitialized; this pointer grants no adoption authority.

Closure metadata publication authorized by Khiêm on 2026-11-09 after read-only review; content commit `9299546` pushed with remote SHA verified; [PR #3](https://github.com/khiemnd777/agent-kit/pull/3) opened against `main`, not merged. No new skill scope, native pilot or deployment. See TASK-009 human acceptance, closure and closure-publication records.

## Kit maintenance pointer — 2026-11-09

Approved README and repository-description refresh completed locally. README now leads with purpose, included components and quick start; workflow details link to existing guidance. README manifest hash updated. Local checks PASS: 24 README paths/applicable anchors, documented package integrity recipe, and diff whitespace. Description draft: “Shared instructions, technical skills, and optional agents for Codex and Claude Code—with explicit planning, approval, and verification.” GitHub rendering/native behavior NOT_RUN. Khiêm accepted the result and authorized commit/push and GitHub description update in the current chat. Description updated and read back on GitHub; content commit `98f491f` pushed and remote SHA verified; [PR #2](https://github.com/khiemnd777/agent-kit/pull/2) opened against `main`, not merged. Publication completion is recorded in the linked correction event. See the linked human-acceptance and publication records beside the implementation journal. [Implementation journal](engineering/skill-usage/records/README-2026-11-09/implementation-1.json) records scope, authority and limits; adoption values above remain uninitialized. Prior TASK-009 closure edits preserved.

## WHAT conversation rule — 2026-11-10

Khiêm authorized adding the WHAT conversation rule and updating the original Agent Kit immediately. Core/workflow/template updated locally; manifest hashes synchronized. Details and verification limits: [WHAT-CHAT-2026-11-10](tasks/WHAT-CHAT-2026-11-10.md). No application implementation, commit/push or deployment. The original kit's adoption template and Church CMS P0 authority remain unchanged.

Package/source checks PASS; implementation journal saved. Cross-session behavior NOT_RUN; human acceptance pending.

Scoped publication now authorized: WHAT changes and related records on `refactor/what-conversation-table` into `main` via PR. Publication in progress; no merge/deploy. See the task publication section.

Publication VERIFIED: WHAT content commit `b10a2b9` pushed with matching remote SHA; [PR #4](https://github.com/khiemnd777/agent-kit/pull/4) open into `main`, not merged. Publication completion correction linked from the task; receipt metadata published separately. Human acceptance pending; cross-session behavior NOT_RUN.

## Kit maintenance pointer — visual acceptance handoff, 2026-11-10

[KIT-HANDOFF-2026-11-10](tasks/KIT-HANDOFF-2026-11-10.md) records the approved original-kit update: delivery classification and planning declaration, two visual handoff templates, predefined meaningful packages and explicit user/Product Owner acceptance/continuation stops. Core/workflow/policy and adoption guidance are synchronized. Source/package checks PASS; [journal](engineering/skill-usage/records/KIT-HANDOFF-2026-11-10/implementation-1.json) saved; human acceptance of this original-kit delivery pending. Native/cross-session behavior NOT_RUN. No commit/push/PR/deployment. Fresh adoption values above remain uninitialized; no Church CMS product scope or execution authority is imported.

Handoff publication VERIFIED: content commit `f112ebf473dc996bb57de6b204ce9362eaca2b3e` pushed with matching remote SHA; [PR](https://github.com/khiemnd777/agent-kit/pull/5) open into `main`, not merged. Completion correction linked from the task; receipt metadata published separately. Native/cross-session behavior NOT_RUN; no deployment.

## Kit maintenance pointer — planning-only documentation, 2026-11-10

[KIT-PLANNING-NOTES-2026-11-10](tasks/KIT-PLANNING-NOTES-2026-11-10.md) implements the approved default permission for bounded local planning documentation from task start, retaining existing task records. Implementation approval, explicit read-only/no-file limits, runtime restrictions and shared-record ownership remain required. Core/policy/workflow, affected skills/mirrors and native instruction wording are synchronized. Source/package checks PASS; [journal](engineering/skill-usage/records/KIT-PLANNING-NOTES-2026-11-10/implementation-1.json) saved; **HUMAN ACCEPTED** by Khiêm; [acceptance](engineering/skill-usage/records/KIT-PLANNING-NOTES-2026-11-10/human-acceptance-1.json). Native/cross-session behavior NOT_RUN. At source handoff Git publication was not yet authorized; adoption template values remain uninitialized.

Planning-note publication VERIFIED: accepted content commit `806b346ac1331ea065333693dfb65007cd466026` pushed with matching remote SHA; [PR](https://github.com/khiemnd777/agent-kit/pull/6) open into `main`, not merged. Completion correction linked from the task; receipt metadata published separately. Native/cross-session behavior NOT_RUN; no deployment.

## Kit maintenance pointer — multi-client proposal, 2026-11-12

[KIT-MULTI-CLIENT-2026-11-12](tasks/KIT-MULTI-CLIENT-2026-11-12.md) is plan v1 for Gemini CLI, Cursor and Grok consumer web/app support. Main session owns delivery. One handoff; no parent roadmap. Khiêm approved plan v1 (“Duyệt”), including Gemini CLI, Cursor and manual Grok web/app support. Local source/package implementation complete under main-session ownership; human acceptance pending. Six new native adapters, shared Gemini import, manual Grok reference/exporter and docs delivered. PASS: 112 inventory entries, 35 mirror pairs, 12 native role definitions, 78 protected files unchanged, 279 links/anchors and four exporter regression tests. Native loading/behavior, Cursor duplicate skill resolution and Grok upload remain NOT_RUN. No client installation, external write, Git publication or deployment performed/authorized. Next action: Khiêm reviews/accepts the source package or authorizes bounded runtime verification. [Validation](tasks/KIT-MULTI-CLIENT-2026-11-12/validation.json); [implementation journal](engineering/skill-usage/records/KIT-MULTI-CLIENT-2026-11-12/implementation-1.json). Fresh adoption template fields remain uninitialized. [Planning journal](engineering/skill-usage/records/KIT-MULTI-CLIENT-2026-11-12/planning-1.json).

## Kit maintenance pointer — README visual redesign, 2026-11-12

[README-VISUAL-2026-11-12](tasks/README-VISUAL-2026-11-12.md) records plan v1 approved by Khiêm (“Duyệt”) and the completed local README redesign: centered introduction, factual badges, benefits, workflow SVG, copyable prompts, component/client tables and documentation links. Concurrent multi-client source content preserved. Source/package, 38 local link/anchor, verbatim prompt and localhost preview checks PASS at desktop/narrow/dark settings; [evidence](tasks/README-VISUAL-2026-11-12/). Actual GitHub rendering/native behavior NOT_RUN. Human acceptance PENDING; no Git publication/deployment authorized. Adoption template fields remain uninitialized. Next action for this task: user reviews local preview and accepts or requests scoped adjustments.

## README visual v1 acceptance / v2 Support proposal — 2026-11-12

Khiêm accepted README v1 and requested a v2 Support presentation for Claude, Codex, Gemini, Cursor and Grok. [Existing task](tasks/README-VISUAL-2026-11-12.md) now records v1 HUMAN ACCEPTED and the v2 standalone one-handoff proposal. Khiêm approved v2 layout with “Duyệt bố cục v2.” Support hero line and standalone reordered client table implemented; README hash synchronized. Package, 39 local path/anchor, labels/order, unchanged prompts and desktop/narrow/dark local preview checks PASS; [v2 evidence](tasks/README-VISUAL-2026-11-12/v2/). v2 human acceptance PENDING; actual GitHub/native rendering NOT_RUN. No Git publication/external writes authorized. Next action: user reviews and accepts v2 or requests scoped adjustments.

### README v2 feedback revision 2 — 2026-11-12

Current README v2 incorporates Khiêm's requested removal of NOT_RUN content from the README; Status and limits now links to verification guide/results. Package integrity, diff whitespace and desktop/narrow/dark preview checks PASS. [Task/evidence](tasks/README-VISUAL-2026-11-12.md). Revised v2 awaits human acceptance; no publication authorized.

### README prompt simplification proposal — 2026-11-12

User requested shorter new-project/existing-codebase prompts. Concrete three-line replacements recorded in [existing task](tasks/README-VISUAL-2026-11-12.md). One handoff, no parent roadmap. Proposed scope replaces the previously preserved prompt bodies and updates README hash/checks. Khiêm approved both drafts and requested README/preview update. Both three-line prompt bodies implemented exactly; README hash synchronized. Package, exact-content, whitespace and local desktop/narrow/dark preview checks PASS. [Evidence](tasks/README-VISUAL-2026-11-12/simplified-prompts/). User review pending. Next action: review updated Quick start preview. No publication authority.

### README preview Copy controls proposal — 2026-11-12

User requests Copy controls. Existing README fenced blocks already use GitHub's built-in copy presentation. Local preview proposal: two semantic Copy buttons, exact prompt clipboard text, success/failure feedback and keyboard/narrow checks. [Task](tasks/README-VISUAL-2026-11-12.md). One handoff, no roadmap; Khiêm approved the Copy UI plan with “Duyệt.” Two buttons implemented in temporary preview. Real clipboard text comparisons, Enter activation, desktop/narrow/dark views and retry after injected API rejection PASS; [evidence](tasks/README-VISUAL-2026-11-12/copy-controls/). Source snapshots saved with task evidence. HUMAN ACCEPTED by Khiêm: “Nghiệm thu nút copy.” README/manifest unchanged in this package; no publication.

### README review-strengths proposal — 2026-11-12

Copy controls HUMAN ACCEPTED. Khiêm approved the review-strengths scope and added Planning/triage/discussion before Handoff & acceptance. Four-part README explanation, benefit bullets and Review outputs navigation implemented. [Existing task](tasks/README-VISUAL-2026-11-12.md) and [evidence](tasks/README-VISUAL-2026-11-12/review-strengths/) record source/package, 48 paths/anchors, preserved prompts/Support, local desktop/narrow/dark and real Copy regression PASS. One handoff; no parent roadmap. Khiêm rejected the literal ASCII treatment: authoring direction must be translated into reader-facing benefits. Superseded the ASCII additions, removed both blocks and internal-format language, and explained proposed-solution clarity before coding plus result/design comparison during handoff. Package/whitespace and desktop/narrow/dark checks PASS; [current evidence](tasks/README-VISUAL-2026-11-12/reader-facing-correction/). Latest content human acceptance PENDING; exact GitHub rendering unverified. No rules/skills/adapters or publication changed. Next action: user reviews and accepts the four-part README preview or requests scoped adjustments.

### README/package version 1.0.0 — 2026-11-12

Khiêm requested 1.0.0, removal of product preview status and field-tested SME positioning. README/badge/manifest updated consistently; hero says “Field-tested across multiple SME projects.” Claim provenance: maintainer instruction, no new independent runtime audit. Historical checks retain original versions. Source/package/Grok-export/whitespace and desktop/narrow/dark local preview PASS; [evidence](tasks/README-VISUAL-2026-11-12/version-1.0.0/). HUMAN ACCEPTED: Khiêm replied “Nghiệm thu.” to the integrated README 1.0.0 handoff. Copy controls previously accepted. Relevant prior technical checks retained. No Git tag, publication, remote release or deploy authorized/performed. No README changes remain requested; publication requires explicit authority.

## Git publication — 2026-11-12

Khiêm explicitly authorized committing all current changes, pushing a task branch and creating a PR into `main`. This supersedes earlier no-publication boundaries for this publication only; no merge, tag or deployment authorized. Current main equals origin/main at 8161bfe. Package integrity, four exporter regression tests, Grok freshness and whitespace checks PASS. Publication is in progress on planned branch `refactor/multi-client-readme-1.0.0`. Runtime/client observations and historical acceptance statuses remain unchanged. [Publication journal](engineering/skill-usage/records/GIT-PUBLISH-2026-11-12/implementation-1.json).
