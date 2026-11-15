# Part 4 · Supporting documents when needed

Choose by problem and risk, not a preordained file count. The linked files are independent [copyable examples](../templates/README.md).

## License and rights

An unlicensed public repository is **not** automatically open source. Absent an explicit license, default copyright generally reserves reproduction, modification and distribution rights to copyright owners; the authors retain rights to their work, subject to employment, contract, joint ownership, exceptions and platform terms. Resolve ownership/distribution before inviting contributions. MIT/Apache-2.0/GPL-3.0 involve materially different terms; use the **full legal text** of an appropriate license. An SPDX identifier or a package allowlist is helpful metadata/screening, not legal clearance. Seek qualified advice when ownership or compatibility is uncertain. [Source already in V3](../appendix/tool-specific.md#standards-and-platform-ledger).

## Compact document cards

| File | What it owns | Example |
| --- | --- | --- |
| `CODE_OF_CONDUCT.md` | Contributor behavior, coverage, real enforcement channel; adopt full named policy | [sample pointer](../templates/CODE_OF_CONDUCT.md) |
| `SUPPORT.md` | Non-security support/bug channels, expectations; link to private SECURITY reporting | Not mandatory for small private projects |
| `CHANGELOG.md` | Released user-visible changes and migration notes; don't reproduce git logs | [sample](../templates/CHANGELOG.md) |
| `docs/README.md` | An index of document owners and read triggers | [sample](../templates/docs/README.md) |

## Setup and safe configuration

`docs/setup.md`: OS/tool prerequisites, pinned versions based on the repo, dependency startup, one-step reproducible commands, success criteria and troubleshooting. `docs/configuration.md`: variable purpose, constraints, defaults and where source config is defined. `.env.example`: **fake** safe placeholders with each documented variable; never real secrets. In `.gitignore`, protect local `.env*` without hiding safe templates (`!.env.example`, optionally `!.env.*.example`). Ignore rules restrict tracking/search in some tools but do not prevent all reads or subprocess access.

Examples: [setup guide](../templates/docs/setup.md), [safe `.env.example`](../templates/.env.example), [ignore patterns](../templates/env.gitignore.example).

## Specifications, glossary and contracts

`docs/specs/` contains observable problem, goal, non-goals, behavior, acceptance, affected areas, owner and unresolved questions. A spec is not permission for production changes. [Example per-field LWW spec](../templates/docs/specs/0012-sync-conflicts.md) explicitly retains different-field edits and documents handling of competing same-field edits; proposed history needs actual verification. `docs/glossary.md` defines domain vocabulary once (e.g., Workspace, Member, Task). `docs/data-model.md` describes schema owners, important constraints, migration safety and retention—not every column. `docs/api.md` or `openapi.yaml` owns requests, responses, auth, errors, pagination and compatibility; prefer a machine-readable contract as canonical when possible ([example API error](../templates/api-error.json)).

## Operating software

`docs/deployment.md` and runbooks describe real environments, ownership, approvals, safe release and rollback paths, migration ordering, backup restoration and alerts. Agents can draft release instructions but must not improvise production operations. [Illustrative runbook entry](../templates/docs/runbook-entry.md) contains a rollback command **that must not be executed without verifying the target and authorization**. `docs/troubleshooting.md` uses symptom → root cause → verified fix. `docs/performance.md` records targets and how measured; don't invent numbers or treat them as universal. Third-party notices and a dependency policy become important when license distribution terms or supply-chain risk require them.

## Long tasks and repo hygiene

A plan under `docs/plans/` records a durable objective, decisions, checked progress, next steps and limitations across agent sessions ([sample](../templates/docs/plans/migrate-sessions-to-redis.md)); archive after completion. `.editorconfig` keeps whitespace consistent. Pull-request and issue templates collect reproducible evidence. CODEOWNERS requests the right reviews; see [enforcement distinction](05-practice.md#guidance-vs-enforcement) and [template](../templates/CODEOWNERS).
