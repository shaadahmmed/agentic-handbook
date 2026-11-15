# Audit Docs Consistency

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Read README.md, AGENTS.md, CLAUDE.md, CONTRIBUTING.md, SECURITY.md and every
file in docs/. Do not edit anything.

Report, in tables with file and line references:
1. Contradictions (two files giving different answers: commands, versions,
   paths, rules).
2. Duplicated facts that should live in one place, with a proposed owner file.
3. Links to files or headings that do not exist.
4. Commands or paths mentioned that do not exist in the repository.
5. Terms used inconsistently compared with docs/glossary.md.
6. Rules written as advice that could be enforced by a tool (lint rule, test,
   hook, CI check), with the suggested mechanism.
End with the 5 highest value fixes in priority order.
