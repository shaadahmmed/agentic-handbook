# Changelog

All notable changes to this project are documented here.
Format: Keep a Changelog. Versioning: Semantic Versioning.

## [Unreleased]

### Added
- Export a task list to CSV from the list menu.

### Fixed
- Sync no longer duplicates task records when devices reconnect; same-field values still follow LWW conflict handling.

## [1.4.0] - 2026-11-02

### Added
- Webhooks for task created, updated and completed events.
- `GET /v1/workspaces/{id}/members` endpoint.

### Changed
- Default page size for list endpoints is now 50 (was 20).

### Deprecated
- `GET /v1/tasks/all` is deprecated. Use `GET /v1/tasks` with pagination.
  It will be removed in 2.0.0.

### Security
- Upgraded the session library to address a token reuse issue (fictional example; link a real advisory in a real changelog).

## [1.3.1] - 2026-10-14

### Fixed
- Login failed for email addresses containing a plus sign.

[Unreleased]: https://github.com/example/taskflow/compare/v1.4.0...HEAD
[1.4.0]: https://github.com/example/taskflow/compare/v1.3.1...v1.4.0
[1.3.1]: https://github.com/example/taskflow/releases/tag/v1.3.1
