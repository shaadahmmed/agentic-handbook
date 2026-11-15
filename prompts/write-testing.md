# Write Testing

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write docs/testing.md by inspecting the test setup, config files and a sample
of existing tests.
[PROJECT BRIEF] [COMMON RULES]

Sections: strategy (test types actually present and their rough share);
tools with versions; commands table (goal, command, approximate duration;
measure durations only if safe to run, otherwise [VERIFY]); where tests live
and naming conventions observed; test data and fixtures approach; mocking
rules observed; determinism rules (time, randomness, ids); coverage settings
found in config; CI behavior found in workflow files; flaky test policy as a
proposal marked [CONFIRM]; rules for agents.

The rules for agents section must include: link the repository testing-integrity policy
to get a green result; do not update snapshots without reading the diff; write
a failing test first for bug fixes; run the narrow tests while iterating and
the full check before finishing; say so when a check cannot run instead of
claiming it passed.
Constraints: describe the real setup. Put improvements in a separate
"Suggested improvements" list, not in the main text.
