# TASK-001 — README ASCII logo

## Assignment and authority

- Goal: give the README a technical visual identity with the approved ASCII logo.
- Plan: P1, proposed in this chat on 2026-10-13.
- Human approval: Khiêm directly wrote “Approve P1, thêm logo ASCII này vào README.” in this chat on 2026-10-13.
- Developer owner: Khiêm. Task Owner: this Codex desktop main session, performing documentation, verification and sequential review.
- Branch / base commit: `main` / `51b1c810a9920be7fe3957ce454fc25fedf7b155`.
- Owned files: `README.md` and this task record.
- Covered actions: insert the P1 logo below the README title, maintain this record, inspect the diff and run local text/whitespace checks.
- Latest restriction: implementation remains within P1; Git delivery of README and both task records is now explicitly authorized as recorded below. No stop instruction received for P1.
- Shared project context, plan and state remain unassigned templates; this task grants no project-wide coordinator write authority.

## Sources, approach and acceptance

Sources: the user-approved P1 sample, existing README, `AGENTS.md`, team policy, coordination templates and TechNote. Applied workflows: `using-agent-skills`, `technote`, `git-workflow`, `documentation-and-adrs` and `code-review-and-quality`.

Use a fenced `text` block so Markdown preserves ASCII spacing. The existing heading remains readable without decoding the logo. No dependencies or external assets are needed.

Acceptance criteria:

1. The exact approved logo appears once, immediately below `# Agent Kit`.
2. All original README content remains byte-identical after removing the inserted block.
3. The logo contains ASCII characters and spaces without tabs or trailing whitespace; Markdown fences are balanced.
4. Final review finds only the approved README insertion and this task record.

Dependencies: none. Model routing: inherit the developer-selected model; no override requested. Exact observed model/effort: Unknown. No subagents or independent native reviewer ran for this small documentation edit.

## Current state and verification

- Updated: 2026-10-13, Asia/Ho_Chi_Minh.
- State: Verified locally — approved logo inserted; applicable text checks and sequential review passed.
- Baseline: `git --no-optional-locks status --short --branch` showed a clean `main...origin/main`; `git rev-parse HEAD` confirmed the base commit above.
- Exact-content check: PASS — a one-off Python standard-library check compared `README.md` with `git show HEAD:README.md`; it verified the exact P1 block, placement, original bytes, ASCII, no tabs/trailing whitespace and balanced fences. Maximum logo width: 44 characters.
- `git diff --check`: PASS — exit 0.
- `git diff -- README.md`: inspected — exactly nine added lines below the existing title.
- `git --no-optional-locks status --short --branch`: only `README.md` modified and this task record untracked; no unrelated changes.
- GitHub rendered preview: NOT_RUN; rendered layout was not inspected during P1 verification.
- Application tests/builds: NOT_RUN; this task changes documentation only.
- Review question: does the change reproduce P1, preserve existing content and avoid added dependencies or authority claims? PASS — the Task Owner inspected the final README diff and task record. This is sequential self-review, not independent reviewer or human approval.

Coordinator checklist applied within this task's ownership: direct P1 approval and current restrictions checked; the approved approach and file ownership preserved; acceptance defined before editing; actual output and evidence limits inspected; applicable checks and review completed; no earlier feedback remains open; this record updated; closing report prepared; authorized execution complete with no expansion of authority. Shared template documents were not updated.

## Handoff

Current output: [README](../../README.md). P1 implementation is complete; this record accompanies the authorized documentation delivery.

No required implementation work remains within P1. Human visual acceptance remains separate from local verification.

## Git delivery — 2026-10-13

Khiêm directly authorized delivery in this chat: “Commit và push các thay đổi README cùng hai task records lên origin/main.” Covered files are `README.md`, `docs/tasks/TASK-001.md` and `docs/tasks/TASK-002.md`. The Task Owner performs an ordinary commit and push from the current `main` branch, then verifies remote SHA, divergence and worktree status.

Remote preflight: `git ls-remote origin refs/heads/main` returned `51b1c810a9920be7fe3957ce454fc25fedf7b155`, matching the local base. No unrelated work or staged changes were present. This record is included in the requested delivery commit. Actual commit/push outcomes and final remote verification are reported in the closing chat; this preflight is not proof of a completed push.

See [TASK-002](TASK-002.md) for the companion prompt change. Template installation, native behavior, application changes and configuration changes remain outside this delivery scope.
