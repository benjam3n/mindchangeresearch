from pathlib import Path
from collections import Counter
import json,hashlib,re,zipfile,datetime

ROOT=Path(__file__).parent
lines=['inquiry','representation','values','conditions','methods','systems']
allocation=json.loads((ROOT/'allocation.json').read_text())['skills']
slots=[]
for line in lines:
    entries=json.loads((ROOT/line/'application-ledger.json').read_text())
    entries={(x['skill_id'],x['application_number']):x for x in entries}
    for s in [s for s in allocation if s['line']==line]:
        for n in range(1,s['applications']+1):
            entry=dict(entries.get((s['id'],n),{'skill_id':s['id'],'application_number':n,'status':'pending','missing_requirements':['No application entry yet']}))
            entry.update({'line':line,'rank':s['rank'],'slot_id':f"{s['id']}-{n:02d}",'integration_review':'not individually certified by root; see review records'})
            f=entry.get('file')
            if f:
                p=Path(f)
                if not p.is_absolute():p=ROOT/p if p.parts[0]==line else ROOT/line/p
                entry['file']=str(p.relative_to(ROOT))
                entry['record_exists']=p.exists()
                if p.exists():entry['record_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
            slots.append(entry)
assert len(slots)==300 and len({x['slot_id'] for x in slots})==300
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
run_state_path=ROOT/'run-state.json'
run_state=json.loads(run_state_path.read_text())
if run_state.get('status')=='ready_for_continuation':
    run_state['base_ledger_updated_utc']=now
    run_state_path.write_text(json.dumps(run_state,indent=2)+'\n')
counts=Counter(x['status'] for x in slots)
post_cycles=[]
for f in sorted(ROOT.glob('post-allocation/cycle-*/cycle-ledger.json')):
    cycle=json.loads(f.read_text())
    cycle['ledger_file']=str(f.relative_to(ROOT))
    post_cycles.append(cycle)
post_attempts=sum(c.get('attempt_counts',{}).get('substantive_records',0) for c in post_cycles)
post_complete=sum(c.get('attempt_counts',{}).get('complete_within_scope',0) for c in post_cycles)
post_partial=sum(c.get('attempt_counts',{}).get('partial',0) for c in post_cycles)
post_distinct=sum(c.get('attempt_counts',{}).get('distinct_new_keep_findings',0) for c in post_cycles)
ledger={'intended_mind_change':'Preserve exact remaining obligations and distinguish recorded attempts from completed original operations.',
 'updated_utc':now,'required_applications':300,'status_counts':dict(counts),'status_basis':'Per-line source-aware execution ledger. These are scoped reported statuses, not independent certification that every semantic edge is valid.',
 'gosm':json.loads((ROOT/'gosm/progress.json').read_text()),'applications':slots,
 'post_allocation_cycles':post_cycles,
 'actual_mind_change':'Missing original requirements survive aggregation instead of disappearing behind a document count; post-allocation applications, distinct findings and later uptake are counted separately.',
 'benefit':'Unperformed human and dependency stages remain retrievable, while continuing inquiry cannot inflate the frozen quota or discovery count.','verdict':'KEEP for this concrete accounting; no discovery credit for ordinary persistence.',
 'organization':'Frozen skill quotas with independent execution, depth, evidence and review fields, followed by separately frozen post-allocation cycles.','next_attempts':['Resume gated original stages only when their inputs exist','Add genuinely diverse prospective cycles','Consolidate only each next group of four distinct findings']}
integration_path=ROOT/'research/chat-integration.json'
if integration_path.exists():
    ledger['chat_integrations']=[json.loads(integration_path.read_text())]
(ROOT/'Research_Ledger.json').write_text(json.dumps(ledger,indent=2))

mds=list((ROOT/'sources').glob('*.md'));hashes={}
for f in mds:hashes.setdefault(hashlib.sha256(f.read_bytes()).hexdigest(),[]).append(str(f.relative_to(ROOT)))
receipts=[]
for f in (ROOT/'sources').glob('*.txt'):
    t=f.read_text();m=re.search(r'original-source: skills/([^/]+)/SKILL.md',t);h=re.search(r'original-sha256: ([0-9a-f]+)',t)
    if m and h:receipts.append({'skill_id':m.group(1),'requirements':str(f.relative_to(ROOT)),'source_sha256':h.group(1),'matching_emitted_sources':hashes.get(h.group(1),[])})
audit={'scope':'Original reader receipt identities versus preserved emitted byte hashes. Does not certify procedure execution or findings.','receipts':receipts,'selected_skills_without_verified_source':[s['id'] for s in allocation if not any(r['skill_id']==s['id'] and r['matching_emitted_sources'] for r in receipts)]}
(ROOT/'Source_Integrity.json').write_text(json.dumps(audit,indent=2))
byline={line:Counter(x['status'] for x in slots if x['line']==line) for line in lines}
table='\n'.join(['| Line | Complete in stated scope | Partial | Blocked | Pending |','| --- | ---: | ---: | ---: | ---: |']+['| '+line+' | '+' | '.join(str(byline[line][s]) for s in ['complete','partial','blocked','pending'])+' |' for line in lines])
# Current subject views are generated separately from execution accounting.
import sys
sys.path.insert(0, str(ROOT / 'tools'))
from build_mind_change import build as build_subject_views
from checkpoint_archive import build as build_archive
build_subject_views()
import subprocess
subprocess.run([sys.executable, str(ROOT / 'tools/check_mind_change.py')], check=True)
build_archive()
print(json.dumps({'updated_utc': now, 'applications': dict(counts),
                  'verified_selected_source_missing': audit['selected_skills_without_verified_source']}))
