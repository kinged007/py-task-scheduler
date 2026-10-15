# AGENTS.md — py-task-scheduler

Python background task scheduler with cron-like clock-boundary execution, YAML frontmatter task configs, per-task dependency isolation and SQLite tracking.

## How to work in this repo

- Default branch is `master`. Do not push directly to it. Create a feature branch and open a PR.
- Commit as `kinged007 <599286+kinged007@users.noreply.github.com>`.
- Keep changes focused; run checks before opening a PR.

## Checks

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pip install ruff mypy pytest pytest-cov
ruff check .
ruff format --check .
mypy task_scheduler helpers --ignore-missing-imports
pytest -v                          # full suite
pytest --cov=task_scheduler --cov-report=term-missing -v
python scripts/run_tests.py        # wrapper (same suite)
```

CI (`.github/workflows/ci.yml`) runs `ruff check`, `ruff format --check`, `mypy` and `pytest` on push/PR to `master` (Python 3.10–3.12).

## Repo layout

- `task_scheduler/` — core scheduler (decorators, database, memory manager, venv manager)
- `tasks/` — task files (`*.py` with YAML frontmatter); `example_*.py` enabled via `config/config.yaml: tasks.include_example_tasks`
- `helpers/` — reusable helpers (config_loader, task_logging, system_notifications, external_execution)
- `config/config.yaml` — scheduler config; task-specific configs live in `config/*.yaml`
- `scripts/` — install, cron setup, `reset_schedules.py`, `restart_scheduler.py`, `run_tests.py`, `check_overdue.py`
- `tests/` — pytest suite (`pytest.ini` defines markers `slow`/`integration`/`unit`)
- `main.py` — entry point (`--config` path, `--daemon`, `--status`)

See `README.md` for frontmatter reference, scheduling model and usage.

## Skills and tooling

- Use `ruff` for lint/format, `mypy` for type checks, `pytest` for tests. Do not add another formatter or runner.
- Keep helper dependencies declared in each task's YAML frontmatter; the scheduler installs them per-task.

## Permissions and scope

- No secrets in commits. `config/secrets.yaml` and `config/*_secrets.yaml` are gitignored; commit only `*.example` templates.
- Keep this repo self-contained. Do not copy private code without explicit owner approval.
- Do not delete, archive or change visibility of the repo without explicit approval.
