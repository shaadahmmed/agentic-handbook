# Part 1 · Foundations

**Audience:** people and coding agents working from solo repositories to production systems. Use the minimum documentation appropriate to risk, not every file in this handbook. For a practical entry point, see [START-HERE](../START-HERE.md).

## Five foundations

1. **Bounded active context; variable persistence.** Agents may use durable memory, retrieval or summaries, but neither completeness nor automatic loading is guaranteed. Keep critical repository facts discoverable and check them against code.
2. **Load only what the task needs.** Repository instruction files are short indexes; architecture, testing and playbooks are read on demand. Whether instruction files are loaded/inherited varies by tool, version and scope ([tool appendix](../appendix/tool-specific.md)).
3. **One fact, one authoritative home.** A command may be repeated briefly as an entry point if it comes from the same script; avoid competing descriptions. Use linked decision records and code-owned configuration.
4. **Concrete beats aspirational.** Give exact, repository-confirmed commands, files, consequences and acceptance criteria. Explain prohibitions so exceptions can be evaluated.
5. **Documentation is reviewed software.** Update docs with changing behavior; use tests and independent merge controls for checkable policy. Guidance is not enforcement ([central distinction](05-practice.md#guidance-vs-enforcement)).

## Which mechanism or document?

| Need | Authoritative destination | Starting point |
| --- | --- | --- |
| What the project does; quick start | `README.md`, `docs/setup.md` | [Root files](02-root-files.md) |
| Agent workspace commands/boundaries | Supported agent instruction file, linked scripts | [AGENTS example](../templates/AGENTS.min.md) |
| Design/architecture decisions | `docs/architecture.md`, `docs/adr/` | [Docs folder](03-docs-folder.md) |
| Acceptance and scope | Issue, task contract, `docs/specs/` | [Task contract](05-practice.md#task-execution-contract) |
| Test policy | `docs/testing.md` | [Testing integrity](03-docs-folder.md#testing-integrity) |
| Risk, autonomy, verification evidence | Reviewed task/PR + independently enforced controls | [Practice](05-practice.md) |
| Reusable prompt or procedure | [Prompts](../prompts/README.md), optional skills/scripts | [Tooling](07-tooling.md) |
| Production release and response | Authorized deployment/runbook system | [Additional docs](04-additional-docs.md) |

## Adoption menu, not a mandate

**Early if applicable:** working README, an actual verification command, concise supported agent instructions, `.gitignore`/safe example configuration if needed, plus an explicit rights/distribution decision. **With contributors/users:** CONTRIBUTING, SECURITY, architecture overview, specs/ADRs for consequential changes, CI and review controls. **For high-impact production:** supported runbooks, migration recovery, access controls, observability and approvals. See [tiered rollout](08-rollout.md).

A repository may also use a docs index, glossary, API contract, data model, roadmap, design tokens, support policy, dependency notices, troubleshooting and machine-readable setup. Add an artifact when its expected value exceeds ownership and maintenance cost. `LICENSE` is particularly important when distributing: no license generally means no general permission granted to outsiders, but authors retain rights; ownership and employment contracts matter. See [additional docs](04-additional-docs.md#license-and-rights).

## Repository shape

Keep root files discoverable; put deep technical descriptions under `docs/` and optional automations under the selected agent tool's configuration directory. The [illustrative complete repository tree](../appendix/repository-layout.md) shows copyable pieces; not every project needs `.claude/`, CODEOWNERS, subagents, MCP, or one ADR per trivial decision. Nested instructions are not universally “closest file wins”: confirm loading and precedence on your installed tool.
