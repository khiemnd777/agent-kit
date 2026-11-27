#!/usr/bin/env python3
"""Check kit source/package consistency. No native agent or workload is executed."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
import tomllib
from urllib.parse import unquote

import check_contract
import export_grok
import sync_assets

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "docs/package-manifest.json"
# Output evidence is excluded to avoid a self-referential hash/report cycle.
EVIDENCE = {"docs/verification-results.md", "docs/delivery/checks.log",
            "docs/delivery/verification.json"}
IGNORED_PARTS = {".git", ".venv", "__pycache__", ".kit-work"}
SKILLS = {
    "api-and-interface-design", "code-review-and-quality", "code-simplification",
    "context-engineering", "debugging-and-error-recovery", "documentation-and-adrs",
    "frontend-ui-engineering", "incremental-implementation", "observability-and-instrumentation",
    "performance-optimization", "planning-and-task-breakdown", "security-and-hardening",
    "source-driven-development", "spec-driven-development", "technote",
    "test-driven-development", "using-agent-skills", "execution-delegation",
}


def maintained_files(root: Path = ROOT) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if set(rel.parts) & IGNORED_PARTS:
            continue
        if path.is_symlink():
            raise ValueError(f"Package symlink is unsupported: {rel}")
        if not path.is_file() or rel.as_posix() == MANIFEST or rel.as_posix() in EVIDENCE:
            continue
        if path.suffix in {".pyc", ".pyo"}:
            continue
        result[rel.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def update_manifest(root: Path = ROOT) -> None:
    path = root / MANIFEST
    if path.is_symlink():
        raise ValueError("Manifest must not be a symlink")
    document = {"schema_version": 1, "kit_version": (root / "VERSION").read_text().strip(),
                "purpose": "Accidental-drift inventory, not authentication or security proof",
                "excluded_evidence": sorted(EVIDENCE), "files": maintained_files(root)}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")


def manifest_errors(root: Path = ROOT) -> list[str]:
    path = root / MANIFEST
    if path.is_symlink() or not path.is_file():
        return ["Manifest missing or unsafe; do not claim integrity"]
    document = check_contract.load_json(path)
    if not isinstance(document, dict) or not isinstance(document.get("files"), dict):
        return ["Invalid maintained-file manifest"]
    if document.get("schema_version") != 1 or document.get("kit_version") != "2.0.0":
        return ["Manifest schema/version mismatch"]
    if document.get("excluded_evidence") != sorted(EVIDENCE):
        return ["Manifest evidence exclusions mismatch"]
    current = maintained_files(root)
    stored = document["files"]
    errors = []
    for rel in sorted(set(stored) | set(current)):
        if stored.get(rel) != current.get(rel):
            errors.append(f"Manifest mismatch: {rel}")
    return errors


def _without_fences(text: str) -> str:
    return re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", text,
                  flags=re.MULTILINE | re.DOTALL)


def anchors(text: str) -> set[str]:
    text = _without_fences(text)
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    counts: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, flags=re.MULTILINE):
        slug = re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        result.add(slug if count == 0 else f"{slug}-{count}")
        counts[slug] = count + 1
    return result


def link_errors(root: Path = ROOT) -> list[str]:
    errors = []
    for path in sorted(root.rglob("*.md")):
        if set(path.relative_to(root).parts) & IGNORED_PARTS:
            continue
        if path.is_symlink():
            errors.append("Unsafe Markdown symlink")
            continue
        text = _without_fences(path.read_text(encoding="utf-8"))
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = target.strip().split(' "', 1)[0]
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            filepart, _, fragment = target.partition("#")
            destination = path if not filepart else path.parent / unquote(filepart)
            if not destination.resolve().is_relative_to(root.resolve()):
                errors.append(f"Escaping local link in {path.relative_to(root)}")
            elif not destination.exists():
                errors.append(f"Broken link in {path.relative_to(root)}: {target}")
            elif fragment and destination.is_file() and destination.suffix == ".md":
                if unquote(fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"Broken anchor in {path.relative_to(root)}: {target}")
    return errors


def source_errors(root: Path = ROOT) -> list[str]:
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError("NOT_RUN: PyYAML unavailable; frontmatter checks did not run") from exc
    class UniqueKeyLoader(yaml.SafeLoader):
        pass

    def unique_mapping(loader, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in mapping:
                raise ValueError("Duplicate YAML metadata key")
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
    errors = []
    actual = {path.parent.name for path in (root / ".agents/skills").glob("*/SKILL.md")}
    if actual != SKILLS:
        errors.append("Canonical skill inventory differs from the 18 reviewed identities")
    for name in sorted(actual):
        path = root / ".agents/skills" / name / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f"Invalid frontmatter: {name}")
            continue
        front = yaml.load(parts[1], Loader=UniqueKeyLoader)
        if not isinstance(front, dict) or set(front) != {"name", "description"} or front.get("name") != name:
            errors.append(f"Unexpected skill metadata: {name}")
        elif not isinstance(front["description"], str) or not front["description"].strip():
            errors.append(f"Missing skill trigger description: {name}")
    for path in sorted((root / ".codex/agents").glob("*.toml")):
        doc = tomllib.loads(path.read_text(encoding="utf-8"))
        if set(doc) != {"name", "description", "developer_instructions"} or doc["name"] != path.stem:
            errors.append(f"Unexpected native adapter fields: {path.relative_to(root)}")
    for client in ("claude", "gemini", "cursor"):
        for path in sorted((root / f".{client}/agents").glob("*.md")):
            parts = path.read_text(encoding="utf-8").split("---", 2)
            doc = yaml.load(parts[1], Loader=UniqueKeyLoader) if len(parts) == 3 else None
            if not isinstance(doc, dict) or set(doc) != {"name", "description", "model"} or (
                    doc.get("name") != path.stem or doc.get("model") != "inherit"):
                errors.append(f"Unexpected native adapter fields: {path.relative_to(root)}")
    for client in ("CLAUDE.md", "GEMINI.md"):
        if (root / client).read_text(encoding="utf-8").strip() != "@AGENTS.md":
            errors.append(f"Shared core import drift: {client}")
    if (root / "VERSION").read_text().strip() != "2.0.0":
        errors.append("Unexpected kit version")
    for path in (root / "scripts").glob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    provenance = check_contract.load_json(root / "docs/source-provenance.json")
    if provenance["baseline"]["commit"] != "df3b058a52acc9ea10a7556733baae44ac12d1f2":
        errors.append("Source pin drift")
    if provenance["swamp_source_included"] is not False:
        errors.append("Unexpected Swamp-source inclusion claim")
    if len(provenance["skills"]) != 18:
        errors.append("Skill provenance count mismatch")
    for path, expected in (("LICENSE", "8dcb6505c15c7b1ae6e51702dcf82174b07fa7fc"),
                           (".agents/ADDY-AGENT-SKILLS-LICENSE", "d67778ada6b9cda6227e9130da182c13e73c8b2e")):
        data = (root / path).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if blob != expected:
            errors.append(f"Inherited license notice changed: {path}")
    for path in ("docs/project-context.md", "docs/project-plan.md", "docs/project-state.md"):
        if "UNINITIALIZED" not in (root / path).read_text(encoding="utf-8"):
            errors.append(f"Fresh adopter record state missing: {path}")
    return errors


def contract_errors(root: Path = ROOT) -> list[str]:
    errors = []
    for path in sorted((root / "contracts").glob("*.schema.json")):
        errors.extend(f"{path.name}: {error}" for error in
                      check_contract.validate_schema_document(check_contract.load_json(path)))
    base = root / "contracts/examples"
    req = check_contract.load_json(base / "request-inventory.json")
    cap = check_contract.load_json(base / "capability-inventory.json")
    errors.extend(check_contract.request_errors(req, cap, root))
    for path in sorted(base.glob("result-*.json")):
        errors.extend(f"{path.name}: {error}" for error in
                      check_contract.result_errors(req, check_contract.load_json(path), cap, root))
    return errors


def verify(root: Path = ROOT) -> dict[str, object]:
    checks: dict[str, list[str]] = {}
    for name, function in (("inventory", manifest_errors), ("mirrors_and_adapters", sync_assets.check_assets),
                           ("source_formats_and_licenses", source_errors), ("local_links", link_errors),
                           ("draft_contracts", contract_errors)):
        try:
            checks[name] = function(root)
        except Exception as exc:
            checks[name] = [f"NOT_VALIDATED: {type(exc).__name__}: {exc}"]
    try:
        output = root / export_grok.OUTPUT
        checks["manual_export"] = [] if output.is_file() and not output.is_symlink() and (
            output.read_text(encoding="utf-8") == export_grok.render(root)) else ["Missing/stale manual export"]
    except Exception as exc:
        checks["manual_export"] = [f"NOT_VALIDATED: {type(exc).__name__}: {exc}"]
    return {"status": "PASS" if not any(checks.values()) else "FAIL",
            "scope": "source/package checks only", "checks": checks,
            "native_clients": "NOT_RUN", "sidecar_interoperability": "NOT_RUN",
            "token_benchmark": "NOT_RUN"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update-manifest", action="store_true",
                        help="Record current reviewed files; does not establish review or authority")
    args = parser.parse_args(argv)
    try:
        if args.update_manifest:
            update_manifest()
        report = verify()
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
