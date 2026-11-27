#!/usr/bin/env python3
"""Run the actual local suite and retain inspectable evidence. No auto-install."""
from __future__ import annotations
import argparse
import importlib.metadata
import json
from pathlib import Path
import platform
import sys
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", type=Path, required=True)
    args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    with (args.out/"tests.log").open("w",encoding="utf-8") as log:
        suite=unittest.defaultTestLoader.discover(str(ROOT/"tests"))
        result=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
    report={"status":"PASS" if result.wasSuccessful() else "FAIL", "tests":result.testsRun,
            "failures":len(result.failures), "errors":len(result.errors), "skipped":len(result.skipped),
            "elapsed_seconds":time.monotonic()-start, "python":sys.version,
            "platform":platform.platform(),
            "dependencies":{p:importlib.metadata.version(p) for p in ("jsonschema","PyYAML")},
            "scope":"Local Python unit, CLI, filesystem and POSIX process tests; includes synthetic probes",
            "native_coding_client_tests":"NOT_RUN", "token_benchmark":"NOT_RUN"}
    (args.out/"verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__=="__main__":raise SystemExit(main())
