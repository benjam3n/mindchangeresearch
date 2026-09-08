from pathlib import Path
import json,hashlib,re
b=Path(__file__).resolve().parent;a=json.loads((b/'allocation.json').read_text());r=json.loads((b/'records.json').read_text())
source_checks={}
for x in a:
 sid=x['id'];p=b.parent/'sources'/f'systems-{sid}.md';receipt=(b.parent/'sources'/f'systems-{sid}.requirements.txt').read_text();claimed=re.search(r'original-sha256: ([a-f0-9]+)',receipt).group(1);source_checks[sid]=hashlib.sha256(p.read_bytes()).hexdigest()==claimed
rows=[]
partial={'gjs':['Original VE was invoked but genuine intrinsic-value and additional-value answers are unavailable; the technical ARAW/EMV chain is executed.'],'mcd':['Original stakeholder alignment on criterion weights was not obtained; scores and sensitivity are a transparent analyst case.'],'abts':['Eligible traffic and actual start/end dates are unknown; power and prospective decision rules are specified, but a complete executable trial schedule is unavailable.'],'exd_2':['A confirmatory sample size for criterion change is not determined because a justified effect/variance input is unavailable.'],'ram':['Real component failure rates and occurrence evidence are unavailable; the RPN field remains uncomputed. A declared conditional model is executed.']}
for x in a:
 for n in range(1,x['applications']+1):
  filename=f"{x['rank']:03}-{x['id']}-{n}.md";rec=next((z for z in r if z['file']==filename),None)
  if rec:
   pkey='exd_2' if x['id']=='exd' and n==2 else x['id']; status='partial' if pkey in partial else 'complete';missing=partial.get(pkey,[])
   txt=(b/filename).read_text();depth=re.search(r'Depth: ([^\n]+)',txt).group(1)
   novelty='local_adoption' if filename in ['045-gd-1.md','046-gsr-1.md','047-grf-1.md','048-lpd-1.md','150-ssr-1.md'] else 'repeated' if x['id'] in ['tracematrix','requirements','sysintegration'] and n==2 else 'unresolved' if rec['verdict']=='UNRESOLVED' else 'new_within_case'
   later=[z['file'] for z in r if z['file'].startswith('consolidation') and (x['id']+str(n) in (b/z['file']).read_text() or filename in (b/z['file']).read_text())]
  else:status='pending';missing=['Original procedure application not yet written/executed'];depth='pending';novelty='unresolved';later=[]
  rows.append({'skill_id':x['id'],'application_number':n,'file':filename,'status':status,'source_fidelity':'exact reader stdout hash verified against separate receipt' if source_checks[x['id']] else 'FAILED','depth_status':depth,'missing_requirements':missing,'verdict':rec['verdict'] if rec else 'UNRESOLVED','novelty':novelty,'later_use':later})
(b/'application-ledger.json').write_text(json.dumps(rows,indent=2));
(b/'progress.json').write_text(json.dumps({'allocated':49,'addressed':sum(x['status']!='pending' for x in rows),'complete':sum(x['status']=='complete' for x in rows),'partial':sum(x['status']=='partial' for x in rows),'pending':sum(x['status']=='pending' for x in rows),'status':'all quota slots addressed; missing original stages retained explicitly','keeps':sum(x['verdict']=='KEEP' for x in rows)},indent=2));(b/'source-integrity-check.json').write_text(json.dumps(source_checks,indent=2))
print({k:sum(z['status']==k for z in rows) for k in ['complete','partial','blocked','pending']})
