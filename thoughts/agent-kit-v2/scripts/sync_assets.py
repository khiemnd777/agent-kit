#!/usr/bin/env python3
"""Generate repository-local mirrors and optional role adapters, never install them."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def contained_path(root: Path, path: Path) -> Path:
    """Reject symlinked ancestors as well as final components before reading/writing."""
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise ValueError("Path is outside package") from exc
    if ".." in relative.parts or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("Path escapes package")
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError("Symlinked source/destination component is unsupported")
    return path


def expected_assets(root: Path = ROOT) -> dict[str, bytes]:
    assets: dict[str, bytes] = {}
    for directory in ("skills", "references"):
        base = contained_path(root, root / ".agents" / directory)
        if not base.is_dir():
            raise ValueError("Missing canonical source directory")
        for path in sorted(base.rglob("*")):
            if path.is_symlink():
                raise ValueError("Canonical sources must not be symlinks")
            if path.is_file():
                contained_path(root, path)
                rel = path.relative_to(root / ".agents")
                assets[(Path(".claude") / rel).as_posix()] = path.read_bytes()
    assets[".claude/ADDY-AGENT-SKILLS-LICENSE"] = contained_path(root, root / ".agents/ADDY-AGENT-SKILLS-LICENSE").read_bytes()
    roles = json.loads(contained_path(root, root / "config/roles.json").read_text(encoding="utf-8"))
    if not isinstance(roles, list) or len(roles) != 3 or {r.get("name") for r in roles if isinstance(r, dict)} != {"kit-explorer", "kit-implementer", "kit-reviewer"}:
        raise ValueError("Expected the three unique reviewed role identities")
    for role in roles:
        source = contained_path(root, root / role["source"])
        if source.is_symlink() or not source.resolve().is_relative_to(root.resolve()):
            raise ValueError("Unsafe canonical role path")
        body = source.read_text(encoding="utf-8").split("\n", 1)[1].strip() + "\n"
        name, desc = role["name"], role["description"]
        if not isinstance(name, str) or not re.fullmatch(r"kit-[a-z][a-z0-9-]{0,40}", name):
            raise ValueError("Invalid role name for a generated filename")
        # JSON string syntax is valid for these TOML/YAML basic string fields.
        codex = (f'name = {json.dumps(name)}\ndescription = {json.dumps(desc)}\n'
                 f'developer_instructions = {json.dumps(body, ensure_ascii=False)}\n')
        assets[f".codex/agents/{name}.toml"] = codex.encode()
        markdown = ("---\nname: " + name + "\ndescription: " + json.dumps(desc) +
                    "\nmodel: inherit\n---\n\n" + body)
        for client in ("claude", "gemini", "cursor"):
            assets[f".{client}/agents/{name}.md"] = markdown.encode()
    return assets


def check_assets(root: Path = ROOT) -> list[str]:
    expected = expected_assets(root)
    errors = []
    for rel, data in expected.items():
        path = contained_path(root, root / rel)
        if path.is_symlink() or not path.is_file() or path.read_bytes() != data:
            errors.append(f"Missing/stale generated asset: {rel}")
    generated_roots = (".claude/skills", ".claude/references", ".codex/agents",
                       ".claude/agents", ".gemini/agents", ".cursor/agents")
    for directory in generated_roots:
        for path in (root / directory).rglob("*"):
            if path.is_symlink():
                errors.append(f"Unsafe generated symlink: {path.relative_to(root)}")
            elif path.is_file() and path.relative_to(root).as_posix() not in expected:
                errors.append(f"Unexpected generated asset: {path.relative_to(root)}")
    return errors


def sync(root: Path = ROOT) -> None:
    expected = expected_assets(root)
    # Do not delete unexpected user files. Review/removal remains explicit.
    for rel, data in expected.items():
        path = contained_path(root, root / rel)
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("Refusing generated destination outside package")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        if not args.check:
            sync()
        errors = check_assets()
    except (OSError, ValueError, KeyError, IndexError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: canonical skills/references and 12 optional role adapters match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
