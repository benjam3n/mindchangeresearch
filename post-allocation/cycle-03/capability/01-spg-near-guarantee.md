# SPG — replace a vague near-guarantee with an implementable test

Intended mind change: Stop treating “a good recipe near-guarantees success even with a mediocre executor” as an implementation-ready capability claim.

Actual starting judgment: The cooking analogy seemed specific enough to govern system design.

Concrete input: original claim plus the boundary case of a physical relocation requested from a text-only model.

## Specificity gate result

### Original claim and type

“A good mind-change recipe near-guarantees success even with a mediocre executor.” Type: CAPABILITY with an embedded property claim.

### Element status

- TRIGGER: MISSING — eligible request, inputs, authority, and risk conditions are unspecified.
- PROCEDURE: MISSING — “good recipe” and what the executor must do are unspecified.
- OUTPUT: MISSING — success could mean a plan, attempt, changed state, action, or durable effect.
- VALIDATION: MISSING — “near-guarantees,” comparison class, witness, time horizon, and harms are undefined.

### Questions and concrete options

| Question | A | B | C |
|---|---|---|---|
| What triggers compilation? | every user request | only a request with a frozen target state and witness | only an evaluator-selected benchmark case |
| What cases are eligible? | all mind changes | cases with available inputs and supported authority | finite text-only belief cases |
| What procedure is mandatory? | one named skill | typed recipe compiler | fixed catalog lookup |
| What output counts? | polished response | attempt plus transition receipt | changed target state observed later |
| What is success? | executor says KEEP | preregistered witness passes and no veto condition occurs | recipient reports satisfaction |
| What means “near”? | any high rate | a prespecified lower confidence bound | a fixed 95% threshold |
| How is mediocre executor defined? | informal judgment | held-out executors below a frozen baseline band | deliberately degraded model |
| What happens at unavailable physical gates? | call plan success | emit typed handoff and UNRESOLVED target | exclude the case |

Options are design alternatives, not observed facts. For prospective testing, choose: frozen target/witness; supported inputs and authority; typed compiler; attempt plus shape-specific receipt; prespecified statistical threshold; held-out executor band; typed handoff for unavailable gates.

## Specific replacement claim

TRIGGER: When a new request has a frozen target state, a named transition locus, a preregistered success witness, available evidence inputs, and an authorized action boundary. Detected by a four-field eligibility record plus risk/authority checks.

PROCEDURE:

1. Exclude attempts violating supported benefit, harm, autonomy, authority, or feasibility constraints.
2. Diagnose the controlling locus from intermediate evidence rather than final output alone.
3. Specify state variable, locus, criterion, operator, preserved invariant, and witness.
4. Select a message, technique, tool, or handoff capable of executing that operator at that locus.
5. Execute only the authorized available component.
6. Verify with the preregistered shape-specific witness; record downstream action separately.

OUTPUT: one JSON-compatible transition record containing `case_id`, `eligibility`, `admissibility`, `pre_state`, `target_state`, `locus`, `operator`, `invariant`, `mechanism`, `authority`, `attempt_receipt`, `success_witness`, `observed_post_state`, `adverse_events`, `downstream_action`, and `status`.

VALIDATION: On a prospectively frozen held-out case set and frozen executor band, success occurs only when the case-specific witness passes and no veto-level harm or unauthorized transition occurs. “Near-guarantee” is accepted only if a threshold and confidence rule are fixed before data and met on the held-out set. No threshold is asserted as achieved here.

### Implementation check

| Check | Result |
|---|---|
| programmer can implement the complete recipe without supplying missing intellectual operations | UNRESOLVED: diagnosis and mechanism construction are not implemented by the field schema |
| each step has sufficient operational content | PARTIAL: named inputs and outputs constrain the interface but do not determine the missing transformation |
| output format specified | PASS |
| validation measurable | PASS prospectively; efficacy UNRESOLVED |

Implementation correction from the 2026-09-08 intent audit: this record completes a specificity exercise and supplies a prospective schema. It does not establish an executable general recipe. [Contribution construction](../../../mind-change/contribution-construction.md) supplies conditional operations; [the audit](../../../research/intent-audit.md) preserves the exact earlier PASS claims. The original procedure source and execution history remain unchanged.

## Boundary case

Request: “Move me from the living room to the quiet room” sent to a text-only model with no actuator or human execution receipt. Eligibility for direct relocation fails at feasibility/authority. The valid output is an interface plan or typed handoff with target status UNRESOLVED—not a successful location change. A recipe that always reports success here is bad regardless of prose quality; a good recipe cannot make an incapable executor perform the physical edge.

## Outcome

Actual mind change: I changed from a broad chef/recipe near-guarantee to a more specific prospective claim with an explicit implementation gap and unavailable execution edges.

Benefit or harm: The replacement prevents plan quality from being counted as physical success and supplies a record structure for later testing. It proves no success rate.

Verdict: REJECT the original as nonspecific; KEEP the testable specification; UNRESOLVED mechanism implementation and whether any near-guarantee threshold is attainable.

Content assessment: Trigger, procedure, output, validation, threshold timing, executor definition, and nonapplication boundary are explicit.

Organization assessment: Capability claims belong after eligibility and authority checks; the recipe may compensate for selection/execution variance only inside the executor’s available transition set.

Next attempts: Define a held-out executor band; preregister a threshold; test an actuator-enabled case; test a recipient-controlled case; measure failure calibration rather than success alone.
