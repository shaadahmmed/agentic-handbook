# Part 3 · The `docs/` folder

Store deeper, change-owned knowledge here, and give agents a short *when to read it* pointer. Each example is editable independently under [templates](../templates/README.md).

## Architecture and ADRs

`docs/architecture.md` should state system context, principal modules and ownership boundaries, key flows, data stores, interfaces, important constraints, known debt and cross-links to decisions. Prefer text diagrams such as Mermaid (and keep their source) over image-only diagrams. Don't duplicate every source function or API schema. [TaskFlow architecture](../templates/docs/architecture.md) includes its per-field last-writer-wins (LWW) sync policy; same-field conflicts may lose an update. The example is **not** a lossless CRDT.

ADRs record significant, nontrivial decisions as **Status, Context, Decision, Consequences**, including rejected options. A superseding ADR references the old one rather than silently replacing history. Use them when a decision affects several modules, costs a lot to reverse or is likely to be challenged. [Example accepted sync ADR](../templates/docs/adr/0004-use-last-writer-wins.md). An accepted ADR still needs review before architectural changes.

## UI design and accessibility

`docs/design.md` (or `ui.md`) links to canonical tokens/components, layout rules, keyboard and focus behavior, interactive/loading/error/empty states, responsive/localization/motion guidelines and ways to verify UI. Keep actual token values in code; avoid independent lists that drift. WCAG 2.2 **AA** target size minimum is **24 × 24 CSS pixels with specified exceptions**; **44 × 44** is the enhanced **AAA** criterion, and may still be a useful design goal ([standards ledger](../appendix/tool-specific.md#standards-and-platform-ledger)). [TaskFlow design example](../templates/docs/design.md).

## Roadmap and specs

A roadmap records **Now / Next / Later**, prioritized outcomes, non-goals, milestone exit criteria, owner and major dependencies. “Later” is not authorized scope. Date a commitment only where one exists. [Example roadmap](../templates/docs/roadmap.md). Feature acceptance belongs in a [spec](../templates/docs/specs/0012-sync-conflicts.md) or in a ticket/task contract-not both independently.

## Testing strategy

`docs/testing.md` owns: exact test commands, where tests live, coverage and confidence by risk, fixtures and privacy, mocking boundaries, flaky-test handling, behavioral/negative-case expectations, and which checks block merging. Numeric floors (80% or 95% coverage), ratios (70/25/5 tests), retries and timing limits in an example are **team-selected illustrations**, not proof or universal best practices. Coverage counts executed lines/branches; it does not establish behavioral correctness. [TaskFlow testing example](../templates/docs/testing.md) no longer contains a fictitious Playwright version pin.

### Testing integrity

**Authoritative D1 rule:** Never delete, skip, weaken, blindly rewrite assertions/snapshots, or change expected results merely to hide a failure. When a test is genuinely wrong, explain the evidence and obtain appropriate review for the correction. Reproduce a bug with a meaningful failing test when practical, then fix behavior and rerun relevant checks. Investigate flaky tests, document ownership, and set an appropriate remediation deadline rather than silently masking them. A failed or unrun check must be reported by the [evidence standard](05-practice.md#evidence-based-completion).

Write tests for observable behavior and boundary failures, not just internal implementation. Prefer controlled clocks and realistic I/O boundary testing. Run narrow tests during iteration and broader, justified checks for completion; if the environment cannot run a suite, record the limitation instead of reclassifying it as passed.

## Other possible docs

`docs/README.md` maps responsibilities ([example index](../templates/docs/README.md)). Setup, configuration, data model, API contract, deployment and incident runbooks, troubleshooting, glossary, performance and observability are explained in [Part 4](04-additional-docs.md). Use Markdown-relative links for all cross references.
