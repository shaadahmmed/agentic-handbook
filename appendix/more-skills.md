# Other optional skills and why you might want them

[Return to five starter skills](../reference/07-tooling.md#five-useful-starter-skills). These are **ideas from V3**, not required tools or permission grants. Confirm runtime behavior before packaging one.

| Candidate | Add only when the repository needs | Main workflow |
| --- | --- | --- |
| `implement-from-spec` | Approved detailed specs | Implement incrementally and report acceptance evidence |
| `changelog-entry` | Manual changelog management | Draft a user-visible entry |
| `docs-sync` | Frequent behavior/config changes | Identify affected docs and propose edits |
| `security-review` | Sensitive paths and frequent security reviews | Report weaknesses against real policy |
| `refactor-safely` | Complex behavior-preserving redesigns | Characterization tests and incremental refactor |
| `debug-failing-ci` | Expensive CI failures | Diagnose environment vs code, propose smallest repair |
| `dependency-upgrade` | Routine package maintenance | Review lockfile, upstream change, licensing and regressions |
| `add-endpoint` | HTTP API | Contract, auth, validation, tests |
| `db-migration` | Databases with controlled migrations | Expand/migrate/contract and recovery checks |
| `add-ui-component` | Shared component system | Tokens, states, keyboard/focus behavior |
| `a11y-audit` | UI accessibility requirements | WCAG-relevant keyboard/contrast/semantics checks |
| `performance-check` | Measured performance budgets | Compare before/after under controlled load |
| `release-checklist` | Versioned releases | Prepare non-production artifacts, stop for approval |
| `incident-postmortem` | Operated services | Blameless timeline and follow-ups from authorized records |
| `onboarding-tour` | New contributors | Trace core modules, setup and first task |
| `data-validation` | Data and ML systems | Schemas, missing data, leakage, reproducibility |
| `terraform-plan-review` | Infrastructure-as-code | Read-only drift/destructive-change report; never apply |

Document-generation formats (Word, slides, spreadsheets, PDFs) can use an installed supported capability when that is a deliverable; keep Markdown as source where practical. Review any externally sourced skill like third-party code: read scripts and referenced files, assess provenance, pin reviewed versions, and deny extra privileges by default. Skill name, frontmatter, loading and invocation details are **tool-specific** ([dated appendix](tool-specific.md)).

## Skill authoring details preserved from V3

1. Use names that identify a real task, and descriptions that say **when** a skill applies; names/metadata format depend on the chosen tool.
2. Disclose large supporting context progressively: short playbook first, deeper references/scripts only when needed. Any fixed 500-line skill size is a heuristic, not a standard.
3. Make steps testable and match instruction strictness to risk; run deterministic validations through reviewed scripts instead of relying on prose.
4. Keep terms consistent, remove stale time-relative claims, and review third-party skills/scripts before adoption.
5. Treat skill and command invocation as tool-specific; see the [verification ledger](tool-specific.md).
