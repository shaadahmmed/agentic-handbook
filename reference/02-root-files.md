# Part 2 · Core root files

The examples below are **copyable files**, not fenced documents hidden in prose. Choose the template that matches your project and edit placeholders before adoption. The shared caveats are in [Guidance vs enforcement](05-practice.md#guidance-vs-enforcement).

## README.md - project front door

Readers should learn *what it does, why it matters and how to run it*. Include status, supported prerequisites/versions, installation, safe configuration, a verified quick start, the relevant docs and license. Keep architecture essays, sprint notes, release history and agent-only process in their own homes. Success is an independently reproducible onboarding flow, not an arbitrary ten-minute promise.

**Example:** [TaskFlow README](../templates/PROJECT-README.md) (fictional stack and commands). Run its steps only against the real project after review.

## AGENTS.md - short, tool-supported entry point

Use it for project summary, canonical install/check/single-test commands, module map, coding conventions not enforced elsewhere, explicit boundaries, and triggered links to deeper docs. It should not duplicate CONTRIBUTING or contain secrets or generic “write clean code” slogans. Agents may support different instruction filenames and inheritance, so [confirm loading](../appendix/tool-specific.md).

Choose [minimal ~25-line AGENTS.md](../templates/AGENTS.min.md) first; expand to [full TaskFlow AGENTS.md](../templates/AGENTS.full.md) only where recurring defects justify it. The real project must supply its commands and testing rules; link its `docs/testing.md` rather than independently restating the testing-integrity policy.

**When to grow:** add an exact prohibition with its reason after a repeatable mistake; trim it when enforcement replaces prose. Code or generated artifacts should remain the ultimate source of truth. A file-count threshold to trigger planning is a heuristic, not a risk assessment.

## CLAUDE.md / tool-specific instruction files

Optional. A short compatibility file can import the shared AGENTS rules or document a supported tool-specific workflow. Do not maintain two contradictory copies. Claude Code native `AGENTS.md` support, instruction modes, scope and versions are dated in the [tool appendix](../appendix/tool-specific.md#claude-code-instruction-loading). Example: [CLAUDE.md](../templates/CLAUDE.md).

Supported `.claude/` settings may restrict certain tool operations, but cannot guarantee system-level isolation. See [settings](../templates/.claude/settings.json) and [limits](05-practice.md#guidance-vs-enforcement); verify in your deployment before trusting any permission pattern.

## SECURITY.md - reporting and contribution boundaries

For outsiders: supported versions, **private** reporting contact, scope, realistic response timelines, disclosure expectations and a carefully reviewed good-faith research statement. For insiders: secret handling, authorization, input validation, redaction, privacy, dependency scrutiny and prompt-injection handling. Never publish details of unpatched vulnerabilities or copy real credentials into docs. Policies and legal text require owner/qualified review.

**Example:** [SECURITY.md](../templates/SECURITY.md). For concrete mitigations, prefer least-privilege access, isolation, tests, required CI, and branch/deployment policy rather than text alone. [Tool enforcement limits](05-practice.md#guidance-vs-enforcement).

## CONTRIBUTING.md - human review agreement

Describe setup link, issue selection, branch/commit convention, review process, quality bar, AI-assisted contribution accountability, and licensing expectations. Human authors should understand their diff, resolve comments and account for tests and risks. Keep changes focused; **400 changed lines** may be a discussion trigger, never a universal cap. Agents do not receive merge, force-push or deployment rights from this guide.

**Example:** [CONTRIBUTING.md](../templates/CONTRIBUTING.md) and [PR template](../templates/PULL_REQUEST_TEMPLATE.md). Templates prompt evidence; they do not technically enforce truthful answers.

## CHANGELOG.md - user-visible changes

Keep notable release changes, a current Unreleased section where the team uses one, compatible version links, migration notes and human-readable categories (Added, Changed, Deprecated, Removed, Fixed, Security). Do not paste raw commit history or invent release dates/CVE references. Automate generation only if humans review the result.

**Example:** [CHANGELOG.md](../templates/CHANGELOG.md). Release standards and versioning policies are team choices; apply SemVer only when it fits the published API contract.

## Other short root files

- **LICENSE:** full chosen license text, not an AI-authored summary; see [rights](04-additional-docs.md#license-and-rights).
- **CODE_OF_CONDUCT.md:** behavior and reporting process; choose/reproduce a real policy and contact. [Example pointer](../templates/CODE_OF_CONDUCT.md).
- **SUPPORT.md:** route questions and non-security bugs to the right channel; security findings to SECURITY.md.
- **CODEOWNERS:** lists ownership/review requests; merge approval requires applicable enforced branch rules. [Source of this caveat](05-practice.md#guidance-vs-enforcement).
