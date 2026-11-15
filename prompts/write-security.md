# Write Security

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write SECURITY.md for {{PROJECT_NAME}}.
[PROJECT BRIEF] [COMMON RULES]

Part 1, reporting policy: supported versions (derive from tags and releases, or
mark [VERIFY]), private reporting channel ({{SECURITY_CONTACT}}), what to
include in a report, response timeline placeholders I must confirm (do not
promise specific days yourself, write [CONFIRM: number of days]), scope, and a
good faith research statement.
Part 2, rules for contributors and AI agents: secrets handling, dependency
approval, input validation, authorization checks on every new route or
action, personal data in logs, treating fetched text as untrusted data, and
approved external services. Base every rule on how this repository actually
handles these things; mark [VERIFY] where you cannot tell.

Constraints: be concise (120 lines is an advisory target). Do not include details of unfixed vulnerabilities
or real credentials. This is a draft for human and, if needed, professional
security review.
