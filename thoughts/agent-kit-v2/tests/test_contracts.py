"""Offline semantic regression tests; none represents a Sidecar execution."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_contract as c


class ContractTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / "contracts/examples"
        self.request = c.load_json(base / "request-inventory.json")
        self.result = c.load_json(base / "result-success.json")
        self.capability = c.load_json(base / "capability-inventory.json")

    def errors(self):
        return c.result_errors(self.request, self.result, self.capability)

    def refresh_digest(self):
        self.result["request_digest"] = c.canonical_digest(self.request)

    def test_all_synthetic_terminal_examples_are_consistent(self):
        for path in (ROOT / "contracts/examples").glob("result-*.json"):
            with self.subTest(path=path.name):
                self.assertEqual([], c.result_errors(self.request, c.load_json(path), self.capability))

    def test_all_schemas_are_well_formed(self):
        for path in (ROOT / "contracts").glob("*.schema.json"):
            with self.subTest(path=path.name):
                self.assertEqual([], c.validate_schema_document(c.load_json(path)))

    def test_request_alone_is_valid_design_not_authority(self):
        self.assertEqual([], c.request_errors(self.request, self.capability))
        self.assertEqual("draft", self.capability["lifecycle"])
        self.assertTrue(self.request["authorization"]["decision_ref"].startswith("example://"))

    def test_required_not_run_is_not_success(self):
        self.result["checks"][0].update(status="NOT_RUN", evidence_ids=[], detail="Tool unavailable")
        self.assertTrue(any("required check must PASS" in x for x in self.errors()))

    def test_required_skipped_is_not_success(self):
        self.result["checks"][0].update(status="SKIPPED", evidence_ids=[], detail="Not applicable was claimed")
        self.assertTrue(self.errors())

    def test_fail_cannot_be_greenwashed(self):
        self.result["checks"][0]["status"] = "FAIL"
        self.assertTrue(any("failed check" in x for x in self.errors()))

    def test_missing_check_is_not_success(self):
        self.result["checks"].pop()
        self.assertTrue(any("exactly the requested" in x for x in self.errors()))

    def test_unknown_check_is_rejected(self):
        self.result["checks"][0]["id"] = "unrequested"
        self.assertTrue(self.errors())

    def test_duplicate_result_check_is_rejected(self):
        self.result["checks"].append(copy.deepcopy(self.result["checks"][0]))
        self.assertTrue(any("Duplicate result" in x for x in self.errors()))

    def test_duplicate_requested_check_is_rejected(self):
        self.request["checks"].append(copy.deepcopy(self.request["checks"][0]))
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_no_required_acceptance_check_is_rejected(self):
        for check in self.request["checks"]:
            check["required"] = False
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_correlation_mismatch_is_rejected(self):
        self.result["request_id"] = "req-some-other-intent"
        self.assertTrue(any("request_id" in x for x in self.errors()))

    def test_workflow_version_and_digest_are_pinned(self):
        for key, value in (("version", "other-version"), ("digest", "sha256:" + "f" * 64)):
            with self.subTest(key=key):
                changed = copy.deepcopy(self.result)
                changed["capability"][key] = value
                self.assertTrue(c.result_errors(self.request, changed, self.capability))

    def test_source_environment_and_policy_mismatch_are_rejected(self):
        for key in ("snapshot", "environment_digest", "policy_digest"):
            with self.subTest(key=key):
                changed = copy.deepcopy(self.result)
                if key == "snapshot":
                    changed["target"][key]["value"] = "sha256:" + "f" * 64
                else:
                    changed["target"][key] = "sha256:" + "f" * 64
                self.assertTrue(c.result_errors(self.request, changed, self.capability))

    def test_changed_inputs_invalidate_digest(self):
        self.request["inputs"]["include"].append("untracked-change")
        self.assertTrue(any("request_digest" in x for x in self.errors()))

    def test_malformed_git_and_content_snapshots_are_rejected(self):
        for kind, value in (("git_commit", "HEAD"), ("content_digest", "abc123"),
                            ("git_commit", "sha256:" + "b" * 64)):
            with self.subTest(kind=kind, value=value):
                changed = copy.deepcopy(self.request)
                changed["target"]["snapshot"] = {"kind": kind, "value": value}
                self.assertTrue(c.request_errors(changed, self.capability))

    def test_success_needs_observed_run(self):
        for key in ("run_id", "started_at"):
            with self.subTest(key=key):
                changed = copy.deepcopy(self.result)
                changed[key] = None
                self.assertTrue(c.result_errors(self.request, changed, self.capability))

    def test_no_automatic_human_acceptance_field(self):
        self.result["human_accepted"] = True
        self.assertTrue(self.errors())

    def test_unknown_top_level_request_field(self):
        self.request["auto_approve"] = True
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_missing_artifact_and_unknown_reference_are_rejected(self):
        self.result["artifacts"] = []
        self.assertTrue(any("undeclared artifact" in x for x in self.errors()))

    def test_pass_without_evidence_is_rejected(self):
        self.result["checks"][0]["evidence_ids"] = []
        self.assertTrue(any("needs evidence" in x for x in self.errors()))

    def test_duplicate_artifacts_are_rejected(self):
        self.result["artifacts"].append(copy.deepcopy(self.result["artifacts"][0]))
        self.assertTrue(any("must be unique" in x for x in self.errors()))

    def test_traversal_absolute_and_encoded_artifact_paths_are_rejected(self):
        for path in ("../secret", "reports/../../secret", "/etc/secret", "C:\\secret",
                     "reports//file", "reports/./file", "reports/%2e%2e/file", "reports/file/"):
            with self.subTest(path=path):
                changed = copy.deepcopy(self.result)
                changed["artifacts"][0]["relative_path"] = path
                self.assertTrue(c.result_errors(self.request, changed, self.capability))

    def test_authorization_paths_are_logical_and_contained(self):
        for path in ("/tmp/source", "source:/../secret", "scratch:/x/../../secret", "source:/x//y"):
            with self.subTest(path=path):
                changed = copy.deepcopy(self.request)
                changed["authorization"]["allowed_paths"] = [path]
                self.assertTrue(c.request_errors(changed, self.capability))

    def test_extra_capability_side_effects_are_rejected(self):
        self.capability["effects"].append("write_source")
        self.assertTrue(any("exceed" in x for x in c.request_errors(self.request, self.capability)))

    def test_network_effect_needs_allowlisted_hosts(self):
        self.request["authorization"]["allowed_effects"].append("network")
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_hosts_without_network_effect_are_rejected(self):
        self.request["authorization"]["network_hosts"] = ["example.com"]
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_unsupported_production_effect_is_rejected(self):
        self.request["authorization"]["allowed_effects"].append("deploy_production")
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_unknown_capability_input_is_rejected(self):
        self.request["inputs"]["run_command"] = "not-an-authorized-input"
        self.assertTrue(any("inputs:" in x for x in c.request_errors(self.request, self.capability)))

    def test_open_capability_input_schema_is_rejected(self):
        self.capability["input_schema"] = {}
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_reviewed_descriptor_needs_review_reference(self):
        self.capability["lifecycle"] = "reviewed"
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_non_safe_replay_cannot_request_automatic_attempts(self):
        self.capability["replay_policy"] = "requires_reconciliation"
        self.request["limits"]["max_attempts"] = 2
        self.assertTrue(c.request_errors(self.request, self.capability))

    def test_result_cannot_exceed_attempts(self):
        self.result["metrics"]["attempts"] = 2
        self.assertTrue(any("Attempt count" in x for x in self.errors()))

    def test_success_cannot_exceed_time_budget(self):
        self.result["metrics"]["duration_seconds"] = 121
        self.assertTrue(any("duration" in x for x in self.errors()))

    def test_summary_budget_is_utf8_bytes_not_characters(self):
        self.request["limits"]["max_summary_bytes"] = 128
        self.refresh_digest()
        self.result["summary"] = "đ" * 100
        self.assertTrue(any("UTF-8 byte" in x for x in self.errors()))

    def test_artifact_budget_is_enforced(self):
        self.result["artifacts"][0]["size_bytes"] = self.request["limits"]["max_evidence_bytes"] + 1
        self.assertTrue(any("evidence exceeds" in x for x in self.errors()))

    def test_time_cannot_run_backwards(self):
        self.result["finished_at"] = "2026-11-17T01:59:00Z"
        self.assertTrue(any("earlier" in x for x in self.errors()))

    def test_unknown_usage_needs_reason(self):
        self.result["metrics"]["usage"]["unavailable_reason"] = None
        self.assertTrue(any("Unavailable usage" in x for x in self.errors()))

    def test_zero_usage_is_a_measurement_needing_provenance(self):
        self.result["metrics"]["usage"]["input_tokens"] = 0
        self.assertTrue(any("including zero" in x for x in self.errors()))

    def test_measured_zero_with_provenance_and_unknown_other_counts_is_valid(self):
        self.result["metrics"]["usage"].update(input_tokens=0, source="example counter")
        self.assertEqual([], self.errors())

    def test_success_cannot_have_unknown_effects(self):
        self.result["effects_state"] = "unknown"
        self.assertTrue(self.errors())

    def test_non_success_needs_reason(self):
        self.result["status"] = "failed"
        self.assertTrue(any("Non-success" in x for x in self.errors()))

    def test_unknown_effects_need_reconciliation(self):
        self.result = c.load_json(ROOT / "contracts/examples/result-timed-out.json")
        self.result["exceptions"][0]["next_action"] = "reason"
        self.assertTrue(any("reconciliation" in x for x in self.errors()))

    def test_unknown_exception_check_is_rejected(self):
        self.result = c.load_json(ROOT / "contracts/examples/result-failed.json")
        self.result["exceptions"][0]["related_check"] = "other-check"
        self.assertTrue(self.errors())

    def test_whitespace_check_reason_is_rejected(self):
        self.result["checks"][0]["detail"] = "   "
        self.assertTrue(self.errors())

    def test_canonical_digest_does_not_depend_on_key_insertion_order(self):
        self.assertEqual(c.canonical_digest({"b": 1, "a": 2}), c.canonical_digest({"a": 2, "b": 1}))

    def test_remote_schema_reference_is_rejected_without_network(self):
        with mock.patch("socket.socket", side_effect=AssertionError("Network forbidden")):
            self.assertTrue(c.validate_with_schema({"$ref": "https://example.com/private"}, {}))

    def test_duplicate_json_keys_and_nonfinite_values_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            for value in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}', '{"a":1e400}'):
                with self.subTest(value=value):
                    path.write_text(value)
                    with self.assertRaises(ValueError):
                        c.load_json(path)

    def test_json_input_size_and_nesting_are_bounded(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_bytes(b" " * (c.MAX_DOCUMENT_BYTES + 1))
            with self.assertRaises(ValueError):
                c.load_json(path)
            path.write_text("[" * 70 + "0" + "]" * 70)
            with self.assertRaises(ValueError):
                c.load_json(path)

    def test_bad_shape_is_an_error_not_a_crash(self):
        for value in (None, [], "invalid", 1, {}, {"kind": "execution_result"}):
            with self.subTest(value=value):
                self.assertTrue(c.result_errors(self.request, value, self.capability))


if __name__ == "__main__":
    unittest.main()
