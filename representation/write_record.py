from pathlib import Path
import json, hashlib, re
ROOT=Path('/workspace/scratch/78b838bd97fc/mind-change-research/representation')
receipts={r['id']:r for r in json.loads((ROOT/'source-receipts.json').read_text())}
def record(n,skill,run,title,intent,start,body,actual,benefit,verdict,organization,next_attempts,depth):
    r=receipts[skill]
    name=f'{n:03d}-{skill}-{run}.md'
    text=f'''Intended mind change: {intent}\n\n# {title}\n\nStarting working state: {start}\n\nInput and execution scope: This is application {run} of `{skill}` in the representation line. The actor whose working state is observed is this model in this local research run. Human effects are untested unless explicitly identified otherwise.\n\nSource: [original {skill}](../sources/representation-{skill}.md); [separate requirements](../sources/representation-{skill}.requirements.txt). Emitted source SHA-256 `{r['source_sha256']}`. The complete receipt is in [source-receipts.json](source-receipts.json).\n\nDepth accounting: {depth}\n\n{body.strip()}\n\nActual mind change: {actual}\n\nBenefit: {benefit}\n\nVerdict: {verdict}\n\nOrganization: {organization}\n\nNext attempts: {next_attempts}\n'''
    (ROOT/name).write_text(text)
    return name

def progress():
    files=sorted(ROOT.glob('[0-9][0-9][0-9]-*.md'))
    counts={}; verdicts={}; keeps=[]
    for p in files:
        skill=p.name.split('-')[1]; counts[skill]=counts.get(skill,0)+1
        m=re.search(r'^Verdict: (KEEP|REJECT|UNRESOLVED)',p.read_text(),re.M)
        if m:
            verdicts[m[1]]=verdicts.get(m[1],0)+1
            if m[1]=='KEEP':keeps.append(p.name)
    x={'line':'representation','assigned_applications':51,'completed_documents':len(files),'applications_by_skill':counts,'verdicts':verdicts,'keeps':keeps,'consolidations':[p.name for p in sorted(ROOT.glob('consolidation-*.md'))],'status':'in_progress'}
    (ROOT/'progress.json').write_text(json.dumps(x,indent=2))
    print(json.dumps(x))
