from pathlib import Path
import json,re
R=Path('/workspace/scratch/78b838bd97fc/mind-change-research/inquiry')
alloc=json.loads((R/'allocation.json').read_text());by={x['id']:[] for x in alloc}
for p in sorted(R.glob('[0-9][0-9]-*.md')):
 sk=p.name.split('-')[1]
 if sk in by:by[sk].append(p)
rows=[]
for a in alloc:
 for i in range(1,a['applications']+1):
  ps=by[a['id']];p=ps[i-1] if len(ps)>=i else None;t=p.read_text() if p else '';v=re.findall(r'^Verdict: (KEEP|REJECT|UNRESOLVED)',t,re.M)
  status='pending' if p is None else 'partial' if ('Dependency status: PENDING' in t or 'Depth status: PARTIAL' in t) else 'blocked' if 'Depth status: BLOCKED' in t else 'complete'
  missing=['required GG/QAG dependency and later use'] if 'Dependency status: PENDING' in t else ['see source-specific unperformed operations in record'] if 'Depth status: PARTIAL' in t or 'Depth status: BLOCKED' in t else []
  later=re.search(r'(?:Distinct later (?:application|operation|action):|Actual use:)(.*?)(?:\n\n|$)',t,re.S)
  novelty='unresolved'
  if v and v[-1]=='KEEP':novelty='new_within_case'
  if 'no new keep' in t.lower() or 'no independent new' in t.lower():novelty='repeated'
  rows.append({'skill_id':a['id'],'application_number':i,'file':p.name if p else None,'status':status,'source_fidelity':'exact original read with separate receipt; see source-receipt-audit.json' if p else 'not executed','depth_status':'met as recorded' if status=='complete' else 'pending' if status=='pending' else 'unmet requirements recorded','missing_requirements':missing,'verdict':v[-1] if v else 'UNRESOLVED','novelty':novelty,'later_use':later.group(1).strip() if later else None})
(R/'application-ledger.json').write_text(json.dumps(rows,indent=2)+'\n')
progress={'line':'inquiry','assigned_applications':len(rows),'complete':sum(x['status']=='complete' for x in rows),'partial':sum(x['status']=='partial' for x in rows),'blocked':sum(x['status']=='blocked' for x in rows),'pending':sum(x['status']=='pending' for x in rows),'substantive_keeps':sum(x['verdict']=='KEEP' for x in rows),'rejects':sum(x['verdict']=='REJECT' for x in rows),'unresolved_attempts':sum(x['verdict']=='UNRESOLVED' and x['status']!='pending' for x in rows),'consolidations':len(list(R.glob('consolidation-[0-9][0-9].md'))),'ledger':'application-ledger.json','source_receipts':'source-receipt-audit.json','graph':'questionroute-original-exports.json'}
(R/'progress.json').write_text(json.dumps(progress,indent=2)+'\n');print(progress)
