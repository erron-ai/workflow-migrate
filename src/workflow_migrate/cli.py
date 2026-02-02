"""CLI for workflow_migrate."""

from __future__ import annotations

import argparse
import json

from .core import analyze_records


SAMPLE_RECORDS = [
    {"name": "alpha", "value": 14, "status": "ok"},
    {"name": "beta", "value": 22, "status": "ok"},
    {"name": "gamma", "value": 5, "status": "review"},
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="workflow-migrate",
        description="Run a baseline analysis for this repository's core use case.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = analyze_records(SAMPLE_RECORDS)
    payload = {
        "item_count": result.item_count,
        "score": result.score,
        "summary": result.summary,
        "signals": result.signals,
    }
    if args.json:
        print(json.dumps(payload, sort_keys=True))
        return
    print("Result:", payload["summary"])
    print("Score:", payload["score"])
    print("Signals:", payload["signals"])


if __name__ == "__main__":
    main()
