# Write Design

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write docs/design.md by inspecting the existing UI code, theme and component
files.
[PROJECT BRIEF] [COMMON RULES]

Sections: design principles (3 to 5, only if they are evident or I provided
them: {{DESIGN_PRINCIPLES}}); token table (name, meaning, where defined, use
for) built from the real theme file; component inventory with import path and
when to use each; layout and breakpoints; required states for interactive
components and lists; accessibility target ({{A11Y_TARGET}}, default WCAG 2.2
AA) with concrete checks; content and tone rules inferred from existing copy,
marked [VERIFY]; verification steps (storybook, visual tests, screenshots).

Constraints: link to the tokens file as the source of truth, never duplicate
raw values that already live in code. No pasted component code.
If no design system exists, say so, list the inconsistencies you found (for
example five different blues), and propose a minimal token set as a separate
suggestion section, not as fact.
