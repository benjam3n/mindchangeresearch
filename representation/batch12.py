from write_record import record, progress, ROOT
import json,itertools
cases=[('A narrated counterexample','Perception','Reasoning'),('A pause before a choice','Attention','Choice'),('A cue opened when actor changes','Memory','Action'),('A label expanded into a definition','Reasoning','Perception'),('An optional method catalog','Choice','Attention'),('A restructured dependency graph','Reasoning','Action'),('A familiar example used as a reminder','Memory','Reasoning'),('A color label copied into text','Perception',None),('A retained stop option','Choice','Action'),('A reference reopened for a new input','Memory','Action'),('A contrastive unknown completion','Reasoning',None),('A scheduled point to reconsider','Attention','Memory')]
over=sum(x[2] is not None for x in cases);me=(1-over/len(cases))*100;score=(me+100)/2
record(35,'mv',1,'Mind-change loci are useful perspectives without being exclusive buckets',
'Test whether the six locus labels can support exclusive counting, and preserve their useful overlap if forcing a partition would hide a real intervention relation.',
'The broad labels perception, attention, memory, reasoning, choice and action guide search. They have not been established as mutually exclusive or as collectively exhaustive of all changes.',
'''Interpretation 1: validate an existing breakdown. Structure: six categories and twelve declared fixture interventions; target perfect MECE only if these labels will be used as counting buckets. They currently function as search perspectives. The actual observed object is the classification, not any human intervention effect.

| Fixture | Primary search perspective | Also fits | Overlap |
|---|---|---|---|
'''+ '\n'.join(f'| {a} | {b} | {c or "None identified"} | {"Yes" if c else "No"} |' for a,b,c in cases)+f'''

Mutual exclusivity: {over}/{len(cases)} fixtures have more than one defensible label, an {over/len(cases)*100:.2f}% overlap rate; local ME score {me:.2f}%. All twelve fixtures were checked. Splitting “narrated counterexample” into channel and content records can isolate direct operations, but it does not make the effects of each operation exclusive. Assigning a primary label by declared intent is possible for a counting convention; secondary relationships must remain accessible. Merging all six categories would eliminate overlap by erasing the distinctions that made the list useful. Accept overlap for perspective search.

Collective exhaustiveness: each of these twelve fixtures has at least one label, so fixture coverage is 12/12=100%. This is not coverage of all possible mind changes. Known dimensions outside the six labels include the actor's criterion, social coordination, available resources and physical setting. Some can influence the six processes, but influence is not identity. No defensible size of the unrestricted universe is available; a global gap percentage or global CE score would be fabricated.

| Edge probe | Present in fixture list? | Disposition |
|---|---|---|
| Minimum: no intervention performed | No | Add a separate performance state, not a seventh mental locus. |
| Boundary: compound timing and content change | Partly | Use atomic operation children under 034; retain multiple intended loci. |
| Negative: source checksum | No | Exclude from mind-effect evidence; it is provenance. |
| Historical: prior reference reopened | Yes | Preserve the old observation and new use separately. |
| Future: a proposed sensory channel not yet available | No | Proposed channel remains untested; do not invent a new observed outcome. |
| Edge actor: another participant | No | Add actor scope to the record, not a presumed effect category. |

What's missing brainstorm, explicitly model-generated rather than expert testimony: a domain specialist might add emotional appraisal or bodily state; a contrarian might ask whether deliberate non-change preserves a useful state; an adjacent organizational view would add authority and coordination. These possibilities challenge global exhaustiveness but do not establish the actual incidence or causal effects of those changes.

Source-requested numerical summary, restricted to the declared fixture universe: ME={me:.2f}%, CE=100%, mean={score:.2f}%. Under the source's aggregate bands this is “Good Enough”; under its strict overlap thresholds it is “Needs Work.” The source's two scoring conventions therefore diverge on this case. The actual recommendation follows the substantive 83.33% overlap, not a flattering averaged label. For an unrestricted domain, CE and the overall score are unknown.

Actual revised representation: retain these six as multi-select search facets. For exclusive counts, use direct atomic operation category plus a declared primary intended locus and secondary tags, as in 034. On “pause before choice,” direct operation=retime, primary intended locus=choice if that is the stated aim, secondary=attention. The record no longer implies attention and choice are mutually exclusive changes. On “source checksum,” no mental-effect category is assigned at all.

Certificate: the twelve inspected fixtures refute the exclusive-bucket interpretation of these six perspective labels. The strong alternative—declare a primary coding convention—works for a particular count but does not establish an ontology. The practical repair mostly applies already-established faceting and actor/evidence boundaries, so no new KEEP is credited.''',
'I rejected exclusive counting by the six broad loci and retained a primary-plus-secondary coding convention for one pause/choice case.',
'The check prevents a misleading category claim. Its repair repeats existing faceting and scope distinctions rather than establishing a new independent benefit.',
'REJECT — the proposed MECE claim and extra KEEP credit fail; the perspectives remain useful.',
'Use multi-select locus search and separate atomic-operation counts; report finite fixture coverage separately from global completeness.',
'Test an emotional-appraisal intervention with a real criterion; classify an inseparable compound; validate a strictly defined finite action vocabulary.',
'Full structure, all twelve overlap checks, dimension and six edge probes, missing-item brainstorm, scoped scores, source-band conflict, recommendations and two actual classifications. No numeric 8x floor is defined in the original.')

inventory=[('Mixed observed [1,0]','Distinguish not every from none','complete','high'),('Positive plus unknown [1,?]','Preserve some while every is unresolved','complete','high'),('Empty domain []','Expose the logical convention','partial','medium'),('All-positive singleton [1]','Show every and some can agree','missing','medium'),('All-negative singleton [0]','Separate none from not every','missing','medium'),('Negative plus unknown [0,?]','Every false while some unresolved','missing','critical'),('Only unknown [?]','Both universal and existential unresolved','missing','high'),('Uncertain membership of a known negative','Separate denominator uncertainty from outcome uncertainty','partial','high')]
def truth(vec):
 vals=[[]]
 for x in vec: vals=[v+[a] for v in vals for a in ([0,1] if x=='?' else [x])]
 def v(fn):
  z={fn(a) for a in vals};return 'true' if z=={True} else 'false' if z=={False} else 'unresolved'
 return [v(all),v(any),v(lambda a:not any(a)),v(lambda a:not all(a))]
truthrows=[]
for v in [[1,0],[1,'?'],[],[1],[0],[0,'?'],['?']]:truthrows.append({'input':str(v),'every':truth(v)[0],'some':truth(v)[1],'none':truth(v)[2],'not_every':truth(v)[3]})
# Membership alternative is [1] or [1,0], a different source of alternatives.
truthrows.append({'input':'[1] or [1,0] by membership','every':'unresolved','some':'true','none':'false','not_every':'unresolved'})
(ROOT/'logical-category-fixtures.json').write_text(json.dumps(truthrows,indent=2))
record(36,'ctgp',1,'The missing negative-plus-unknown case reverses which claim is settled',
'Complete a bounded logical exercise inventory by identifying missing truth-pattern cases and adding the one that distinguishes known falsity from unresolved existence.',
'The teaching specimen uses [1,0] and [1,?], with an empty-domain caveat. It is sufficient for its three displayed concepts. It does not yet cover a case where every is already false while some remains unresolved.',
'''Category: finite binary outcome examples for understanding every, some, none and not-every under incomplete information. Scope includes stipulated small domains, unknown values and one uncertain-membership case. Causal claims, probabilities and human learning effects are excluded. Completeness means the eight selected instructional distinctions below, derived from truth conditions and the live missing-information task; it does not mean every possible vector length.

| Ideal item | Purpose | Current status | Importance of gap |
|---|---|---|---|
'''+ '\n'.join(f'| {a} | {b} | {c} | {d} |' for a,b,c,d in inventory)+'''

Current inventory has four existing entries: two complete cases and two partial caveats. Complete coverage is 2/8=25%; presence including partial entries is 4/8=50%. These denominators concern the eight-case ideal, not all research coverage. The slide about changed criteria is extra relative to this narrow category: KEEP in the presentation because it serves a different stated goal, not remove it to make the inventory look pure.

Diff: four missing complete cases, two incomplete explicit evaluations, two already complete; gap count six. Priority 1 is [0,?], because carrying the positive-unknown example's conclusion over would wrongly leave every unresolved. Priority 2 is uncertain membership, because an unknown denominator must not be mislabeled an unknown observed value. Priority 3 is [?], because no known result anchors either quantifier. Add next the empty-domain truth table, then the positive and negative singleton anchors. Skip larger duplicate vectors for this target when they add no new distinction; keep them as later transfer possibilities.

Actual additions and evaluation:

| Input | Every | Some | None | Not every |
|---|---|---|---|---|
'''+ '\n'.join(f"| {r['input']} | {r['every']} | {r['some']} | {r['none']} | {r['not_every']} |" for r in truthrows)+'''

These outputs were computed by enumerating both 0/1 completions of each `?`. The empty-domain row uses standard finite conjunction/disjunction conventions: all([])=true, any([])=false. That convention is stated rather than smuggled in from a nonempty example. The membership row instead compares two admissible domains, [1] and [1,0]; the negative is known when included, and uncertainty concerns whether it belongs.

Actual later use inside this application: given the first observed result 0 and a missing second result, the updated exercise returns every=false immediately. It requests the second outcome only to settle some/none. The old [1,?] cue would have requested the second outcome to settle every. This changes which question is already answered and which missing value matters; it is a substantive new case, not a reformatted caveat.

Strong alternative: retain only the three-slide specimen for a short projected introduction. Its smaller scope is legitimate. The expanded inventory is selected for constructing and checking a transfer exercise, where both signs of an observed anchor matter. No claim is made that eight examples improve human learning over two.

Certificate: the completion sets for [0,?] are [0,0] and [0,1]; every is false in both, while some differs. This establishes the local change in inference. Contrary: the underlying quantifier distinction already exists; the newly useful finding is the asymmetric missing-data question exposed and used by this unrepresented case.''',
'I added and executed the missing cases, then used [0,?] to settle every as false while withholding some and none.',
'The local exercise now distinguishes two asymmetric unknown-value situations and requests the missing result for the correct proposition.',
'KEEP — new negative-anchor case changes the local inference and missing-information request.',
'The eight-case reference is a transfer/checking inventory; the sparse presentation remains an introduction with a narrower purpose.',
'Test mixed positive and negative anchors with several unknowns; change the eligibility of a known negative; compare a reader’s answer before and after the new case.',
'All five original steps executed: bounded category and derivation, eight-item ideal, actual complete/partial inventory, missing/incomplete/extra diff, priorities, concrete additions and later inference use. Original has no numeric 8x floor.')
progress()
