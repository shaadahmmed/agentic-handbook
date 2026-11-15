# TaskFlow

A self-hosted task manager for small teams with offline-first sync.

Status: beta. Used in production by the authors; APIs may change before 1.0.

## Why TaskFlow

Most task tools need a constant connection and lock your data in a vendor.
TaskFlow stores everything locally first and syncs when a network is available.

## Features

- Offline-first task lists with per-field last-writer-wins sync (conflicts can discard one value)
- Team workspaces with role based access
- REST API and webhooks

## Tech stack

TypeScript, Node 22, PostgreSQL 16, React 19, pnpm workspaces.

## Quick start

Prerequisites: Node 22, pnpm 9, Docker 27.

```bash
git clone https://github.com/example/taskflow.git
cd taskflow
cp .env.example .env        # then fill in the values, see docs/configuration.md
pnpm install
docker compose up -d db     # starts PostgreSQL
pnpm dev                    # app on http://localhost:3000
pnpm test                   # run the test suite
```

## Documentation

- Setup details: docs/setup.md
- Architecture: docs/architecture.md
- Testing: docs/testing.md
- Roadmap: docs/roadmap.md
- Contributing: CONTRIBUTING.md
- Security policy: SECURITY.md

## License

MIT, see LICENSE.
