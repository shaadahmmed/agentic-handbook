# Local setup

## Requirements

| Tool | Version | Check |
| --- | --- | --- |
| Node | 22.x | `node -v` |
| pnpm | 9.x | `pnpm -v` |
| Docker | 27.x | `docker -v` |

## Steps

1. `git clone ... && cd taskflow`
2. `cp .env.example .env` and fill values (see configuration.md)
3. `pnpm install`
4. `docker compose up -d db redis`
5. `pnpm db:migrate && pnpm db:seed`
6. `pnpm dev`

## Verify

Open http://localhost:3000. Log in as `demo@example.com` / `demo-password`.
Run `pnpm test`; all tests should pass.

## If something fails

- Port 5432 busy: stop your local PostgreSQL or change `DB_PORT` in `.env`.
- `pnpm install` fails on Node 20: use Node 22 (`nvm use`).
