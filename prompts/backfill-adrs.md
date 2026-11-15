# Backfill Adrs

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Find the 5 most significant architectural decisions already embodied in this
repository (examples: framework, database, auth approach, state management,
monorepo tooling, API style). Use code, config, dependency files, git history
and existing docs as evidence.

For each, write docs/adr/NNNN-title.md with: Status (Accepted), Context,
Decision, Consequences, Alternatives considered.
Rules:
- Where history or docs do not say why a decision was made, write
  "Rationale unknown: [CONFIRM with maintainers]" instead of inventing one.
- Do not fabricate alternatives that nobody considered. If none are recorded,
  say "Not recorded".
- Keep each ADR focused (60 lines is an advisory target). Number them in order starting at 0001, and
  make 0001 "Record architecture decisions".
Also create docs/adr/README.md with a table of all records and their status.
