# Write Contributing Pr

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write CONTRIBUTING.md and .github/PULL_REQUEST_TEMPLATE.md for {{PROJECT_NAME}}.
[PROJECT BRIEF] [COMMON RULES]

Contributing sections: welcome and scope; setup (link docs/setup.md, do not copy
steps); finding work; branch naming; commit messages (Conventional Commits
unless the repo already uses another style, which you must detect and follow);
pull request rules (one purpose per PR, reviewability target of {{PR_SIZE_LIMIT}} changed
lines (advisory; justify exceptions), tests, docs, changelog entry); review process and merge strategy
(detect from repo settings or history, otherwise [VERIFY]); rules for AI
assisted contributions (human accountable, read the full diff, disclose
significant agent use, never push to main, never bypass checks); license and
conduct links.
PR template: what and why, how tested, risk and rollback, checklist (tests,
docs, changelog, no secrets, AI use disclosed).

Constraints: keep CONTRIBUTING.md concise; 150 lines is an optional target, not an enforced limit.
