Intended mind change: Replace live-position shorthand with an explicit account of the assumptions required to target the same items across destructive edits.

# AEX dependency — edit targeting

Input claim: “Resolving original item references to unique stable IDs before mutation preserves the intended targets of delete-A/tag-B across list reordering.” Interpretation: audit assumptions in a proposed technical writing artifact. Actor: this model; evidence: stipulated list fixtures; no editor response.

Core claims: C1 pre-resolved IDs preserve targets across deletion and reordering; C2 the revision can be atomic after preflight; C3 ID wording improves a human editor’s accuracy.

| ID | Assumption | Type | Hiddenness | Risk if wrong | Test |
|---|---|---|---|---|---|
| A1 | A, B and C are record identities, not display positions. | knowledge | surface | high | inspect input |
| A2 | IDs are unique in the live document. | existence | deep | critical | duplicate-ID fixture |
| A3 | The request binds to the original snapshot. | timing | buried | critical | live/original fixture |
| A4 | Delete and tag resolve selectors before mutation. | timing | deep | critical | preflight comparison |
| A5 | Deleting A does not rename B. | stability | shallow | high | execute ID edits |
| A6 | Reordering changes position but not identity. | stability | deep | high | reordered held-out fixture |
| A7 | The editor can access the original identity map. | access | buried | critical | absent-map case |
| A8 | The editing system can select by ID. | capability | deep | high | execute ID operations |
| A9 | Failure on a missing or duplicate target occurs before mutation. | timing | buried | critical | preflight/late failure |
| A10 | Partial mutation is undesirable for this request. | value | deep | high | compare failure states |
| A11 | Tagging B and deleting A are independent when A≠B. | causal | deep | high | order both ID edits |
| A12 | The requested final state is B tagged, C unchanged, A absent. | value | surface | high | exact final-state assertion |
| A13 | Visible text need not uniquely identify a record. | existence | deep | high | duplicate-text fixture |
| A14 | The document version still represents the same task. | stability | buried | critical | task/version precondition |
| A15 | The actor has permission to delete A and tag B. | permission | shallow | high | authorization input |
| A16 | Retrying the patch does not reinterpret a live ordinal. | causal | buried | high | repeat positional deletion |
| A17 | Accuracy means correct target selection, not typing speed. | value | deep | medium | define outcome |
| A18 | Human accuracy requires observed editor selections. | access | buried | critical | deferred editor study |

Dependency chains: A3 → original snapshot → ordinal-to-ID resolution → unique-match preflight → atomic mutation (five layers; locally tested). A14 → task version → request identity → permitted target set → final-state assertion (five layers; one dependency remains an external input). A18 → editor access → paired instructions → observed selections → comparative accuracy (five layers; deferred).

Categories represented: causal, existence, stability, access, capability, value, knowledge, permission, timing. Hidden assumptions: A2–A4, A6–A11, A13–A14, A16–A18 exceed the six-assumption floor.

Immediately/already tested: A1–A14 and A16 via `finish-fixture-results.json`, `resume-wre-local-tests.json` and the ARAW registry. Version mismatch and missing B both abort without changing the input. A15 needs actual authorization input. Deferred: A17’s human relevance and A18 require an editor comparison. Priority: A2, A3, A4 and A9 decide whether the actual objects survive the mutation sequence.

Ten-question coverage by claim:

| Claim | Causal | Existence | Stability | Access | Capability | Value | Knowledge | Resources | Permission | Timing |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | A11,A16 | A2,A13 | A5,A6,A14 | A7 | A8 | A12 | A1 | no distinct resource beyond supplied snapshot | A15 | A3,A4 |
| C2 | unchanged-on-failure consequence of A9 | A2 | A14 | A7 | A8 | A10,A12 | A1 | no distinct resource dependency | A15 | A4,A9 |
| C3 | selector wording→selection claim | editor/task exists within A18 | A6,A14 | A18 | A8 | A17 | A1,A3 | paired documents/edit interface are part of deferred A18 | participant permission belongs to deferred study | paired-condition timing belongs to deferred study |

Summary: 3 claims; 18 assumptions; types—knowledge 1, existence 2, timing 3, stability 3, access 2, capability 1, value 3, causal 2, permission 1. Hiddenness—surface 2, shallow 2, deep 8, buried 6; 14 deep/buried assumptions. High/critical assumptions: 17; priority assumptions: A2, A3, A4, A9.

Assumption map: C1 depends on A1–A8, A11–A14, A16; C2 depends on A2, A4, A9–A12, A15; C3 depends on A7–A8, A17–A18. C1 and C2 survive the declared fixtures. C3 remains unresolved.

Actual mind change: The edit artifact now binds ordinals in the named initial snapshot, checks unique live IDs before mutation, and states the exact final state.

Benefit: The assumptions make the fixture’s positional noncommutativity testable. Human editing accuracy remains unobserved.

Verdict: KEEP as a completed AEX dependency; repeated identity/scope rules receive no separate discovery credit.

Organization: Claims → eighteen assumptions → five-layer dependencies → testability and priority.

Next attempts: Add a task/version mismatch fixture; obtain paired editor selections before making an accuracy claim.
