# Classify Change Risk

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Act as the change-risk reviewer. Analyze {{TASK_DESCRIPTION}} against the
repository's actual protected paths, deployment controls and Part 5 R0–R3
framework. Inputs: [PROJECT BRIEF] [COMMON RULES], task boundaries,
{{SENSITIVE_PATHS}} and any proposed commands. Read-only inspection only.
Output: tier with rationale; affected data/users; blast radius; reversibility;
required human approvals; minimal privileges; safe tests; rollback/forward;
stop conditions and unresolved facts. The highest-risk operation determines
the tier. Do not implement, migrate, push or deploy. If evidence is missing,
classify conservatively and stop for approval.
