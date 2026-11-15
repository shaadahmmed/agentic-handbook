# Design Guide

Tokens live in `packages/ui/src/tokens.ts`. This guide explains how to use them.
Design file: https://www.figma.com/file/example (read only).

## Principles

1. Clarity over decoration.
2. Everything is reachable and operable by keyboard.
3. One primary action per screen.

## Tokens (use names, never raw values)

| Token | Meaning | Use for |
| --- | --- | --- |
| color.primary | Brand blue | Primary buttons, links, focus ring |
| color.danger | Red | Destructive actions, errors |
| color.surface | Page background | Cards, panels |
| color.text.muted | Secondary text | Hints, timestamps |
| space.1 to space.8 | 4px steps | All margins and padding |
| radius.md | 8px | Cards, inputs, buttons |

Rules:
- No hex codes, pixel margins or font sizes inside components. Use tokens.
- Need a value that is not a token? Propose a new token; do not hard code.

## Components

Import from `@taskflow/ui`. Check Storybook before building anything new.

| Component | Use when |
| --- | --- |
| Button (primary, secondary, ghost, danger) | Any action. One primary per view |
| TextField | Single line input, always with a visible label |
| Dialog | Blocking decisions only. Not for forms with more than 5 fields |
| Toast | Non-blocking confirmation, disappears after 5 seconds |

## States checklist

Every new interactive component ships with: default, hover, focus visible,
disabled, loading and error. Every list ships with an empty state that says
what to do next.

## Accessibility (target: WCAG 2.2 AA)

- For WCAG 2.2 AA, normal text generally needs 4.5:1; large text 3:1; essential non-text UI graphics/components 3:1, subject to the applicable exceptions.
- All inputs have labels. Icon-only buttons have an `aria-label`.
- Pointer targets meet WCAG 2.2 AA SC 2.5.8 (24×24 CSS px or an allowed spacing/equivalence/other exception). Prefer larger touch targets; 44×44 CSS px is the enhanced AAA SC 2.5.5 target, not an AA minimum. [W3C AA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) · [W3C AAA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced).
- Never rely on color alone to show status; add an icon or text.
- Respect `prefers-reduced-motion`.

## Writing

- Buttons: verb first, sentence case ("Create task", not "Submit").
- Errors: say what happened and how to fix it. No blame, no codes alone.

## Verification

Run `pnpm storybook:test` and attach a screenshot of each changed screen at
375 px and 1280 px widths to the PR.
