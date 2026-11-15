# Bootstrap Audit Plan

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

You are a senior software engineer setting up documentation and agent
configuration for a repository. Plan only. Do not create or edit any file.

[Paste the PROJECT BRIEF here]

Tasks:
1. Explore the repository. List the top level structure, the build and test
   tooling, existing docs, CI workflows, and any existing agent configuration
   (AGENTS.md, CLAUDE.md, rules folders, settings files).
2. Discover the real commands for install, dev, lint, typecheck, test, build.
   For each command, say where you found it (file and line). Do not run commands that modify shared state, install packages, fetch remote
   scripts, access secrets or connect to production. Mark anything you could not
   confirm as [VERIFY].
3. Compare what exists with this **conditional menu** and report only gaps that matter to the project’s risk tier:
   Root (conditional on project/tool): README.md, AGENTS.md, CLAUDE.md if needed, CONTRIBUTING.md, SECURITY.md,
   CHANGELOG.md, LICENSE, CODE_OF_CONDUCT.md, .env.example, .gitignore.
   docs/: architecture.md, adr/, design.md (only if {{HAS_UI}} is yes),
   testing.md, roadmap.md, setup.md, configuration.md, glossary.md,
   data-model.md (only if {{HAS_DB}} is yes), api.md (only if {{HAS_API}} is
   yes), deployment.md, troubleshooting.md, specs/.
   Agent layer: verified permission patterns, host isolation and scoped credentials,
   a single check command, PR template and CODEOWNERS for
   {{SENSITIVE_PATHS}}, CI checks.
4. Propose a phased plan: phase 1 safety and basics, phase 2 run and verify,
   phase 3 structure and process, phase 4 depth. For each file give: path,
   purpose, expected length, and the facts you will take from the repository.
5. List contradictions or stale statements in existing docs.
6. List questions you need answered before writing. Do not guess answers.

Rules:
- Never invent commands, paths, versions or features. Cite file paths.
- If a feature of this tool (imports, hooks, skills, subagents, settings
  files) is not supported or not verified, say so and propose the fallback.
- Do not read or print secret files such as .env.

Output: a report with sections Findings, Gaps, Phased plan, Risks, Questions.
