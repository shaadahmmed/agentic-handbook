# Write Agents

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write AGENTS.md for {{PROJECT_NAME}}, a rulebook for coding agents.
[PROJECT BRIEF] [COMMON RULES]

Include, in this order:
1. Project snapshot (2 to 3 lines).
2. Commands: install, dev, lint, typecheck, test all, test one, build,
   codegen if any, and the single full check command.
3. Project map: 5 to 10 lines on where code lives (verify each path exists).
4. Conventions that tools do NOT enforce: {{CONVENTIONS}}. Skip anything a
   linter or formatter already enforces; say which command fixes it instead.
5. Boundaries in three tiers: Always, Ask first, Never. Use {{HARD_RULES}} and
   {{SENSITIVE_PATHS}}. Typical Ask first items: new dependencies, schema
   changes, public API changes, auth changes, deleting files.
6. Definition of done (checks pass, tests added, docs updated, changelog entry).
7. Gotchas: non-obvious traps you found in the repo (slow tests, generated
   folders, required services).
8. Read-before-you-start pointers: one line per doc in docs/ with a trigger
   ("Read docs/testing.md before changing tests"). Only link files that exist.

Constraints: prefer concise, testable rules (150 lines is a heuristic). Every line should have a purpose. If a
line would not change an agent's behavior, omit it. No generic advice.
After the file, list lines you are least sure about so I can review them.
