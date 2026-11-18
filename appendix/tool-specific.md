# Tool-specific behavior and verification ledger

**Purpose:** isolate fast-changing tool and standards details from universal guidance. **Last verified per section: 2026-11-15**, by opening the already-cited official links. This verifies what the published pages say, **not installed runtime behavior, account settings, CI branch enforcement, safety of shell access, or live execution of example hooks.** Review before adoption. [Central policy/enforcement limits](../reference/05-practice.md#guidance-vs-enforcement).

## Claude Code instruction loading

**Last verified: 2026-11-15.** [Claude Code - project memory](https://code.claude.com/docs/en/memory).

According to the cited official documentation, **native `AGENTS.md` support requires Claude Code v2.1.277 or later**; particular sessions before v2.1.281 had additional limitations. Project instruction mode `claude-md-or-agents-md` uses qualifying `CLAUDE.md` files preferentially, otherwise supported `AGENTS.md` in scope. The `claude-md-and-agents-md` setting reads both while avoiding duplicated imported content; `claude-md` and managed-only modes have different loading behavior. A local `CLAUDE.local.md` can alter fallback. Scoped/nested files may be loaded on file access rather than at startup. Inspect installed `/config` or context/instruction diagnostics and use [the optional import example](../templates/CLAUDE.md) only if needed. Do not infer that Codex, Copilot, Cursor or Gemini CLI have identical precedence; their behavior was **not independently re-verified** in this V4 revision.

## Claude Code skills and commands

**Last verified: 2026-11-15.** [Claude Code - skills](https://code.claude.com/docs/en/skills); [skill-authoring guidance](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) (the URL currently redirects to a Claude Platform docs page).

In current documentation, legacy `.claude/commands/name.md` is compatible with skills; `.claude/skills/name/SKILL.md` can expose `/name` invocation, and invocation eligibility depends on metadata and configuration. They are not simply “manual commands versus automatic skills.” Metadata, allowed tools, loading and scope are tool-dependent. [Skill example](../templates/.claude/skills/write-adr/SKILL.md); [legacy command example](../templates/.claude/commands/ship.md). No command/skill invocation was tested here.

## Claude Code hooks and permissions

**Last verified: 2026-11-15.** [Claude Code - hooks](https://code.claude.com/docs/en/hooks), [permissions](https://code.claude.com/docs/en/permissions).

Hooks are event- and matcher-scoped; official reference describes `PreToolUse` and blocking a matching tool call on exit code 2. Settings/allow/ask/deny paths must be tested against the actual version and command shape. The [hook config](../templates/hook-config.json) attaches [protect-paths.py](../templates/.claude/hooks/protect-paths.py) to Edit/Write. It does not cover shell and other tool writes, all path escape forms, Git tracking versus *database-applied* migration status, or host security boundaries. New untracked migrations and tracked migrations receive different illustrative treatment; independently protect already applied migrations via authorized CI/human review and actual migration state. The `Read(./.env.*)` pattern in V2 was too broad because it may match `.env.example`; the [settings sample](../templates/.claude/settings.json) enumerates particular secret filenames. Its JSON syntax is not proof of policy enforcement.

## Standards and platform ledger

**Last verified: 2026-11-15.** Only sources already cited in V3 are used below. URLs were opened and the named pages returned readable content in this revision.

| Claim, from V3 | Existing official source | Verification status |
| --- | --- | --- |
| Native Claude `AGENTS.md` support, mode and version | [Project memory](https://code.claude.com/docs/en/memory) | Official page opened; **v2.1.277 appears on page**; local tool not tested |
| Skills and legacy command compatibility | [Skills](https://code.claude.com/docs/en/skills) | Official page opened; not invoked |
| `Read`/Bash permission patterns and limits | [Permissions](https://code.claude.com/docs/en/permissions) | Official page opened; example rules not applied |
| PreToolUse hooks/exit code 2 | [Hooks](https://code.claude.com/docs/en/hooks) | Official page opened; hook not executed here |
| CODEOWNERS ownership and required-review branch settings | [GitHub code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) | Official page opened; repository rules not checked |
| Default copyright for unlicensed repositories | [GitHub licensing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) | Official guidance opened; no legal case review |
| WCAG 2.2 AA 24 px target with exceptions; AAA enhanced 44 px | [W3C AA 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) and [W3C AAA 2.5.5](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced) | Official explanations opened; no UI audited |

**A1:** V3's “Playwright 1.5” example was not independently substantiated as a correct modern version. V4 removes the numeric pin from the **illustrative** [testing template](../templates/docs/testing.md) and instructs adopters to use the project lockfile; no replacement version claim was invented.

**A2:** `.claude/settings.json` indentation was reformatted only ([template](../templates/.claude/settings.json)). **A3:** Claude v2.1.277 claim retained **only here**, with dated source. **A4:** Seven existing verification-ledger source entries resolved through the official pages; they were not treated as tested installations.

**Not performed:** verification of actual TaskFlow source/scripts, package runtime versions, GitHub Actions tags, MCP server schemas/permissions, test infrastructure, local Claude installation, deployment commands or platform-specific hook behavior. Any such example is an untested illustration. Tool loading may change; revalidate before adopting.
