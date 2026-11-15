# Start here · Agentic Coding Documentation Handbook V4

November 15, 2026 · **Based on V2 by @Shaad Ahmmed** · V4 is a docs-only, read-only-source restructuring. Examples are not runtime-tested; [guidance vs enforcement](reference/05-practice.md#guidance-vs-enforcement).

**Scope:** Humans and coding agents working from small repositories to production systems. Adopt only the files, verification and controls justified by risk. This page is self-contained for the first setup; deeper detail lives in [reference](reference/01-foundations.md), [prompts](prompts/README.md) and [templates](templates/README.md).

## The five ideas

1. A model's **active context is limited** even if it has persisted memory; don't assume every instruction auto-loads.
2. Keep its entry-point instructions **short**; link to exact docs and source.
3. **One fact, one home**: derive repeated commands from one executable script.
4. Written permissions, rules and hooks are **not an OS security boundary**; enforce critical actions with independent controls.
5. An agent's summary is not a test result; record **what was actually observed**.

## Three reader tracks

| Reader | Start here | Then use |
| --- | --- | --- |
| **Solo developer** | 25-line agent file below, README and a check command | [small setup checklist](reference/08-rollout.md#small-and-solo); [bug/spec prompts](prompts/README.md) |
| **Team lead** | Clear acceptance, PR evidence, technical conventions | [team checklist](reference/08-rollout.md#growing-team); [task contract](templates/task-contract.md) |
| **Platform/security owner** | Least privilege, sensitive changes and stop conditions | [R0–R3](reference/05-practice.md#risk-based-agent-autonomy), [E0–E5](reference/05-practice.md#evidence-based-completion), [production checklist](reference/08-rollout.md#production-high-impact-operations) |

## 25-line AGENTS.md core (copy and adapt)

Use an instruction filename and loading mechanism verified for your agent. The copyable original is [templates/AGENTS.min.md](templates/AGENTS.min.md).

```markdown
# AGENTS.md
Project: <one-sentence purpose and stack>.
Read README.md for setup and project scope.

## Commands (replace with tested repo commands)
- Install: `<install-command>`
- Check: `<check-command>`
- One test: `<single-test-command>`

## Map
- Source: `<source-directory>`
- Tests: `<test-directory>`
- Generated: `<generated-directory-or-none>`

## Working boundaries
- Work only within the approved task and paths.
- Plan and seek approval before sensitive changes.
- Never edit generated output manually.
- Do not access or reveal secrets.

## Completion
- Follow the project's testing-integrity policy.
- Record checks actually run, outcomes, and limitations.
- Update relevant docs when behavior changes.
- Hand off a diff; do not commit or deploy without approval.
```

## The check command

Prefer a single existing **project-owned** `check` script/task that combines relevant lint, type/build and tests. **Illustrative only:** `pnpm check`; do not run it unless it is present in the real project and its side effects are understood. Report actual command, environment, exit status and unperformed checks ([evidence policy](reference/05-practice.md#evidence-based-completion)).

## Four deny boundaries before granting agent access

1. **Credentials:** no reading, copying, displaying, logging or committing secrets.
2. **Destructive actions:** no mass deletion, force-push or history rewriting without owner approval.
3. **External effects:** no production deploy, incident change, data write or secret rotation by the agent.
4. **Unapproved scope:** no dependency, schema, auth, billing or security-sensitive changes without the review/approval defined by [risk policy](reference/05-practice.md#risk-based-agent-autonomy).

These are **human policies to implement in real controls**, not magic deny-pattern syntax. [Tool settings example](templates/.claude/settings.json) is intentionally narrower; [limits](reference/05-practice.md#guidance-vs-enforcement).

## Tiny PR handoff template

```markdown
## Why and what changed
## Scope and risk classification
## Checks performed (commands, status, environment) and not performed
## Acceptance evidence / limitations
## Rollback and approvals still needed
```

Copy the [full PR template](templates/PULL_REQUEST_TEMPLATE.md) only if it fits your team. Choose your [adoption tier](reference/08-rollout.md), use the [one-page cheat sheet](CHEATSHEET.md) during reviews and leave the agent in plan-only mode when approval is missing.
