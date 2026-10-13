# TASK-003 — Explorer and Reviewer responsibilities

## Assignment and authority

- Goal: separate investigation/review responsibilities from runtime permissions. Explorer and Reviewer do not change application code or implement features or repairs; neither deploys.
- Plan: bounded adapter/documentation correction presented and directly approved in this chat on 2026-10-13.
- Human approval: Khiêm wrote “Approved. Sửa adapters và docs trong Agent Kit theo đúng ý này: Explorer và Reviewer không codechange, không triển khai; permissions theo runtime và task scope, không ép read-only sandbox theo role.”
- Developer owner: Khiêm. Task Owner: this Codex desktop main session for bounded kit maintenance, local verification and sequential review.
- Branch / base commit: `main` / `adba3ee1029690bc4d82dd5dbd28717b238989ba`.
- Owned files: `.codex/agents/kit-explorer.toml`, `.codex/agents/kit-reviewer.toml`, `.claude/agents/kit-explorer.md`, `.claude/agents/kit-reviewer.md`, `AGENTS.md`, `README.md`, `docs/team-policy.md`, `docs/agent-coordination-templates.md`, `docs/roles/explorer.md`, `docs/roles/reviewer.md`, `docs/model-routing.md`, `docs/agent-compatibility.md`, `docs/verification-guide.md`, `docs/skills-manifest.json`, `docs/verification-results.md` and this record.
- Covered actions: remove role-imposed sandbox/tool restrictions from the four adapters; align documentation and verification criteria; refresh affected inventory digests; maintain this record and run local package/documentation checks.
- Latest restriction: no stop instruction received. Git delivery of the owned files is now explicitly authorized as recorded below. Native client/fixture execution, other repositories, global configuration and production actions remain outside this task.
- Shared project context, plan and state remain unassigned templates. This bounded task grants no project-wide coordinator write authority.

## Sources and accepted approach

Sources: direct human clarification and approval, current project instructions and policy, coordination templates, role documents, native adapters, manifest and verification guide. Applied workflows: `using-agent-skills`, `technote`, `documentation-and-adrs`, `code-review-and-quality` and official OpenAI documentation.

Remove Codex `sandbox_mode` and Claude `tools` overrides from Explorer and Reviewer. Do not add another role-based permission profile. Keep existing model inheritance and the implementer adapter unchanged. Use instructions to prohibit application code changes, implementation and deployment. Permit authorized checks, browser/application inspection and evidence capture within actual runtime permissions and assigned side effects, fixtures and destinations. Preserve runtime approval mechanisms, task authority and shared-document ownership.

Official documentation fetched on 2026-10-13: [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents), [Claude frontmatter/tool inheritance](https://code.claude.com/docs/en/sub-agents#frontmatter-reference) and [Claude permission modes](https://code.claude.com/docs/en/sub-agents#permission-modes). These support omitted-field inheritance; they do not prove effective behavior of this checkout in either client.

Acceptance criteria:

1. Codex Explorer/Reviewer omit sandbox overrides; Claude Explorer/Reviewer omit tool and permission overrides. Model inheritance remains unchanged.
2. Both runtimes and common role/policy documents distinguish responsibility from permissions, prohibit application code changes and implementation, and allow authorized verification/evidence capture.
3. V18 checks role behavior and effective permissions separately. Historical verification results remain historical and do not claim current native enforcement.
4. Inventory hashes, skill mirrors, adapter syntax and relevant Markdown references pass local checks. Unrelated files, imported skills, implementer adapters, fresh project state and earlier task records remain unchanged.

Dependencies: none. Model routing: inherit the developer-selected model; no override requested. Exact runtime-observed model/effort: Unknown. No subagents or independent native reviewer are assigned; review is sequential self-review.

## Current state and verification

- Updated: 2026-10-13, Asia/Ho_Chi_Minh.
- State: Verified locally — approved adapter/documentation correction complete; applicable package checks and sequential review passed.
- Initial `git status --short`: empty; no pre-existing changes.
- `git rev-parse HEAD`: confirmed the base commit above.
- Native discovery, invocation, effective permissions and V18 behavioral checks: NOT_RUN; this approval covers package edits and local verification, not a separate client/fixture run.
- The implementation approval did not authorize commit/push. The later direct human delivery approval is recorded below.

| Actual check | Result | Evidence and limit |
| --- | --- | --- |
| Published package-integrity recipe | PASS | Inline `python3` extracted and executed the exact recipe from verification-guide.md: inventory hashes, mirror bytes and 17 skills per root passed. The recipe itself remains byte-identical to the base |
| Adapter syntax and responsibility boundaries | PASS | Inline `python3` with `tomllib` parsed all three Codex adapters; exact required keys, omitted permission/model overrides and matching Codex/Claude instruction bodies passed. Explorer/Reviewer retain no-code-change, no-implementation, no-deployment and runtime/task limits |
| YAML syntax and defaults | PASS | `ruby -rpsych -e` parsed 37 frontmatters: 34 skills and three Claude adapters. Claude adapter keys remain name, description and model; model is inherit, with no tools/disallowedTools/permissionMode override |
| Manifest and provenance | PASS | Inline `python3` compared manifest metadata, 78 inventory entries and 27 mirror definitions with the base; only 13 owned source digests changed. Upstream Git blob hashes match pinned provenance |
| Local Markdown references | PASS | Inline `python3` scanned all tracked Markdown plus TASK-003 outside fenced examples: 202 local links/anchors across 79 files resolved. External links were not checked by this scan; the permission inheritance sources were fetched separately |
| Scope and preservation | PASS | Inline `python3` compared every tracked file with `git show` at the base. Exactly 15 owned tracked files changed; all other tracked files, imported skills, implementer adapters, fresh project context/plan/state and earlier task records remain byte-identical. Verification results retain their complete historical prefix |
| Whitespace and Git state | PASS | `git diff --check` exited 0. `git status --short --branch` showed the 15 owned tracked edits and TASK-003 untracked on main; no staged changes or Git delivery |
| Final review | PASS | Task Owner reviewed responsibilities, permission inheritance, approval/ownership boundaries, both adapter instruction bodies, affected documentation and V18. No unresolved finding. This is sequential self-review; no independent native reviewer ran |
| Native behavior and two-machine compatibility | NOT_RUN | No fresh client discovery/invocation, permission observation or V18 fixture run; static checks do not establish runtime behavior |

The coordinator checklist was applied within this task's ownership: direct approval and restrictions checked; bounded ownership and accepted approach preserved; acceptance defined; outputs and verification limits reviewed; the original misunderstanding corrected across affected adapters/docs and historical evidence; this record updated; handoff prepared. No material approach change or unresolved decision remains. Shared project templates retain their original authority state.

## Handoff

The approved package correction is complete. Current sources: [role responsibilities and runtime permissions](../model-routing.md#role-responsibilities-and-runtime-permissions), [Explorer](../roles/explorer.md), [Reviewer](../roles/reviewer.md) and [V18 verification guidance](../verification-guide.md#required-scenarios).

No required package work remains in TASK-003. The completed changes accompany the authorized delivery below. Native behavior remains Unknown; a future V18 client/fixture run needs its own identified verification scope. This kit-maintenance approval does not grant authority to adopting projects or other repositories.

## Git delivery — 2026-10-13

Khiêm directly authorized delivery in this chat: “Commit và push các thay đổi adapters, docs và TASK-003 lên origin/main.” The scope covers the 16 owned files listed above, including this approval update. The Task Owner stages those exact files, reviews the staged content and whitespace, creates an ordinary commit and pushes the current main branch to origin/main. No branch switch, history rewrite or force push is authorized or required.

Preflight: current branch main; HEAD is `adba3ee1029690bc4d82dd5dbd28717b238989ba`; the index is empty; only the 15 owned tracked edits and TASK-003 are present. The published integrity recipe passed again. The initial sandboxed remote check could not resolve github.com; the approved elevated `git ls-remote origin refs/heads/main` returned the same base SHA. No unrelated changes exist.

This record is included in the delivery commit. Actual commit/push outcomes, remote SHA comparison, divergence and final worktree status are reported in the closing chat after verification; this preflight and approval are not proof that delivery completed. Native behavior remains NOT_RUN.
