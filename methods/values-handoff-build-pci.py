from pathlib import Path
import json,copy,hashlib
b=Path(__file__).parent;P='values-handoff-'
def save(n,x): (b/(P+n)).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
schema={'name':'Local procedure tiers from PCI field requirements','origin':'Authored schema for these four local specifications; not an archived GOSM schema.','additional_fields':'preserved','tiers':{'Bronze':['id','name','version','description','steps'],'Silver':['inputs','outputs','when_to_use','examples'],'Gold':['failure_modes','gosm_integration','verification']},'types':{'id':'str','name':'str','version':'str','description':'str','steps':'list','inputs':'dict','outputs':'dict','when_to_use':'list','examples':'list','failure_modes':'list','gosm_integration':'dict','verification':'list'},'nonempty':True}
save('schema.json',schema)
# The file is loaded, rather than validating against an in-memory substitute.
schema=json.loads((b/(P+'schema.json')).read_text())
adds={
'invitation-record':{
'id':'local-invitation-record','version':'1.0.0','when_to_use':['A concrete invitation has separable requests and a supplied reply or explicit absence of reply.','Preparing a bounded collaboration draft without claiming live confirmation.'],
'examples':[
{'input':'Invitation: read and host. Reply: I will read two pages; I cannot host.','output':'Reading accepted for two pages; hosting declined; no motive inferred.'},
{'input':'Invitation: join once. Reply: Only if it is audio.','output':'Joining conditional on audio; a proposed audio arrangement remains unconfirmed.'},
{'input':'Invitation: attend. Reply absent.','output':'Attendance stance unknown; no assent or disinterest inferred.'},
{'input':'Invitation: read. Reply: I like the idea but cannot take this on.','output':'Positive stated interest; task declined; the predicates coexist.'}],
'failure_modes':[
{'failure':'Single overall yes label','consequence':'A bounded acceptance spreads to another request.','prevention':'Keep one stance per component.'},
{'failure':'Reading emotion into silence','consequence':'An absent reply becomes invented disinterest.','prevention':'Keep missing reply unknown.'},
{'failure':'Reason rewritten as motive','consequence':'An explicit timing constraint becomes reluctance.','prevention':'Retain evidence and mark extra interpretations hypothetical.'},
{'failure':'Condition dropped in summary','consequence':'A conditional offer becomes a commitment.','prevention':'Carry the condition into every derived output.'}],
'gosm_integration':{'after':'Invitation components and available reply are supplied.','before':'Local follow-up choice.','external_gate':'Actual confirmation requires the participant.','artifact_scope':'Local authored procedure, not an original skill.'}},
'followup-choice':{
'id':'local-followup-choice','version':'1.0.0','when_to_use':['A scoped response record is available and a draft next step is useful.','Several different stances occur in one reply.'],
'examples':[
{'input':'Reading accepted for two pages; hosting declined.','output':'Thank them for two-page reading; acknowledge no hosting; assign neither extra reading nor hosting.'},
{'input':'Joining conditional on audio; audio option available.','output':'Draft the audio option as a proposal with confirmation pending.'},
{'input':'Unknown whether “too much” concerns length or recurrence.','output':'Draft one question distinguishing those two meanings.'},
{'input':'All requested components explicitly declined.','output':'Acknowledge decline; do not generate persuasion as an accepted next step.'}],
'failure_modes':[
{'failure':'Goal silently replaced after refusal','consequence':'The original desired relationship disappears.','prevention':'Retain the desired goal and its current unmet components.'},
{'failure':'Draft is treated as delivery','consequence':'The record invents an interaction.','prevention':'Label draft and keep delivery unperformed.'},
{'failure':'Repeated invitation after a clear no','consequence':'Selection ignores the stated boundary.','prevention':'Choose bounded acknowledgement or no further action.'},
{'failure':'A promise attached to a conditional option','consequence':'Recipient appears committed before an answer.','prevention':'Preserve proposed and confirmed states.'}],
'gosm_integration':{'after':'Invitation response record.','before':'Any separately authorized human interaction.','external_gate':'No external message is authorized by this artifact.','artifact_scope':'Local draft selection.'}},
'curiosity-trace':{
'id':'local-curiosity-trace','version':'1.0.0','when_to_use':['A local exploration has a concrete input and output to preserve.','A proposed operation should remain visibly unperformed.'],
'examples':[
{'input':'Same question label placed at a platform and a drawing.','output':'Two constructed interpretations; no audience effect claimed.'},
{'input':'A causal experiment is proposed but not performed.','output':'Planned status; predicted result is a prediction.'},
{'input':'An explored metaphor produced no distinct comparison.','output':'Dead-end reason retained; interest can remain.'},
{'input':'A second note revises an earlier question.','output':'New trace linked to the earlier note and its changed question.'}],
'failure_modes':[
{'failure':'Interesting idea labeled true','consequence':'Value substitutes for evidence.','prevention':'Keep interest reason separate from evidence status.'},
{'failure':'Planned operation narrated in past tense','consequence':'An unperformed test becomes a result.','prevention':'Retain planned status.'},
{'failure':'Missing earlier record','consequence':'A later question loses its derivation.','prevention':'Carry a resolvable prior link or mark it unavailable.'},
{'failure':'No utility is coded as no value','consequence':'Pure-interest exploration disappears.','prevention':'Retain the stated interest reason without promised benefit.'}],
'gosm_integration':{'after':'Actual exploration operation or explicit plan.','before':'Continuation choice.','external_gate':'Human outcome claims need observations beyond a constructed trace.','artifact_scope':'Evidence-bearing local inquiry record.'}},
'continuation-choice':{
'id':'local-continuation-choice','version':'1.0.0','when_to_use':['Several threads compete for the next local operation.','A recorded result repeats an existing distinction.'],
'examples':[
{'input':'One repeated label comparison and one new object scene.','output':'Select the object scene for a different referent question; retain repeated thread if still interesting.'},
{'input':'A test requires an unavailable participant.','output':'Keep the human question pending and choose an available local operation without calling it that test.'},
{'input':'A pure-interest thread and a direct-use thread both fit the interval.','output':'Compare the current question and breadth needs; pure interest remains eligible.'},
{'input':'No concrete unresolved question survives.','output':'Stop this thread and retain its result; do not invent another pull.'}],
'failure_modes':[
{'failure':'Newest label receives automatic priority','consequence':'Renaming repetition displaces a distinct question.','prevention':'Compare the proposed operation with recorded outputs.'},
{'failure':'Unavailable human test is replaced by fictional responses','consequence':'The original causal question is falsely settled.','prevention':'Keep the original test pending and state the local operation\'s separate scope.'},
{'failure':'Hard dependency ignored','consequence':'Selected operation cannot occur in the interval.','prevention':'Read available resources and dependencies.'},
{'failure':'Deferred thread discarded','consequence':'Unfinished interest is lost.','prevention':'Retain its open question and reason for deferral.'}],
'gosm_integration':{'after':'Curiosity trace records exist.','before':'A new actual local operation, or a separately available empirical study.','external_gate':'Human participation, time and permission remain dependencies.','artifact_scope':'Local selection, not autonomous control of people.'}}
}

def validate(o):
 missing={};last='none';ok=True
 for tier,fields in schema['tiers'].items():
  miss=[f for f in fields if f not in o or not o[f] or type(o[f]).__name__!=schema['types'][f]]
  missing[tier]=miss
  if ok and not miss:last=tier
  else:ok=False
 return {'tier':last,'missing':missing}
reports=[]
for caseno,names in [(1,['invitation-record','followup-choice']),(2,['curiosity-trace','continuation-choice'])]:
 inv=[]
 for name in names:
  old=json.loads((b/(P+name+'.pcd.json')).read_text());v=validate(old)
  usage=1 if caseno==1 else 3;classification='domain-specific' if caseno==1 else 'meta'
  severity=3 if v['missing']['Bronze'] else 2 if 'examples' in v['missing']['Silver'] else 1
  effort=2 # Multi-field additions, with existing sections preserved: section_add, not rewrite.
  inv.append({'name':name,'usage_class':classification,'usage_weight':usage,'severity':'failing_schema','severity_weight':severity,'effort_class':'section_add','effort_estimate':effort,'priority':usage*severity/effort,'before':v})
 inv.sort(key=lambda r:(-r['priority'],r['name']))
 for row in inv:
  name=row['name'];old=json.loads((b/(P+name+'.pcd.json')).read_text());improved=copy.deepcopy(old)
  for field,value in adds[name].items():
   assert field not in improved
   improved[field]=value
  row['preserved_all_original_fields']=all(improved[k]==v for k,v in old.items())
  row['after']=validate(improved);assert row['after']['tier']=='Gold';assert row['preserved_all_original_fields']
  row['fields_added']=list(adds[name]);row['before_file']=P+name+'.pcd.json';row['after_file']=P+name+'.pci.json'
  row['before_sha256']=hashlib.sha256((b/row['before_file']).read_bytes()).hexdigest()
  save(name+'.pci.json',improved)
 reports.append({'application':caseno,'schema_path':P+'schema.json','target_count':2,'procedures_analyzed':2,'queue':inv,'tier_distribution_before':{'none':2,'Bronze':0,'Silver':0,'Gold':0},'tier_distribution_after':{'none':0,'Bronze':0,'Silver':0,'Gold':2},'remaining_schema_gaps':[],'semantic_limit':'Gold certifies these local structural field requirements; it is not proof of semantic completeness or human effectiveness.'})
save('pci-validation.json',reports)

later=[
{'case':'PCI1-later-A','input':'Invitation asks for a written comment and a recurring chair role. Supplied reply: A short written comment is fine, but I am not taking the chair role.','generated_output':{'written_comment':{'stance':'accepted','scope':'short'},'chair_role':{'stance':'declined'},'draft':'Thanks; I have this as a short written comment and no chair role.','human_effect':'unobserved'},'field_used':'examples + failure_modes; the improvement fills schema sections but repeats the established scope rule.'},
{'case':'PCI1-later-B','input':'Supplied reply: I am intrigued by the question but cannot join.','generated_output':{'stated_interest':'intrigued','joining':'declined','draft':'Thanks for letting me know. I have your answer as not joining.','desired_goal':'Discussion with willing participants still desired and unmet for this participant.'},'field_used':'when_to_use + goal-replacement failure mode; interest and participation are distinct.'},
{'case':'PCI2-later-A','input':'A constructed label changes from “What is missing?” over a blank page to the same label over a crowded desk.','generated_output':{'operation':'Compare absence of marks with an object potentially hidden by clutter.','status':'constructed comparison','open_question':'Does a third setting make “missing” mean a person rather than an object?','interest_reason':'The relation sought changes while the wording stays fixed.'},'field_used':'examples retain imaginative comparison without claiming an audience response.'},
{'case':'PCI2-later-B','input':'Proposed audience study of the blank-page and desk labels; no people observed.','generated_output':{'status':'planned','prediction':'People may select different referents; this is an untested prediction.','actual_observations':[],'next_available_operation':'Write candidate interpretations for a third fictional scene.','original_study':'pending'},'field_used':'unavailable-human-test failure mode; a local construction does not close the causal question.'}
]
save('pci-later-outputs.json',later)

for caseno in [1,2]:
 report=reports[caseno-1];names=[r['name'] for r in report['queue']]
 title='Invitation roles and follow-up' if caseno==1 else 'Curiosity traces and continuation choices'
 initial='The two authored invitation specifications look operationally sufficient, and I have not yet checked whether a downstream reader can identify their stable names, proper use, examples or failure cases.' if caseno==1 else 'The two exploration specifications contain the right main steps; I expect a field-completeness pass chiefly to improve retrieval, without yet knowing whether it changes a later interpretation.'
 rows='\n'.join(f"| {r['name']} | {r['usage_class']} ({r['usage_weight']}) | failing_schema ({r['severity_weight']}) | section_add ({r['effort_estimate']}) | {r['priority']} | none → Gold |" for r in report['queue'])
 outputs='\n\n'.join('Input: '+x['input']+'\n\nActual generated output:\n```json\n'+json.dumps(x['generated_output'],indent=2,ensure_ascii=False)+'\n```\n\nField used: '+x['field_used'] for x in later if x['case'].startswith('PCI'+str(caseno)))
 text=f'''Intended mind change: Determine which additions to the authored {title.lower()} procedures are justified by an explicit schema, and whether their later use changes a concrete output.

# PCI application {caseno}: {title}

Starting working judgment: {initial}

Actor and scope: actual authored local procedure artifacts and subsequent generated outputs; human examples are constructed. The original broad mind-change goal is retained. No original source or installed personal skill is changed.

Source: values-handoff-pci.original.md; separate requirements: values-handoff-pci.requirements.txt. Exact reader hashes match. PCI defines no numerical 8x multiplier. Actual expanded scope is two procedure inventories, all twelve tier fields, consistent priority scoring, twelve missing-field additions across the two files, eight examples, eight failure modes and two later applications.

## Loaded schema and inventory

Schema path: values-handoff-schema.json. This is an explicit local schema authored from PCI's Bronze/Silver/Gold field lists, not a claim that an unseen canonical GOSM schema was loaded. Its required types and nonempty constraints are inspectable. Procedure paths: {', '.join(P+n+'.pcd.json' for n in names)}. The on-disk JSON files were parsed before validation. Target count: two.

Both input specifications have name, description, steps, inputs, outputs and verification plus the source-requested success criteria, complexity, dependencies and reuse scope. Both lack id, version, when_to_use, examples, failure_modes and gosm_integration. They are high-level PCD specifications, but they do not yet reach Bronze under this declared schema. Missing advanced fields do not substitute for the missing Bronze fields.

| Procedure | Usage | Severity | Effort | Priority | Tier |
|---|---|---|---|---|---|
{rows}

Priority equals usage × severity / effort. Equal scores are ordered by stable filename; no nonexistent usage statistics are invented. The effort category is a section addition because original steps and I/O are retained. These are planning weights from the source, not measured authoring times.

## Actual changes

For each procedure, id was assigned a stable local name, missing version became 1.0.0, when_to_use was derived from its existing purpose, four concrete examples were added, four failure modes were added, and gosm_integration states its upstream/downstream placement and external gate. The original inputs, outputs, steps, success criteria, verification, complexity, dependencies and reuse text remain equal as parsed values.

Improved files: {', '.join(P+n+'.pci.json' for n in names)}. Values-handoff-pci-validation.json records the actual queue, before/after fields, original hashes and equality checks. Distribution changed from two below Bronze to two Gold. No existing content was deleted or rewritten; archives and baseline specifications remain available. Remaining schema gaps: zero under this local schema. Remaining semantic or human-effect gaps are not measured by a field-presence result.

## Later applications actually produced

{outputs}

Certificate: the initial unvalidated artifacts lack six required fields each; the declared schema deterministically places them below Bronze. The written additions provide those fields and preserve every original value, yielding Gold under the same checks. The strongest contrary branch is that a field can be present yet incomplete or semantically wrong; that remains true and prevents the stronger verdict “Gold proves reliable human operation.” Later outputs instantiate useful distinctions, but those distinctions were already present in this program and no comparison isolates a new schema-induced semantic benefit.

Actual mind change: The authored specifications now have explicit identity, use cases, examples, failure cases and workflow placement; the completeness verdict is bounded to the declared local schema.

Benefit: A downstream reader can retrieve concrete examples and gaps without inventing them, and original content remains inspectable. Human effectiveness is unobserved; new semantic benefit from the tier change remains unresolved.

Verdict: UNRESOLVED

Novelty: repeated distinctions in a newly formalized local artifact; no new KEEP credit for schema completeness alone.

Organization: Field validation now separates missing information from substantive correctness. A compact priority report points to the four preserved source snapshots and improved files. The remaining improvement is to exercise cases that cross those new sections, where field presence can hide inconsistent transitions.

Next attempts: Apply the improved artifact to a revision rather than an initial reply; inspect mixed constructed and observed inputs; compare a downstream draft with the exact component and version it uses.
'''
 (b/f'pci-{caseno:02}.md').write_text(text)
print(json.dumps({'procedures':4,'all_original_fields_preserved':all(x['preserved_all_original_fields'] for r in reports for x in r['queue']),'after_gold':sum(x['after']['tier']=='Gold' for r in reports for x in r['queue'])}))
