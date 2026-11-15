# Write Changelog

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Draft CHANGELOG.md in Keep a Changelog format from the repository's git
history and tags. Use read-only `git log` and `git tag`; do not modify history.
Verify the release notes against the actual behavior rather than trusting subjects.

Rules:
- Use existing tags for versions and their real dates. Do not invent versions
  or dates. Put untagged work under [Unreleased].
- Write each entry as one plain sentence for a user of the software. Group by
  Added, Changed, Deprecated, Removed, Fixed, Security.
- Skip refactors, test, CI and chore commits unless they affect users.
- Combine related commits into one entry. Mark breaking changes clearly.
- If history has no tags, create only [Unreleased] plus a summary of the last
  {{NUMBER_OF_COMMITS}} commits and tell me.
Add compare links at the bottom only if a remote URL exists.
