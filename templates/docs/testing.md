# Testing

## Strategy

| Level | Share | What it covers | Speed |
| --- | --- | --- | --- |
| Unit | illustrative mix, about 70% | Pure functions, services with fake repositories | milliseconds |
| Integration | illustrative mix, about 25% | API routes against a real test database | under 1 s each |
| End to end | illustrative mix, about 5% | Critical user journeys in a browser | seconds each |

## Tools

Example tools (pin real versions from your lockfile): Vitest (unit, integration), Playwright (end to end), Testcontainers for
the database, `@faker-js/faker` for generated data.

## Commands

| Goal | Command | Time |
| --- | --- | --- |
| All unit and integration | `pnpm test` | about 40 s |
| One file | `pnpm test path/to/file.test.ts` | seconds |
| One test by name | `pnpm test -t "rejects expired token"` | seconds |
| Watch mode | `pnpm test --watch` | n/a |
| Coverage | `pnpm test --coverage` | about 60 s |
| End to end | `pnpm e2e` | about 90 s |

Integration tests need the database: `docker compose up -d db`.

## Conventions

- Test files sit beside the code: `user-service.ts` and `user-service.test.ts`.
- Test names describe behavior: `it("rejects an expired token")`.
- Use the Arrange, Act, Assert layout with a blank line between the parts.
- Build data with factories in `tests/factories/`. Do not copy production data.
- Freeze time with `vi.useFakeTimers()`; never use the real clock or `Math.random()`.
- Mock only network, email and the clock. Use the real database in integration tests.

## Coverage

Illustrative **team-selected** policy: 80% overall line coverage and 95% for `auth/`/`billing/`, with CI warning if coverage drops by one percentage point. These numbers are **not industry standards**; choose thresholds from baseline, risk, code churn and test quality. Coverage does not prove security or meaningful assertions; use branch/behavior tests for critical paths.

## Bug fixes

1. Write a failing test that reproduces the bug.
2. Confirm it fails for the right reason.
3. Fix the code. Confirm the test passes.

## Flaky tests

An intermittently failing test needs investigation. Track it with an issue, isolate it where feasible and assign a risk-appropriate deadline; seven days is an example team policy, not a universal SLA. Limited retries can diagnose environmental noise but must not conceal regressions.

## Rules for agents

- Apply the testing-integrity policy agreed for this repository.
- Resolve snapshots by the repository testing-integrity policy.
- Run `pnpm lint && pnpm typecheck && pnpm test` before saying a task is done.
- Report every check outcome using the approved completion-evidence policy.
