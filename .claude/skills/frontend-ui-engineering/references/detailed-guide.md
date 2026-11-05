# Frontend UI Engineering: detailed techniques

Read the section that resolves the current technical question. The [skill entrypoint](../SKILL.md) sets scope and completion; examples here do not select a stack, authorize side effects or add delivery gates. Preserve the project's actual security and release requirements.

## Contents

- [Component Architecture](#component-architecture)
- [State Management](#state-management)
- [Design System Adherence](#design-system-adherence)
- [Accessibility](#accessibility)
- [Responsive Design](#responsive-design)
- [Loading and Transitions](#loading-and-transitions)
- [See Also](#see-also)
- [UI tradeoffs](#ui-tradeoffs)
- [Relevant warning signs](#relevant-warning-signs)
- [Verification](#verification)

## Component Architecture

### File Structure

Follow the project's component layout. When a new component needs its own files, colocation can keep them understandable; this example does not require adding tests, stories or hooks that the task does not need:

```
src/components/
  TaskList/
    TaskList.tsx          # Component implementation
    TaskList.test.tsx     # Tests
    TaskList.stories.tsx  # Storybook stories (if using)
    use-task-list.ts      # Custom hook (if complex state)
    types.ts              # Component-specific types (if needed)
```

### Component Patterns

**Prefer composition over configuration:**

```tsx
// Good: Composable
<Card>
  <CardHeader>
    <CardTitle>Tasks</CardTitle>
  </CardHeader>
  <CardBody>
    <TaskList tasks={tasks} />
  </CardBody>
</Card>

// Avoid: Over-configured
<Card
  title="Tasks"
  headerVariant="large"
  bodyPadding="md"
  content={<TaskList tasks={tasks} />}
/>
```

**Keep components focused:**

```tsx
// Good: Does one thing
export function TaskItem({ task, onToggle, onDelete }: TaskItemProps) {
  return (
    <li className="flex items-center gap-3 p-3">
      <Checkbox checked={task.done} onChange={() => onToggle(task.id)} />
      <span className={task.done ? 'line-through text-muted' : ''}>{task.title}</span>
      <Button variant="ghost" size="sm" aria-label={`Delete ${task.title}`} onClick={() => onDelete(task.id)}>
        <TrashIcon />
      </Button>
    </li>
  );
}
```

**Separate data fetching from presentation:**

```tsx
// Container: handles data
export function TaskListContainer() {
  const { tasks, isLoading, error, refetch } = useTasks();

  if (isLoading) return <TaskListSkeleton />;
  if (error) return <ErrorState message="Failed to load tasks" retry={refetch} />;
  if (tasks.length === 0) return <EmptyState message="No tasks yet" />;

  return <TaskList tasks={tasks} />;
}

// Presentation: handles rendering
export function TaskList({ tasks }: { tasks: Task[] }) {
  return (
    <ul role="list" className="divide-y">
      {tasks.map(task => <TaskItem key={task.id} task={task} />)}
    </ul>
  );
}
```

## State Management

**Choose the simplest approach that works:**

```
Local state (useState)           → Component-specific UI state
Lifted state                     → Shared between 2-3 sibling components
Context                          → Theme, auth, locale (read-heavy, write-rare)
URL state (searchParams)         → Filters, pagination, shareable UI state
Server state (React Query, SWR)  → Remote data with caching
Global store (Zustand, Redux)    → Complex client state shared app-wide
```

Use explicit props while ownership and dependencies remain clear. Tree depth alone does not require context or restructuring. Extract context or change composition only when a concrete coupling/state problem obstructs the approved change and the repair fits its scope; do not refactor an otherwise clear component tree for an unrelated label or layout edit.

## Design System Adherence

### Approved-template application

If the human approved an internal or user-supplied template for implementation, preserve its agreed structure, hierarchy, navigation/action order, controls, interactions and responsive behavior. Use the identified template source/version and approved differences. For broad or resumed work, retain that information and relevant prototype cleanup in the existing checkpoint; a local fix does not need a new record. Follow the [template application reference](../../../references/template-application.md) and [shared acceptance checklist](../../../../docs/template-application-acceptance.md). Apply the external-reference guidance below only to external designs used as inspiration; it must not change the approved template contract.

Present an ASCII text mockup for discussion and approval before coding, including small UI tasks. Complete all approved UI files and real controller/data wiring before writing/updating and running tests and rendered verification. Compare rendered desktop and mobile results with the template at matching viewports, including primary interactions and applicable populated, empty, loading, error and permission states. Check each required control's visibility and focus/reachability inside its own container; page-level no-overflow does not prove that a nested button is visible. Record evidence and missing prerequisites as PASS/FAIL/NOT_RUN. Resolve uncertain design choices in the planning preview before approved implementation. Material solution changes require amended approval. Check usable flows under normal review/acceptance without a Coordinator gate per screen or edit.

### External reference-led UI quality

When the task introduces a visual direction that existing designs do not resolve, use relevant supplied or authorized references to answer the open question:

1. Prefer references supplied by the product team or its established design system; search only for the unresolved question.
2. Examine enough relevant evidence to choose hierarchy, density and interactions. There is no required screen count.
3. State material choices briefly in the existing task or conversation when they need agreement. Do not create a design document for a routine style repair.
4. Implement the chosen structure with the product's own components, tokens and content. Respect the rights and authorized use of external material.

For external designs used as inspiration, use references as evidence, not as approved templates. If external references are unavailable, document the assumptions and verify the result against the product's existing design system.

### Avoid the AI Aesthetic

Generic defaults can conflict with a project's visual direction. Evaluate the examples below against that direction; a deliberately approved gradient, palette or card layout is not a defect merely because it appears here:

| AI Default | Why It Is a Problem | Production Quality |
|---|---|---|
| Purple/indigo everything | Models default to visually "safe" palettes, making every app look identical | Use the project's actual color palette |
| Excessive gradients | Gradients add visual noise and clash with most design systems | Flat or subtle gradients matching the design system |
| Rounded everything (rounded-2xl) | Maximum rounding signals "friendly" but ignores the hierarchy of corner radii in real designs | Consistent border-radius from the design system |
| Generic hero sections | Template-driven layout with no connection to the actual content or user need | Content-first layouts |
| Lorem ipsum-style copy | Placeholder text hides layout problems that real content reveals (length, wrapping, overflow) | Realistic placeholder content |
| Oversized padding everywhere | Equal generous padding destroys visual hierarchy and wastes screen space | Consistent spacing scale |
| Stock card grids | Uniform grids are a layout shortcut that ignores information priority and scanning patterns | Purpose-driven layouts |
| Shadow-heavy design | Layered shadows add depth that competes with content and slows rendering on low-end devices | Subtle or no shadows unless the design system specifies |

### Spacing and Layout

Reuse the project's spacing scale. Introduce a new value only when the actual layout needs it and it fits the design; this example illustrates consistency, not a universal numeric rule:

```css
/* Use the scale: 0.25rem increments (or whatever the project uses) */
/* Good */  padding: 1rem;      /* 16px */
/* Good */  gap: 0.75rem;       /* 12px */
/* Bad */   padding: 13px;      /* Not on any scale */
/* Bad */   margin-top: 2.3rem; /* Not on any scale */
```

### Typography

Respect the type hierarchy:

```
h1 → Page title (one per page)
h2 → Section title
h3 → Subsection title
body → Default text
small → Secondary/helper text
```

Don't skip heading levels. Don't use heading styles for non-heading content.

### Color

- Use semantic color tokens: `text-primary`, `bg-surface`, `border-default` — not raw hex values
- Ensure sufficient contrast (4.5:1 for normal text, 3:1 for large text)
- Don't rely solely on color to convey information (use icons, text, or patterns too)

## Accessibility

Preserve the accessibility criteria applicable to the changed UI, including the project's required WCAG target. These examples cover common affected controls; a local edit does not require auditing every component:

### Keyboard Navigation

```tsx
// Every interactive element must be keyboard accessible
<button onClick={handleClick}>Click me</button>        // ✓ Focusable by default
<div onClick={handleClick}>Click me</div>               // ✗ Not focusable
<div role="button" tabIndex={0} onClick={handleClick}    // ✓ But prefer <button>
     onKeyDown={e => {
       if (e.key === 'Enter') handleClick();
       if (e.key === ' ') e.preventDefault();
     }}
     onKeyUp={e => {
       if (e.key === ' ') handleClick();
     }}>
  Click me
</div>
```

### ARIA Labels

```tsx
// Label interactive elements that lack visible text
<button aria-label="Close dialog"><XIcon /></button>

// Label form inputs
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// Or use aria-label when no visible label exists
<input aria-label="Search tasks" type="search" />
```

### Focus Management

```tsx
// Illustrative initial focus only; use the project's complete modal primitive.
// It must also handle trapping, dismissal and focus restoration.
function Dialog({ isOpen, onClose }: DialogProps) {
  const closeRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (isOpen) closeRef.current?.focus();
  }, [isOpen]);

  // The open attribute alone does not implement modal focus trapping.
  return (
    <dialog open={isOpen}>
      <button ref={closeRef} onClick={onClose}>Close</button>
      {/* dialog content */}
    </dialog>
  );
}
```

### Meaningful Empty and Error States

```tsx
// Don't show blank screens
function TaskList({ tasks }: { tasks: Task[] }) {
  if (tasks.length === 0) {
    return (
      <div role="status" className="text-center py-12">
        <TasksEmptyIcon className="mx-auto h-12 w-12 text-muted" />
        <h3 className="mt-2 text-sm font-medium">No tasks</h3>
        <p className="mt-1 text-sm text-muted">Get started by creating a new task.</p>
        <Button className="mt-4" onClick={onCreateTask}>Create Task</Button>
      </div>
    );
  }

  return <ul role="list">...</ul>;
}
```

## Responsive Design

Use the project's supported responsive strategy. For a mobile-first layout, for example:

```tsx
// Tailwind: mobile-first responsive
<div className="
  grid grid-cols-1      /* Mobile: single column */
  sm:grid-cols-2        /* Small: 2 columns */
  lg:grid-cols-3        /* Large: 3 columns */
  gap-4
">
```

Select viewport checks from the project-supported layouts and the changed behavior. Check affected breakpoint boundaries or representative widths where the layout can fail; reuse valid evidence for untouched layouts. There is no fixed four-viewport matrix for every UI edit. Approved-template tasks retain their matched desktop/mobile fidelity criteria at usable-flow milestones.

## Loading and Transitions

```tsx
// Skeleton loading is one option when it matches the content and design.
function TaskListSkeleton() {
  return (
    <div className="space-y-3" aria-busy="true" aria-label="Loading tasks">
      {Array.from({ length: 3 }).map((_, i) => (
        <div key={i} className="h-12 bg-muted animate-pulse rounded" />
      ))}
    </div>
  );
}

// Optimistic updates for perceived speed
function useToggleTask() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: toggleTask,
    onMutate: async (taskId) => {
      await queryClient.cancelQueries({ queryKey: ['tasks'] });
      const previous = queryClient.getQueryData(['tasks']);

      queryClient.setQueryData(['tasks'], (old: Task[]) =>
        old.map(t => t.id === taskId ? { ...t, done: !t.done } : t)
      );

      return { previous };
    },
    onError: (_err, _taskId, context) => {
      queryClient.setQueryData(['tasks'], context?.previous);
    },
  });
}
```

## See Also

For detailed accessibility requirements and testing tools, see `../../../references/accessibility-checklist.md`.

## UI tradeoffs

Reuse the supported design system and accessible controls. Address the affected responsive and interaction requirements while building the change. Do not add animations, redesign a working tree or replace state management merely to make a local edit look more ambitious.

## Relevant warning signs

- The approved change is obstructed by mixed responsibilities or unclear state ownership; extract only the cohesive part needed to resolve it.
- A changed control loses its accessible name, keyboard access or visible focus.
- An affected state or supported viewport hides a required action or its feedback.
- New styling contradicts the approved template or design system.
- A rendered claim relies only on source or build output.

Use these signals to select checks on the changed UI; they do not create a full-site cleanup task.

## Verification

Select checks for the changed UI and its supported requirements; reuse valid evidence for unaffected components:

- [ ] For an approved-template task, matched desktop/mobile evidence and applicable criteria support the claimed fidelity; missing required proof remains NOT_RUN
- [ ] The changed UI renders without new attributable console errors; relevant existing failures and their impact remain explicit
- [ ] Changed interactive controls retain keyboard access and focus behavior
- [ ] Changed content/state can be understood with the relevant accessibility tools
- [ ] Affected supported layouts and breakpoint behavior have representative rendered evidence
- [ ] Applicable loading, empty, error, success and permission behavior affected by the change is checked
- [ ] Changed UI follows the project's design system
- [ ] Relevant rendered/interaction evidence supports the completed flow at normal review/acceptance milestones
- [ ] New or worsened accessibility findings are assessed and repaired within scope; pre-existing findings are recorded separately

Do not require a warning-free entire page/site or new axe tooling for every local edit. A pre-existing issue that prevents the agreed flow or violates an actual required criterion still needs an explicit defect/owner; calling it baseline does not establish a pass.
