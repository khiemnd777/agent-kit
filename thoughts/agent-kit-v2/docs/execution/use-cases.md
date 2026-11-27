# Use-case selection

These recommendations are design decisions for V2, not measured performance.

| Use case | Preferred route | Boundary |
| --- | --- | --- |
| One test/lint/build command | DIRECT | No new runtime needed |
| Existing Makefile/script/CI already covers the job | DIRECT | Reuse it instead of wrapping needlessly |
| Repeated multi-repository inventory | DELEGATE when available | Fixed targets, bounded reads, compact evidence |
| Multi-service verification with real dependencies | DELEGATE when it adds value | Pin snapshots; retain project CI as authority where required |
| Repeatable API health/audit batch | DELEGATE when authorized | Network targets, timeouts, rate limits, privacy |
| Fixed source collection before review | DIRECT or DELEGATE | No automatic claim of semantic code review |
| New architecture/business feature | REASON | Can delegate stable subproblems, not product judgment |
| Unknown defect/root cause | REASON | Reuse diagnostics, but do not force a speculative workflow |
| Production deployment or migration | WAIT until explicit authority; use existing deployment tooling | Sidecar is not an approval bypass |
| Repeating a failed assertion unchanged | Do not repeat | Investigate new evidence |
| Uncertain payment/write after timeout | Reconcile first | Repeatable does not mean idempotent |
| Export all agent history to mine tasks | Out of scope | Separate privacy/authorization decision |

A small script can be better than a Sidecar. A stable workflow may still need
human or LLM judgment at a bounded exception. The purpose is to remove unnecessary
LLM orchestration, not all reasoning or all oversight.
