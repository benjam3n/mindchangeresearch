Intended mind change: Replace source-order selection among four newly demonstrated computational mind changes with a compact question order that prevents optimization over impossible actions or undefined probabilities.

Starting working judgment: The four retained findings are individually useful, but I would initially retrieve them by method name: MRC for changed inquiry, MTCG for transformation, MTCG for probability, and UF for utility. That arrangement preserves provenance yet does not say which question must be settled first in a mixed case.

Concrete input: A controller starts at state 1 modulo 5. Operation A adds 2 and operation B subtracts 1. It must reach state 4. Two evidence sources report one success in two trials and eight successes in eight trials. A later decision asks whether to use the controller, but its utility rule has not yet been selected. The four eligible KEEP findings are MRC3's finite-state orbit classification, MTCG2's reachability coefficients, MTCG3's sampling-unit distinction, and UF1's conditional utility selection. No rejected or unresolved finding is promoted into this consolidation.

# State, reachability, measure, consequence

## Organization A: source lineage

The source-lineage view is `MRC3 → MTCG2 → MTCG3 → UF1`. It makes derivation and receipts easy to retrieve. On the concrete input, however, the names do not reveal why reachability must precede outcome optimization or why the evidence denominator must be declared before a probability enters utility. A user can start with UF, score an unreachable target, or combine the nine successes and ten trials when the actual sampling operation chooses a source first.

## Organization B: dependency questions

1. **State:** What transition rule evolves the object, and is the question about a future state, a transient, or an eventual cycle? MRC3 supplies the bounded classification route.
2. **Reachability:** Under the allowed operations, can the target be attained, and what witness attains it? MTCG2 supplies the exact coefficient/witness route.
3. **Measure:** What random operation generates the observation—uniform token, uniform source, or an unspecified prior? MTCG3 supplies the denominator check.
4. **Consequence:** Which utility representation survives the actual failure conditions, constraints, and switch cases? UF1 supplies the conditional selection rather than one universal formula.

This is a dependency graph, not a claim that every task needs all four questions. A known deterministic transition can skip measure. A pure evidence question can stop before consequence. Proven impossibility stops the branch before probability and utility are used to rank implementations of that target.

## Performed reuse

State and reachability first: the target difference is 3 modulo 5. The coefficients `a=2, b=1` satisfy `2a-b=3 (mod 5)`. Executing A, A, B gives `1 → 3 → 0 → 4`, so the target is reachable in three operations. This witness is retained; a utility score is not asked to substitute for it.

Measure next: pooling individual trials yields `9/10`. Choosing a source uniformly and then a trial within that source yields `(1/2 + 8/8)/2 = 3/4`. Both calculations are correct for different sampling operations. Because the input did not state which operation supplies the next case, the success probability remains the pair `{9/10 under token sampling, 3/4 under equal-source sampling}` rather than one collapsed number.

Consequence last: UF1's switch table rejects an expected-value calculation that silently chooses between those measures. The present decision is therefore returned as conditional on the sampling rule and the declared loss function. The consolidation changes an attempted immediate score into a reachable witness plus a two-measure decision boundary. That is an actual later use of all four findings, not evidence that a person adopted the result.

## Boundary cases and preservation

- If operation B is removed, the two-control coefficient formula cannot be copied unchanged. Reachability must be recomputed for the remaining generator.
- If a source prior is supplied, the probability can be evaluated under that prior; if it remains absent, uncertainty is the correct output.
- If the target is unreachable, utilities can compare alternative targets or information gathering, but cannot make the stated target reachable.
- If consequences include a hard safety ceiling or noncompensable constraint, an additive expectation may be the wrong UF alternative even after probability is known.
- Source lineage remains the provenance view. The dependency questions become the selection view; neither replaces the application records.

## Organization decision

Use Organization B to select and order operations in mixed cases. Preserve Organization A as the derivation and receipt index. The performed case favors B because it blocked two concrete invalid moves—scoring before proving reachability and using a probability before fixing its sampling unit—while still retrieving every source record. No navigation-time or global-optimality claim follows from one case.

Actual mind change: I changed from method-name retrieval to the order `state → reachability → measure → consequence` for mixed computational cases, while keeping source lineage for provenance. Applied to the concrete input, this produced a three-operation witness and retained two conditional probabilities instead of one premature utility score.

Benefit: The chosen arrangement prevented optimization over an unproved action and prevented an undefined sampling choice from being hidden inside a number. Its benefit is demonstrated for this finite reuse case only.

Verdict: KEEP — organization and later reuse; no new substantive discovery credit and no claim of globally maximal organization.

Organization: Dependency-question card for selection; source lineage and the four application records for derivation, limits, and receipts.

Next attempts: Apply the card where the state is stochastic rather than deterministic; test a target reachable by several witnesses with different hard constraints; compare the card with source-order retrieval on a new input frozen before either route is evaluated.
