# Write Architecture

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write docs/architecture.md for {{PROJECT_NAME}} by reading the code.
[PROJECT BRIEF] [COMMON RULES]

Sections: purpose and scope; system context (who and what interacts with the
system); a Mermaid diagram of containers or modules; components table with
columns Component, Owns, Must not, Depends on; two or three key flows traced
through real files; data stores and what each holds; cross-cutting concerns
(auth, errors, logging, config, background jobs); architectural rules that can
be checked (for example allowed dependency directions); quality goals only if
they are stated somewhere in the repo; known debt and risks; links to ADRs.

Constraints: describe only what exists. Cite file paths for every component
and rule. Do not describe individual functions. Do not include plans for the
future. Add "Last reviewed: {{TODAY}}" and "Owner: {{OWNER}}".
For rules you infer from code patterns rather than documentation, label them
"observed, not enforced" so I can decide whether to make them real rules.
