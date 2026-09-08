from pathlib import Path
import json,datetime,re
ROOT=Path(__file__).resolve().parent
SLOTS=[('satr',1),('satr',2),('uf',1),('boc',1),('adep',1)]
def put(name,intent,start,body,actual,benefit,verdict,organization,next_attempts,depth,status='complete',missing=None,novelty=None,later_use=None):
 skill=name.split('-')[0]
 s=f'Intended mind change: {intent}\n\nStarting working judgment: {start}\n\nActor: methods utility/options handoff agent operating on stored artifacts and finite constructed cases.\n\nOriginal source: ../sources/conditions-handoff-{skill}.original.md; separate requirements: ../sources/conditions-handoff-{skill}.requirements.txt. Exact emission receipts: conditions-handoff-source-receipts.json.\n\nExecution scope and depth: {depth}\n\n'+body.strip()+f'\n\nActual mind change: {actual}\n\nBenefit: {benefit}\n\nVerdict: {verdict}\n\nOrganization: {organization}\n\nNext attempts: {next_attempts}\n'
 (ROOT/f'{name}.md').write_text(s)
 path=ROOT/'conditions-handoff-results.json'
 rows=json.loads(path.read_text()) if path.exists() else [{'skill_id':sk,'application_number':n,'file':str(ROOT/f'{sk}-{n:02d}.md'),'status':'pending','source_fidelity':'Exact source loaded/read; application pending','depth_status':'pending','missing_requirements':['Application not executed'],'verdict':None,'novelty':'unresolved','later_use':None} for sk,n in SLOTS]
 for r in rows:
  if name==f"{r['skill_id']}-{r['application_number']:02d}":r.update(file=str(ROOT/f'{name}.md'),status=status,source_fidelity='Exact stdout and separate requirements fully read; emission hashes retained',depth_status=depth,missing_requirements=missing or [],verdict=verdict,novelty=novelty or ('new_within_case' if verdict=='KEEP' else 'unresolved' if verdict=='UNRESOLVED' else 'repeated'),later_use=later_use or organization)
 path.write_text(json.dumps(rows,indent=2)+'\n')
 print(name,status,verdict)
