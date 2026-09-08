from write_records import save,BASE
from statistics import NormalDist
import math,json,itertools
N=NormalDist();h=abs(2*(math.asin(math.sqrt(.7))-math.asin(math.sqrt(.6))));z=N.inv_cdf(.975)
def power(n):
 delta=h*math.sqrt(n/2);return 1-N.cdf(z-delta)+N.cdf(-z-delta)
lo,hi=1,10000
while hi-lo>1:
 m=(lo+hi)//2
 if power(m)>=.8:hi=m
 else:lo=m
(BASE/'power-calculation.json').write_text(json.dumps({'hypothetical_baseline':.6,'hypothetical_treatment':.7,'alpha':.05,'power_target':.8,'effectsize_arcsine':h,'required_per_group':hi,'achieved_power':power(hi),'previous_n_power':power(hi-1),'method':'two-sided normal approximation on arcsine effect; no observed rate data'},indent=2))
save('142-abts-1','abts','Design a human retrieval comparison with an honest sample boundary','Change whether a local replay can justify saying a new organization helps readers.','The decision index works in local exact lookups. I do not have independent reader evidence that it improves retrieval accuracy or time.',
 f'''Observation: the systems line can resolve known decision keys, but the assistant created both the index and its queries. Hypothesis: for eligible independent readers, adding a decision-key entry point to unchanged content increases accurate scope-preserving retrieval from a planning value .60 to .70. Those rates and the ten-percentage-point minimum effect are hypothetical design inputs; no baseline rate has been observed. Null: no difference in population retrieval accuracy. Two-sided test allows harm to be detected.

Control A: same complete source records in chronological order. Treatment B: the same records plus a decision-key index. Only navigation differs; content, questions and available time remain equal. Unit of randomization and analysis is reader, not individual question, because repeated questions share a person. Eligible readers must not have seen this corpus; people who wrote it are excluded. No participants are recruited or messages sent in this assignment.

Primary metric: each reader's correctness on one preselected held-out retrieval-and-boundary case, coded against a fixed answer key by a blinded scorer. Secondary: retrieval time and subjective ease. Guardrail: false broad-transfer assertions must not rise; missing a material scope exception invalidates an otherwise correct title lookup. Treatment label can be hidden from the scorer; participants necessarily see navigation format, so full participant blinding is impossible.

Sample calculation: a normal approximation uses arcsine effect h={h:.9f}; alpha .05, power .80, equal groups. The executed calculation gives {hi} readers per group. Formula and power semantics are documented by [statsmodels effect size](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_effectsize.html) and [power solver](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.NormalIndPower.solve_power.html). The local implementation uses the standard normal CDF and checks that n={hi-1} falls below target while n={hi} reaches it. Real baseline, clustering and attrition can alter the requirement.

Traffic is unknown, so a runtime cannot honestly be computed. The planned minimum is full weekly blocks after recruitment begins, with a fixed end defined before outcomes are inspected. No calendar experiment has been scheduled. Sample-ratio mismatch is checked against the assignment list; dropout is retained as missingness with sensitivity bounds. Novelty, practice, disclosure between readers, source familiarity and question difficulty are documented threats. No early stopping on significance and no mid-flight primary-metric change.

Decision rule predeclared: positive significant effect at alpha .05, at least the practical ten-point effect, and guardrail satisfied→candidate adoption; negative significant effect or guardrail failure→retain control; nonsignificance→inconclusive, not no effect. Root/user is the eventual decision owner. `power-calculation.json` preserves design inputs, and no nonexistent results are reported.''',
'The local index result is now separated from the unperformed reader comparison; its sample and decision conditions are explicit.','The design is concrete, but human retrieval benefit remains untested and actual eligible traffic is unknown.','UNRESOLVED','Control/treatment and outcome contracts preserve the causal question; a success anecdote does not.','Measure baseline without changing criteria; recruit only with authorization; pilot the answer key for ambiguous cases.')
save('100-exd-1','exd','Separate a representation effect from a content effect','Change the planned experiment so it isolates what the representation contributes.','A graph-plus-extra-explanation treatment would plausibly help some tasks, but any difference could come from additional information rather than the graph.',
 f'''H1: holding propositions and relation edges fixed, relational display changes correct dependency inference on a new six-node task by at least ten percentage points. H0: no difference. The direction is not forced; a graph can confuse a simple chronological question. The mechanism is visibility of the same relations, not added factual content.

IV1 is display (prose adjacency versus graph). IV2 is query type (dependency versus chronological order). DV is a correct answer with required scope boundary, one primary scored query per participant. Controls: same nodes, same edges, same words, same time budget. Moderator is prior graph familiarity, measured before allocation; mediation by gaze or subjective clarity is not claimed without measurement.

Design is a 2×2 factorial with between-person display assignment and preassigned query type. Four groups avoid carryover from seeing both formats. A within-person crossover would need counterbalancing and still risk teaching the relation; it is rejected for the confirmatory trial. Randomization is blocked by graph familiarity; the sequence is produced before assignment and concealed from the enrolling person. Blinded scoring uses a fixed answer key; participant display blindness is impossible. An active information-equivalent control is used, not an empty page.

Sample planning for a two-arm primary contrast uses the same hypothetical .60→.70 rate, alpha .05 and .80 power, yielding {hi} per compared arm under the normal approximation. A four-cell interaction requires a separate interaction power model; borrowing the two-arm N for that claim is not allowed. Attrition and clustering are unknown. The confirmatory target is therefore the prespecified dependency contrast; the interaction is exploratory until powered.

Validity: history/maturation balanced by concurrent randomization; testing carryover avoided; instrument held fixed; selection controlled by assignment; dropout kept visible; diffusion recorded; population generalization limited to recruited readers; ecological validity requires later real tasks; temporal durability untested; construct validity guarded by equal information and boundary scoring; multiple tests labeled secondary/exploratory; missing outcomes receive best/worst sensitivity bounds rather than disappearance.

Analysis plan is written before human data: two-proportion comparison with interval for the primary contrast, alpha .05; report raw group rates and practical effect; no primary switch after observing results. Interaction analysis is explicitly exploratory. No public preregistration is posted and no participants are recruited here.

Actual transformation now: the treatment's extra explanation is removed from the design; both variants contain exactly the five relations A→D,B→D,C→D,D→E,E→F. The controlled objects are constructed as matching edge lists. Thus a future difference is no longer intentionally confounded by added edges. This is a design correction, not demonstrated human benefit.''',
'The experimental treatment now differs only in representation; the confirmatory contrast excludes an unpowered interaction claim.','The concrete stimulus specification removes an identified information-content confound. The intended human effect remains untested.','KEEP','A factorial variable table with an information-equivalent control retains the competing causal account; a treatment/control label alone would hide it.','Validate the held-out key; estimate baseline rates; examine whether the same result survives a real task.')
save('100-exd-2','exd','Design a test for criterion change itself','Change whether a post-intervention choice is evidence of better reasoning or merely a changed objective.','A later improved task score can look like success. If the intervention also changes the scoring criterion, the two explanations are entangled.',
'''H1: exposing a concrete countercase changes the criterion version explicitly chosen by a participant and improves coherence of the resulting choice under that participant's stated criterion. H0: no change in explicit criterion choice or coherence. Two outcomes are distinct; a criterion shift is not automatically an improvement.

IV is countercase exposure versus an equal-length relevant neutral case. DVs: declared criterion version before/after, and correctness of applying that declared criterion to an unseen option set. The intervention cannot be said to improve the original objective merely because the participant adopts a different one. Control variables are option data, presentation time and response opportunity. Moderator is initial criterion strength; mediator such as felt surprise is exploratory and unmeasured unless collected.

Design options: post-only groups cannot distinguish preexisting criteria; simple pre/post cannot separate natural revision; pre/post randomized active-control groups are selected. The pretest itself can influence criteria, so a Solomon-style no-pretest extension is a distinct future design, not silently assumed equivalent. Randomization occurs by participant and scoring is blinded to exposure; the person knows the material they saw.

Power: criterion shift rate is unknown and cannot inherit the .60 baseline from a retrieval task. A pilot can estimate dispersion, but confirmatory sample size remains unresolved until a smallest meaningful shift/coherence criterion is justified. The calculation in the other experiment is not imported as applicable evidence. No fabricated N or participant results are inserted.

Validity checks: history, maturation, regression to mean, selection, attrition and instrument change remain recorded; preference shift and procedural compliance are separate constructs; demand characteristics are addressed by a neutral framing and blinded scorer; apparent agreement with the experimenter is not coded as benefit. Generalization requires additional settings and time. Primary analysis compares each participant's choice with their recorded criterion version, then compares randomized groups; any after-the-fact recoding is labeled exploratory. Missing reports leave criterion version unknown.

Actual local control example: v1 fidelity .8 favors A (4.4 versus3.4); v2 fidelity .3 favors B (2.9 versus4.4). A post-only B choice is compatible with correct v2 application, incorrect v1 application, or unrecorded criterion change. The new design records both version and choice, so those cases are no longer collapsed into one outcome. Real improvement of anyone's values remains unresolved.''',
'The design now treats criterion version and correct criterion application as separate observed variables.','The constructed A/B example reveals an actual ambiguity the revised design can discriminate; a powered human causal result remains unavailable.','UNRESOLVED','Two linked outcome records preserve a change of objective; a single task score does not.','Define a noncoercive criterion-shift outcome; obtain pilot variance; test a person who keeps the original criterion for good reasons.')
# EMV validates a transformed recurrence formula across finite cases with multiple mathematical checks.
pre=[{'id':f'P{i+1}','confidence':c,'prediction':p} for i,(c,p) in enumerate([(90,'A cheaper for n=1'),(90,'tie at n=6'),(90,'B cheaper for n=7'),(80,'expiry at5 prevents B crossover'),(90,'setup0 makes B cheaper for positive n')])]
(BASE/'emv-predictions-before.json').write_text(json.dumps(pre,indent=2))
cases=[(6,2,1,n,None) for n in [0,1,5,6,7,10]]+[(6,2,1,10,5),(0,2,1,1,None),(6,1,1,10,None),(6,1,2,10,None),(6,2,1,6,6),(6,2,1,7,6)]
results=[]
for setup,a,b,n,expiry in cases:
 valid=expiry is None or n<=expiry
 ca=a*n;cb=setup+b*n
 results.append({'setup':setup,'a_per':a,'b_per':b,'n':n,'expiry':expiry,'A':ca,'B':cb,'B_valid':valid,'preferred':'A' if not valid or ca<cb else 'B' if cb<ca else 'tie'})
checks={
'direct_arithmetic':results[1]['A']==2 and results[1]['B']==7,
'algebra_crossover':results[3]['A']==results[3]['B'],
'independent_sum_implementation':all(x['A']==sum([x['a_per']]*x['n']) and x['B']==x['setup']+sum([x['b_per']]*x['n']) for x in results),
'metamorphic_increment':results[5]['B']-results[4]['B']==3,
'expiry_separate_from_cost':results[6]['B']<results[6]['A'] and not results[6]['B_valid']}
outcomes=[results[1]['preferred']=='A',results[3]['preferred']=='tie',results[4]['preferred']=='B',results[6]['preferred']=='A',results[7]['preferred']=='B']
cal=[dict(p,outcome=bool(o),status='CONFIRMED' if o else 'DISCONFIRMED') for p,o in zip(pre,outcomes)]
(BASE/'emv-validation.json').write_text(json.dumps({'tests':results,'independent_checks':checks,'edge_cases':['zero recurrence','zero setup','equal per-use costs','prepared option more expensive per use','expiry before crossover','expiry at crossover'],'calibrations':cal},indent=2))
save('143-emv-1','emv','Validate an option trigger before using it as a reusable rule','Change confidence in the prepared-route crossover by checking both arithmetic and validity.','The n>6 crossover is algebraically plausible. I have not yet run its edge cases or verified that validity expiration remains distinct from numerical cheapness.',
 f'''Plan: retain prepared route B when it becomes cheaper within its valid lifetime. Prediction if correct: A costs2n, B costs6+n, tie at6, B cheaper after6 only while valid. Failure would be an arithmetic mismatch, a false crossover or acceptance after expiry. Crux is whether the same trigger handles zero/equal-cost and expiry boundaries.

Minimum viable test uses twelve finite parameter cases; resource is local arithmetic, action reversible, test cheaper than committing an unsupported reusable rule. Test-first is selected. The pretest predictions and five confidence declarations were saved in `emv-predictions-before.json` before this suite; they express working expectations, not calibrated probabilities.

{table if False else ''}
Twelve tests are in `emv-validation.json`: recurrence0,1,5,6,7,10; expiry5 at n10; setup0; equal per-use costs; B higher per-use; expiry exactly6; and n7 beyond expiry6. Six edge categories are explicitly retained. Five checks use distinct mathematical routes: direct arithmetic, algebraic crossover, repeated-addition implementation, metamorphic increment and separate eligibility predicate. They are computationally independent checks of representation, not independent human replications.

Five calibration outcomes: {json.dumps(cal)}. All five declared predictions are confirmed in the defined cases. Five confirmations cannot establish that a 90% or80% confidence level is calibrated across future claims; this batch is too small and selected. The result is preserved without inflating general confidence.

Post-validation update: numerical cheapness and input validity remain separate. A prepared option can cost16 against A20 at n10 and still be ineligible because validity expired after5. Equal per-use costs never repay positive setup. Zero setup changes the strict threshold. The reusable formula is now `n(a−b)>setup` AND lifetime valid, with equality treated as a tie.

Actual use: the earlier B trigger is refined by the general cost-difference condition and explicit validity conjunction. The specific n>6 result is retained as one parameter case, not erased. External recurring behavior has not been observed.''',
'The reusable option trigger now handles arbitrary per-use differences and validity separately, while retaining the n>6 special case.','Twelve executed cases and five distinct checks support the exact algebra/eligibility transformation. They do not establish actual future demand or human benefit.','KEEP','Parameter table plus separate validity state exposes cases that a single crossover number hides.','Add stochastic reuse counts; inspect setup renewal; observe an actual matching recurrence.',depth='Original 8x floors: 12 validation tests executed, 5 distinct independent mathematical checks, 6 edge cases tested, 5 predeclared confidence calibrations compared with outcomes.')
