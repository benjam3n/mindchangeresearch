# NCL — efficiency is subordinate to admissibility

Intended mind change: Replace the universal rule “every beneficial mind-change attempt should maximize efficiency” with a rule that cannot trade away benefit, safety, or autonomy merely to save time.

Actual starting judgment: If two attempts aim at the same beneficial change, the faster one should be selected.

Concrete input: frozen cases N1–N3 in `frozen-inputs.md`, plus the changed N1 boundary where the faster option’s harm becomes zero.

## Normative claim

ORIGINAL STATEMENT: “Every beneficial mind-change attempt should maximize efficiency.”

NORMATIVE CLAIM: A mind-change system should select the least costly attempt among attempts that achieve the intended benefit.

CLAIM SCOPE: universal. PRESCRIBES: minimize time or other cost. IMPLICIT AUDIENCE: designers and executors of mind-change attempts. This is prudential and moral: it appeals both to resource conservation and to avoiding needless burden.

## Value analysis

- Primary value: efficiency—obtaining the supported benefit with fewer resources. Type: prudential; stated and widely shared.
- Coupled value: benefit. Type: prudential/moral; stated, but “beneficial” must be independently assessed rather than inferred from speed.
- Constraints: safety and autonomy. Type: moral/prudential; supplied by the cases and not compensable by small time savings.

The program premise supports efficiency, but does not show that efficiency outranks every other value. Someone rejecting the universal says: “An option outside the acceptable harm or autonomy boundary does not become admissible because it is fast.” That is a value objection when the boundary itself is disputed and a factual objection when harm, time, or reversibility is disputed.

## Prescription effectiveness

| Case | Faster option | Competing fact | Result |
|---|---|---|---|
| N1 | saves 10 minutes | severe-harm probability rises from 0.1% to 2% | reject faster option under the supplied risk boundary |
| N2 | saves 30 seconds | removes the user’s veto | reject; autonomy loss is not repaired by speed |
| N3 | same time | one option is reversible, one irreversible | efficiency ties; reversibility selects |
| changed N1 | saves 10 minutes | severe-harm increase becomes zero | faster option becomes admissible and wins |

The original prescription only partially serves its values. It saves resources in changed N1, but misselects N1 and N2 and is silent on N3. Unintended consequence: labeling a fast attempt “maximally beneficial” can hide a noncompensatory violation.

Alternatives:

1. Optimize efficiency only within an admissible set defined by benefit, harm, autonomy, authority, and feasibility constraints.
2. Retain a Pareto set when the constraints do not determine one option; expose the unresolved tradeoff instead of inventing one scalar score.

## Value tensions

1. Safety versus efficiency: safety wins in N1 under the supplied boundary; both are served by the slower safe option. In changed N1 the conflict disappears.
2. Autonomy versus efficiency: the veto-preserving route wins in N2; the 30-second saving cannot compensate for eliminating control.
3. Reversibility versus efficiency: N3 is a time tie, so future correction capacity selects the reversible option.
4. Thoroughness versus efficiency: more work is justified only when it changes admissibility, selection, or verification; otherwise it is waste.

## Verdict

Underlying value: strong. Prescription effectiveness: partial. Competing values addressed: no. OVERALL ASSESSMENT: WEAK as a universal; COMPELLING after qualification.

Strongest version: **For a specified intended change, first exclude attempts that violate supported benefit, harm, autonomy, authority, or feasibility constraints; among the remaining attempts, select an efficient option, retaining an explicit tradeoff set when no option dominates.**

Key objection: admissibility boundaries can themselves consume time, conflict, or be uncertain. Disposition: use the strongest already-supported boundaries proportionate to consequence; do not claim a final boundary when one is unavailable.

## Distinct later use

When N1’s harm increase changes from 2% to zero, the rule selects the faster route. The rule therefore does not merely prefer caution: it changes action when the competing constraint changes. Applied to consolidation design, it rejects the shortest field list if that list drops provenance or the human veto, but allows a shorter indexed view when both are preserved.

## Outcome

Actual mind change: I changed from direct efficiency maximization to constrained efficiency inside an admissible set.

Benefit or harm: The revised rule makes the supplied choice differ in two of four cases and gives a reason for the tie in a third without inventing a common utility scale.

Verdict: KEEP as a refinement and later use of `noncompensatory-value-conflict-by-field-transformation`; not counted as a distinct new discovery.

Content assessment: The normative force, factual dependencies, and noncompensatory conflicts are separated. Human acceptance of the boundaries is unobserved.

Organization assessment: `admissibility → Pareto comparison → efficiency` is more reusable than one weighted score in these cases; where boundaries conflict, preserve the tradeoff.

Next attempts: Elicit a real user boundary; test uncertain harm intervals; test two admissible nondominating routes; measure decision cost; test when added safeguards themselves create delay harm.
