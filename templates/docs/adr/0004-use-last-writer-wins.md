# 0004. Use last writer wins for sync conflicts

Status: Accepted (2026-08-12)

## Context

Two devices can edit the same task while offline. We need a deterministic merge.
We considered CRDTs, operational transforms and last writer wins (LWW).

## Decision

Use LWW per field, using a hybrid logical clock for ordering.

## Consequences

- Relatively simple conflict policy; implementation and testing still need robust clock handling, retry/idempotency and tie-break rules.
- Concurrent edits to the same field lose one change. Acceptable for task
  titles and statuses; revisit for rich text notes (see ADR 0007).
- Rejected for this fictional example: CRDTs. They may provide stronger merge properties, at additional design/integration cost. Confirm this tradeoff for a real project.
