---
name: write-adr
description: Writes an architecture decision record in docs/adr/. Use when the user makes or asks about a significant technical decision, such as choosing a library, database, API style or pattern, or asks to document why something was built a certain way.
---

# Write an ADR

## Steps

1. Read docs/architecture.md and the existing records in docs/adr/ so the
   decision does not contradict or duplicate one.
2. Get the next number: run `scripts/next-number.sh`.
3. Ask the user for anything missing: the question, constraints, options
   considered, and who decided. Do not invent alternatives or reasons.
4. Copy `template.md` to `docs/adr/NNNN-short-title.md` and fill it in.
   Status is `Proposed` until the user accepts it.
5. Add a row to the table in docs/adr/README.md.
6. If the decision replaces an old one, set the old record's status to
   `Superseded by NNNN` and link both ways. Never edit the old decision text.
7. Check: record is focused, has Context, Decision and Consequences, and
   every claim of fact is true of the current code.

## Do not

- Write an ADR for routine choices that are easy to reverse.
- Mark a record Accepted without the user's confirmation.
