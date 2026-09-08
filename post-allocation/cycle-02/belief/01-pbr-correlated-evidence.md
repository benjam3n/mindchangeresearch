# PBR — correlated evidence changes the action

Intended mind change: Replace an intuitive two-confirmation update with a calibrated update that respects evidence dependence.

Actual starting judgment: Two positive dashboard fields felt substantially stronger than one; I had not checked whether they were distinct observations.

Concrete input: `frozen-inputs.md`, PBR case. D has prior 0.10. Each alarm event has sensitivity 0.80 and false-positive rate 0.20. A1 and A2 are copied from the same sensor event and are equal in every state. Replacement requires posterior above 0.50.

## Precise hypothesis and base

H: this component is defective at the decision time. Verification in the constructed model is the component’s binary D/not-D state. The supplied component population is the only supported reference class; P(D)=0.10. No second empirical class is available, so none is invented. Prior odds are `0.10/0.90 = 1/9`.

## Evidence register

| Item | Direction | P(item|D) | P(item|not-D) | LR | Dependence |
|---|---:|---:|---:|---:|---|
| Sensor event is HIGH | supports D | 0.80 | 0.20 | 4 | one event |
| A1 displays HIGH | supports D | 0.80 | 0.20 | 4 | deterministic copy of event |
| A2 displays HIGH | supports D | 0.80 | 0.20 | 4 | deterministic copy of same event and A1 |
| No independent sensor | neutral as observed; informative absence | — | — | 1 | prevents a second independent update |

The diagnostic evidence is one positive event, not two. The two fields add display redundancy but no new likelihood factor.

## Updates

Correct dependent update:

`posterior odds = (1/9) × 4 = 4/9`

`P(D|A1=A2=HIGH) = (4/9)/(1+4/9) = 4/13 = 0.307692`

Independence-assumed update:

`posterior odds = (1/9) × 4 × 4 = 16/9`

`P_independent(D|two HIGH fields) = (16/9)/(1+16/9) = 16/25 = 0.64`

The independence assumption crosses the 0.50 replacement threshold; the stated joint structure does not.

## Alternatives and action

The exhaustive binary hypotheses are D with posterior `4/13` and not-D with posterior `9/13`; they sum to one. A separate hypothesis “dashboard duplicated a single event” is observed in the supplied data structure rather than a third component-state alternative.

Action: inspect; do not replace. A bet paying 1 on D is unattractive above a price of `4/13` under the supplied model. The estimate is exact conditional on the given prior and likelihoods; uncertainty about whether those parameters describe a real component remains outside this constructed case.

Update cruxes: a genuinely independent second sensor, a changed prior, or a changed replacement threshold.

## Distinct later use and boundary

Later input: A2 is changed from a copied field to an independent sensor with the same sensitivity and false-positive rate, conditionally independent given D.

Now the second LR is admissible: posterior becomes `16/25 = 0.64`, so the action changes to replace. If the threshold were `0.30`, even one event’s `4/13` would trigger replacement. Thus evidence count, evidence dependence, and action loss/threshold remain separate.

## Outcome

Actual mind change: My working posterior changed from an uncomputed “two confirmations, likely replace” impression to `4/13` and inspect. I now treat provenance/dependence as part of an evidence item’s inferential identity, not metadata added after counting.

Benefit or harm: The corrected update avoids a threshold-crossing false amplification in the frozen case. It also supplies a boundary in which a truly independent second observation legitimately changes the action. No human belief or real equipment state changed.

Verdict: KEEP — complete within the finite supplied probability model. `evidence-dependence-before-aggregation` is a distinct new finding.

Content assessment: The arithmetic, alternatives, action, dependence condition, and boundary are checkable. Empirical calibration of the supplied rates remains untested.

Organization assessment: `hypothesis → base → evidence/provenance → joint update → loss threshold → action` was more reusable here than listing positive fields before their dependency relation.

Next attempts: Test partially correlated alarms rather than perfect copies; estimate sensitivity to uncertain likelihoods; compare a provenance graph with a flat evidence list on retrieval time; score prospective real predictions when outcomes become observable.
