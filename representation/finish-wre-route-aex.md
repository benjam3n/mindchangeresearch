Intended mind change: Replace an unexamined preference for adding route words with explicit assumptions that determine whether a relative-command continuation is executable.

# AEX dependency — route checkpoint

Input claim: “A checkpoint that stores position, heading, and an ordered relative-command suffix determines one endpoint under a fixed decoder.” Interpretation: audit assumptions in a proposed technical writing artifact. Actor: this model; evidence: stipulated integer-grid fixtures; no reader response.

Core claims: C1 the checkpoint state is sufficient for relative decoding; C2 the suffix order changes permitted endpoints; C3 adding body-turn prose improves a human reviewer’s accuracy.

| ID | Assumption | Type | Hiddenness | Risk if wrong | Test |
|---|---|---|---|---|---|
| A1 | Position is an ordered pair on the declared x/y grid. | knowledge | surface | high | inspect schema |
| A2 | Heading is one of north/east/south/west. | existence | shallow | high | inspect decoder domain |
| A3 | F advances one unit in the current heading. | knowledge | shallow | high | execute one-token cases |
| A4 | R and L rotate by one quarter-turn. | knowledge | deep | high | mirror fixture |
| A5 | Commands are decoded left to right. | stability | deep | critical | FRF versus RFF |
| A6 | The saved position and heading refer to the same point in one route instance. | existence | buried | critical | bind checkpoint identity |
| A7 | The suffix begins after, not before, the saved checkpoint. | timing | deep | high | compare prefix/suffix trace |
| A8 | Axes and handedness remain fixed while decoding. | stability | buried | critical | axis/mirror cases |
| A9 | The decoder is available to the recipient. | access | deep | high | omit versus include legend |
| A10 | The recipient can distinguish relative from compass commands. | capability | buried | high | external reader task |
| A11 | The route is evaluated for endpoint, not forbidden intermediate points. | value | deep | high | two paths, same endpoint |
| A12 | Every token belongs to the fixed codebook. | permission | shallow | high | reject unknown token |
| A13 | Coordinates use exact unit lengths rather than “nearby.” | knowledge | deep | high | nearby={1,2} countercase |
| A14 | A route name or index is bound to this route instance. | existence | buried | high | two instances, same index |
| A15 | No concurrent writer mutates the checkpoint during decoding. | stability | deep | medium | version precondition |
| A16 | Additional turn wording does not conflict with the coordinate instruction. | causal | buried | critical | east versus body-right conflict |
| A17 | Extra wording is valued only if it changes a defined outcome. | value | deep | medium | equal-endpoint comparison |
| A18 | Human accuracy can be known only from an actual reader comparison. | access | buried | critical | deferred reader study |

Dependency chains: A18 → actual participant access → paired answers → scored endpoints → comparative accuracy (five layers; deferred). A6 → route identity → checkpoint identity → shared coordinate frame → deterministic token lookup (five layers; locally inspectable). A5 → preserved order → turn-before-move state → displacement sequence → endpoint (five layers; tested).

Categories represented: causal, existence, stability, access, capability, value, knowledge, permission, timing. Hidden assumptions: A4–A11 and A14–A18 are deep or buried; six-assumption minimum exceeded.

Immediately/already tested: A1–A9, A11–A16 via `finish-fixture-results.json`, `resume-wre-local-tests.json` and the ARAW countercases. The r1/r2 guard aborts without using the mutated checkpoint. Deferred: A10, A17, A18 require a real reader and a stated accuracy comparison. Priority: A6, A8 and A16 prevent symbolic misdecoding; A18 prevents upgrading a local result into a human effect.

Ten-question coverage by claim:

| Claim | Causal | Existence | Stability | Access | Capability | Value | Knowledge | Resources | Permission | Timing |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | A3,A4,A16 | A2,A6,A14 | A5,A8,A15 | A9 | A10 | A11 | A1,A13 | no distinct resource beyond supplied card/decoder | A12 | A7 |
| C2 | A3–A5 | A6 | A5,A8 | A9 | A10 | A11 | A1,A3,A4 | no distinct resource dependency | A12 | A7 |
| C3 | A16 | no additional entity beyond reader/task | A8,A15 | A18 | A10 | A17 | outcome definition in A17 | real reader/task materials are part of deferred A18 | no additional permission claim | paired-condition timing is part of deferred A18 |

Summary: 3 claims; 18 assumptions; types—knowledge 4, existence 3, stability 3, access 2, capability 1, value 2, permission 1, timing 1, causal 1. Hiddenness—surface 1, shallow 3, deep 8, buried 6; 14 deep/buried assumptions. High/critical assumptions: 16; priority assumptions: A6, A8, A16, A18.

Assumption map: C1 depends on A1–A9, A12–A15; C2 depends on A3–A5, A7–A8; C3 depends on A9–A10, A16–A18. C1 and C2 survive the declared fixtures. C3 remains unresolved.

Actual mind change: The route artifact is now conditioned on a fixed decoder, shared frame, bound route instance and ordered suffix; extra prose no longer counts as improvement by itself.

Benefit: The assumptions define executable symbolic checks. Human endpoint accuracy remains unobserved.

Verdict: KEEP as a completed AEX dependency; repeated scope rules receive no separate discovery credit.

Organization: Claims → eighteen assumptions → five-layer dependencies → testability and priority.

Next attempts: Test concurrent checkpoint mutation; obtain a paired reader comparison before making an accuracy claim.
