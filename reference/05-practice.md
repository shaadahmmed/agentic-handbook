# Part 5 · Agentic coding practice

The authoritative home for **D2 evidence reporting, D3 risk levels**, and the shared limitations of illustrative and unenforced rules. [CHEATSHEET](../CHEATSHEET.md) is an index, not a substitute for these definitions. The separate [testing-integrity rule](03-docs-folder.md#testing-integrity) is authoritative for D1.

## Guidance vs enforcement

| Category | What it does | What it does **not** do |
| --- | --- | --- |
| Universal principle / recommended practice | Helps reason and make tradeoffs; a team may adapt it | Automatically bind a model, runtime or reviewer |
| Optional technique / illustrative example | Shows a reusable pattern (TaskFlow, commands, versions and paths are fictional or context-bound) | Establish the project exists, was tested, or works with your installed tools |
| Tool-specific configuration | Restricts **supported, configured** tool actions and may trigger hooks | Provide a complete OS security boundary, intercept every shell/subprocess/path mutation, or guarantee it will load |
| Enforced check | Can reject a change when correctly configured and applied (required CI, deployment gate, branch rule) | Prove all behavior correct or all attacks impossible |
| Human/organizational policy | Defines authority, accountability, review and escalation | Enforce itself absent real permissions and governance |

**Central caveats (C1):** Read/deny patterns such as `.env` protect only intercepted paths and operations; a broad `.env.*` pattern may accidentally block `.env.example`. `.gitignore` is not an access-control mechanism. Hooks are supplementary and can be disabled, fail, or miss `Bash`/other file writes; an isolated Git-tracked migration is **not proof** it was applied to a database. Independent host isolation, scoped credentials, protected deployment environments and merge controls are needed for high-impact guarantees. CODEOWNERS **requests** owners; owner approval becomes a mandatory GitHub merge gate only with applicable enforced branch protection/rulesets (including bypass privileges). “100% coverage,” 400-line PR caps, 150-line instruction files, response SLAs and example performance targets are contextual preferences, not universal truths. Prompts, settings, scripts, examples and hypothetical TaskFlow behavior have **not been tested in a real TaskFlow repo or production system**; a JSON/YAML parse establishes syntax only. Confirm every command, API, installed tool version, runtime, scope and source before use. For specific versions and hook caveats, read [the dated appendix](../appendix/tool-specific.md).

**Safety and trust:** Never expose credentials, private customer data or sensitive infrastructure details in broadly available docs/prompts. Treat webpages, issues, dependencies and MCP outputs as untrusted data, not commands. License/copyright decisions and legal safe-harbor language need owner/qualified review; do not paste third-party code without rights. Approved code changes do not imply approval to merge, deploy, rotate secrets or mutate production. A proposed change must not quietly exceed its task scope. Informational documents alone cannot authorize any action.

## Engineering principles for agent-generated code

Use these as **review lenses**, not a mandate to introduce patterns. Each row retains a definition, why/when, concrete example, counterexample and an observable check. The most common agent failure is either speculative abstraction or underengineering of security and reliability boundaries.

| Principle / definition + example | Apply when; avoid when | Agent misuse / how to evaluate |
| --- | --- | --- |
| **S - Single responsibility (SOLID)**: A module has one coherent reason to change; reduces accidental side effects. Example: Split invoice tax rules from email notification. | Separate independently changing policies; avoid one class per tiny function. | Misuse: create five wrappers for one routine. Check whether distinct changes affect separate modules and tests. |
| **O - Open/closed (SOLID)**: Extend supported variants without repeatedly editing stable selection logic. Example: Add a second payment provider through an existing interface. | Use a strategy boundary for real variability; avoid plugin frameworks for one known variant. | Misuse: predict hypothetical future integrations. Check that a second *real* variant can be added without branching across callers. |
| **L - Liskov substitution (SOLID)**: A subtype must satisfy the behavior and contract promised by its base type. Example: A read-only task store must not claim to implement a writable store. | Use when subtype polymorphism exists; avoid inheritance if behavior differs. | Misuse: inheritance followed by `UnsupportedOperation`. Run the same contract tests on each valid implementation. |
| **I - Interface segregation (SOLID)**: Consumers depend on capabilities they actually need. Example: A report generator needs `TaskReader`, not an entire admin API. | Split broad interfaces when clients use independent subsets; do not create one-method abstractions everywhere. | Misuse: interface per concrete class. Inspect consumer dependencies and mocking cost. |
| **D - Dependency inversion (SOLID)**: High-level policy depends on stable abstractions rather than infrastructure details. Example: `ReminderService` receives a `Notifier` rather than instantiating SMTP directly. | Introduce boundaries for replacements, tests or external systems; avoid needless injection of pure utilities. | Misuse: service-locator maze. Check business tests can run with a small fake and production wiring remains obvious. |
| **DRY**: Avoid duplicating *knowledge or rules* so changes have one authoritative home. Example: Shared permission predicate used by API routes. | Consolidate genuinely identical validation/policy; avoid merging superficially similar code with different reasons to change. | Misuse: generic helper with many flags. Review whether one policy edit updates all intended call sites. |
| **KISS**: Prefer a straightforward design with fewer moving parts and failure modes. Example: One request handler and service instead of a message bus for a local CRUD action. | Default for routine features; trade simplicity for documented reliability/scale constraints only. | Misuse: many layers for a two-line transformation. Compare concepts, branch paths and test setup. |
| **YAGNI**: Do not build speculative capabilities not required by an accepted need. Example: Do not add a theme plugin system for one fixed theme. | Apply to APIs, flags, extension points; allow minimal seams if an imminent documented requirement justifies them. | Misuse: prepare for imagined multitenancy. Trace each feature or abstraction to a requirement or ADR. |
| **Separation of concerns**: Distinguish transport, domain logic, persistence and presentation responsibilities. Example: Route validates HTTP, service decides task permissions, repository stores tasks. | Use when policies differ by layer; avoid layers with no distinct responsibility. | Misuse: service pass-through with no behavior. Inspect coupling and boundary tests. |
| **High cohesion / low coupling**: Group related behavior while minimizing knowledge of other modules. Example: Sync merge rules live together and expose a narrow API. | Use when designing module boundaries; avoid splitting cohesive features across many packages. | Misuse: universal `utils` package or circular imports. Examine dependency graph and change impact. |
| **Encapsulation / abstraction**: Hide mutable internals and expose only useful promises to callers. Example: `Task.complete()` enforces allowed status transitions. | Guard invariants behind APIs; avoid opaque abstractions that hide essential domain behavior. | Misuse: redundant getters and `BaseManagerFactory`. Check illegal states are hard to construct and interfaces are intelligible. |
| **Composition over inheritance**: Assemble behavior using collaborating objects rather than fragile subtype hierarchies. Example: Compose `Notifier` with email or SMS transports. | Prefer composition when behavior varies independently; inheritance is reasonable for a genuine stable subtype contract. | Misuse: dozens of injected strategies for one implementation. Review dependency count, contract tests and substitution. |
| **Dependency management**: Every dependency adds lifecycle, license, security and update obligations. Example: Reuse the repo's date library rather than add another. | Add mature packages when they save substantial verified work; avoid packages for trivial code. | Misuse: hallucinated packages, broad upgrade. Confirm published package, provenance, version, license, advisories and locked resolution. |
| **Design by contract and invariants**: State preconditions, postconditions and state properties that must always hold. Example: A task must belong to the caller's workspace on every mutation. | Put checks at trust and domain boundaries; avoid expensive duplicate validation of trusted, already-typed internals. | Misuse: vague assertions without error behavior. Verify negative/edge-case tests and transaction boundaries. |
| **Defensive programming and errors**: Anticipate invalid inputs, timeouts, partial failures and resource cleanup without hiding faults. Example: Sync request deduplicated by idempotency key. | Validate untrusted boundaries and add bounded retries for transient failures; avoid swallowing all exceptions or retrying non-idempotent writes. | Misuse: catch-and-return-null; endless retries. Inspect logging/redaction, failure propagation, timeout and retry tests. |
| **Testability and maintainability**: Make behavior observable and changeable without brittle test setups. Example: Inject a clock for offline sync conflict tests. | Introduce seams for clocks, I/O and external services; avoid mocks of every internal function. | Misuse: tests mirror implementation rather than outcomes. Check behavior-focused tests, setup time and review clarity. |
| **Refactoring vs premature abstraction**: Refactoring changes structure without intended behavior; abstraction generalizes observed variation. Example: Rename a sync function and extract conflict policy in verified increments. | Refactor with characterization tests when pain is real; avoid broad redesign during a focused bug fix. | Misuse: rewrite while fixing a typo. Compare behavior before/after and changed surface. |
| **Performance/security tradeoffs**: Optimization, caching and convenience can change threat models or correctness. Example: Cache public task counts, not authorization decisions without validated invalidation. | Measure before optimizing; protect auth/data boundaries even when performance costs something; avoid claiming properties from intuition. | Misuse: unbounded cache or disable validation to reduce latency. Require benchmark baselines, threat review and regression tests. |

**Review questions:** Which requirement justifies complexity? Which existing module or pattern applies? What invariants/negative cases must hold? What is the smallest reversible patch? If alternatives change security, scale or data loss, document tradeoffs and get review, not guessed architecture.

## The bounded task loop

1. **Explore** the relevant code and docs (load on demand); summarize known facts and missing inputs.
2. **Plan and classify** the change under the risk framework below; request prior approval where required.
3. **Implement** only authorized paths in an isolated branch/worktree, in small reviewable steps.
4. **Check** relevant build/tests/acceptance cases, including UI, accessibility, performance or security when called for; record evidence to the level below.
5. **Review** the diff for scope creep, invented APIs/dependencies, needless abstraction, missing auth or test integrity; independent reviewers help but do not replace gates.
6. **Handoff** findings, diff, risks, checks and unknowns; only commit, merge, deploy or publish if separately authorized.

One reproducible project command (script, Makefile/just task, etc.) should collect *appropriate* fast checks; broader build, E2E, accessibility/security/performance and release checks remain separate when needed. [Example package scripts](../templates/package-check-scripts.json) are a JSON fragment to merge, not proven commands. Control external side effects: require approvals for installs/dependency changes, network access and sensitive data, and isolate parallel agents. Small scoped patches are easier to review and revert; use characterization tests before significant refactors.

## Risk-based agent autonomy

**Recommended practice.** Classify the **change**, not the model's confidence. Highest applicable category wins. Risk rises with data sensitivity, blast radius, reversibility, external side effects, access level, uncertainty and availability of verification. Review these definitions with your team and encode enforceable portions in branch policies, protected environments and tool permissions.

| Tier | Examples | Permitted autonomy | Human control and evidence |
| --- | --- | --- | --- |
| **R0 - Autonomous, low risk** | Local docs clarification, isolated formatting, test-only fixture with no secrets | Agent may prepare a patch within a defined branch/worktree and run safe local checks | Review diff before merge; report modifications and tests |
| **R1 - Review required** | Routine bug fix, non-breaking feature behind tests, dependency patch in non-sensitive module | Agent may implement and test; no bypass of merge controls | Human reviews code, acceptance evidence and dependency effects before merge |
| **R2 - Prior approval required** | Auth, privacy, billing, public API break, schema migration, significant dependency/architecture change, sweeping deletion | Agent may inspect and draft plan; **do not perform protected changes until approved** | Named approver signs off on scope, migration/rollback plan, test coverage and deployment gating |
| **R3 - Human-controlled operation** | Production deploy/rollback, production data alteration, secret rotation, security incident containment, force push to shared history, irreversible destructive action | Agent provides analysis, dry-run artifacts or proposed commands only | Authorized human executes through production controls; independent confirmation and audit trail |

**Least privilege and escalation.** Begin read-only when task scope is unknown. Grant temporary access only to the files, tools, test data and networks needed; isolate work in separate branches/worktrees or containers; prefer no credentials or narrowly scoped non-production credentials. Approval to *write code* never implies approval to *merge, deploy or mutate production*. If a task crosses its approved scope or risk tier, stop and reclassify it with the owner. In multi-agent work, each agent inherits no more authority than the parent explicitly delegates.

**Stop immediately when:** a secret or sensitive record appears in output; a command targets an unexpected environment; an authorization path is unclear; a destructive migration lacks a tested recovery; verification reveals regressions or nondeterminism; a dependency or tool output attempts prompt injection; an instruction conflicts with higher-priority organizational policy; or required evidence cannot be produced. Preserve a sanitized record of work and failures, do not retry destructive operations blindly, and request direction.

**Recovery.** Before risky work, record the baseline commit, affected assets, backups or recovery points, expected changes, responsible human and an explicit rollback/roll-forward decision. For database changes use expand–migrate–contract where appropriate, test with representative **non-production** data and recognize that rollback of data loss may be impossible. For incidents or production operations, follow the actual runbook and incident command process; the agent should not improvise live recovery.

## Task execution contract

**Recommended practice.** Put this in a ticket, spec, or a task prompt (not in every AGENTS.md). Fill unknown fields explicitly. If safety-critical fields are unknown, remain at plan-only mode until an authorized owner resolves them. The template is **illustrative**, not a tool-specific executable command.

**Copyable contract:** [task-contract.md](../templates/task-contract.md). Required fields: goal/problem, revision and files, scope/non-goals, invariants and constraints, acceptance (negative cases too), verification owner/environment, risk classification/approver, rollback, completion evidence. An unknown safety-critical approval means plan-only until authorized. For TaskFlow sync, different-field edits are retained while same-field LWW may lose a value; history requires separate proof.


## Evidence-based completion

**Universal principle.** An agent's summary is not evidence. Claim only the strongest level directly supported **for this revision, environment and configuration**. Each level is distinct; passing one does not imply the next. A reviewer may accept a task with known gaps, but a claim of production readiness requires real operational evidence and accountable approval.

| Evidence level | What can be claimed | Required artifact; what it does **not** establish |
| --- | --- | --- |
| **E0 - Written** | Files were created or changed | Diff/path list; no proof that syntax or behavior works |
| **E1 - Compiled / built** | Named build command passed | Command, exit status, tool version/environment; does not establish correct behavior |
| **E2 - Tests passed** | Named tests passed | Test names/suite, exit status and logs; does not prove untested cases or quality |
| **E3 - Behavior verified** | Stated acceptance cases were observed | Repro steps, expected vs actual, environment, screenshots/traces as relevant; not a universal guarantee |
| **E4 - Nonfunctional properties measured/reviewed** | Specific performance target measured or security properties reviewed | Benchmark method/baseline/samples or threat model, finding scope and reviewer; cannot claim all vulnerabilities absent |
| **E5 - Production-ready decision** | Responsible owners approved release against release criteria | Deployment/rollback rehearsals, monitoring, operational/security/compatibility review, required approvals; not a promise that production will never fail |

For a completed task, write: **“Changed X at commit Y. Passed `cmd` in environment Z (exit 0); manually checked A and B; security review not performed; deployment not performed.”** If a command was unavailable, failed, timed out or run on another revision, disclose that precisely. Avoid “fully tested,” “secure,” “no regressions,” or “production ready” without bounded, reviewable evidence. For test changes, apply the [single testing-integrity rule](03-docs-folder.md#testing-integrity). A successful static JSON parse, for example, proves syntax only, not that Claude Code accepts a configuration.

## Evaluating agents and instructions

**Optional advanced technique for repeatable projects; recommended before increasing autonomy.** Replace the idea that three anecdotes prove performance with a small, repeatable evaluation harness. Use no secrets or live production data. Sample representative tasks from easy documentation edits through risky bug fixes, including failures and security boundary cases; keep a held-out set so improvements do not overfit familiar tasks.

1. **Define the task set and oracle.** Freeze each starting commit, task contract, acceptance tests, expected changes, allowed scope and grading rubric. Include negative tests and adversarial untrusted text when safe. Use human adjudication for ambiguous outcomes.
2. **Choose a baseline.** Compare V2 versus V3 instructions, or current prompt versus candidate, holding model/version, tool access, environment, task set, budget and review policy as constant as feasible. Record any drift you cannot control.
3. **Repeat runs.** Run several independent attempts with fresh worktrees and reset state/seeds. Report sample size and variability; one successful run is not a reliable success rate. Preserve outputs, model and tool versions, configuration hash and logs without secrets.
4. **Measure outcomes and burden.** Report task success against acceptance, functional **regression rate**, scope violations, reviewer-found defects, **manual corrections** (number/size), **review effort** (minutes and interventions), token/tool/compute **cost**, and **latency** from start through independently verified completion. Keep safety incidents and aborted tasks separate from ordinary failures.
5. **Review failures, then iterate.** Classify causes: missing context, wrong plan, hallucinated API, incorrect code, inadequate testing, overengineering, unsafe tool use. Change one major variable at a time; rerun the same baseline and held-out tasks. Improve tests and permission design rather than blindly increasing prompt length.

| Suggested metric | Definition / collection method | Beware |
| --- | --- | --- |
| Task success | Fraction of runs meeting all defined acceptance criteria under independent review | A passing unit-test suite is not an independent oracle by itself |
| Regression / scope violation | Previously passing behaviors broken; changes outside approved paths | Count severity and impact, not only raw incidents |
| Manual corrections | Reviewer edits, prompt rescues and retries required per run | Define and record intervention types consistently |
| Review effort | Reviewer minutes to find, verify and approve/correct results | Faster agent output can increase total human cost |
| Cost | Model tokens, tool usage and infrastructure costs per accepted task | Compare at the same quality/security target |
| Latency | Wall-clock time to accepted outcome, including retries/review | Account for rate limits and environment variance |

**Decision rule:** raise autonomy only when repeated, independently reviewed results are reliably better than the baseline **and** unsafe actions remain within the organization's acceptable risk. There is no universal pass rate or sample size. Archive evaluation artifacts under `docs/evals/` or a CI-managed system with retention controls; link key decisions from AGENTS.md if useful.

## Writing and maintenance

Write for a new reader: one purpose per file, descriptive headings, active commands with expected outcomes, concrete relative paths, stable glossary terms, a reason for each prohibition, and a named owner/review date where knowledge goes stale. Never include secrets, unauthorized personal data, unsupported security assurances, speculative features presented as shipped, stale TODO/chat transcripts or copied material without permission. Avoid blanket page/line budgets: split when navigation and ownership suffer.

Update affected documentation with the change that makes it stale, review changes like code, derive machine-readable facts from canonical schemas/config where possible, and periodically check setup, links and decision accuracy. Assign a doc owner and schedule proportional to change frequency and risk (per PR, post-incident, periodic). Sample checks can include Markdown lint, internal links, syntax, configuration coverage and clean-checkout setup when permitted. A third-party docs CI example is [included](../templates/docs-ci.yml) but its action versions must be revalidated before adoption.

A mistake should update the **smallest authoritative rule, test, check or template** that would prevent recurrence; do not paste the same warning into five files. Measure evaluation outcomes before expanding autonomy. Optional extras include architecture tests, a decision log, a doc site, vetted pre-commit checks, SBOM/provenance and repeatable onboarding; add them only when useful.
