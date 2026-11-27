"""Content-addressed source snapshots. Isolation of copies, not an OS sandbox."""
from __future__ import annotations
import os
from pathlib import Path
import shutil
import stat
import tempfile
from typing import Any

from .contract import canonical_digest
from .io import SidecarError, atomic_json, contained, digest_bytes, read_bytes, read_json, safe_relative

EXCLUDE_DIRS = {".git", ".sidecar", ".venv", "venv", "node_modules", "__pycache__",
                ".pytest_cache", ".mypy_cache", ".ruff_cache"}
MAX_FILES = 10000
MAX_TOTAL = 64 * 1024 * 1024
MAX_FILE = 8 * 1024 * 1024


def excluded(name: str) -> bool:
    return (name in EXCLUDE_DIRS or (name.startswith(".env") and name != ".env.example")
            or name.endswith((".pem", ".key", ".p12", ".pfx"))
            or name in {"credentials.json", "id_rsa", "id_ed25519", ".DS_Store"})


def initialize_state(root: Path) -> Path:
    if root.is_symlink():
        raise SidecarError("unsafe_state", "State root must not be a symlink")
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    root = root.resolve()
    if os.name == "posix":
        st = root.stat()
        if st.st_uid != os.getuid() or st.st_mode & 0o077:
            raise SidecarError("unsafe_state", "State must be owned by the caller with mode 0700")
    for child in ("snapshots", "runs", "claims", "requests"):
        path = root / child
        if path.is_symlink():
            raise SidecarError("unsafe_state", "State child is a symlink")
        path.mkdir(mode=0o700, exist_ok=True)
    return root


def _files(root: Path, *, filtering: bool) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    omitted: list[str] = []
    for parent, dirs, names in os.walk(root, followlinks=False):
        dirs.sort(); names.sort()
        keep = []
        for name in dirs:
            path = Path(parent) / name
            rel = path.relative_to(root).as_posix()
            if filtering and excluded(name):
                omitted.append(rel + "/")
            elif path.is_symlink():
                raise SidecarError("snapshot_symlink", "Source contains an included symlink directory")
            else:
                keep.append(name)
        dirs[:] = keep
        for name in names:
            path = Path(parent) / name
            rel = path.relative_to(root).as_posix()
            if filtering and excluded(name):
                omitted.append(rel)
                continue
            if not safe_relative(rel) or path.is_symlink() or not stat.S_ISREG(path.stat().st_mode):
                raise SidecarError("snapshot_unsafe", "Source contains an unsafe path or special file")
            files.append(path)
            if len(files) > MAX_FILES:
                raise SidecarError("snapshot_limit", "Source exceeds 10000 files; use a narrower source root")
    return sorted(files), sorted(omitted)


def _signature(files: list[Path], root: Path) -> list[tuple[Any, ...]]:
    return [(p.relative_to(root).as_posix(), p.stat().st_size, p.stat().st_mtime_ns,
             p.stat().st_ino, bool(p.stat().st_mode & 0o111)) for p in files]


def create_snapshot(source: Path, state: Path, repository: str | None = None) -> dict[str, Any]:
    source = source.resolve(strict=True)
    state = initialize_state(state)
    if not source.is_dir() or state.is_relative_to(source) or source.is_relative_to(state):
        raise SidecarError("snapshot_overlap", "Source and Sidecar state must be disjoint directories")
    repository = repository or str(source)
    if not repository.strip() or len(repository) > 256:
        raise SidecarError("repository_id", "Repository identifier must be 1..256 characters")
    files, omitted = _files(source, filtering=True)
    before = _signature(files, source)
    temp = Path(tempfile.mkdtemp(prefix=".snapshot-", dir=state / "snapshots"))
    try:
        tree = temp / "source"; tree.mkdir(mode=0o700)
        records = []
        total = 0
        for path in files:
            content = read_bytes(path, MAX_FILE)
            total += len(content)
            if total > MAX_TOTAL:
                raise SidecarError("snapshot_limit", "Source exceeds 64 MiB; use a narrower source root")
            rel = path.relative_to(source).as_posix()
            out = tree / rel; out.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            out.write_bytes(content)
            executable = bool(path.stat().st_mode & 0o111)
            out.chmod(0o500 if executable else 0o400)
            records.append({"path": rel, "size_bytes": len(content),
                            "digest": digest_bytes(content), "executable": executable})
        after_files, after_omitted = _files(source, filtering=True)
        if before != _signature(after_files, source) or omitted != after_omitted:
            raise SidecarError("source_changed", "Source changed while snapshotting; retry only after it is stable")
        payload = {"format": "sidecar.snapshot/v1", "files": records, "excluded": omitted}
        digest = canonical_digest(payload)
        atomic_json(temp / "manifest.json", {**payload, "digest": digest})
        destination = state / "snapshots" / digest.split(":")[1]
        if destination.exists():
            verify_snapshot(state, digest)
        else:
            try:
                os.rename(temp, destination)
            except OSError:
                if not destination.exists():
                    raise
                verify_snapshot(state, digest)
        return {"repository": repository, "snapshot": {"kind": "content_digest", "value": digest},
                "files": len(records), "size_bytes": total, "excluded": omitted}
    finally:
        if temp.exists():
            shutil.rmtree(temp)


def verify_snapshot(state: Path, digest: str) -> tuple[Path, dict[str, Any]]:
    from .io import DIGEST_RE
    if not DIGEST_RE.fullmatch(digest):
        raise SidecarError("invalid_snapshot", "Snapshot needs a SHA-256 identity")
    root = contained(state / "snapshots", digest.split(":")[1])
    manifest = read_json(contained(root, "manifest.json"))
    if set(manifest) != {"format", "files", "excluded", "digest"}:
        raise SidecarError("snapshot_corrupt", "Unknown snapshot manifest fields")
    payload = {k: v for k, v in manifest.items() if k != "digest"}
    if manifest["format"] != "sidecar.snapshot/v1" or manifest["digest"] != digest or canonical_digest(payload) != digest:
        raise SidecarError("snapshot_corrupt", "Snapshot manifest identity differs")
    source = contained(root, "source")
    files, _ = _files(source, filtering=False)
    actual = []
    total = 0
    for path in files:
        data = read_bytes(path, MAX_FILE); total += len(data)
        if total > MAX_TOTAL:
            raise SidecarError("snapshot_limit", "Stored snapshot exceeds its limit")
        actual.append({"path": path.relative_to(source).as_posix(), "size_bytes": len(data),
                       "digest": digest_bytes(data), "executable": bool(path.stat().st_mode & 0o111)})
    if actual != manifest["files"]:
        raise SidecarError("snapshot_corrupt", "Stored source bytes, modes or file set changed")
    return source, manifest


def private_copy(source: Path, destination: Path) -> Path:
    """Each process step gets a private writable tree; no shared mutable workspace."""
    shutil.copytree(source, destination, symlinks=False)
    for root, dirs, files in os.walk(destination):
        Path(root).chmod(0o700)
        for name in files:
            p = Path(root) / name
            p.chmod(0o700 if p.stat().st_mode & 0o111 else 0o600)
    return destination
