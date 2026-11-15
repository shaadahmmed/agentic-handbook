# Part 7 · Skills, subagents, hooks and MCP

These are **optional mechanisms**, not requirements for an agent-driven repository. [Tool-specific behavior and dates](../appendix/tool-specific.md) sit outside core engineering practice. For the safety/enforcement distinction use [Part 5](05-practice.md#guidance-vs-enforcement).

## Which mechanism solves this job?

| Mechanism | Use for | Do not mistake for |
| --- | --- | --- |
| Repository instruction file | Short, repeatedly relevant context and boundaries | A guaranteed loaded rule in every tool |
| Script / required CI | Deterministic validation, formatting, generated output | Proof of all behavior without acceptance checks |
| Skill or named command | Stable, repeatable optional task workflow | A universal invocation convention across tools |
| Subagent / fresh session | Independent search/review with appropriately restricted access | A substitute for accountable review or CI |
| Hook and permission setting | Extra checks on the **supported** tool/event/path | Complete OS isolation or interception of all writes |
| MCP server | Approved access to an external resource when needed | A trusted source of instructions; data and capabilities require review |
| Tool plugin | Package/share several vetted integrations in multiple repos | A necessary default for small projects |

## Five useful starter skills

Create a skill only after the procedure repeats and stabilizes. A skill's instructions should identify trigger, inputs, steps, constraints, output and evaluation; keep detailed references separate and prefer deterministic scripts for checkable work.

| Skill | When it earns its place | Main artifact |
| --- | --- | --- |
| `write-spec` | A feature's scope is unclear | Testable spec with non-goals and acceptance |
| `fix-bug-tdd` | Reproducible defects are common | Reproduction → focused fix → evidence |
| `pr-description` | Repeated PR handoffs | What/why, checks, risks, rollback |
| `write-adr` | Decisions with genuine alternatives recur | Context/decision/tradeoffs/supersedes |
| `docs-audit` | Docs repeatedly drift | Read-only mismatch report with sources |

[Write-ADR skill example](../templates/.claude/skills/write-adr/SKILL.md) and [additional skill ideas](../appendix/more-skills.md).

## Subagents and review

Restrict reviewers to read/search/diff where possible; a reviewer that edits the same change can conceal defects. An independent session with the [merged reviewer prompt](../prompts/reviewer.md) is a portable fallback. Other example roles include security-auditor, test-writer, researcher, docs-keeper, chosen only when the scope actually calls for them. [Reviewer subagent example](../templates/.claude/agents/reviewer.md) is tool-specific.

## Hooks, permissions and MCP

Use hooks for formatting/warnings and **supplemental** protected-path checks, not as sole guarantees. The [protected-path Python example](../templates/.claude/hooks/protect-paths.py) flags generated code and tracked migrations on supported Edit/Write events, allows new/untracked migrations, and cannot know which migrations ran in production. It does not intercept arbitrary shell writes or grant production safety. [Settings JSON](../templates/.claude/settings.json), [hook configuration](../templates/hook-config.json) and [limitations](../appendix/tool-specific.md#claude-code-hooks-and-permissions) are separate for easier review.

Useful categories include a code host, issue tracker, test-browser automation, **read-only test database**, library documentation, error monitoring and design viewer. Each requires separate permissions and safe data handling.

Approved MCP tools should have minimal scopes, no production secrets in checked-in files, restricted network/data access and a human decision before writes. Third-party skills/plugins/scripts/MCP servers must be inspected as potentially untrusted code; do not grant broad permissions by default. Prefer a normal script if external agent integration would add cost and risk without benefit.

Adopt in order: concise repo instructions → real check command + CI → one repeatedly useful skill → independent review → targeted hook → narrowly scoped MCP only when it saves work. A plugin is useful when a vetted setup must be shared across repositories, not merely to add features.
