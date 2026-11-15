# Prompt library · Part 6

These are reusable instructions, not agent permissions. Combine a [filled project brief](project-brief.md), the **shared eight-line contract** below and exactly one selected prompt. No runtime, tool or repository action is authorized merely by copying a prompt. Follow [risk tiers](../reference/05-practice.md#risk-based-agent-autonomy) and [evidence](../reference/05-practice.md#evidence-based-completion).

## Shared rules

```text
1. Role/objective: act as careful repository engineer; produce only the named artifact.
2. Inputs/context: use the brief, revision, task contract, code and relevant docs.
3. Scope: respect paths/non-goals; no install, publish, deploy, merge or deletion by implication.
4. Constraints: least privilege, no secrets/personal data; prior approval for sensitive work.
5. Acceptance/output: produce requested file/diff and evidence, risks, assumptions, gaps.
6. Sources: cite repository paths and test outputs; do not invent facts/commands/features.
7. Unknowns: mark [VERIFY]; stop and ask if safety, scope or correctness depends on them.
8. Verification: state checks performed and not performed; apply the evidence standard.
```

`[VERIFY]` flags unconfirmed input; `[CONFIRM]` flags owner questions. Text such as `[PROJECT BRIEF]` or `[COMMON RULES]` in legacy prompts means **include the linked brief and rules above**, not that the runtime will automatically load them. Task-specific approval and stop conditions take precedence over this generic preface.

## Find a prompt

- **Bootstrap:** [audit and plan](bootstrap-audit-plan.md) → [create approved phase](bootstrap-create-phase.md).
- **Core files:** [README](write-readme.md), [AGENTS](write-agents.md), [CLAUDE](write-claude.md), [SECURITY](write-security.md), [CHANGELOG](write-changelog.md), [CONTRIBUTING/PR](write-contributing-pr.md).
- **Engineering docs:** [architecture](write-architecture.md), [backfill ADRs](backfill-adrs.md), [evaluate tradeoffs/write ADR](write-adr-tradeoffs.md), [design](write-design.md), [roadmap](write-roadmap.md), [testing](write-testing.md), [setup](write-setup.md), [configuration](write-config.md), [glossary](write-glossary.md), [data model](write-data-model.md), [API](write-api.md), [deployment/runbook](write-deployment-runbook.md), [troubleshooting](write-troubleshooting.md).
- **Work:** [write spec](write-spec.md), [implement approved spec](implement-spec.md), [long-task plan](write-plan.md), [classify risk first](classify-change-risk.md).
- **Review:** [one reviewer with focus](reviewer.md), [docs consistency](audit-docs-consistency.md), [docs vs code](audit-docs-against-code.md), [prune AGENTS](prune-agents.md), [test quick start](test-quickstart.md), [learn from mistake](learn-from-mistake.md), [agent configuration safety](audit-agent-config.md).

## Variable reference

## Project-brief variables

| Placeholder | Meaning | Example |
| --- | --- | --- |
| `{{PROJECT_NAME}}` | Name of the project | TaskFlow |
| `{{ONE_LINE_PURPOSE}}` | What it does and for whom, in one sentence | Self-hosted task manager for small teams |
| `{{PROJECT_TYPE}}` | Web app, API, library, CLI, mobile app, data pipeline, ML system | Web app with REST API |
| `{{STAGE}}` | Idea, prototype, alpha, beta, production | Beta |
| `{{AUDIENCE}}` | Who uses it and who contributes | Small teams; two maintainers |
| `{{LANGUAGES}}` | Languages and runtime versions | TypeScript 5, Node 22 |
| `{{FRAMEWORKS}}` | Main frameworks and libraries | React 19, Express 5 |
| `{{PACKAGE_MANAGER}}` | Dependency tool | pnpm 9 |
| `{{DATA_STORES}}` | Databases, caches, queues | PostgreSQL 16, Redis 7 |
| `{{HOSTING}}` | Where it runs | Docker on a VPS, GitHub Actions for CI |
| `{{REPO_LAYOUT}}` | Single package or monorepo and the main folders | Monorepo: apps/web, apps/api, packages/shared |
| `{{INSTALL_CMD}}`, `{{DEV_CMD}}`, `{{LINT_CMD}}`, `{{TYPECHECK_CMD}}`, `{{TEST_CMD}}`, `{{SINGLE_TEST_CMD}}`, `{{BUILD_CMD}}`, `{{E2E_CMD}}`, `{{CHECK_CMD}}` | Exact commands | `pnpm install`, `pnpm dev`, `pnpm check` |
| `{{CONVENTIONS}}` | Code rules not enforced by tools | Named exports only; errors via `AppError` |
| `{{HARD_RULES}}` | Things that must never happen | Never edit applied migrations |
| `{{SENSITIVE_PATHS}}` | Folders needing extra review | `auth/`, `billing/`, `migrations/` |
| `{{HAS_UI}}`, `{{HAS_API}}`, `{{HAS_DB}}` | Yes or no, to skip irrelevant docs | yes, yes, yes |
| `{{AGENT_TOOLS}}` | Which agent tools you use | Claude Code, Cursor |
| `{{LICENSE}}` | License choice or intent | MIT |
| `{{SECURITY_CONTACT}}` | Where to report vulnerabilities | security@example.com |
| `{{COMPLIANCE}}` | Regulatory needs, if any | none; or GDPR, HIPAA, PCI |
| `{{TEAM_SIZE}}` | People working in the repo | 2 humans, several agents |

## Task-specific variables

| Placeholder | Meaning |
| --- | --- |
| `{{PHASE_NUMBER}}`, `{{PHASE_FILE_LIST}}` | Which phase of the approved plan to create, and its files |
| `{{TODAY}}`, `{{OWNER}}` | Date for "Last reviewed" and the person or team responsible |
| `{{NUMBER_OF_COMMITS}}` | How many recent commits to summarize when there are no tags |
| `{{PR_SIZE_LIMIT}}` | Advisory reviewability target, e.g. 400 changed lines; justify exceptions |
| `{{DECISION_QUESTION}}`, `{{CONSTRAINTS}}`, `{{OPTIONS}}` | Inputs for a new ADR |
| `{{DESIGN_PRINCIPLES}}`, `{{A11Y_TARGET}}` | Inputs for the design doc |
| `{{PLANNING_PERIOD}}`, `{{GOALS}}`, `{{IN_PROGRESS}}`, `{{IDEAS}}`, `{{NON_GOALS}}` | Inputs for the roadmap |
| `{{FEATURE_IDEA}}`, `{{SPEC_FILE}}` | Inputs for writing and implementing a spec |
| `{{TASK_DESCRIPTION}}`, `{{TASK_SLUG}}` | Inputs for a long task plan file |
| `{{BASE_BRANCH}}` | Branch to compare against in a review, usually `main` |
| `{{DESCRIBE_MISTAKE}}` | A plain description of what the agent got wrong |
| `{{CONFIG_FILES}}` | The agent configuration paths to review |
| `{{DESIGN_OR_DIFF}}` | Design artifact, file paths, commit range or proposed patch under review |
| `{{ACCEPTANCE_CRITERIA}}` | Authoritative checklist from approved issue, spec or task contract |

**Additional reviewer variable:** `{{FOCUS}}` is `full`, `design`, `simplicity`, `acceptance`, or `post-implementation`. All other `{{…}}` variables must appear in this legend or a prompt's local definition. Paths and suggested commands are guesses until confirmed in the repository.

## How to adapt by project type

| Situation | Change in the prompts |
| --- | --- |
| Library or SDK | Replace design and deployment docs with public API reference, semantic versioning and deprecation policy, and a compatibility matrix. CHANGELOG becomes critical |
| Command line tool | Add a usage reference (commands, flags, exit codes, examples) and shell completion notes. Skip design.md |
| Monorepo | Root AGENTS.md holds shared rules and how to run commands per package. Add a nested AGENTS.md in each package with local rules. Add a workspace level check command |
| Mobile app | Add build and signing documentation (no secrets), a device and OS test matrix, and store release steps. Keep keystores and certificates out of the repository |
| Data or machine learning project | Add docs for datasets (source, license, privacy), reproducibility (seeds, environment), experiment tracking, evaluation metrics, and model cards. Add rules against committing data and model files |
| Infrastructure as code | Add rules that agents may run plan but never apply to production. Document state storage and environments |
| No UI, no database or no API | Delete the matching docs and prompts rather than leaving empty files |
| Solo or tiny project | Merge CONTRIBUTING into README, skip CODEOWNERS and templates, keep AGENTS.md, testing and setup |
| Legacy code with few tests | In the testing prompt, ask for a plan to add characterization tests around risky areas first, and tell agents to avoid broad refactors until that exists |
| Open source and public | Keep CODE\_OF\_CONDUCT, SUPPORT, SECURITY with a private channel, and issue templates. Review all docs for internal references |
| Private or internal | Replace public reporting with an internal security channel and add an onboarding checklist |
| Regulated (health, finance, payments, children's data) | Add a compliance document describing data classes, retention and audit trails. Require human sign-off steps in AGENTS.md. Have a qualified professional review policy text. This handbook does not provide compliance guidance |

Use a read-only planning pass when access or facts are unclear. Edit one target at a time; request a diff for updates. For the source-to-prompt mapping and why five reviewer prompts became one, see [REVISION-LOG](../REVISION-LOG.md#merged-reviewer-prompt-coverage-p1).
