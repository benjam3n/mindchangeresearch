from pathlib import Path
import json
BASE=Path('/workspace/scratch/78b838bd97fc/mind-change-research/values')
ALLOC={x['id']:x for x in json.loads((BASE/'allocation.json').read_text())}
INDEX=BASE/'index.json'

def add(skill,n,title,intent,start,body,change,benefit,verdict,organization,next_attempts,depth,transfer=''):
    key=f"{ALLOC[skill]['rank']:03d}-{skill}-{n}"
    path=BASE/(key+'.md')
    text=f'''Intended mind change: {intent}\n\n# {title}\n\nApplication: {key}. Actor: this assistant's current working model and generated artifacts unless a constructed case is explicitly identified. Human outcomes are not observed.\n\nStarting working judgment: {start}\n\nSource: ../sources/values-{skill}.md. Requirements receipt: ../sources/values-{skill}.receipt.txt. Original loaded through read_original.py; byte checks are recorded separately in source-integrity.json.\n\nDepth: {depth}\n\n{body.strip()}\n\n'''
    if transfer:text+=f"Subsequent application, executed: {transfer}\n\n"
    text+=f'''Actual mind change: {change}\n\nBenefit: {benefit}\n\nVerdict: {verdict}\n\nOrganization: {organization}\n\nNext attempts: {next_attempts}\n'''
    path.write_text(text)
    rows=json.loads(INDEX.read_text()) if INDEX.exists() else []
    row={'key':key,'skill':skill,'application':n,'title':title,'file':path.name,'verdict':verdict,'change':change,'benefit':benefit,'transfer':transfer,'depth':depth}
    rows=[r for r in rows if r['key']!=key]+[row]
    INDEX.write_text(json.dumps(rows,indent=2))
    progress={'status':'in_progress','assigned':50,'documents_written':len(rows),'keeps':sum(r['verdict']=='KEEP' for r in rows),'rejects':sum(r['verdict']=='REJECT' for r in rows),'unresolved':sum(r['verdict']=='UNRESOLVED' for r in rows),'last_completed':key}
    (BASE/'progress.json').write_text(json.dumps(progress,indent=2))

N='The original specifies no numerical 8x scaling. All presently executable stages are addressed; unavailable live stages are recorded separately. Expanded scope is stated rather than inventing an 8x certification.'
if __name__=='__main__':
 print('Record writer ready')
