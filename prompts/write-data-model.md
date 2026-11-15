# Write Data Model

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write docs/data-model.md from the schema or migrations. Include: a Mermaid
entity relationship diagram of the main tables; for each table its purpose, key
columns, constraints and notable indexes; data retention and personal data
locations you can identify; migration rules found in the repo (and these
defaults if none exist, marked as proposals: never edit applied migrations,
make changes backward compatible, add before remove).
Do not paste full column lists. Link to the schema file instead.
