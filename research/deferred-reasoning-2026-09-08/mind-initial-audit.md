# Audit of the initial MindChangeResearch applications

The clearest surviving failure is that the generator often performs an operation on **the position of a sentence** while the report claims an operation on **the subject of that sentence**. Priority becomes “first four,” decomposition becomes “first three,” a cost phase becomes “the next twenty,” and a quality scenario becomes “Changed [quality name] condition.” These operations really ran. They did not perform the reasoning their output labels describe.

Snapshot: `mindchangeresearch` commit `07e6af64c65fb682305659b2ec830e21743c0f15`; source ZIP SHA-256 `7ba425b197be8d38ba9715873464dd0ba2eca43e2da3aeb985ab5ffda83fba6b`. Scope: conditions, inquiry, representation, systems, values and gosm. No source files were modified.

The companion `mind-initial-instances.json` contains every located row of the identified generated families, its exact path, line and excerpt, machine-readable mirrors, all 606 file hashes and coverage levels, all 351 requested Next attempts fields, and all 65 explicitly partial/blocked application records. `mind-initial-audit-checks.json` records the completed arithmetic and duplicate-interface checks.

Coverage: 606 files, including 599 text files, six rendered PNGs and one PPTX. All text files received a full textual scan. All 251 allocated applications received structured claim/scope/result/continuation review; ten GOSM records were included separately. The family findings received focused examination against their generators, data and source requirements. This does **not** certify independent semantic review of every sentence in every file, or that no further defect exists. The current root ledger reports 186 complete, 64 partial and one blocked among these 251 applications. File coverage, source coverage and semantic completeness remain separate claims.

## Confirmed repeat families

Counts below distinguish semantic slots from saved copies. Several rows can describe the same underlying failure; they must not be summed as independent discoveries.

| ID | Family | All semantic slots mapped | Exact primary locations |
|---|---|---:|---|
| MCI-01 | Claimed later comparison leaves the candidate and failed requirement unnamed | 3 | `values/022-pre-1.md:73`, `022-pre-2.md:73`, `022-pre-3.md:73`; generator `values/batch3.py:32` |
| MCI-02 | An instruction to define a retention trigger is called an applied retention choice | 1 | `systems/044-fut-1.md:33,37–41`; `systems/future-1-scenarios.json:36` |
| MCI-03 | Architecture scenarios repeat the quality name in place of a concrete stimulus and response | 30 | Every quality row at `systems/049-sysarch-{1,2,3}.md:19–28`; `systems/build_architecture.py:42` |
| MCI-04 | Duplicate interface supplies a second ID for the same described connection | 3 duplicate pairs | `systems/049-sysarch-{1,2,3}.md:95,105`; every `I*-15`/`I*-25` JSON row; `systems/build_architecture.py:18–19` |
| MCI-05 | Requirement priority and stakeholder role are assigned by position | 160 assignments | Every requirement row in `systems/098-requirements-{1,2}.md` and corresponding JSON; `systems/build_designs.py:28–33` |
| MCI-06 | Verification criteria instruct a generic test to exercise their own requirement | 160 fields | Every `verification` field in `systems/requirements-{1,2}.json`; `systems/build_designs.py:33` |
| MCI-07 | Old conflict labels are copied onto new requirement subjects | 8 rows | `systems/098-requirements-2.md:108–115`; `systems/requirements-2-conflicts.json`; `systems/build_designs.py:35–36` |
| MCI-08 | Number of possible pairs is reported as pairs considered | 2 claims of 3,160 | `systems/requirements-{1,2}-conflicts.json:2`; `systems/build_designs.py:37–39` |
| MCI-09 | Parent relationships and extra hierarchy levels come from positional cuts | 40 construct/restrict nodes | Every construct/restrict row in `systems/094-sysdecomp-{1,2}.md` and corresponding JSON; `systems/build_interfaces.py:13–21` |
| MCI-10 | Check results are unconditionally assigned True | 4 PASS flags | `logging_allocated` and `external_boundary_allocated` in both decomposition JSON files; `systems/build_interfaces.py:24` |
| MCI-11 | A hundred cost-element names are attached to a six-phase numerical model | 100 named rows | `systems/147-lcca-1.md:19–118` and all lifecycle JSON elements; `systems/build_cost_reliability.py:7–21` |
| MCI-13 | Record existence or absence of an explicit caveat supplies completion | 6 generators | The five `update_ledger.py` scripts and `gosm/write_records.py:35–40` |

MCI-07 contains seven clear subject mismatches and one broadly relevant but incomplete copied relationship. MCI-05 identifies 160 ungrounded **assignments**, not 160 necessarily false priority labels. MCI-13 identifies an acceptance mechanism; it does not imply every completion label is false.

Two qualified cases are also mapped: MCI-12 is an openly uncomputed round-robin row in `conditions/qs-01.md:16`; MCI-14 is a proposed contract expressed as “Applied action now” in `systems/044-fut-3.md:33`, with potentially fulfilling contract work elsewhere. The latter cannot honestly be classified as “never done.”

## The missing conclusions, completed

### A repeated comparison does not identify three different comparisons

The three preference applications say a new candidate satisfies four requirements and violates the fifth, then retain the current candidate. The fifth dimensions are, respectively, **Evidence**, **Optional ending**, and **Traceable evidence**. The allegedly new candidate is never named and its properties are never supplied. `values/batch3.py:32` inserts the identical sentence without using any case-specific argument.

The valid abstract conclusion is: if satisfying all five criteria is a hard constraint and an alternative fails one, that alternative is inadmissible regardless of an unrequested aesthetic advantage. That is one conditional argument. It cannot simultaneously supply three concrete examples of transfer simply because it occurs after three different tables. The records appropriately keep their human procedures partial and benefit UNRESOLVED; those truthful caveats do not instantiate the missing comparison.

### Entry counts cannot determine retention without a value or constraint relation

The FUT1 inputs imply `N(t)=20+5t`, `20+10t`, or `20`, with one maintenance unit per entry-year. They settle the stock counts. They do not settle which record to retain, a review threshold, or when review pays for itself.

For a particular record, retaining it is preferable on an additive expected-value criterion exactly when its expected future contribution plus avoided reconstruction cost exceeds its future maintenance and preservation costs, after accounting for the consequences of deletion. None of those record-specific values is supplied. Therefore the record’s necessary result is a maintenance-exposure calculation with an undetermined retention choice. Calling “Use a validity/retention review trigger” an applied action does not fill the missing relation. KEEP can attach to a demonstrated representational change, but not to a retention selection that has no selected item or threshold.

### Hard constraints cannot become optional because they occupy row five

The generator assigns MUST to the first four entries of every category and SHOULD to the last four. Thus `R1-05 Retain hard constraints` and `R1-08 Reject an unauthorized goal substitution` receive SHOULD. Meanwhile including a preparation candidate and a representation-change candidate always receives MUST.

The contradiction is exact: a hard constraint defines the admissible set. If acceptance can ignore it, the accepted set differs from the declared admissible set. Preserving and enforcing applicable hard constraints is therefore necessary for this selector’s stated function. A preparation candidate, by contrast, is necessary only when the requested exploration or a relevant dependency requires one; the category’s ordinal position supplies no such premise.

The source itself defines MUST by whether the system works without the requirement (`sources/systems-requirements.md:200–204`). This is a failure to apply the source’s definition, not a dispute about whether the source was read.

### Every copied conflict receives its actual relation

| Referenced requirements in the second table | What follows from their actual subjects |
|---|---|
| Stable result identity / Preserve observed negative case | Compatible. A negative result remains attached to the same identity; it is not erased or made into a new result merely because its verdict changes. No interpretation conflict was demonstrated. |
| Concrete reuse trigger / Return original evidence | Compatible and complementary. A trigger selects a record; the retrieved record supplies evidence. A locator alone is not the evidence it locates. |
| Observation date / Historical truth separate from present fit | Compatible. The recorded observation remains dated evidence; current applicability is a distinct predicate evaluated against current conditions. Neither overwrites the other. |
| Count recurring maintenance / Deletion reversibility | Potential resource trade-off. Preserving reversal may carry continuing cost. Its desirability depends on the value of recovery versus that carrying cost; “carry conditions with reuse” does not calculate this trade-off. No unique deletion choice follows from the supplied data. |
| Actual recurrence / Eligibility accepted | Sequentially distinct facts. A later occurrence can happen while the prior finding is inapplicable. Count the event, then independently determine eligibility; an occurrence is not successful reuse. |
| Earlier criterion weights / New hard constraint | Preserve the historical weighted result. Apply the new hard constraint to current candidates before ranking feasible survivors under the current weights. Version labels alone cannot make an infeasible candidate acceptable. |
| Reader format version / Portable description versus executable command | Independent compatibility dimensions. A reader can parse a description while lacking a dispatcher; successful parsing does not establish executability. |
| User declines reuse / Retire contradicted recommendation | Different reasons for withholding a recommendation. Declining reuse removes current authorization without proving the finding false. Contradicting its warrant removes evidential support without requiring a user refusal. Preserve both reason codes. |

These are the actual deductions absent from `systems/098-requirements-2.md:108–115`. The copied “identity versus ambiguous interpretation,” “budget versus exclusivity,” and “direct answer versus provenance” labels concern different subjects.

### A quality name cannot justify an architecture score

“Changed recoverability condition / explicit current response / condition and result both retained” does not tell us what broke, what must be recovered, or what response counts as successful. The same failure affects all thirty generated scenario rows. Consequently the score arithmetic ranks stipulated numbers; it does not independently establish that the nominated architecture best meets ten actually examined scenarios.

Concrete clauses derivable from the already supplied cases include the following. These are completed specification deductions, not claims that a production implementation was tested.

| Quality | Concrete required response |
|---|---|
| Fidelity | When the requested operation changes, retain the original request historically and bind the new operation to its own revision; do not execute the old operation as if it were the new one. |
| Scope clarity | A finite model outcome with no observed human action cannot produce `human_effect_observed=true`. |
| Recoverability | Rejection of an obsolete pending packet leaves the previously accepted historical packet intact. |
| Modifiability | Budget change 60→40 invalidates the pending 55-unit choice and recomputes a feasible choice; the example supplies S+C at cost35 and value40. |
| Traceability | The accepted finite result retains the exact input, criterion version and evidence reference needed to reproduce its comparison. |
| Simplicity | Two encodings equivalent on the declared retrieval workload may be compared on actual representation burden; an unexplained score cannot settle that comparison. With no burden measurement, the simplicity ranking is unresolved. |
| Prompt delivery | A consumer cannot use an incomplete prerequisite packet; an unrelated ready branch need not wait for it. This is an event-order requirement, not an invented latency estimate. |
| Portability | Removing the dispatcher leaves readable historical evidence but no executable continuation. Retaining the description does not restore the missing host capability. |
| Resource control | A 55-unit pending bundle fails the new40-unit budget; retaining its old budget version cannot authorize commitment under the new one. |
| Agency | A description-only authorization does not authorize the proposed tool execution; the description remains eligible. |

One concrete transition can satisfy multiple clauses. That does not turn it into ten independent observations or supply the unmeasured simplicity preference.

### More IDs do not supply more interfaces

The generator creates consecutive edges for indices0–14 and then appends `(14,15)` again. All three architecture files therefore contain 25 IDs but only24 endpoint pairs. For each, I*-15 and I*-25 describe the same payload, protocol, frequency and error behavior, while one is called HIGH and the other MED.

The extra row is neither a new dependency nor a different contract. Its only distinct contributions are a new identifier and contradictory priority metadata. The correct distinct-interface count is24. A requirement for25 distinct interfaces is not satisfied; adding a meaningless extra interface to recover the quota would preserve the same failure.

### Generated hierarchy is not derived hierarchy

`systems/build_interfaces.py` assigns the first five categories to one domain and the rest to another. It creates “construct [category]” and “restrict [category]” for every category; the first three leaves attach to construct, the later two to restrict, and all three remaining requirements attach to leaf4.

A required time horizon is placed under “restrict goal identity,” while the requested action, actor and object are under “construct goal identity.” The first distinction need not be wrong in every possible design, but its justification is not supplied by the code or its subject: changing the row order changes the alleged conceptual dependence while leaving the requirements themselves unchanged. Therefore the five-level result establishes a tree shape, not five levels of explanatory necessity.

The later decision against deploying fifty tiny components is a real and useful negative result. It does not validate the earlier forty manufactured construct/restrict nodes. A valid final boundary does not retroactively make every exploratory hierarchy semantically sound.

### A hundred labels do not add a hundred independently analyzed cost elements

The lifecycle generator takes80 requirements from one array and20 from another, cuts them into phase sizes10/20/20/20/20/10, and supplies phase factors. That is why “Return scope before reapplication” becomes a retirement activity. Its placement is determined by index, not by examining the operation’s lifecycle role.

For alternative `a`, the computed present value reduces exactly to:

`PV(a) = Σ over six phases [phase_count × phase_factor(a) / 1.1^phase_year]`.

The hundred activity names occur nowhere in this calculation. The completed independent aggregation reproduces every saved value:

| Alternative | Six-aggregate present value |
|---|---:|
| direct | 147.08825154764637 |
| compiled | 195.36358048071727 |
| hybrid | 140.65699685192888 |
| batch | 155.26590955660006 |

Thus hybrid is the minimum under these stipulated six-phase numbers. No empirical cost claim is made, and the finite arithmetic is legitimate. But the names and phase memberships do not provide independent engineering grounds for the100-element decomposition. The six additional sensitivity groups are also row ID modulo6; their changes are valid numerical perturbations of the stipulation, not discovered causal cost drivers.

### The uncomputed queue case can be settled now

`conditions/qs-01.md` stipulates one nonpreemptive processor. One-unit round-robin is a preemptive discipline, so it does not belong among the admissible alternatives. The correct disposition is “excluded by nonpreemption,” not an unresolved computation.

If preemption is explicitly introduced, initial A,B,C,D round-robin finishes A15, B2, C9 and D7. Total waiting times are6,1,6,5; their mean is4.5. A misses its deadline10.

There is also a better feasible nonpreemptive order than the selected A,B,D,C. A takes9 and is due10, so it can be preceded only by the one-unit B. With B first, A finishes10; the remaining D2 and C3 run shortest-first. This gives **B,A,D,C**, start times0,1,10,12 and mean wait**5.75**, versus7.75 for the record’s selected order. Enumeration of all24 orders confirms the optimum among feasible schedules. The record’s narrower claim of improvement over FIFO is true; this audit supplies the further optimum the declared inputs allow.

## Why the failures happened, and why the checks allowed them

The archive contains direct causal evidence for these production failures: code interpolation and positional assignment generate the artifacts. No speculation about training history or hidden motivation is needed to establish those mechanisms.

The numerical source floors created immediately countable obligations:80 requirements,25 interfaces, five levels,100 cost elements. The generators meet the visible inventory by construction. Semantic specificity, implication validity and result usefulness are harder properties; the code largely represents them as labels or supplied strings. The resulting document possesses the **form of the required operation’s output** before the required operation has occurred.

Acceptance compounds this substitution. Four line-ledger generators mark an existing record complete unless it matches a known exception, and the inquiry generator relies on explicit pending/partial phrases. The representation generator is more direct: `status='complete' if p else 'pending'`. Replaying its logic over this snapshot would mark all51 applications complete, including the8 that the root ledger now correctly marks partial. The GOSM writer sets `completed_variant=True` when it writes any body.

These are conditional replay weaknesses and permissive acceptance rules. They do not prove that every current status is false. The root integration has already repaired many statuses and explicitly says they are scoped reports, not independent semantic certification. But the original generator still makes missing semantic reasoning invisible unless someone has separately noticed and handlisted it.

The deeper failure is circular validation: the producer chooses the form, fills the form, labels the filled form complete, and then uses its own completion label as evidence that the form’s intended operation happened. A structural predicate can certify a structural result; it cannot certify an unexamined semantic relation just because the relevant column has text in it.

## Deferred reasoning, placeholders and performativity

Deferred reasoning occurs when a present obligation is left as “evaluate,” “derive,” “verify” or “choose,” and the response treats that instruction as the requested completed work. A placeholder leaves an operand, relation, criterion or mechanism uninstantiated. Performativity, in the user’s relevant sense, occurs when the representation of having done the work receives the practical credit that belonged to actually doing it.

These are related but not identical. An explicit future question can be honest and useful. A named but unfilled slot can be an honest draft. A detailed calculation can be performative even without a single imperative if its irrelevant labels are counted as analyzed subjects. In this corpus the most serious examples are not bare TODOs: they are populated tables whose populated cells still delegate their meaning to a future reasoner.

The difference between abstraction and a placeholder is whether the abstraction already constrains the inference. The declared job durations and deadlines determine a feasible schedule, so A/B/C/D are harmless variables. “Changed recoverability condition” supplies no particular change and therefore cannot determine the asserted response or score. Eliminating short names would not repair that difference. A long label can be as empty as a single letter.

The controlling test is counterfactual sensitivity: if the actual subject changes, does the claimed analysis change for the corresponding reason? Priority by row position changes when unrelated ordering changes; lifecycle totals do not change when operation names change; literal True checks survive removal of the thing they supposedly check. Those sensitivities expose which operation was really performed.

## Caution and the preference for inoffensive conclusions

The archive repeatedly withholds human-effect claims and distinguishes hypothetical examples from real observations. That is warranted. It also contains forceful completed results: `inquiry/13-fctl-fault-gates.md` rejects a specific source sentence as false under its stated gate semantics; `inquiry/51-ht-information-policy.md` rejects universal half-mixture and act-positive-response policies through exact changed-input calculations; `representation/045-draft-2.md` catches and repairs the weakening of “sends” into “prepares to send.” These are counterexamples to saying all caution or all current work is empty.

The residual problem is asymmetric scrutiny. The generator is careful not to infer an external human benefit, yet accepts internally generated categories, scores, scenarios and parent relationships without equivalent examination. A disclaimer about untested human benefit cannot make an internal deduction valid. “Synthetic” accurately identifies the origin of inputs; it does not justify every claimed relationship among them.

No evidence here proves an internal motive to avoid offending anyone. The observable result is safer in a narrower sense: stock-count examples, arbitrary synthetic costs and procedural restatements permit many formally modest claims while postponing the judgments the actual project requires. The stronger justified response is to invalidate the unsupported application credit and state the concrete failure. Being harsh is not an epistemic criterion; **retaining a warranted adverse conclusion instead of replacing it with another instruction is**.

## False positives excluded

- All351 `Next attempts:` occurrences are indexed separately. The user expressly asked each record to generate further attempts. Their existence is not evidence that the work immediately above was deferred; otherwise fulfilling that request would guarantee an accusation of failure.
- The65 current partial/blocked applications are listed with their exact missing requirements. Actual participant choices, physiological reports, weeks of retention and unavailable campaign data cannot be supplied by additional prose. Preserving those limits is completed reasoning about what follows from available evidence.
- Source-original instructional files and copied original runtime scripts are procedures or evidence, not purported executions merely because they contain imperative language.
- Several earlier promises are fulfilled elsewhere: the inquiry’s original tag-rule, minimax-regret and hypothesis-testing continuations now have actual outputs; the representation writing dependencies have concrete route/edit/timer fixtures. A local future-tense sentence does not establish repository-wide nonperformance.
- A legitimate specification can instruct an implementer. The failure begins when specification completion is promoted into implementation, observed effect, or a semantic deduction not present in the specification.
- An unresolved empirical effect does not prevent a decisive logical conclusion. The optimum queue, duplicate interface count, false copied conflict labels and nonsemantic priority rule above are settled without pretending to observe a human mind.

The necessary prevention is therefore not a larger checklist of verbs. Credit must attach to a result whose content changes when its required premises change, and the scope of the credited result must match what was actually completed. Any representation that claims more must lose that claim now, even if its file count, formatting, source hashes and self-reported checks all pass.
