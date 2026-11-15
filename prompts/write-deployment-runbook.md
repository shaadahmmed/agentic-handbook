# Write Deployment Runbook

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write docs/deployment.md from the CI, container and infrastructure files.
Include: environments and how they differ; how a release happens step by
step; migration order; rollback procedure; feature flags if present; required
secrets by name only (never values) and where they are stored; backup and
restore if configured; a runbook with one entry per alert or failure mode you
can find (symptom, first checks, fix, escalation). Where facts are missing,
write [CONFIRM: ...] for me to fill in. Do not invent infrastructure.
