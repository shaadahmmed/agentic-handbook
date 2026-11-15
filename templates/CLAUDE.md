@AGENTS.md

## Claude Code specifics

- For high-risk or cross-cutting changes, propose a plan and seek approval
  before editing; follow the risk table in the task contract.
- Use the `reviewer` subagent if installed and permitted; otherwise request
  a separate human or fresh-session review.
- Use `/ship` only if the repository defines it; do not commit without approval.
- In a long task, retain the goal, modified paths, unresolved blockers and
  verification evidence across compaction or a new session.
