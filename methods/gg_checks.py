from write_support import *
exports=json.loads((ROOT/'inquiry/questionroute-original-exports.json').read_text())
byid={x['data']['question']['id']:x for x in exports}
sure=byid['sure']['data']
edges=[]
for e in sure['outgoing']:
 edges.append({'source':'sure','target':e['targetId'],'relation':e['type'],'weight':e['weight'],'original_reason':e['reason'],'target_definition':byid[e['targetId']]['data']['question']['definition'],'endorsed_inference':None,'scope':{'actor':None,'proposition':None,'time':None,'sense':None}})
(D/'sure-edge-overlay.json').write_text(json.dumps(edges,indent=2))
checks={'first_hop_edges':len(edges),'contradiction_edges':sum(x['relation']=='contradiction' for x in edges),'unique_contradiction_reasons':len({x['original_reason'] for x in edges if x['relation']=='contradiction'}),'source_reason_preserved':all(x['original_reason']==e['reason'] for x,e in zip(edges,sure['outgoing'])),'weights':sorted(set(x['weight'] for x in edges)),'unfilled_scope_fields':sum(v is None for x in edges for v in x['scope'].values())}
# Finite logical fixtures, defined independently of source self-assessment.
cases=[{'case':'same P same time','left':('model','P','t','probability_one'),'right':('model','P','t','strictly_between_zero_one')}, {'case':'P versus Q','left':('model','P','t','probability_one'),'right':('model','Q','t','strictly_between_zero_one')},{'case':'same P different time','left':('model','P','t','probability_one'),'right':('model','P','u','strictly_between_zero_one')},{'case':'different actor','left':('model','P','t','probability_one'),'right':('reader','P','t','strictly_between_zero_one')},{'case':'subjective sure','left':('model','P','t','subjective_report'),'right':('model','P','t','strictly_between_zero_one')}]
def verdict(c):
 l,r=c['left'],c['right']
 if l[:3]!=r[:3]:return 'no contradiction established by these scoped labels'
 if l[3]=='subjective_report':return 'unresolved without a relation between report and credence'
 return 'incompatible under declared probability definitions'
checks['scope_fixtures']=[{'case':c['case'],'label_only':'contradiction','scoped':verdict(c)} for c in cases]
(D/'gg-01-observations.json').write_text(json.dumps(checks,indent=2))
# Actual in-session serialization/restore and a changed-version input.
source=ROOT/'inquiry/09-spd-timing.md'
import hashlib
capsule={'exact_input':'Find changes of timing, pace, control channel, and preserved state that can make the next mind-change attempt occur under the actual capabilities of this active model session and a later resumed session.','next_operation':'inspect the first incomplete dependency and execute a ready independent slot','source_path':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'status':'saved; not scheduled','required_depth':'original 8x floors','unresolved_dependency':'later session must be explicitly resumed through an available host channel','invalidated_by':['changed user goal','changed source bytes','missing required capability','expired opportunity'],'observed_scope':'current active model session only'}
(D/'resumption-capsule.json').write_text(json.dumps(capsule,indent=2));restored=json.loads((D/'resumption-capsule.json').read_text())
obs={'exact_roundtrip':capsule==restored,'source_available':Path(restored['source_path']).exists(),'current_source_matches':hashlib.sha256(Path(restored['source_path']).read_bytes()).hexdigest()==restored['source_sha256'],'schedule_acknowledgment':None,'current_restore_not_later_session':True,'changed_source_fixture_action':'re-read before relying on preserved source','changed_user_goal_fixture_action':'recompute next operation; preserve historical preparation'}
(D/'gg-02-observations.json').write_text(json.dumps(obs,indent=2))
print(checks);print(obs)
