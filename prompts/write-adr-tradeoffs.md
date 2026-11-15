# Write Adr Tradeoffs

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

I need to decide: {{DECISION_QUESTION}}.
Constraints: {{CONSTRAINTS}}. Options I know about: {{OPTIONS}}.

Compare options using explicit criteria: correctness, architecture fit,
security/privacy, complexity, operational cost, performance evidence, failure
modes, reversibility and team capacity. Identify assumptions and missing data;
recommend the simplest justified choice, explain rejected alternatives and what
evidence would change the recommendation. Then draft the ADR
using the same template as docs/adr/ files. Status: Proposed. Do not implement
anything until I accept it.

Evaluate each viable alternative for correctness/invariants, security and privacy,
performance measurement needs, portability, migration/rollback reversibility,
dependency/maintenance cost, and uncertainty. Cite source paths and mark
unknowns [VERIFY]. Record status as Proposed until a named owner approves;
do not treat this prompt as permission to implement the decision.
