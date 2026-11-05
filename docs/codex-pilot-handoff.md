# Codex pilot handoff — Agent Kit lean refactor

**Status: prepared; pilot NOT_RUN.** The current task authorizes source refactoring, package checks and a review PR. It does not authorize applying the kit to another project. Run the pilot only after the owner selects a target and authorizes its isolated worktrees. Do not merge, deploy, change global settings or use real customer data.

## Revisions and fair setup

- **A baseline:** `4f5c3bc7dcb2d052e8fd28699f118a22eb1f82c5`.
- **B candidate:** resolve the review PR's head to one full commit SHA before starting; record it and keep it fixed across the six runs. Branch: `refactor/agent-kit-lean-20261105`.
- Use the **same application starting commit** in separate clean worktrees and independent Codex sessions. Never give one variant the other's implementation, solution, conversation or test results.
- Keep task prompt, acceptance, client/version, model/effort, tools, permissions, dependency lock and environment matched. Record unavoidable differences and known waits separately.
- Apply only the kit instruction surfaces needed for the pilot in the authorized disposable worktrees. Preserve the application's domain rules and project-required controls. Resolve instruction conflicts before timing and document any adaptation equally for A and B.
- Inspect effective loaded instructions and skills. Personal, managed or plugin copies may override repository definitions. If the intended variant is not loaded, the comparison is invalid; do not silently change global configuration to force it.
- Record native discovery/invocation separately from task success. Claude behavior and two-machine compatibility stay NOT_RUN unless separately observed.

Use existing capabilities and safe synthetic data. Do not create a benchmark runner, inject artificial environment failures or install tooling solely to fill a metric.

## Three independent task pairs

| Case | Select a real bounded task | Acceptance and observations |
| --- | --- | --- |
| Focused | A contained content/UI spacing issue with an already clear desired result | Correct changed output; relevant rendered/source check; time to first useful edit; unnecessary approvals, plans, records or skill reads |
| Standard | A reproducible business bug | Cause fixed through actual callers; a regression assertion fails before and passes after; unaffected behavior preserved; relevant checks |
| Long/resume | A feature crossing meaningful layers with fixed acceptance | Complete wiring, relevant tests and no scope drift; pause at the same agreed milestone, explicitly resume in a fresh session, assess preserved decisions/evidence and unnecessary restarts |

Run A and B independently for each case: **six initial runs**. For the long case, choose an observable pause milestone before either run (for example, the first complete vertical slice). Give an explicit resume instruction after each pause. Record one checkpoint per variant with enough state to resume; do not transfer evidence between variants.

Alternate A/B order across cases where practical. Report this small pilot descriptively, not as statistically established universal savings. Repeat only an inconclusive or noisy case, stating why.

## Ready-to-use Codex instruction after pilot authorization

Replace the bracketed values before use. This prompt is for the later authorized pilot, not permission inferred from this file.

```text
Run the Agent Kit pilot described in docs/codex-pilot-handoff.md.

Target repository: [repository/path]
Application starting commit: [full SHA]
Kit A: 4f5c3bc7dcb2d052e8fd28699f118a22eb1f82c5
Kit B: [full reviewed PR head SHA]
Codex client/model/effort: [fixed configuration]
Three task prompts and acceptance: [link or exact text]
Long-case pause milestone: [same observable point for A and B]
Allowed output: [local report or authorized results branch]

I authorize creating disposable local worktrees and running these tasks/checks
there with synthetic data. Keep each A/B task in an independent session and
use the same starting source, prompt, tools and permissions. Preserve project
security/data controls. Do not merge, deploy, alter global configuration,
change the original application worktree or apply the kit elsewhere.

Check effective kit loading before measuring. Execute the six runs using
existing capabilities. Record observed results and unavailable metrics honestly.
Use one concise checkpoint for each long-case resume. Do not build a new harness.
Compare correctness first, then time/tool/context overhead. Return the evidence,
limitations and a recommendation; do not claim native results from source checks.
```

Until that scope is authorized, Codex can review this PR and prepare candidate task prompts read-only; it must not start adoption or pilot execution.

## Record per run

```text
Case / A or B / kit SHA / app SHA:
Exact task prompt, acceptance and long-case pause milestone:
Client version / observed model-effort / effective instruction paths:
Time to first useful application edit / total elapsed / setup and known waits:
Tool calls / skill reads / unchanged rechecks / redundant approvals and records:
Client usage: input/output/reasoning/cache, or NOT_AVAILABLE:
Final diff / acceptance results / security-data and scope findings:
Actual checks: command or observation -> PASS / FAIL / NOT_RUN + limits:
Resume: retained decisions, lost state, unnecessary rereads/rechecks:
```

Time to first useful edit starts at the task prompt, after matched setup. Count checks/reads from available logs; label estimates as estimates. Do not infer token usage from Markdown bytes. Avoid publishing secrets, session credentials or private application content in reports.

## Decision and handoff

Compare correctness and retained boundaries first: missing acceptance, weaker security/data checks or out-of-scope changes fail the case regardless of cost. Then compare time to useful change, total time, tool/skill overhead, unnecessary approvals/records, repeated checks and resume quality. Note any baseline failure too; speed alone is not success.

Return task-by-task deltas, relevant sanitized traces/diffs, full kit/app revisions, actual check results and measurement limits. Recommend adopt, revise or run one targeted follow-up based on the evidence. Source/package checks do not establish native behavior, human acceptance or release. The owner decides adoption and merge separately.
