from pathlib import Path
import json
B=Path('/workspace/scratch/78b838bd97fc/mind-change-research/values')

def ar(name,claim,branches,tests):
 nodes=[]
 def node(text,parent,strength,kind,bedrock=None):
  z={'id':f'R{len(nodes)+1}','parent':parent,'text':text,'strength':strength,'kind':kind,'bedrock':bedrock};nodes.append(z);return z['id']
 root=node(claim,None,'Assumed analytical proposition','Root')
 def walk(branch,parent):
  text,s1,s2=branch[0]
  me=node(text,parent,'Possible under the explicit case premises' if len(branch)>1 else 'Necessary within the stated case','Implication' if len(branch)>1 else 'Testable prediction','BEDROCK-TEST-DEFERRED: real participant/data unavailable' if len(branch)==1 and name.endswith('2-ar') else 'BEDROCK-OBSERVE: generated record shown below' if len(branch)==1 else None)
  if len(branch)>1:
   walk(branch[1:],me)
   node(s1,me,'Necessary within stated premises','Foreclosure' if 'FORECLOSED' in s1 else 'Commitment','BEDROCK-LOGIC or explicitly deferred human test in statement')
   node(s2,me,'Possible with the condition stated','Cost or alternative implication','BEDROCK-LOGIC or explicitly deferred human test in statement')
 for br in branches:walk(br,root)
 report={'claim':claim,'nodes':nodes,'total':len(nodes),'max_edges':max(len(x) for x in branches),'nonterminal_children':3,'tests':tests}
 (B/(name+'.json')).write_text(json.dumps(report,indent=2))
 lines=[f'Intended mind change: Follow the commitments of the intuition “{claim}” without treating conditional implications as observed human effects.','',f'# {name}: original /ar 8x dependency','',
 'Source: ../sources/values-ar.md; receipt: ../sources/values-ar.receipt.txt. Corruption-pre-inoculation loaded separately. Original read before execution; source bytes and requirements are preserved separately.',
 '', 'Starting judgment: the intuition is plausible enough to investigate, but no general effect has been established. “Intuition” here is a provisional working pattern, not a claim that the assistant has a human feeling, body or lifetime of expertise.',
 '', 'Premise check: the specific replies and designs below are explicitly constructed case inputs. Their existence as generated text is observable; their occurrence in a real conversation is not asserted. No false factual premise is assumed true. Every causal human implication is conditional or deferred.',
 '', '## Phase 1: rightness exploration','']
 for z in nodes:
  lines.append(f"{z['id']} — parent {z['parent'] or 'none'}; {z['strength']}; {z['kind']}. {z['text']}"+(f" [{z['bedrock']}]" if z['bedrock'] else ''))
 lines+=['','## Actual generated applications / deferred tests','']+tests
 lines+=['','Pattern: constraining and convergent. The rightness assumption creates obligations to preserve the chosen outcome, the actor’s choice and the evidence scope. It does not authorize counting a convenient proxy as the full effect.','', '## Phase 2: complete claim registry','']
 for z in nodes:lines.append(f"{z['id']} | {z['kind']} | {z['strength']} | parent {z['parent'] or 'root'} | {z['text']}")
 lines+=['','## Phase 3: synthesis from the registry','']
 for z in nodes[1:]:lines.append(f"{z['id']}: {z['text']}")
 lines += ['',f"Depth accounting: {len(nodes)} claims; root has three branches; every nonterminal node has three children; longest root-to-leaf path has seven recursive edges. Other branches stop after five edges. The case premises and possible causal edges remain explicit; numerical depth is not evidence that a human effect occurred.",
 '', 'Weakest links: conditional causal/interpretive implications above depend on the stated input being accurate and on the relevant actor actually responding or participating. Logically scoped transcript fields are inspectable here; participant effects are BEDROCK-TEST-DEFERRED. The additional premises are not smuggled into the original intuition as proven facts.',
 '', 'Actual mind change: The intuition now has explicit scope, costs, foreclosures and testable consequences; its broad human effect remains unproven.',
 '', 'Benefit: The next application can test the relevant effect rather than a more convenient proxy.',
 '', 'Verdict: UNRESOLVED',
 '', 'Organization: Every R-node is retained in the registry and synthesis. Required source operations remain separate from these results; narrower branches are not padded to match the longest chain.',
 '', 'Next attempts: Run a permitted local transcript test; supply actual participant evidence before human-effect claims; challenge the strongest conditional link.','']
 (B/(name+'.md')).write_text('\n'.join(lines))
 return report

A1=[
('When a refusal explicitly names a participation condition, treating it as information preserves that condition in the next-question state.','FORECLOSED: replacing the stated condition with “uncooperative” loses the specific information present in the reply.','If a refusal gives no reason, this branch supplies no basis to invent a condition; a neutral stop can be the entire next step.'),
('For the supplied reply “the hour is fine; mandatory homework is not,” the contested variable is obligation while duration is accepted.','A time-shortening proposal does not directly change mandatory preparation.','The actor can accept duration and still decline the group; the accepted component is not a global yes.'),
('If preparation remains mandatory, shortening the meeting leaves the explicitly named objection in place.','FORECLOSED: recording “objection solved by shorter meeting” contradicts the unchanged preparation condition.','An actor with a separate time objection is a different case; that possibility is not inferred from this reply.'),
('For a proposal intended to address that objection, the option comparison includes a genuinely optional-preparation format or a decision not to proceed.','An option that still penalizes unprepared attendance is not the stipulated optional format.','Allowing the person to stop can end the intended shared activity; that cost remains visible.'),
('A newly offered optional-preparation role is a proposal; the earlier refusal does not establish its acceptance.','FORECLOSED: the proposal cannot be entered as an agreed weekly commitment without a new acceptance premise.','A real reply can accept one visit and reject recurrence, so the response field retains scope.'),
('With no reply to that proposal, the agreement record remains pending even though the next question has improved its fit to the stated condition.','The model can change a question without changing the other actor’s commitment.','The opportunity cost is a conversation that may end unresolved; the original voluntary goal permits that state.'),
('Generated record: “Obligation was the stated objection; optional-preparation role offered; acceptance unknown.” This matches the constructed transcript and no further commitment.','','')]
B1=[
('An invitation that permits refusal can obtain a clear no; that no is still a response rather than a missing success mark.','FORECLOSED: interpreting every no as a defect in the invitation assumes the very participation outcome left optional.','A clearer refusal can reduce ambiguity while decreasing the number of continuing interactions.'),
('If the no expresses a stable boundary, the next useful operation can be recording the boundary instead of persuading the actor to reverse it.','The record “raw notes not for publication” preserves a condition relevant to future drafts.','The actor can later change the boundary; current recording does not freeze a permanent personality trait.'),
('A recorded scope boundary changes which future draft options remain authorized under the constructed participation rule.','FORECLOSED: a majority preference cannot supply a contributor’s missing permission when that rule reserves it to the contributor.','An independent synthetic example remains a possible draft if labeled and genuinely independent.'),
('If a later draft uses only an approved finalized excerpt, it can meet the scope rule without converting the earlier no into general agreement.','Approval of one finalized excerpt says nothing about all raw material.','Exact version tracking adds work, but prevents a different excerpt from silently inheriting permission.'),
('Generated draft record: “finalized excerpt v2 approved; raw notes excluded; general endorsement unknown.” This is a distinct local output using the refusal boundary.','','')]
C1=[
('The informative-refusal hypothesis distinguishes accuracy of the next question from renewed interest in the activity.','FORECLOSED: a better-matched next question is not itself an observed increase in interest.','The person may prefer no further conversation even when the question accurately represents their concern.'),
('If the target is accurate understanding, a correct stop after “I do not want to discuss this” can meet that local target.','A follow-up demanding the hidden reason is unnecessary for representing the stated stop preference.','The broader relationship aim can remain unmet while the local understanding is accurate.'),
('A stop response creates a different next-action set from a response that invites an alternative format.','The generated reply to stop can be “Understood”; the reply to a format invitation can compare specific options.','Different branches cost some template simplicity, but preserve the explicit difference in the supplied replies.'),
('For the two reply forms, a branching answer policy preserves more of the available explicit information than a fixed persuasion script.','FORECLOSED: one compulsory encouragement paragraph cannot be assumed appropriate for both the stop and alternatives-invited branches.','This comparison is finite and textual; its interpersonal impact is deferred until actual responses exist.'),
('Generated outputs: stop reply → “Understood; we can leave it here.” Alternatives-invited reply → “Would an optional-preparation session fit?” No actual person receives either.','','')]

A2=[
('If a self-chosen two-minute gateway can increase voluntary starts without lowering intrinsic interest, at least one eligible context must show both outcomes together.','FORECLOSED: a start increase with an interest decrease does not demonstrate this conjunctive intuition.','An interest gain with no increased starts is another possible benefit but not this exact effect.'),
('A study of that conjunction must distinguish initiated inquiry from time spent preparing and must record inherent interest separately.','A document-open event alone does not establish an initiated substantive inquiry if the defined behavior is a written example.','A self-report of enjoyment alone cannot count the actual example; measurement channels differ.'),
('Given a comparison that holds the chosen question and freedom to decline fixed, the manipulated gateway can be separated from a change in task content.','FORECLOSED: switching to a more attractive question at the same time prevents attributing a difference solely to gateway structure.','Equal question content still leaves individual preferences and prior skill as possible moderators; human data are unavailable.'),
('If groups are randomly assigned to the gateway and equally optional active-control conditions, measured baseline differences are not a required explanation of an average difference.','Randomization does not guarantee identical finite groups; baseline imbalance remains reportable.','Allocation concealment prevents a recruiter from selecting a favored condition for particular people, if actually implemented.'),
('If the planned comparison preserves optionality and measures both endpoints, a positive start effect still needs an interest-loss bound before satisfying the no-reduction part.','FORECLOSED: failure to find a significant interest decrease is not itself evidence of no meaningful decrease.','A predeclared noninferiority margin operationalizes a bounded version; exact zero loss is harder and remains distinct.'),
('A predefined start threshold and interest-loss margin make a future result classifiable as supporting, conflicting or unresolved for the operationalized hypothesis.','Changing the margin after seeing results would test a new hypothesis.','Adequate sample assumptions and missing outcomes remain necessary for interpreting the planned interval.'),
('Deferred test: compare a voluntary gateway and an equally voluntary active control using the predeclared substantive-start outcome and interest-loss margin. No participants or outcome data are available in this run.','','')]
B2=[
('Because the intuition concerns self-chosen inquiry, a compulsory gateway is outside its specified scope even if it raises starts.','FORECLOSED: a required daily streak cannot demonstrate an effect on self-chosen initiation merely by producing completions.','A person can freely choose a routine initially and later withdraw; the original consent is not perpetual interest evidence.'),
('If participants can decline each opportunity, the record distinguishes offered opportunities, accepted opportunities and completed examples.','A missing opportunity is not a refusal; refusal is not a failed completion.','This distinction can reduce the apparent completion rate compared with a simplistic denominator.'),
('A valid denominator for voluntary initiation must be fixed to the declared opportunity definition before comparing conditions.','FORECLOSED: removing refusals from only one arm changes the comparison population.','Accessibility failures can be recorded separately if the definition treats them as no valid opportunity; that rule must be symmetric.'),
('A symmetrical opportunity rule permits interpreting a rate difference without silently treating one group’s nonparticipation differently.','The rule does not identify why a person declined; motive remains unobserved.','The resulting study can have fewer usable opportunities and wider uncertainty than a convenient completed-only analysis.'),
('Deferred test: audit offered, accessible, declined, started and completed events in both proposed conditions using the same rules. Actual human events are absent.','','')]
C2=[
('A two-minute gateway is an entry behavior, so its completion and the full inquiry’s completion are separate possible outcomes.','FORECLOSED: a checked gateway box does not establish a completed comparison when no countercase was written.','A gateway can be worthwhile as preparation even if the larger inquiry is postponed; that is a different benefit claim.'),
('If the full goal remains independent inquiry, monitoring includes later substantive continuation rather than only the small start.','A rise in starts with no continuation can indicate a bottleneck moved downstream.','A person can intentionally stop after a useful example; continuation is interpreted with the chosen goal, not as mandatory escalation.'),
('A follow-up comparison distinguishes a gateway that opens meaningful inquiry from one that merely shifts effort into record keeping.','FORECLOSED: more tracking marks alone cannot demonstrate more independent investigation.','Measuring substantive work costs coding effort; criterion reliability is not yet established.'),
('A blind assessment of de-identified examples against a fixed criterion could test substantive inquiry while reducing knowledge of the assigned condition.','Blinding is proposed, not performed; recognizable prompt wording can still reveal condition.','Disagreements between coders would need resolution without changing the criterion to favor the expected result.'),
('Deferred test: rate actual later examples/counterexamples under a fixed rubric and inspect agreement and condition visibility. No human submissions exist here.','','')]

if __name__=='__main__':
 ar('dependency-ig-1-ar','A refusal can carry useful information for choosing the next conversational step.',[A1,B1,C1],[
 'Constructed input 1: “The hour is fine; mandatory preparation is not.” Actual generated question: “Would a session without required preparation fit, or would you rather leave it here?” Agreement field remains pending.',
 'Constructed input 2: “Please do not publish the raw notes; this finalized excerpt is okay.” Actual generated scope record permits that excerpt only. No permission is inferred for a new excerpt.',
 'Constructed input 3: “I do not want to discuss it.” Actual generated response ends the thread. Human reception is deferred.'])
 ar('dependency-ig-2-ar','A self-chosen two-minute gateway can increase voluntary starts without reducing intrinsic interest.',[A2,B2,C2],[
 'Local measurement application: mock event sequence offered/access missing is marked no accessible opportunity; offered/declined is a decline; offered/accepted/example written is a substantive start. These are constructed classifications, not participant outcomes.',
 'All causal human predictions are deferred because there are no participants, independent consented conditions, repeated opportunity records or interest outcomes. The separate EXD design specifies what would be measured.'])
 print('Two AR dependency registries written')
