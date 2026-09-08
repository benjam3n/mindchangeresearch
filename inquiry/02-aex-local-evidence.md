Intended mind change: Determine whether the new scoped-keep proposition warrants a stronger benefit or causal claim, and alter the next investigation’s attribution target if it does not.

# AEX 01 — source fidelity, local use, and transfer

Input: “A source-faithful, depth-sufficient execution that changes the present model’s next choice can qualify as a local keep even when human transfer remains unresolved.” The candidate instance is AR 01’s continuation queue. Actor: the current inquiry assistant. Starting judgment: the new scope fields seem useful, but I had not separated evidence that the fields help from evidence that original AR caused their helpfulness.

Core claims: C1 the candidate is a source-faithful and depth-sufficient execution; C2 its changed next choice can qualify as a useful local change; C3 unresolved human transfer is compatible with that local qualification. These are instance premises, not a claim that every changed choice is useful.

Source: ../sources/inquiry-aex.original.md and ../sources/inquiry-aex.requirements.txt. 8x floor: 18 assumptions, five layers, seven categories, six hidden assumptions. Actual: 30 distinct premises/constraints, all ten source categories applied to each core claim, 15 Deep and six Buried entries, and chain A1→A2→A3→A4→A5→A6 (five prerequisite edges). Causal entries identify an extra premise needed for causal attribution, not a necessary premise for merely observing a change.

| ID | Core | Type | Hiddenness | Risk if wrong | Assumption / required distinction | Requires | Testability and evidence |
|---|---|---|---|---|---|---|---|
| A1 | C1 | Capability | Deep | High | The present actor can identify which required original operations the output actually performs. | A2 | Effort: match operations to source; the receipt alone is insufficient. |
| A2 | C1 | Knowledge | Deep | High | That identification depends on understanding input-sensitive instructions, including subordinate invocations. | A3 | Now: inspect named invocation clauses in each loaded source. |
| A3 | C1 | Access | Shallow | High | The input-sensitive instructions are available as emitted source bytes. | A4 | Tested: inquiry-ar.original.md is locally readable. |
| A4 | C1 | Existence | Surface | High | The emitted bytes correspond to the identified original archive member. | A5 | Now: compare source digest in the separately emitted requirements receipt. |
| A5 | C1 | Stability | Buried | High | The digest comparison refers to the bytes actually used in this application, not another copy or a later revision. | A6 | Now: digest the preserved stdout file and compare its exact receipt. |
| A6 | C1 | Timing | Deep | High | The source was loaded before the claimed execution rather than attached retrospectively. | — | Tested: tool transcript loads ar before write_ar01.py runs. |
| A7 | C1 | Resources | Shallow | Medium | The actor has enough context and work capacity to execute the source operations rather than only list their names. | — | Effort: inspect actual products; available byte count is no proxy. |
| A8 | C1 | Permission | Surface | Low | The assignment authorizes reading original material and changing the actor’s own working files. | — | Tested: working-instruction.md and delegated scope. |
| A9 | C1 | Value | Deep | Medium | Original fidelity remains part of the requested benefit even when a shorter ordinary operation appears adequate. | — | Tested as request, not universal value: original-depth instruction. |
| A10 | C1 | Causal | Buried | High | Any claim that source fidelity produced the useful effect needs evidence beyond the fact that a source preceded the effect. | — | Effort: compare equivalent input with a credible ordinary continuation; causation unresolved. |
| A11 | C2 | Existence | Surface | High | There is a distinct later operation whose observable input or output can be compared with the starting working judgment. | — | Tested: continuation-queue.json and the present AEX input are distinct from the AR tree. |
| A12 | C2 | Causal | Deep | High | A difference between outputs is not itself proof that the difference is useful for the user’s concern. | — | Now: inspect which uncertainty or decision the difference resolves. |
| A13 | C2 | Value | Deep | High | The consequence preserves a concern supported by the request rather than substituting document production as the criterion. | — | Tested: actor/scope distinctions answer the request; numerical skill efficacy remains untested. |
| A14 | C2 | Knowledge | Shallow | Medium | The actor can state its credible pre-application choice without inventing a worse one after seeing the result. | — | Tested only by transcript chronology and the initial record, not independent memory validation. |
| A15 | C2 | Stability | Buried | High | The before/after comparison refers to the same decision obligation even if the representation changes. | — | Now: compare rank allocation with queue order; requested application identities remain constant. |
| A16 | C2 | Capability | Shallow | Medium | The actor can separate a revised working representation from changes to model weights. | — | Tested in present wording; no future reliability conclusion. |
| A17 | C2 | Access | Deep | High | A later consumer can reach the scoped finding when making its actual choice. | — | Tested: this AEX consumes AR’s explicit next input; future retrieval is unresolved. |
| A18 | C2 | Timing | Buried | High | A record does not count the anticipated success of its next procedure as an already observed result. | — | Tested: the AR limits its observation to construction/queue, not AEX success. |
| A19 | C2 | Resources | Shallow | Medium | The extra fields do not displace content whose loss changes the decision materially. | — | Effort: compare full and compact later use; not settled by current input. |
| A20 | C2 | Permission | Surface | Low | The actor can revise its queue while retaining all assigned obligations. | — | Tested: delegated task explicitly permits dependency-sensitive reorder. |
| A21 | C3 | Knowledge | Buried | High | Unresolved human transfer is not silently used as an argument that local model evidence is worthless. | — | Now: local decision and human effect remain separate propositions. |
| A22 | C3 | Existence | Surface | High | No performed human intervention appears in this local record. | — | Tested: available transcript concerns model/file operations only. |
| A23 | C3 | Causal | Deep | High | The record’s lack of human observation does not establish that the candidate has no human effect. | — | Logic: absence of a performed test leaves effect unresolved. |
| A24 | C3 | Value | Deep | Medium | A locally useful model operation is within the user’s allowed target space. | — | Tested: working-instruction.md explicitly includes model working state. |
| A25 | C3 | Stability | Shallow | Medium | The local label continues to refer to this run when copied into a later collection. | — | Effort: actual consolidation query, not yet run. |
| A26 | C3 | Timing | Deep | Medium | Later evidence can revise transfer judgment without rewriting what happened in the current run. | — | Logic: historical observation and later applicability differ. |
| A27 | C3 | Access | Buried | High | Human-effect evidence would need an available channel suited to the claimed outcome; model self-report cannot supply that channel. | — | Now: current tool inventory and transcript supply no performed human outcome. |
| A28 | C3 | Capability | Shallow | Medium | The model can preserve the unanswered transfer proposition while continuing authorized local work. | — | Tested: this document proceeds and labels transfer unresolved. |
| A29 | C3 | Resources | Deep | Medium | No human assessment burden is imposed merely to make this local result count. | — | Tested: no user questionnaire or intervention is sent. |
| A30 | C3 | Permission | Surface | High | Authorization for research files does not by itself authorize person-directed intervention. | — | Tested: assignment authorizes this bounded file work; no person-directed action is performed. |

Root dependencies: A6 roots the source-timing chain; A7–A30 have no deeper prerequisite established here. The chain is epistemic access, not a claim that a digest causes correct reasoning. A1 needs correct instruction understanding; A2 needs the instruction content; A3 needs identifiable source bytes; A4 needs the matching bytes; A5 needs their chronology. Failure of the weaker evidence premise removes the claimed verification, not the underlying source’s existence.

Priority: A12 controls the distinction between difference and benefit; A10 controls source-to-effect causal attribution; A25 controls later scope. A12 is inspected against the present AEX output: the scope fields separate three propositions that would otherwise admit different evidential conclusions. A10 remains untested because no ordinary-continuation counterfactual was performed. A25 awaits actual consolidation. No premise is labeled inherently untestable; absent human observations are unavailable now, not metaphysically inaccessible.

Distinct later operation: the next causal-claim input is now “AR’s source-specific recursion caused the useful field separation, beyond the separation already requested in the brief.” Its rival is “The brief and ordinary input construction were sufficient; AR supplied an inspectable route but no demonstrated marginal cause.” This replaces the looser “Did AR work?” target with a discriminating attribution claim. Causal attribution is now UNRESOLVED while the visible field separation remains an observed local output.

Certificate: exact conclusion—this record does not establish AR-specific causal benefit. Decisive premise A10: chronology plus one output does not identify the counterfactual ordinary continuation. Inference: preserve the observed change and withhold the source-specific causal conclusion. Strong contrary branch: AR explicitly derived and used the fields; that supports a plausible mechanism and temporal sequence but not the missing comparison. Remaining dependency: a credible ordinary-continuation comparison.

Actual mind change: Causal attention moves to the marginal contribution of AR beyond the explicit brief; the next CSCL input now includes that rival.
Benefit: The causal test will assess a claim that can fail on a concrete alternative account. This is a distinct attribution-target change, not another keep for actor/scope field separation.
Verdict: UNRESOLVED — the discriminating target is constructed, but its causal result remains untested and the distinction is already required by the brief. No new keep credit.
Organization: Assumptions are grouped by the three core claims, with all ten extraction categories visible. The causal-attribution target is separately retained for actual later CSCL use. New keep ledger 0/4.
Next attempts: Execute CSCL on the source-specific causal claim; test source-byte assumptions; use DD to vary targets beyond evidential beliefs; inspect whether a compact keep preserves this unresolved rival.
