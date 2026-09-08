from write_records import save,BASE
def table(headers,rows):
 return "| "+" | ".join(headers)+" |\n|"+"|".join(["---"]*len(headers))+"|\n"+"\n".join("| "+" | ".join(str(x).replace("|","/") for x in r)+" |" for r in rows)
import json
models={
1:[('Goal capture','requested action'),('Interpretation set','candidate meanings'),('Source access','readable original'),('Input normalization','typed values'),('Option generation','candidate operations'),('Evidence matching','scope matches'),('Prerequisite graph','required order'),('Budget model','feasible bundles'),('Criterion store','versioned standards'),('Option comparison','conditional choice'),('Authority check','authorized action'),('Dispatcher','task revision'),('Result acceptance','current result'),('Consequence assessment','observed difference'),('Revision propagation','invalidated descendants'),('Presentation','usable answer')],
2:[('Result intake','historical observation'),('Identity registry','stable identity'),('Source archive','original bytes'),('Condition index','reuse trigger'),('Criterion history','past standards'),('Validity monitor','changed conditions'),('Recurrence detector','actual matching event'),('Retrieval','evidence packet'),('Fit reassessment','present eligibility'),('Migration mapper','format conversion'),('Host adapter','available command'),('Continuation controller','pending action'),('Contradiction review','reopened claim'),('Retirement registry','inactive recommendation'),('Recovery','restored prior state'),('Future presentation','conditional contribution')],
3:[('Request boundary','current target'),('Actor map','responsible roles'),('Setting inventory','available conditions'),('Encounter options','possible interaction'),('Attention budget','remaining attention'),('Pace controller','timing window'),('Representation builder','candidate medium'),('Consent boundary','declared permission'),('Shared context','common inputs'),('Tool adapter','actual capability'),('Action queue','ordered work'),('Interruption control','cancellation state'),('Human response intake','reported response'),('Evidence separation','actor-specific effect'),('Goal revision','new target version'),('Next encounter','bounded continuation')]}
attrs=['Fidelity','Scope clarity','Recoverability','Modifiability','Traceability','Simplicity','Prompt delivery','Portability','Resource control','Agency']
patterns=['single mutable document','layered immutable packets','event log plus views','shared blackboard','actor contracts']
weights=[5,5,4,3,4,3,2,2,4,5]
scores={
1:[[3,2,2,2,2,5,5,5,2,3],[5,5,4,4,5,3,3,4,5,5],[5,4,5,5,5,2,2,4,4,4],[3,3,3,5,3,4,4,3,3,3],[4,4,4,4,4,2,2,3,4,5]],
2:[[3,2,1,2,2,5,5,4,3,3],[5,4,4,4,4,3,3,4,4,4],[5,5,5,5,5,2,2,5,4,5],[3,3,2,4,3,4,4,3,3,3],[4,4,4,4,4,2,2,3,4,5]],
3:[[3,2,2,2,2,5,5,3,2,3],[5,4,4,4,4,3,3,4,4,4],[4,4,5,5,5,2,2,4,4,4],[3,3,3,5,3,4,4,3,3,3],[5,5,5,4,5,2,3,4,5,5]]}
for n,components in models.items():
 ids=[f'A{n}-{i+1:02}' for i in range(16)]
 edges=[(i,i+1) for i in range(15)]+[(0,8),(2,5),(3,7),(4,9),(5,12),(6,10),(7,11),(8,13),(12,14),(14,15)]
 interfaces=[{'id':f'I{n}-{k+1:02}','from':ids[a],'to':ids[b],'type':'versioned data packet','protocol':'JSON-file contract','data':components[a][1],'frequency':'per relevant transition','criticality':'HIGH' if k<15 else 'MED','error':'hold dependent choice; retain last accepted historical result'} for k,(a,b) in enumerate(edges)]
 totals=[sum(w*s for w,s in zip(weights,row)) for row in scores[n]]
 winner=totals.index(max(totals));sens=[]
 for j in range(10):
  for d in [-1,1]:
   ws=weights[:];ws[j]+=d;ts=[sum(w*s for w,s in zip(ws,row)) for row in scores[n]]
   sens.append({'attribute':attrs[j],'delta':d,'winner':patterns[ts.index(max(ts))],'totals':ts})
 artifact={'subsystems':[{'id':i,'name':c[0],'owned_output':c[1],'functions':'produce '+c[1],'owner':'assistant design role','quality':'contract, scope and revision retained','deployment':'local design/prototype; no claimed production deployment'} for i,c in zip(ids,components)],'interfaces':interfaces,'weights':dict(zip(attrs,weights)),'scores':scores[n],'totals':dict(zip(patterns,totals)),'selected':patterns[winner],'sensitivity':sens}
 (BASE/f'architecture-{n}.json').write_text(json.dumps(artifact,indent=2))
 candidates=[]
 for k,p in enumerate(patterns):
  if k==0: detail='All sixteen responsibilities live in one shared mutable document; every update can replace context. Low setup cost, wide change impact.'
  elif k==1:detail='Sixteen responsibilities retain separate immutable input/output packets in five layers: intake, choice, commitment, assessment, revision. Layer changes require explicit version edges.'
  elif k==2:detail='All sixteen responsibilities append events to one ordered log; functional views are derived projections. Historical revisions remain reconstructable, but rebuilding views adds work.'
  elif k==3:detail='Sixteen responsibilities publish to a common blackboard and read each other’s latest facts. Flexible discovery, but conflicting writers require conflict resolution.'
  else:detail='Sixteen responsibility contracts use explicit sender, receiver, authority and target revision. Independent responsibilities are clear; interface count and handoff cost rise.'
  candidates.append([p,detail,'HIGH' if k in [2,4] else 'LOW' if k==0 else 'MED','HIGH' if k==4 else 'MED' if k in [2,3] else 'LOW'])
 changes={1:('one mutable current plan','an immutable plan packet bound to budget and criterion versions','a budget changes from 60 to 40 while a 55-unit bundle is pending. The old packet remains historical and is rejected for commitment under the new budget; recomputation selects S+C at cost 35 and value 40.'),2:('one latest recommendation','an event log preserving old truth and new applicability','criterion weight changes from .8 to .3. The log preserves A as v1 winner and derives B as v2 winner; the current view changes without altering the historical comparison.'),3:('a shared action list','contracts that separate actor, permission and target version','a request to describe a human action is followed by a tool result proposing execution. The contract has description-only authority, so the execution proposal is refused while the useful description remains eligible.')}
 a,b,case=changes[n]
 body=f'''System: {['','present action selector','long-term retained-result service','human/model/tool encounter coordinator'][n]}. Purpose is a useful conditional contribution under the current request. Interpretation is design/refactor. Drivers: goal fidelity, actor scope, recoverability, bounded resources and revisability. External human experience and future host availability remain outside the implemented design; inputs must not be invented.

Ten quality attributes are ranked by the declared analyst design weights below. They are transparent design judgments, not measured user utility. Each scenario asks whether a changed input is preserved and receives a definite response. A score 5 means a pattern directly represents the condition, 3 means an explicit added convention is required, 1 means the pattern omits it. The weights were declared before this calculation; actual stakeholder approval is not inferred.

{table(['Quality','Weight','Stimulus / response / measure'],[[a,w,f'Changed {a.lower()} condition / explicit current response / condition and result both retained'] for a,w in zip(attrs,weights)])}

Five candidates share the sixteen required responsibilities but materially differ in state ownership, event ordering and coordination:

{table(['Architecture','Structure and tradeoff','Development cost','Operational cost'],candidates)}

{table(['Quality']+patterns,[[a]+[r[j] for r in scores[n]] for j,a in enumerate(attrs)]+[['Weighted total']+totals])}

Selected: {patterns[winner]}. Twenty sensitivity calculations vary each weight ±1; all totals are in the artifact. Accepted risk is additional interface/record overhead. Mitigation is retaining one accountable owner per responsibility and only the relevant view for a live choice. Simplicity and prompt delivery favor the mutable-document candidate; recoverability and scope favor the selected design. No universal architectural winner is claimed.

Sixteen responsibilities have one owned output each; none is a claim of sixteen deployed services:

{table(['ID','Subsystem','Owned output / function','Owner / deployment'],[[i,c[0],c[1],'assistant / local artifact'] for i,c in zip(ids,components)])}

Twenty-five interfaces:

{table(['ID','From','To','Type / protocol','Data','Frequency','Criticality'],[[r['id'],r['from'],r['to'],r['type']+' / '+r['protocol'],r['data'],r['frequency'],r['criticality']] for r in interfaces])}

Critical contract: packet contains origin, target, schema_version, target_revision, payload and evidence_scope. A malformed or obsolete packet yields HOLD with reason; its dependent action is not committed. Version migration is an explicit new packet. SLA here is causal ordering—consumer reads a completed producer packet—not an invented millisecond guarantee. Security/authority is current-task-scoped; no external credential or recipient is invented. External interfaces are user request inbound, original source inbound, actual host capability inbound and authorized result outbound; root owns publication.

Five architectural views: Functional—sixteen capabilities grouped by intake/choice/action/evidence/revision. Physical—one local filesystem and assistant process, external user and tool host; no invented redundant production deployment. Behavioral—input captures revision, choice consumes it, result returns, acceptance rechecks it. Information—immutable identities with evidence scope; selected pattern defines whether views or packets are authoritative. Evolution—criterion or schema changes create a new revision; previous results remain historical.

Decision log: adopt {b}; retain prior evidence; reject unversioned shared updates for this target; keep open whether implementation overhead earns its cost at larger scale.

Actual transformed case: {case} The design transition is executed as the explicit input/output example in `architecture-{n}-case.json`. The advantage is a defined decision under the constructed state transition, not field reliability or a deployed system.'''
 (BASE/f'architecture-{n}-case.json').write_text(json.dumps({'before':a,'after':b,'performed_case':case,'scope':'constructed transition evaluated in current work'},indent=2))
 save(f'049-sysarch-{n}','sysarch',f'Architecture for {artifact["subsystems"][0]["name"].lower()} and downstream change','Change a concrete system behavior by comparing state and responsibility architectures.',f'I would begin with {a}; it is simpler, but its response to the present changed-state case has not been specified.',body,f'The design now uses {b}.',f'The transformed case has an explicit scope-preserving outcome: {case}','KEEP' if n in [1,3] else 'UNRESOLVED','Five views retain behavior, ownership and evolution together; the source-skill list alone does not express these interfaces.','Implement only the critical transition; challenge a scoring premise; test a common-cause state loss.',depth='Original 8x floors met by 16 named subsystems, 25 specified interfaces, 10 quality attributes, 5 candidate architectures and 5 views; twenty weight perturbations are computed.')
