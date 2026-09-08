from write_support import *
seed='The drawer was empty, except for a rectangle of unfaded wood.'
products='''Seed: The drawer was empty, except for a rectangle of unfaded wood.

1. Absence as a measure
She laid the letter over the pale rectangle and folded the edges inward until the dark wood showed all around it. Whatever had gone was still deciding the size of what could stay.

2. Absence as a route
He set a finger at one corner and followed the pale edge to the next. For once, an empty drawer offered a way around something.

3. The obvious reading, retained
The box was gone. Its outline remained, precise enough to make the emptiness look deliberate.
'''
(D/'drawer-continuations.txt').write_text(products)
body=f'''Exact creative input: “{seed}” Continue it without explaining the absent object’s true identity. The baseline is an ordinary missing-box/memory continuation; it fits the seed and is retained. There is no known-optimal continuation, and no user enjoyment rating is available.

Layer 1 — The obvious. An object formerly covered the pale rectangle; a character notices its loss. This is coherent and economical. It is a proposed literary continuation, not a verified physical explanation of the wood.

Selected disruption techniques (four, actually applied): first-answer rejection retains the loss reading but searches past it; assumption elimination removes “the absence must be explained” and separately “the mark is only evidence of the past”; role randomization uses a paper folder’s concern with size rather than a detective’s concern with identity; provocation says “the missing object is still a tool,” then removes the impossible living object and retains its present usable geometry.

Layer 2 — Three structurally different candidates and quality gates:

'''+table(['Candidate','Structural difference','Feasibility/need','Conventionality judgment','Disposition'],[
['Use the rectangle as a folding measure','Changes from interpreting a past object to performing a present operation with a trace.','A constructed scene can use a boundary to size paper while leaving identity unspecified.','The exact fold-to-empty-outline combination is locally non-obvious relative to the missing-box baseline; measuring by a trace is not claimed as an unknown technique.','Survives as an exact creative product.'],
['Treat the pale perimeter as a tiny route','Changes the trace into an action path rather than an explanation.','A finger can trace the edge in the written scene; no actual touch is claimed.','Tracing is conventional, but its use as a way around absence supplies a distinct scene.','Keep as a secondary continuation, no expert-surprise claim.'],
['Let the missing box issue instructions','Adds an impossible speaking agent instead of using the given geometry.','Possible fantasy but weak fit to this seed’s exact material opportunity.','Personification is conventional, so verbal weirdness does not establish novelty.','Reject and replace with the measure candidate.']])+'''

Layer 3 — Reframed. The task need not be “infer what used to be here”; it can be “discover what this remaining shape makes possible now.” This changes the creative operation while preserving the seed and its unspecified past. It does not decide that the user’s exploration should become utility-maximization: the resulting scenes remain literary play.

Structural-difference check: Layer2’s first candidate actually uses a boundary as a sizing constraint; it is not merely a new adjective for loss. Layer3 changes the question from historical identity to current affordance. Quality gate: the exact first scene is feasible as fiction, preserves the original, addresses the continuation request and departs from the local baseline. No empirical claim that a domain expert would be surprised is available; novelty is restricted to this constructed candidate, not the underlying folding operation.

Actual products are in drawer-continuations.txt. Further local use: a new seed “A clean circle remained on the dusty shelf” becomes “She centered the cup on the circle, then moved it aside and used the rim of light to place the next one.” The trace becomes a spacing guide in the written continuation. This is performed generation, not observed human action. It also reveals overlap with CRTV-01’s already established use of material traces and UNX-01’s physical staging. The requested product is made, but repeated concept credit is withheld.'''
record('unx-02','Expand a material-absence reading into a present possible operation without resolving its hidden history.','A missing-box or memory continuation already fits the drawer seed; no evidence says it is a bad reading.',body,'A concrete folding-to-outline continuation and a further spacing-guide scene were produced while the conventional reading remained available.','The creative artifacts satisfy the current need, but the beneficial interpretation shift substantially repeats established material-trace and physical-staging operations. No new KEEP credit.','REJECT','Place the exact seed with the finished variants; retain the technique audit behind them. No hidden correct interpretation is selected.','Try an action trace rather than material residue; invite actual reader response only if supplied; examine whether a genuinely new operation survives the local novelty boundary.')
seqs={'first':'AABB','second':'ABAB','third':'BBAA'}
from collections import Counter
out={k:{'sequence':v,'counts':dict(Counter(v)),'adjacent_changes':sum(a!=b for a,b in zip(v,v[1:])),'runs':[len(list(g)) for _,g in __import__('itertools').groupby(v)]} for k,v in seqs.items()}
(D/'sequence-attention-products.json').write_text(json.dumps(out,indent=2))
body='''Exact input: three four-symbol blocks AABB, ABAB, BBAA. Goal: offer a structurally different description of their organization while preserving exact strings; no block is declared erroneous. The obvious comparison already sees that ABAB alternates and AABB/BBAA form pairs. I do not pretend a simple visual comparison missed this.

Known-optimal check: the descriptive goal has no single optimal representation. If the goal were merely count A and B, direct counting is already sufficient and should remain. The present task permits additional organization views without changing count truth.

Layer 1 — Obvious baseline: state the exact blocks and compare symbol order. Each has two A and two B; ABAB alternates. This already answers a basic organization question accurately.

Four selected disruptions: first-answer rejection preserves that answer; domain transfer takes run segmentation from a score (contiguous repeated marks as held notes); assumption elimination removes “the symbol is the only unit” and separately “the first symbol must anchor comparison”; scale shift compares what remains usable when twenty repeated blocks replace one, then returns to these exact four-character cases.

Layer 2 — Three candidates:

'''+table(['Candidate','Structural difference','Feasibility and need','Conventionality/quality','Outcome'],[
['Describe boundaries as stay/change events','Transforms four symbols into three transition relations.','Computed AABB has one change, ABAB three, BBAA one; exact strings retained.','Transition counts are conventional; useful but cannot be called expert-surprising.','Retain as baseline-adjacent, no novelty claim.'],
['Read equal-symbol runs as held durations','Changes unit from symbol to contiguous segment.','Computed run lengths [2,2], [1,1,1,1], [2,2].','Run-length encoding is familiar; a score metaphor alone does not make it unexpected.','Retain for a different answer family, no novelty claim.'],
['Create a reply that preserves counts but flips the place where attention turns','Construct a new block as a response to structure, not a description of the old block.','For AABB, answer ABBA: same counts, changes2, run lengths[1,2,1]; exact original remains.','The specific paired response is locally generated from both count preservation and a new center; not a claim that an expert lacks such a general operation.','Survives as the exact creative candidate.']])+'''

Replacement after the first two conventional candidates: the third response is built, not merely renamed. It combines a fixed inventory with a moved structural center, yielding the concrete pair AABB→ABBA. The discomfort check is an editorial observation about the generated form, not a claimed affective experience of a model or person. The quality gate accepts the exact form as local divergence; wider expert surprise is unmeasured.

Layer 3 — Reframe: rather than “which block is wrong?”, ask “which structural relation should a reply preserve, and which can it change?” This preserves the input’s absence of an error criterion. The output now contains both descriptions and a built response. It does not claim that choosing a new answer family disproves an earlier correct count.

Actual further use: BBAA→BAAB likewise preserves two of each symbol while moving the paired segment to the center. This is a new concrete generated reply. The adjacent-change and run calculations for the original inputs are saved in sequence-attention-products.json. Local products differ, but the original visual baseline already recognized the main organization difference; no improved decision or human attention benefit is observed. The general move to alternative representations is already established in this corpus, so a transformation claim here would overcount.'''
record('unx-03','Make a different unit of attention available for short symbolic patterns while preserving the declared descriptive goal.','The ordinary visual comparison already identifies alternating versus paired blocks; a new representation must add a real use beyond redescribing that fact.',body,'Run, transition and response views were built, including exact AABB→ABBA and BBAA→BAAB replies.','Distinct creative operations are available, but no additional beneficial mind change beyond existing representation/continuation practices is established in this case.','REJECT','Keep exact strings next to transformations so no compressed answer silently replaces a richer answer family.','Use the transition view on a task that actually asks about changes; test a count-only query where the added view is unnecessary; retain the creative reply without claiming it is the correct pattern.')
