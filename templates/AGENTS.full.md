# AGENTS.md

TaskFlow is a self-hosted task manager. TypeScript monorepo (pnpm), Node 22,
PostgreSQL 16, React 19. See README.md for the product overview.

## Commands

- Install: `pnpm install`
- Dev server: `pnpm dev` (http://localhost:3000)
- Lint (non-mutating check): `pnpm lint`; run a formatter or `--fix` separately only when deliberately editing
- Type check: `pnpm typecheck`
- All tests: `pnpm test`
- One test file: `pnpm test path/to/file.test.ts`
- Regenerate API client after editing `openapi.yaml`: `pnpm codegen`
- Database migration: `pnpm db:migrate` (local/test environment only; production runs require approval; never rewrite migrations applied to shared environments)

## Project map

- `apps/web/` React frontend
- `apps/api/` Express API (routes in `src/routes/`, logic in `src/services/`)
- `packages/shared/` types and validation schemas used by both apps
- `apps/api/src/generated/` generated code, do not edit by hand

## Conventions

- TypeScript strict mode. No `any`; use `unknown` and narrow it.
- Named exports only. No default exports.
- Validate all external input with the zod schemas in `packages/shared/`.
- Errors: throw `AppError` (see `apps/api/src/errors.ts`), never plain `Error`.
- Tests live next to the code as `*.test.ts`. Write the test first for bug fixes.
- Use `date-fns` for dates. Do not add `moment`.

## Boundaries

Always:
- Run the verified non-mutating checks relevant to the task and report which passed; use `pnpm lint && pnpm typecheck && pnpm test` only if the TaskFlow scripts exist.
- Add or update tests for every behavior change.
- Add a CHANGELOG.md entry under "Unreleased" for user visible changes.

Ask first:
- Adding or upgrading a dependency.
- Changing database schema or any file in `migrations/`.
- Changing public API shapes or auth logic.
- Deleting files or large refactors across many modules.

Never:
- Commit secrets or edit `.env`. Use `.env.example` for new variables.
- Edit `src/generated/` or applied migrations.
- Force push, rewrite history, or push directly to `main`.
- Violate the testing-integrity policy in `docs/testing.md`.

## Gotchas

- `pnpm test` needs a local test database: inspect Compose configuration before running `docker compose up -d db`. Never target shared or production data.
- Integration tests in `apps/api/tests/e2e/` take about 90 seconds. Run them last.

## Read before you start

- Changing structure or adding modules: docs/architecture.md
- Writing or changing tests: docs/testing.md
- UI work: docs/design.md
- Making a design decision: docs/adr/ (add a new record if you decide something)
