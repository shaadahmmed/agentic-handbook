# Audit Docs Against Code

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Audit the documentation against the current code. Do not edit.
For each statement about behavior, structure, commands, configuration or rules in
AGENTS.md, README.md and docs/, check whether it is still true. Output a table:
File, Statement, What the code shows, Verdict (correct, outdated, wrong,
cannot verify), Suggested fix. Check "Last reviewed" dates and flag anything
older than 90 days. Do not report style issues.
