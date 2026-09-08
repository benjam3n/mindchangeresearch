from write_records import save,BASE
from build_araw import build_araw,sets
import json
# Exact-scope disagreements with explicit original source assertions.
sets['audit-evidence'][2]=('A shared property of all three generated scenarios is thereby a high-confidence prediction.','Three selected worlds would be enough to assign high confidence to their common property.','In a defined ten-world equiprobable space, the three considered worlds have P and seven omitted worlds lack P; probability(P)=.3.','Scenario agreement remains conditional on coverage and probability assumptions.','REJECTED')
sets['audit-evidence'][11]=('Every intervention that pushes against a balancing loop is absorbed by the system’s compensation.','A restoring controller would always offset the external push.','A controller removes at most.5 unit/cycle while an external input adds1; stock grows by at least.5 despite the balancing signal.','Compensation is limited by actuator capacity and disturbance magnitude.','REJECTED')
sets['audit-evidence'][15]=('An analysis with more than80% of claims validating the user’s position is necessarily confirming rather than analyzing.','Even independently derived correct claims would make the analysis invalid because too few were rejected.','A finite analytical set can contain nine true propositions and one false one; testing every proposition correctly yields90% validation without skipping a test.','Verdict proportion is a warning signal; validity depends on actual tests and parent-child inferences.','REJECTED')
chains={
'audit-purpose':{'AR':[
'Given C1’s coherence sufficiency, a coherent source→comparison→decision chain would establish benefit without checking access.',
'Given that chain requires an original source, producing the comparison depends on actually obtaining its contents.',
'Given the constructed source endpoint is unavailable, its contents do not enter the comparison input.',
'Given the comparison input is absent, the defined comparison operation cannot execute on the required source.',
'Given the required operation has not executed, no actual comparison consequence is available to support the decision.',
'Given no actual comparison consequence, coherent descriptions of later benefit remain predictions rather than observed effects.',
'Given coherence persists while the required effect is unavailable, C1’s sufficiency is refuted by this source-access case.'],
'AW':[
'Given the wrongness case, the plan separately represents coherent chain and available prerequisites.',
'Given source access is marked unavailable, execution status remains blocked at that input rather than complete.',
'Given blocked input status, the downstream comparison cannot be credited as a performed operation.',
'Given the comparison is unperformed, its proposed benefit cannot enter the demonstrated-keep set.',
'Given no demonstrated keep from that comparison, a consolidation cannot cite it as established support.',
'Given the unsupported citation is excluded, the integration retains only actual earlier evidence while preserving the planned comparison as pending.',
'Given the original source later becomes available, the same preserved plan can resume without rewriting a fictional prior success.']},
'audit-evidence':{'AR':[
'Given C1’s field-pass sufficiency, a packet passing every required field would establish its returned proposition true.',
'Given a complete packet contains the literal claim2+2=5, all required field names can still be present.',
'Given the field consumer checks presence and version only, the complete false-claim packet is accepted by that contract.',
'Given C1, accepting the packet by those checks would imply its arithmetic proposition is true.',
'Given integer addition yields2+2=4, the returned proposition2+2=5 is false.',
'Given a field-accepted packet carries a false proposition, the C1 implication from field pass to truth fails in the exact case.',
'Given that failure, increasing the number of identical field checks does not establish semantic truth of that packet.'],
'AW':[
'Given the wrongness case, the result type is split into contract-valid and proposition-verified.',
'Given presence/version checks pass, only contract-valid becomes true.',
'Given a separate arithmetic evaluation returns4, the claim2+2=5 fails proposition verification.',
'Given proposition verification fails, the downstream truth claim is rejected while the successful contract result remains historical.',
'Given the truth claim is rejected, a later synthesis cannot cite the field tests as evidence that2+2=5.',
'Given source/evidence identity is retained, the mismatch can be traced to the semantic-verification gap rather than blaming an absent input field.',
'Given that exact gap is repaired with a relevant arithmetic check, the corrected packet can carry2+2=4 without rewriting the first false output as correct.']}}
for n,key in enumerate(['audit-purpose','audit-evidence'],1):
 reg=build_araw(key,chains[key]);counts={v:sum(x['verdict']==v for x in reg['verdicts']) for v in ['VALIDATED','REJECTED','CONDITIONAL','UNCERTAIN']}
 extra=''
 if n==2:
  external=[];x=0
  for t in range(10):x+=1-min(.5,x);external.append(x)
  check={'scenario_countermodel':{'worlds':10,'considered_P_worlds':3,'omitted_notP_worlds':7,'P_probability':.3},'saturated_balancing_loop':external,'verdict_ratio_countermodel':{'true_analytical_claims':9,'false_analytical_claims':1,'independent_correct_tests':10,'validation_fraction':.9}}
  (BASE/'audit-source-disagreements.json').write_text(json.dumps(check,indent=2))
  extra='''Three independent disagreements with source assertions are explicitly retained. Original `/fut` labels a property shared by all three generated scenarios high-confidence; a ten-world countermodel gives it probability.3. Original `/systhink` says balancing-loop resistance absorbs the push; a bounded.5 actuator facing1 inflow accumulates stock despite that loop. Original ARAW treats a high validation fraction as confirming rather than analyzing; a fully tested nine-true/one-false analytical set is a countermodel to using the fraction as sufficient proof. These disagreements concern exact asserted relationships, not stronger substituted claims. They do not imply the procedures never help. `audit-source-disagreements.json` contains the executed finite models.'''
 body=f'''Audit scope: {'GOSM goal-chain and completion claims' if n==1 else 'the original system’s evidence, dynamics and confidence claims'}. Source material includes the exact GJS, EMV, ARAW and related original system procedures already retained. Imported standards are labeled as such; independently generated countercases are the audit evidence. The assistant is auditing its own work and procedures, so this is not independent certification.

Claim inventory distinguishes literal source statements, design implications and deliberately tested sufficiency candidates. A candidate such as coherence-is-sufficient is not attributed as a literal GOSM promise: original EMV explicitly rejects it. Its role is to test whether the current execution accidentally behaves that way. All eighteen claims, their evidence, falsifiers, contrary branches and derived alternatives are in `{key}-araw.md` and the complete registry.

Mandatory `/araw` execution has18 claims, {reg['totals']['findings']} tracked findings, {reg['totals']['independent_propositions_before_semantic_dedup_review']} independent proposition candidates after excluding repeated scope-review remarks, two seven-edge branches, eight cruxes and two executed subject-specific tests. Counts do not by themselves certify semantic validity; every certificate points to its actual countercase or failed contrary argument.

Own-standards results: the audit preserves direct useful contributions, explicit scope and observed current behavior. It rejects load-bearing sufficiency claims about coherence/format/retention and preserves the full user program. No claim about a pleasant human conversation is established without human feedback. The current budget arithmetic repair and actual packet evaluations are available behavior; source/SSR tooling gaps remain visible rather than becoming fictitious successes.

Limitations: {'an intrinsic-value chain remains incomplete when no real elicitation response exists; source receipt cannot fill that gap; a full method can be excessive for a trivial question; quoted documentation is not evidence of execution' if n==1 else 'contract tests miss semantic truth; hypothetical rates do not establish field reliability; power for a different estimand cannot be imported; generic validation percentages cannot replace actual countercases'}. Required missing original tools are recorded as unmet dependencies.

Alternatives compared: direct useful answer has lower cost for a settled simple fact; finite enumeration precisely resolves small constrained choices; original goal-chain analysis helps expose the gap between a means and the requested goal; empirical study is needed for human outcome/transfer claims. No broad head-to-head effectiveness trial is present, so general GOSM superiority remains unresolved.

{extra}

Report:18 claims tested; validated{counts['VALIDATED']}; refuted{counts['REJECTED']}; weakened0; unresolved0 at the stated finite propositions, with transfer and real human effects still unresolved. Refuted universals are not relabeled conditional; their narrower alternatives are separate registry items. Improvement priority is {'preserve blocked source/value/tool stages as partial and continue available authorized operations' if n==1 else 'tie confidence and completion claims to the exact tested proposition, and correct overbroad source heuristics only in application without modifying original archives'}.

Actual application: {'the completion ledger will label GJS’s missing interpersonal elicitation partial instead of allowing the passing finite suite to certify a fully completed intrinsic-value chain' if n==1 else 'the current report no longer calls three-scenario agreement high-confidence or assumes a balancing loop necessarily absorbs disturbance; the executed countermodels govern those claims'}. The source archives are unchanged.'''
 save(f'093-gaa-{n}','gaa','GOSM approach audit: '+key,'Change the current system’s own claims where its original standards fail the concrete case.', 'The original procedures supply detailed operations and have produced useful local examples; their general sufficiency and every strong heuristic have not been established.',body,'The audit rejects specific load-bearing sufficiency claims and preserves supported finite results without certifying general superiority.','The altered completion/confidence/dynamics claims follow concrete countercases; independent human validation remains absent.','KEEP','Claim inventory plus exact certificates retains what was literally sourced versus what was tested as an execution implication.','Obtain actual human feedback on fit; test an independent held-out case; inspect a source claim that survives a strong contrary branch.',depth='GAA has no own numeric 8x table. Its mandatory ARAW dependency executes18 claims, more than55 independent proposition candidates, two seven-edge branches,8 cruxes and2 live tests; root semantic review remains important.')
