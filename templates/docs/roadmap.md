# Roadmap

Last updated: 2026-11-10. Owner: product lead.

## Goal for 2027

Reach a stable 1.0: reliable offline sync, team workspaces, and a documented API.

## Now

| Item | Outcome | Link |
| --- | --- | --- |
| Sync conflict handling | Different-field edits are retained; same-field conflicts follow the documented LWW and history policy | docs/specs/0012-sync-conflicts.md |
| Workspace roles | Owner, editor and viewer roles enforced in the API | docs/specs/0014-roles.md |

## Next

1. Webhook retries and dead letter queue
2. CSV import and export
3. Public API documentation site

## Later (not committed)

- Mobile apps
- Calendar integration
- Rich text task notes (needs a new sync approach, see ADR 0007)

## Non-goals

- Real time collaborative editing. We favor offline-first over live cursors.
- A hosted SaaS offering. TaskFlow stays self-hosted.
- Plugin marketplace.

## Milestone: 1.0

Ready when all of these are true:
- Sync conflict tests pass for the agreed multi-device scenarios, including concurrent same-field edits and recoverable history where specified.
- Every public endpoint is documented in openapi.yaml.
- Security review complete; no open high severity issues.

## Risks

- Role enforcement touches every route; schedule it before the API docs freeze.
