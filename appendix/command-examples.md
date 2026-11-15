# Stack command suggestions (from V3)

These examples are **unverified for your repository** and are reference text, not instructions to install dependencies or execute commands. The project's actual scripts/configurations own command syntax. No commands were executed for this handbook revision.

## Illustrative commands by stack

Use these to fill the command placeholders when you are unsure. They are common defaults, not facts about your project.

| Stack | Install | Lint and format | Type check | Test | Build |
| --- | --- | --- | --- | --- | --- |
| Node and TypeScript | `pnpm install` | `pnpm lint` | `pnpm tsc --noEmit` | `pnpm test` | `pnpm build` |
| Python | `uv sync` or `pip install -e .[dev]` | `ruff check .` and `ruff format --check .` | `mypy .` or `pyright` | `pytest` | `python -m build` |
| Go | `go mod download` | `golangci-lint run` | `go vet ./...` | `go test ./...` | `go build ./...` |
| Rust | `cargo fetch` | `cargo clippy -- -D warnings` | `cargo check` | `cargo test` | `cargo build --release` |
| Java (Gradle) | `./gradlew dependencies` | `./gradlew spotlessCheck` | compiler | `./gradlew test` | `./gradlew build` |
| .NET | `dotnet restore` | `dotnet format --verify-no-changes` | `dotnet build` | `dotnet test` | `dotnet publish` |
| Ruby on Rails | `bundle install` | `bundle exec rubocop` | optional (Sorbet) | `bundle exec rspec` | not applicable |


[Return to shared prompt variables](../prompts/README.md#variable-reference).
