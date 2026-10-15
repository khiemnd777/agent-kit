---
name: incremental-implementation
description: Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the next task from a plan. Use when rolling a change out behind a feature flag, when you're about to write a large amount of code at once, or when a task feels too big to land in one step.
---

# Incremental Implementation

## Overview

Build in thin vertical slices — implement one piece, test it, verify it, then expand. Avoid implementing an entire feature in one pass. Each increment should leave the system in a working, testable state. This is the execution discipline that makes large features manageable.

This Agent Kit adaptation follows [verification scope and completion](../../../docs/team-policy.md#verification-scope-and-completion). Choose checks for the changed behavior and risk; the cycle below is guidance, not a mandatory full-suite/runtime/commit gate for every edit.

When the task applies a human-approved internal or user-supplied template, follow the [template application reference](../../references/template-application.md) and [shared acceptance checklist](../../../docs/template-application-acceptance.md). External design references remain evidence for design selection, not substitutes for the approved template.

## When to Use

- Implementing any multi-file change
- Building a new feature from a task breakdown
- Refactoring existing code
- Any time you're tempted to write more than ~100 lines before testing

**When NOT to use:** Single-file, single-function changes where the scope is already minimal.

## The Increment Cycle

```
Implement a coherent slice
    → Run applicable authorized checks
    → Review the result and evidence limits
    → Repair affected findings or hand off the stated result
    → Continue independent authorized work
```

For each slice:

1. **Implement** the smallest complete piece of functionality
2. **Select checks** for the slice's criteria, changed behavior and risk; write meaningful regression coverage where appropriate
3. **Verify the claim** with applicable authorized checks; reuse valid evidence and state what remains unproved
4. **Review and hand off** the actual result; commit only when Git delivery is explicitly authorized
5. **Move to independent work** while keeping affected unmet criteria open; carry forward valid evidence

## Slicing Strategies

### Vertical Slices (Preferred)

Build one complete path through the stack:

```
Slice 1: Create a task (DB + API + basic UI)
    → Tests pass, user can create a task via the UI

Slice 2: List tasks (query + API + UI)
    → Tests pass, user can see their tasks

Slice 3: Edit a task (update + API + UI)
    → Tests pass, user can modify tasks

Slice 4: Delete a task (delete + API + UI + confirmation)
    → Tests pass, full CRUD complete
```

Each slice delivers working end-to-end functionality.

For approved-template application, the first slice is one representative screen wired to the real controller and data path. Compare its rendered desktop/mobile result with the approved template at matched viewports and check the primary interaction sequence and applicable data/permission states. Record PASS/FAIL/NOT_RUN for structure, hierarchy, controls, focus, responsive behavior, preview identity and clipping where relevant. The Coordinator confirms the screen against evidence before dependent implementation expands. Build/source PASS alone cannot confirm UI fidelity; a missing runtime or data prerequisite stays NOT_RUN. This checkpoint uses current approval and does not demand human approval for each step.

### Contract-First Slicing

When backend and frontend need to develop in parallel:

```
Slice 0: Define the API contract (types, interfaces, OpenAPI spec)
Slice 1a: Implement backend against the contract + API tests
Slice 1b: Implement frontend against mock data matching the contract
Slice 2: Integrate and test end-to-end
```

### Risk-First Slicing

Tackle the riskiest or most uncertain piece first:

```
Slice 1: Prove the WebSocket connection works (highest risk)
Slice 2: Build real-time task updates on the proven connection
Slice 3: Add offline support and reconnection
```

If Slice 1 fails, you discover it before investing in Slices 2 and 3.

## Implementation Rules

### Rule 0: Simplicity First

Before writing any code, ask: "What is the simplest thing that could work?"

After writing code, review it against these checks:
- Can this be done in fewer lines?
- Are these abstractions earning their complexity?
- Would a staff engineer look at this and say "why didn't you just..."?
- Am I building for hypothetical future requirements, or the current task?

```
SIMPLICITY CHECK:
✗ Generic EventBus with middleware pipeline for one notification
✓ Simple function call

✗ Abstract factory pattern for two similar components
✓ Two straightforward components with shared utilities

✗ Config-driven form builder for three forms
✓ Three form components
```

Three similar lines of code is better than a premature abstraction. Implement the naive, obviously-correct version first. Optimize only after correctness is proven with tests.

### Rule 0.5: Scope Discipline

Touch only what the task requires.

Do NOT:
- "Clean up" code adjacent to your change
- Refactor imports in files you're not modifying
- Remove comments you don't fully understand
- Add features not in the spec because they "seem useful"
- Modernize syntax in files you're only reading

If you notice something worth improving outside your task scope, note it — don't fix it:

```
NOTICED BUT NOT TOUCHING:
- src/utils/format.ts has an unused import (unrelated to this task)
- The auth middleware could use better error messages (separate task)
→ Want me to create tasks for these?
```

### Rule 1: One Thing at a Time

Each increment changes one logical thing. Don't mix concerns:

**Bad:** One commit that adds a new component, refactors an existing one, and updates the build config.

**Good:** Three separate commits — one for each change.

### Rule 2: Keep It Compilable

Keep each slice coherent and avoid knowingly breaking dependent work. Run build/tests when the changed behavior or task criteria require them; documentation changes do not inherit application checks. If an API/UI/library error occurs, pause its affected flow and plan the specific repair before editing under the current approval boundary.

### Rule 3: Feature Flags for Incomplete Features

If a feature isn't ready for users but you need to merge increments:

```typescript
// Feature flag for work-in-progress
const ENABLE_TASK_SHARING = process.env.FEATURE_TASK_SHARING === 'true';

if (ENABLE_TASK_SHARING) {
  // New sharing UI
}
```

This lets you merge small increments to the main branch without exposing incomplete work.

### Rule 4: Safe Defaults

New code should default to safe, conservative behavior:

```typescript
// Safe: disabled by default, opt-in
export function createTask(data: TaskInput, options?: { notify?: boolean }) {
  const shouldNotify = options?.notify ?? false;
  // ...
}
```

### Rule 5: Rollback-Friendly

Each increment should be independently revertable:

- Additive changes (new files, new functions) are easy to revert
- Modifications to existing code should be minimal and focused
- Database migrations should have corresponding rollback migrations
- Avoid deleting something in one commit and replacing it in the same commit — separate them

## Working with Agents

When directing an agent to implement incrementally:

```
"Let's implement Task 3 from the plan.

Start with just the database schema change and the API endpoint.
Don't touch the UI yet — we'll do that in the next increment.

After implementing, run the authorized checks relevant to the schema
and endpoint, and report the result and unverified limits."
```

Be explicit about what's in scope and what's NOT in scope for each increment.

## Increment Checklist

At a meaningful slice boundary, choose applicable checks using the repository's actual commands. The following is a selection guide, not an all-items gate:

- [ ] The change does one thing and does it completely
- [ ] Relevant behavior/regression checks pass where required
- [ ] Build/type/lint checks cover the changed code where applicable
- [ ] The claimed behavior has supporting evidence; missing runtime evidence remains explicit
- [ ] The handoff includes actual callers and required instructions
- [ ] Git delivery is performed only if authorized; a commit is not an implementation acceptance criterion by default

**Note:** Recheck when relevant code, inputs, environment or findings invalidate the evidence. A stage change or unrelated edit alone does not justify repeating checks. If verification tooling fails, identify a bounded next action; do not build another harness or block unrelated work.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "I'll test it all at the end" | Select checks at meaningful boundaries so defects do not propagate into dependent work. A human-requested untested handoff must retain its evidence limits. |
| "It's faster to do it all at once" | It *feels* faster until something breaks and you can't find which of 500 changed lines caused it. |
| "These changes are too small to commit separately" | Small commits are free. Large commits hide bugs and make rollbacks painful. |
| "I'll add the feature flag later" | If the feature isn't complete, it shouldn't be user-visible. Add the flag now. |
| "This refactor is small enough to include" | Refactors mixed with features make both harder to review and debug. Separate them. |
| "Let me run the build command again just to be sure" | After a successful run, repeating the same command adds nothing unless the code has changed since. Run it again after subsequent edits, not as reassurance. |

## Red Flags

- Expanding dependent implementation while a known relevant failure is unresolved
- Multiple unrelated changes in a single increment
- "Let me just quickly add this too" scope expansion
- Claiming verification without the applicable evidence
- Build or tests broken between increments
- Large uncommitted changes accumulating
- Building abstractions before the third use case demands it
- Touching files outside the task scope "while I'm here"
- Creating new utility files for one-time operations
- Running the same build/test command twice in a row without any intervening code change

## Verification

After completing all increments for a task:

- [ ] Required source/callers are integrated and reviewed
- [ ] Applicable authorized checks support the claimed completion level
- [ ] Required unmet criteria and FAIL/NOT_RUN limits remain visible
- [ ] Runtime behavior and human acceptance are separate from code completion
- [ ] Full-suite/build/Git actions run only when relevant and authorized

## See Also

Use the [Definition of Done](../../references/definition-of-done.md) for the agreed deliverable and completion level. It does not impose every check or a commit on every increment.
