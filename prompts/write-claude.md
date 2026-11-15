# Write Claude

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write CLAUDE.md for {{PROJECT_NAME}}.
[COMMON RULES]

First determine whether the installed tool loads AGENTS.md natively and whether a
CLAUDE.md file would suppress that loading. If a CLAUDE.md is needed, import
AGENTS.md with verified syntax (for Claude Code, `@AGENTS.md`) and report how
loading was checked. Do not rely on an ordinary "read it" sentence as proof.
Then add only tool specific guidance that does not belong in AGENTS.md:
workflow preferences (for example plan before changes touching more than 3
files), which commands, skills and subagents exist in this repo and when to use
them, and compaction guidance (what to keep when context is summarized).

Constraints: keep minimal. CLAUDE.md is optional when native AGENTS.md loading covers your needs; verify the effective instructions. Do not duplicate AGENTS.md. Do not
include personal preferences. If the tool you run in is not Claude Code,
adapt the filename and syntax and tell me what you changed.
