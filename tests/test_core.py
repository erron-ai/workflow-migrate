"""Tests for workflow_migrate."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest

from workflow_migrate.core import analyze_records


class AnalyzeRecordsTests(unittest.TestCase):
    def test_analyze_records_computes_structured_result(self) -> None:
        # Arrange
        records = [
            {"a": 10, "b": "x"},
            {"a": 20, "b": "y", "c": 3},
            {"a": 15, "b": "z"},
        ]
        # Act
        result = analyze_records(records)
        # Assert
        self.assertEqual(result.item_count, 3)
        self.assertGreaterEqual(result.score, 0.0)
        self.assertLessEqual(result.score, 1.0)
        self.assertIn("summary", result.__dict__)
        self.assertIn("coverage", result.signals)

    def test_analyze_records_rejects_empty_records(self) -> None:
        with self.assertRaises(ValueError):
            analyze_records([])

    def test_summary_contains_repo_purpose(self) -> None:
        records = [{"value": 1}, {"value": 2}]
        result = analyze_records(records)
        self.assertTrue(result.summary)
        self.assertIn("result for:", result.summary)


class CliTests(unittest.TestCase):
    def test_cli_emits_valid_json(self) -> None:
        cmd = [
            sys.executable,
            "-m",
            "workflow_migrate.cli",
            "--json",
        ]
        process = subprocess.run(cmd, text=True, capture_output=True, check=True)
        payload = json.loads(process.stdout.strip())
        self.assertIn("score", payload)
        self.assertIn("signals", payload)
        self.assertIn("summary", payload)


if __name__ == "__main__":
    unittest.main()
