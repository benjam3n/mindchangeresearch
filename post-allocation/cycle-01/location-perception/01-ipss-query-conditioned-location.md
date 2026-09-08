# IPSS — “best location” as a query-conditioned policy

Intended mind change: Replace my judgment that an inspection location can be ranked as best once with a tested judgment about whether “best location” denotes a physical site, a next action, or a query-conditioned sequence policy.

Actual starting judgment: I expected the three sites to support one stable ranking because each site has a fixed feature set. I had not yet tested whether the noun “location” was concealing a policy over query and inspection history.

Concrete input: The prospectively frozen case in `../frozen-inputs.md`: L1={surface crack, serial identity}, L2={surface crack, internal void}, L3={internal void, serial identity}; decision queries alternate between structural safety and chain of custody. Before scoring, I fixed the structural predicate as `{surface crack, internal void}` and the custody predicate as `{internal void, serial identity}`. A site satisfies a query only when it contains both predicate features. This subordinate predicate freeze preceded all scores and selections below.

Prospective boundary: The observations, alternating-query rule, predicates, score criteria, and tie rule were fixed before the IPSS result was evaluated. The tie rule is: predicate satisfaction, then number of predicate features, then lowest location label. The case changes only model-side interpretation, representation, query, and location selection; it measures no human perception.

Source fidelity: Original `ipss` stdout SHA-256 `4967477d67334da4798c05381ce3b81a6a3648b419f189019ff7710405537377`; current-requirements stderr SHA-256 recorded in `source-receipts/IPSS.stderr.txt`. The original source contains no numerical 8x rule. All eight original steps and all verification checks are executed at expanded scope; no 8x certification is claimed.

## 1. Raw input

> Choose the best inspection location.

The words “best,” “inspection,” and “location” are unchanged.

## 2. Context

- Source: constructed prospective inspection case.
- Available sites: L1, L2, L3.
- Fixed observations: each site exposes exactly two of the same three possible properties.
- Current decision query: structural safety.
- Known next decision query: chain of custody.
- No access cost, travel time, sensor-error rate, or human observation is supplied.
- Success requires a changed location selection when the query changes, or a justified rejection of a query-independent best site.

## 3. Interpretations

1. **Current-query site:** “Best location” is the physical site that most completely answers the query active now. Assumptions: the active query is known; its two-feature predicate is sufficient.
2. **Alternating-query policy:** “Best location” is the next action returned by a policy `π(query, history)`, not a permanent property of one site. Assumptions: alternation is known; revisiting or changing sites is allowed.
3. **Maximum-output site:** “Best” means the site revealing the greatest number of properties, independently of their identities. Assumptions: feature count is the objective; composition is irrelevant.
4. **Maximum-complement site:** “Best” means the site adding the most properties absent from the immediately preceding inspection. Assumptions: an inspection history exists; novelty is worth more than current-query sufficiency.
5. **Lowest-cost site:** “Best” means cheapest, fastest, or safest to access. Assumptions: access properties exist and dominate the evidence objective.
6. **Custody-first site:** “Best” means the site that most completely answers chain of custody even while structural safety is active. Assumptions: custody has priority over the stated current query.
7. **Evidence-storage location:** “Location” means the place in a record where observations should be stored. Assumptions: “inspection location” refers to document position rather than L1–L3.
8. **Universally dominant site:** “Best” means one physical site that weakly dominates the others across every alternating query. Assumptions: a query-independent dominance relation exists.

## 4. Obvious filters

- Interpretation 7 is removed: the context explicitly identifies L1–L3 as inspection sites, not record positions.
- Interpretation 5 remains possible in ordinary inspection work but is not rankable here because no access data were supplied.
- Interpretation 8 remains for scoring; the fixed matrix can decide whether dominance exists.
- Interpretations 1–4 and 6 are coherent and consistent with at least one ordinary use of “best.”

## 5. Scores

Criteria and weights fixed before scoring: contextual fit 0.25; decision discrimination 0.30; supplied-data sufficiency 0.20; next-query usefulness 0.15; low unsupported-assumption cost 0.10. Each component is 1–10; higher is better.

| ID | Interpretation | Fit | Discrimination | Data | Next query | Low assumption cost | Weighted total |
|---|---|---:|---:|---:|---:|---:|---:|
| I1 | Current-query site | 10 | 10 | 10 | 6 | 9 | 9.30 |
| I2 | Alternating-query policy | 10 | 10 | 10 | 10 | 8 | 9.80 |
| I3 | Maximum-output site | 7 | 2 | 10 | 6 | 9 | 6.15 |
| I4 | Maximum-complement site | 8 | 8 | 6 | 10 | 6 | 7.70 |
| I5 | Lowest-cost site | 5 | 4 | 1 | 5 | 2 | 3.60 |
| I6 | Custody-first site | 5 | 2 | 10 | 10 | 9 | 6.25 |
| I8 | Universally dominant site | 6 | 4 | 10 | 9 | 5 | 6.55 |

## 6. Ranking

1. I2 — 9.80
2. I1 — 9.30
3. I4 — 7.70
4. I8 — 6.55
5. I6 — 6.25
6. I3 — 6.15
7. I5 — 3.60

Gap between first and second: 0.50/10. I2 and I1 agree on the immediate structural action; they differ on whether the result is a durable site ranking or one state of a policy.

## 7. Confidence

Confidence in I2 over I1: moderate, not high. The explicit query alternation supports a policy interpretation, but if the instruction concerned only a one-time inspection, I1 would lose none of the required information. Confidence that I3 is inadequate: high, because every location reveals exactly two properties and therefore raw count cannot discriminate. Confidence that I8 is false in this case: high, because no one site satisfies both fixed query predicates.

## 8. Selection and verification

Selected interpretation: I2, alternating-query policy.

Policy produced from the fixed predicate and tie rules:

- `π(structural safety, no prior inspection) = L2`, because only L2 contains both surface crack and internal void.
- `π(chain of custody, after L2) = L3`, because only L3 contains both internal void and serial identity.

The interpretation accounts for “best” through predicate satisfaction, “inspection” through the stipulated observations, “location” through L1–L3, and the broader context through the alternating query. It would change to I1 if the next query were removed, and would become unresolved if site-changing were forbidden or its cost were supplied and dominated evidence value.

## Distinct later use

The current query was changed from structural safety to chain of custody without changing any observation or score criterion. A stored scalar ranking would have retained L2. The selected interpretation recomputed the next action and changed the location to L3. The later use therefore consumed the interpretation as a policy, not as a label attached to the first answer.

## Closing assessment

Actual mind change: My working judgment changed from “the fixed site features support one best-location ranking” to “this input denotes `π(query, history)`; the selected physical location is L2 for the first query and L3 for the next.”

Benefit or harm: Beneficial within the finite constructed case. It prevented an answer to the first query from becoming an unjustified permanent ranking and produced the prospectively required location change. Cost: five interpretations were scored despite only I1 and I2 being close contenders; the expanded search was less efficient than a direct two-way test.

Verdict: **KEEP** as a prospective model-side interpretation and later-use result. The broad principle that location relevance depends on the query existed earlier in the program; only the explicit replacement of a scalar ranking by `π(query, history)` is eligible for new-within-case credit.

Performative check: Not performative. The interpretation changed the stored object from a location rank to a policy and changed the later selected location. It does not show that a human noticed differently, believed differently, or acted differently.

Content assessment: The result is sufficient for the stipulated three-site matrix and two query predicates. It does not generalize to noisy sensors, unequal inspection costs, inaccessible sites, or more than one permitted inspection without new inputs.

Organization assessment: Raw input, interpretations, filters, scores, rank, confidence, selection, later use, and reflection are kept in the original order. The score table is reusable; the caveats remain next to the policy rather than being detached into a generic warning section.

Next attempts: Add unequal movement costs and test whether the policy still switches; hide one feature until after the first selection and test genuine information acquisition; allow two inspections and compare greedy selection with sequence optimization; introduce sensor false negatives and test whether predicate satisfaction remains the right objective.
