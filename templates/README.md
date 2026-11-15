# Copyable TaskFlow examples

**Illustrative; not executed against a TaskFlow repository.** Files here are examples, not universally correct project defaults. Validate referenced commands, paths, tools, security contacts, GitHub identities, migration state and policy before use. Syntax checks of sample JSON/YAML do **not** establish runtime support. The governing limitations are in [Guidance vs enforcement](../reference/05-practice.md#guidance-vs-enforcement).

| Copy this example | Intended repository destination |
| --- | --- |
| `AGENTS.min.md` / `AGENTS.full.md` | `AGENTS.md` (choose **one**) |
| `CLAUDE.md` | `CLAUDE.md` only when supported and needed |
| `.claude/settings.json`, `.claude/hooks/protect-paths.py` | Corresponding `.claude/` paths, after reviewing permissions/hooks |
| `.claude/skills/write-adr/SKILL.md`, `.claude/skills/add-endpoint/SKILL.md`, `.claude/agents/reviewer.md`, `.claude/commands/docs-audit.md` | Matching tool-specific paths if supported |
| `PULL_REQUEST_TEMPLATE.md`, `CODEOWNERS` | `.github/` paths; review requirements must be configured separately |
| `docs-ci.yml` | `.github/workflows/docs.yml` after version/action review |
| `env.gitignore.example` | Adapt into `.gitignore` |
| `package-check-scripts.json` | Merge scripts into an existing `package.json`, do not replace it |
| `api-error.json` | API documentation example, not a standalone project contract |
| `docs/runbook-entry.md` | Append to an authorized runbook; don't execute its sample rollback command |
| `docs/…`, `PROJECT-README.md`, `SECURITY.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.env.example` | Matching project paths after editing the illustrative details |
| `task-contract.md` | A ticket/spec/task template, not an agent permission grant |

TaskFlow uses **per-field last-writer-wins** (LWW) with a proposed optional history mechanism, not lossless conflict-free concurrent editing. These examples illustrate a policy; they do not demonstrate that any implementation exists.

A real `LICENSE` is intentionally **not** templated: choose appropriate full legal terms for the owner and distribution. A code-of-conduct link/example does not replace the full covenant when adopting it.
