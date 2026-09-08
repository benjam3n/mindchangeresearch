from write_record import record, progress, ROOT
import json,itertools
record(32,'categorize',2,'Seven views do not support the required category split',
'Test whether the seven existing working views contain a qualifying hidden categorization before adding a new navigation layer.',
'The seven views have distinct useful jobs and are readable directly. A second category index might reduce search, but its categories must pass the original numerical and non-obviousness gates.',
'''Interpretation 1: inventory an explicit seven-file input. Full contents were read: routing-v1, selector-view-v1, serial-reuse-card, reuse-trigger-v1, and consolidations 01–03. The consolidation 05 production card was used: select the existing-item branch, retain a serial answer with the exact source condition, and test the failed-split possibility. `/gg` does not apply.

| Discovery source | Content found | Quality result |
|---|---|---|
| Names | Four named working views, three numbered consolidations | 4/3 split fails >3 in both groups; already visible from names. |
| Content | Broad selection/routing and more specific reuse/scope access | Plausible semantic distinctions, but no disjoint split can place at least four of seven in each group. |
| Relationships | Direct links and linked consolidation routes | Useful for following a known concern; the numerical gate still cannot pass. |
| Format | Seven Markdown files | Single group, no discrimination. |
| Scale | Compact cards versus longer comparison records | Natural 4/3 division; same failed gate, partly redundant with named/consolidated structure. |
| Time | Creation sequence and three consolidation milestones | Already exposed in filenames and dependencies; not hidden structure. |

Ranking: the content/job dimension is the most relevant candidate; scale is second for choosing a reading commitment; relationships are third for auditing derivations. Names, format and chronology add no non-obvious classification. None passes all three required tests. Two nonoverlapping categories with >3 members each need at least 8 items. Assigning the same view to both groups merely to reach 4/4 would change the unit-counting convention and would not establish the intended discriminating split.

Result distribution: Items 7; accepted dimensions 0; accepted categories 0; items without a new category 7. No non-obvious qualifying pattern is claimed. This does not mean the seven contents are equivalent or unstructured. Their existing task routes already express real differences.

Actual use: for the concrete question “what if the actor changes?”, the current reuse-trigger view points to the serial rule. For “does a hash prove benefit?”, routing-v1 supplies provenance-only. For “does an ineligible record become a failed outcome?”, consolidation 03 supplies the domain/evidence distinction. A proposed two-folder layer adds a category choice before these already direct routes and offers no accepted dimension under this source. It is not adopted.

Strong alternative: the existing question index is useful for someone who knows the encounter question; a chronological reading remains useful for reconstructing derivation. Both survive. The rejected proposal is a new inferred categorization of this finite input, not the use of any organization whatsoever.

Certificate: exact source condition—two or more groups with more than three items each—combined with seven discrete items prevents the declared disjoint split. Contrary: overlapping facets or eight new items could change the problem, but manufacturing them would no longer be this application. The conditional-source lesson was already established in 025; this record receives no fresh KEEP credit for it.''',
'I declined the proposed category layer and used the existing direct routes on three current questions.',
'No incremental organizational benefit was established. Existing useful routes and the exact failed gate remain visible.',
'REJECT — forced categorization adds no qualified result for this seven-item input.',
'Retain the seven views with their current task links; no new folder or mandatory category choice was added.',
'Apply the same source to eight or more genuinely new items; compare direct question lookup with a known-file lookup; test an overlapping facet request explicitly.',
'Full seven-file content scan, all six discovery sources, all found dimensions ranked, numerical/orthogonal/non-obvious filters, three actual retrieval uses and recommendations. The original 8x scan/ranking/validation requirements are met; its allowed no-passing-dimension result is retained.')

names=[
('Two labels checked; both correctly mapped','One label checked; second text extraction missing'),
('New actor mentioned; aggregate excludes human outcome','Proposed listener session has no observations'),
('A changed task awaits a scope decision','Unclear whether the new task needs the third case'),
('Full extraction preserves three required clauses','Both required slide labels extracted'),
('A diagram drops the zero label','A serial export loses the empty-domain condition'),
('Partial text extraction captures one of two labels','One required clause has been inspected; another has not'),
('Old pilot kept although its criterion differs','A prior render belongs to an earlier layout version'),
('Out-of-scope historical trial lost a label','A previous artifact fails its own recorded criterion'),
('Partial historical capture from excluded version','A past event is preserved but its second outcome is missing'),
('Boundary unresolved despite complete positive result','A correct label mapping may fall outside the requested medium'),
('Boundary unresolved despite complete negative result','A content-loss observation may concern a different task'),
('Both applicability and one required result remain open','Partial extraction from a possibly relevant source')]
# Twelve valid factor states, each with two substantively distinct fixtures.
states=[('yes','none',None),('no','none',None),('unknown','none',None),('yes','decisive','improved'),('yes','decisive','did_not_improve'),('yes','partial',None),('no','decisive','improved'),('no','decisive','did_not_improve'),('no','partial',None),('unknown','decisive','improved'),('unknown','decisive','did_not_improve'),('unknown','partial',None)]
# None-state fixtures should describe intended checks, not already checked results.
names[0]=('Two-label check proposed, not performed','Second-case inspection planned, no result yet')
fixtures=[]
for i,(state,pair) in enumerate(zip(states,names)):
 for j,label in enumerate(pair):
  fixtures.append({'id':f'T{2*i+j+1:02d}','case':label,'eligible':state[0],'observation':state[1],'outcome':state[2]})
def valid(x):
 return x['eligible'] in {'yes','no','unknown'} and ((x['observation'] in {'none','partial'} and x['outcome'] is None) or (x['observation']=='decisive' and x['outcome'] in {'improved','did_not_improve'}))
assert len(fixtures)==24 and all(map(valid,fixtures))
invalid={'eligible':'yes','observation':'partial','outcome':'did_not_improve'}
assert not valid(invalid)
(ROOT/'taxonomy-observation-v2.json').write_text(json.dumps({'version':'2.0.0','unit':'One event, declared actor/task/criterion, and current eligibility assessment','facets':{'eligible':['yes','no','unknown'],'observation':['none','partial','decisive'],'outcome':['improved','did_not_improve',None]},'constraint':'Only decisive observations carry a binary outcome. Partial means some relevant result was captured but the criterion remains undecided.','fixtures':fixtures,'validation':{'valid_fixtures':24,'invalid_partial_negative_rejected':True},'migration':'yes+binary maps decisive; no+null maps none; yes+null requires review of raw evidence, never automatic conversion to negative'} ,indent=2))
table='\n'.join(f"| {x['id']} | {x['case']} | {x['eligible']} | {x['observation']} | {x['outcome'] or '—'} |" for x in fixtures)
record(33,'txm',1,'A partial observation is neither an absent observation nor a negative result',
'Update the existing observation taxonomy so that a captured but incomplete result remains retrievable without being converted into an unsuccessful outcome.',
'State-schema-v1 has eligibility, observed yes/no and a binary outcome or null. It preserves unknown versus negative outcomes, but observed=yes with a null result does not say whether any relevant result exists or whether the observation supports a decision.',
'''Scope: local records of one event under one declared actor, task and benefit criterion. This taxonomy informs aggregation and the next missing-information request. It does not classify causes, human mental states, or every kind of scientific uncertainty. A compound observation across criteria must be split by criterion.

Existing structure review: v1 correctly separates eligibility from observedness. The unresolved boundary is a partial result, such as extracting one of two required labels. Reclassifying that as no observation loses a real captured result; classifying it as failure invents the missing second result. Existing root feedback requires faithful outcome scope and no manufactured completion. No human user study of these labels was collected.

The chosen structure is faceted, with a conditional outcome field. A strict ladder remains the strong small-status alternative when observations are guaranteed atomic and decisive, but that guarantee is false for the present two-label input. An unconventional alternative—preserve the raw partial capture with no status—also works for one record; it is less directly queryable across the 24 cases and remains the fallback when the taxonomy itself is uncertain.

| Facet/category | Definition | Example | Non-example / relationship |
|---|---|---|---|
| Eligibility: yes | Included under the current declared scope | Current-version local mapping check | A human proposal in a model-outcome aggregate |
| Eligibility: no | Currently excluded; history retained | Earlier-version check excluded from present-version aggregate | Erased or nonexistent event |
| Eligibility: unknown | Scope membership needs evidence | Unclear whether the task requires a third case | A known member with an unobserved result |
| Observation: none | No relevant result captured for this criterion | Proposed check | One of two labels already read |
| Observation: partial | Some relevant result captured, insufficient for this criterion | First label extracted, second unavailable | Complete decisive negative result |
| Observation: decisive | Available result settles the declared criterion | Both labels recovered or a required label conclusively absent | Merely having a file or checksum |
| Outcome: improved / did_not_improve | Binary comparison assigned only after decisive evidence | Exact preservation passes / required condition absent | Null while evidence is partial |

Each facet has a single parent and consistent granularity. Outcome is conditional on decisive observation, not another sibling in the observation facet. Null is an unassigned outcome, not a third benefit value. Every category has an instance; the valid product contains 12 combinations, not the unconstrained 18.

Full classification and consistency test:

| ID | Concrete fixture | Eligible | Observation | Outcome |
|---|---|---|---|---|
'''+table+'''

The executable validation in [taxonomy-observation-v2.json](taxonomy-observation-v2.json) records all 24 valid fixtures. An injected partial+did_not_improve combination was rejected by the constraint. There are no orphan categories, duplicated definitions or ambiguous valid facet memberships in these stipulated cases. These tests do not establish coverage of every future research event.

Actual application: the first extracted label `1` from an expected `[1,0]` display is retained as a partial observation. The outcome stays null. When the second value `0` is supplied, the observation becomes decisive and the preservation criterion is satisfied. If the second value were `1` instead, the same partial first capture would lead to a decisive failure. The taxonomy therefore preserves the common prefix without deciding its unknown continuation.

Version and migration: `1.0.0` → `2.0.0` is a breaking change because the boolean observed field is replaced. Old yes+binary records map to decisive+the same outcome. Old no+null maps to none. Old yes+null requires inspecting raw evidence; it is not automatically interpreted as partial or negative. The old schema remains unchanged for provenance. A future added eligibility value is a minor change only if old meanings remain valid; a wording-only clarification is a patch. Change log: add partial/decisive distinction; constrain outcome; add 24 cases and migration rules.

User decision path: establish current domain; ask whether any relevant result exists; if yes, ask whether it settles this criterion; assign outcome only at that last step. FAQ: “Does partial mean bad?” No. “Can an excluded event have a decisive result?” Yes; exclusion changes the aggregate, not the historical evidence. “Can one result be decisive for one criterion and partial for another?” Yes; separate the criterion records.

Maintenance: review when an unclassifiable event occurs, when a category gets two conflicting interpretations, or when the actor/task/criterion unit changes. No automated future review was scheduled. The first review should inspect raw cases and migrations, unused categories, and feedback from actual users if available.

Certificate: the local two-completion test establishes that the old observed flag underspecifies what has been captured for this criterion. The new category preserves that difference and changes the next action from assigning an outcome to retrieving the second value. A single raw note could also preserve it; the facet's benefit is the tested queryable distinction, not universal taxonomy superiority.''',
'I preserved a real partial capture, withheld its outcome, and then resolved the same prefix through two different complete inputs without changing the earlier evidence.',
'The local record can request the missing value without erasing the captured value or inventing a negative result. Human use and broad-domain completeness remain untested.',
'KEEP — partial observation now has a tested, distinct representation and next action.',
'Faceted v2 schema plus raw evidence and explicit migration; the v1 file remains available to interpret earlier records.',
'Test a criterion that changes after capture; inspect an old yes/null record with no raw evidence; ask an actual maintainer to classify a new partial observation.',
'All eight original stages executed: scope, existing review, category definitions/examples/nonexamples, faceted hierarchy, 24 diverse fixture classifications, constraints, version/change log/migration, documentation and review triggers. No original numeric 8x floor exists; actual finite scope is explicit.')

ops=[
('reword','Replace not-every with an explicit exception claim','meaning'),('reword','Expand an unexplained symbol in a spoken sentence','access'),('reword','Put the changed actor into a retrieval cue','retrieval'),('reword','State the criterion beside the retained verdict','evaluation'),
('reorder','Move a known answer before its derivation','access'),('reorder','Place a prerequisite before the dependent step','coordination'),('reorder','Put the current concern before method choices','selection'),('reorder','Put a transfer boundary before a prior success','evaluation'),
('change_content','Add the inverse counterexample','meaning'),('change_content','Remove a decorative duplicate sentence','access'),('change_content','Add the unknown completion that flips every','evaluation'),('change_content','Retain the failed attempt in a reusable note','retrieval'),
('retime','Insert a pause with all words unchanged','access'),('retime','Delay a cue until a new actor is encountered','retrieval'),('retime','Allow separate response time after each question','selection'),('retime','Move review after all independent checks finish','coordination'),
('switch_channel','Speak the same three-clause rule','access'),('switch_channel','Display the exact pair as two labeled circles','meaning'),('switch_channel','Provide a serial equivalent of a branch','evaluation'),('switch_channel','Make an offline copy of the complete cue rule','retrieval'),
('change_choice','Make the current-case answer available before the catalog','selection'),('change_choice','Offer a stop route after a sufficient answer','selection'),('change_choice','Allow a reader to choose case-first or rule-first','access'),('change_choice','Route a handoff to the actor authorized to save','coordination')]
rows=[{'id':f'O{i+1:02d}','operation':a,'case':b,'primary_intended_locus':c,'performance':'proposal unless linked to an actual application'} for i,(a,b,c) in enumerate(ops)]
(ROOT/'taxonomy-operations-v1.json').write_text(json.dumps({'version':'1.0.0','scope':'Atomic local representation interventions in this 24-case vocabulary','rows':rows,'compound_rule':'Split independently executable changes; retain a shared parent intervention ID','no_effect_inference':'Intended locus does not establish actual effect'},indent=2))
op_table='\n'.join(f"| {r['id']} | {r['case']} | {r['operation']} | {r['primary_intended_locus']} |" for r in rows)
record(34,'txm',2,'Split independently executable changes before assigning an operation category',
'Maintain a taxonomy of concrete interventions that can distinguish a pause from a rewording even when both aim at the same access problem.',
'The prior selector already separates an operation from its intended locus. A compound proposal such as “simplify and slow the explanation” can still be stored as one vague operation, hiding which change was actually performed.',
'''Scope: atomic local representation interventions; one independently executable change per record. Intended effect is a separate facet and is never an observed-effect assertion. Physiological, clinical and global psychological taxonomies are outside this local vocabulary. Users are model/research maintainers choosing and comparing actual operations.

Existing review: the selector's operation/locus separation is sound and is prior shared practice, not a new discovery here. The maintenance problem is compound entries. Available reviewer feedback requires distinct operations and honest unperformed human actions. No actual listener feedback was collected. The unconventional structure is an event decomposition with a shared parent ID, rather than one hierarchical label for the entire sentence. Alternative: keep a compound natural-language note; it preserves wording, but it cannot by itself answer which component was executed when only a pause occurred.

| Operation category | Definition | Typical example | Non-example |
|---|---|---|---|
| Reword | Change linguistic form while preserving intended propositions | Expand a symbol in words | Delete an exception condition |
| Reorder | Change relative location/sequence of the same units | Move answer before derivation | Add a new answer |
| Change content | Add, remove or alter propositions/examples | Add an inverse counterexample | Insert silence with identical words |
| Retime | Change temporal delivery while units stay fixed | Insert a pause | Omit a paragraph to finish sooner |
| Switch channel | Encode the same specified information in another medium/access form | Speak a serial rule | Assume speech improves comprehension |
| Change choice | Change available/default actions or required selections | Offer an optional catalog after an answer | Merely rename the catalog |

These six siblings classify a stipulated atomic direct operation. Compound cases are split, not forced into an arbitrary “dominant” bucket. The intended-locus facet has meaning, access, retrieval, evaluation, selection and coordination, chosen from the explicit main aim; other aims remain secondary notes. Loci are perspectives and may overlap in reality. No claim of a perfect mutually exclusive ontology of mind change follows.

All 24 diverse examples were classified:

| ID | Intervention | Direct operation | Primary intended locus |
|---|---|---|---|
'''+op_table+'''

The [machine-readable taxonomy](taxonomy-operations-v1.json) retains the same rows. Every operation has four instances and a common parent. Every intended-locus category occurs. Definitions are operational rather than circular: a pause is identified by changed timing with preserved units, not by “being an access intervention.” The same locus appears under several operations and the same operation under several loci.

Concrete compound test: parent P = “shorten the two-paragraph explanation, then pause before the example.” P1 removes a redundant sentence (`change_content`, intended access); P2 inserts silence while retaining the remaining words (`retime`, intended access). If only P2 is performed, the ledger records P2 performed and P1 proposed. The one-label alternative “simplify” cannot preserve that performance difference without another field. A second compound, “reorder then narrate the unchanged clauses,” decomposes into reorder and switch_channel; narration alone does not imply reordering occurred. A third case, “move the paragraph earlier without changing timing in a static page,” is one reorder operation, not a two-record timing change.

Version/change control: create local `1.0.0`; migrate the two tested compound entries into atomic children while preserving the original phrase and parent ID in this record. Old operation/locus entries already atomic require no migration. A future boundary redefinition is major; a new compatible operation is minor; a clarified example is patch. Change log: six operational categories, six intended-locus labels, 24 examples, compound splitting rule and three split/non-split tests.

User decision path: identify independently executable changes; preserve the parent proposal; classify each direct change; record intended locus separately; attach actual performance only when observed. FAQ: speech is a channel change even if its hoped-for effect is memory; omission is content change even if the author calls it faster delivery; a listener's response cannot be inferred from the category.

Maintenance triggers: an atomic operation fits two definitions, a new operation fits none, or two maintainers split the same proposal differently. Review the original cases, category balance, needed additions, migration impact and actual user feedback when available. No recurring automation was promised.

Certificate: the new within-case result is the atomic split that preserves performed-versus-proposed components, demonstrated on two compounds and one negative splitting case. The general operation/locus distinction is local adoption of an earlier shared standard. A taxonomy is unnecessary for a single clear action; this structure is retained only for comparing compound intervention records.''',
'I decomposed two compound interventions and preserved which component could be performed independently; the pure reorder case remained one operation.',
'The decomposition prevents an unperformed content change from being credited when only timing changed. It does not show that either change helps a human.',
'KEEP — tested compound decomposition; operation/locus separation itself is prior local adoption.',
'Atomic child records share their original parent proposal. Direct operations and intended loci stay in separate facets; raw wording remains accessible.',
'Test a compound with inseparable steps; compare two maintainers’ decomposition; add a resource or physical-setting change only when a real case requires it.',
'All eight original stages executed with six operation definitions and nonexamples, six locus labels, 24 diverse cases, three decomposition tests, version/migration/change log and review triggers. Original gives no numeric 8x floor. Taxonomy scope and missing human feedback remain explicit.')
progress()
