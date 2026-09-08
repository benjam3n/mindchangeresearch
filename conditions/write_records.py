from pathlib import Path
import json,datetime,re
ROOT=Path('/workspace/scratch/78b838bd97fc/mind-change-research/conditions')
def put(name,intent,start,body,actual,benefit,verdict,organization,next_attempts,depth=None):
 skill=name.split('-')[0]
 src=f'Original source: ../sources/conditions-{skill}.original.md. Exact stdout and separate requirements receipt: ../sources/conditions-{skill}.requirements.txt; byte checks are in source-receipts.json.' if skill!='consolidation' else 'Provenance: only the cited KEEP records below enter this consolidation.'
 text=f'Intended mind change: {intent}\n\nStarting working judgment: {start}\n\n{src}\n\n'
 if depth:text+=f'Execution scope and depth: {depth}\n\n'
 text+=body.strip()+f'\n\nActual mind change: {actual}\n\nBenefit: {benefit}\n\nVerdict: {verdict}\n\nOrganization: {organization}\n\nNext attempts: {next_attempts}\n'
 (ROOT/f'{name}.md').write_text(text)
def refresh():
 import subprocess,sys
 subprocess.run([sys.executable,str(ROOT/'update_ledger.py')],check=True,capture_output=True,text=True)
 ledger=json.loads((ROOT/'application-ledger.json').read_text())
 ids=lambda status:[f"{r['skill_id']}-{r['application_number']:02d}" for r in ledger if r['status']==status]
 records=[f"{r['skill_id']}-{r['application_number']:02d}" for r in ledger if r['status']!='pending']
 keeps=[f"{r['skill_id']}-{r['application_number']:02d}" for r in ledger if r['verdict']=='KEEP']
 consolidations=sorted(p.stem for p in ROOT.glob('consolidation-*.md'))
 counts={k:len(ids(k)) for k in ['complete','partial','blocked','pending']}
 prog={'line':'conditions','actor':'conditions subagent','allocated_applications':50,'recorded_applications':records,'completed_applications':ids('complete'),'partial_applications':ids('partial'),'blocked_applications':ids('blocked'),'pending_applications':ids('pending'),'execution_counts':counts,'keeps':keeps,'consolidations':consolidations,'status':'available_work_addressed' if not ids('pending') else 'executing','updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'completion_meaning':'Completed means original application operations executed within the declared agent/design scope. Partial and blocked procedures are separate. A verdict or a written design is not proof of human effect, delayed retention, or durable agent learning.'}
 (ROOT/'progress.json').write_text(json.dumps(prog,indent=2)+'\n')
 print(f"{len(records)}/50 recorded; execution={counts}; {len(keeps)} KEEP; {len(consolidations)} consolidations")
if __name__=='__main__':refresh()
