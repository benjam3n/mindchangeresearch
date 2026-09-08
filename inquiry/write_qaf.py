from pathlib import Path
import json
R=Path('/workspace/scratch/78b838bd97fc/mind-change-research/inquiry')
def write(name,intent,start,qs,found,paths,later):
 s=f'''Intended mind change: {intent}

Starting working judgment and concrete input: {start}

Original: ../sources/inquiry-qaf.original.md and separate receipt. Eighteen questions are classified, at least twelve actual dependencies mapped, five foundation questions designated and five resolution paths executed. Original scales name Foundationality, Prior Art, Verifiability and Tractability from1–5 but do not supply a scoring formula. The local transparent ordering score here is F+V+T+(6−P), favoring foundational, answerable and less-settled questions; it is an implementation choice, not an original-source formula. Resolved prerequisite checks are retained but filtered from the next unresolved queue. Scores are ordinal planning judgments, not truth probabilities.

Foundation questions: {', '.join('Q'+str(i) for i in found)}. These define the actual object, premises, meaning or criterion used by dependent questions, rather than five invented synonyms for “what is the goal?”. Prior-art scores concern exact prior records/formal definitions available here; no claim of a comprehensive literature review is made.

| ID | Exact question | F/P/V/T | Position / score | Actual answer and premise confidence | Depends on |
|---|---|---|---|---|---|\n'''
 for i,(q,sc,ans,deps) in enumerate(qs,1):
  f,p,v,t=sc;score=f+v+t+6-p;pos='foundation' if i in found else 'derived'
  s+=f'| Q{i} | {q} | {f}/{p}/{v}/{t} | {pos}; {score} | {ans} | '+(', '.join('Q'+str(x) for x in deps) if deps else 'declared input / direct observation')+' |\n'
 depcount=sum(len(x[3]) for x in qs);assert depcount>=12
 s+=f'\nThe dependency graph has {depcount} directed prerequisite edges. Edges mean “this specified derivation consumes that answer,” not that every imaginable way of answering requires the same path. No cycles occur because each dependency refers to an earlier numbered question.\n\n'
 for i,path in enumerate(paths,1):s+=f'Resolution path {i}: {path}\n\n'
 s+='''Certainty documentation: “deductive under declared premises” assigns guessing=0 to that derivation while retaining the premise condition; “direct receipt” assigns guessing=0 to the observed bytes, not their semantic truth; an unavailable source intention or human observation is guessing=1 if someone tried to supply its missing value now, so no such value is supplied. No frequentist calibration or global certainty is inferred from these bookkeeping values. Empirical questions remain empirical even when a related formula is known.

'''+ 'Distinct later application: '+later+'''\n
Actual mind change: The next unanswered question is selected from its actual prerequisite set, while already resolved foundations remain available as support.
Benefit: The performed dependency order preserves known answers and genuine gaps. No independent new keep is claimed for repeating earlier scope or control distinctions.
Verdict: UNRESOLVED
Organization: The classification table, dependency edges and five actual answer paths retain separate roles; uncertainty remains attached to the specific unavailable premise.
Next attempts: Answer a decision-relevant unresolved leaf when evidence becomes available; skip a missing premise only when the declared rule demonstrably does not depend on it; test the same ordering on a new target.
'''
 (R/name).write_text(s);(R/(name[:-3]+'.json')).write_text(json.dumps({'questions':[{'id':i,'question':q,'scores':sc,'answer':ans,'depends_on':ds} for i,(q,sc,ans,ds) in enumerate(qs,1)],'foundation':found,'edges':depcount},indent=2)+'\n')
q=[
('Is the query literal source attribution or semantic applicability?',[5,5,5,5],'Input specifies applicability of the sure/maybe relation plus the declared clause11 fixture; direct task observation.',[]),
('Which exact source bytes are available?',[5,5,5,5],'438 receipts and hashes are available; parent integrity check verifies bytes, not meanings.',[]),
('What are the two endpoint scopes?',[5,4,4,4],'Paired fixture supplies P,t; original generic edge scope remains unspecified.',[]),
('Which predicate meanings are admitted?',[5,4,5,5],'S=p=1, M=p>0 or strict0<p<1; meanings are stipulated separately.',[]),
('Which conditions qualify clause11?',[5,2,5,5],'FRQ43 fixture declares conjunction of clauses2 and7; completeness is a fixture premise.',[]),
('What exactly does the export assert?',[4,5,5,5],'sure→maybe uses the certainty/uncertainty reason; direct receipt, no endorsement.',[1,2]),
('Are the instantiated relation operands aligned?',[4,4,5,5],'The specified P,t pair is aligned; original generic use remains unknown.',[3,6]),
('Is the aligned S∧M set nonempty?',[4,5,5,5],'Positive M: witness1; strict reading: empty by p=1 andp<1; deductive.',[4,7]),
('Does the source label alone resolve its semantic verdict?',[4,5,5,5],'No: Q8 gives different results under the two meanings; intended sense unresolved.',[6,8]),
('Does an edge’s high weight overturn that distinction?',[2,5,5,5],'No in the declared predicate model: weight is not an operand; source ranking remains separately available.',[1,9]),
('Which declared qualifier values are currently available?',[4,2,5,5],'Clause2=true; clause7 unavailable in this supplied fixture.',[2,5]),
('Is clause11 applicable with those values?',[5,3,5,5],'Unresolved: 1∧1=1 and1∧0=0; the unavailable value changes output.',[5,11]),
('Which retrieval could resolve applicability?',[4,3,5,5],'Condition7, because its two completions differ while2 is fixed true.',[1,12]),
('Would7 still be necessary if2 were false?',[3,3,5,5],'No for this conjunction: 0∧x=0. This changed-input test settles inapplicability.',[5,12]),
('Has a person understood or benefited from this view?',[2,1,1,1],'No relevant human observation supplied; unanswered empirical question.',[1,10]),
('Has the historical author’s intended maybe sense been observed?',[2,1,1,1],'No author-context receipt supplies that missing choice; exact current definition is a proxy only.',[2,4]),
('Can the index retain both semantic outcomes and the unresolved scope?',[2,4,5,5],'Yes: paired-semantic-instances plus condition index preserve both explicit cases and null source intent.',[9,12]),
('What is the next ready question, given these answers?',[4,2,5,5],'For the current fixture, missing7 is the discriminator; for source intent no available local observation resolves it.',[13,14,17])]
write('46-qaf-semantic-access.md','Order semantic and applicability questions by their actual prerequisites.','FRQ43 provides a two-condition fixture with one unavailable qualifier; AEX33 supplies two meanings for maybe; SRC30 keeps source attribution separate from semantic trust. The starting temptation is to list all gaps together, but the current action depends on which gap changes the exact requested answer.',q,[1,2,3,4,5],[
'Q1→Q2→Q6: read the exact edge for literal attribution; no inference about its truth is added.',
'Q3/Q4→Q7→Q8→Q9: align P,t, compute positive witness and strict emptiness, leave original sense unknown.',
'Q5→Q11→Q12→Q13: fix2=true, vary7, obtain opposite applicability outputs and select7.',
'Q5→Q14: change2=false, evaluate both7 completions, obtain inapplicability without retrieving7.',
'Q9/Q12→Q17→Q18: retain both scoped results in the index and select only the presently answerable discriminator.'
], 'The next formal-test queue uses two cases separately: current2=true requires7; changed2=false does not. RCA49 receives the source of missing qualification as a retrieval question rather than a blanket claim that every missing clause must be fetched.')
q=[
('What is the current objective of the signal choice?',[5,5,5,5],'AR45 side branch declares worst expected regret over models A/B; original uniform optimum remains separately impossible.',[]),
('What payoffs and price are fixed?',[5,5,5,5],'+6/−4, decline0, price1 from exact timing model; stipulated, not measured human values.',[]),
('Which conditional signal models are admitted?',[5,4,5,5],'For AR45 regret branch exactly A/B; original .8-accuracy family is wider.',[]),
('Which actions are allowed?',[5,4,5,5],'Current regret model allows a mixture of buy and now; no physical random act is requested.',[]),
('What current versus future initiating evidence exists?',[5,4,5,5],'Active tools execute now; saved capsule has no scheduling acknowledgment.',[]),
('What are buy and now values in A/B?',[5,5,5,5],'A: .8/1; B:1.2/1, computed in signal-value-tests.',[2,3]),
('What regret does a buy-probability q incur?',[5,4,5,5],'A:.2q; B:.2(1−q), expected payoff subtraction.',[1,4,6]),
('Which q minimizes the worst regret?',[4,4,5,5],'q=.5, worst=.1 on the declared A/B set.',[3,7]),
('Does this identify which signal model is actual?',[3,4,5,5],'No: optimization uses both models; no new signal measurement occurred.',[3,8]),
('Does a different uncertainty set preserve that minimizer?',[5,2,5,4],'Not assumed; AV50 tests a broader regret function and model-set premise.',[1,3,7]),
('Which source role does the capsule’s mismatched hash identify?',[4,3,5,5],'Origin SPD09 status changed; capsule-current-check shows SP original hash still matches.',[5]),
('Does a changed origin hash prove the next skill changed?',[3,3,5,5],'No: the performed two-role comparison has origin mismatch and next-source match.',[11]),
('Is the exact next input present after restoration?',[4,4,5,5],'Methods v2 includes full frozen input and a specific SP02 operation; v1 was incomplete.',[5,11]),
('Does restored input mean a later session ran?',[3,5,5,5],'No future event receipt exists; restored current bytes are observed.',[5,13]),
('Can expiry invalidate the future recommendation while preserving the saved history?',[4,4,5,5],'Yes under declared opportunity change; historical saved bytes remain an earlier observation.',[2,5,14]),
('Does the user endorse the hypothetical regret objective as a real personal preference?',[2,1,1,1],'No such endorsement is supplied; no need to infer it for this formal inquiry.',[1,4]),
('What can be performed now without the unavailable future/human evidence?',[4,3,5,5],'AV50 can verify the finite model and sensitivity; it cannot observe a future person.',[8,10,12,16]),
('Which missing premise has the highest current selection value?',[5,2,5,5],'Exhaustiveness and objective sensitivity of the regret model are inspectable; future initiation is separately unavailable.',[10,15,17])]
write('47-qaf-timing-objective.md','Separate the next decision-model verification from unrelated future-execution uncertainty.','AR45 produced a .5 mixture for a specifically exhaustive A/B regret model, while the actual capsule has distinct source-role hashes. These are two independent uncertainty sources. A missing future event does not prevent present finite calculations; a valid calculation does not supply that future event.',q,[1,2,3,4,5],[
'Q2/Q3→Q6→Q7→Q8: compute model values, two regret lines and their intersection.',
'Q1/Q3/Q7→Q10: preserve the uncertainty-set sensitivity question for the performed AV50 comparison.',
'Q5→Q11→Q12: inspect actual hashes by role; origin changed, next-skill source did not.',
'Q5/Q11→Q13→Q14→Q15: read repaired payload, preserve unscheduled status and expiry condition.',
'Q8/Q10/Q12/Q16→Q17→Q18: select current formal verification without substituting it for a human preference observation.'
], 'AV50 now verifies the regret assumptions first, while no request for the user’s feelings, future reopening or a scheduling permission is introduced. The exact model case can be completed under its declared scope.')
print('QAF46/47:18 questions each,5 foundation questions and5 performed resolution paths.')
