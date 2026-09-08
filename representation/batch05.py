from write_record import record,progress,ROOT
record(15,'omtx',1,'A state model that keeps inapplicability out of the outcome count',
'Choose a record representation that distinguishes an eligible but unobserved outcome from an operation outside the present task’s domain.',
'The two-field observedness/outcome representation from 013 handles missing evidence well. It still lacks an explicit domain-membership field, so an inapplicable operation can look like a missing observation.',
'''
Rows are four complete candidate state encodings at the same abstraction level: binary outcome, three-state outcome, four-state outcome, and factored eligibility/observedness/outcome. Columns test six independent demands: missing evidence, non-improvement, out-of-domain case, uncertainty about eligibility, reversibility of later update, and serial readability. Priority is high on preserving distinctions, medium on update operation, low on display brevity. Ratings are exact supported/unsupported or explicit design judgment, never measured human performance.

| Encoding | Missing outcome | Observed non-improvement | Outside domain | Eligibility unknown | Later update | Serial display |
|---|---|---|---|---|---|---|
| Binary improved/not | Unsupported: both collapse to not | Supported | Unsupported | Unsupported | Overwrites conflated state | Two short words; ambiguous semantics |
| Three-state improved/not/unknown | Supported | Supported | Unsupported: unknown conflates domain absence | Unsupported | Resolves outcome only | Three words, legend needed |
| Four-state adds inapplicable | Supported | Supported | Supported | Unsupported unless unknown is overloaded | Inapplicable→eligible needs reclassification | Four named states are manageable in this specimen |
| Factored eligible yes/no/unknown; observed yes/no; outcome if observed | Supported | Supported | Supported with eligible=no | Supported independently | One field can change while others remain intact | Longer but each question has an explicit answer |

Six finite input cases fill the comparison: eligible observed improvement; eligible observed non-improvement; eligible unobserved; known inapplicable; eligibility unknown; and eligibility established later while outcome remains unobserved. Binary has a deal-breaker on the third case; three-state fails the fourth; four-state fails the fifth without redefining unknown. The factored model represents all six, but has a brevity cost. It does not dominate the four-state display on brevity. The strongest alternate is a four-state display backed by the factored record; that hybrid preserves semantic detail while showing a short label when eligibility is known.

Actual generated records:

- `{eligible: yes, observed: yes, outcome: improved}` → count as an observed improvement in the declared domain.
- `{eligible: yes, observed: no, outcome: null}` → keep both possible outcomes; no positive or negative count.
- `{eligible: no, observed: no, outcome: null}` → exclude from this domain’s denominator, without calling it a failed operation.
- `{eligible: unknown, observed: no, outcome: null}` → domain size itself unresolved; request no probability by default.

Constraint: eligible=no with an observed result is not universally impossible—a pilot may have been run before discovering inapplicability. The record can retain that event, but the result remains outside this task’s outcome aggregation. This countercase repairs an initially tempting rule that would erase the observed event. Historical observation and current eligibility are separate.

Later application: the proposed group-listening activity is outside a claim about changes actually performed by this model. It is therefore marked `eligible=no` for that aggregate, not counted as a model failure or missing result. Its prospective human claim has a different domain and remains unobserved. Certificate: exact claim—the factored record preserves the six declared cases and the late-inapplicability countercase—is supported by the displayed assignments; the simplest three-state record has an explicit collision. Strong contrary—extra fields add authoring burden; the compact display backed by factors is retained. No universal schema completeness claim is made.
''',
'I added domain eligibility independently of observedness and outcome and used it to exclude the unperformed human activity from the model-change aggregate.',
'The local aggregate no longer mixes out-of-domain operations with missing outcomes or failures. The observed-event countercase remains representable after eligibility changes.',
'KEEP — factored domain membership and outcome state.',
'The underlying factors are stored in state-schema-v1.json; compact labels are a view over them rather than their replacement.',
'Test an operation partly inside the domain; test changing the benefit criterion while eligibility remains constant; check whether aggregate counts retain the declared denominator.',
'No numerical 8x floor exists. Four candidate rows × six dimensions were filled from six finite cases, deal-breakers/trade-offs/clusters were compared, a late-inapplicability countercase repaired a constraint, and the chosen model was used on a later aggregation case.')
import json
(ROOT/'state-schema-v1.json').write_text(json.dumps({'version':'1.0.0','fields':{'eligible':['yes','no','unknown'],'observed':['yes','no'],'outcome':['improved','did_not_improve',None]},'scope':'One declared task domain and benefit criterion; no causal attribution implied','rules':['An observed outcome can be retained even if later judged outside the domain.','Aggregation includes only currently eligible records; unknown eligibility leaves the denominator unresolved.','Unobserved is not did_not_improve.'],'examples':[{'id':'local_performed_improvement','eligible':'yes','observed':'yes','outcome':'improved'},{'id':'prospective_human_activity_in_model_aggregate','eligible':'no','observed':'no','outcome':None}], 'provenance':'015-omtx-1.md'},indent=2))
progress()
