# Write Setup

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write docs/setup.md for a new machine, based on the repository files only.
[PROJECT BRIEF] [COMMON RULES]

Include: supported operating systems (only those evidenced in CI or docs);
requirements table (tool, version, how to check); numbered setup steps with
exact commands; how to start dependencies; how to seed sample data if a seed
script exists; a "verify it works" section with expected results; common
failures with fixes you can derive from config (ports, versions, missing env
variables).
Do not run scripts from untrusted sources or commands that target shared services.
Do not run anything that needs real credentials. List every step you could not
verify under [VERIFY].
