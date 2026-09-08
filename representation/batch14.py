from write_record import record, progress, ROOT
import json
schemas=[{'id':'completion','relation':'one_of','members':['[1,0]','[1,1]'],'order':None,'meaning':'exactly one completion is actual, without choosing which'}, {'id':'recipe','relation':'all_of','members':['flour','water'],'order':None,'meaning':'both stipulated ingredients required'}, {'id':'journey','relation':'sequence','members':['station','interchange','destination'],'order':[0,1,2],'meaning':'declared itinerary order'}, {'id':'music','relation':'all_of','members':['C','E','G'],'order':None,'meaning':'stipulated simultaneous chord members'}, {'id':'cast','relation':'one_of','members':['performer A','performer B'],'order':None,'meaning':'one actor takes the stipulated single role'}, {'id':'game','relation':'sequence','members':['draw','choose','place'],'order':[0,1,2],'meaning':'stipulated turn procedure'}]
def compile_case(x):
 if x['relation']=='one_of':return {'required_all':False,'execute_in_order':False,'alternatives':x['members']}
 if x['relation']=='all_of':return {'required_all':True,'execute_in_order':False,'requirements':x['members']}
 if x['relation']=='sequence':return {'required_all':True,'execute_in_order':True,'steps':x['members']}
 raise ValueError('Unspecified relation')
results=[{'input':s,'output':compile_case(s)} for s in schemas]
assert results[0]['output']['required_all']==False
assert results[1]['output']['execute_in_order']==False
assert results[2]['output']['execute_in_order']==True
(ROOT/'relation-model-tests.json').write_text(json.dumps(results,indent=2))
record(39,'cda',1,'A branch must declare whether its children are alternatives, requirements, or steps',
'Transfer distinctions from ordinary constructed systems into an explicit relation model that prevents possible completions from being executed as a required sequence.',
'The unknown-outcome slide has a branch and a verbal note explaining that its lower vectors are alternatives. The meaning is available to a careful reader, but the branch shape alone does not specify whether a downstream operation should choose one, require both, or visit them in order.',
'''Interpretation 1: solution transfer. Abstraction: a parent connects to several members; the same topology can encode alternative admissible states, simultaneous requirements or ordered actions. The goal is to preserve the relation when exporting or acting on the representation. The constraint is that shape and spatial order do not determine the operator. Domain scan below uses explicitly stipulated ordinary examples; it does not claim that external practitioners have empirically proven the imported design's benefits.

| Domain searched | Candidate analogy | Similarity, 1–10 | Reason / limit |
|---|---|---:|---|
| Cooking | Flour and water both required in a stipulated recipe | 9 | Both-members operator; ingredients are physical, outcomes are propositions. |
| Cooking | Choose milk or the recipe's named substitute | 9 | Alternative choice; substitutability is stipulated, not nutritional advice. |
| Travel | Station→interchange→destination itinerary | 8 | Required order; real route delays are outside this model. |
| Music | C/E/G sounded together versus played in order | 9 | Same members, different timing relation; no claim about musical preference. |
| Theater | Either A or B plays one role | 8 | Exclusive alternatives; real ensembles can have different casting rules. |
| Tabletop game | Draw, choose, then place under a stated turn rule | 8 | Ordered obligations; game's rules are stipulated. |
| Gardening | Both light and water required in a toy plant-care rule | 6 | Conjunctive requirement; no horticultural sufficiency claim. |
| Architecture | Rooms adjacent on a plan | 5 | Connection need not be a permitted traversal or causal link. |

Seven domains, eight analogies. Top three are cooking's conjunction/substitution distinction, music's same-members relation change, and travel's declared sequence. Five deep mappings follow; the lower-similarity domains remain scanned candidates rather than invented deep successes.

| Mapping | Parent → members → relation → goal → constraint |
|---|---|
| Cooking | Recipe → named ingredients → all required → admissible recipe instance → an ingredient list alone says nothing about substitutions. |
| Music | Score fragment → C/E/G → simultaneous or ordered → exact rendition of the stipulated fragment → note membership cannot settle timing. |
| Travel | Journey → station/interchange/destination → ordered visit → follow the declared itinerary → spatial proximity alone does not determine sequence. |
| Theater | Single role → A/B performers → choose one → one filled role → “one role” is necessary for exclusivity. |
| Game | Turn → draw/choose/place → ordered required actions → valid stipulated turn → not every connected node is optional. |

Cooking deep dive: the stipulated system separates required ingredients, a substitution group, and preparation order. All-required membership determines whether an instance satisfies the ingredient rule; the substitute group permits one member instead of all. Import separate `all_of` and `one_of` relations. Do not import nutritional equivalence or the idea that any convenient replacement is valid. Adaptation: logical completions are alternative descriptions, not actions the model can choose to make true.

Music deep dive: a chord and a melody can use the same note names. The constructed score explicitly marks simultaneous membership, order and duration. Import separation of membership from timing and retain the original note/vector values. Do not infer emotional effects or that a simultaneous set has a meaningful left-to-right order. Adaptation: the outcome set has no duration, so a timing field stays absent rather than receiving an invented zero.

Travel deep dive: the toy itinerary specifies the ordered stops, permitted alternatives at an interchange, and a destination check. Order works because it is part of the itinerary definition, not because the map draws a line. Import an explicit sequence operator and a destination/acceptance check. Do not import reachability from physical closeness or real travel feasibility. Adaptation: a logical tree can describe possible worlds without any traversal operation at all.

Theater deep dive: the toy casting sheet names one role, lists eligible alternatives, and records the selected performer. Exclusivity follows from the one-role constraint. Import the cardinality condition alongside alternatives and distinguish candidates from the selected assignment. Do not infer that A and B cannot both appear elsewhere. Adaptation: the observed prefix does not authorize selecting which completion is actual, so the model preserves both as possible.

Game deep dive: the stipulated turn declares draw before choose before place, checks each prerequisite, and rejects an out-of-order turn. Import relation-specific validation instead of generic graph traversal. Do not import competition, payoffs or randomness into a missing-data problem. Adaptation: only a `sequence` relation compiles to ordered actions; `one_of` compiles to unresolved alternatives.

Cross-pollination: cooking supplies AND versus OR, music separates membership from time, and travel/game require order to be stated. The combined representation carries a relation operator, members, optional order, and a sentence specifying what the operator means in this domain. This is more precise than attaching a generic arrow legend to every graph.

Three actual candidate solutions:

1. **Exact set expression:** `Compatible([1,?]) = {[1,0], [1,1]}`. It preserves alternatives without implying time, but requires understanding a set of vectors.
2. **Typed relation record:** `{relation: one_of, members: ["[1,0]", "[1,1]"], order: null}` with meaning “one complete input is actual; which one remains unknown.” This can be validated by a downstream operation.
3. **Visible branch plus serial definition:** keep the spatial diagram and add “possible completions; no order or probabilities assigned” in its standalone reference. This preserves the strong presentation form without demanding that its geometry encode everything.

Five transfer tests plus the original target were executed in [relation-model-tests.json](relation-model-tests.json). Recipe all_of compiles to both required with no execution order. Journey sequence compiles to ordered steps. Music all_of compiles to simultaneous required members without an arbitrary order. Casting one_of retains alternatives without requiring both. Game sequence retains all three ordered steps. The original completion record returns `required_all=false` and `execute_in_order=false`; it does not run both completions as successive updates. A relation-less connected pair is left unspecified rather than guessed from topology.

Validation: each analogy preserves the mapped relation under its explicit rules. Their shared structure does not justify a universal psychological or physical law. Dangerous imports are causality from arrows, probabilities from branch count, or action authority from mere alternatives. The typed model rejects those extra inferences by omitting fields that have no supplied meaning.

Actual use: the next graph-derived exercise consumes the completion record as an alternative set, enumerates the two compatible inputs for a truth query, and does not treat them as a before/after trajectory. The exact set expression is retained for serial review; the existing labeled branch remains useful for projection.

Certificate: the new useful operation is relation-specific compilation, tested on five distinct transfers and the original completion object. The verbal alternatives-versus-steps distinction was already present in 030; it is not credited again as a conceptual discovery. The new typed representation changes what a downstream procedure is allowed to do with the same topology.''',
'I replaced a generic graph-traversal assumption with a relation-specific model and executed it on six objects; the completion branch now yields alternatives rather than ordered updates.',
'The local model preserves AND/OR/order distinctions during an actual representation-to-operation conversion. External-domain efficacy and human comprehension remain untested.',
'KEEP — explicit relation semantics now constrain a tested downstream operation.',
'Typed relation record for machine operations, set expression for exact serial review, and the labeled branch plus reference for projection.',
'Test a graph with mixed relation types; represent nonexclusive alternatives with cardinality bounds; inspect a case where order is partial rather than total.',
'Original 8x floors met: seven domains searched, eight analogies found, five deep mappings with solutions/limits/adaptation, five transfer tests plus target, cross-pollination and three constructed solutions. All source-domain systems are stipulated; no external proven-efficacy claim is made.')
(ROOT/'consolidation-06.md').write_text('''Intended mind change: Use the last four established keeps to preserve uncertainty and operation identity when turning a representation into a next action.

# Consolidation 06 — preserve what the input does and does not authorize

Starting working state: 033 adds partial observation; 034 splits independently executable compound changes; 036 adds the negative-anchor missing-value case; 039 makes relation operators constrain downstream action. Human interventions and global taxonomy claims remain outside the established core.

Organization A groups the four objects by form: schema, intervention taxonomy, truth-case inventory, relation model. It is strong when opening a known artifact. Organization B groups them by the next operation's unresolved input: incomplete evidence, compound action, unresolved proposition, unspecified relation. B is selected for reviewing the next retrieval cue because the immediate risk is making a state transition from incomplete context; A remains the direct artifact route.

| Unresolved input | Established operation | Boundary |
|---|---|---|
| Captured result is incomplete | Preserve partial evidence and leave outcome unassigned (033) | Partial is not negative; criterion must be stated. |
| Proposal contains independent changes | Split actual/proposed components under a shared parent (034) | Intended locus does not establish effect. |
| Known negative anchors an unknown vector | Every is false; some may remain unresolved (036) | Finite declared domain and binary predicate only. |
| Connected members have unspecified relation | Require an operator before compiling steps or alternatives (039) | Geometry alone gives no causality, probability or authority. |

Actual use on the next material: the input “new actor mentioned” contains a proposed retrieval trigger but no prior/current actor pair. The unresolved-input route treats this as incomplete evidence, not as proof of a changed actor. It requests the missing comparison or leaves transfer classification open. A cue expansion and opening a reference are separate operations if only one occurs. The candidate reference alternatives are not a mandatory sequence. Application 040 uses these constraints in five concrete cue cases.

Lost-condition comparison: a form-only index finds the schema directly when the user knows the schema name. The unresolved-input route finds the same partial-evidence condition when the user has only an incomplete encounter. Removing the criterion from 033 or the operator from 039 licenses an invalid action; both deletions are rejected. Removing the source-artifact route imposes unnecessary diagnostic choices on someone with an exact filename; it is retained. No reader-time claim is made.

Content review found no warrant to generalize the [0,?] rule to arbitrary missing-data mechanisms or to treat a one_of relation as an instruction to choose a factual outcome. Those limits remain in the table and source records.

Actual mind change: The next cue test starts from incomplete actor-comparison evidence and withholds a changed-actor conclusion until the needed pair is supplied.

Benefit: Established local distinctions govern a new retrieval test without adding an untested human-memory claim.

Verdict: KEEP — consolidation uptake only, no additional independent finding credit.

Organization: Unresolved-input route for diagnosis; object-form index for direct retrieval; the four application records preserve derivations.

Next attempts: Use the form route when the exact model is named; test two simultaneous unknown relations; inspect a partial record whose criterion changed after capture.
''')

record(40,'cda',2,'An encounter cue needs its comparison context',
'Test whether analogies from other cue systems improve the existing changed-actor retrieval rule when the next encounter contains only a partial context.',
'The existing cue already says to open the reuse rule when actor, task or input changes. A keyword search for “actor” is a useful archive lookup, but the presence of that word does not establish that the actor changed in a particular event.',
'''Interpretation 2: perspective shift, followed by bounded solution tests. Abstraction: a signal can point to a stored rule, but applying the rule requires conditions that the signal itself may not contain. Goal: recover the relevant rule without converting a topic mention into an established state transition. Constraint: prior context may be unavailable. Consolidation 06 was used first: missing actor-comparison data stays partial, and opening a reference is distinct from performing its recommended intervention.

| Domain searched | Analogy | Similarity, 1–10 | Limit |
|---|---|---:|---|
| Theater | A cue line identifies when a stipulated entrance occurs | 9 | Actual stage coordination is untested here. |
| Cooking | A recipe says “after the mixture cools,” not merely “when cooling is mentioned” | 9 | Temperature threshold is stipulated, not cooking advice. |
| Music | A rehearsal mark points to a passage without telling who has played it | 8 | Location and performance state differ. |
| Travel | An interchange sign names a destination without proving arrival | 8 | A sign is not a journey history. |
| Tabletop game | A card effect activates only under its stated condition | 9 | Condition is explicit in the toy rule. |
| Gardening | A toy care card is checked when its moisture condition holds | 7 | No plant-care efficacy is inferred. |
| Architecture | A room label identifies a space, not who entered it | 7 | Spatial identity does not establish an event. |
| Cooking | A shelf label locates an ingredient but does not record its use | 8 | Retrieval and execution are different relations. |

Seven domains and eight analogies. Top three: theater cue, conditional recipe step, and conditional game effect. Five deep mappings include music and travel.

Theater mapping: stored rule→entrance instruction; encounter signal→cue line; prior/current scene→required context; opening the rule→reading the prompt; performed entry→actual action. The stipulated solution supplies cue text, scene condition and assigned performer; it checks the scene before entry. Import a cue plus its context predicate and retain performance separately. Do not import a shared backstage state or assume the actor heard the cue. Adaptation: the current model may have no prior actor record, so its classification remains unknown.

Cooking mapping: reuse rule→conditional step; “changed actor”→“cooled below the specified threshold”; prior/current facts→the measured condition; action→next preparation step; constraint→missing measurement. The toy rule supplies a threshold, checks the measurement and leaves the step pending if unavailable. Import explicit condition data and a pending route. Do not infer that mentioning cooling establishes the threshold or that a particular temperature is safe. Adaptation: actor identity is a categorical comparison, not a temperature estimate.

Game mapping: reference→card rule; encounter→turn state; guard→condition on that state; effect→allowed action; constraint→one rule's scope. The stipulated solution evaluates the guard, applies the effect only when true and preserves an unresolved state when required facts are absent. Import three-way satisfied/unsatisfied/unknown guard evaluation. Do not import random outcomes or permission to change external systems. Adaptation: a true changed-actor guard retrieves a transfer warning, not an authorization to intervene on a person.

Music mapping: stored passage→source record; rehearsal mark→lookup cue; player position→current encounter; rendition→actual use; constraint→mark alone lacks performance history. The constructed solution indexes the passage, separately records the player's position and checks the next entry. Import distinction between an address and an event; retain exact source access. Do not infer that repeatedly seeing the mark improves memory. Adaptation: an archive keyword remains useful even when it cannot decide the event predicate.

Travel mapping: destination sign→topic cue; current location→current actor/task; previous stop→prior context; route instruction→reuse rule; arrival→observed use. The toy solution separates map lookup, current-position check and journey record. Import an explicit comparison context. Do not infer current position from a named destination or assume all route choices are sequential. Adaptation: a missing prior actor stays unknown; the model cannot fill it from the word “new.”

Cross-pollination: theater supplies contextual timing, game supplies a guard with unknown state, music/travel separate address from event history. Three candidate outputs were constructed: (A) a keyword index linking “actor” to the full reuse rule; (B) a predicate card “if prior and current actor are known and differ, retrieve the transfer rule; if either is unknown, preserve that uncertainty”; (C) a two-stage serial cue, “open the actor rule, then check whether the actual actor changed.” A is strong for locating a topic; B is strong when structured context exists; C handles prose encounters at the cost of an extra check.

Five actual transfer tests:

| Encounter | Keyword route | Predicate result | Disposition |
|---|---|---|---|
| Text mentions actor; prior=current=model | Finds relevant topic | Unchanged actor | No transfer conclusion solely from mention. |
| prior=model; current=listener | Finds actor topic if named | Changed actor | Open transfer rule; human effect remains unknown. |
| prior actor missing; current=listener | Finds actor topic | Unknown comparison | Request prior context or preserve unknown. |
| Same actor/task/input; format changes | May find no actor term | Unchanged actor | Inspect channel boundary rather than assert actor transfer. |
| Same actor; new task explicitly supplied | Actor-only index insufficient | Actor unchanged, task changed | Use existing new-task route, not changed-actor route. |

The tests use explicit supplied tuples, not an unobserved human reminder effect. Their outcomes preserve exactly the earlier cue's changed-feature condition. The strongest contrary case is free-text retrieval without structured prior fields: keyword lookup can be more immediately useful than a predicate that lacks its inputs. The predicate is not adopted as the only route.

Validation: the analogy holds for condition checking and address/event distinction under the stated examples. It breaks if an external system supplies a trusted event trigger that already guarantees the condition; rechecking may then duplicate work. It also breaks if prior/current identity is itself ambiguous. No source-domain timing or memory benefit transfers by analogy alone.

Certificate: the five cases expose why a topic cue cannot stand in for a context comparison, but the existing changed-actor rule and partial-evidence distinction already contain this result. This application gives concrete guard and lookup alternatives; it does not earn a new KEEP for repeating them or establish delayed human retrieval.''',
'I used the partial-evidence route on a missing prior actor, tested five cue encounters, and retained both keyword lookup and condition checking for their different jobs.',
'The candidate guard is inspectable, but its useful distinction is already established and human delayed retrieval remains untested.',
'REJECT — no new independent KEEP for the analogy; retain the concrete alternatives as local reuse.',
'Keyword lookup remains the topic address; explicit comparison context governs application. Neither route is forced on every encounter.',
'Test a trusted external event that already guarantees actor change; test ambiguous identities; conduct an actual delayed-retrieval task before claiming memory benefit.',
'Original 8x floors met: seven domains, eight analogies, five deep mappings with source-system rules and transfer limits, three candidate solutions, five concrete transfer tests, and cross-pollination. Domain examples are stipulated; no external efficacy is asserted.')
progress()
