from __future__ import annotations
import copy
from datetime import datetime, timedelta, timezone
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from agent_sidecar.contract import canonical_digest, result_errors
from agent_sidecar.engine import execute, verify_result
from agent_sidecar.executors import Outcome, expand
from agent_sidecar.io import (SidecarError, atomic_json, digest_bytes, now, read_json,
                              strict_json_bytes, structured)
from agent_sidecar.policy import (admit, authorize, environment, load_policy,
                                  make_policy, prepare_request)
from agent_sidecar.registry import load_registry, load_workflow
from agent_sidecar.snapshots import create_snapshot, initialize_state, verify_snapshot


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="sidecar-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "source"; self.source.mkdir()
        (self.source / "a.txt").write_text("alpha", encoding="utf-8")
        (self.source / "package.json").write_text('{"scripts":{"test":"node --test"}}')
        self.state = self.base / "state"
        self.registry = self.base / "registry"; self.registry.mkdir()

    def builtin_step(self, sid="inventory", needs=None, operation="inventory", **extra):
        return {"id": sid, "executor": "builtin", "operation": operation,
                "needs": needs or [], "criterion": "Requested inputs are checked", "timeout_seconds": 10, **extra}

    def process_step(self, code, sid="command", needs=None, **extra):
        return {"id": sid, "executor": "process", "argv": ["python3", "-c", code],
                "needs": needs or [], "criterion": "Trusted local test command exits successfully",
                "timeout_seconds": 10, **extra}

    def workflow(self, steps=None, **extra):
        doc = {"format": "sidecar.workflow/v1", "id": "test.work", "version": "1.0.0",
               "description": "Synthetic workflow for local unit/integration tests", "lifecycle": "reviewed",
               "review_ref": "test-fixture:reviewed-code", "effects": ["read_source", "write_scratch"],
               "replay_policy": "safe_read_only",
               "input_schema": {"type": "object", "properties": {}, "additionalProperties": False},
               "steps": steps or [self.builtin_step()], **extra}
        p = self.registry / "work.json"; atomic_json(p, doc)
        return load_workflow(p)

    def bundle(self, wf=None, *, inputs=None, changes=None):
        wf = wf or self.workflow()
        policy = make_policy([wf], [str(self.source)], {"python3": sys.executable} if wf.has_process else {}, wf.has_process)
        if changes: changes(policy)
        snapshot = create_snapshot(self.source, self.state)
        req = prepare_request(wf, policy, snapshot, inputs or {}, "Synthetic local implementation test",
                              "local-test", "test-fixture:not-production-approval")
        return wf, policy, req, authorize(req, wf, policy)

    def run_bundle(self, b, event=None):
        wf, policy, req, permit = b
        result = execute(req, wf, policy, permit, self.state, event)
        self.assertEqual([], result_errors(req, result, wf.descriptor))
        if result["run_id"]:
            verify_result(req, result, self.state / "runs" / result["run_id"], wf.descriptor)
        return result

    def receipt(self, result, step):
        return read_json(self.state / "runs" / result["run_id"] / "evidence" / (step + ".json"))


class IOTests(Fixture):
    def test_duplicate_json(self):
        with self.assertRaises(SidecarError): strict_json_bytes(b'{"a":1,"a":2}')
    def test_nonfinite_json(self):
        for raw in (b'{"v":NaN}', b'{"v":Infinity}', b'{"v":1e999}'):
            with self.subTest(raw=raw), self.assertRaises(SidecarError): strict_json_bytes(raw)
    def test_utf8_canonical(self):
        obj = {"x": "Việt Nam 🎯", "a": 1.5}
        raw = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
        self.assertEqual(canonical_digest(obj), digest_bytes(raw))
    def test_invalid_surrogate(self):
        with self.assertRaises(SidecarError): strict_json_bytes(b'"\\ud800"')
    def test_deep_json(self):
        with self.assertRaises(SidecarError): strict_json_bytes(b'['*60+b'1'+b']'*60)
    def test_large_json(self):
        with self.assertRaises(SidecarError): strict_json_bytes(b' '*(2*1024*1024+1))
    def test_duplicate_yaml(self):
        p=self.base/'x.yaml';p.write_text('a: 1\na: 2\n')
        with self.assertRaises(SidecarError): structured(p)
    def test_yaml_alias(self):
        p=self.base/'x.yaml';p.write_text('a: &x [1]\nb: *x\n')
        with self.assertRaises(SidecarError): structured(p)
    def test_yaml_custom_tag(self):
        p=self.base/'x.yaml';p.write_text('!!python/object/apply:os.system ["echo bad"]')
        with self.assertRaises(SidecarError): structured(p)
    def test_no_overwrite(self):
        p=self.base/'x.json';atomic_json(p,{},exclusive=True)
        with self.assertRaises(FileExistsError):atomic_json(p,{"b":1},exclusive=True)
    def test_symlink_read(self):
        p=self.base/'link';p.symlink_to(self.source/'package.json')
        with self.assertRaises(SidecarError): read_json(p)
    def test_schema_remote_ref_forbidden(self):
        schema={"type":"object","additionalProperties":False,"properties":{"v":{"$ref":"https://example.invalid/remote"}}}
        with self.assertRaises(SidecarError): self.workflow(input_schema=schema)


class RegistryTests(Fixture):
    def test_bundled_registry_valid(self):
        self.assertEqual(set(load_registry(ROOT/'workflows')), {'repo.prepare','agentkit.integrity','agentkit.verify'})
    def test_unknown_field(self):
        with self.assertRaises(SidecarError):self.workflow(unrecognized=True)
    def test_duplicate_steps(self):
        with self.assertRaises(SidecarError):self.workflow([self.builtin_step(),self.builtin_step()])
    def test_cycle(self):
        with self.assertRaises(SidecarError):self.workflow([self.builtin_step('a',['b']),self.builtin_step('b',['a'])])
    def test_self_cycle(self):
        with self.assertRaises(SidecarError):self.workflow([self.builtin_step('a',['a'])])
    def test_missing_dependency(self):
        with self.assertRaises(SidecarError):self.workflow([self.builtin_step('a',['missing'])])
    def test_executable_cannot_be_interpolated(self):
        s=self.process_step('pass');s['argv'][0]='{{inputs.command}}'
        with self.assertRaises(SidecarError):self.workflow([s])
    def test_no_absolute_executable(self):
        s=self.process_step('pass');s['argv'][0]=sys.executable
        with self.assertRaises(SidecarError):self.workflow([s])
    def test_cwd_escape(self):
        with self.assertRaises(SidecarError):self.workflow([self.process_step('pass',cwd='../')])
    def test_unknown_builtin(self):
        with self.assertRaises(SidecarError):self.workflow([self.builtin_step(operation='invented')])
    def test_retry_assertion_exit_code_refused(self):
        with self.assertRaises(SidecarError):self.workflow([self.process_step('pass',retry_exit_codes=[1])])
    def test_retry_never_workflow_refused(self):
        with self.assertRaises(SidecarError):self.workflow([self.process_step('pass',retry_exit_codes=[75])],replay_policy='never')
    def test_workflow_env_injection_refused(self):
        with self.assertRaises(SidecarError):self.workflow([self.process_step('pass',env={'LD_PRELOAD':'bad'})])
    def test_digest_changes_when_workflow_changes(self):
        a=self.workflow().digest;b=self.workflow(description='Different reviewed description').digest
        self.assertNotEqual(a,b)
    def test_draft_not_authorized(self):
        wf=self.workflow(lifecycle='draft',review_ref=None)
        with self.assertRaises(SidecarError):make_policy([wf],[str(self.source)],{})
    def test_process_requires_opt_in(self):
        wf=self.workflow([self.process_step('pass')])
        with self.assertRaises(SidecarError):make_policy([wf],[str(self.source)],{'python3':sys.executable})
    def test_template_literal_no_shell(self):
        self.assertEqual(expand('$(echo bad)',{},self.source,self.base),'$(echo bad)')
    def test_template_requires_whole_argument(self):
        with self.assertRaises(SidecarError):expand('prefix-{{inputs.x}}',{'x':'a'},self.source,self.base)


class SnapshotTests(Fixture):
    def test_snapshot_includes_untracked(self):
        (self.source/'new.txt').write_text('untracked')
        snapshot=create_snapshot(self.source,self.state)
        source,_=verify_snapshot(self.state,snapshot['snapshot']['value'])
        self.assertEqual((source/'new.txt').read_text(),'untracked')
    def test_same_content_same_digest(self):
        a=create_snapshot(self.source,self.state);b=create_snapshot(self.source,self.state)
        self.assertEqual(a['snapshot'],b['snapshot'])
    def test_source_change_changes_digest(self):
        a=create_snapshot(self.source,self.state);(self.source/'a.txt').write_text('beta')
        b=create_snapshot(self.source,self.state);self.assertNotEqual(a['snapshot'],b['snapshot'])
    def test_source_mutation_after_snapshot_does_not_change_copy(self):
        a=create_snapshot(self.source,self.state);(self.source/'a.txt').write_text('beta')
        source,_=verify_snapshot(self.state,a['snapshot']['value']);self.assertEqual((source/'a.txt').read_text(),'alpha')
    def test_sensitive_exclusions_disclosed(self):
        (self.source/'.env').write_text('SECRET=not-real');(self.source/'key.pem').write_text('test')
        a=create_snapshot(self.source,self.state)
        self.assertIn('.env',a['excluded']);self.assertIn('key.pem',a['excluded'])
    def test_source_symlink_refused(self):
        (self.source/'link').symlink_to(self.base/'elsewhere')
        with self.assertRaises(SidecarError):create_snapshot(self.source,self.state)
    def test_source_directory_symlink_refused(self):
        (self.source/'link').symlink_to(self.registry,target_is_directory=True)
        with self.assertRaises(SidecarError):create_snapshot(self.source,self.state)
    def test_state_overlap_refused(self):
        with self.assertRaises(SidecarError):create_snapshot(self.source,self.source/'state')
    def test_snapshot_tamper_refused(self):
        a=create_snapshot(self.source,self.state);source,_=verify_snapshot(self.state,a['snapshot']['value'])
        (source/'a.txt').chmod(0o600);(source/'a.txt').write_text('tamper')
        with self.assertRaises(SidecarError):verify_snapshot(self.state,a['snapshot']['value'])
    def test_extra_snapshot_file_refused(self):
        a=create_snapshot(self.source,self.state);source,_=verify_snapshot(self.state,a['snapshot']['value'])
        (source/'extra').write_text('tamper')
        with self.assertRaises(SidecarError):verify_snapshot(self.state,a['snapshot']['value'])
    def test_snapshot_executable_mode_bound(self):
        a=create_snapshot(self.source,self.state);source,_=verify_snapshot(self.state,a['snapshot']['value'])
        (source/'a.txt').chmod(0o500)
        with self.assertRaises(SidecarError):verify_snapshot(self.state,a['snapshot']['value'])
    @unittest.skipUnless(os.name=='posix','POSIX permissions')
    def test_state_world_access_refused(self):
        self.state.mkdir(mode=0o755)
        with self.assertRaises(SidecarError):initialize_state(self.state)


class AdmissionTests(Fixture):
    def test_no_permit_is_not_valid_permit(self):
        wf,pol,req,permit=self.bundle()
        r=execute(req,wf,pol,{},self.state)
        self.assertEqual(r['status'],'blocked');self.assertIsNone(r['run_id'])
    def test_permit_bound_to_complete_request(self):
        wf,pol,req,permit=self.bundle();req['objective']='Changed intent'
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'permit_mismatch')
    def test_expired_authorization(self):
        wf,pol,req,permit=self.bundle();req['authorization']['expires_at']='2000-01-01T00:00:00Z'
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'authorization_expired')
    def test_policy_change_refused(self):
        wf,pol,req,permit=self.bundle();pol['limits']['max_concurrency']=1
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'policy_changed')
    def test_environment_change_refused(self):
        wf,pol,req,permit=self.bundle();req['target']['environment_digest']='sha256:'+'a'*64
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'environment_changed')
    def test_wrong_repository(self):
        wf,pol,req,permit=self.bundle();req['target']['repository']='not-authorized'
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'target_not_authorized')
    def test_required_criterion_cannot_be_redefined(self):
        wf,pol,req,permit=self.bundle();req['checks'][0]['criterion']='Infer business correctness'
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'check_mismatch')
    def test_no_network_effect(self):
        wf,pol,req,permit=self.bundle();req['authorization']['allowed_effects'].append('network');req['authorization']['network_hosts']=['example.org']
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'unsupported_authority')
    def test_no_source_write_effect(self):
        wf,pol,req,permit=self.bundle();req['authorization']['allowed_effects'].append('write_source')
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'unsupported_authority')
    def test_snapshot_corruption_blocks_before_run(self):
        b=self.bundle();source,_=verify_snapshot(self.state,b[2]['target']['snapshot']['value'])
        (source/'a.txt').chmod(0o600);(source/'a.txt').write_text('tamper')
        r=self.run_bundle(b);self.assertEqual(r['status'],'blocked');self.assertIsNone(r['run_id'])
    def test_small_evidence_budget_refused(self):
        with self.assertRaises(SidecarError):self.bundle(changes=lambda p:p['limits'].update(max_evidence_bytes=16))
    def test_policy_unknown_properties(self):
        _,pol,_,_=self.bundle();pol['bypass']=True;p=self.base/'policy.json';atomic_json(p,pol)
        with self.assertRaises(SidecarError):load_policy(p)
    def test_policy_requires_risk_ack(self):
        _,pol,_,_=self.bundle();pol['allow_trusted_process']=True;p=self.base/'policy.json';atomic_json(p,pol)
        with self.assertRaises(SidecarError):load_policy(p)
    def test_git_commit_profile_refused(self):
        wf,pol,req,permit=self.bundle();req['target']['snapshot']={'kind':'git_commit','value':'a'*40}
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'snapshot_profile')


class BuiltinAndEngineTests(Fixture):
    def test_basic_success(self):
        r=self.run_bundle(self.bundle());self.assertEqual(r['status'],'succeeded')
        self.assertEqual(r['metrics']['usage']['input_tokens'],0)
    def test_no_source_mutation(self):
        before={p.name:p.read_bytes() for p in self.source.iterdir()}
        self.run_bundle(self.bundle())
        self.assertEqual(before,{p.name:p.read_bytes() for p in self.source.iterdir()})
    def test_declared_entrypoints_only(self):
        b=self.bundle(self.workflow([self.builtin_step('entrypoints',operation='entrypoints')]))
        r=self.run_bundle(b);payload=self.receipt(r,'entrypoints')['payload']
        self.assertFalse(payload['commands_executed']);self.assertEqual(payload['manifests'][0]['declared_scripts']['test'],'node --test')
    def test_json_failure_is_fail(self):
        (self.source/'bad.json').write_text('{broken')
        schema={'type':'object','properties':{'paths':{'type':'array','items':{'type':'string'}}},'required':['paths'],'additionalProperties':False}
        wf=self.workflow([self.builtin_step('json',operation='json-files')],input_schema=schema)
        r=self.run_bundle(self.bundle(wf,inputs={'paths':['bad.json']}));self.assertEqual(r['status'],'failed')
    def test_missing_input_blocks(self):
        wf=self.workflow([self.builtin_step('manifest',operation='manifest')])
        r=self.run_bundle(self.bundle(wf));self.assertEqual(r['status'],'blocked');self.assertEqual(r['checks'][0]['status'],'NOT_RUN')
    def test_failure_blocks_dependents_but_always_runs(self):
        schema={'type':'object','properties':{'paths':{'type':'array','items':{'type':'string'}}},'additionalProperties':False}
        wf=self.workflow([self.builtin_step('bad',operation='json-files'),self.builtin_step('dependent',['bad']),
                          self.builtin_step('collector',['bad'],when='always')],input_schema=schema)
        r=self.run_bundle(self.bundle(wf,inputs={'paths':['absent.json']}))
        self.assertEqual([c['status'] for c in r['checks']],['FAIL','NOT_RUN','PASS'])
    def test_dependency_order_not_file_order(self):
        wf=self.workflow([self.builtin_step('last',['first']),self.builtin_step('first')])
        r=self.run_bundle(self.bundle(wf));self.assertEqual(r['status'],'succeeded')
    def test_bounded_concurrency(self):
        wf=self.workflow([self.builtin_step('step'+str(i)) for i in range(6)])
        b=self.bundle(wf,changes=lambda p:p['limits'].update(max_concurrency=2))
        active=0;peak=0;lock=threading.Lock()
        def measured(*a):
            nonlocal active,peak
            with lock:active+=1;peak=max(peak,active)
            time.sleep(.05)
            with lock:active-=1
            return Outcome('PASS','Synthetic concurrency probe',attempts=1,payload={'synthetic':True})
        with patch('agent_sidecar.engine.builtin',measured):r=self.run_bundle(b)
        self.assertEqual(r['status'],'succeeded');self.assertEqual(peak,2)
    def test_duplicate_request_reuses_verified_result(self):
        b=self.bundle();a=self.run_bundle(b)
        with patch('agent_sidecar.engine.builtin',side_effect=AssertionError('Must not rerun')):r=self.run_bundle(b)
        self.assertEqual(a,r)
    def test_request_id_conflict_refused(self):
        b=self.bundle();self.run_bundle(b);wf,pol,req,_=b
        req['objective']='changed';permit=authorize(req,wf,pol)
        r=execute(req,wf,pol,permit,self.state);self.assertEqual(r['exceptions'][0]['code'],'request_id_conflict')
    def test_stranded_claim_no_replay(self):
        b=self.bundle();wf,pol,req,permit=b
        atomic_json(self.state/'claims'/(req['request_id']+'.json'),{'request_digest':canonical_digest(req),'run_id':'run-stranded','state':'running'})
        r=self.run_bundle(b);self.assertEqual(r['exceptions'][0]['next_action'],'reconcile')
    def test_evidence_tamper_refused(self):
        b=self.bundle();r=self.run_bundle(b);artifact=self.state/'runs'/r['run_id']/r['artifacts'][0]['relative_path'];artifact.write_bytes(b'wrong')
        with self.assertRaises(SidecarError):verify_result(b[2],r,self.state/'runs'/r['run_id'],b[0].descriptor)
    def test_reuse_checks_actual_evidence(self):
        b=self.bundle();r=self.run_bundle(b);(self.state/'runs'/r['run_id']/r['artifacts'][0]['relative_path']).unlink()
        with self.assertRaises(SidecarError):self.run_bundle(b)
    def test_result_wrong_snapshot_rejected(self):
        b=self.bundle();r=self.run_bundle(b);r['target']=copy.deepcopy(r['target']);r['target']['snapshot']['value']='sha256:'+'b'*64
        with self.assertRaises(SidecarError):verify_result(b[2],r,self.state/'runs'/r['run_id'])
    def test_missing_required_check_rejected(self):
        b=self.bundle();r=self.run_bundle(b);r['checks']=[]
        with self.assertRaises(SidecarError):verify_result(b[2],r,self.state/'runs'/r['run_id'])
    def test_cancel_before_start(self):
        event=threading.Event();event.set();r=self.run_bundle(self.bundle(),event)
        self.assertEqual(r['status'],'cancelled');self.assertEqual(r['metrics']['attempts'],0)
    def test_evidence_overflow_never_success(self):
        for i in range(150):(self.source/('file'+str(i))).write_text('data')
        r=self.run_bundle(self.bundle(changes=lambda p:p['limits'].update(max_evidence_bytes=8192)))
        self.assertEqual(r['status'],'escalated');self.assertTrue(r['logs_truncated'])
        self.assertLessEqual(sum(a['size_bytes'] for a in r['artifacts']),8192)
    def test_unexpected_executor_error_is_escalated(self):
        b=self.bundle()
        with patch('agent_sidecar.engine.builtin',side_effect=RuntimeError('secret')):r=self.run_bundle(b)
        self.assertEqual(r['status'],'escalated');self.assertNotIn('secret',json.dumps(r))


@unittest.skipUnless(os.name=='posix','Trusted process executor is POSIX-only')
class ProcessTests(Fixture):
    def test_process_success_and_usage_unknown(self):
        r=self.run_bundle(self.bundle(self.workflow([self.process_step('print("hello")')])))
        self.assertEqual(r['status'],'succeeded');self.assertIsNone(r['metrics']['usage']['input_tokens'])
    def test_process_failure_has_evidence(self):
        r=self.run_bundle(self.bundle(self.workflow([self.process_step('raise SystemExit(1)')])))
        self.assertEqual(r['status'],'failed');self.assertEqual(r['checks'][0]['status'],'FAIL');self.assertTrue(r['checks'][0]['evidence_ids'])
    def test_missing_cwd_is_not_product_failure(self):
        wf=self.workflow([self.process_step('pass',cwd='missing')])
        r=self.run_bundle(self.bundle(wf));self.assertEqual(r['status'],'blocked');self.assertEqual(r['checks'][0]['status'],'NOT_RUN')
    def test_private_copy_writes_leave_original_unchanged(self):
        code='from pathlib import Path; Path("a.txt").write_text("changed")'
        r=self.run_bundle(self.bundle(self.workflow([self.process_step(code)])))
        self.assertEqual(r['status'],'succeeded');self.assertEqual((self.source/'a.txt').read_text(),'alpha')
    def test_environment_not_inherited(self):
        code='import os; assert "SIDECAR_FAKE_SECRET" not in os.environ; assert "PYTHONPATH" not in os.environ; print("clean")'
        b=self.bundle(self.workflow([self.process_step(code)]))
        with patch.dict(os.environ,{'SIDECAR_FAKE_SECRET':'not-real'}):r=self.run_bundle(b)
        self.assertEqual(r['status'],'succeeded')
    def test_no_shell_expansion(self):
        step=self.process_step('import sys; assert sys.argv[1]=="$(touch BAD)"');step['argv'].append('$(touch BAD)')
        r=self.run_bundle(self.bundle(self.workflow([step])));self.assertEqual(r['status'],'succeeded')
    def test_step_timeout_requires_reconciliation(self):
        wf=self.workflow([self.process_step('import time; time.sleep(10)',timeout_seconds=.1)])
        r=self.run_bundle(self.bundle(wf));self.assertEqual(r['status'],'timed_out');self.assertEqual(r['effects_state'],'unknown')
    def test_cancel_running_process(self):
        b=self.bundle(self.workflow([self.process_step('import time; time.sleep(10)')]))
        event=threading.Event();timer=threading.Timer(.25,event.set);timer.start();self.addCleanup(timer.cancel)
        r=self.run_bundle(b,event);self.assertEqual(r['status'],'cancelled');self.assertEqual(r['effects_state'],'unknown')
    def test_output_overflow_escalates(self):
        b=self.bundle(self.workflow([self.process_step('print("X"*1000000)')]),changes=lambda p:p['limits'].update(max_evidence_bytes=8192))
        r=self.run_bundle(b);self.assertEqual(r['status'],'escalated');self.assertTrue(r['logs_truncated'])
        self.assertLessEqual(sum(x['size_bytes'] for x in r['artifacts']),8192)
    def test_transient_retry_is_bounded(self):
        code='from pathlib import Path; p=Path("attempt"); n=int(p.read_text())+1 if p.exists() else 1; p.write_text(str(n)); raise SystemExit(75 if n==1 else 0)'
        wf=self.workflow([self.process_step(code,retry_exit_codes=[75],retry_delay_seconds=.05)])
        r=self.run_bundle(self.bundle(wf,changes=lambda p:p['limits'].update(max_attempts=3)))
        self.assertEqual(r['status'],'succeeded');self.assertEqual(r['metrics']['attempts'],2)
    def test_assertion_failure_not_retried(self):
        wf=self.workflow([self.process_step('raise SystemExit(1)',retry_exit_codes=[75])])
        r=self.run_bundle(self.bundle(wf,changes=lambda p:p['limits'].update(max_attempts=3)))
        self.assertEqual(r['status'],'failed');self.assertEqual(r['metrics']['attempts'],1)
    def test_retry_exhausted(self):
        wf=self.workflow([self.process_step('raise SystemExit(75)',retry_exit_codes=[75],retry_delay_seconds=.05)])
        r=self.run_bundle(self.bundle(wf,changes=lambda p:p['limits'].update(max_attempts=2)))
        self.assertEqual(r['status'],'failed');self.assertEqual(r['metrics']['attempts'],2)
    def test_background_child_escalates(self):
        code='import subprocess,sys; subprocess.Popen([sys.executable,"-c","import time; time.sleep(20)"]); print("spawned")'
        r=self.run_bundle(self.bundle(self.workflow([self.process_step(code)])))
        self.assertEqual(r['status'],'escalated');self.assertEqual(r['effects_state'],'unknown')
    def test_signal_termination_requires_reconciliation(self):
        code='import os,signal; os.kill(os.getpid(),signal.SIGTERM)'
        r=self.run_bundle(self.bundle(self.workflow([self.process_step(code)])))
        self.assertEqual(r['status'],'escalated');self.assertEqual(r['effects_state'],'unknown')
    def test_independent_process_workspaces(self):
        steps=[self.process_step('from pathlib import Path; Path("isolated").write_text("a")','a'),
               self.process_step('from pathlib import Path; assert not Path("isolated").exists()','b',['a'])]
        r=self.run_bundle(self.bundle(self.workflow(steps)));self.assertEqual(r['status'],'succeeded')


class CLITests(Fixture):
    def cli(self,*args):
        return subprocess.run([sys.executable,str(ROOT/'sidecar'),*map(str,args)],capture_output=True,text=True,timeout=15)
    def test_version(self):
        p=self.cli('--version');self.assertEqual(p.returncode,0);self.assertIn('0.1.0',p.stdout)
    def test_capabilities(self):
        p=self.cli('capabilities','--registry',ROOT/'workflows');self.assertEqual(p.returncode,0);self.assertEqual(len(json.loads(p.stdout)['capabilities']),3)
    def test_authorize_requires_confirmation(self):
        p=self.cli('authorize','--request','missing','--policy','missing','--output',self.base/'permit.json')
        self.assertEqual(p.returncode,2);self.assertEqual(json.loads(p.stderr)['error'],'confirmation_required')
    def test_e2e_cli(self):
        wf,pol,req,permit=self.bundle()
        for name,doc in [('policy',pol),('request',req),('permit',permit)]:atomic_json(self.base/(name+'.json'),doc)
        p=self.cli('run','--registry',self.registry,'--state',self.state,'--request',self.base/'request.json',
                   '--policy',self.base/'policy.json','--permit',self.base/'permit.json')
        self.assertEqual(p.returncode,0,p.stderr);r=json.loads(p.stdout);self.assertEqual(r['status'],'succeeded')
        p=self.cli('result','--state',self.state,'--run-id',r['run_id']);self.assertEqual(p.returncode,0,p.stderr)
        p=self.cli('history','--state',self.state);self.assertEqual(len(json.loads(p.stdout)['runs']),1)
    def test_no_overwrite_after_execution(self):
        p=self.base/'already.json';p.write_text('{}')
        out=self.cli('run','--state',self.state,'--registry',self.registry,'--request','missing','--policy','missing','--permit','missing','--output',p)
        self.assertEqual(json.loads(out.stderr)['error'],'output_exists');self.assertFalse(self.state.exists())


class AdditionalBoundaryTests(Fixture):
    def test_null_permit_cannot_bypass_admission(self):
        wf,pol,req,_=self.bundle();r=execute(req,wf,pol,None,self.state)
        self.assertEqual(r['status'],'blocked');self.assertIsNone(r['run_id'])
        self.assertEqual(r['exceptions'][0]['code'],'invalid_permit')
    def test_live_duplicate_cannot_start_second_workflow(self):
        b=self.bundle();entered=threading.Event();release=threading.Event();holder=[]
        def slow(*a):
            entered.set();release.wait(5)
            return Outcome('PASS','Synthetic worker',attempts=1,payload={'test':True})
        with patch('agent_sidecar.engine.builtin',slow):
            thread=threading.Thread(target=lambda:holder.append(self.run_bundle(b)))
            thread.start();self.assertTrue(entered.wait(5))
            second=self.run_bundle(b);release.set();thread.join(5)
        self.assertFalse(thread.is_alive());self.assertEqual(second['status'],'blocked')
        self.assertEqual(second['exceptions'][0]['code'],'inflight_or_interrupted')
        self.assertEqual(holder[0]['status'],'succeeded')
    def test_artifact_symlink_refused(self):
        b=self.bundle();r=self.run_bundle(b);root=self.state/'runs'/r['run_id']
        artifact=root/r['artifacts'][0]['relative_path'];data=artifact.read_bytes();artifact.unlink()
        elsewhere=self.base/'elsewhere';elsewhere.write_bytes(data);artifact.symlink_to(elsewhere)
        with self.assertRaises(SidecarError):verify_result(b[2],r,root)
    def test_snapshot_change_during_execution_cannot_succeed(self):
        b=self.bundle();source,_=verify_snapshot(self.state,b[2]['target']['snapshot']['value'])
        def changing(*a):
            path=source/'a.txt';path.chmod(0o600);path.write_text('changed mid-run')
            return Outcome('PASS','Synthetic tampering test',attempts=1,payload={'test':True})
        with patch('agent_sidecar.engine.builtin',changing):r=self.run_bundle(b)
        self.assertEqual(r['status'],'escalated');self.assertEqual(r['effects_state'],'unknown')
    def test_evidence_overflow_preserves_failure(self):
        b=self.bundle(changes=lambda p:p['limits'].update(max_evidence_bytes=8192))
        with patch('agent_sidecar.engine.builtin',return_value=Outcome('FAIL','Actual synthetic failure',
                   terminal='failed',attempts=1,payload={'large':'x'*100000})):r=self.run_bundle(b)
        self.assertEqual(r['status'],'escalated');self.assertEqual(r['checks'][0]['status'],'FAIL')
    def test_global_timeout_bounds_long_step(self):
        wf=self.workflow([self.process_step('import time; time.sleep(20)',timeout_seconds=10)])
        r=self.run_bundle(self.bundle(wf,changes=lambda p:p['limits'].update(max_duration_seconds=1)))
        self.assertEqual(r['status'],'timed_out');self.assertLess(r['metrics']['duration_seconds'],4)
    def test_summary_utf8_budget(self):
        b=self.bundle(changes=lambda p:p['limits'].update(max_summary_bytes=128));r=self.run_bundle(b)
        self.assertLessEqual(len(r['summary'].encode()),128)
    def test_blocked_result_retains_exact_check_set(self):
        b=self.bundle(self.workflow([self.builtin_step('one'),self.builtin_step('two')]))
        wf,pol,req,permit=b;permit['request_digest']='sha256:'+'f'*64
        r=self.run_bundle(b);self.assertEqual([c['id'] for c in r['checks']],['one','two'])
        self.assertTrue(all(c['status']=='NOT_RUN' for c in r['checks']))

class DelegateCLITests(Fixture):
    cli = CLITests.cli
    def test_delegate_needs_existing_authority(self):
        p=self.cli('delegate','--source',self.source,'--state',self.state,'--policy','missing',
                   '--workflow','test.work','--scope-id','test','--decision-ref','test', '--objective','test')
        self.assertEqual(p.returncode,2);self.assertEqual(json.loads(p.stderr)['error'],'confirmation_required')
        self.assertFalse(self.state.exists())
    def test_delegate_one_call(self):
        wf,pol,_,_=self.bundle();policy=self.base/'policy.json';atomic_json(policy,pol)
        p=self.cli('delegate','--source',self.source,'--state',self.state,'--policy',policy,
                   '--registry',self.registry,'--workflow','test.work','--scope-id','test-scope',
                   '--decision-ref','test-fixture:authorized','--objective','Test one-call delegation','--confirm-authorized')
        self.assertEqual(p.returncode,0,p.stderr);r=json.loads(p.stdout);self.assertEqual(r['status'],'succeeded')
        self.assertTrue((self.state/'requests'/(r['request_id']+'.request.json')).exists())
    def test_cli_sigint_returns_cancelled(self):
        wf,pol,req,permit=self.bundle(self.workflow([self.process_step('import time; time.sleep(20)')]))
        for name,doc in [('policy',pol),('request',req),('permit',permit)]:atomic_json(self.base/(name+'.json'),doc)
        p=subprocess.Popen([sys.executable,str(ROOT/'sidecar'),'run','--registry',str(self.registry),
                            '--state',str(self.state),'--request',str(self.base/'request.json'),
                            '--policy',str(self.base/'policy.json'),'--permit',str(self.base/'permit.json')],
                            stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        try:
            deadline=time.monotonic()+5
            while time.monotonic()<deadline:
                if list((self.state/'runs').glob('*/scratch/command/work')):break
                time.sleep(.02)
            else:self.fail('Child run did not start')
            time.sleep(.15);p.send_signal(signal.SIGINT)
            stdout,stderr=p.communicate(timeout=5)
            self.assertEqual(p.returncode,130,stderr);self.assertEqual(json.loads(stdout)['status'],'cancelled')
        finally:
            if p.poll() is None:p.kill();p.wait()

if __name__ == "__main__":
    unittest.main()
