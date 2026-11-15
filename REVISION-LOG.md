# V3 → V4 Revision Log

> Documentation-only R1 revision. Source is read-only: `../Agentic Coding Documentation Handbook v3.md`. No repository commit/push/merge or application execution.

## 1. Measured V3 baseline (before editing)

Method: GNU `wc -l` and `wc -w` on the original and on each exact Part byte slice. Counts include tables, fenced examples and prompts.

| segment | Words (`wc -w`) | Lines (`wc -l`) |
| --- | ---: | ---: |
| **Entire V3** | **29,561** | **3,088** |
| Preface and navigation | 569 | 37 |
| ## Part 1: Foundations | 1,406 | 114 |
| ## Part 2: Core root files | 4,432 | 574 |
| ## Part 3: The docs folder | 3,216 | 401 |
| ## Part 4: Additional documents | 2,203 | 292 |
| ## Part 5: Agentic coding practice | 6,243 | 424 |
| ## Part 6: AI prompt library | 6,863 | 839 |
| ## Part 7: Skills, subagents, hooks and MCP | 3,456 | 306 |
| ## Part 8: Rollout and checklist | 1,173 | 101 |

### Caveat phrase baseline (case-insensitive substring scan)

| Phrase | matches |
| --- | ---: |
| `illustrative` | 22 |
| `not a security boundary` | 1 |
| `OS-level` | 2 |
| `verify` | 53 |
| `not tested` | 3 |
| `not a universal` | 5 |
| `enforced` | 18 |
| `cannot` | 24 |
| `CODEOWNERS` | 15 |
| `[VERIFY]` | 15 |
| `R0` | 3 |
| `E0` | 2 |

### Repeated normative rule inventory (semantic clusters, not only identical strings)

Semantic repetitions, not necessarily verbatim; source lines refer to V3.

| Rule or caveat repeated | line anchors / locations | Proposed authority |
| --- | --- | --- |
| Never skip/delete/weaken tests to hide failure | 302–314 AGENTS example; 1049–1058; 1119–1125; 2290–2313 prompt; 3031–3080 checklist | `reference/03-docs-folder.md#testing-integrity` |
| Do not represent unrun checks as passed | 1109–1125 testing; 1495–1510 check loop; 1600–1635 contract/evidence; 2033–2060 COMMON RULES; 2586–2616 reviewer prompts; rollout | `reference/05-practice.md#evidence-based-completion` |
| R0–R3 autonomy, approvals and stop conditions | 299–304 AGENTS example; 1450–1555 guardrails; 1557–1573; 1605–1614 contract; 2559–2572; 2992–3080 rollout | `reference/05-practice.md#risk-based-agent-autonomy` |
| Permissions/hooks are not OS security boundary | 9 prefatory labels; 68–81 foundations; 379–441 Claude settings; 1450–1495 layered guardrails; 2857–2938 hooks | `reference/05-practice.md#guidance-vs-enforcement` + tool-specific technical caveats in appendix |
| CODEOWNERS approval only mandatory under enforced branch rules | 474 security; 675 review example; 1356–1374 supporting docs; 1484 guardrail table; 2982 source ledger; 2996–3080 rollout | `reference/05-practice.md#guidance-vs-enforcement`, platform detail in appendix |
| Illustrative examples, not live-tested | 7–9 introduction; 97 layout; 392 settings; 1074–1107 testing; 1856 prompt disclaimer; 2870–2938 hook; 2972 ledger | `reference/05-practice.md#guidance-vs-enforcement` and specific template README only |
| Secret handling, never paste/read/log credentials | 248 AGENTS; 301 boundaries; 379–441 tool config; 449–536 SECURITY; 1701–1714 writing rules; 1850–1868 prompt preface; 3000+ rollout | `reference/05-practice.md#guidance-vs-enforcement`; security source in `reference/02-root-files.md` |
| Do not add dependencies without approval; vet provenance/licenses | 294–298 AGENTS; 454 SECURITY; 1125 licensing; 1423 principles; 1701 doc rules; 3000+ rollout | `reference/05-practice.md#risk-based-agent-autonomy` and `reference/02-root-files.md` security |
| Documentation updates accompany behavior change | 60–81 foundations; 288–294 AGENTS; 544–555 changelog; 1030+ testing; 1715–1738 maintenance; 3000+ rollout | `reference/05-practice.md#maintenance` |
| Scope control: no unapproved edits/deploys/commits | 289–305 AGENTS; 630–640 contributions; 1450–1465 task loop; 1574–1615 contract; 1953–2029 bootstrap; 2368–2382 implementation | `reference/05-practice.md#task-execution-contract` + autonomy |
| Tool loading depends on version/scope; do not assume | 7–9 preface; 68–95 foundations; 341–440 Claude details; 1847–1882 prompt preface; 2682–2712 tools; 2972–2986 sources | `appendix/tool-specific.md`; principle in `reference/01-foundations.md` |
| Numerical thresholds (coverage, size, lengths) contextual | 68–81 foundations; 625–640 contributions; 1029–1125 testing; 1686–1700 writing length; 2992–3080 rollout | `reference/05-practice.md#guidance-vs-enforcement`; local example retains labeled numbers |
| Prompts must cite paths, avoid invention, mark unknowns | 1847–1952; 1953–2616 prompts | `prompts/README.md` shared ~8-line contract |


## 2. Changes and rationale

- **Added:** `START-HERE.md` (three tracks, five ideas, 25-line core, check command, four human deny boundaries, PR handoff); `CHEATSHEET.md` (R0–R3, E0–E5, layers); dated tool appendix, prompt index and per-file templates.
- **Split:** V3 Parts 1–5, 7–8 become the seven files under `reference/`; Part 6 becomes `prompts/` with one workflow per file; full TaskFlow examples, configurations, shell-adjacent descriptions and plans become files under `templates/`. Eight-part sequence retained; Part 6 is now a prompt index.
- **Consolidated:** Enforcement and caveats live in `reference/05-practice.md#guidance-vs-enforcement` (C1). D1 testing integrity has one policy home in `reference/03-docs-folder.md#testing-integrity`; D2 evidence claims in `reference/05-practice.md#evidence-based-completion`; D3 risk tiers and approval/stop conditions in `reference/05-practice.md#risk-based-agent-autonomy`.
- **Condensed:** Boilerplate *why / what goes in / what stays out / example* becomes short purpose-and-link cards, particularly LICENSE, conduct, support and changelog. Numeric heuristics remain contextual. The 18-row engineering-principles table is **three columns**, preserving definition, when/avoid, example, misuse and evaluation in every row. Long per-doc maturity checklists become tiered adoption guidance. Skills are five starter patterns and 17 additional ideas.
- **Retained examples:** TaskFlow LWW architecture/ADR/spec, code and risk guards, docs CI, sample README/SECURITY/CHANGELOG/CONTRIBUTING/PR, runbook, setup, env example, CODEOWNERS, hooks, settings, reviewer and skill examples. A complete optional repo tree and illustrative commands by stack are in the appendix.
- **Accuracy (A1–A4):** Removed unsupported numeric Playwright version from copied testing template (no replacement version asserted); reformatted settings JSON only; kept the versioned Claude loading claim in the dated appendix only; opened the seven already-cited official ledger sources and recorded what was verified versus not tested.

### Deleted repetition, not safety

| passage | Status | Why no safety claim was removed |
| --- | --- | --- |
| Repeated “illustrative”, “not tested”, OS-boundary and CODEOWNERS caveat sentences | Moved to central C1/dated appendix; readers link from affected sections | Limitations preserved in their full qualified form |
| Duplicate test-integrity wording in examples/prompts | Replaced with links or template references to single D1 home | Same policy, no divergent phrasing |
| Duplicate “unrun check passed” warnings | Replaced with D2 evidence reference; report fields remain | Exact E0–E5 distinction retained |
| Restated R0–R3 summaries in multiple chapters | Single D3 definition; cheat sheet only indexes it | Approval and stop conditions preserved |
| Five overlapping review prompts | One `{{FOCUS}}` reviewer with all required checks | Coverage mapping below |
| Common prompt rules (roughly twenty lines) | Eight durable lines, project-specific content in each prompt | Sources, [VERIFY], no invention, least privilege, stop/approval, evidence still included |
| “Why/what stays out” boilerplate, repeated examples and speculative rollout timing | Compact cards/tiered sequence | Unique templates and non-universal threshold caveats preserved |
| long list of suggested skills in core chapter | 5 starter skills + 17 suggestions in appendix | No idea lost; no claim that they must all be installed |

## Merged reviewer prompt coverage (P1)

Use [`prompts/reviewer.md`](prompts/reviewer.md) with `{{FOCUS}}`; common checks apply to every mode.

| prompt | V4 focus | Preserved checks / outputs |
| --- | --- | --- |
| Fresh-session reviewer | `full` | Independent diff against base, scope, meaningful tests and altered assertions, dependencies/config, security/privacy, conventions/architecture, docs/changelog, severity + file/line, not-performed checks |
| Software design review | `design` | SOLID only if applicable, DRY/KISS/YAGNI, cohesion/coupling, contracts/invariants, testability, security/privacy, alternative options, risk/verification, evidence |
| Overengineering review | `simplicity` | Extra interfaces/factories/packages/options/layers/helpers, requirement trace, maintenance cost, minimal safe alternative, losses, **underengineering**, severity vs confidence, regression tests |
| Acceptance verification | `acceptance` | Every acceptance criterion, expected/actual evidence, paths/commands, status verified/failed/not performed, revision/environment, E0–E5, scope/test changes, approval stops |
| Post-implementation review | `post-implementation` | Final diff vs approved contract, correctness, regressions, error/concurrency handling, architecture/security/dependencies, rollback, review effort, go/revise/blocked, cited findings |

Architecture tradeoffs reuse `prompts/write-adr-tradeoffs.md`.

## 4. Source-to-destination traceability

All V3 Markdown headings outside code fences are mapped; grouped subheadings share the parent destination, with examples extracted. Lines refer to V3.

| heading / subheading (source line) | V4 destination or disposition |
| --- | --- |
| Preface and navigation, lines 1–37 | `START-HERE.md`, `CHEATSHEET.md`, `reference/01-foundations.md`; attribution retained |
| 38: **Part 1: Foundations** | `reference/01-foundations.md` |
| 152: **Part 2: Core root files** | `reference/02-root-files.md` |
| 726: **Part 3: The docs folder** | `reference/03-docs-folder.md` |
| 1127: **Part 4: Additional documents** | `reference/04-additional-docs.md` |
| 1419: **Part 5: Agentic coding practice** | `reference/05-practice.md` |
| 1843: **Part 6: AI prompt library** | `prompts/README.md` |
| 2682: **Part 7: Skills, subagents, hooks and MCP** | `reference/07-tooling.md` |
| 2988: **Part 8: Rollout and checklist** | `reference/08-rollout.md` |
| 42: **The short answer: what you are missing** | `reference/01-foundations.md` |
| 68: **How coding agents read documentation**; subheads: Who reads which file | `reference/01-foundations.md` |
| 95: **Recommended repository layout** | `reference/01-foundations.md + appendix/repository-layout.md` |
| 156: **README.md**; subheads: What goes in; What stays out; Example; Common mistakes | `reference/02-root-files.md` |
| 243: **AGENTS.md**; subheads: What goes in; What stays out; Example; How to grow it | `reference/02-root-files.md` |
| 341: **CLAUDE.md and other tool files**; subheads: One source of truth, with a fallback; CLAUDE.md: what goes in and what stays out; The .claude/ folder: tool configuration, not a security boundary | `reference/02-root-files.md + appendix/tool-specific.md + templates/CLAUDE.md` |
| 442: **SECURITY.md**; subheads: What goes in; Agent specific threats to write down; What stays out; Example | `reference/02-root-files.md` |
| 537: **CHANGELOG.md**; subheads: Format rules (Keep a Changelog style); Agent rules; What stays out; Example; Automation option | `reference/02-root-files.md` |
| 611: **CONTRIBUTING.md**; subheads: What goes in; Rules for AI assisted contributions; What stays out; Example; Pair it with a PR template | `reference/02-root-files.md` |
| 730: **docs/architecture.md and ADRs**; subheads: What goes in; What stays out; Example; Architecture Decision Records (docs/adr/) | `reference/03-docs-folder.md` |
| 857: **docs/design.md (or ui.md)**; subheads: What goes in; What stays out; Example | `reference/03-docs-folder.md` |
| 951: **docs/roadmap.md**; subheads: What goes in; What stays out; Rule for agents; Example | `reference/03-docs-folder.md` |
| 1029: **docs/testing.md**; subheads: What goes in; Hard rules for agents; What stays out; Example | `reference/03-docs-folder.md` |
| 1131: **Documents you are missing, one by one** (supporting-doc index) | `reference/04-additional-docs.md` |
| 1135: LICENSE | `reference/04-additional-docs.md`; linked templates where present |
| 1143: CODE\_OF\_CONDUCT.md | `reference/04-additional-docs.md`; linked templates where present |
| 1161: docs/README.md (the docs index) | `reference/04-additional-docs.md`; linked templates where present |
| 1182: docs/setup.md (local development guide) | `reference/04-additional-docs.md`; linked templates where present |
| 1221: .env.example and docs/configuration.md | `reference/04-additional-docs.md`; linked templates where present |
| 1245: docs/specs/ (feature specs for agents) | `reference/04-additional-docs.md`; linked templates where present |
| 1284: docs/glossary.md (domain language) | `reference/04-additional-docs.md`; linked templates where present |
| 1299: docs/data-model.md | `reference/04-additional-docs.md`; linked templates where present |
| 1307: docs/api.md or openapi.yaml | `reference/04-additional-docs.md`; linked templates where present |
| 1325: docs/deployment.md and runbook | `reference/04-additional-docs.md`; linked templates where present |
| 1344: docs/troubleshooting.md | `reference/04-additional-docs.md`; linked templates where present |
| 1350: SUPPORT.md | `reference/04-additional-docs.md`; linked templates where present |
| 1356: .github/ templates and CODEOWNERS | `reference/04-additional-docs.md`; linked templates where present |
| 1375: .gitignore, .editorconfig and agent ignore rules | `reference/04-additional-docs.md`; linked templates where present |
| 1381: docs/performance.md and observability notes | `reference/04-additional-docs.md`; linked templates where present |
| 1387: THIRD\_PARTY\_NOTICES and dependency policy | `reference/04-additional-docs.md`; linked templates where present |
| 1393: Plans for long agent tasks (PLAN.md or docs/plans/) | `reference/04-additional-docs.md`; linked templates where present |
| 1423: **Engineering principles for agent-generated code** | `reference/05-practice.md` |
| 1450: **Universal setup for agentic coding**; subheads: 1. The task loop; 2. Write prompts like tickets; 3. Layer your guardrails; 4. Least privilege; 5. One command to verify everything; 6. Manage context deliberately; 7. Git habits; 8. CI gates that matter; 9. What to look for when reviewing agent code; 10. Make the loop learn | `reference/05-practice.md` |
| 1557: **Risk-based agent autonomy and stop conditions** | `reference/05-practice.md` |
| 1574: **Reusable task execution contract** | `reference/05-practice.md + templates/task-contract.md` |
| 1621: **Evidence-based verification and completion claims** | `reference/05-practice.md` |
| 1636: **Evaluating agents, prompts and repository instructions** | `reference/05-practice.md` |
| 1657: **Writing rules and what never belongs in docs**; subheads: Style rules for every doc; Good and bad rule wording; Length budget; What must never be in any doc | `reference/05-practice.md` |
| 1715: **Keeping docs alive**; subheads: Habits; Review rhythm; Automated checks; Let an agent audit the docs, then verify; Signs your docs are healthy | `reference/05-practice.md` |
| 1791: **Best practices and good-to-have**; subheads: By document; Cross-cutting best practices; Good-to-have extras once the basics are stable | `reference/05-practice.md + reference/08-rollout.md` |
| 1847: **Read first: disclaimer and how to use these prompts** | `prompts/README.md` |
| 1849: Disclaimer | `prompts/README.md` |
| 1859: If your tool does not support a feature | `prompts/README.md` |
| 1874: How to use the prompts | `prompts/README.md` |
| 1884: **Placeholders and the project brief** | `prompts/README.md` |
| 1888: Placeholder legend | `prompts/README.md` |
| 1914: The project brief (fill once, reuse in every prompt) | `prompts/project-brief.md` |
| 1953: **Master bootstrap prompts (universal project setup)** | `prompts/README.md` |
| 1957: Prompt A: audit and plan (no edits) | `prompts/bootstrap-audit-plan.md` |
| 1998: Prompt B: create one phase (run after you approve the plan) | `prompts/bootstrap-create-phase.md` |
| 2029: **Prompts for the core root files** | `prompts/README.md` |
| 2033: COMMON RULES and execution/output contract (add to every prompt) | `prompts/README.md (short shared rules)` |
| 2063: README.md | `prompts/write-readme.md` |
| 2082: AGENTS.md | `prompts/write-agents.md` |
| 2109: CLAUDE.md (or the equivalent file of your tool) | `prompts/write-claude.md` |
| 2129: SECURITY.md | `prompts/write-security.md` |
| 2151: CHANGELOG.md (bootstrap from history) | `prompts/write-changelog.md` |
| 2170: CONTRIBUTING.md and PR template | `prompts/write-contributing-pr.md` |
| 2191: **Prompts for the docs folder: architecture, ADRs, design, roadmap, testing** | `prompts/README.md` |
| 2195: docs/architecture.md | `prompts/write-architecture.md` |
| 2216: ADRs: backfill existing decisions | `prompts/backfill-adrs.md` |
| 2236: ADR: record a new decision | `prompts/write-adr-tradeoffs.md` |
| 2251: docs/design.md (skip if {{HAS\_UI}} is no) | `prompts/write-design.md` |
| 2273: docs/roadmap.md | `prompts/write-roadmap.md` |
| 2290: docs/testing.md | `prompts/write-testing.md` |
| 2314: **Prompts for supporting documents** | `prompts/README.md` |
| 2318: docs/setup.md | `prompts/write-setup.md` |
| 2335: .env.example and docs/configuration.md | `prompts/write-config.md` |
| 2352: A feature spec from a rough idea | `prompts/write-spec.md` |
| 2368: Implement from a spec | `prompts/implement-spec.md` |
| 2383: docs/glossary.md | `prompts/write-glossary.md` |
| 2393: docs/data-model.md (only if {{HAS\_DB}} is yes) | `prompts/write-data-model.md` |
| 2405: docs/api.md (only if {{HAS\_API}} is yes) | `prompts/write-api.md` |
| 2417: docs/deployment.md and runbook | `prompts/write-deployment-runbook.md` |
| 2429: docs/troubleshooting.md | `prompts/write-troubleshooting.md` |
| 2439: A plan file for a long task | `prompts/write-plan.md` |
| 2449: **Review, audit and improvement prompts** | `prompts/README.md` |
| 2453: Consistency check across all docs | `prompts/audit-docs-consistency.md` |
| 2471: Docs versus code audit (monthly) | `prompts/audit-docs-against-code.md` |
| 2482: AGENTS.md value check (prune it) | `prompts/prune-agents.md` |
| 2495: Fresh session reviewer for an agent's changes | `prompts/reviewer.md (merged P1)` |
| 2510: Quick start test | `prompts/test-quickstart.md` |
| 2519: Learn from a mistake | `prompts/learn-from-mistake.md` |
| 2530: Agent configuration safety review | `prompts/audit-agent-config.md` |
| 2542: Software design review against engineering principles (read-only) | `prompts/reviewer.md (merged P1)` |
| 2559: Classify risk before implementation (plan-only) | `prompts/classify-change-risk.md` |
| 2573: Find overengineering and unnecessary abstractions (read-only) | `prompts/reviewer.md (merged P1)` |
| 2586: Verify completed implementation against acceptance (read-only by default) | `prompts/reviewer.md (merged P1)` |
| 2600: Post-implementation engineering review (read-only) | `prompts/reviewer.md (merged P1)` |
| 2617: **Adapting the prompts to your project** | `prompts/README.md` |
| 2621: Extra placeholders used inside prompts | `prompts/README.md` |
| 2640: Typical commands by stack (confirm against your repository) | `appendix/command-examples.md` |
| 2654: Variants by project type | `prompts/README.md (project variants)` |
| 2671: Tips for modifying a prompt | `prompts/README.md` |
| 2686: **Which mechanism for which job** | `reference/07-tooling.md` |
| 2713: **Suggested skills to create**; subheads: Useful in almost any project; Useful when you have the matching part; Skills for producing documents and deliverables; Using skills from other people | `reference/07-tooling.md + appendix/more-skills.md` |
| 2757: **Writing good skills**; subheads: Authoring rules; Example: a write-adr skill | `reference/07-tooling.md` |
| 2819: **Suggested subagents, hooks and MCP servers**; subheads: Subagents; Hooks; MCP servers (if applicable); When not to use these; Suggested adoption order | `reference/07-tooling.md` |
| 2972: **Official-source verification ledger (checked 2026-11-15)** | `appendix/tool-specific.md` |
| 2992: **Rollout order and final checklist**; subheads: Choose a setup tier before adding files; Suggested order; Use an agent to draft, then verify; Final checklist (apply only the items justified by the chosen tier); The five ideas to remember | `reference/08-rollout.md` |

## 5. Verification and owner decisions

See the final measured results below and [the per-file metrics](appendix/file-metrics.csv).

### Final completion evidence

Changed **84 files** in new `handbook/` folder; source V3 unchanged (SHA-256 `a331a895e2e517646b9c1f4783c4e14da0a9695414b0a18d91567068aa28ffd6`). Baseline **29,561 words / 3,088 lines**. V4 **22,914 words / 2,502 lines** (**-22.5% word change**), including log and metrics. Excluding the audit log and metrics, core content is **19,840 words (-32.9%)**. Seven reference chapters, **74** Markdown files. `reference/05-practice.md` has 3,309 words because risk, evidence, principles and enforcement definitions share one authority; other Markdown files are under 3,000 words. See [per-file word/line counts](appendix/file-metrics.csv).

**Static validation:** Markdown fences/headings parsed / balanced; local links 235 checked, PASS (0 broken); 4 JSON templates and 1 YAML template plus 3 YAML frontmatter examples syntactically valid; 56 documented prompt variables, no unknown placeholders. Duplicate-phrase scan: illustrative=22, not a security boundary=3, verify=37, not tested=5, not a universal=4. Residual repeats are templates, labels and traceability; D1–D3 each has one authority. **Syntax ≠ runtime enforcement.**

**Not performed:** installs, application/build tests, hook integration, CI, production operations, Git actions, live Claude or MCP. **Owner decisions:** (1) confirm single-folder distribution (used here), (2) retain TaskFlow as fictional until a separate tested reference repo is authorized, (3) attribution retained in START-HERE (confirm desired per-file attribution), (4) confirm real licenses, contacts, scripts, migrations and merge policy before adoption.
