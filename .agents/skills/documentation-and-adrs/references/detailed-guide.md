# Documentation and ADRs: detailed techniques

Read the section that resolves the current technical question. The [skill entrypoint](../SKILL.md) sets scope and completion; examples here do not select a stack, authorize side effects or add delivery gates. Preserve the project's actual security and release requirements.

## Contents

- [Architecture Decision Records (ADRs)](#architecture-decision-records-adrs)
- [Inline Documentation](#inline-documentation)
- [API Documentation](#api-documentation)
- [README Structure](#readme-structure)
- [Changelog Maintenance](#changelog-maintenance)
- [Documentation for Agents](#documentation-for-agents)
- [Documentation choices](#documentation-choices)
- [Relevant warning signs](#relevant-warning-signs)
- [Verification](#verification)

## Architecture Decision Records (ADRs)

ADRs preserve the rationale for significant technical decisions when a durable decision record is useful or required by the project.

### When to Write an ADR

Use an ADR when the choice is significant, costly to reverse or governed by the project's decision-record convention. Possible subjects include:

- Choosing a framework, library, or major dependency
- Designing a data model or database schema
- Selecting an authentication strategy
- Deciding on an API architecture (REST vs. GraphQL vs. tRPC)
- Choosing between build tools, hosting platforms, or infrastructure
- Any decision that would be expensive to reverse

### Match the existing convention first

Before creating an ADR, inspect the available repository context for an established convention — existing ADRs, project instructions, and ADR-related configuration or tooling (e.g. an `.adr-dir` file). An established convention overrides the defaults below. Match:

- **Location and format** — e.g. `docs/adr/*.md`, `Documentation/Decisions/*.rst`, a MADR layout, or an `adr-tools` setup. Match the existing directory, file extension, and markup (Markdown vs reStructuredText).
- **Numbering and naming** — continue the existing sequence and filename pattern (`ADR-004-Title.rst`, `0004-title.md`, …); don't restart at 001 or introduce a second scheme.
- **Section headings** — reuse the project's heading set rather than imposing this template's.

If the available evidence conflicts, surface the conflict rather than silently introducing another scheme. Only when no convention can be established do you apply the default below.

### ADR Template

If an ADR is needed and no convention exists, `docs/decisions/` with sequential numbering is one simple option. The following is a fictional decision illustrating the format; its technology comparisons are assumptions for that example, not current product recommendations:

```markdown
# ADR-001: Use PostgreSQL for primary database

## Status
Proposed | Accepted | Superseded by ADR-XXX | Deprecated

## Date
2025-01-15

## Context
We need a primary database for the task management application. Key requirements:
- Relational data model (users, tasks, teams with relationships)
- ACID transactions for task state changes
- Support for full-text search on task content
- Managed hosting available (for small team, limited ops capacity)

## Decision
Use PostgreSQL with Prisma ORM.

## Alternatives Considered

### MongoDB
- Pros: Flexible schema, easy to start with
- Cons: Our data is inherently relational; would need to manage relationships manually
- Rejected: Relational data in a document store leads to complex joins or data duplication

### SQLite
- Pros: Zero configuration, embedded, fast for reads
- Cons: Limited concurrent write support, no managed hosting for production
- Rejected: Not suitable for multi-user web application in production

### MySQL
- Pros: Mature, widely supported
- Cons: PostgreSQL has better JSON support, full-text search, and ecosystem tooling
- Rejected: PostgreSQL is the better fit for our feature requirements

## Consequences
- Prisma provides type-safe database access and migration management
- We can use PostgreSQL's full-text search instead of adding Elasticsearch
- Team needs PostgreSQL knowledge (standard skill, low risk)
- Hosting on managed service (Supabase, Neon, or RDS)
```

### ADR Lifecycle

```
PROPOSED → ACCEPTED → (SUPERSEDED or DEPRECATED)
```

- **Don't delete old ADRs.** They capture historical context.
- When a recorded decision changes materially, follow the project's supersession convention and link the replacement. Routine implementation details do not each need a new ADR.

## Inline Documentation

### When to Comment

Comment the *why*, not the *what*:

```typescript
// BAD: Restates the code
// Increment counter by 1
counter += 1;

// GOOD: Explains non-obvious intent
// Keep the count and its fixed-window start together so a stale count
// is not carried into the next window.
if (now - windowStart > WINDOW_SIZE_MS) {
  counter = 0;
  windowStart = now;
}
```

### When NOT to Comment

```typescript
// Don't comment self-explanatory code
function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// Record actionable follow-up when it is outside the current scope.
// Do not create a TODO instead of implementing required behavior.

// Remove obsolete commented-out code when it is part of the change;
// a local documentation edit is not a repository-wide cleanup task.
```

### Document Known Gotchas

```typescript
/**
 * IMPORTANT: This function must be called before the first render.
 * If called after hydration, it causes a flash of unstyled content
 * because the theme context isn't available during SSR.
 *
 * See ADR-003 for the full design rationale.
 */
export function initializeTheme(theme: Theme): void {
  // ...
}
```

## API Documentation

For changed public APIs (REST, GraphQL or library interfaces), update the relevant existing contract documentation. Select the format the project already uses:

### Inline with Types (Preferred for TypeScript)

```typescript
/**
 * Creates a new task.
 *
 * @param input - Task creation data (title required, description optional)
 * @returns The created task with server-generated ID and timestamps
 * @throws {ValidationError} If title is empty or exceeds 200 characters
 * @throws {AuthenticationError} If the user is not authenticated
 *
 * @example
 * const task = await createTask({ title: 'Buy groceries' });
 * console.log(task.id); // "task_abc123"
 */
export async function createTask(input: CreateTaskInput): Promise<Task> {
  // ...
}
```

### OpenAPI / Swagger for REST APIs

```yaml
paths:
  /api/tasks:
    post:
      summary: Create a task
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTaskInput'
      responses:
        '201':
          description: Task created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
        '422':
          description: Validation error
```

## README Structure

When the task requires a new README or changes setup/usage, include the sections needed by its reader. This example does not require creating missing sections for an unrelated edit; substitute the project's actual commands:

```markdown
# Project Name

One-paragraph description of what this project does.

## Quick Start
1. Clone the repo
2. Install dependencies: `npm install`
3. Set up environment: `cp .env.example .env`
4. Run the dev server: `npm run dev`

## Commands
| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm test` | Run tests |
| `npm run build` | Production build |
| `npm run lint` | Run linter |

## Architecture
Brief overview of the project structure and key design decisions.
Link to ADRs for details.

## Contributing
How to contribute, coding standards, PR process.
```

## Changelog Maintenance

If the project maintains a changelog and this task changes a release entry, follow its convention. For example:

```markdown
# Changelog

## [1.2.0] - 2025-01-20
### Added
- Task sharing: users can share tasks with team members (#123)
- Email notifications for task assignments (#124)

### Fixed
- Duplicate tasks appearing when rapidly clicking create button (#125)

### Changed
- Task list now loads 50 items per page (was 20) for better UX (#126)
```

## Documentation for Agents

Update only the agent-facing information affected by the task; do not create every document type below:

- **CLAUDE.md / rules files** — Document project conventions so agents follow them
- **Spec files** — Keep specs updated so agents build the right thing
- **ADRs** — Help agents understand why past decisions were made (prevents re-deciding)
- **Inline gotchas** — Prevent agents from falling into known traps

## Documentation choices

Code can establish what an implementation does; a short rationale can preserve constraints that are otherwise invisible. Add that rationale where a future reader needs it. Avoid repeated summaries, speculative promises and new records whose only purpose is satisfying a template.

## Relevant warning signs

- A significant new decision lacks the rationale needed to maintain it.
- Changed contract or setup instructions disagree with the implementation.
- A document invents acceptance, approval or runtime evidence.
- An explanation repeats syntax but omits the non-obvious constraint.
- Multiple records present conflicting versions of the same current decision.

Existing documentation debt outside the agreed change remains separate work.

## Verification

Check documentation affected by this task, in the project's existing locations:

- [ ] A significant architectural decision made or changed by this task has its rationale recorded; use an ADR when that is the applicable convention
- [ ] Setup/commands/architecture instructions are updated if this task changes them
- [ ] Changed public API contracts have the relevant parameter, result and error documentation/types
- [ ] Gotchas introduced or encountered in the affected flow are recorded where useful
- [ ] Project rules are updated only if this task intentionally changes an agent-facing convention

Do not backfill historical ADRs, rewrite unrelated API documentation or clean commented-out code across the repository to close a local documentation task. Existing documentation debt stays separate unless it blocks the agreed outcome or is explicitly included in scope.
