## Alert: API error rate above 5 percent for 5 minutes

1. Check the latest deploy: `gh run list --workflow deploy -L 3`.
2. If a recent deploy correlates with the incident, assess rollback safety and
   obtain the incident commander’s authorization before any production rollback.
   Example command, **do not run without checking deployment target**: `pnpm deploy:rollback`.
3. If not, check database health in the dashboard (connections, CPU).
4. Post status in #incidents. Escalate to the on call lead after 15 minutes.
