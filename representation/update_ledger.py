from pathlib import Path
import json,re
R=Path('/workspace/scratch/78b838bd97fc/mind-change-research/representation')
alloc=json.loads((R/'allocation.json').read_text())
files={}
for p in R.glob('[0-9][0-9][0-9]-*.md'):
 a=p.stem.split('-'); files[(a[1],int(a[2]))]=p
local={('orgn',1),('orgn',2),('sim',1),('ro',1),('alt',2)}
repeated={('sim',2),('anag',1),('ma',1)}
uses={('orgn',1):['003-ro-1.md','consolidation-01.md'],('orgn',2):['consolidation-01.md'],('sim',1):['consolidation-01.md'],('ro',1):['004-orgn-2.md','consolidation-01.md'],('sim',3):['007-orgn-3.md','009-alt-2.md','consolidation-02.md'],('alt',1):['consolidation-02.md'],('alt',2):['consolidation-02.md'],('ctcov',1):['012-difr-1.md','013-difr-2.md','consolidation-02.md'],('difr',1):['013-difr-2.md','020-ma-1.md','consolidation-03.md'],('difr',2):['015-omtx-1.md','018-anag-2.md','consolidation-03.md'],('difr',3):['consolidation-03.md'],('omtx',1):['016-nusr-1.md','consolidation-03.md'],('nusr',1):[],('met',1):['021-ma-2.md']}
explicit={'ro','ma','wre','draft','cda','categorize'}
rows=[]
for a in alloc:
 for run in range(1,a['applications']+1):
  p=files.get((a['id'],run)); s=p.read_text() if p else ''
  m=re.search(r'^Verdict: (KEEP|REJECT|UNRESOLVED)',s,re.M)
  ver=m.group(1) if m else None
  status='complete' if p else 'pending'
  rows.append({'skill_id':a['id'],'application_number':run,'file':p.name if p else None,'status':status,'source_fidelity':'exact source and separate requirements loaded; original operations present' if p else 'source captured; execution pending','depth_status':('explicit_8x_floors_recorded' if a['id'] in explicit else 'expanded_execution_original_has_no_numeric_8x_definition') if p else 'pending','missing_requirements':[] if p else ['original-procedure execution and outcome record'],'verdict':ver,'novelty':('local_adoption' if (a['id'],run) in local else 'repeated' if (a['id'],run) in repeated else 'unresolved' if ver=='UNRESOLVED' or not p else 'new_within_case'),'later_use':uses.get((a['id'],run),[])})
(R/'application-ledger.json').write_text(json.dumps(rows,indent=2))
print(json.dumps({'slots':len(rows),'complete':sum(r['status']=='complete' for r in rows),'pending':sum(r['status']=='pending' for r in rows)}))
