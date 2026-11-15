# Audit Agent Config

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Review the agent configuration files ({{CONFIG_FILES}}, for example settings,
hooks, MCP configuration, command and skill folders). Report: permissions that
are broader than the documented workflow needs; any way a secret file could be
read or printed; commands that can delete data or push to protected branches;
hooks or scripts that run untrusted input; MCP servers or external services
not listed in docs/configuration.md; secrets stored in these files. Do not edit. Include bypassable tool permissions and subprocess access limits;
give each finding a severity, evidence, safer alternative and human approval need.
