# Write Config

Use the [shared eight-line contract](README.md#shared-rules) and [project brief](project-brief.md). Risk, test and evidence definitions remain in their linked authoritative references.

Find every environment variable and configuration key the code reads (search
for process.env, os.environ, config loaders, docker-compose and CI files;
adapt to {{LANGUAGES}}). Do not open real .env files.

Produce:
1. .env.example with every variable, a harmless placeholder value, and a
   comment on how to generate secrets where relevant.
2. docs/configuration.md with a table: Variable, Required, Default, Description,
   Where it is read (file path). Mark unknown meanings [VERIFY].
3. A list of variables used in code but missing from existing example files,
   and the reverse.
Never write real secrets. Use obviously fake values.
