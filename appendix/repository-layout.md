# Illustrative full repository layout (from V3)

A reference for teams that actually need these documents. This is **not** the minimum setup; unused directories and files should be omitted. Tool-specific files may not load in your tool. See [foundation decisions](../reference/01-foundations.md) and [tiered setup](../reference/08-rollout.md).

```text
project/
  README.md                 what it is, quick start
  AGENTS.md                 rules and commands for any coding agent
  [CLAUDE.md]               optional import or Claude-specific notes when required
  CONTRIBUTING.md           branches, commits, PR and review rules
  SECURITY.md               vulnerability reporting + security rules
  CHANGELOG.md              user facing history per release
  LICENSE                   legal terms
  CODE_OF_CONDUCT.md        behavior standards (open source or teams)
  [SUPPORT.md]              where to ask questions
  .env.example              every environment variable, placeholder values
  .gitignore                keep secrets, builds and local files out
  .editorconfig             indentation and line endings

  .claude/
    settings.json           shared permissions and hooks (committed)
    settings.local.json     personal overrides (git ignored)
    [commands/]             legacy compatible command prompts; skills also expose /names
    [skills/]               reusable playbooks, invoked explicitly or by agent
    [agents/]               subagent definitions (reviewer, test writer)

  .github/
    PULL_REQUEST_TEMPLATE.md
    ISSUE_TEMPLATE/         bug.yml, feature.yml
    CODEOWNERS              required reviewers per path
    workflows/              CI: lint, test, build, security scan

  docs/
    architecture.md         system structure and boundaries
    design.md               UI, tokens, components (or ui.md)
    roadmap.md              now, next, later
    testing.md              strategy, commands, conventions
    setup.md                local environment, step by step
    configuration.md        every setting and variable explained
    glossary.md             domain terms
    data-model.md           schema, relations, migration rules
    api.md                  endpoints and contracts (or openapi.yaml)
    deployment.md           release, rollback, runbook
    troubleshooting.md      known problems and fixes
    adr/
      0001-record-decisions.md
      0002-choose-database.md
    specs/
      0001-user-login.md    one spec per feature or task

  src/                      application code
  tests/                    tests (or beside the code, per your convention)
  scripts/                  helper scripts the docs refer to
```
