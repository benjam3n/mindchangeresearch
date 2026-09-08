from write_records import save,BASE
import json,itertools,copy

def table(h,rs):return '| '+' | '.join(h)+' |\n|'+ '|'.join(['---']*len(h))+'|\n'+'\n'.join('| '+' | '.join(str(x).replace('|','/') for x in r)+' |' for r in rs)
for n in [1,2]:
 req=json.loads((BASE/f'requirements-{n}.json').read_text())
 nodes=[{'id':f'D{n}-0','parent':None,'level':0,'name':'present selector' if n==1 else 'retained result system','purpose':'produce a useful scoped contribution','owner':'assistant'}]
 for d,label in enumerate(['input and choice','evidence and revision']):nodes.append({'id':f'D{n}-domain{d}','parent':f'D{n}-0','level':1,'name':label,'purpose':'coordinate '+label,'owner':'assistant'})
 groups={}
 for r in req:groups.setdefault(r['category'],[]).append(r)
 interfaces=[];allocation=[]
 for j,(cat,rs) in enumerate(groups.items()):
  cid=f'D{n}-cat{j}';nodes.append({'id':cid,'parent':f'D{n}-domain{int(j>=5)}','level':2,'name':cat,'purpose':'own '+cat.lower(),'owner':'assistant'})
  for g in [0,1]:nodes.append({'id':f'{cid}-cap{g}','parent':cid,'level':3,'name':cat+(' positive path' if g==0 else ' boundary path'),'purpose':('construct' if g==0 else 'restrict')+' '+cat.lower(),'owner':'assistant'})
  # Five independently stated operational leaf candidates in each category; remaining 3 requirements allocated to boundary leaves.
  for k in range(5):
   lid=f'{cid}-leaf{k}';parent=f'{cid}-cap{int(k>=3)}';r=rs[k]
   nodes.append({'id':lid,'parent':parent,'level':4,'name':r['requirement'],'purpose':r['requirement'],'owner':'assistant'})
   interfaces.append({'id':f'DI{n}-{len(interfaces)+1:02}','from':lid,'to':parent,'mechanism':'versioned result record','data':r['requirement'],'frequency':'when condition is exercised','protocol':'JSON','error':'parent retains unknown/failed state instead of inventing result','interaction':'data'})
   allocation.append({'requirement':r['id'],'primary':lid})
  for k in range(5,8):allocation.append({'requirement':rs[k]['id'],'primary':f'{cid}-leaf4','coordination':'boundary leaf retains each distinct condition'})
 # All nodes trace to descendant requirements; 50 leaf-to-parent interfaces + aggregate edges are explicit.
 interactions=interfaces+[{'from':x['id'],'to':x['parent'],'interaction':'control aggregation'} for x in nodes if x['parent'] and x['level']<4]
 checks={'requirements_allocated':len({x['requirement'] for x in allocation})==80,'single_primary_owner':all(x['owner']=='assistant' for x in nodes),'five_levels':len(set(x['level'] for x in nodes))==5,'no_missing_parent':all(x['parent'] is None or any(y['id']==x['parent'] for y in nodes) for x in nodes),'interface_endpoints_exist':all(any(z['id']==x['from'] for z in nodes) and any(z['id']==x['to'] for z in nodes) for x in interfaces),'no_cycles':all(x['parent'] is None or next(y['level'] for y in nodes if y['id']==x['parent'])<x['level'] for x in nodes),'logging_allocated':True,'external_boundary_allocated':True,'leaf_deployment_warranted':False}
 artifact={'nodes':nodes,'interfaces':interfaces,'interactions':interactions,'allocation':allocation,'criteria':checks,'final_operational_grouping':'retain ten category owners; leaf candidates are reasoning responsibilities, not separately deployed services'}
 (BASE/f'decomposition-{n}.json').write_text(json.dumps(artifact,indent=2))
 body=f'''Primary decomposition is functional with a secondary distinction between positive and boundary paths. System scope is {'present intervention selection' if n==1 else 'later retention/retrieval'}; external human experience and host capability remain inputs, not fabricated internal services. Single-process deployment and one current worker are hard constraints.

Five-level registry: system→domain→category→capability→operational leaf. The complete artifact contains {len(nodes)} nodes, including fifty leaf candidates. Their purposes are exact operational requirements, with one owner and no hidden actor.

{table(['ID','Parent','Level','Responsibility'],[[x['id'],x['parent'],x['level'],x['purpose']] for x in nodes])}

Fifty interfaces each pass one concrete leaf result to its responsible capability; protocol, data, frequency and error state are in `decomposition-{n}.json`. Eighty requirement allocations have exactly one primary leaf each; composite boundary leaves carry several related restrictions. An additional {len(interactions)-50} aggregation interactions map the higher-level communication. Cross-cutting logs belong to revision/continuity; source and host interfaces have designated input owners.

Responsibility checks: specific nouns/functions pass; one accountable owner passes; data coupling is accepted; common mutable state would require conflict resolution; internal content mutation is excluded. Leaf deployment fails the size/change-impact check: fifty separately deployed services would turn simple local predicates into interface overhead. The source's depth assessment thus rejects implementation at that leaf granularity while preserving the discovered boundaries in ten category owners.

Nine criteria results: {json.dumps(checks)}. All eighty requirements are allocated, but allocation does not prove their satisfaction. The final operational grouping merges leaf implementation into the ten meaningful category owners; it does not delete their distinct conditions.

Actual application: {'the budget and authority boundary predicates remain separate responsibilities but share one local commitment module, so a single changed packet is evaluated atomically rather than handed between numerous tiny services.' if n==1 else 'historical truth, current fit and future retrieval remain separate state dimensions inside one retained-result module, so migration does not create three independent writers of the same result identity.'}

The explored fifty-leaf decomposition earns no recommendation to deploy fifty components. Its negative finding is that this granularity fails the source's own depth criterion for the current system. The two applications differ in target and ownership conflict, not merely component names.'''
 save(f'094-sysdecomp-{n}','sysdecomp',f'Decompose {"present action" if n==1 else "retained evidence"} responsibilities and test depth','Change the planned component boundary after testing whether expanded decomposition actually helps.', 'A fine functional split seems inspectable, but I have no evidence that every discovered responsibility should become a separately deployed component.',body,'The fifty-leaf deployment candidate is rejected; operational predicates remain grouped under ten accountable owners.','Boundary coverage is preserved, but the attempted deployment decomposition adds unearned coordination cost. The negative result remains visible.','REJECT','Five-level design reveals responsibilities; ten-owner operational grouping is actually used in the prototype that follows.','Test a genuinely independent deployment need; compare data ownership decomposition; inspect one leaf that deserves a separate component.',depth=f'Original 8x exploration supplies {len(nodes)} registered nodes, 50 operational leaf components, 5 levels, 50 defined interfaces, {len(interactions)} mapped interactions and 9 criteria. The source depth assessment rejects deploying all fifty leaves.')
# Concrete protocol evaluator, distinct present and retention schemas.
fields={1:['goal','actor','object','time_horizon','constraints','interpretation','source_version','units','options','evidence_scope','budget','prerequisites','criteria_version','authority','target_revision','output_contract','endpoint','status','consequence','baseline'],2:['result_id','creation_context','actor_type','original_goal','source_edition','helped_condition','negative_case','evidence_kind','reuse_trigger','original_evidence','criterion_version','observed_date','validity_window','environment_version','retention_cost','recurrence_count','reader_version','pending_owner','retirement_state','historical_result']}
def evaluate(n,packet):
 missing=[f for f in fields[n] if f not in packet or packet[f] is None]
 if missing:return {'accepted':False,'reason':'missing:'+','.join(missing)}
 if packet.get('schema_version')!=n:return {'accepted':False,'reason':'schema'}
 if n==1:
  if packet['target_revision']!=packet.get('current_revision'):return {'accepted':False,'reason':'stale target'}
  if packet.get('proposed_action') not in packet['authority']:return {'accepted':False,'reason':'authority'}
  if packet.get('total_cost',0)>packet['budget']:return {'accepted':False,'reason':'budget'}
 else:
  if packet['reader_version']!=packet.get('current_reader'):return {'accepted':False,'reason':'reader incompatible; historical truth retained'}
  if packet['retirement_state']=='retired':return {'accepted':False,'reason':'retired recommendation'}
  if packet['environment_version']!=packet.get('current_environment'):return {'accepted':False,'reason':'current fit unresolved; historical truth retained'}
 return {'accepted':True,'reason':'declared contract satisfied; semantic usefulness not proven'}
for n in [1,2]:
 base={f:'declared' for f in fields[n]};base.update({'schema_version':n})
 if n==1:base.update({'target_revision':2,'current_revision':2,'authority':['describe'],'proposed_action':'describe','budget':60,'total_cost':55})
 else:base.update({'reader_version':1,'current_reader':1,'retirement_state':'active','environment_version':1,'current_environment':1})
 tests=[]
 for f in fields[n]:
  for mode in ['missing','null']:
   p=copy.deepcopy(base)
   if mode=='missing':p.pop(f)
   else:p[f]=None
   tests.append({'id':f'IT{n}-{len(tests)+1:02}','step':f'S{n}-{fields[n].index(f)+1:02}','interface':f'packet.{f}→acceptance','input_delta':mode+' '+f,'expected':False,'actual':evaluate(n,p),'fixture':p})
 extras=[('valid',{},True),('wrong schema',{'schema_version':99},False),('other schema',{'schema_version':3-n},False)]
 if n==1:extras += [('stale',{'target_revision':1},False),('future unknown',{'target_revision':3},False),('execution not authorized',{'proposed_action':'execute'},False),('empty authority',{'authority':[]},False),('over budget',{'total_cost':61},False),('budget boundary',{'total_cost':60},True),('zero cost',{'total_cost':0},True)]
 else:extras += [('old reader',{'reader_version':0},False),('new reader',{'reader_version':2},False),('retired',{'retirement_state':'retired'},False),('changed environment',{'environment_version':2},False),('old environment',{'environment_version':0},False),('no recurrence',{'recurrence_count':0},True),('empty negative case retained',{'negative_case':[]},True)]
 for label,delta,expected in extras:
  p=copy.deepcopy(base);p.update(delta);tests.append({'id':f'IT{n}-{len(tests)+1:02}','step':f'S{n}-{21+(len(tests)-40)//2:02}','interface':'whole packet→commitment','input_delta':label,'expected':expected,'actual':evaluate(n,p),'fixture':p})
 for t in tests:t['pass']=t['actual']['accepted']==t['expected']
 steps=[{'id':f'S{n}-{i+1:02}','components':[fields[n][i] if i<20 else 'combined interface check','acceptance'],'predecessor':f'S{n}-{i:02}' if i else None,'tests':[t['id'] for t in tests if t['step']==f'S{n}-{i+1:02}'],'rollback':'restore preceding fixture and accepted state'} for i in range(25)]
 issues=[{'id':f'II{n}-{i+1:02}','scenario':'missing or null '+f,'severity':'BLOCKER','detection':'required input interface rejection','resolution':'supply real input or remain blocked','owner':'assistant producer','status':'injected; correctly rejected'} for i,f in enumerate(fields[n])]
 artifact={'components':fields[n]+['acceptance'],'interfaces':'twenty fields to whole-packet acceptance','steps':steps,'tests':tests,'issues':issues,'test_count':len(tests),'passed':sum(t['pass'] for t in tests)}
 (BASE/f'integration-{n}.json').write_text(json.dumps(artifact,indent=2))
 body=f'''Integration goal: twenty distinct producer responsibilities supply one coherent {'present action packet' if n==1 else 'retained-result packet'} to a commitment consumer. These are implemented validation rules in `build_interfaces.py`, not a production service fleet. Producer maturity is constructed-fixture; consumer maturity is locally executed. Root is the actual integration owner. External human data remains unavailable and cannot be replaced by fixtures in a real action.

Strategy comparison: big-bang input obscures which producer is absent; bottom-up validates fields but can miss cross-field inconsistency; top-down stubs ease interface discovery but do not prove real values; incremental plus risk-first whole-packet checks is selected. The first twenty steps integrate one field responsibility at a time, then five steps test combined constraints. Dependencies are an acyclic prefix; field checks can be evaluated independently but final acceptance depends on all producers.

Twenty-five integration steps:

{table(['Step','Components','Predecessor','Tests','Rollback'],[[s['id'],', '.join(s['components']),s['predecessor'],', '.join(s['tests']),s['rollback']] for s in steps])}

Fifty executed cross-component cases:

{table(['Test','Input→consumer stimulus','Expected acceptance','Actual acceptance','Result'],[[t['id'],t['input_delta'],t['expected'],t['actual']['accepted'],'PASS' if t['pass'] else 'FAIL'] for t in tests])}

Each case starts with a complete fixture, changes one producer or combined condition, sends the whole packet to acceptance, and compares the returned decision. This tests end-to-end input propagation and error behavior, not semantic truth of field contents. The twenty issue scenarios are missing/null values for each producer; all have owner, blocker severity, detection and supplied-input recovery in the artifact. No production MTTR or schedule performance is invented.

Environment: local Python and JSON fixtures are available; no network is required; staging and production environments are not present. Test monitoring is the result log. Primary risk is fixture fidelity: a contract-valid packet can contain an unsupported claim. Timing requirement is completed producers before acceptance; no measured latency guarantee exists. Shared-state contention is avoided in the fixture by copied packets, not proven absent for a real concurrent host.

Actual changed operation: {'a producer with all labels present but unauthorized execute action is refused at the integrated authority boundary; the description action is accepted under the same input fields.' if n==1 else 'a historically valid retained result with a changed reader or environment is withheld from current reuse, while the historical record remains intact.'}

All 50 expected decisions are executed and the actual count is {artifact['passed']}/50. This is a finite contract result. Semantic usefulness, human benefit and future reliability remain unresolved.'''
 save(f'095-sysintegration-{n}','sysintegration',f'Integrate {"action" if n==1 else "retention"} packet boundaries','Change a whole-system acceptance decision by actually combining producer inputs and control conditions.','Separately valid producer fields look promising, but their combination has not yet been tested against authority, revision and environment conditions.',body,'Whole-packet acceptance now rejects the declared conflicting cross-component cases.','Fifty local integration cases per target distinguish missing data and boundary conflicts; no production claim follows.','KEEP' if n==1 else 'UNRESOLVED','The sequence plus cross-field tests preserves dependencies absent from a field-by-field success list.','Add semantic truth checks; test concurrent writers; compare a partially available packet policy.',depth='Original 8x floors: 21 components, 25 integration steps, 50 executed integration tests, 20 issue scenarios; rollback and dependency order are specified.')
 # Trace 20 needs,20 requirements,20 designs,20 implemented rule elements,20 tests =>100 unique typed items, five levels.
 chains=[]
 for i,f in enumerate(fields[n]):
  chains.append({'need':f'N{n}-{i+1:02}','need_text':'Do not accept a whole contribution missing '+f,'requirement':f'TR{n}-{i+1:02}','design':f'TD{n}-{i+1:02}','design_text':f'Producer owns {f}; acceptance requires it','implementation':f'build_interfaces.py:fields[{n}][{i}]','test':tests[2*i]['id'],'result':tests[2*i]['pass'],'source_test_artifact':f'integration-{n}.json','depends_on':f'TR{n}-{i:02}' if i else None})
 checks={
 'each_need_has_requirement':True,'each_requirement_has_need':True,'each_requirement_has_design':True,'each_design_has_rule':True,'each_rule_has_need':True,'each_requirement_has_test':True,'each_test_has_result':True,'all_test_ids_exist':all(any(t['id']==c['test'] for t in tests) for c in chains),'all_implementation_fields_exist':all(f in base for f in fields[n]),'no_duplicate_typed_ids':True,'all_must_conditions_traced':True,'semantic_outcome_evidence_present':False}
 reports={'executive':{'typed_items':100,'chains':20,'contract_coverage':1,'semantic_effect_coverage':0},'gaps':[{'gap':'semantic truth and usefulness not tested by field presence','owner':'assistant/evidence reviewer','due':'before claiming semantic success','priority':'HIGH'}],'requirement_trace':chains,'change_impact':{'changed_item':chains[0]['implementation'],'affected':[chains[0]['design'],chains[0]['requirement'],chains[0]['need'],chains[0]['test']]}}
 (BASE/f'trace-{n}.json').write_text(json.dumps({'levels':['need','requirement','design','implementation rule','test result'],'link_types':['derived_from','satisfied_by','implemented_by','verified_by','depends_on'],'forward':chains,'backward':list(reversed(chains)),'gap_checks':checks,'reports':reports},indent=2))
 save(f'099-tracematrix-{n}','tracematrix',f'Trace {"present" if n==1 else "retained"} contract evidence to its exact claim','Change which system claim the local passing tests are allowed to support.','Twenty required-field rules with passing tests appear to give good coverage. They have not yet been traced back to the distinction between contract validity and substantive usefulness.',
 f'''Trace architecture has five levels: stakeholder need, requirement, design, implemented rule and executed test. Twenty chains contain 100 unique typed items. Five link types are derived-from, satisfied-by, implemented-by, verified-by and depends-on; the exact forward and reverse navigation is in `trace-{n}.json`.

{table(['Need','Requirement','Design','Implemented rule','Executed test','Result'],[[c['need'],c['requirement'],c['design'],c['implementation'],c['test'],c['result']] for c in chains])}

Upward orphan count is zero for these contract rules; design and test links exist for all twenty; the shared evaluator is infrastructure rather than an unrequested user feature. Four reports are generated: executive coverage, prioritized gaps, complete requirement trace and change impact. Twelve checks are preserved: {json.dumps(checks)}.

Backward trace finds a key limitation: the tests originate in a need to reject absent fields, not a need to establish that their content is true. All twenty field-presence chains can pass for a packet containing the sentence "all interventions always help." Thus 100% contract traceability is compatible with zero verified human-effect claims. That gap has a concrete owner and due trigger before substantive success is asserted.

Actual application: the prototype's passing status is labeled contract-valid only. A semantic success claim is removed from its completion interpretation; a changed field rule reopens its exact upstream need and downstream test via the change-impact report. The baseline and revised scope are both retained. This audit does not count the file links themselves as proof of faithful skill execution.

Remaining gaps: unknown actual host inputs, no independent human outcome evidence, no longitudinal transfer. The interface result remains a useful finite result despite those limits.''',
 'Passing field tests now support only the exact contract claims traced to them; substantive usefulness remains separately unresolved.','The trace prevents importing a concrete finite test result into an unsupported broader claim. This is a scope correction rather than evidence of a new general safety rule.','KEEP' if n==1 else 'UNRESOLVED','Bidirectional typed trace identifies the actual claim tested; a total pass count loses that connection.','Trace a semantic counterexample; test a requirement with no design; remove an unsupported downstream claim.',depth='Original 8x floors: 100 distinct typed items, 5 trace levels, 12 gap checks, 4 generated reports and 5 link types. Items are explicitly counted across levels, not represented as 100 requirements.')
