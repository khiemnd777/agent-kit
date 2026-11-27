#!/usr/bin/env python3
"""Verify against an exact, operator-supplied Agent Kit V2 source directory.

Explicit --confirm-trusted-code permits executing that directory's maintenance
scripts on private copies. No Git writes, installation, native-client launch or API.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from agent_sidecar.engine import execute
from agent_sidecar.io import atomic_json, read_json
from agent_sidecar.policy import authorize,make_policy,prepare_request
from agent_sidecar.registry import load_registry
from agent_sidecar.snapshots import create_snapshot


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint(root: Path) -> dict[str,str]:
    return {p.relative_to(root).as_posix():file_hash(p) for p in sorted(root.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--agent-kit',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--confirm-trusted-code',action='store_true')
    args=p.parse_args()
    if not args.confirm_trusted_code:p.error('Explicit --confirm-trusted-code is required')
    kit=args.agent_kit.resolve(strict=True)
    out=args.out.resolve()
    if out.exists():p.error('Use a new output directory; do not mix run evidence')
    if out.is_relative_to(kit):p.error('Output must be outside the Agent Kit source')
    out.mkdir(parents=True,mode=0o700)
    before=fingerprint(kit)
    schemas={}
    for filename in ('capability.schema.json','execution-request.schema.json','execution-result.schema.json'):
        actual=file_hash(ROOT/'src/agent_sidecar/contracts'/filename)
        expected=file_hash(kit/'contracts'/filename)
        schemas[filename]={'sidecar_sha256':actual,'agentkit_sha256':expected,'equal':actual==expected}
    registry=load_registry(ROOT/'workflows');runs=[]
    cases=[('repo.prepare',ROOT/'examples/demo-project',{'include':['package.json','src']}),
           ('agentkit.integrity',kit,{}),('agentkit.verify',kit,{})]
    for name,source,inputs in cases:
        case=out/name;case.mkdir(mode=0o700);state=case/'state';wf=registry[name]
        policy=make_policy([wf],[str(source.resolve())],{'python3':sys.executable} if wf.has_process else {},wf.has_process)
        snap=create_snapshot(source,state)
        request=prepare_request(wf,policy,snap,inputs,'Local Sidecar interoperability test on supplied source',
                                'interop-test','test-fixture:explicit-cli-confirmation')
        result=execute(request,wf,policy,authorize(request,wf,policy),state)
        for filename,value in [('request.json',request),('result.json',result),('capability.json',wf.descriptor)]:
            atomic_json(case/filename,value)
        check=subprocess.run([sys.executable,str(kit/'scripts/check_contract.py'),
                              '--request',str(case/'request.json'),'--result',str(case/'result.json'),
                              '--capability',str(case/'capability.json')],capture_output=True,text=True,timeout=30)
        (case/'agentkit-validator.log').write_text(check.stdout+check.stderr,encoding='utf-8')
        baseline_tests=None
        if result['run_id']:
            run_root=state/'runs'/result['run_id']
            evidence=case/'export';evidence.mkdir(mode=0o700)
            for item in result['artifacts']:
                dest=evidence/item['relative_path'];dest.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(run_root/item['relative_path'],dest)
                if item['relative_path'].endswith('regression.log'):
                    match=re.search(r'Ran (\d+) tests',dest.read_text(errors='replace'))
                    if match:baseline_tests=int(match.group(1))
        runs.append({'workflow':name,'status':result['status'],'run_id':result['run_id'],
                     'original_v2_validator_exit':check.returncode,'original_v2_validator':check.stdout.strip(),
                     'baseline_regression_tests_observed':baseline_tests,
                     'checks':result['checks'],'duration_seconds':result['metrics']['duration_seconds']})
    unchanged=fingerprint(kit)==before
    valid=all(x['equal'] for x in schemas.values()) and unchanged and all(
        r['status']=='succeeded' and r['original_v2_validator_exit']==0 for r in runs)
    report={'status':'PASS' if valid else 'FAIL','schema_bytes':schemas,'agentkit_source_unchanged':unchanged,
            'runs':runs,'scope':'Actual local execution plus original V2 document validator, not a native coding-client integration',
            'native_clients':'NOT_RUN','token_savings':'NOT_MEASURED'}
    atomic_json(out/'interop.json',report);print(json.dumps(report,indent=2))
    return 0 if valid else 1


if __name__=='__main__':raise SystemExit(main())
