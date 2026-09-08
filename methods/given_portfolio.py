from write_support import *
A=json.loads((ROOT/'allocation.json').read_text())['skills']
# Classification, upside, cost, risk, timing, concrete present-state rationale.
raw='''ar|H|High|Medium|Low|Right time|Derive commitments of the accepted program before choosing what to omit.
aex|M|High|High|Medium|Right time|Hidden premises matter, but a full recursive expansion competes with actual trials.
dd|H|High|Medium|Low|Right time|New change dimensions prevent all 300 targets from becoming belief audits.
se|M|High|High|Medium|Early|Enumeration needs the discovered dimensions to avoid abundant same-kind cases.
spd|H|High|Medium|Low|Right time|Map actors and possible change locations before broad guesses.
u|M|High|High|Medium|Early|Universalization expands scope but needs definite claims to remain tractable.
ipss|H|High|Medium|Low|Right time|Mind change includes condition and capability changes; preserve these readings.
mss|M|Medium|Medium|Medium|Early|Competing causal models become useful once concrete outcomes exist.
frq|M|Medium|Low|Low|Early|The task is clear; local unresolved questions can still change the next target.
orgn|L|Low|Medium|Medium|Wrong time|Organizational incentives are useful for coordination, not for arranging Markdown findings.
sim|L|Low|Medium|Medium|Early|Compressing a barely populated corpus risks deleting scope before its uses appear.
ro|M|High|Medium|Low|Early|Reordering benefits concrete queues after dependencies and findings exist.
wre|M|Medium|Medium|Low|Right time|The shared document contract is present; remaining requirements must add distinctions.
w|L|Low|High|Medium|Early|Polishing prose before substantive outputs would consume the drafting budget.
alt|H|High|Medium|Low|Right time|Changing abstraction can expose a different intervention rather than more wording.
ma|H|High|Medium|Low|Right time|Crossing actor with locus creates substantively different application inputs.
ctcov|H|High|Medium|Low|Right time|Coverage checks can detect missing perception or action despite many reasoning skills.
difr|H|High|Medium|Low|Right time|Distinguishing effect from attribution changes what can be kept.
vcl|M|Medium|Medium|Medium|Early|Criteria may change, but the user's stated aims already constrain first trials.
ve|N|Low|High|High|Wrong time|A new value interview now delays authorized work and invents uncertainty about the stated scope.
vcd|M|High|Medium|Medium|Early|Efficiency and exhaustive exposure can conflict locally without invalidating the program.
pre|N|Low|High|High|Wrong time|Asking the user to rank the already specified scope offloads our current task.
grfr|N|Low|High|High|Wrong time|Reframing the 300-application goal as a smaller goal would violate the premise.
funr|H|High|Medium|Low|Right time|Exploration for interest adds targets beyond error correction.
mp|M|Medium|Medium|Medium|Early|Human motivational orderings need an actor; model output pace is observable here.
trust|M|High|Medium|Medium|Early|Source and execution trust differ; interpersonal trust effects remain unobserved.
td|M|Medium|Medium|Low|Right time|Sequence timing is actionable even without an external deadline.
rso|H|High|Medium|Low|Right time|Separate fixed exposures from changing execution queues to use available work efficiently.
ecal|M|High|Medium|Medium|Right time|Effort can vary above original floors, but calibration cannot cut mandatory depth.
kta|H|High|Medium|Low|Right time|A finding must change an actual subsequent operation before earning KEEP.
de|H|High|Medium|Low|Right time|Original subordinate invocations and input gates are genuine prerequisites.
to|H|High|Medium|Low|Right time|Dependencies determine the next executable slot rather than numerical rank alone.
lt|M|High|High|Medium|Early|A useful local change needs a distinct later use before transfer is claimed.
memy|M|Medium|Medium|Low|Early|Retention cues need findings; initial filing is not demonstrated future retrieval.
sp|L|Low|Low|Low|Early|The global prompt has just been improved; another identical rewrite is redundant.
given|M|High|High|Low|Right time|The 150-row ranking separates coverage placement from current readiness at substantial cost.
wsib|H|High|Medium|Low|Right time|A concrete next-skill decision can now use the loaded sources and current blockage.
mrc|H|High|Low|Low|Right time|A progress checkpoint can keep counts from replacing substantive exploration.
mtcg|M|High|Medium|Low|Right time|A current strategy switch can be inspected after the first products appear.
pbtc|M|High|High|Medium|Early|Audit actual verdicts after they exist; assuming the program right is a premise, not a discovered effect.
unx|H|High|Medium|Low|Right time|Structural alternatives are needed so the next targets are not all prompt or audit edits.
foht|H|High|Medium|Low|Right time|Method tests can change an actual representation or available operation now.
gjs|H|High|Medium|Low|Right time|The GOSM runs need goal chains that preserve rather than substitute the request.
fut|M|High|High|Medium|Early|Future use is important but speculative effects must not become current keeps.
gd|H|High|Medium|Low|Right time|Decomposition turns the full exposure request into independently executable work.
gsr|M|Medium|Medium|Low|Early|Goal reconstruction can check apparent reversals once recommendations exist.
grf|L|Low|Medium|Medium|Wrong time|Making the already quantified goal SMART adds little now.
lpd|M|High|Medium|Medium|Early|Insertion points become concrete when observed bottlenecks exist.
sysarch|M|High|High|Medium|Early|Architecture can preserve interfaces but an elaborate framework before outputs adds cost.
ltai|M|High|High|Medium|Right time|Handoffs are real, while claims of autonomous future runs need actual continuation mechanisms.
ifss|M|High|High|Medium|Early|Inference alternatives need a definite claim rather than the entire program.
qaf|M|Medium|Medium|Low|Early|Local question classification helps after a blockage is identified.
qr|M|Medium|Medium|Medium|Early|Routes can expose adjacent questions without making all of them new goals.
ael|M|High|Medium|Medium|Early|Removing a real optional assumption can unlock conditions; removing requirements cannot.
fctl|M|High|Medium|Low|Early|Factual claims must be tested when introduced; few external facts exist yet.
cscl|M|High|High|Medium|Early|Causal attribution needs contrasts; a generated case alone supplies none.
rci|M|High|High|Medium|Early|Recursive causal interrogation should follow actual failure evidence.
rca|L|Low|Medium|Medium|Early|No root cause is yet established; generic failure diagnosis would repeat warnings.
op|M|Medium|Medium|Low|Early|Order individual operations once their prerequisites are explicit.
cn|L|Low|Medium|Medium|Early|Narrative order is premature for a developing evidence corpus.
draft|M|Medium|Medium|Low|Right time|Separate initial products from repaired versions to preserve revision evidence.
re|H|High|Medium|Low|Right time|Reading exact originals affects numerical floors and permissible invocations now.
anag|M|Medium|Medium|Medium|Early|Analogy can generate operations but transfers need concrete mappings.
cda|M|High|Medium|Medium|Early|Cross-domain mechanisms broaden targets but do not independently validate them.
categorize|M|High|Medium|Low|Early|Grouping will help actual keep retrieval once several findings exist.
txm|L|Low|Medium|Low|Early|Taxonomy maintenance requires categories used beyond a single trial.
gu|N|Low|High|High|Wrong time|Reopening the clear full goal now would replace execution with intake.
ig|M|Medium|Medium|Medium|Early|Intuitive preferences can be explored as model working choices, not diagnosed human states.
eg|H|High|Medium|Low|Right time|Some trials can discover a worthwhile destination instead of beginning with an error.
hab|L|Low|High|High|Early|Human habit formation lacks repeated human behavior in this session.
hf|L|Low|High|High|Early|Habit durability cannot be observed from a model-written schedule.
eqi|M|Medium|Medium|Medium|Early|Emotional appraisal is a target design; current human effects remain unknown.
socg|M|Medium|Medium|Medium|Early|Role interpretations matter but need signals beyond invented stakeholder motives.
al|M|Medium|Low|Low|Right time|Exact instruction uptake is observable; psychological listening benefit is not assumed.
empth|M|Medium|Medium|Medium|Early|Perspective taking can alter response design without proving another's feelings.
qs|H|High|Medium|Low|Right time|A ready queue can start useful lower-ranked work while exposure counts remain fixed.
enough|L|Low|Medium|High|Early|Stopping required applications early is not sufficiency; settled subbranches may stop.
tobd|M|Medium|Low|Low|Right time|Flag absent ratings and unavailable dependencies without silently imputing them.
nstep|H|High|Low|Low|Right time|Select a concrete next operation after identifying a real blockage.
pt|H|High|Medium|Low|Right time|Three counters prevent progress inflation and reveal unfinished gates.
acr|M|High|Medium|Low|Early|Recall checks become meaningful after findings exist to retrieve.
spr|L|Low|High|Medium|Early|Longer spaced retention awaits elapsed time and a real continuation.
ska|M|High|High|Medium|Early|Capability acquisition needs tasks that distinguish trained from untrained behavior.
dlp|M|High|High|Medium|Early|Deliberate practice needs a specific weak operation and feedback.
svs|H|High|Medium|Low|Right time|Mechanical substitutions can change medium or operation in a bounded trial.
crtv|H|High|Medium|Low|Right time|Novel designs broaden attention beyond procedure fidelity.
gg|M|High|High|Medium|Right time|The original 200-plus search is expensive but supports requested breadth on two targets.
md|H|High|Low|Low|Right time|Derive a method from current available evidence instead of familiar router order.
pcd|H|High|Medium|Low|Right time|Missing operation signatures can be identified before a long attempted execution.
pci|L|Low|Medium|Medium|Early|Schema improvement needs a declared schema and authored procedures; originals are immutable.
pv|H|Critical|Medium|Low|Urgent|Actual source gates already distinguish ready work from unavailable human calibration.
satr|L|Low|Medium|Medium|Early|Item counts alone do not establish redundant results before use records exist.
gaa|M|High|High|Low|Early|Audit an actual GOSM run, not a title and planned phase list.
sysdecomp|M|High|Medium|Medium|Right time|Decompose work while retaining shared source and integration dependencies.
sysintegration|M|High|High|Medium|Early|Integration should follow developed line outputs and clear evidence scopes.
sya|M|High|High|Medium|Early|System analysis needs interfaces or failures to avoid generic architecture prose.
systhink|M|High|Medium|Medium|Early|Feedback in selection is real; claims about psychological feedback remain hypotheses.
requirements|M|High|Medium|Low|Right time|Source requirements can be traced to actual products without adding a new framework.
tracematrix|H|High|Medium|Low|Right time|Exposure, procedure and benefit obligations need separate evidence links.
exd|M|High|High|Medium|Early|Design comparison tasks before claiming causal benefit, but avoid unnecessary measurement burdens.
ht|M|High|High|Medium|Early|Test definite live claims; the entire user program is the accepted premise.
src|H|High|Medium|Low|Right time|Receipts, archive source and execution evidence support different trust judgments.
av|H|High|Medium|Low|Right time|Verify concrete capability and source assumptions with available files.
sdc|M|High|High|Medium|Early|Actual conclusions supply audit material; inventing bias does not.
mtcl|M|Medium|Medium|Medium|Early|Claims about KEEP quality need distinction from underlying beneficial effect.
rlcl|M|Medium|Medium|Medium|Early|A prerequisite relation is not a causal treatment effect.
icl|M|Medium|Medium|Medium|Early|The user expressed intention is evidence; hidden motives stay uncertain.
dvs|H|High|Medium|Low|Right time|Diversity belongs in input selection before 300 repetitions become repetitive.
mv|L|Low|Medium|Medium|Early|Mind-change dimensions overlap legitimately; forced exclusivity can erase interactions.
ctgp|H|High|Medium|Low|Right time|Coverage gaps can direct next targets while keeping required exposures.
nusr|M|Medium|Medium|Low|Early|A newcomer simulation can test retrieval after a populated index exists.
vdp|L|Low|Medium|Medium|Early|Visual decoration adds no present operation unless a comparison is hard to read.
prd|N|Low|High|High|Wrong time|Building slides now displaces authorized substantive documents without a presentation need.
sum|L|Low|Medium|Medium|Early|A final summary before records exist risks a preselected narrative.
omtx|H|High|Low|Low|Right time|Exact comparison tables preserve criteria across different method choices.
met|M|Medium|Medium|Medium|Early|Metaphors can alter representation but require explicit limits.
collab|M|High|High|Medium|Right time|Separate lines and shared constraints create real coordination choices.
col|M|High|Medium|Low|Right time|Owned files and integration interfaces prevent conflicting edits.
gdm|L|Low|High|Medium|Early|There is no real stakeholder vote to report; group procedure remains a design trial.
tfac|L|Low|High|High|Early|A session plan is not an attended group facilitation outcome.
fd|M|High|Medium|Low|Early|Feedback can change the next model application once an actual defect exists.
cfr|L|Low|High|Medium|Early|No evidenced interpersonal conflict requires resolution now.
rtas|L|Low|High|High|Early|A rights analysis needs a concrete rights-bearing context; no legal facts are inferred here.
rlg|L|Low|High|Medium|Early|A relationship goal is not established merely because communication occurs.
memk|H|High|Medium|Low|Right time|Preserve usable triggers and provenance as outputs accumulate.
lrs|M|High|High|Medium|Early|Learning-system changes need observed application results rather than all-positive logs.
ld|H|High|Medium|Low|Right time|Schedule discriminating tasks before cosmetic reporting.
pwif|M|High|Medium|Medium|Early|Physical feasibility matters for target designs; model cannot enact human relocation.
rwif|M|High|Medium|Medium|Early|Logistics distinguish actionable instructions from performed physical changes.
hsi|M|High|High|Medium|Early|Accessibility is valuable but effects need actual users or scoped inspection.
rva|H|High|Medium|Low|Right time|Reversible working-state trials can proceed without waiting for global certainty.
fr|M|High|Medium|Low|Early|A recovery path becomes useful when a specific step is blocked.
iterate|L|Low|High|Medium|Early|Before a substantial target exists, iteration becomes meta-work; reserve the assigned run.
uf|M|High|Medium|Low|Early|Fit maps become sharper after several distinct uses expose switch conditions.
adep|N|Low|High|High|Wrong time|Twenty actual user ratings are absent; pretending calibration and pruning exposures would mislead.
upth|M|High|Medium|Medium|Early|Visible choice transitions can reveal operations; private cognition is not a data source.
la|M|High|Medium|Low|Right time|Capability limits can redirect work to a feasible locus without abandoning scope.
benf|M|Medium|Medium|Medium|Early|Benefit estimates need stated scenarios and cannot turn probabilities into observations.
boc|M|High|Medium|Medium|Early|Twenty options help a live commitment; current program itself is accepted.
utp|M|High|Medium|Medium|Early|An ideal can reveal neglected capabilities while remaining a constructed scenario.
cmplx|M|High|High|Medium|Early|Interactions among evidence, timing and reuse need tracking after first outputs.
abts|M|High|High|Medium|Early|Controlled tests need interventions and outcome criteria before sample-size claims.
emv|M|High|High|Medium|Early|External validation cannot be replaced with the model affirming its own output.
dom|H|High|Low|Low|Right time|Supported dominance can choose between concrete local options without arbitrary weights.
mcd|M|High|High|Medium|Early|Multi-criteria choices help genuine tradeoffs; weights are not yet elicited.
cba|N|Low|High|High|Wrong time|Dollar-valued NPV of unobserved cognitive benefits would invent commensurability.
lcca|N|Low|High|High|Wrong time|A life-cycle cost forecast before artifacts and usage exist adds unsupported precision.
ram|N|Low|High|High|Wrong time|Reliability rates require failure observations; a made-up MTBF would distort confidence.
ret|L|Low|Medium|Low|Early|A retrospective belongs after a meaningful batch has actually executed.
ssr|L|Low|Medium|Low|Early|Session review before substantive outcomes records intentions rather than learning.'''
S={}
for line in raw.splitlines():
 id,cl,u,c,r,t,why=line.split('|');S[id]={'roi':{'H':'HIGH','M':'MEDIUM','L':'LOW','N':'NEGATIVE'}[cl],'upside':u,'cost':c,'risk':r,'timing':t,'reason':why}
assert set(S)=={s['id'] for s in A}
rows=[]
for s in A:
 q=S[s['id']];rows.append([s['rank'],s['id'],q['roi'],q['upside'],q['cost'],q['risk'],q['timing'],q['reason']])
interactions=[
'dd raises se: discovered loci supply categories before enumeration.',
'spd raises gg: a known actor and scope make 200-plus guesses less repetitive.',
'de raises to: actual dependencies constrain ordering.',
'pv raises foht: capability gates eliminate impossible methods before deep testing.',
'sp lowers another identical sp: its missing-criteria benefit has already been harvested.',
'foht raises kta: viable methods supply executable first actions.',
'ctcov raises dvs: demonstrated gaps select diverse next inputs.',
'lt raises memy: an observed later use identifies what is worth encoding.',
'given lowers wsib cost: the shortlist supplies candidate comparisons, but wsib still checks current state.',
'orgn does not raise file categorization: its organizational-incentive input is a different subject.',
'satr lowers sim risk only after use: an actual redundancy cluster permits loss-aware compression.',
'exd raises emv: outcome and contrast declarations make empirical observations interpretable.',
'upth raises pci after a procedure exists: a declared operation can gain schema fields without changing originals.',
'adep remains blocked after given: a ranking cannot substitute for human calibration ratings.'
]
body='GOAL: Complete the fixed 150-skill portfolio with 300 exposures plus ten GOSM runs while each next operation has a concrete beneficial opportunity. TYPE: exploration + achievement. CONSTRAINTS: original depth, assigned ownership, actual capabilities, no invented human data. CURRENT STATE: all 25 methods originals loaded; SP-01 completed; most product-specific data do not yet exist. GOAL CLARITY: clear. URGENCY: ready to act.\n\nCandidate selection covers direct, preparatory, validation, risk and recovery roles across all 150 allocated skills. Scores below are qualitative judgments of use NOW. Cost means original-depth work and required dependencies; risk means misdirection from absent input or wrong timing; upside refers to the current opportunity, not intrinsic superiority. Each row states the concrete fact that drives its four-dimensional judgment. “Early” means input or phase has not arrived. No score estimates a measured effect size.\n\n'+table(['Frozen rank','Skill','ROI now','Upside','Cost','Risk','Timing','Present rationale'],rows)+'\n\nRUN_NOW: /pv on the actual methods execution plan (Critical upside, urgent source gates); /foht on an actionable representation change (after feasibility); /unx on an unfamiliar attention target (diversity); /wsib on the next observed local blockage (concrete selection). These four differ in validation, method discovery, exploration and immediate routing.\n\nNegative-now conditions are in the nine NEGATIVE rows. They become positive when their real inputs arrive: a live value conflict for ve/pre/gu; an explicitly revised goal for grfr; a requested presentation for prd; actual calibration ratings for adep; observable costs/benefits and a commensurable decision for cba/lcca; reliability event data for ram. None is deleted from the frozen exposure allocation.\n\nInteractions:\n\n'+ '\n'.join(f'{i+1}. {v}' for i,v in enumerate(interactions))+'\n\nPresent ranking correction: pv (frozen rank 91) now precedes wsib (37). orgn (10) is not a leading file-organization method; it remains scheduled on coordination and incentives. The numeric portfolio is a coverage allocation rather than a global leaderboard.\n\nActual uptake: methods/queue.json is written with pv-01 first, then foht-01, unx-01 and wsib-01, preserving every remaining application slot. The archive allocation file remains unchanged. The next completed application is pv-01; this distinguishes the recommendation from a static ranked list.'
record('given-01','Separate coverage rank from executable present priority across the whole portfolio.','The frozen numerical allocation supplies a reasonable starting sequence; I expected to proceed from given to wsib unless a source dependency changed the choice.',body,'PV moved ahead of WSIB because actual source/input gates matter now. Organization Analysis was removed from the role of arranging files and retained for coordination.','The next queue selects an executable prerequisite check without discarding any of the 300 required exposures. This is an observable allocation change, not measured superiority of PV across domains.','KEEP','The table retains all 150 scores while the four-item RUN_NOW slice is usable. A numeric score would falsely imply measurement; qualitative columns preserve uncertainty and reasons.','Execute PV on readiness; revisit ROI for attention and for a populated archive; test whether the new queue preserves original prerequisites.',depth='Original 8x floors: at least 25 candidates/scored, six negative-now entries, ten interactions. Actual: 150 candidates/scored, nine negative-now entries, fourteen interactions, four RUN_NOW entries.')
allslots=[f"{s['id']}-{i:02}" for s in json.loads((D/'allocation.json').read_text()) for i in range(1,s['applications']+1)]
first=['pv-01','foht-01','unx-01','wsib-01'];queue=[x for x in first+allslots if x not in ['sp-01','given-01']]
queue=list(dict.fromkeys(queue))
(D/'queue.json').write_text(json.dumps({'reason':'given-01 present priority; frozen exposure slots retained','ready_next':first,'remaining_slots':queue},indent=2))
(D/'portfolio-scores.json').write_text(json.dumps(S,indent=2))
