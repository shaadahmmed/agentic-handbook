# Write Api

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Write docs/api.md as a human guide on top of the machine readable contract.
If an OpenAPI or GraphQL schema exists, link it as the source of truth and do
not duplicate endpoints. Document: base URL pattern, authentication,
versioning policy, error format (from real error handling code), pagination,
rate limits if configured, and 3 representative request and response examples
taken from tests or fixtures. If no schema exists, propose creating one and list
the routes you found in a table (method, path, auth, purpose).
