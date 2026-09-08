from write_support import *
ids=[x['id'] for x in json.loads((D/'allocation.json').read_text())]
def make(n,goal,state,raw,run,inter,after):
 scores={}
 for line in raw.splitlines():
  sk,cl,u,c,r,t,why=line.split('|');scores[sk]=[cl,u,c,r,t,why]
 assert set(scores)==set(ids)
 rows=[[sk]+scores[sk] for sk in ids]
 body=f'GOAL: {goal}\n\nGOAL TYPE: exploration and achievement. GOAL CLARITY: clear. CURRENT STATE: {state} URGENCY: ready to act. CONSTRAINTS: preserve exact supplied inputs, original depth and model-only observation scope.\n\nAll twenty-five assigned method skills are candidates, covering direct action, preparation, validation, risk and recovery. Scores are qualitative present-task judgments, not measurements or global superiority. The final column states the present fact driving upside, cost, risk and timing.\n\n'+table(['Candidate','ROI','Upside','Cost','Risk','Timing','Concrete rationale'],rows)+'\n\nRUN_NOW (four or fewer): '+run+'\n\nInteractions:\n\n'+ '\n'.join(f'{i+1}. {x}' for i,x in enumerate(inter))+'\n\nNegative-now candidates remain required portfolio exposures on appropriate inputs; they are not removed. The conditions in their rationale indicate when they become useful: an actual procedure, unresolved method, verdict to audit, calibration ratings, or an explicit selection task must exist.\n\nActual later application: '+after
 record(f'given-{n:02}',goal,'I can identify a strong direct next operation from the concrete input; the full ranking must add something beyond that ordinary choice.',body,'The ranked output identifies the direct next operation and recovery conditions, but the ordinary task reading already favored that same class of operation.','The ranking is executed for the required diverse exposure. It supplies no demonstrated extra local benefit over the direct choice; no second benefit credit is earned from downstream artifacts.','REJECT','A short current slice is usable; the full twenty-five-row comparison is retained for original-depth fidelity and audit. Repeating it before every small task would add unjustified overhead.','Execute the selected concrete operation; test its boundary; reserve later ranking for a genuine state change.',depth='Original 8x floors: twenty-five candidates/scored, at least six negative-now entries, ten interactions. Each candidate has all four qualitative score dimensions and a specific rationale.')
raw2='''sp|NEGATIVE|Low|Medium|High|Wrong time|The comparison input is exact; another prompt rewrite postpones inspecting dependencies.
given|NEGATIVE|Low|High|High|Wrong time|A full ranking repeats the already clear need to compare actual order.
wsib|MEDIUM|Medium|Medium|Low|Right time|A one-skill choice can state a fallback, but MD is already a close fit.
mrc|LOW|Low|Low|Low|Early|The goal is fixed; a metagoal loop adds little until progress stalls.
mtcg|MEDIUM|Medium|Medium|Low|Right time|Can switch from word differences to dependency inspection if evidence warrants.
pbtc|NEGATIVE|Low|High|High|Wrong time|No conclusion has yet been presented to audit for backward reasoning.
unx|MEDIUM|Medium|Medium|Medium|Early|A surprising representation is useful only if direct comparison leaves a gap.
foht|MEDIUM|High|High|Medium|Right time|Tests a full method space, but the six-action dependency task is small.
svs|MEDIUM|High|Medium|Low|Right time|Can vary a diff display after the relevant relation is identified.
crtv|NEGATIVE|Low|High|High|Wrong time|Inventing instruction variants before preserving required order changes the object under review.
gg|NEGATIVE|Low|High|High|Wrong time|A 200-plus search on an exact six-action comparison creates irrelevant possibilities now.
md|HIGH|High|Low|Low|Right time|Derives word versus order versus dependency method from the actual task.
pcd|MEDIUM|Medium|Medium|Low|Early|Needed only if no existing operation checks the dependency signature.
pci|NEGATIVE|Low|Medium|High|Wrong time|No procedure schema defect is the current blocker.
pv|HIGH|High|Medium|Low|Right time|Validates the concrete revised action order once represented.
satr|NEGATIVE|Low|Medium|High|Wrong time|Pruning apparently similar actions could erase their distinct prerequisites.
iterate|MEDIUM|Medium|High|Medium|Early|A repair follows an identified actual defect, not the initial comparison.
uf|LOW|Low|Medium|Low|Early|A broad tool-fit map is unnecessary for this one exact diff.
adep|NEGATIVE|Low|High|High|Wrong time|Actual user calibration is absent and selective extraction is not this task.
upth|MEDIUM|Medium|Medium|Medium|Early|Visible comparison choices could later reveal an unformalized operation.
la|MEDIUM|High|Medium|Low|Right time|Can expose loss of an action dependency or missing input.
benf|LOW|Low|Medium|Medium|Early|Benefit estimation needs an actual proposed repair and comparison horizon.
boc|MEDIUM|Medium|High|Medium|Early|Twenty options are useful only if the current checking approach fails.
utp|NEGATIVE|Low|Medium|High|Wrong time|An ideal instruction world does not decide whether this reorder is valid.
cmplx|LOW|Low|High|Medium|Early|The present dependency relation has six actions and no nonlinear system model. '''.strip()
make(2,'Choose an operation that detects consequential dependency changes between two instruction versions.','Version A is gather→connect→select→power→check→start. Version B changes gather wording and moves power before connect. Check success is still required for start.',raw2,'/md on the exact A/B input; /pv on the resulting dependency representation.',[
'MD raises PV by defining which relation the validation must check.','PV raises SVS only if a display defect obscures a valid dependency.','MTcg raises MD when a word-diff strategy is visibly missing order.','FOHT becomes more valuable if direct relation checking cannot express the condition.','SP has lower ROI after exact A/B input is preserved.','PCD becomes positive if a needed conditional dependency has no available operation.','PCI becomes positive after PCD produces an authored procedure with a schema.','SATR becomes less risky only after actions are proven redundant.','BENF becomes more useful after an actual repair changes effort or error.','ITERATE follows a specific defect instead of redesigning a correct instruction.'], 'MD-01 consumes these exact two versions; it does not ask for an invented user preference or discard original exposures.')
raw3='''sp|LOW|Low|Low|Low|Early|The open creative input is already intentionally precise about preserving openness.
given|NEGATIVE|Low|High|High|Wrong time|Scoring a full method portfolio consumes the play opportunity without resolving ambiguity in the goal.
wsib|LOW|Low|Medium|Low|Early|The next act is generation; another router adds little.
mrc|MEDIUM|Medium|Low|Low|Right time|Checks whether exploration is being replaced by solving.
mtcg|HIGH|High|Medium|Low|Right time|Can reveal a drift from noticing possibilities into judging them.
pbtc|NEGATIVE|Low|High|High|Wrong time|There is no factual thesis whose provenance requires an eight-pass audit.
unx|HIGH|High|Medium|Low|Right time|Can disrupt the first conventional reading of a punctuation-only seed.
foht|LOW|Low|High|Medium|Early|Method search assumes a defined outcome beyond the requested exploration.
svs|HIGH|High|Medium|Low|Right time|Changing spacing, orientation or role creates different symbolic readings.
crtv|HIGH|High|Medium|Low|Right time|Divergence and combinations directly produce the requested different forms.
gg|MEDIUM|Medium|High|Medium|Early|Broad guesses are possible but 200-plus exceeds the current small seed’s need.
md|MEDIUM|Medium|Low|Low|Right time|Can identify generation rather than proof as the present operation.
pcd|LOW|Low|Medium|Low|Early|No missing procedural dependency blocks making a new continuation.
pci|NEGATIVE|Low|Medium|High|Wrong time|Schema polishing replaces the creative object with procedure administration.
pv|NEGATIVE|Low|Medium|High|Wrong time|Treating open readings as valid/invalid procedures changes their purpose.
satr|NEGATIVE|Low|Medium|High|Wrong time|Early pruning suppresses divergent variants before any use is visible.
iterate|MEDIUM|Medium|Medium|Medium|Early|Useful after actual variants exist, with the open brief preserved.
uf|LOW|Low|Medium|Low|Early|A twelve-case fit map is not needed to begin this particular play.
adep|NEGATIVE|Low|High|High|Wrong time|User-rating calibration is absent and extraction is not generation.
upth|MEDIUM|Medium|Medium|Medium|Early|A visible unexpected move can be formalized after it occurs.
la|LOW|Low|Medium|Medium|Early|A broad limitation inventory can crowd out the intended playful encounter.
benf|LOW|Low|Medium|Medium|Early|An expected-value calculation is not supplied a commensurable creative payoff.
boc|NEGATIVE|Low|High|High|Wrong time|Forcing a best option conflicts with retaining multiple readings.
utp|MEDIUM|High|Medium|Medium|Right time|Can open an ideal possibility without claiming that it is the chosen destination.
cmplx|LOW|Low|High|Medium|Early|The short seed does not yet require a feedback-system decomposition.'''
make(3,'Choose a way to explore a punctuation-only seed while preserving curiosity rather than forcing a correct interpretation.','Seed: “. . : / .” The task is to produce different readable arrangements or continuations; no hidden correct answer is specified.',raw3,'/crtv on the exact seed; /unx if the generated forms remain conventional.',[
'CRTV raises UNX quality by making the cached first readings visible.','SVS supplies structural raw variants to CRTV without demanding a winner.','MRC prevents a hidden switch from exploration to proof.','MTcg can change the active operation when scoring crowds out generation.','SP loses value after the prompt already protects openness.','ITERATE becomes useful only after variants exist to compare.','UPTH can capture a new operation after an unexpected output occurs.','SATR becomes relevant only after repeated variants reveal actual redundancy.','UTP can enrich a candidate world without selecting it as the required goal.','PV remains inappropriate for judging literary truth but can later validate a technical rendering artifact.'], 'CRTV-02 consumes the punctuation seed and produces several interpretations; no lowest-cost or highest-scoring reading is made the correct one.')
