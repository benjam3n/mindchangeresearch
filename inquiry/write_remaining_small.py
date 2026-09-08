from pathlib import Path
import json
R=Path('/workspace/scratch/78b838bd97fc/mind-change-research/inquiry')

def put(name,text): (R/name).write_text(text.strip()+'\n')
def end(change,benefit,verdict,org,nexts):
 return f'\n\nActual mind change: {change}\nBenefit: {benefit}\nVerdict: {verdict}\nOrganization: {org}\nNext attempts: {nexts}\n'
def aex_table(groups):
 types=['Causal','Existence','Stability','Access','Capability','Value','Knowledge','Resources','Permission','Timing'];out=['| ID / core | Type | Necessary assumption for the stated version | Hiddenness / risk | Testability and finding |','|---|---|---|---|---|']
 for j,group in enumerate(groups):
  for i,(claim,hid,risk,test) in enumerate(group):out.append(f'| A{j*10+i+1} / C{j+1} | {types[i]} | {claim} | {hid} / {risk} | {test} |')
 return '\n'.join(out)
groups=[
[
('Serialization preserves the two operands rather than merging values.','Deep','High','Now: compare independent operands with shared scalar.'),
('There are two endpoint occurrences, not one unary predicate.','Shallow','High','Tested: sure and maybe source/target fields.'),
('Endpoint meanings do not silently change between stored and evaluated records.','Deep','High','Now: freeze source bytes; interpretation remains a separate object.'),
('The display exposes both endpoint definitions.','Shallow','Medium','Tested: methods overlay contains both question identity and target definition; sure definition retrieved in QR01.'),
('The consumer can represent unequal proposition/time values without overwriting either.','Buried','High','Now: single scalar scope cannot encode P and Q without an additional convention.'),
('Lossless scope for this query is more useful than the shortest row.','Deep','Medium','Now: exact query asks whether scopes differ; compact literal lookup has a different objective.'),
('The consumer knows which endpoint a scope value qualifies.','Buried','High','Now: shared time=t does not specify two unequal times.'),
('The added paired record fits the available file and display.','Surface','Low','Tested: eight-edge overlay and one instance are small; no human reading-time inference.'),
('A derived annotation may be added without rewriting the archived source.','Surface','Medium','Tested: working instruction authorizes analyses in inquiry.'),
('The annotation is inspected before drawing the relation verdict.','Deep','Medium','Now: the later compatibility test below consumes paired operands first.')],
[
('The exclusion rule is triggered by semantic incompatibility, not simply a tag match.','Deep','High','Tested: existing generator uses tags; that is not this stronger semantic rule.'),
('A common probability value p exists for the stipulated exact same proposition.','Shallow','High','Formal fixture: p in [0,1], not a measured human probability.'),
('Both predicates use the same interval and event at the same time.','Deep','High','Now: frozen fixture aligns these before testing meanings.'),
('The intended sense of maybe can be recovered from evidence or declared for the fixture.','Deep','High','Source defines chance; author pragmatic intent still unresolved.'),
('A compatibility checker can intersect the two allowed probability sets.','Shallow','Medium','Tested below: finite cases plus endpoint algebra.'),
('False exclusions cost more than preserving a live semantic ambiguity in this inquiry.','Surface','Medium','Normative: user asks to reopen foreclosed possibilities; adopt locally, not universal.'),
('Maybe means 0<p<1 rather than merely p>0 for the proposed contradiction.','Buried','High','Now: p=1 refutes contradiction under positive-possibility sense.'),
('The relevant context that licenses the strict upper bound is available.','Deep','High','Not present in export; no fabricated speaker context.'),
('The model may declare the source intended the strict sense.','Buried','High','Rejected: analysis authority does not supply missing source intent.'),
('The certainty and possibility assessments refer to one time.','Shallow','High','Tested by fixture, historical general use unknown.')],
[
('Editing a definition changes the code path that emits the edge.','Buried','High','Already falsified in CSCL27; imported finding.'),
('A generator consumes definitions for this contradiction family.','Deep','High','Already falsified: isolated rule uses tags.'),
('The same rule still governs the code revision being assessed.','Deep','Medium','Current exact receipt only; no claim about all versions.'),
('The generator source is available rather than guessed from output.','Shallow','High','Tested: authentic generator receipts.'),
('The repair process can alter the actual emitting condition in a derived test.','Shallow','Medium','Yes in isolated fixture; production repository not changed.'),
('The repair objective is semantic eligibility rather than prettier definitions.','Surface','High','Declared objective; literal wording improvements would be a different aim.'),
('The author intended a strict probability interpretation for every uncertainty tag.','Buried','High','No supporting source; threatening and unknown have other definitions.'),
('Review effort can inspect a small set of semantic cases before generalizing.','Shallow','Low','Performed three probability cases and a cross-proposition instance.'),
('A tested replacement rule can be deployed to the original repository now.','Deep','High','No deployment is part of this assigned operation; local analysis only.'),
('A regenerated edge set, rather than only a saved definition, is the relevant later observation.','Deep','Medium','CSCL27 already measured the emitter; next test below is semantic, not historical regeneration.')]]
text='''Intended mind change: Determine whether the new scope overlay can represent two operands faithfully and whether aligned “sure” and “maybe” must contradict.

AEX 02 — paired operands and the upper endpoint

Starting working judgment: The methods dependency supplied a useful overlay with one shared scope object. I had accepted same-proposition/time plus sense clarification as the next test, without yet determining the exact endpoint difference between possibility and uncertainty. I did not assume every “maybe” occurrence means strict uncertainty. The concrete input is methods/sure-edge-overlay.json, the exact maybe definition (“is there a chance this could be true or happen?”), and the sure→maybe contradiction reason. The new question is whether the existing representation can encode and test these alternatives without inventing source intent.

Original: ../sources/inquiry-aex.original.md and separate requirements receipt. Interpretation 1: extract assumptions in a proposed argument/representation. Three core claims: C1 one shared scope tuple is sufficient for a binary relation query; C2 same-proposition sure and maybe are necessarily incompatible; C3 definition-only editing repairs the tag-generated contradiction. C3 is an imported rejected candidate, retained to ensure the earlier consolidation changes the actual control point considered.

All ten extraction questions were applied to each core. In each row, “necessary” qualifies that stated version or chosen method; irrelevant universal assumptions are not added to rescue a preferred verdict.

'''+aex_table(groups)+'''

Assumption map: C1 uses A1–A10; C2 A11–A20; C3 A21–A30. The priority roots are A17 (strict upper bound), A7/A5 (operand attribution/representability), and A21 (causal control point, already rejected). High-risk C2 is not rescued by assuming A17; it remains conditional.

Five-level recursive extraction, with five actual dependency edges: “The declared intersection test can certify universal incompatibility” requires “its interpreted predicates have empty intersection” (D1); D1 requires “no allowed p satisfies both” (D2); given sure(p) iff p=1, D2 requires “maybe(1) is false” (D3); given the two candidate senses here, D3 requires “the selected sense excludes p=1” (D4); selecting that sense as the source meaning rather than a stipulation requires “source/context evidence warrants the exclusion” (D5). D5 is a genuine unknown: the retrieved question defines a chance, and does not state the strict upper bound. This chain establishes a missing warrant; it does not supply one. Other roots: source bytes and the two endpoint occurrences are direct observations; normative loss preference is explicitly adopted for this task.

Testability: all serialization, predicate and code assumptions are testable now or already tested as stated in the table. Historical author intent and an unperformed future context are not currently verifiable; searched exact definition/reason and generator, found no strict-bound assertion. Closest proxy is the “uncertainty” tag, which is weaker than a probability definition. No human belief measurement exists. Priorities therefore place a present predicate intersection before speculative intent attribution.

Performed comparisons and later application: the shared scalar scope record cannot distinguish left=(P,t) and right=(Q,u) without introducing a new encoding convention; paired operands retain both. On an aligned instance, sure(p): p=1; possible(p): p>0; uncertain(p): 0<p<1. At p=0, none applies. At p=1/2, possible and uncertain hold but sure does not. At p=1, sure and possible both hold while uncertain does not. Thus even after fixing both operands to P,t, “sure contradicts maybe” fails under the chance/positive-possibility reading. It succeeds under the explicitly stipulated strict-uncertainty reading. The source intent remains unresolved. I wrote paired-semantic-instances.json and used it to decide the distinct next enumeration input: SE35 must retain the p=1 overlap case, rather than filtering it as a tag contradiction. This is an actual change to that prepared finite input, not an observed human effect.

Depth: 30 tabulated assumptions plus five nested warrant conditions; ten categories; five dependency edges; at least six Deep/Buried entries. Counts are lower bounds, not proof of relevance; each row names its test and scope. C1 is rejected for the scalar representation, retained for an explicitly paired extension. C2 is conditional on a meaning not supplied by the source. C3 remains rejected from prior evidence and earns no additional credit.
'''+end('The working semantic model now separates positive possibility (p>0) from strict uncertainty (0<p<1); operand alignment alone does not settle this route. The shared annotation is extended in a derived instance to preserve both endpoints.','The actual next finite enumeration retains a valid sure-and-possible case at p=1 that a strict-uncertainty substitution would exclude. This is a new current-case logical/representation benefit, not source-intent or human evidence.','KEEP','The original edge, source definition, each endpoint scope, stipulated predicates and tested verdict are distinct. The new semantic endpoint finding is K9; the paired representation supports it but is not counted as an additional keep.','Enumerate boundary cases in SE35; test related “perhaps” without assuming it equals maybe; inspect a same-time different-proposition case; compare semantic filters with the authentic tag emitter.')
put('33-aex-possibility.md',text)
inst={'source_edge':'sure→maybe','original_reason':'Certainty contradicts uncertainty','source_intent':'unresolved','instances':[{'id':'aligned-positive','left':{'question':'sure','proposition':'P','time':'t','sense':'p=1'},'right':{'question':'maybe','proposition':'P','time':'t','sense':'p>0'},'witness':1,'compatible':True},{'id':'aligned-strict','left':{'question':'sure','proposition':'P','time':'t','sense':'p=1'},'right':{'question':'maybe','proposition':'P','time':'t','sense':'0<p<1'},'witness':None,'compatible':False},{'id':'unaligned','left':{'question':'sure','proposition':'P','time':'t','sense':'p(P)=1'},'right':{'question':'maybe','proposition':'Q','time':'u','sense':'0<p(Q)<1'},'witness':{'p(P)':1,'p(Q)':.5},'compatible':True}],'se35_frozen_input':{'probabilities':[0,.5,1],'predicates':['p=1','p>0','0<p<1'],'retain_overlap_at_one':True}}
(R/'paired-semantic-instances.json').write_text(json.dumps(inst,indent=2)+'\n')
p=R/'08-spd-representation.md';s=p.read_text().replace('The GG dependency is pending and prevents completion of this application.','The exact-input GG/QAG/ARAW dependency is complete; the actual later test is recorded below.').replace('Dependency status: PENDING.','Dependency status: COMPLETE. The actual 301 guesses are in ../methods/gg-01.md and gg-01-guesses.json; all QAG and its required ARAW products are in gg-01-qag.md and gg-01-araw.md. No second independent GG exposure is counted for this reuse.')
s=s[:s.index('Actual mind change:')]+'''Distinct later application: AEX33 consumed the dependency’s sure-edge-overlay.json, checked the single shared scope tuple, and instantiated the sure→maybe edge with paired operands. The actual predicate intersection at p=1 distinguishes positive possibility from strict uncertainty and changes SE35’s frozen input. This specific finding is credited only in AEX33; the SPD application receives no additional KEEP for the same change. The dependency was useful input to the operation, but its marginal causal effect beyond already known scope distinctions is not isolated.

Actual mind change: The expanded representation search now feeds a performed semantic test; one overlay is used and amended rather than merely proposed.
Benefit: The dependent operation is concrete and inspectable. Its new semantic finding is recorded once in AEX33, and no separate beneficial effect is attributed to the size of the SPD/GG inventory.
Verdict: UNRESOLVED
Organization: The exact frozen input links to the original 301-guess dependency, completed upstream questions and ARAW registry, then to the one actual instantiation.
Next attempts: Use other candidates only where they distinguish a live question; preserve the compact literal lookup boundary; assess timing candidates on their separate input.
''';p.write_text(s)
