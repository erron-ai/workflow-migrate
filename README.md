# workflow-migrate

CLI to convert RPA workflows into agent architectures.

Built by [Erron AI](https://erron.ai).

## Why this exists
- Solve a concrete business problem with a practical, extensible baseline.
- Provide a tested implementation that teams can adapt quickly.
- Ship with professional repository standards and automation.

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python -m workflow_migrate.cli --help
python -m unittest discover -s tests -v
```

## Project structure
- `src/workflow_migrate/`: production code
- `tests/`: unit/integration-oriented tests
- `.github/`: CI and collaboration templates
- `AGENT.md`: contributor and agent workflow guide

## Release readiness
- MIT licensed
- CI test workflow
- PyPI metadata in `pyproject.toml`
- Homebrew install notes for CLI usage

## Status
This repository is initialized as part of the Erron AI multi-repo launch and is intentionally production-minded while remaining extensible for deeper roadmap features.

## Company and Contact
- Built and maintained by [Erron AI](https://erron.ai).
- Contact: [info@erron.ai](mailto:info@erron.ai)
