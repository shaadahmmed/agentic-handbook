# Part 8 · Rollout and tiered checklists

Pick a tier by **data/operation risk and review needs**, not project size or number of stars. The [START-HERE guide](../START-HERE.md) and [CHEATSHEET](../CHEATSHEET.md) cover immediate adoption. Testing integrity, evidence reporting and risk tiers have single authoritative homes: [testing](03-docs-folder.md#testing-integrity), [evidence](05-practice.md#evidence-based-completion) and [autonomy](05-practice.md#risk-based-agent-autonomy).

## Small and solo

- [ ] README explains purpose, owner/distribution choice, reproducible quick start and relevant commands.
- [ ] Minimal [AGENTS.md](../templates/AGENTS.min.md) or verified supported equivalent names allowed scope and existing scripts.
- [ ] Local secret files are excluded from commits; safe `.env.example` if needed; no real credentials in examples.
- [ ] A meaningful test/check command exists, with clear failure evidence and limits.
- [ ] One task/issue records goal, scope and acceptance; updates remain reviewable.

Optional: one-page spec for ambiguous work; no mandatory MCP, subagent, CODEOWNERS, CLAUDE shim or elaborate design system.

## Growing team

Everything applicable from small tier, plus:

- [ ] CONTRIBUTING and PR template set review expectations, acceptance evidence and rollback questions.
- [ ] SECURITY has an approved private reporting channel and contributor threat guidance.
- [ ] Architecture overview, decisive ADRs, testing strategy, setup and docs index exist as warranted.
- [ ] Relevant lint/type/tests/security scans run in CI; repository rules actually require the checks/reviews intended to gate merges.
- [ ] Teams confirm code ownership and review policy, and can reproduce the review/handoff process.
- [ ] Contracts, migration handling, data/PII handling, version and dependency process are documented where used.

## Production high-impact operations

Everything applicable from the earlier tiers, plus:

- [ ] Environments, credentials, network/storage boundaries and production approvals are independently enforced.
- [ ] Backups/restore and migration recovery are rehearsed with approved, non-production data.
- [ ] Runbooks, on-call escalation, alerting, roll-forward/rollback and incident learning are owned and reviewed.
- [ ] Auth/security/privacy/compatibility changes have independent review and required tests, with documented release criteria.
- [ ] Agents and optional tools are evaluated against representative, repeatable tasks before increasing autonomy.
- [ ] Any MCP integration, subagent, hook or third-party skill receives security review and minimally necessary access.

## Rollout sequence

1. Confirm repo rights, supported development environment and safe agent access; choose a documented risk tier.
2. Make the **smallest** setup runnable and verifiable: README + a canonical check command + agent entry point where supported.
3. Add architecture/spec/ADR context only when the work needs it; introduce CI and human review as collaboration grows.
4. Add runbooks and protected environment policy **before** live operations; make risk approval evidence explicit.
5. Periodically audit docs against reality and measure whether agent instructions improve success, risk, review effort and latency.

Do not infer a universal “2 hours / day 1 / week 1” timetable from the illustrative V3 rollout schedule. The order is advice, not a promise. The handbook’s checklists are adoption aids rather than a declaration of tool policy or production readiness.
