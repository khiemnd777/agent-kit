#!/usr/bin/env python3
"""Create a local manual reference; no upload or native integration is performed."""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = "docs/grok/agent-kit-reference.md"
# Explicit allowlist excludes project state, task history, delivery approvals,
# contract examples, native configuration and arbitrary newly added files.
POLICY = ["AGENTS.md", "docs/team-policy.md", "docs/team-workflow.md",
          "docs/execution/when.md", "docs/execution/delegation-policy.md",
          "docs/execution/evidence-policy.md", "docs/execution/use-cases.md",
          "docs/handoff-templates.md", "docs/skills-catalog.md", "docs/technote.md",
          "docs/roles/explorer.md", "docs/roles/implementer.md", "docs/roles/reviewer.md",
          "contracts/README.md", "LICENSE", ".agents/ADDY-AGENT-SKILLS-LICENSE"]


def sources(root: Path = ROOT) -> list[str]:
    result = list(POLICY)
    for folder in (".agents/skills", ".agents/references"):
        result.extend(path.relative_to(root).as_posix()
                      for path in sorted((root / folder).rglob("*.md")) if path.is_file())
    return result


def anchor(path: str) -> str:
    return "src-" + hashlib.sha256(path.encode()).hexdigest()[:16]


def render(root: Path = ROOT) -> str:
    paths = sources(root)
    mapping = {str((root / rel).resolve()): anchor(rel) for rel in paths}
    chunks = ["# Agent Kit V2 — manual reference\n\n"
              "Generated local reference; not a runtime, registered skill or permission grant.\n"
              "No Sidecar implementation is included. This file is not uploaded automatically.\n"
              "Native attachment/retrieval behavior: NOT_RUN.\n\n"
              "Relative links to embedded sources point inside this file; unavailable package\n"
              "references are labelled as package-only, not silently treated as attached.\n\n"]
    for rel in paths:
        path = root / rel
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("Unsafe export source")
        content = path.read_text(encoding="utf-8")
        digest = hashlib.sha256(content.encode()).hexdigest()

        def replace_link(match: re.Match[str]) -> str:
            label, target = match.group(1), match.group(2)
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                return match.group(0)
            filepart = target.split("#", 1)[0]
            resolved = str((path.parent / filepart).resolve())
            if resolved in mapping:
                return f"[{label}](#{mapping[resolved]})"
            return f"{label} (package reference: `{target}`)"

        content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, content)
        chunks.append(f'<a id="{anchor(rel)}"></a>\n\n## Source: `{rel}`\n\n'
                      f"SHA-256: `{digest}`\n\n" + content.strip() + "\n\n---\n\n")
    return "".join(chunks)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        wanted = render()
        output = ROOT / OUTPUT
        if args.check:
            if output.is_symlink() or not output.is_file() or output.read_text(encoding="utf-8") != wanted:
                print("FAIL: manual reference is missing/stale", file=sys.stderr)
                return 1
        else:
            if output.is_symlink() or not output.resolve().is_relative_to(ROOT):
                raise ValueError("Unsafe export destination")
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(wanted, encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("PASS: local manual reference matches current allowed sources; no upload")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
