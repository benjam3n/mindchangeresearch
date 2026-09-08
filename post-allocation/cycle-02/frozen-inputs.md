# Cycle 02 prospective freeze

Freeze time: 2026-09-08T09:14:00Z. No cycle-02 result or consolidation existed when these inputs and criteria were fixed.

Program state: the frozen initial obligation remains 233 complete, 66 partial, and 1 blocked; GOSM is 10/10. Cycle 01 left three unconsolidated findings: `query-history-location-policy`, `lossless-does-not-determine-retrieval-cost`, and `proposal-log-versus-bidirectional-trace`.

## PBR — correlated alarms

Intended mind change: Replace an intuitive two-confirmation update with a calibrated update that respects evidence dependence.

Starting judgment: Two positive alarms feel substantially stronger than one, but I have not computed whether they are independent.

Concrete input: hypothesis D is “component defective.” Prior P(D)=0.10. An alarm has P(A|D)=0.80 and P(A|not-D)=0.20. A1 and A2 are two dashboard fields copied from the same sensor event, so A1=A2 in every state. Both display positive. Replacement occurs only if posterior P(D)>0.50; otherwise inspect. Compare the duplicated-field update with an independence-assumed update. Success requires explicit odds/LR arithmetic, alternatives summing to one, an action, and a boundary case.

## ARAW 8x — transition-first universal

Intended mind change: Determine whether the cycle-01 transition-first rule survives a genuinely adversarial belief-correction case or needs a scoped repair.

Starting judgment: The rule was useful in two prior constructed cases, but its phrase “select the state transition” may permit a direction-laden target that anchors the answer.

Exact frozen claim C0: “For every belief update in this program, selecting the intended state transition before selecting a reasoning skill weakly reduces decision error compared with selecting the reasoning skill first.”

Concrete test input: the correlated-alarm case above. Transition-first Run T receives the target “increase confidence that D is defective” before method selection. Skill-first Run S receives only the evidence and decision rule, then applies PBR. A repaired transition target may be derived only after C0 is tested. Success requires the original 8x floors: at least 18 claims, 55 nonduplicated findings, 6–8 recursive edges on live branches, eight cruxes, and two executed tests. A counterexample to C0 rejects C0; it may not be relabeled a universal conditional.

## SATRDA — two-run selector stability

Intended mind change: Find whether the current transition-gate card has a repeatability defect on a fixed belief input.

Starting judgment: The card is concise and useful, but “smallest supported transition” does not define whether a belief transition names a direction, a representation, or an evaluation criterion.

Concrete input: run the cycle-01 transition-gate card twice on the alarm case, once fresh each time. Required output fields: target transition, locus, evidence gate, chosen skill, posterior, action, unresolved dependency. Stopping rule: two runs, one comparison, one rewrite queue. Divergence is a defect signal, not proof that either output is false.

## PRCP — mixed observation log

Intended mind change: Restore literal observations that a fluent incident summary turns into inferred causes.

Starting judgment: I initially read the log as evidence that the operator ignored a warning.

Concrete input: `09:00 sensor S reports HIGH; 09:01 dashboard D shows NORMAL; 09:02 operator note says “checked D; no action”; 09:04 S reports HIGH; no acknowledgment field is present; 09:06 automated shutdown.` Success requires two literal reads, observations, patterns, absences, O/I/A audit, restored filtered items, and a later incident-description use that does not claim the operator saw S.

## VCD — privacy versus auditability

Intended mind change: Replace a single weighted score with a navigable policy when privacy and auditability impose different noncompensatory constraints.

Starting judgment: I expect a weighted retention score to rank four record types, but I do not know whether a low privacy score should be compensable by audit value.

Concrete input: R1 public decision rationale (audit 5, privacy risk 0); R2 named medical detail irrelevant to decision (audit 1, privacy risk 5); R3 pseudonymous evidence summary necessary to reproduce decision (audit 5, privacy risk 2); R4 contributor contact data needed only for possible follow-up (audit 2, privacy risk 4). Goal: preserve reproducibility and prevent unnecessary personal-data exposure. Produce a concrete policy, success criteria, risk mitigations, pivot triggers, and a second use on R5: an anonymous dissent whose content is required to understand a rejected option.

## DWT — checksum stopping decision

Intended mind change: Stop analysis using an external decision criterion instead of a feeling of completeness.

Starting judgment: A third integrity check feels safer even though two checks already agree.

Concrete input: release deadline is 09:32; now is 09:20. Two independently implemented SHA-256 checks over the same 5 MB archive match the expected digest. A third remote check takes 10 minutes, leaving 2 minutes for a 4-minute release procedure. If the archive is not released by 09:32, the opportunity expires; if a mismatch is detected before release, release must stop. Current leading action: begin release. Mind-change trigger: credible evidence that the first two checks share an implementation or byte-source failure. Success requires the applicable original branch, a written decision, rationale, and boundary where the action changes.

## ALT — one record, two abstraction needs

Intended mind change: Stop treating one maximally compressed representation as best for both action and audit.

Starting judgment: A six-line summary seems more efficient than the 24-row event record.

Concrete input: the event record contains 24 timestamped rows, including four state transitions and one rollback. Query Q1 asks “what action is authorized now?” Query Q2 asks “which prior field caused the rollback?” Candidate levels: L0 raw rows; L1 state-transition table; L2 six-line narrative. Success requires selecting levels for Q1 and Q2, testing information loss, and using the selected representation on both queries.

## ECAL — unequal reasoning budget

Intended mind change: Allocate effort by decision consequence and action divergence rather than giving every open question equal analysis.

Starting judgment: Equal time per question is procedurally tidy.

Concrete input: 30-minute budget and three questions. E1: whether a title should use “and” or “&” (reversible, no downstream dependency). E2: whether a result computed under criterion C0 can be merged into accepted criterion C1 (irreversible publication risk, known incompatibility signal). E3: whether a delayed human reader will retain a lesson (important but no observation can arrive within 30 minutes). Success requires original triage, explicit section assignments/time budgets, executed analysis within the declared budget model, and a second use after swapping E1 and E2 labels while keeping their properties.

## CAPG — capability is step-local

Intended mind change: Replace whole-task “can/cannot do” labels with requirement-local capability classifications.

Starting judgment: “Validate the field report” reads like one task and tempts one capability label.

Concrete input: steps are (a) recompute totals from an attached CSV, (b) inspect a physical seal in Chicago, (c) email the named owner for confirmation, but no email connector or verified recipient identity is available, and (d) decide whether the evidence warrants publication. Budget is $0 and deadline is 30 minutes. Success requires requirement analysis, exact capability categories, costs/prerequisites, transformations or gates, success criteria, and a later use after a photograph of the seal becomes available but no custody proof accompanies it.

## Consolidation trigger

If and only if PBR or another cycle-02 attempt demonstrates a genuinely distinct fourth finding, consolidate it with the three cycle-01 findings. Compare at least two organizations on a separately frozen reuse case, include a boundary where evidence must not be combined, and preserve provenance. Do not count ARAW’s repair of transition-first as the fourth unless it is demonstrably independent of the earlier transition-gate consolidation.
