# Spec 0012: Sync conflict handling

Status: Approved. Owner: Sam. Date: 2026-11-08.

## Problem
Two devices editing the same task offline need deterministic resolution; LWW can still discard one concurrent same-field value.

## Goal
Concurrent edits to different fields of one task are both retained, while same-field conflicts follow the documented LWW policy.

## Non-goals
Rich text merging. Real time collaboration.

## Behavior
1. Each field carries a version stamp from a hybrid logical clock.
2. On sync, the newest stamp wins per field.
3. The losing value is stored in `task_history` for 30 days.

## Acceptance criteria
- [ ] Edit title on device A and status on device B: after sync, both changes remain.
- [ ] Edit the same field on both: the later edit wins and the other is in history.
- [ ] Existing sync tests still pass.

## Affected areas
`apps/api/src/services/sync.ts`, `packages/shared/src/task.ts`, migration for `task_history`.

## Open questions
- Should the user be told when their edit lost? (Decide before UI work.)
