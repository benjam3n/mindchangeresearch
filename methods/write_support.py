from pathlib import Path
import json
ROOT=Path('/workspace/scratch/78b838bd97fc/mind-change-research')
D=ROOT/'methods'
def record(name,intent,start,body,change,benefit,verdict,organization,nexts,depth='Original source defines no numerical 8x floor. The record expands the actual operations and reports its concrete scope; it makes no numerical 8x certification.',status='executed'):
 skill=name.rsplit('-',1)[0]
 text=f'Intended mind change: {intent}\n\nActual starting judgment: {start}\n\nOriginal: ../sources/methods-{skill}.original.md. Separate requirements receipt: ../sources/methods-{skill}.requirements.txt.\n\nDepth: {depth}\n\n{body.strip()}\n\nActual mind change: {change}\n\nBenefit: {benefit}\n\nVerdict: {verdict}\n\nOrganization: {organization}\n\nNext attempts: {nexts}\n'
 (D/f'{name}.md').write_text(text)
 p=D/'progress.json'
 data=json.loads(p.read_text()) if p.exists() else {'assigned_applications':49,'records':[],'consolidations':[]}
 data['records']=[x for x in data['records'] if x['id']!=name]+[{'id':name,'skill':skill,'verdict':verdict,'status':status,'file':f'{name}.md'}]
 data['attempts_recorded']=len(data['records']);data['procedures_executed']=sum(x['status']=='executed' for x in data['records']);data['keep_records']=sum(x['verdict']=='KEEP' for x in data['records'])
 p.write_text(json.dumps(data,indent=2))
def table(headers,rows):
 return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(c).replace('|','/') for c in row)+' |' for row in rows])
