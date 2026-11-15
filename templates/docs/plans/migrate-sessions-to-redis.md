# Plan: migrate sessions to Redis

Goal: replace in-memory sessions so the API can run on several instances.

- [x] Add Redis service to docker-compose
- [x] Create SessionStore interface and in-memory implementation
- [ ] Implement RedisSessionStore with tests
- [ ] Switch config flag SESSION_STORE=redis in staging
- [ ] Remove in-memory store after one release

Decisions:
- Session TTL stays 7 days (matches current behavior).

Notes for next session:
- Redis tests need `docker compose up -d redis`.
