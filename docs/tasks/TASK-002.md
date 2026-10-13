# TASK-002 — README quick-start prompts

## Assignment and authority

- Goal: let developers copy a prompt to start a new project or integrate Agent Kit into an existing codebase.
- Plan: revised P2; both prompt samples proposed in this chat on 2026-10-13.
- Human approval: Khiêm directly wrote “Approve P2, thêm cả hai phần New project và Existing codebase vào README với prompt như trên.” in this chat on 2026-10-13.
- Developer owner: Khiêm. Task Owner: this Codex desktop main session, performing documentation, local verification and sequential review.
- Branch / base commit: `main` / `51b1c810a9920be7fe3957ce454fc25fedf7b155`.
- Owned files: `README.md` and this task record.
- Covered actions: add both approved prompt sections under Quick start, maintain this record and run local text/formatting checks.
- Latest restriction: implementation remains within revised P2; Git delivery of README and both task records is now explicitly authorized as recorded below. Actual template installation and application changes remain outside scope. No stop instruction received for P2.
- Shared context, plan and state remain fresh unassigned templates; this task gives no project-wide coordinator write authority.

## Sources, approach and acceptance

Sources: the current README, the two user-approved prompt samples, `AGENTS.md`, team policy, coordination templates and TechNote. Reuse the documentation, Git inspection and review workflows already read in this chat.

Add `New project` and `Existing codebase` subsections under Quick start. Use fenced `text` blocks. Explain where to paste each prompt and how to replace the new-project input fields. The new-project prompt starts with fresh records; the existing-codebase prompt preserves current rules, skills, configuration and records. Both prompts require approval before writing.

Acceptance criteria:

1. Each subsection contains its exact approved prompt once and the template URL.
2. All pre-P2 README content, including the approved ASCII logo and preview verification limits, remains unchanged.
3. Markdown fences and relative links remain valid; no trailing whitespace is added.
4. The prior P1 task record is unchanged; only README and this record receive P2 edits.

Baseline: README SHA-256 `50d64efad051ba700989b78fabf17936ab381ae61bf6f850c5a9f0fbbecffb4a`; TASK-001 SHA-256 `f4c54ebd12827dadd02f8bae887e0bca4de0ede342b933b828ab89f65a144dc2`. Initial Git status contained only the P1 README edit and untracked TASK-001.

Dependencies: none. Model routing: inherit the developer-selected model with no override. Exact observed model/effort: Unknown. No subagents or independent native reviewer ran for this small documentation task.

## State, verification and handoff

- Updated: 2026-10-13, Asia/Ho_Chi_Minh.
- State: Verified locally — both approved sections added; applicable documentation checks and sequential review passed.
- One-off Python standard-library check: PASS — both exact prompt blocks appear once under Quick start; removing only the P2 insertions restores the recorded pre-P2 README hash; TASK-001 hash is unchanged; all three `text` blocks have balanced fences; relative links/anchors and whitespace are valid; Git scope contains only the P1/P2 files.
- `git diff --check`: PASS — exit 0.
- `git diff -- README.md`: inspected — P2 adds 33 lines under Quick start; the earlier nine-line P1 logo addition remains intact.
- Changed-file scope at P2 implementation completion: `README.md` modified; TASK-001 and TASK-002 untracked; no unrelated changes.
- GitHub rendered preview and native integration behavior: NOT_RUN; this approval covers documentation only.
- Application tests/builds: NOT_RUN; no application behavior changes.
- Review question: do the examples match the approved prompts, clearly distinguish both starting points and preserve approval/data boundaries? PASS — the Task Owner inspected the README diff and this record. This is sequential self-review, not independent or human acceptance. The earlier daily-use command proposal was superseded before writing; only the approved two integration prompts were added.

Coordinator checklist applied within task ownership: direct revised-P2 approval and restrictions checked; approach, ownership and existing work preserved; acceptance defined before writing; actual output and evidence limits inspected; checks and review completed; clarification reflected across both requested sections; this record updated; closing report prepared; approved implementation complete with no expanded authority. Shared template state was not updated.

Output: [README](../../README.md). Both prompt sections are complete; this record accompanies the authorized documentation delivery. No required implementation work remains in P2. Human acceptance remains separate from local verification.

## Git delivery — 2026-10-13

Khiêm directly authorized delivery in this chat: “Commit và push các thay đổi README cùng hai task records lên origin/main.” Covered files are `README.md`, `docs/tasks/TASK-001.md` and `docs/tasks/TASK-002.md`. This delivery also updates both records to reconcile their earlier Git restrictions with the current human authorization.

Remote preflight: `git ls-remote origin refs/heads/main` returned `51b1c810a9920be7fe3957ce454fc25fedf7b155`, matching the current local HEAD. The Git index was empty and only the requested files were changed. The Task Owner stages those exact paths, reviews the staged diff and whitespace, creates an ordinary documentation commit and pushes `main` to `origin/main` without rewriting history.

This record is included in that delivery commit. Actual commit/push outcomes, final remote SHA, divergence and worktree status are reported in the closing chat after verification; this preflight does not establish completed delivery. Native integration and application verification remain NOT_RUN. Shared project template state is unchanged.
