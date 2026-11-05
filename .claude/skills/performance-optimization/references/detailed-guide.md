# Performance Optimization: detailed techniques

Read the section that resolves the current technical question. The [skill entrypoint](../SKILL.md) sets scope and completion; examples here do not select a stack, authorize side effects or add delivery gates. Preserve the project's actual security and release requirements.

## Contents

- [Core Web Vitals Targets](#core-web-vitals-targets)
- [The Optimization Workflow](#the-optimization-workflow)
- [See Also](#see-also)
- [Measurement choices](#measurement-choices)
- [Relevant warning signs](#relevant-warning-signs)
- [Verification](#verification)

## Core Web Vitals Targets

Use the project's agreed metrics and acceptance. These reference thresholds illustrate web performance assessment; they are not gates for unrelated backend work or a requirement to install field monitoring. Verify version-sensitive external targets when the task depends on them.

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | ≤ 4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | ≤ 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | ≤ 0.25 | > 0.25 |

## The Optimization Workflow

```
1. MEASURE  → Establish baseline with real data
2. IDENTIFY → Find the actual bottleneck (not assumed)
3. FIX      → Address the specific bottleneck
4. VERIFY   → Measure again; keep or revert
5. GUARD    → Reuse an appropriate regression check within scope
```

### Step 1: Measure

Choose evidence for the performance claim using available authorized tools:

- **Controlled measurement (for example, an existing profiler, query plan or benchmark):** Compare the affected operation before/after under representative repeatable conditions. This can verify a local improvement within those conditions.
- **RUM (real user monitoring, such as existing web-vitals or CrUX data):** Use available field evidence to assess actual user impact. Without it, do not claim a measured real-user improvement; a locally verified fix can still be handed off.

Both are useful when available, but a local optimization does not require installing RUM, adding a CI platform or waiting for a field-data window. A project-defined field acceptance criterion remains open until its evidence exists.

**Frontend:**
```bash
# Synthetic: Lighthouse in Chrome DevTools (or CI)
# Chrome DevTools → Performance tab → Record
# Chrome DevTools MCP → Performance trace

# RUM: Web Vitals library in code
import { onLCP, onINP, onCLS } from 'web-vitals';

onLCP(console.log);
onINP(console.log);
onCLS(console.log);
```

**Backend:**
```bash
# Response time logging
# Application Performance Monitoring (APM)
# Database query logging with timing

# Simple timing
console.time('db-query');
const result = await db.query(...);
console.timeEnd('db-query');
```

### Where to Start Measuring

Use the symptom to select the first observation, then follow the evidence:

| Symptom | First useful observation |
| --- | --- |
| Slow first load | Inspect bundle size and the network waterfall for connection setup, server wait and blocking resources. |
| Sluggish interaction | Profile main-thread work, renders or layout/reflow activity. |
| Slow navigation | Compare data-loading time, fetch waterfalls and component rendering. |
| One slow endpoint | Inspect its query timing and relevant plan. |
| Widespread backend latency | Inspect connection wait, resource saturation and shared dependencies. |
| Intermittent slowness | Look for contention, pauses or dependency variation during the affected operation. |

These observations select a hypothesis; they do not authorize deployment, configuration changes or production experiments.

### Step 2: Identify the Bottleneck

Common bottlenecks by category:

**Frontend:**

| Symptom | Likely Cause | Investigation |
|---------|-------------|---------------|
| Slow LCP | Large images, render-blocking resources, slow server | Check network waterfall, image sizes |
| High CLS | Images without dimensions, late-loading content, font shifts | Check layout shift attribution |
| Poor INP | Heavy JavaScript on main thread, large DOM updates | Check long tasks in Performance trace |
| Slow initial load | Large bundle, many network requests | Check bundle size, code splitting |

**Backend:**

| Symptom | Likely Cause | Investigation |
|---------|-------------|---------------|
| Slow API responses | N+1 queries, missing indexes, unoptimized queries | Check database query log |
| Memory growth | Leaked references, unbounded caches, large payloads | Heap snapshot analysis |
| CPU spikes | Synchronous heavy computation, regex backtracking | CPU profiling |
| High latency | Missing caching, redundant computation, network hops | Trace requests through the stack |

### Step 3: Fix the Bottleneck

Change the supported bottleneck and necessary callers. Keep independent optimization ideas outside the current experiment unless their interaction is part of the hypothesis. The anti-patterns below are the usual suspects; each entry gives the rule and the signature to recognize it, and links to a worked fix in [optimization-patterns.md](optimization-patterns.md). Open the one you need when you reach that code, not before.

**Backend**

- **N+1 queries.** One query per row is the most common backend bottleneck. Fetch the relation in the same query (join/include) instead of in the loop. [Pattern](optimization-patterns.md#n1-queries-backend).
- **Unbounded data fetching.** For the affected growing collection, use appropriate bounds and stable ordering while preserving its consumer contract. [Pattern](optimization-patterns.md#unbounded-data-fetching).
- **Queries that ignore their index.** "Add an index" is the guess; `EXPLAIN ANALYZE` is the measurement. A `Seq Scan` where you expected an index, a `rows=` estimate off by an order of magnitude, and a `Sort` node above the scan each call for a different fix; a poor `rows=` estimate can indicate stale statistics or another estimation problem, so inspect the cause before choosing an index or a maintenance action. Data/production operations require their actual authority. Index for the shape of the query (equality columns first, then the range or sort column). A plain index will not help a query on a low-selectivity dominant value (a partial index serves the rare value), a leading wildcard (needs trigram or full-text), or a function applied to the column (index the expression, as in `WHERE lower(email) = ?`), and every index taxes every write. Compare the relevant plan and measured behavior afterwards; retain an index only when its benefit and write/storage cost justify it for the agreed workload. [Pattern](optimization-patterns.md#queries-that-ignore-their-index).
- **Connection pool exhaustion.** Signature: *every* endpoint slows at once, time is spent waiting for a connection rather than executing, and the database shows mostly idle sessions. One pool per process, sized so `instances × max` stays under the database's connection ceiling. Bigger is not faster; it relocates the queue to the database where it is harder to see. With unbounded instance counts (serverless, autoscaling), multiplex through a proxy (pgbouncer, RDS Proxy) instead of raising `max`. [Pattern](optimization-patterns.md#connection-pool-exhaustion).
- **Missing caching.** Cache what is expensive to produce and read far more often than it changes; caching an already-fast query adds a network hop and a staleness bug in exchange for nothing. Pick the layer deliberately (in-process, shared, CDN). Every input that changes the response belongs in the key (tenant, locale, permissions, feature flags): a key that omits the viewer is how one user's data gets served to another. Choose one invalidation strategy (TTL, event or tag based, versioned keys) and state the acceptable staleness window explicitly. Guard hot keys against the stampede: serve stale while one request recomputes, or coalesce concurrent misses behind a single in-flight promise. Never cache what must be fresh (balances, permissions, inventory at checkout). [Pattern](optimization-patterns.md#missing-caching-backend); request coalescing, write strategies, and negative caching in `../../../references/performance-checklist.md`.

**Frontend**

- **Missing image optimization.** For images implicated by the profile, reserve appropriate layout space, size sources for the supported display and consider priority or lazy loading according to where they appear. Do not lazy-load the measured LCP image or rewrite every image to match the example. [Pattern](optimization-patterns.md#missing-image-optimization-frontend).
- **Unnecessary re-renders.** An object or function created in render is a new reference every time and re-renders every child that receives it. Hoist constants; reserve `React.memo` and `useMemo` for work the profile shows is expensive, since overuse is its own cost. [Pattern](optimization-patterns.md#unnecessary-re-renders-react).
- **Large bundle size.** Modern bundlers tree-shake ESM named imports on their own; the real gains are route-level code splitting and lazy-loading heavy, rarely-used features behind `Suspense`. Profile before changing import styles. [Pattern](optimization-patterns.md#large-bundle-size).

### Step 4: Verify (Keep or Revert)

A fix is a hypothesis until you re-measure. This step decides whether it survives.

**Re-measure the way you measured the baseline:** same command, same conditions, same fixed budget (wall-clock, sample count, or request count). A baseline taken on a cold cache against a result taken on a warm one measures the cache, not your change.

**Keep attribution clear.** Isolate changes when practical. When related changes must be measured together, report the combined effect and its attribution limit instead of claiming each part has an independently measured gain.

**Consider noise, not just the mean.** Repeat when another comparable observation can resolve the decision, and compare the delta with run-to-run variance. A 3% difference inside ±5% variance does not establish a gain. If further runs stop adding useful evidence, report an inconclusive result and its limits rather than benchmarking indefinitely.

Decide for the experiment's stated purpose:

| Result vs. baseline | Action |
|---|---|
| Past the threshold, tests green | **Keep.** Record before/after numbers in the existing task or handoff. Commit only when separately authorized. |
| Within noise (no demonstrated improvement) | Treat as inconclusive. Remove task-owned complexity whose only justification was the unobserved performance gain, or state a separate approved reason to retain it. |
| Worse | Remove or revise the task-owned experiment unless the agreed acceptance explicitly trades this cost for another required result. Preserve other work. |
| Improved, but a check is red or unavailable | **Classify the failure first.** Repair a regression caused by the change within valid scope. For a pre-existing defect or unrelated runner/environment failure, retain the source and measured result with explicit verification limits; follow workflow failure ownership rather than automatically reverting. |

A performance-only change needs a demonstrated benefit worth its complexity. Do not call an unmeasured or inconclusive result a win, and do not use this guidance to undo unrelated work or an independently required correctness change.

A red check alone does not justify undoing a measured fix. Identify whether it reports a business assertion, a product regression or a tooling failure. Recheck only affected evidence and use the [failure-handling guidance](../../../../docs/team-workflow.md#failures-and-blockers) when needed; do not enter a revert/reimplement/full-suite loop. If an experiment is removed, remove only the task-owned change and preserve other work; no Git mutation is authorized by this table.

**Correctness gates the metric.** A performance-verification claim needs a comparable improvement and relevant passing correctness/regression checks. Required failed or unavailable proof keeps that claim open. An "optimization" that wins by dropping work the product needed (skipping a validation, caching something that must be fresh, removing an `await` that was load-bearing) is a regression, not a win.

#### Retain useful experimental evidence

If a non-obvious failed hypothesis is likely to be retried, keep a short note in the existing checkpoint or handoff. Reuse the baseline and measurement limits already recorded; no per-attempt ledger or additional file is required. For example:

| Idea | Baseline → Result | Verdict | Why |
|---|---|---|---|
| Memoize the row component | INP 240ms → 235ms | reverted | Inside noise (±15ms). Rows weren't the bottleneck. |
| Virtualize the list | INP 240ms → 90ms | kept | Long tasks gone from the trace. |
| Preconnect to the API origin | LCP 2.8s → 2.8s | reverted | Already same-origin. |

Use an existing task or PR section when useful. A new session alone is not a reason to repeat an unaffected experiment; repeat only if changed inputs or a concrete uncertainty justify it.

### Step 5: Guard Against Regression

Guard the metric the user actually feels, not every available number. Use the
same LCP, INP, p95 latency, or other primary metric that justified the fix.

Use the existing regression mechanism that fits the measured bottleneck: a focused check, repeatable profiling command or already configured performance budget. Record the command and measurement limits in the same task.

A synthetic CI budget and field monitoring are complementary options when the project already uses them or explicitly includes their setup. Neither is a universal prerequisite for local completion. Do not add a new runner, RUM service or alert pipeline to satisfy this skill. If a required guard is missing, report the affected acceptance/release criterion and owner rather than starting infrastructure work.

When an existing relevant guard fires, diagnose the observed regression using a comparable baseline.

**Example budgets, only when selected for the project's workload and acceptance:**

```
JavaScript bundle: < 200KB gzipped (initial load)
CSS: < 50KB gzipped
Images: < 200KB per image (above the fold)
Fonts: < 100KB total
API response time: < 200ms (p95)
Time to Interactive: < 3.5s on 4G
Lighthouse Performance score: ≥ 90
```

**Examples for an already authorized/configured CI budget; these commands do not authorize installation or a new gate:**
```bash
# Bundle size check
npx bundlesize --config bundlesize.config.json

# Lighthouse CI
npx lhci autorun
```

## See Also

For detailed performance checklists, optimization commands, and anti-pattern reference, see `../../../references/performance-checklist.md`.


## Measurement choices

Use representative conditions and a comparable baseline. Profile the actual query or execution path before choosing indexes, caching or memoization. Keep evidence that distinguishes a useful improvement from variance, and disclose when the available measurement cannot support a real-user claim. Correctness and security remain part of acceptance.

## Relevant warning signs

- A proposed optimization has no observed symptom, applicable requirement or supported bottleneck.
- A changed cache omits tenant/viewer inputs or its invalidation and staleness contract.
- An index or connection-pool adjustment has no evidence explaining the measured problem.
- A comparison changes workload, environment or cache state without acknowledging it.
- A measured "win" comes from dropping required validation, work or correctness coverage.
- Repeated experiments add cost without resolving uncertainty, or unchanged work is restarted after a session boundary.

Select the warning that applies to this task; do not turn a local performance fix into a whole-project audit.

## Verification

For the performance behavior actually changed:

- [ ] A supported bottleneck or required outcome identifies the measurement to compare.
- [ ] Baseline and result use comparable conditions; variance and attribution limits are stated.
- [ ] The claimed improvement is supported rather than inferred from code shape or a noisy sample.
- [ ] Relevant correctness, authorization and data requirements remain satisfied; failed or unavailable proof is explicit.
- [ ] If a cache, query/index, bundle or image path changed, its relevant compatibility and resource tradeoffs were checked.
- [ ] The existing regression guard or reproducible command is available for the next useful check; unrelated monitoring/CI infrastructure was not created.

Finish when the agreed result has sufficient evidence. A remaining field-data requirement stays open without preventing an accurately scoped local handoff. Retain only useful experimental notes in the existing record and do not repeat unaffected checks simply because the stage or session changed.
