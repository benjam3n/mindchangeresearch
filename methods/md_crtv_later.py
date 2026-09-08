from write_support import *
A=['gather','connect','select','power','check','start']
B=['gather','power','connect','select','check','start']
B2=['gather','connect','select','power','start','check']
def relations(seq):return {(a,b) for i,a in enumerate(seq) for b in seq[i+1:]}
def check(seq):
 return {'power_before_connect':seq.index('power')<seq.index('connect'),'start_requires_prior_successful_check':'satisfiable_order' if seq.index('check')<seq.index('start') else 'violated_order','physical_power_constraint':'unspecified'}
obs={'A':A,'B':B,'B2':B2,'removed_precedence':sorted(relations(A)-relations(B)),'added_precedence':sorted(relations(B)-relations(A)),'A_check':check(A),'B_check':check(B),'B2_check':check(B2),'gather_wording':'A: Gather materials. B: Assemble the materials.'}
(D/'instruction-difference-observations.json').write_text(json.dumps(obs,indent=2))
rows=[
['Word diff (obvious)','Wording and moves are the desired answer family.','Yes for edited text; insufficient for physical validity.','Reports gather wording and power move; cannot invent a causal rule.','Equivalent synonym could dominate visual diff despite no action change.'],
['Treat all reordered versions as equivalent (opposite)','Only bag of actions matters.','No: check success must precede start.','Erases both the potentially harmless power move and B2’s definite violation.','B2 has same actions and starts before check.'],
['Dependency graph from build systems (cross-domain)','Prerequisites are declared independently of display order.','Partly: check-success before start is declared; cable/power physics are absent.','Separates observed precedence from required causal relation.','A missing physical rule would change validation; do not call B safe.'],
['Execute every instruction as a physical experiment','A device and safe experiment are available.','No physical device or specifications are supplied.','Could resolve causal order but unavailable in this bounded model task.','A symbolic trace is not physical evidence.'],
['Full permutation enumeration','Every ordering can be judged by the supplied rules.','Only for the declared check-before-start rule.','Enumerates formal violations but leaves device validity unmeasured.','An allowed permutation may violate an undeclared real prerequisite.']]
body='''Exact input from GIVEN-02: A = gather→connect→select→power→check→start. B changes gather wording and moves power before connect: gather→power→connect→select→check→start. Check success is still required for start. A’s original wording is “Gather materials.”; the concrete B wording used for the lexical fixture is “Assemble the materials.” This added wording fixture is labeled, not claimed as another user-supplied fact.

Step 1 — Situation. This is a comparison of two symbolic instructions under one explicit prerequisite. Resources are the original six-state interface, both orderings and exact source strings. Success means identify consequential declared changes without promoting procedural sequence into a physical law. No device manual or performed setup is available. Word comparison has not failed at finding the move; its limitation is that edit size does not answer dependency validity.

Step 2–3 — Distinct methods and fit:

'''+table(['Method','Assumption','Fit','Actual output/omission','What would show it wrong'],rows)+'''

Step 4 — Derived method. Preserve three relation types: lexical edits, descriptive action precedence, and independently required prerequisites. First compare words; then compare all ordered action pairs; finally evaluate only declared prerequisites. Because the input supplies one mandatory check-before-start relation but no cable/power rule, this gives one definite validation domain and one unresolved physical domain.

Executed product in instruction-difference-observations.json: B removes connect< power and select< power, adding power< connect and power< select. B retains check< start. Calling B physically invalid would require a new premise. Calling it physically safe would require the same missing knowledge. The lexical fixture records a gather wording change but no new action identity.

Step 5 — Question derivation and actual subsequent use. A new boundary B2 uses gather→connect→select→power→start→check. The chosen method flags a definite violation of the supplied check-before-start condition. The bag-of-actions method misses it because A and B2 have identical bags. A word diff detects both B and B2 moves but does not by itself establish which violates a declared condition. This subsequent comparison is performed, not merely suggested. Retaining unresolved physical validity is part of the output rather than a promise to obtain device facts.

Characterization review: the task is not a device-safety certification; no source says connect-before-power is physically required. Method diversity is real: textual edit, equivalence erasure, typed relation validation, physical trial and exhaustive symbolic enumeration produce different answers. The graph analogy survives only for declared relations. Its main revision from the preliminary selection is to refuse to label every removed precedence a broken prerequisite. Current no further method change is justified by these three versions.'''
record('md-01','Attend to declared prerequisites when comparing instruction versions, while preserving unresolved physical causality.','Word differences are a sensible first comparison, but the supplied action order alone does not establish which orderings are physically necessary.',body,'The comparison now types an observed reorder separately from a violated declared prerequisite; B remains physically unresolved while the later B2 fixture is flagged.','Actual B2 use distinguishes a definite supplied-rule failure from the unsupported claim that B is physically invalid. New within this constructed instruction case; no human setup effect is claimed.','KEEP','Typed relation output preserves the answer family better than either a word-only display or a bag of actions; exact original strings remain available.','Use the typed relation input in FOHT-02; supply a real additional rule before resolving B; compare a pure wording edit as a negative case.')
raw=[
('ellipsis with slash as line break','cached'),('face with colon eyes','cached'),('a sparse star map','cached'),('beats separated by a rest','cached'),
('footsteps approaching a doorway','free list'),('two seats beside a table, one seat beyond a screen','free list'),('a seam of four stitch kinds','free list'),('a key for an invented map with no hidden legend','free list'),('three camera cuts around a paired object','free list'),('a tiny score whose colon asks for two simultaneous taps','analogy: score'),('two singles, a pair, a crossing, a single','free list'),('the slash becomes a dividing wall while the dots stay on both sides','SCAMPER: role substitution'),
('a courtroom where punctuation sues the blank spaces','absurd'),('a planet that files tax returns as dots','absurd'),('a slash that eats all the ink and leaves the page heavier','absurd'),('a colon trying to become two separate rooms','absurd'),
('repeat the row below with the slash moved one place','SCAMPER: movement'),('read the same marks once as positions and once as durations','analogy: coordinate systems'),('make the blank intervals the foreground and marks their boundaries','inversion'),('preserve the row and append a mirrored reply','SCAMPER: reversal')]
comb=[('10+18','Same marks with separate spatial and temporal legends; no assertion that either decodes the seed.'),('12+19','A wall map whose gaps, not occupants, receive names.'),('17+20','A second row replies by mirroring, allowing visual conversation without speakers.'),('11+16','A pair splits into separate rooms, made concrete through spacing rather than a narrative claim.')]
scored=[['dual score/map',3,5,8,'Two distinct operations on unchanged marks; local novelty only.'],['gap-first wall map',4,4,8,'Attention shifts to intervals; labels may overdetermine it.'],['mirrored reply',2,5,7,'Simple but immediately makeable.'],['colon becomes rooms',3,4,7,'One visible structural event.'],['punctuation lawsuit',2,2,4,'Amusing premise but drops the exact formal opportunity.'],['tax planet',3,1,4,'Absurdity supplies little usable connection.'],['ellipsis line break',1,4,5,'Conventional but still permitted.'],['unlabeled constellation',1,3,4,'Preserves openness but offers little distinct action.']]
products='''Seed, unchanged: . . : / .

A. Two readings for the same marks
Spatial: dot, gap, dot, gap, pair, gap, crossing, gap, dot.
Temporal score: tap — tap — two together — sweep — tap.
The spatial reading asks where; the score asks what to do next. These are offered conventions, not recovered meanings.

B. A reply
. . : / .
. / : . .

C. The pair leaves itself
. . : / .
. . . . / .
The colon has become two separate dots in the continuation. The first line remains untouched.
'''
(D/'punctuation-continuations.txt').write_text(products)
body='''Step 1 — Creative brief. Need: explore different readable arrangements or continuations of the exact seed “. . : / .”. Constraint: preserve it visibly and do not invent a hidden correct answer. Domain: typographic play and invented reading conventions. Current baseline: ellipsis, face or constellation are plausible first readings; there is no evidence they disappoint the user. “Better” here means delivering distinguishable playable operations, not proving enjoyment or semantic correctness.

Step 2 — Twenty raw ideas from free listing, role substitution/reversal and score analogy. First four are explicitly cached; four are absurd. Generation is retained before convergence.

'''+table(['#','Raw idea','Generation role'],[[i+1,*r] for i,r in enumerate(raw)])+'''

Step 3 — Actual combinations:

'''+table(['Parents','Hybrid'],comb)+'''

Step 4 — Local candidate judgments, novelty/usefulness 1–5. These are model editorial judgments, not user ratings or expert novelty measurements.

'''+table(['Idea','Novelty','Usefulness','Total','Rationale'],scored)+'''

Step 5 — Three candidates developed and built in punctuation-continuations.txt. A dual score/map works by assigning two explicit conventions to unchanged marks; first build is the actual pair of readings; risk is falsely presenting one convention as decoding; edge is a different available operation. The mirrored reply works by preserving the first row and adding a reversal; first build is the actual two-line object; risk is sameness masquerading as diversity; edge is a visual continuation with no prose explanation required. The splitting colon works by changing the continuation’s pair into separate dots; first build is its second row; risk is changing the original, avoided by retaining it verbatim; edge is a visible structural event.

Step 6 — Fit check: all three preserve the exact seed and produce readable distinctions; no true reading is named. They differ within this set. Reader pleasure and expert surprise are untested. I would retain the built set for the requested exploration. Candidate A is the strongest operational departure, B the low-demand runner-up; this selection is about development attention, not semantic correctness.

Step 7 — Creative output: the finished three-part artifact is saved. In a further actual use, a new seed “: / :” is read once as paired positions separated by a boundary and once as “two together — sweep — two together.” This demonstrates local reuse of distinct reading conventions. It does not show that this second application benefits a reader or adds a new research finding beyond UNX-01’s prior established expansion of possible readings.'''
record('crtv-02','Make several playful operations available for a punctuation-only seed without turning exploration into a correctness contest.','An ellipsis or sparse face is a reasonable first reading; no preference evidence says it needs replacement.',body,'Three concrete continuations are now available, and a new seed was processed under both spatial and temporal conventions.','The requested creative products exist. An additional beneficial mind change beyond already established alternative-reading operations is not demonstrated; local use is not automatically novel benefit.','REJECT','Keep exact seed and developed variants together; retain the raw list for fidelity but do not make it the primary reading experience.','Try spacing alone; allow a human reader to choose a convention without presuming enjoyment; use UNX-02 to seek a structurally different operation.')
