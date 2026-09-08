from pathlib import Path
import json
BASE=Path(__file__).resolve().parent

def save(name,skill,title,intent,start,body,change,benefit,verdict,organization,next_attempts,depth=None):
    text=f'''Intended mind change: {intent}

# {title}

Starting judgment: {start}

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-{skill}.md`; current requirements are retained separately in `../sources/systems-{skill}.requirements.txt`.

Depth: {depth or 'The original defines no numerical 8x floor. The expanded execution below covers the actual operations and multiple dependencies/countercases; no numerical 8x certification is asserted.'}

{body.strip()}

Actual mind change: {change}

Benefit: {benefit}

Verdict: {verdict}

Organization: {organization}

Next attempts: {next_attempts}
'''
    (BASE/f'{name}.md').write_text(text)
    ledger_path=BASE/'records.json'
    ledger=json.loads(ledger_path.read_text()) if ledger_path.exists() else []
    row={'file':f'{name}.md','skill':skill,'title':title,'verdict':verdict,'change':change,'benefit':benefit}
    ledger=[r for r in ledger if r['file']!=row['file']]+[row]
    ledger_path.write_text(json.dumps(ledger,indent=2))
    allocated=[r for r in ledger if r['file'][0].isdigit()]
    (BASE/'progress.json').write_text(json.dumps({'allocated':49,'executed':len(allocated),'keeps':sum(r['verdict']=='KEEP' for r in allocated),'status':'executing','records':allocated},indent=2))
