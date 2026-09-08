from write_support import *
ledger=json.loads((D/'application-ledger.json').read_text());by={(x['skill_id'],x['application_number']):x for x in ledger}
p=json.loads((D/'progress.json').read_text())
for r in p['records']:
 sk,num=r['id'].rsplit('-',1);x=by[(sk,int(num))]
 if x.get('author')=='root':continue
 x.update(file='methods/'+r['file'],status='complete' if r['status']=='executed' else 'partial',verdict=r['verdict'])
 if x['status']=='complete':
  x['missing_requirements']=[]
  if x['depth_status'].startswith('pending'):x['depth_status']='Original operations executed; numerical floors where defined; see record for actual expanded scope.'
  if x['novelty']=='unresolved':x['novelty']='new_within_case' if r['verdict']=='KEEP' else ('local_adoption' if sk in ['sp','wsib'] else 'repeated')
root=D/'root-slot-results.json'
if root.exists():
 for row in json.loads(root.read_text()):
  x=by[(row['skill_id'],row['application_number'])];x.update(row);x['file']='methods/'+row['file']
  name=f"{row['skill_id']}-{row['application_number']:02}"
  if not any(r['id']==name for r in p['records']):p['records'].append({'id':name,'skill':row['skill_id'],'verdict':row['verdict'],'status':'executed' if row['status']=='complete' else 'partial','file':row['file'],'author':'root'})
(D/'application-ledger.json').write_text(json.dumps(ledger,indent=2));p['attempts_recorded']=len(p['records']);p['procedures_executed']=sum(x['status']=='complete' for x in ledger);p['keep_records']=sum(x['verdict']=='KEEP' for x in ledger);(D/'progress.json').write_text(json.dumps(p,indent=2))
print({s:sum(x['status']==s for x in ledger) for s in ['complete','partial','blocked','pending']})
