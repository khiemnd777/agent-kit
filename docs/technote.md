# TechNote

TechNote is a four-level method for explaining technical work. Use it for investigation, planning, review and solution explanations. Start at Level 1 unless the user requests another level. An explicit request such as “TechNote Level 3: booking conflicts” selects the medium and topic; it does not require delivery of earlier levels.

Use English by default. Follow an explicit request for another language. Preserve exact product labels, quotations, identifiers and project naming conventions. The user chooses when to advance, revisit a level or request more detail. Silence does not establish understanding or approval.

## Evidence and scope

Before explaining existing behavior, inspect the relevant source and available evidence. Name the topic, purpose, audience, current authorization, relevant project decisions and evidence limits. If no topic can be identified, ask one short question. Do not expand the agreed problem to fill a presentation.

Distinguish these evidence states in every level:

- **Verified:** supported by inspected evidence. Name the check or source and its scope.
- **Proposed:** a suggested change or approach that has not become an approved decision.
- **Unknown:** information that is missing or behavior that has not been checked. State the next useful check.

An explanation, diagram or simulation does not verify application behavior. A passing build does not establish runtime, integration or production behavior. State relevant limits close to the claim. Separate a supported cause from a hypothesis and identify how to test the hypothesis.

Before producing a website, video or other artifact, check tool capabilities, destination and authorized side effects. A TechNote request authorizes the requested explanation within the existing task boundary; it does not authorize application changes, provider configuration, Git operations, paid services or public publication. Follow project permissions and explicit user authorization. Avoid exposing secrets, personal data or unapproved source material in artifacts or external tools.

## Level 1 — Technical note

Lead with the main result or purpose. Then provide the evidence and limits needed to assess it, followed by the next action. Keep a simple answer short; use labels such as **Verified**, **Proposed**, **Unknown**, **Evidence** and **Next action** only when useful.

Give each sentence one main idea and each paragraph one topic. Prefer active sentences that name the component or actor. Use one term for each concept. Define unfamiliar technical terms on first use. Keep conditions, objects, actions and results explicit: “If the booking overlaps an existing appointment, the service rejects the request.” Do not invent an actor when evidence does not identify one.

Use quantities, units, timing, scope and exceptions when they affect the conclusion. Use numbered steps for a sequence. Explain decisions and tradeoffs briefly. Remove filler, metaphors and unsupported quality claims without losing business meaning. This style is inspired by ASD-STE100; it is not a claim of compliance with that standard or its controlled vocabulary.

### Adaptive reports

Use these minimum before-and-after formats for conversation, planning and implementation. Conversation means discussion or investigation. Select the format for the current work segment; one chat can contain several stages.

Send an opening report when meaningful work starts or its scope changes. Send a closing report when that segment reaches an outcome or needs a material decision. Answer simple follow-ups directly. Reports do not create a new approval gate; continue routine authorized work and repairs.

| Stage | Before work | After work |
| --- | --- | --- |
| Conversation | **Purpose:** question to resolve. **Approach:** how to examine the question. | **Conclusion:** answer or recommendation with its evidence status. **Next:** remaining question, decision or practical action. |
| Planning | **Goal:** observable outcome. **Scope:** components and boundaries the plan covers. | **Plan:** proposed changes in execution order and their purpose. **Acceptance:** observable success conditions. **Decision / Next:** exact decision needed or next authorized action. |
| Implementation | **Change:** intended behavior, affected component, purpose and approval reference. **Verification plan:** checks needed to confirm the change. | **Result:** what changed, where and why. **Verification:** actual checks, results and relevant limits. **Next:** remaining work, delivery action or human review. |

These fields are a starting point, not a length limit. Add information when it affects scope, confidence or the next decision. Keep the following rules across all six formats:

- Place material blockers, failed checks and Unknown information beside the affected claim. Explain the impact and next useful action. Preserve Verified and Proposed distinctions where relevant; omit empty evidence-state sections.
- In implementation's Change field, identify the approved plan or task. Keep approval, implementation, verification, integration and human acceptance distinct. An agent finishing a segment does not establish task completion.
- Report actual check commands and results when applicable. Mark unavailable checks NOT_RUN with the reason. Include meaningful verification limits even when local checks pass.
- Name important components and link current outputs or evidence when useful. For larger plans, link the full plan when an authorized document exists; keep the recommendation, material decisions and acceptance summary visible in chat.
- Omit empty fields, repeated context, unchanged plans, routine tool activity and full logs. Keep detailed acceptance evidence, approval provenance and handoff data in the authorized task record. A short chat report does not replace that record or permit a new file write.
- During meaningful progress updates, state the user result reached, specific remaining failure/dependency, new evidence and limits, and owner/next action with its current approval coverage. Explain the actual problem instead of reporting only “reviewing” or “gating”. Use the current record rather than copying a long template into every message. Follow the environment's update frequency requirements without repeating unchanged information.
- If the approved approach changes materially, explain the evidence, Unknowns and impact, identify affected execution as stopped and present the replacement plan for explicit human approval. An unchanged allowlist does not make the new approach approved. For a human stop, distinguish sent from acknowledged and disclose in-flight/uncancellable or Unknown status; reporting or reviewer PASS cannot resume it. See [approval and autonomy](team-policy.md#approval-and-autonomy).

#### Conversation example

All six examples below describe a fictional mobile export issue. Findings, approval references, commands and results are illustrative; they are not evidence for a real project or a choice of application stack.

Before:

> **Purpose:** Determine why users cannot find Export on mobile.
>
> **Approach:** Inspect the page toolbar and responsive styles.

After:

> **Conclusion — Verified:** Export sits inside a toolbar hidden below 768 px.
>
> **Next — Proposed:** Plan a mobile placement that keeps Export visible. The preferred placement remains Unknown.

#### Planning example

Before:

> **Goal:** Keep Export easy to find on desktop and mobile.
>
> **Scope:** Plan the page toolbar change and its checks. Preserve the existing export behavior.

After:

> **Plan — Proposed:** Move Export into the toolbar's responsive action area, then verify desktop and mobile layouts. Keep the existing export handler.
>
> **Acceptance:** Export remains visible at 390 px and 1280 px, works with keyboard navigation, and downloads the expected file.
>
> **Decision:** Approve plan P1 for the toolbar change and local verification. Deployment requires separate authorization.

#### Implementation example

Before:

> **Change:** Under approved plan P1, update the page toolbar so mobile users can reach Export.
>
> **Verification plan:** Check both viewport sizes, keyboard navigation, downloaded content and the build.

After:

> **Result:** Export is now visible in the page toolbar at desktop and mobile sizes. The export handler is unchanged.
>
> **Verification:** `npm run build` — PASS. Browser checks at 390 px and 1280 px, keyboard navigation and downloaded content — PASS. Production verification — NOT_RUN: deployment is outside the approved scope.
>
> **Next:** Review the local result against P1 acceptance criteria.

## Level 2 — Diagrams

Show actors, data, actions, conditions and results. Use the same terms and examples as the topic's Level 1 explanation when one exists. Separate workflow, data flow and decision logic if combining them would obscure responsibility or state changes.

Choose a diagram format the available tools can render and the user can inspect. Label evidence states within or beside the diagram. Distinguish a proposed architecture from the verified implementation. Explain the diagram's key implication and any omitted scope. A small static engineering diagram can use Mermaid when supported; do not claim a rendered artifact exists without checking it.

## Level 3 — Interactive explanation website

Deliver a usable interactive website that lets the user move through the explanation and inspect data and state changes. Include **Previous**, **Next** and **Replay** controls. Keep state changes understandable and distinguish illustrative simulation from observed application behavior. Use the same topic, terminology and examples as earlier levels when available.

Check navigation, replay/reset behavior, content readability and important viewport sizes with the available tools. Identify Verified, Proposed and Unknown content in the website. Provide a usable local or authorized hosted result and report checks actually performed. If tools cannot create or present the website, state that limitation and the concrete missing capability; do not substitute prose while claiming Level 3 delivery. Public hosting requires authorization.

## Level 4 — Explanation video

Deliver an actual exported video. Use a script, visuals and narration with short segments the user can pause and replay. Use English script, narration, subtitles and on-screen text unless another language is explicitly requested. Keep project labels and evidence states consistent with the topic.

Check recording/rendering capabilities and authorized audio, capture, processing and destination before production. Plan only the necessary segments. Protect source data and distinguish genuine capture from illustration. Verify the exported media, its readability, timing and relevant audio/caption behavior with available tools; report listening or viewing limits. A script, storyboard or render plan alone does not satisfy a video request. If export is unavailable, explain the exact limitation without presenting a script as a finished video.

## Acceptance and examples

Before delivery, check that the selected medium exists, explains the requested topic, preserves scope and naming, separates evidence states and states meaningful verification limits. The user controls further levels and acceptance.

- **Investigation:** “Why do overlapping bookings succeed?” Inspect the booking path and tests. At Level 1 report the verified transaction behavior, any untested concurrency hypothesis and the next check. Do not treat an existing bug as an approved business rule.
- **Direct diagram:** “TechNote Level 2: approval flow.” Produce the requested diagram from relevant project evidence without requiring a Level 1 lesson first. Identify unconfirmed transitions as Unknown.
- **Interactive request:** “TechNote Level 3: retry outcomes.” Build an authorized local interactive explanation with Previous, Next and Replay, showing success, rejection and unknown outcome states. Label invented sample data as illustrative.
- **Limited capability:** “TechNote Level 4: the cache repair.” If no audio/render/export capability is available, report that the video is not delivered and identify the missing capability. Offer a scoped alternative only as an alternative; do not call a written script a video.
