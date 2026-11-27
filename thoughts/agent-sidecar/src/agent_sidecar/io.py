"""Bounded, strict data IO. No remote schema resolution, shell or network IO."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile
from typing import Any

from .contract import canonical_digest, load_json

MAX_DOCUMENT = 2 * 1024 * 1024
ID_RE = re.compile(r"[a-z][a-z0-9._-]{0,63}\Z")
DIGEST_RE = re.compile(r"sha256:[0-9a-f]{64}\Z")


class SidecarError(Exception):
    def __init__(self, code: str, message: str, action: str = "reason") -> None:
        super().__init__(message)
        self.code, self.message, self.action = code, message, action


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def instant(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("Timezone is required")
    return dt.astimezone(timezone.utc)


def digest_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def safe_relative(value: str, allow_dot: bool = False) -> bool:
    if value == "." and allow_dot:
        return True
    return (isinstance(value, str) and bool(value) and len(value) <= 1024
            and "\\" not in value and not value.startswith("/")
            and all(p not in {"", ".", ".."} for p in value.split("/"))
            and all(ord(c) >= 32 and ord(c) != 127 for c in value))


def contained(root: Path, relative: str, *, allow_dot: bool = False,
              must_exist: bool = True) -> Path:
    if not safe_relative(relative, allow_dot):
        raise SidecarError("unsafe_path", "A path is absolute, ambiguous or traverses a parent")
    root = root.resolve(strict=True)
    path = root if relative == "." else root / relative
    cur = root
    for part in (() if relative == "." else Path(relative).parts):
        cur = cur / part
        if cur.is_symlink():
            raise SidecarError("unsafe_path", "Symlink paths are not accepted")
    resolved = path.resolve(strict=must_exist)
    if not resolved.is_relative_to(root):
        raise SidecarError("unsafe_path", "Path escapes its assigned root")
    return path


def read_bytes(path: Path, limit: int = MAX_DOCUMENT) -> bytes:
    if path.is_symlink():
        raise SidecarError("unsafe_path", "Symlink files are not accepted")
    st = path.stat()
    if not stat.S_ISREG(st.st_mode):
        raise SidecarError("unsafe_file", "Expected a regular file")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    fd = os.open(path, flags)
    with os.fdopen(fd, "rb") as stream:
        actual = os.fstat(stream.fileno())
        if not stat.S_ISREG(actual.st_mode):
            raise SidecarError("unsafe_file", "File changed to a non-regular file")
        if actual.st_size > limit:
            raise SidecarError("size_limit", "File exceeds its byte limit")
        data = stream.read(limit + 1)
    if len(data) > limit:
        raise SidecarError("size_limit", "File exceeds its byte limit")
    return data


def strict_json_bytes(raw: bytes) -> Any:
    from .contract import _unique_object, _no_constant
    if len(raw) > MAX_DOCUMENT:
        raise SidecarError("document_limit", "Document exceeds 2 MiB")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_object,
                           parse_constant=_no_constant)
        # Also catches overflow such as 1e999 and invalid surrogate strings.
        canonical_digest(value)
        stack = [(value, 0)]
        while stack:
            item, depth = stack.pop()
            if depth > 48:
                raise ValueError("Document nesting exceeds 48 levels")
            if isinstance(item, dict):
                stack.extend((v, depth + 1) for v in item.values())
            elif isinstance(item, list):
                stack.extend((v, depth + 1) for v in item)
        return value
    except (ValueError, UnicodeError, RecursionError, TypeError) as exc:
        raise SidecarError("invalid_json", "Invalid, ambiguous or excessive JSON") from exc


def read_json(path: Path) -> Any:
    return strict_json_bytes(read_bytes(path))


def structured(path: Path) -> tuple[Any, bytes]:
    raw = read_bytes(path)
    if path.suffix.lower() == ".json":
        return strict_json_bytes(raw), raw
    import yaml

    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader: Any, node: Any, deep: bool = False) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in out or key == "<<":
                raise ValueError("Non-string or duplicate YAML key")
            out[key] = loader.construct_object(value_node, deep=deep)
        return out

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    try:
        for token in yaml.scan(raw):
            if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
                raise ValueError("YAML anchors and aliases are unsupported")
        value = yaml.load(raw.decode("utf-8"), Loader=UniqueLoader)
        # Round-trip through bounded JSON rejects timestamps, sets, NaN and deep structures.
        encoded = json.dumps(value, ensure_ascii=False, allow_nan=False).encode("utf-8")
        return strict_json_bytes(encoded), raw
    except (ValueError, TypeError, UnicodeError, RecursionError, yaml.YAMLError) as exc:
        raise SidecarError("invalid_yaml", "YAML must be unambiguous, bounded JSON-compatible data") from exc


def atomic_json(path: Path, value: Any, *, exclusive: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.is_symlink():
        raise SidecarError("unsafe_path", "Cannot replace a symlink")
    data = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    if exclusive:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        return
    fd, temp = tempfile.mkstemp(prefix=".pending-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def utf8_prefix(text: str, max_bytes: int) -> str:
    return text.encode("utf-8")[:max_bytes].decode("utf-8", errors="ignore")
