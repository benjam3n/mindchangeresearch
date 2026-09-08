from pathlib import Path
import json,re
from write_records import ROOT
partial={
 'kta-01':['Human listening/exposure and sustainable trigger have not been performed.'],
 'kta-02':['Original physical approach-to-tools test requires a person and has no observed result.'],
 'kta-03':['Required cooperation and human action have not occurred; individual-action override reached.'],
 'rso-02':['No actual reader throughput or cycle-time measurement; eight structural lookup routes only.'],
 'lt-01':['Target-domain human channel-sequencing pilot and comprehension comparison unperformed.'],
 'memy-01':['Scheduled delayed review and across-time retention stages unperformed; current artifact lookups only.'],
 'memy-02':['Human encoding, actual review schedule and later retrieval unperformed.'],
 'memy-03':['Delayed review unperformed; redundancy conclusion is current artifact inspection only.'],
 'spr-01':['Daily review habit, repeated due reviews, maintenance from actual failures, retention measurement unperformed.'],
 'spr-02':['Doing-skill route designed; human baseline, practice cycles, review habit and retention measurement unperformed.'],
 'acr-01':['Unaided context closure cannot be demonstrated for the agent; delayed retrieval stages unperformed.'],
 'acr-02':['Human exposure, closed-material retrieval, feedback and delayed varied attempts unperformed.'],
 'ska-01':['Original timed warmup/focused/integration/recovery cycle and later reassessment not fully performed.'],
 'ska-02':['Human motor baseline, practice cycle, recovery and later reassessment unperformed.'],
 'dlp-01':['Original full timed session and between-session recovery/longitudinal assessment unperformed.'],
 'dlp-02':['Human performance/10–20 actual attempts, calibrated difficulty and practice sessions unperformed.']}
blocked={'lrs-01':['No outreach campaign dataset: contact, response, channel, tier, cost and meeting inputs absent.']}
repeated={'ecal-01','ecal-03','to-02','lt-03','memy-03','enough-01','pt-02'}
local={'nstep-01','rso-01','td-01','de-01','rso-02','rso-03','ecal-02','enough-02','pt-01'}
rows=[]
for sk in json.loads((ROOT/'allocation.json').read_text()):
 for n in range(1,sk['applications']+1):
  name=f"{sk['id']}-{n:02d}";p=ROOT/f'{name}.md';exists=p.exists();s=p.read_text() if exists else ''
  m=re.search(r'^Verdict: (KEEP|REJECT|UNRESOLVED)',s,re.M)
  status='pending' if not exists else 'blocked' if name in blocked else 'partial' if name in partial else 'complete'
  rows.append({'skill_id':sk['id'],'application_number':n,'file':str(p),'status':status,'source_fidelity':'Exact stdout and separate requirements read; receipts retained' if exists else 'Exact source loaded and read; application pending','depth_status':('8x explicit floors documented' if sk['id'] in ['enough','tobd','hsi'] else 'No numerical 8x scale in original; actual expansion and source-specific limits disclosed') if exists else 'pending application','missing_requirements':blocked.get(name,partial.get(name,[])) if exists else ['Application not yet executed'],'verdict':m.group(1) if m else None,'novelty':('repeated' if name in repeated else 'local_adoption' if name in local else 'unresolved' if not m or m.group(1)=='UNRESOLVED' or name in blocked else 'new_within_case'),'later_use':re.search(r'^Organization: (.+)',s,re.M).group(1) if exists and re.search(r'^Organization: (.+)',s,re.M) else None})
(ROOT/'application-ledger.json').write_text(json.dumps(rows,indent=2)+'\n')
counts={k:sum(r['status']==k for r in rows) for k in ['complete','partial','blocked','pending']}
print(json.dumps(counts))
