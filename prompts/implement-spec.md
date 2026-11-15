# Implement Spec

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Implement docs/specs/{{SPEC_FILE}}.
First read AGENTS.md and the spec. Then produce a plan: files to change, tests to
write, order of steps, and risks. Wait for my approval.
After approval: work in small steps, write or update tests alongside the code,
run {{CHECK_CMD}} at appropriate verification points (not blindly after every
trivial step), and stop if something in the spec is
ambiguous or wrong instead of guessing. At the end, tick only acceptance
criteria supported by evidence, list unverified ones with reasons and propose the changelog
entry. Do not change anything outside approved scope without asking. Classify R2/R3
changes before implementation; prepare a rollback plan and completion evidence.
