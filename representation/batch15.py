from write_record import record, progress, ROOT
import json,itertools

dims=['Pattern recognition','Signal detection','Perspective-taking','Deductive reasoning','Inductive reasoning','Abductive reasoning','Analogical reasoning','Causal reasoning','Knowledge capture','Knowledge retrieval','Knowledge transfer','Knowledge pruning','Divergent thinking','Convergent thinking','Recombination','Imagination','Evaluation','Prioritization','Risk assessment','Trade-off analysis','Self-monitoring','Bias detection','Calibration','Strategy selection','Empathy','Motivation modeling','Communication design','Collaboration','Emotion recognition','Emotion regulation','Emotional intelligence','Stress management']
def coverage(rows):
 assert len(rows)==32
 count={s:sum(a[0]==s for a in rows) for s in ['STRONG','PARTIAL','ABSENT']}
 return '\n'.join(f'| {d} | {s} | {e} | {f} |' for d,(s,e,f) in zip(dims,rows)),count
r1=[('STRONG','Three relation patterns explicitly distinguished','high'),('PARTIAL','Relation label present; mixed-node omissions not tested','high'),('PARTIAL','Serial and graph views; no external reader response','medium'),('STRONG','Finite operator compilation checked','high'),('ABSENT','No inference to untested graph populations','low'),('PARTIAL','Several meanings for one topology named; mixed interpretations not diagnosed','high'),('STRONG','Five explicit structural transfers','medium'),('ABSENT','No causal effect estimation','low'),('STRONG','Typed records and exact outputs retained','high'),('STRONG','Records keyed by relation type','high'),('PARTIAL','Single-operator transfers; nested transfer absent','high'),('PARTIAL','Invalid generic traversal rejected; no stale-model review','medium'),('STRONG','Set, typed record and visible branch alternatives','medium'),('STRONG','Representation chosen by use','high'),('PARTIAL','Operators not yet composed in one graph','high'),('PARTIAL','Candidate mixed graphs only proposed','medium'),('STRONG','Exact required/order outputs checked','high'),('PARTIAL','Top analogies ranked; mixed-case probes not prioritized','medium'),('PARTIAL','Causality/probability overreading named; mixed-operator loss untested','high'),('STRONG','Serial exactness versus projection retained','medium'),('STRONG','Unsupported relation defaults rejected','high'),('PARTIAL','Topology-to-order error tested; broader bias unknown','medium'),('PARTIAL','Scope qualified; no confidence-frequency calibration','medium'),('STRONG','Relation-specific operation selected','high'),('ABSENT','No emotion inference from diagram use','low'),('ABSENT','No model of a person’s reasons','low'),('PARTIAL','Projected/serial forms available; readers untested','medium'),('PARTIAL','Root reviewed layout, not mixed-operator semantics','medium'),('ABSENT','No emotion report','low'),('ABSENT','No regulation intervention','low'),('ABSENT','No use of emotions as evidence','low'),('ABSENT','No pressure task','low')]
t1,c1=coverage(r1)
def leaf(a):return {'leaf':a}
def node(op,*members):return {'relation':op,'members':list(members)}
def evaluate(x):
 if 'leaf' in x:return [(frozenset([x['leaf']]),frozenset())]
 op=x['relation'];child=[evaluate(c) for c in x['members']]
 if op=='one_of':return [p for options in child for p in options]
 out=[]
 for combo in itertools.product(*child):
  members=frozenset().union(*(p[0] for p in combo));edges=frozenset().union(*(p[1] for p in combo))
  if op=='sequence':edges=edges|frozenset((a,b) for i,p in enumerate(combo) for q in combo[i+1:] for a in p[0] for b in q[0])
  out.append((members,edges))
 return out
mixed=[]
for outer,inner in itertools.product(['all_of','one_of','sequence'],repeat=2):
 tree=node(outer,node(inner,leaf('A'),leaf('B')),leaf('C'))
 mixed.append({'outer':outer,'inner':inner,'tree':tree,'plans':[{'members':sorted(p[0]),'before':sorted(list(p[1]))} for p in evaluate(tree)]})
assert len(mixed)==9
(ROOT/'mixed-relation-tests.json').write_text(json.dumps(mixed,indent=2))
record(41,'ctcov',2,'Mixed operators need a composition test, not another single-relation example',
'Assess the typed relation toolkit and add the missing composition operation needed to preserve a nested alternative inside a required or ordered group.',
'The relation model has six successful single-operator fixtures. It handles alternatives, requirements and sequences separately, but its transfer evidence does not yet cover a graph that contains more than one operator.',
'''System: the typed relation model and its serial/visual representations from 039. Purpose: preserve the relation between members when converting a representation into possible plans. User: this model maintaining exact finite examples. Coverage ratings below concern implemented components and local executed checks; they do not rate a person's cognitive capacities. Frequency is a task-based priority judgment, not measured user incidence.

All 32 original sub-dimensions were assessed:

| Dimension | Coverage | Evidence / missing component | Need in this task |
|---|---|---|---|
'''+t1+f'''

Initial distribution: {c1['STRONG']}/32 STRONG ({c1['STRONG']/32*100:.2f}%), {c1['PARTIAL']}/32 PARTIAL ({c1['PARTIAL']/32*100:.2f}%), {c1['ABSENT']}/32 ABSENT ({c1['ABSENT']/32*100:.2f}%). Deductive checks, capture and selection are strong. Emotional processing is absent; it is not necessary for the declared exact-operator task and is not added merely to improve a percentage.

The complete absent list and partial list are the corresponding rows above. Priority gaps are recombination/transfer (high: nesting can change which actions are required), signal detection/abductive diagnosis (high: an unlabeled inner branch can be mistaken for its parent's operator), and risk assessment (high: flattening can erase an order constraint). Secondary gaps include pruning, external-reader perspective and confidence calibration; no numerical human outcome data exists to calibrate.

Recommended additions: (1) extend the existing evaluator recursively, small local implementation; (2) construct all nine two-level combinations of the three operators, medium finite coverage; (3) retain a normalized plan showing both member set and before-relations, small output addition. These extend the existing model rather than creating an unrelated toolkit. No empathy or stress module is claimed necessary for evaluating a finite tree.

Actual extension and all nine tests are retained in [mixed-relation-tests.json](mixed-relation-tests.json). Each outer operator takes an inner A/B group and a C leaf. The evaluator returns possible member sets and explicit before-relations. `all_of` combines required members without inventing an order; `one_of` collects alternatives; `sequence` also adds all cross-group before-relations while preserving internal ones.

Three separating outputs:

- `all_of(one_of(A,B), C)` → {{{{A,C}}, {{B,C}}}}, with no before-relations. C is required in every plan; A and B are alternatives.
- `one_of(all_of(A,B), C)` → {{{{A,B}}, {{C}}}}, with no before-relations. C is now an alternative to the A/B group.
- `sequence(one_of(A,B), C)` → {{A before C, B before C}} as two possible plans. It does not require A before B or B before A.

Actual loss test: flattening all leaves into an unordered {{{{A,B,C}}}} incorrectly requires both A and B in the first case and erases the before-condition in the third. Flattening into a generic alternative set {{{{A}},{{B}},{{C}}}} drops the required C in the first case. The recursive typed form rejects both equivalences. A fully labeled mixed diagram is a strong alternative for spatial inspection, but a serial preorder must retain each group's boundaries and operator to have the same meaning.

Later use: the new evaluator processes `sequence(all_of(A,B),C)` and retains A before C and B before C while leaving A/B unordered. The next draft can now distinguish “both before C” from the stronger unsupported “A then B then C.” This is a new substantive relation output beyond the earlier single-operator model.

Updated local coverage: recombination and transfer for the declared two-level finite family become STRONG, while real-reader, causal, global calibration and emotional dimensions remain as rated. The update is not a claim that all deeper graphs have been tested. Strongest area remains finite deduction; the three actual additions are recursive composition, nine fixtures and normalized before-relations.

Certificate: exact normalized plans distinguish the two nestings and the ordered version. The useful change is preserving group scope and partial order during a real nested conversion. Contrary: a knowledgeable reader can already interpret a fully labeled diagram; the new evidence is machine-model composition and its failure cases, not proof of better human understanding.''',
'I extended the representation model to nested operators, executed nine combinations, and retained a partial order that a flat sequence would overstate.',
'The local conversion now preserves required alternatives, group scope and ordering conditions under the tested two-level compositions.',
'KEEP — new composition capability and explicit lost-condition tests.',
'Normalized member sets plus before-relations serve exact checking; the typed tree retains grouping provenance; a labeled diagram remains the visual inspection route.',
'Test three nested levels with shared members; check inconsistent before-cycles; ask a reader to reconstruct the typed tree from the serial form.',
'All six original steps and all 32 prescribed sub-dimensions executed; every partial/absent row grounded, priorities scoped, three concrete additions implemented and nine nested combinations tested. Original has no numeric 8x floor.')

r2=[('PARTIAL','Repeated vectors make patterns available; no learner response','high'),('PARTIAL','Each question isolates one proposition; attention unobserved','high'),('PARTIAL','Reader may choose paced route; actual preferences unknown','high'),('STRONG','Exact finite answer key supplied','high'),('PARTIAL','New vocabulary transfer proposed, no learner generalization observed','medium'),('PARTIAL','Wrong-answer alternatives planned, no diagnosis observed','high'),('ABSENT','No analogy required for this lesson','low'),('ABSENT','No causal attention-effect inference','high'),('PARTIAL','Optional learner answer sheet exists in design','medium'),('PARTIAL','Later cue proposed, delayed retrieval untested','high'),('PARTIAL','Transfer prompt included, no participant','high'),('ABSENT','No existing learner knowledge record to prune','low'),('PARTIAL','Two pace routes offered','medium'),('PARTIAL','Learner choice proposed, not observed','high'),('PARTIAL','Cases and pacing combined without usage evidence','medium'),('PARTIAL','Anticipated encounters explicitly hypothetical','medium'),('STRONG','Finite answer correctness can be checked','high'),('PARTIAL','Most discriminating question first by model judgment','medium'),('PARTIAL','Burden/pressure risks identified, actual experience unknown','high'),('PARTIAL','Fixed pause versus self-paced trade-off stated','high'),('PARTIAL','Optional confidence response before answer','medium'),('PARTIAL','Unknown-as-zero error probed, no learner evidence','high'),('PARTIAL','Confidence/accuracy comparison designed, unperformed','high'),('PARTIAL','Learner may select another route, unused','medium'),('ABSENT','No emotional state inferred','medium'),('PARTIAL','Reason for participation to be asked, not assumed','high'),('STRONG','Exact scripts and accessible serial alternative provided','high'),('PARTIAL','Facilitator/reader roles defined, no session','medium'),('ABSENT','No actual feeling report','low'),('ABSENT','No regulation treatment claimed','low'),('ABSENT','No emotional evidence supplied','low'),('PARTIAL','Stop and self-paced routes available on paper','medium')]
t2,c2=coverage(r2)
script='The first result is zero. The second result is unknown. Is every result positive? Is some result positive? The possible completions are zero zero and zero one. Every is false in both. Some differs between them.'
(ROOT/'pace-trial-script.txt').write_text('Intended mind change: Let a prospective reader distinguish a settled universal from an unresolved existential in [0,?].\n\nCommon words in both proposed routes:\n'+script+'\n\nRoute A: a fixed five-second pause after each of the two questions; all words stay the same.\nRoute B: the reader advances after each question; all words stay the same, and stopping is available.\n\nActual mind change: The model constructed equivalent-content pace routes and their answer key; no human session occurred.\nBenefit: Experimental content is specified; effects on attention, learning and pressure are untested.\nVerdict: UNRESOLVED.\nOrganization: Shared script, separate timing rule, optional answer and confidence record.\nNext attempts: Actual voluntary use, same-content comparison, and delayed transfer.\n')
record(42,'ctcov',3,'A pacing design can cover reasoning on paper while leaving attention effects unknown',
'Assess a proposed paced reading activity and supply missing learner-choice and evaluation components without counting their design as an observed human change.',
'The logical exercise has a correct finite answer key. A pause might give a reader more time, but no participant has used the activity, and a fixed pause can also impose unnecessary waiting.',
'''System: a proposed short activity about [0,?], using the exact common script in [pace-trial-script.txt](pace-trial-script.txt). Purpose: help a willing reader distinguish a settled universal from an unresolved existential. Users: prospective reader and facilitator; neither role has been instantiated in a session. Ratings describe design coverage only. Need-frequency labels are design judgments conditional on this activity, not observed frequencies.

| Dimension | Design coverage | Present component / missing evidence | Need |
|---|---|---|---|
'''+t2+f'''

Distribution: {c2['STRONG']}/32 STRONG ({c2['STRONG']/32*100:.2f}%), {c2['PARTIAL']}/32 PARTIAL ({c2['PARTIAL']/32*100:.2f}%), {c2['ABSENT']}/32 ABSENT ({c2['ABSENT']/32*100:.2f}%). Strongest design area is exact deduction/evaluation and explicit communication material. Weakest observed-evidence area is all human outcomes, including those with strong material coverage. The distinction prevents a correct answer key from being mistaken for demonstrated learning.

All absent and partial dimensions appear in the table. Priority gaps: signal detection/attention (high for the intended purpose; no actual response), transfer/retrieval (high if learning should persist; no delayed encounter), calibration (high if confidence is collected; no paired accuracy yet), and motivation/choice (high because a compulsory wait can be the wrong format). Causal attribution is absent and high priority for a causal claim, but that claim is excluded from the present construction result. Emotional categories remain unmeasured; adding speculative emotion labels would not fill them.

Three specific additions were constructed. First, retain one common verbal script and separate the timing rule: Route A gives a fixed five-second pause after each question; Route B lets the reader advance, including stop. Second, add an optional answer record with fields proposition, answer, confidence-if-offered and reason. Third, add a different-vocabulary transfer prompt: “One inspected lamp is off and another is uninspected: are all lamps on; is at least one on?” These are proposed components, not reports of their use.

The exact common script is: “The first result is zero. The second result is unknown. Is every result positive? Is some result positive? The possible completions are zero zero and zero one. Every is false in both. Some differs between them.” The two routes retain identical words. Timing and choice burden differ; this is not a pure manipulation of pause duration if self-pacing also changes agency. That limitation travels with the comparison.

Concrete content checks were performed by the model: the answer key every=false, some=unresolved follows from [0,0]/[0,1]; the lamp transfer has the same truth pattern under its two-member domain; removing the word “uninspected” would lose the missingness condition and is rejected. The activity explicitly defines zero as not positive; it does not call a person's answer zero or negative. The answer sheet allows no response, avoiding a fabricated failure score for an unperformed task.

Strong alternatives: a self-paced text reference avoids imposed delay and remains reviewable; a fixed narrated version can supply a consistent temporal sequence for a comparison. Neither is declared better without actual use. The current recommendation is to keep both candidate routes until a real participant's context supplies a preference, then collect the exact answer/transfer evidence that the claim requires. No invitation or external session was sent or scheduled.

Organization review: common words in one source prevent accidental content drift across pacing variants. Timing instructions stay separate; outcome records stay empty. The proposed pause is not hidden inside a rewrite, and the reader's stop route remains visible. A design coverage score is not added to the model's demonstrated-benefit aggregate as if it measured human change.

Certificate: the constructed activity has a valid answer key and equivalent verbal content across its two pace rules. The causal claim that pauses improve attention is untested; the self-paced alternative exposes a concrete burden trade-off. The intended human after-state therefore remains unresolved.''',
'I constructed and checked two equal-content pace routes, a response record and a transfer prompt; no person used them.',
'The proposed comparison is concrete and preserves its content and agency differences. Attention, motivation, learning and delayed transfer remain unobserved.',
'UNRESOLVED — human after-state and comparative pace benefit are untested.',
'One shared script, two explicit timing/choice rules, an empty response record and a separate transfer prompt. Designed coverage and observed outcomes stay distinct.',
'Use the activity with a willing reader; compare the selected route against their ordinary reading; test delayed transfer without re-presenting the original answer.',
'All six original steps and all 32 sub-dimensions assessed, absent/partial gaps fully grounded, task-conditional priorities, three concrete design additions and finite content/loss checks. Original has no numeric 8x floor; no human coverage or effect is inferred from construction.')
record(43,'sum',1,'Repeated boundaries across related records are not independent confirmations',
'Synthesize four related representation records while preserving their distinct useful outputs and the shared premises that limit any claim of convergence.',
'Actor routing, eligibility, partial observation and relation typing appear to support a broad pattern: keep distinctions explicit before acting. All four were produced in the same instructed local research context, so agreement alone cannot establish independent confirmation.',
'''Interpretation: synthesize. The need is a combined picture across four sources, not compressing one record or reporting project status.

| Source | Four key points extracted |
|---|---|
| 001 orgn | Actor/evidence routing; model design does not establish human effect; hashes supply provenance; root owns integration/saving. |
| 015 omtx | Eligibility differs from observation; observed-but-ineligible history remains; unknown eligibility leaves membership unresolved; unobserved is not unsuccessful. |
| 033 txm | Partial evidence differs from none; decisive evidence alone carries the binary outcome; old yes/null records need review; one prefix has two possible decisive continuations. |
| 039 cda | Same topology can encode alternatives/requirements/order; typed operators constrain compilation; domain analogies have explicit limits; branch count supplies no probabilities. |

Source independence check: all four share the user instruction, current model, local archive and prior selector. Later records read earlier findings. They are not independent studies or blind replications. Convergence on human-effect limits is partly an echo of the shared instruction. The distinct finite artifacts/tests provide evidence for their own scoped outputs; they do not multiply the confidence of a broad psychological thesis simply because they appear in four documents.

Convergence across at least three sources: source/effect scope must stay explicit, and an incomplete or differently scoped input cannot be silently upgraded to an outcome. Independence: shared premises and sequential uptake, so no independent-convergence credit. Some sources agree more narrowly: 015/033 distinguish current classification from retained raw evidence; 001/039 separate a represented possibility from authority to perform an action. The other sources do not independently test each of those narrower claims.

Divergences are functional, not necessarily contradictions. 001 routes by actor/evidence class; 015 starts with domain membership; 033 asks how much relevant evidence was captured; 039 asks what relation connects members. If all are forced into a single status ladder, an event can no longer be both excluded from an aggregate and decisively observed, or both partially known and linked to two possible completions. The sources support retaining orthogonal questions, not choosing one universal starting label.

Unique useful outputs: 001 assigns real coordination responsibilities; 015 preserves an observed excluded event; 033 provides a migration rule for ambiguous old null records; 039 compiles relation-specific operations. Each matters within its stated object. None is a substitute for the other three.

Combined picture: the four records keep actor, domain membership, evidence completeness and relation meaning available to the operation that uses them. Their local checks show different losses when a field is removed. Their shared provenance prevents treating the repeated caution as independent proof of a universal method.

Strongest local evidence comes from the exact separating cases: observed-but-ineligible, one captured value with two decisive continuations, and one_of versus sequence on the same members. The most repeated wording is the human-effect limitation, but repetition is not the strongest evidence. Open conflict: which question should be the entry point for a particular encounter; the source records supply different useful routes. Missing from all four: actual human transfer, delayed independent retrieval and comparative causal outcome data.

Actual use: a new object has actor=model, currently excluded domain membership, partial text extraction and a one_of completion relation. The synthesis keeps all four fields. It does not turn the object into “failed” or compile its alternatives into a sequence. That result applies already-established checks; no new independent KEEP is earned by recombining their names.

Strong alternative organization: retain the four-source table for source comparison. For immediate action, the unresolved-input route in consolidation 06 is already more direct. The synthesis does not replace it with a mandatory four-step checklist. An executive sentence “all four sources confirm explicit distinctions improve thinking” is rejected: it erases both dependence and the finite object-specific scope.

Certificate: the sixteen extracted points and dependence map support a faithful combined picture. The sources' separate truth-condition checks remain available, while an unjustified evidence-count upgrade is declined. Preserving that limit is prior program practice; the summary's new wording is not a new demonstrated benefit.''',
'I produced the four-source synthesis and declined to treat repeated shared-context boundaries as independent confirmation.',
'The combined record preserves unique outputs and dependence, but its useful guardrails repeat established practice rather than add a new independent result.',
'REJECT — no additional KEEP from summarizing correlated findings.',
'Source comparison table for synthesis; existing unresolved-input route for action; exact source records for the finite tests.',
'Compare an independently produced case without shared premises; test a source that disagrees on the same object; synthesize a genuinely different evidence channel.',
'All synthesis operations executed: four-source inventory, sixteen key points, explicit dependence check, convergences/divergences/unique outputs, combined picture, gaps and actual reuse. The original depth table has no 8x row; expanded scope is reported without inventing an 8x certification.')
progress()
