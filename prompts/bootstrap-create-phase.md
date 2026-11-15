# Bootstrap Create Phase

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Implement phase {{PHASE_NUMBER}} of the approved plan: {{PHASE_FILE_LIST}}.

[Paste the PROJECT BRIEF here]

Rules:
- Create only the files listed for this phase. Do not touch application code.
- Use the structure and length targets from the plan. Aim for concise instructions (concise instruction files are a heuristic, not an acceptance gate).
- Put each fact in exactly one file and link from the others.
- Every command must be one you confirmed in the repository and reviewed
  for external effects. Mark the rest [VERIFY] and list them in your final message.
- Use clear, specific, checkable language. No filler, no marketing words,
  no generic advice such as "write clean code".
- Never include secrets, real personal data, or internal URLs. Use example
  values such as demo@example.com.
- Use clear punctuation and consistent Markdown; do not change technical meaning for a style preference.
- Where this tool does not support a requested feature, create the fallback
  described in the plan and tell me.

When done:
1. Show a table of files created with line counts.
2. List every [VERIFY] item.
3. List any contradictions you noticed with existing files.
4. Stop. Do not start the next phase.
