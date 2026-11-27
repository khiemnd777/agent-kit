# Skills catalog

Eighteen optional skills: 17 V1 identities adapted for V2, plus execution-delegation.
Read only the skill that resolves a current need; a catalog is not a startup sequence.

| Skill | Use when |
| --- | --- |
| [api-and-interface-design](../.agents/skills/api-and-interface-design/SKILL.md) | Design changed API/module contracts with real callers, compatible data shapes, meaningful failures and safe replay semantics. |
| [code-review-and-quality](../.agents/skills/code-review-and-quality/SKILL.md) | Review a coherent diff for concrete correctness, contract, security and maintainability defects; distinguish evidence from preference. |
| [code-simplification](../.agents/skills/code-simplification/SKILL.md) | Reduce evidenced duplication, tangled control flow or needless indirection without silently changing behavior. |
| [context-engineering](../.agents/skills/context-engineering/SKILL.md) | Resume from the relevant checkpoint or reduce irrelevant context without resetting approvals, stops or valid evidence. |
| [debugging-and-error-recovery](../.agents/skills/debugging-and-error-recovery/SKILL.md) | Locate and diagnose an evidenced failure, repair its supported cause, and stop when further attempts have no useful basis. |
| [documentation-and-adrs](../.agents/skills/documentation-and-adrs/SKILL.md) | Update a changed contract or usage instruction, or record a significant architecture decision without inventing approval history. |
| [frontend-ui-engineering](../.agents/skills/frontend-ui-engineering/SKILL.md) | Build or repair the approved UI using real data wiring, accessible controls, responsive layout and relevant visual evidence. |
| [incremental-implementation](../.agents/skills/incremental-implementation/SKILL.md) | Deliver coherent approved capabilities through real callers/layers without artificial file-by-file handoffs. |
| [observability-and-instrumentation](../.agents/skills/observability-and-instrumentation/SKILL.md) | Fill a concrete diagnostic gap with bounded signals using the existing telemetry stack. |
| [performance-optimization](../.agents/skills/performance-optimization/SKILL.md) | Measure a concrete bottleneck and verify a scoped optimization against comparable conditions and correctness. |
| [planning-and-task-breakdown](../.agents/skills/planning-and-task-breakdown/SKILL.md) | Resolve real dependencies, scope and acceptance boundaries with the smallest executable approved plan. |
| [security-and-hardening](../.agents/skills/security-and-hardening/SKILL.md) | Protect affected trust, data and authorization boundaries with scoped verification and real runtime controls. |
| [source-driven-development](../.agents/skills/source-driven-development/SKILL.md) | Resolve a concrete version/API/configuration uncertainty from inspected source and relevant official documentation. |
| [spec-driven-development](../.agents/skills/spec-driven-development/SKILL.md) | Resolve material requirement/domain/interface uncertainty without manufacturing a specification hierarchy. |
| [test-driven-development](../.agents/skills/test-driven-development/SKILL.md) | Design meaningful tests after the approved code/wiring scope; preserve the project code-first order rather than imposing red-green cycles. |
| [technote](../.agents/skills/technote/SKILL.md) | Explain a technical result with the smallest useful medium, making observed evidence and limits explicit. |
| [using-agent-skills](../.agents/skills/using-agent-skills/SKILL.md) | Select a focused available skill when its relevance or effective source is unclear; not a startup ritual. |
| [execution-delegation](../.agents/skills/execution-delegation/SKILL.md) | Decide WHEN to hand a complete stable work block to a real external executor, or use direct tools/reasoning instead. |

No skill grants authority or starts an agent. Preserve the actual client's effective
source and permissions. Claude mirrors match canonical bytes; duplicate discovery
must be observed in the real client, not inferred from the mirror count.
