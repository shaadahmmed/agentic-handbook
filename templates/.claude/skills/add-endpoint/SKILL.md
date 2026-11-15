---
name: add-endpoint
description: Use when adding or changing an HTTP API route in apps/api.
---

1. Update `openapi.yaml` first with the new route and schemas.
2. Run `pnpm codegen` to regenerate types.
3. Add the route in `apps/api/src/routes/` and logic in `src/services/`.
4. Validate input with the shared zod schema.
5. Write tests: one success case, one validation failure, one auth failure.
6. Add a CHANGELOG.md entry under Unreleased.
