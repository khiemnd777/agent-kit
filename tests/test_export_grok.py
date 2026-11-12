"""Regression checks for the local reference exporter; no client/account needed."""

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "export_grok", Path(__file__).resolve().parents[1] / "scripts/export_grok.py"
)
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


class ExportTests(unittest.TestCase):
    def test_portable_links_preserve_commands_and_rebase_references(self):
        text = "[core](../../AGENTS.md#section)\n[missing](missing.md)\n[web](https://example.com)\n```md\n[example](example.md)\n```\n"
        result = exporter.portable_links(text, "docs/roles/explorer.md", {"AGENTS.md": b""})
        self.assertIn(f"[core](#{exporter.anchor('AGENTS.md')})", result)
        self.assertIn("`docs/roles/missing.md`; external to this reference", result)
        self.assertIn("[web](https://example.com)", result)
        self.assertIn("```md\n[example](example.md)\n```", result)

    def test_freshness_detects_source_edit_without_git_commit(self):
        content = exporter.sources()
        script = exporter.read_source("scripts/export_grok.py")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative, data in {**content, "scripts/export_grok.py": script}.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            output = root / "docs/grok/agent-kit-reference.md"
            with patch.object(exporter, "ROOT", root), patch.object(exporter, "OUTPUT", output), contextlib.redirect_stdout(io.StringIO()):
                with patch.object(sys, "argv", ["export_grok.py"]):
                    exporter.main()
                before = output.read_bytes()
                with patch.object(sys, "argv", ["export_grok.py", "--check"]):
                    exporter.main()
                    (root / "AGENTS.md").write_text("# Changed policy\n")
                    with self.assertRaisesRegex(SystemExit, "STALE"):
                        exporter.main()
                self.assertEqual(before, output.read_bytes(), "--check must never repair stale output")

    def test_export_includes_licenses_and_skills_but_excludes_live_history(self):
        content = exporter.sources()
        self.assertEqual(17, sum(p.endswith("SKILL.md") for p in content))
        self.assertIn("LICENSE", content)
        self.assertIn(".agents/ADDY-AGENT-SKILLS-LICENSE", content)
        self.assertNotIn("docs/project-state.md", content)
        self.assertFalse(any(p.startswith("docs/tasks/") and p != "docs/tasks/README.md" for p in content))
        self.assertFalse(any("/records/" in p for p in content))
        rendered = exporter.render()
        self.assertEqual(rendered, exporter.render(), "same inputs must produce identical bytes")
        self.assertNotIn("TASK-009 HUMAN ACCEPTED", rendered)
        self.assertNotIn("TASK-001 through TASK-007 describe historical", rendered)
        for path, data in content.items():
            self.assertIn(exporter.hashlib.sha256(data).hexdigest(), rendered)
            self.assertIn(f'id="{exporter.anchor(path)}"', rendered)

    def test_symlink_source_outside_root_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as external:
            root = Path(directory)
            target = Path(external) / "private.txt"
            target.write_text("not for export")
            (root / "AGENTS.md").symlink_to(target)
            with patch.object(exporter, "ROOT", root):
                with self.assertRaisesRegex(ValueError, "Unsafe source"):
                    exporter.read_source("AGENTS.md")


if __name__ == "__main__":
    unittest.main()
