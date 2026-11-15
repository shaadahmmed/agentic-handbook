# Contributing to TaskFlow

Thanks for helping. Please read this before opening a pull request.
Be kind: see CODE_OF_CONDUCT.md.

## Before you start

- Set up your environment with docs/setup.md.
- For anything larger than a small fix, open an issue first and wait for a reply.
- Good first tasks are labeled `good first issue`.

## Branches and commits

Branch names: `feat/<name>`, `fix/<name>`, `docs/<name>`, `chore/<name>`.

Commits follow Conventional Commits:

```text
feat(sync): merge offline edits per field using version stamps
fix(auth): accept plus signs in email addresses
docs: explain webhook retry policy
feat(api)!: remove GET /v1/tasks/all   (breaking change)
```

Imperative mood, subject line under 72 characters, body explains why.

## Pull requests

- One purpose per PR. Prefer a reviewable diff; use 400 changed lines only as an optional team warning threshold, not an automatic rejection.
- Fill in the PR template completely.
- All checks must pass: lint, type check, tests, security scan.
- Add or update tests, docs, and a CHANGELOG.md entry under Unreleased.
- Keep the branch up to date by rebasing on `main`. PRs are squash merged.

## Review

- At least one approval and code-owner approval for `auth/`, `billing/` and
  `migrations/` **only if the repository’s ruleset/branch protection requires it**;
  otherwise treat them as recommended review requests.
- Maintainers aim to respond within 3 business days.
- Address every comment or reply with your reasoning. Do not resolve threads
  you did not write.

## AI assisted contributions

AI tools are welcome. You are responsible for every line you submit. Read the
full diff, run the checks locally, and tick the AI disclosure box in the PR
template. Do not submit code you cannot explain.

## License

By contributing you agree that your work is released under the MIT license.
