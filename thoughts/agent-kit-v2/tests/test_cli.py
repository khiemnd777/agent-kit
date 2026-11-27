"""Execute maintenance CLIs only. No application commands, accounts or remote I/O."""
from __future__ import annotations
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def run_script(self, script, *args, no_site=False):
        command = [sys.executable]
        if no_site:
            command.append("-S")
        command += [str(ROOT / "scripts" / script), *map(str, args)]
        return subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                              timeout=30, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})

    def test_check_modes_succeed(self):
        for script in ("sync_assets.py", "export_grok.py"):
            with self.subTest(script=script):
                result = self.run_script(script, "--check")
                self.assertEqual(0, result.returncode, result.stderr)

    def test_contract_cli_returns_structured_scope_limits(self):
        result = self.run_script("check_contract.py", "--request",
            "contracts/examples/request-inventory.json", "--result",
            "contracts/examples/result-success.json", "--capability",
            "contracts/examples/capability-inventory.json")
        self.assertEqual(0, result.returncode, result.stderr)
        data = json.loads(result.stdout)
        self.assertTrue(data["valid"])
        self.assertFalse(data["execution_performed"])
        self.assertFalse(data["authority_verified"])

    def test_invalid_contract_exits_nonzero(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.json"
            path.write_text("{}")
            result = self.run_script("check_contract.py", "--request", path)
            self.assertEqual(1, result.returncode)
            self.assertFalse(json.loads(result.stdout)["valid"])

    def test_malformed_json_exits_without_success(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.json"
            path.write_text("{")
            result = self.run_script("check_contract.py", "--request", path)
            self.assertEqual(2, result.returncode)
            self.assertIn("NOT_VALIDATED", result.stderr)

    def test_missing_dependency_is_not_a_pass(self):
        result = self.run_script("check_contract.py", "--request",
            "contracts/examples/request-inventory.json", no_site=True)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("NOT_RUN", result.stderr)

    def test_package_cli_reports_real_static_status(self):
        result = self.run_script("verify_package.py")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("PASS", json.loads(result.stdout)["status"])


if __name__ == "__main__":
    unittest.main()
