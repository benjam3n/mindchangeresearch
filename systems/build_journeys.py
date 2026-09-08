from write_records import save,BASE
from build_araw import build_araw
from fractions import Fraction
import json,itertools
chains={
'journey-budget':{
'AR':[
'Given C1’s sufficiency claim, a direct-benefit maximizer would accept its nominally feasible maximum C+E+G.',
'Given that selected set, C is included; the declared prerequisite edge means S must also be completed.',
'Given S is required and costs10, the selected set’s accounted cost must include an additional10 beyond nominal60.',
'Given nominal60 plus prerequisite10, the actual selected cost is70.',
'Given current budget60, cost70 exceeds the resource bound by10.',
'Given a ten-unit excess, the selected set fails feasibility even though it wins the direct-benefit calculation.',
'Given a direct-benefit-selected set that fails feasibility, C1’s claimed sufficiency for every feasible bundle has a counterexample.'],
'AW':[
'Given the counterexample, a candidate replacement closes selected sets over their prerequisites before comparing costs.',
'Given closure of C+E+G includes S, its cost70 is compared against budget60 before acceptance.',
'Given the over-budget rejection, dropping G removes15 cost and8 supplied value from that closed set.',
'Given that removal, S+C+E costs55 with value58.',
'Given budget60 and all declared dependencies present, S+C+E is feasible with5 units unused.',
'Given unused5 and remaining G cost15, G cannot be restored to this set without violating the budget.',
'Given exhaustive comparison of all16 subsets, no other feasible set exceeds58; the closed-set optimum is S+C+E.']},
'journey-continuity':{
'AR':[
'Given C1’s sufficiency claim, retaining the v1 winner A would be sufficient for correct later reuse.',
'Given the retained v1 record and a later task explicitly using fidelity weight.3, its current recommendation must be evaluated under that weight.',
'Given A scores(5,2) and weight.3, its current weighted score is2.9.',
'Given A’s current score2.9 and B scores(3,5) under the same weight, B scores4.4 and exceeds A by1.5.',
'Given B exceeds A in the later criterion, the saved A recommendation is not the maximizing current choice.',
'Given saved A is not the current maximizing choice, retention alone did not supply a correct reuse decision.',
'Given that same saved-result countercase, C1’s unqualified sufficiency fails while the old v1 arithmetic remains intact.'],
'AW':[
'Given the wrongness case, a replacement retains the criterion version with the saved result.',
'Given the stored version differs from the current.3 criterion, retrieval returns historical A plus a current-fit reassessment obligation.',
'Given reassessment compares 2+3w with5−2w, the difference is5w−3.',
'Given difference5w−3, the sign changes at w=.6.',
'Given present w=.3<.6, B is the current selected option.',
'Given separate historical and current fields, selecting B does not overwrite A’s v1 result.',
'Given both fields are retained, a later w=.8 recurrence can recover the original A comparison without falsely claiming v2 never occurred.']},
'journey-agency':{
'AR':[
'Given C1’s task-name sufficiency, a result labeled T is eligible by that label alone.',
'Given T revision1 was dispatched before revision2 became current, its late output still has the same task name T.',
'Given label-only sufficiency and a matching label, the late revision1 output is accepted.',
'Given acceptance uses that output as the current task answer, the current revision2 goal receives revision1 work.',
'Given revisions differ in their requested target, that work does not satisfy the current target by name identity alone.',
'Given the accepted output fails the current target condition, label matching is insufficient for acceptance.',
'Given this exact same-name changed-revision case, C1 is refuted; the historical work can remain available without current acceptance.'],
'AW':[
'Given the wrongness case, acceptance requires current revision as well as task identity.',
'Given returned revision1 differs from current2, the return is marked obsolete before current acceptance.',
'Given obsolete status, the current accepted-result field remains empty rather than taking revision1.',
'Given no current result exists, a new revision2 result is needed if the task remains active.',
'Given a subsequent stop event sets active=false, that needed new result no longer authorizes dispatch.',
'Given dispatch and acceptance both read active=false, neither new B dispatch nor late A acceptance occurs.',
'Given no new action is committed after stop in the finite trace, the requester’s current cancellation controls these transitions.']}}

def emv_dep(n,key):
 predictions=[{'id':f'P{i+1}','confidence':90 if i!=3 else 80,'status':'PENDING'} for i in range(5)]
 (BASE/f'{key}-emv-pre.json').write_text(json.dumps(predictions,indent=2))
 if n==1:
  acts=[('S',10,0),('C',25,40),('E',20,18),('G',15,8)];tests=[]
  for budget in [0,9,10,14,15,20,34,35,40,55,60,70]:
   feasible=[]
   for bits in itertools.product([0,1],repeat=4):
    selected=[x for x,z in zip(acts,bits) if z];names=[x[0] for x in selected];cost=sum(x[1] for x in selected);value=sum(x[2] for x in selected)
    if cost<=budget and ('C' not in names or 'S' in names):feasible.append({'names':names,'cost':cost,'value':value})
   best=max(feasible,key=lambda x:(x['value'],-x['cost']));tests.append({'budget':budget,'best':best})
  checks={'all_feasible':all(t['best']['cost']<=t['budget'] for t in tests),'prerequisite_closed':all('C' not in t['best']['names'] or 'S' in t['best']['names'] for t in tests),'value_monotonic':all(a['best']['value']<=b['best']['value'] for a,b in zip(tests,tests[1:])),'whole_bundle_algebra':tests[-1]['best']['cost']==10+25+20+15,'direct_40_case':next(t['best']['value'] for t in tests if t['budget']==40)==40}
  edges=['zero budget','below all positive-value actions','zero-value source-only option','first useful action exactly affordable','prerequisite pair exactly affordable','all actions exactly affordable']
  actual=[tests[0]['best']['names']==[],tests[1]['best']['names']==[],tests[4]['best']['names']==['G'],tests[7]['best']['names']==['S','C'],tests[-1]['best']['value']==66]
  pred=['budget0 selects empty','budget9 selects empty','budget15 selects G','budget35 selects S+C','budget70 reaches66']
 elif n==2:
  ws=[Fraction(x,100) for x in [0,10,30,50,59,60,61,70,80,90,100]]+[None];tests=[]
  for w in ws:
   if w is None:tests.append({'w':None,'choice':'UNRESOLVED'});continue
   a=2+3*w;b=5-2*w;tests.append({'w':str(w),'A':str(a),'B':str(b),'choice':'A' if a>b else 'B' if b>a else 'tie'})
  checks={'direct_weighted_form':all((w*5+(1-w)*2)==2+3*w for w in ws if w is not None),'difference_formula':all((2+3*w)-(5-2*w)==5*w-3 for w in ws if w is not None),'boundary_tie':tests[5]['choice']=='tie','unknown_not_imputed':tests[-1]['choice']=='UNRESOLVED','historical_v1_retained':(Fraction(8,10)*5+Fraction(2,10)*2)==Fraction(44,10)}
  edges=['all speed','all fidelity','exact tie','just below tie','just above tie','missing weight']
  actual=[tests[0]['choice']=='B',tests[5]['choice']=='tie',tests[6]['choice']=='A',tests[-1]['choice']=='UNRESOLVED',tests[8]['choice']=='A'];pred=['w0 favors B','w.6 ties','w.61 favors A','unknown weight unresolved','w.8 favors A']
 else:
  tests=[]
  for active,rev,action in itertools.product([False,True],[1,2],['describe','inspect','execute']):
   accepted=active and rev==2 and action in ['describe','inspect'];tests.append({'active':active,'returned_revision':rev,'current_revision':2,'action':action,'accepted':accepted})
  checks={'stopped_rejects':all(not t['accepted'] for t in tests if not t['active']),'obsolete_rejects':all(not t['accepted'] for t in tests if t['returned_revision']==1),'unauthorized_rejects':all(not t['accepted'] for t in tests if t['action']=='execute'),'two_authorized_active_cases':sum(t['accepted'] for t in tests)==2,'conjunction_equivalence':all(t['accepted']==all([t['active'],t['returned_revision']==2,t['action']!='execute']) for t in tests)}
  edges=['stopped current description','active obsolete description','active current execution','stopped obsolete execution','active current inspect','stopped current inspect']
  actual=[not tests[0]['accepted'],not tests[6]['accepted'],tests[9]['accepted'],tests[10]['accepted'],not tests[11]['accepted']];pred=['stopped obsolete describe rejects','active obsolete describe rejects','active current describe accepts','active current inspect accepts','active current execute rejects']
 for p,a,meaning in zip(predictions,actual,pred):p.update({'prediction':meaning,'outcome':a,'status':'CONFIRMED' if a else 'DISCONFIRMED'})
 data={'tests':tests,'checks':checks,'edge_cases':edges,'calibrations':predictions}
 (BASE/f'{key}-emv.json').write_text(json.dumps(data,indent=2))
 save(key+'-emv','emv','EMV dependency: '+key,'Change the parent goal journey’s testable predictions using actual finite input cases.','The parent claims have been explored but the present parameter and boundary suite has not yet been executed.',
 f'''Predictions: {', '.join(pred)}. Failure would mean a feasibility, choice or acceptance result differs from the declared equation/contract. The crux is whether the candidate survives boundaries that change the parent goal choice. Minimal test uses twelve local cases; no human participants or external service data are required.

Test-first is selected because the action is reversible and these checks precede commitment. `{'%s-emv-pre.json'%key}` retains five pre-run confidence declarations; `{'%s-emv.json'%key}` retains every input, actual result and calibration. Exact test products: {json.dumps(tests)}.

Five distinct checks: {json.dumps(checks)}. These are independent mathematical/contract routes in the same local runtime, not independent empirical replications. Six edge cases: {', '.join(edges)}. Five forecast-to-outcome comparisons: {json.dumps(predictions)}. A confirmed definition-level prediction is not evidence of global confidence calibration.

Update: use the computed result only under its supplied budget, criterion or authority conditions. A missing external condition remains unresolved; the favorable finite suite does not prove a human effect. The result is directly consumed by the parent GJS testable-prediction table.''',
'The parent now has twelve actual finite results rather than only proposed tests.','The suite supplies concrete boundary outcomes for the parent plan; scope remains the defined equations/contracts.','KEEP','Inputs, predictions and actuals remain separate and linked; a summary pass count is insufficient.','Change one model premise; add an external observation if available; check whether a new case belongs to the tested domain.',depth='Original 8x floors: 12 tests, 5 distinct mathematical/contract checks, 6 tested edge cases and 5 predeclared confidence comparisons.')
 return data

originals=[
'Judge operations together when one enables, obstructs, or changes another.',
'Include effects on later opportunities and on the ability to recognize, choose, perform, and revise future changes.',
'Keep the person able to inspect, disagree, decline, and redirect.']
for n,key in enumerate(['journey-budget','journey-continuity','journey-agency'],1):
 reg=build_araw(key,chains[key]);emv=emv_dep(n,key)
 save(key+'-ve','ve','Value elicitation dependency: '+key,'Determine whether the practical goal chain reaches a stated intrinsic value without inventing an answer.','The practical purpose is explicit in the selector; the user’s terminal reason for valuing it has not been directly elicited in this subtask.',
 f'''Stated goal, quoted exactly from the governing selector: "{originals[n-1]}"

Step2 question: "What is important to you about this goal?" Available documentary response: the selector requires useful changes grounded in the person’s expressed concerns, agency and observed consequence. This supports practical design constraints; it is not a new human reply to the question.

Step3 chain: performed local contribution→inspectable effect→useful continuation of the requested program. The next "what is important about useful continuation?" has no supplied answer. Step4 circularity is not observed; no "because I value it" answer is invented. Step5 additional-value question is likewise unanswered; absence of a reply is not a negative reply. Step6 additional chains cannot be elicited without an actual answer. Step7 possible efficiency/agency/understanding tradeoffs are candidate interpretations, not confirmed intrinsic conflicts.

Step8 value map therefore preserves the practical chain and an explicitly unknown intrinsic terminus. The original interpersonal elicitation is partial. This blocks certification of a completed intrinsic-value chain while allowing the already authorized practical work to proceed. No permission is requested for reversible local work, and no other person is contacted.''',
'An intrinsic-value assertion is withheld; the known practical goal remains usable.','The scope is honest, but the intended interpersonal elicitation has not been completed.','UNRESOLVED','A partial value map preserves the unanswered question instead of substituting an inferred terminal value.','Use a genuine later answer if provided; compare two supported practical chains; retain uncertainty if the person declines elicitation.')
 body=f'''Context: normal time, medium stakes for this local case, user expertise supported by a detailed selector, cheap reversible artifact actions, rich local instruction but sparse human outcome data. GOSM-Standard context variant is selected; all ten GJS steps are addressed here. Requested 8x expansion is carried by the invoked original ARAW and EMV floors.

Original goal, exact quotation from the governing selector: "{originals[n-1]}" No smaller goal or assumed underlying need replaces it. Clarification is the concrete {'resource-bundle' if n==1 else 'future-reuse' if n==2 else 'agency-boundary'} instance; it does not establish the global goal accomplished.

Parsed claims: eighteen analytical OPEN candidates and their exact consequences/countercases are in `{key}-araw.md` and its registry. Mathematical definitions of the supplied cost/criterion/permission fixtures are CLOSED within the model, not asserted as human facts. All OPEN candidates are explored through the original ARAW dependency; its certificates control this record’s conclusions.

Goal journey: CURRENT STATE—candidate policy with untested broad sufficiency; DESIRED STATE—conditional plan that preserves actual benefit evidence; IMMEDIATE GOAL—{'choose a prerequisite-valid resource bundle' if n==1 else 'make a retained result conditionally reusable' if n==2 else 'preserve current human direction in action interfaces'}; SERVES—the exact quoted practical goal; INTRINSIC GOAL—unknown, requires a real answer; WHY NOW—the assigned systems investigation; SUCCESS—actual changed finite choice with known scope; CONSTRAINTS—original procedures, no invented human effects, current host and authorization.

Chain: {'source preparation→feasible comparison→usable choice→expressed whole-arrangement goal' if n==1 else 'retained criterion and evidence→current fit decision→usable later option→expressed future-change goal' if n==2 else 'current permission and stop state→bounded action acceptance→inspectable voluntary contribution→expressed agency goal'}. Each technical link is supported by the finite tests. The terminal human value is not established; the explicit `/ve` dependency records the missing elicitation rather than inventing it.

Dual analysis: NON-CONTRARIAN—{'retain S’s enabling role and compare closed subsets' if n==1 else 'preserve historical evidence with criterion and validity conditions' if n==2 else 'accept current authorized outputs and preserve declined work as history'}. CONTRARIAN—{'a direct output-only maximum is infeasible' if n==1 else 'saved bytes alone do not secure retrieval or correct reuse' if n==2 else 'a task label, favorable forecast or prepared description does not authorize execution'}. These are derived from the ARAW registry; none replaces the exact program goal.

Testable predictions: twelve finite cases, five independent mathematical/contract routes, six boundaries and five confidence comparisons are executed in `{key}-emv.md`. All high-priority currently executable predictions are tested. Human benefit and future recurrence remain testable only when actual participants/conditions exist; their absence is not a failed human intervention.

Questions ranked: intrinsic reason and additional values—HIGH for full chain completion, unanswered; actual recurrence/authority changes—HIGH for future use, determined by later input; presentation details—LOW, current format adequate. Next route is `/ve` when a real value answer arrives; no substitute intrinsic story is accepted.

Actual application: {'the goal chain retains preparation S rather than deleting its zero-direct-benefit cost; the budget40 and60 outputs are distinct' if n==1 else 'the current choice changes with criterion version while the historical comparison remains intact' if n==2 else 'the active/revision/authority conjunction rejects a seemingly useful but unauthorized execution proposal'}. The transformed case is complete; the original intrinsic-value elicitation dependency remains partial.'''
 save(f'043-gjs-{n}','gjs','Goal journey: '+key,'Change a system goal chain through original claim search and empirical validation while preserving the requested goal.', 'The concrete plan is plausible, but the links from action through goal and intrinsic value have not all been established.',body,'The technical goal chain now uses tested conditional transitions; its intrinsic terminus remains unknown.','The finite application supplies a useful scoped decision, but complete original value elicitation is unavailable.','UNRESOLVED','Goal chain plus source-linked certificates separates technical support from an inferred human motive.','Incorporate an actual elicitation answer; test a new input context; inspect an action whose practical chain differs.',depth='GJS defines no numerical 8x table. Mandatory ARAW and EMV dependencies are executed at their numerical 8x floors; VE is invoked but partial because no genuine elicitation response is available.')
