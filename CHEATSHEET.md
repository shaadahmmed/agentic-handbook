# One-page agentic coding cheatsheet

An index to the **authoritative** definitions, not an alternate policy. Read [Guidance vs enforcement](reference/05-practice.md#guidance-vs-enforcement) before treating any guideline as mandatory or enforced.

## Change-risk gate

| Tier | Recognize it | Next action |
| --- | --- | --- |
| **R0** | Low-risk isolated docs/formatting work | Scoped agent patch and safe checks; review before merge |
| **R1** | Routine code/docs change with review | Agent may prepare evidence; human reviews before merge |
| **R2** | Auth, privacy, billing, significant schema/API/architecture effect | Plan only until named prior approval |
| **R3** | Production mutation, secret rotation, irreversible destruction, incident action | Human executes through authorized operational controls |

[Full risk criteria, escalation, recovery and stop conditions](reference/05-practice.md#risk-based-agent-autonomy). Highest applicable tier wins; **approval to edit never grants approval to deploy**.

## Evidence ladder

| Level | Only claim what evidence supports |
| --- | --- |
| **E0** | Files/diff written |
| **E1** | Named build compiled/passed |
| **E2** | Named tests passed on the specified revision |
| **E3** | Acceptance behavior actually observed |
| **E4** | Measured performance and/or scoped security review |
| **E5** | Accountable production-ready decision with operational/approval evidence |

[Evidence and uncertainty reporting contract](reference/05-practice.md#evidence-based-completion). These are **not** automatically cumulative: a green unit test is not a security or readiness guarantee.

## Six guardrail layers

| Layer | Purpose |
| --- | --- |
| Instructions | Explain scope, conventions and links, but remain guidance |
| Scoped permissions / isolation | Restrict supported tools and independently constrain host access |
| Hooks / local checks | Warn or intercept matching operations; can miss others |
| Required CI | Reject configured failures when protected by rules |
| Branch/deployment controls | Enforce approvals and privileged boundaries when configured |
| Responsible human | Reviews intent, consequences and authorization |

The [central enforcement caveats](reference/05-practice.md#guidance-vs-enforcement) apply to every layer; don't assume CODEOWNERS alone blocks merges or a hook blocks shell writes.

## Route the task

- New project? [START-HERE](START-HERE.md), [minimum AGENTS](templates/AGENTS.min.md).
- New design or bug? [Principles](reference/05-practice.md#engineering-principles-for-agent-generated-code), [task contract](templates/task-contract.md).
- Testing dispute? [Testing integrity](reference/03-docs-folder.md#testing-integrity).
- Reviewing agent work? [Merged reviewer prompt](prompts/reviewer.md).
- Need tool-specific config? [Dated appendix](appendix/tool-specific.md), then [templates](templates/README.md).
- Ready to adopt as a team? [Tiered checklist](reference/08-rollout.md).
