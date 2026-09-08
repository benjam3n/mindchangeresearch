"""Finish the bounded values handoff; authored artifacts, not installed skills."""
from pathlib import Path
import copy, hashlib, json, re

B = Path(__file__).parent
P = 'values-handoff-'

def save(name, data):
    (B / (P + name)).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

names = ['invitation-record', 'followup-choice', 'curiosity-trace', 'continuation-choice']
before = {n: json.loads((B / (P+n+'.pci.json')).read_text()) for n in names}
snapshots = []
for n in names:
    source = B / (P+n+'.pci.json')
    snapshots.append({'file':source.name, 'sha256':hashlib.sha256(source.read_bytes()).hexdigest(), 'content':before[n]})
for n in ['pcd-01.md','pcd-02.md','pci-01.md','pci-02.md']:
    src=B/n; dst=B/(P+'before-'+n)
    if not dst.exists(): dst.write_bytes(src.read_bytes())
save('iteration-before.json', snapshots)

targets = [
 {'id':'T01','priority':'high','dimension':'COMPLETENESS','level':'component','type':'extend','effort':'medium','file':'invitation-record','before':'No record, actor, invitation or component identifiers; context has no event ordering.','change':'Add a typed identity and chronology envelope; a late-arriving earlier message does not automatically become current.'},
 {'id':'T02','priority':'high','dimension':'CORRECTNESS','level':'paragraph','type':'extend','effort':'medium','file':'invitation-record','before':'No prior response input or operation that applies a correction.','change':'Merge explicitly corrected attributes only, retain unchanged component attributes, and preserve superseded values with the correcting evidence.'},
 {'id':'T03','priority':'high','dimension':'ANALYSIS','level':'paragraph','type':'refine','effort':'small','file':'invitation-record','before':'Known speaker appears in input, but quotation and authority do not govern update eligibility.','change':'Keep organizer proposals and third-party reports separate from the participant stance; only the supplied participant statement updates that participant in these cases.'},
 {'id':'T04','priority':'high','dimension':'IDEAS','level':'paragraph','type':'refine','effort':'small','file':'invitation-record','before':'One confirmation status; absolute success criterion says output claims no human effect.','change':'Separate confirmation of interpretation, agreement to an option, and evidence of performance; permit sourced observations while withholding unsupported effects and causation.'},
 {'id':'T05','priority':'high','dimension':'INTEGRATION','level':'component','type':'extend','effort':'medium','file':'followup-choice','before':'Draft refers to an unversioned response record and has no stale status.','change':'Bind each draft to exact component revisions; regenerate only when an affected component changes, retaining the earlier unsent draft as superseded.'},
 {'id':'T06','priority':'high','dimension':'CORRECTNESS','level':'paragraph','type':'extend','effort':'small','file':'followup-choice','before':'Matching option is mentioned, but no defined output exists for a stated condition with no available matching action.','change':'Return no matching option when the supplied availability contradicts the condition; keep the desired goal visible and do not invent a compatible slot or request already-declined work.'},
 {'id':'T07','priority':'high','dimension':'EXPRESSION','level':'paragraph','type':'replace','effort':'medium','file':'curiosity-trace','before':'Actual, constructed and planned share a single alternative status.','change':'Replace that runtime classification with separate input origin, operation state and per-claim evidence kind; an actual comparison of fiction is representable.'},
 {'id':'T08','priority':'high','dimension':'ANALYSIS','level':'component','type':'extend','effort':'medium','file':'curiosity-trace','before':'A generic prior link does not distinguish continuation, contradiction, correction, or a planned test.','change':'Type each relation and identify the exact claim it bears on; a new scene need not invalidate an earlier scene interpretation.'},
 {'id':'T09','priority':'high','dimension':'IDEAS','level':'paragraph','type':'prune and refine','effort':'small','file':'continuation-choice','before':'Selection step requires a distinct question although pure-interest candidates are allowed.','change':'Delete the unconditional distinct-question admission rule from the executable revision; use a declared investigate or revisit-for-interest mode and never score a repeat as new evidence.'},
 {'id':'T10','priority':'high','dimension':'SCOPE','level':'paragraph','type':'refine','effort':'small','file':'continuation-choice','before':'The only goal input is the entire mind-change program.','change':'Add the present local purpose and declared available operations; select against that purpose while retaining the governing goal separately.'},
 {'id':'T11','priority':'medium','dimension':'STRUCTURE','level':'component','type':'extend','effort':'medium','file':'curiosity-trace','before':'Prior existence is requested, but the produced trace has no stable identity; cycles are not distinguished from a valid chain.','change':'Produce stable trace/claim identities and a finite parent relation; missing or cyclic parents remain unresolved instead of claiming retrieved ancestry.'},
 {'id':'T12','priority':'medium','dimension':'META','level':'paragraph','type':'extend','effort':'small','file':'continuation-choice','before':'Stopped-thread reason is free text; exhausted question and unavailable human study have no distinct reopening condition.','change':'Distinguish settled, paused for resources, deferred by purpose, and repeated for interest; reopen a paused study only when its stated missing resource becomes available.'},
]

after=copy.deepcopy(before)
for n,o in after.items():
    o['version']='2.0.0'
    o['revision_origin']={'source_snapshot':P+n+'.pci.json','local_authored_revision':True,'reason':'ITERATE findings T01–T12; not a modification to an archived Reasoningtool original.'}

o=after['invitation-record']
o['inputs'].update({
 'identity':'record_id, participant_id, invitation_id and component_id identify whose answer to which request is represented.',
 'order':'Supplied effective order and received order; uncertain effective order stays uncertain. Do not infer chronology from file position alone.',
 'prior_response':'Exact prior record and per-component revisions, or null for a first reply.',
 'evidence_role':'Participant statement, organizer proposal, third-party report, supplied observation, or authored construction; quoted speaker is distinct from reporting speaker.'})
o['outputs'].update({
 'revision_record':'Append-only event with exact evidence; active component attributes retain their source event; superseded values remain recoverable.',
 'confirmation_dimensions':'interpretation_confirmed, option_agreed, performance_observed are separately evidenced, not inferred from one another.',
 'change_set':'Affected component attributes, unchanged attributes, and unresolved ordering or referent conflicts.'})
o['steps'][0]='Bind the invitation, participant, component identifiers, exact reply, evidence role, supplied effective order, and prior record.'
o['steps'].insert(2,'Apply a participant correction only to the explicitly affected attributes. Carry unchanged attributes from the exact prior record and preserve superseded values. An absent later mention is not a withdrawal.')
o['steps'].insert(3,'Treat organizer proposals and third-party quotations as separate evidence. They do not establish a participant commitment in this local procedure. An earlier effective message received later does not replace a later effective correction.')
o['steps'].insert(-1,'Record confirmation of interpretation, agreement to a proposed option, and observed performance separately. A stated future commitment supplies no performance observation.')
o['success_criteria'][-1]='Human-action observations require supplied provenance; unsupported human effects, inferred feelings and causal changes are not claimed.'
o['verification'] += ['Resolve every inherited attribute to an existing earlier record.', 'Check whether the correction changes a fact, the participant stance, or only an organizer proposal.', 'If chronology or authority is unresolved, return that unresolved state.']

o=after['followup-choice']
o['inputs']['response_record']='Exact participant/invitation record and per-component revision IDs, with evidence, conditions and current-state conflicts.'
o['inputs']['prior_draft']='Existing draft with its source component revisions, if any.'
o['outputs']['source_binding']='Record and component revisions actually used; draft state is current, superseded, or unresolved.'
o['outputs']['availability_gap']='Stated condition and supplied actions that fail it; no matching option when none is supplied.'
o['steps'].insert(1,'Compare source revisions with any prior draft. Mark the prior draft superseded only when an affected component changes; preserve its text and reason. Build the current draft from the current supplied evidence.')
o['steps'][3]='For conditional components, compare the stated condition with each supplied available option. Offer only a matching option; when none matches, state the gap without inventing availability or agreement.'
o['verification'] += ['Every source binding resolves to the record used.', 'No proposed option contradicts a stated condition.', 'A confirmed paraphrase is not treated as acceptance of a new arrangement.']

o=after['curiosity-trace']
o['inputs'].update({'identity':'Stable trace_id and claim_ids.', 'evidence_dimensions':'Input origin (constructed, supplied source, observed local artifact), operation state (planned, performed, unavailable), per-claim evidence kind (interpretation, direct local measurement, prediction, supplied observation).', 'relation':'continues, revises, tests, or contrasts; exact parent trace and claim IDs, or null for a root.'})
o['outputs']['trace_record']='Stable trace and claim identities; exact question, input, performed operation and output; independent evidence dimensions; typed relation; interest reason and uncertainty.'
o['steps'][3]='Record input origin, whether the operation was performed, and the evidence kind of each output claim separately. A performed fictional comparison is constructed input plus performed operation plus interpretive output.'
o['steps'][4]='Resolve the parent trace and any target claim. Record continues, revises, tests, or contrasts as appropriate. A missing parent or cycle remains a provenance gap; a contrast alone does not revoke its parent.'
o['verification'] += ['A revision names the proposition it corrects, not the entire prior thread by default.', 'A returned parent chain terminates at a known root without cycling.', 'A direct character count and an interpretive meaning claim have different evidence kinds even in one trace.']

o=after['continuation-choice']
o['inputs'].update({'local_purpose':'The declared purpose of this next operation: investigate a distinct unresolved question, or revisit a known object for stated interest. Preserve the governing program goal separately.', 'available_operations':'Concrete available actions, supplied resource constraints, and explicitly unestimated costs.', 'thread_state':'settled, paused_for_resource, deferred_by_purpose, or revisit_for_interest, with the reopening condition where relevant.'})
o['steps'][1]='Compare each candidate with the declared local purpose. In investigate mode require an unresolved question; in revisit-for-interest mode a known result remains eligible without a novelty claim.'
o['steps'][3]='Select a feasible operation meeting the declared purpose. Retain known repetition as repetition, preserve its interest reason, and leave unavailable human studies paused.'
o['steps'].insert(-1,'A paused thread reopens only when the named missing resource is supplied or the proposed action changes. A settled question is not reopened by a new label alone.')
o['outputs']['selection']='One concrete next operation or stopping point, declared mode, local purpose and referenced trace; after execution record the actual product separately.'
o['verification'] += ['The selected mode is stated before novelty is assessed.', 'No repeated product is counted as a new discovery.', 'Unknown effort is not converted to an invented numerical priority.', 'A human study requires actual participants and observations before its gate closes.']

schema=json.loads((B/(P+'schema.json')).read_text())
def tier(o):
    last='none'
    for name,fields in schema['tiers'].items():
        if any(f not in o or not o[f] or type(o[f]).__name__!=schema['types'][f] for f in fields): return last
        last=name
    return last

for n,o in after.items():
    assert tier(o)=='Gold'
    save(n+'.iterate.json',o)

# Typed interpretations are authored below. This reducer consumes them; it does
# not claim to interpret natural language or establish another person's state.
events=[
 {'id':'R0','participant':'Kai','invitation':'puzzle-1','effective_order':0,'received_order':0,'role':'participant_statement','constructed':True,'text':'I can read the first two pages on Saturday. I could join once if it is audio only. I cannot host monthly.', 'updates':{'read':{'stance':'accepted','amount':'first two pages','when':'Saturday'},'join':{'stance':'conditional','frequency':'once','medium':'audio only'},'host':{'stance':'declined','frequency':'monthly'}}},
 {'id':'R1','participant':'Kai','invitation':'puzzle-1','effective_order':2,'received_order':1,'role':'participant_statement','constructed':True,'text':'Saturday no longer works; I can read Sunday. I can join once in text chat, not audio. Hosting is still out.', 'updates':{'read':{'when':'Sunday'},'join':{'stance':'accepted','medium':'text chat','frequency':'once'},'host':{'stance':'declined'}}},
 {'id':'R2','participant':'Kai','invitation':'puzzle-1','effective_order':3,'received_order':2,'role':'organizer_proposal','constructed':True,'text':'Let us use audio at 14:00.', 'updates':{'join':{'medium':'audio','time':'14:00'}}},
 {'id':'R3','participant':'Kai','invitation':'puzzle-1','effective_order':1,'received_order':3,'role':'participant_statement','constructed':True,'text':'Saturday is still fine for the two pages.', 'updates':{'read':{'when':'Saturday'}}},
 {'id':'R4','participant':'Kai','invitation':'puzzle-1','effective_order':4,'received_order':4,'role':'third_party_report','constructed':True,'text':'Mira reports: Kai said, “I can host.”', 'updates':{'host':{'stance':'accepted'}}},
]

def reduce_events(records):
    state={};hist=[];seen=set();excluded=[]
    if len({(x['participant'],x['invitation']) for x in records})>1:
        raise ValueError('This reducer requires one participant and invitation; separate the records before reducing.')
    for event in sorted(records,key=lambda x:x['effective_order']):
        if event['id'] in seen: continue
        seen.add(event['id'])
        if event['role']!='participant_statement':
            excluded.append({'id':event['id'],'reason':event['role']});continue
        for component,updates in event['updates'].items():
            current=state.setdefault(component,{})
            for key,value in updates.items():
                prior=current.get(key)
                current[key]={'value':value,'source':event['id']}
                if prior and prior['value']!=value:
                    hist.append({'component':component,'attribute':key,'old':prior,'new':current[key]})
    return {'current':state,'superseded':hist,'excluded_as_commitment':excluded}

initial=reduce_events(events[:1]); current=reduce_events(events)
draft_before={'id':'D0','source_events':['R0'],'text':'Thanks for offering the first two pages on Saturday. An audio-only one-off discussion remains the condition you named; no monthly hosting is assigned.','state':'superseded after R1','sent':False}
draft_after={'id':'D1','source_events':['R0','R1'],'text':'Thanks. I have the reading as the first two pages on Sunday, one text-chat discussion, and no monthly hosting. A particular discussion time remains open.','state':'current','sent':False}
assert current['current']['read']['when']['value']=='Sunday'
assert current['current']['read']['amount']['source']=='R0'
assert current['current']['join']['medium']['value']=='text chat'
assert current['current']['host']['stance']['value']=='declined'
assert reduce_events(events+[events[1]])==current
availability={'condition':'text chat','supplied_options':[{'id':'O1','medium':'audio','time':'14:00'}]}
matches=[x['id'] for x in availability['supplied_options'] if x['medium']==availability['condition']]
assert matches==[]
social={'inputs':events,'initial_typed_output':initial,'current_typed_output':current,'old_draft':draft_before,'current_draft':draft_after,'availability_case':{'input':availability,'matching_options':matches,'output':'No supplied option matches text chat; the 14:00 audio proposal is not an agreed arrangement.'},'semantic_scope':'Participant statements and mappings are explicitly constructed and manually interpreted. Reduction verifies those declared mappings, not natural-language reliability or actual consent.','baseline_comparison':'A competent reading of the prior procedure already yields the same stances on R0 and can infer the R1 correction. The new contribution is an explicit, executable record/update contract and stale-draft binding; no bad prior reply is invented.'}
save('iteration-social-use.json',social)

label='What are you waiting for?'
traces=[
 {'id':'Q0','parent':None,'relation':None,'question':'What waiting referents are available in the same wording across a platform and a drawing?','input':{'origin':'constructed','text':label,'scenes':['empty platform','half-finished drawing']},'operation':{'state':'performed','name':'Generate distinct interpretive alternatives'},'claims':[{'id':'Q0a','kind':'interpretation','text':'The platform supports waiting for transport, a person, or an event.'},{'id':'Q0b','kind':'interpretation','text':'The drawing supports waiting to resume making, obtain materials, or choose a next mark.'}], 'state':'settled','interest':'The same wording opens different relations in the two scenes.'},
 {'id':'Q1','parent':'Q0','relation':'contrasts','question':'Does a closed box permit waiting that is neither transport nor making?','input':{'origin':'constructed','text':label,'scene':'closed box'},'operation':{'state':'performed','name':'Generate three candidate waiting relations'},'claims':[{'id':'Q1a','kind':'interpretation','text':'Waiting to open the box is an action delay.'},{'id':'Q1b','kind':'interpretation','text':'Waiting for permission depends on another actor.'},{'id':'Q1c','kind':'interpretation','text':'Waiting for contents to change depends on a process inside the box.'}], 'state':'settled','interest':'An identical box can be encountered as a delayed action, a social boundary, or a changing process.'},
 {'id':'Q2','parent':'Q1','relation':'continues','question':'Which parts of the same artifact are directly measurable, and which remain interpretations?','input':{'origin':'observed local artifact','text':label},'operation':{'state':'performed','name':'Count the characters of the stored Python string'},'claims':[{'id':'Q2a','kind':'direct local measurement','text':f'The stored label has {len(label)} characters including spaces and punctuation.'},{'id':'Q2b','kind':'interpretation','text':'Character identity leaves the three Q1 waiting relations available; the count chooses none of them.'}], 'state':'settled','interest':'One object supports both an exact measurement and unresolved meaning without averaging their certainty.'},
 {'id':'Q3','parent':'Q1','relation':'tests','question':'Which of the three Q1 meanings would actual viewers report first?','input':{'origin':'constructed','text':label,'scene':'closed box'},'operation':{'state':'unavailable','name':'Collect actual viewer responses'},'claims':[{'id':'Q3a','kind':'prediction','text':'A distribution of viewer choices would distinguish audience prevalence from the available interpretations; none has been observed here.'}], 'state':'paused_for_resource','reopening_condition':'Actual participants and recorded responses supplied.','interest':'A scene can afford interpretations without revealing how often each is selected.'},
 {'id':'Q4','parent':'Q1','relation':'continues','question':'Can I revisit the closed box as a short scene without calling the known three meanings new discoveries?','input':{'origin':'constructed','text':label,'scene':'closed box'},'operation':{'state':'performed','name':'Write a short scene from the known permission and process alternatives'},'claims':[{'id':'Q4a','kind':'creative product','text':'The label asked, “What are you waiting for?” A brass key lay beside the box. The visitor left it there. Behind the lid, something had just gone quiet.'}], 'state':'revisit_for_interest','interest':'The gap between having a key, choosing to open, and hearing a change is worth returning to without a new truth claim.'},
]
def lineage(node_id,records):
    byid={x['id']:x for x in records};path=[];seen=set();cur=node_id
    while cur is not None:
        if cur in seen:return {'status':'cycle','path':path,'at':cur}
        if cur not in byid:return {'status':'missing_parent','path':path,'at':cur}
        path.append(cur);seen.add(cur);cur=byid[cur]['parent']
    return {'status':'resolved','path':path}
selection_before={'local_purpose':'Revisit the closed box for the interest of a short scene.','procedure':'values-handoff-continuation-choice.pci.json','result':'The unconditional distinct-question selection step has no eligible settled repeat, while the same specification also retains pure-interest candidates. Selection is underdetermined for this supplied purpose; no human or model error is fabricated.'}
selection_after={'local_purpose':'Revisit the closed box for the interest of a short scene.','mode':'revisit-for-interest','available_operations':['Write the short scene locally','Compare another new scene locally'],'selected':'Q4','deferred':[{'thread':'Q3','reason':'Actual viewer responses unavailable.'},{'thread':'new-scene comparison','reason':'Available, but serves a different present purpose.'}],'novel_evidence':False,'actual_product':traces[-1]['claims'][0]['text']}
lineages={x['id']:lineage(x['id'],traces) for x in traces}
assert all(x['status']=='resolved' for x in lineages.values())
missing=lineage('Qx',[{'id':'Qx','parent':'absent'}]);cycle=lineage('Qa',[{'id':'Qa','parent':'Qb'},{'id':'Qb','parent':'Qa'}])
assert missing['status']=='missing_parent' and cycle['status']=='cycle'
exploration={'traces':traces,'before_selection':selection_before,'after_selection':selection_after,'lineages':lineages,'separate_invalid_inputs':{'missing':missing,'cycle':cycle},'scope':'All scenes and creative outputs are authored locally. The character count is a direct observation of that local string. No viewer response, pleasure report, or human mind change is present.'}
save('iteration-exploration-use.json',exploration)

# Twelve target executions are separate from the finding count. Multiple edits
# to the same executable local procedure remain visible, with archived inputs.
for t in targets:
    t['status']='executed'
    t['after_file']=P+t['file']+'.iterate.json'
save('iteration-targets.json',targets)
save('iteration-verification.json',{'targets':len(targets),'high_priority':sum(t['priority']=='high' for t in targets),'executed':sum(t['status']=='executed' for t in targets),'tier_before':{n:tier(o) for n,o in before.items()},'tier_after':{n:tier(o) for n,o in after.items()},'baseline_files_unchanged':all(hashlib.sha256((B/s['file']).read_bytes()).hexdigest()==s['sha256'] for s in snapshots),'social_cases':{'ordered_revision':'Sunday','unmentioned_attribute':'first two pages from R0','proposal_not_commitment':True,'third_party_report_not_commitment':True,'duplicate_replay_same':True,'no_matching_option':True},'trace_cases':{'lineages':lineages,'character_count':len(label),'missing_parent_detected':True,'cycle_detected':True,'revisit_product_present':True},'scope':'Checks validate declared typed records, structural fields and these local products. They do not establish general semantic reliability, a human effect, or first-pass success.'})
print(json.dumps({'revised_procedures':len(after),'executed_targets':len(targets),'social_events':len(events),'traces':len(traces),'char_count':len(label)}))
