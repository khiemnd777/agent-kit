# Codex pilot handoff — Agent Kit lean refactor

**Pilot: NOT_RUN.** This is a manual A/B handoff, not a new benchmark harness. Do not merge or deploy during this pilot.

## Revisions and setup

- **A baseline:** `4f5c3bc7dcb2d052e8fd28699f118a22eb1f82c5`.
- **B candidate:** head of `refactor/agent-kit-lean-20261105` / the review PR.
- Start each run in independent worktrees/sessions with the SAME initial application source revision. B must not receive A's code, test results or solution.
- Keep prompt, acceptance, Codex client/version, model/effort, tools, permissions, dependency lock and environment matched.
- Inspect **effective loaded instructions/skills**: personal, managed or plugin copies may override the repo. Do not alter global settings, secrets or real customer data.
- Claude discovery/invocation remains NOT_RUN unless separately observed on Claude.

## Three pilot task pairs

1. **Focused:** adjust a contained UI spacing or content issue. Observe time to first useful edit, redundant approval/records and relevant checks.
2. **Standard:** fix a reproducible business bug with a meaningful regression assertion; inspect root cause, integration and correctness.
3. **Long/resume:** implement a multi-layer feature with fixed acceptance, pause at the same milestone for A and B, resume in new sessions. Observe checkpoint fidelity and unnecessary re-reading/re-testing.

Run A and B independently for each case, six initial runs in total. Prefer existing commands and safe synthetic data. Do not invent environment faults or automatic evaluator infrastructure.

## Record per run

```text
Case / A or B / kit SHA / app SHA:
Exact prompt and acceptance:
Codex client, observed model/effort, effective instruction paths:
Time to first useful change / total elapsed / known waits:
Tool calls / skill reads / unchanged rechecks / redundant approvals and records:
Client usage: input/output/reasoning/cache or NOT_AVAILABLE:
Final diff / quality and scope findings:
Actual checks: command/observation -> PASS / FAIL / NOT_RUN + limits:
Resume: state retained, unnecessary reset or rechecks:
```

Compare quality and security first; reduced cost cannot compensate for missed acceptance, broken permission boundaries or out-of-scope changes. Report task-by-task deltas and measurement limits, not an unverified universal token percentage. Repeat only cases whose results are noisy or inconclusive.

Return the PR link, baseline/candidate SHAs, checks and sanitized native logs/usage if authorized. Source/package checks do not establish runtime, human acceptance or release.
