"""Mutate disposable package copies to check actual maintenance failure paths."""
from __future__ import annotations
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import export_grok
import sync_assets
import verify_package


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "kit"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv", ".kit-work"))
        verify_package.update_manifest(self.root)

    def test_complete_package_checks_pass(self):
        self.assertEqual("PASS", verify_package.verify(self.root)["status"])

    def test_changed_source_is_detected(self):
        with (self.root / "AGENTS.md").open("a") as stream:
            stream.write("\nUnexpected change.\n")
        self.assertTrue(verify_package.manifest_errors(self.root))

    def test_added_and_missing_files_are_detected(self):
        (self.root / "unexpected.txt").write_text("extra")
        (self.root / "VERSION").unlink()
        errors = verify_package.manifest_errors(self.root)
        self.assertTrue(any("unexpected.txt" in e for e in errors))
        self.assertTrue(any("VERSION" in e for e in errors))

    def test_mirror_drift_is_detected(self):
        path = self.root / ".claude/skills/execution-delegation/SKILL.md"
        path.write_text("different")
        self.assertTrue(sync_assets.check_assets(self.root))

    def test_sync_restores_reviewed_generated_content(self):
        path = self.root / ".claude/skills/execution-delegation/SKILL.md"
        path.write_text("different")
        sync_assets.sync(self.root)
        self.assertEqual([], sync_assets.check_assets(self.root))

    def test_extra_generated_file_is_not_silently_deleted(self):
        path = self.root / ".claude/skills/extra/SKILL.md"
        path.parent.mkdir()
        path.write_text("user content")
        sync_assets.sync(self.root)
        self.assertTrue(path.exists())
        self.assertTrue(any("Unexpected" in e for e in sync_assets.check_assets(self.root)))

    def test_duplicate_or_path_shaped_role_name_is_rejected(self):
        path = self.root / "config/roles.json"
        roles = json.loads(path.read_text())
        roles[0]["name"] = "../../bad"
        path.write_text(json.dumps(roles))
        with self.assertRaises(ValueError):
            sync_assets.expected_assets(self.root)

    def test_symlink_source_and_destination_are_rejected(self):
        source = self.root / ".agents/references/symlink.md"
        source.symlink_to(self.root / "README.md")
        with self.assertRaises(ValueError):
            verify_package.maintained_files(self.root)
        with self.assertRaises(ValueError):
            sync_assets.expected_assets(self.root)
        source.unlink()
        destination = self.root / ".claude/skills/execution-delegation/SKILL.md"
        destination.unlink()
        destination.symlink_to(self.root / "AGENTS.md")
        with self.assertRaises(ValueError):
            sync_assets.sync(self.root)

    def test_symlinked_parent_directory_is_rejected_even_inside_package(self):
        destination = self.root / ".claude/skills"
        shutil.rmtree(destination)
        destination.symlink_to(self.root / ".agents/skills", target_is_directory=True)
        with self.assertRaises(ValueError):
            sync_assets.sync(self.root)
        with self.assertRaises(ValueError):
            sync_assets.check_assets(self.root)

    def test_symlinked_canonical_directory_is_rejected(self):
        source = self.root / ".agents/references"
        shutil.rmtree(source)
        source.symlink_to(self.root / "docs", target_is_directory=True)
        with self.assertRaises(ValueError):
            sync_assets.expected_assets(self.root)

    def test_broken_link_and_anchor_are_detected(self):
        path = self.root / "docs/broken.md"
        path.write_text("[missing](absent.md)\n[anchor](../AGENTS.md#no-such-heading)\n")
        errors = verify_package.link_errors(self.root)
        self.assertTrue(any("Broken link" in e for e in errors))
        self.assertTrue(any("Broken anchor" in e for e in errors))

    def test_document_code_samples_are_not_links_to_fetch(self):
        path = self.root / "docs/sample.md"
        path.write_text("```text\n[not-a-real-link](missing.md)\n```\n")
        self.assertEqual([], verify_package.link_errors(self.root))

    def test_duplicate_frontmatter_keys_fail_validation(self):
        path = self.root / ".agents/skills/execution-delegation/SKILL.md"
        path.write_text(path.read_text().replace("name: execution-delegation", "name: bad\nname: execution-delegation", 1))
        with self.assertRaises(ValueError):
            verify_package.source_errors(self.root)

    def test_unsupported_native_permission_override_is_detected(self):
        path = self.root / ".codex/agents/kit-implementer.toml"
        with path.open("a") as stream:
            stream.write('sandbox_mode = "danger-full-access"\n')
        self.assertTrue(verify_package.source_errors(self.root))

    def test_license_notice_modification_is_detected(self):
        path = self.root / "LICENSE"
        path.write_text("different notice")
        self.assertTrue(any("license" in e for e in verify_package.source_errors(self.root)))

    def test_adopter_records_do_not_inherit_acceptance(self):
        path = self.root / "docs/project-state.md"
        path.write_text("# State\nAccepted and released\n")
        self.assertTrue(any("Fresh adopter" in e for e in verify_package.source_errors(self.root)))

    def test_export_is_deterministic_and_includes_notices(self):
        first = export_grok.render(self.root)
        self.assertEqual(first, export_grok.render(self.root))
        self.assertIn("Copyright (c) 2025 Addy Osmani", first)
        self.assertIn("Copyright (c) 2026 agent-kit contributors", first)
        self.assertIn("SHA-256:", first)

    def test_export_excludes_project_approvals_and_contract_fixtures(self):
        self.assertNotIn("docs/project-state.md", export_grok.sources(self.root))
        self.assertNotIn("docs/delivery/V2-BUILD.md", export_grok.sources(self.root))
        self.assertFalse(any("contracts/examples/" in x for x in export_grok.sources(self.root)))
        path = self.root / "docs/project-state.md"
        path.write_text("UNINITIALIZED\nPRIVATE_STATE_MARKER\n")
        self.assertNotIn("PRIVATE_STATE_MARKER", export_grok.render(self.root))

    def test_new_unlisted_document_is_not_automatically_exported(self):
        (self.root / "docs/private.md").write_text("PRIVATE_UNLISTED_MARKER")
        self.assertNotIn("PRIVATE_UNLISTED_MARKER", export_grok.render(self.root))

    def test_output_evidence_does_not_create_manifest_recursion(self):
        path = self.root / "docs/verification-results.md"
        path.write_text("Updated actual evidence")
        self.assertEqual([], verify_package.manifest_errors(self.root))

    def test_observed_package_checks_do_not_claim_native_or_token_results(self):
        report = verify_package.verify(self.root)
        for field in ("native_clients", "sidecar_interoperability", "token_benchmark"):
            self.assertEqual("NOT_RUN", report[field])


if __name__ == "__main__":
    unittest.main()
