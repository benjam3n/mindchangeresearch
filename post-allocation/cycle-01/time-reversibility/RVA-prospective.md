Intended mind change: Replace the judgment “a refundable reservation makes the whole choice reversible until 09:20” with a component-by-component account of what can actually be rolled back, what merely remains uncommitted, and when the information arrives relative to the irreversible boundary—if the original RVA products support that change.

Actual starting judgment: Reserve machine A at 09:00; because the reservation is refundable through 09:20, treat the whole choice as reversible until then.

Actor: the model's explicit decision policy. No human belief, behavior, learning, emotion, or model-weight change is tested or claimed.

Concrete input: Frozen before evaluation in `../frozen-inputs.md` at 2026-09-08T08:12:00Z and reproduced in `source-receipts/prospective-input.freeze.json` (SHA-256 `15a8f05cbec87702182fec349d483066b2b79959e7173591db28261b4b23bbd4`). At 09:00, A costs $10 and can be reserved with a full refund only through 09:20; B costs $0, its availability is revealed at 09:15, and its stipulated availability is 0.6. Both runs take 20 minutes; completion by 09:40 is hard. Reservation guarantees A's use. Switching/setup time and unpriced reservation cost are zero in the frozen model.

# RVA products

## 1. Commitment being made

Decision: at 09:00, choose among immediate A use, refundable A reservation with delayed machine selection, or reliance on B.

| Choice | Money committed now | Time committed now | Duration | Doors closed | Doors opened |
|---|---:|---:|---:|---|---|
| Start A at 09:00 | $10 | 20 minutes | until 09:20 | Avoiding A's cost; using B for this run | Certain 09:20 completion |
| Reserve A, select at 09:15 | $10 temporarily; $0 if refunded through 09:20 | No run time before selection | reservation until cancel/use | No stipulated machine door before 09:15 | Guaranteed A fallback plus possible free B |
| Rely on B without A | $0 | No run time before 09:15 | until report | Guaranteed completion if B is unavailable | Free completion if B is available |

The reservation commits temporary control of $10 but not the 20-minute run or the final $10 expense. Elapsed clock time is not reversible even while the reservation is financially refundable.

## 2. Reversibility of each option

| Chosen option, then regret | Reversal or exit | Financial cost | Time/effort cost | Relationship/reputation cost | Spectrum |
|---|---|---:|---:|---:|---|
| Start A at 09:00; prefer B at 09:15 | A has already consumed 15 of 20 minutes; abandoning it does not recover the $10 or elapsed time | $10 remains spent | 15 minutes unrecoverable | $0 stipulated | Mostly irreversible after start |
| Reserve A at 09:00; B is available at 09:15 | Cancel A by 09:20 and start B at 09:15 | $0 net | reservation/cancellation effort stipulated as 0 | $0 stipulated | Financially reversible |
| Reserve A; B unavailable | Retain A and start at 09:15 | $10 | no reversal needed | $0 stipulated | Staged commitment |
| Rely only on B; B unavailable | No stipulated fallback remains guaranteed | missed hard requirement | at least the lost completion opportunity | $0 stipulated | Irreversible after the branch is observed |

“Refundable” applies to A's payment. It does not reverse elapsed time, restore an expired latest-start window, or guarantee recovery after the 09:20 boundary.

## 3. Option value

The reserved-A policy preserves two future options at 09:15: free B if available and paid A if unavailable. It eliminates neither before the report. Immediate A use eliminates the chance to avoid $10. B-only eliminates guaranteed completion.

Under the frozen assumptions:

- Reserved-A conditional policy: completion probability `1`; expected charge `0.6($0) + 0.4($10) = $4`.
- Immediate A: completion probability `1`; charge `$10`.
- B-only: completion probability `0.6`; charge `$0`; hard-deadline failure probability `0.4`.

Relative to immediate A, the preserved conditional choice has `$10 - $4 = $6` expected monetary option value while maintaining the stipulated completion requirement. If deadline failure were instead assigned a finite loss `L`, B-only would have expected loss `0.4L`; it would be cheaper than the fallback policy only for `L < $10`, equal at `$10`, and more costly for `L > $10`. The frozen input calls completion hard, so the B-only failure branch is inadmissible rather than silently priced.

## 4. Timing and information

B's report arrives at 09:15 and changes the selected machine on both possible observations. The cost of waiting from 09:00 to 09:15 is no missed deadline under the reservation: either branch can start at 09:15 and finish at 09:35. Waiting beyond 09:20 loses both the A refund and the latest feasible fresh start.

The value of the 09:15 report is therefore `$6` relative to immediate A under the specified monetary-and-hard-deadline objective. The report has value because it arrives before the rollback and latest-start boundaries; reversibility alone does not create the information, and information arriving after the boundary cannot restore reversibility.

## 5. Appropriate decision rigor

The 09:00 reservation is a two-way financial door through 09:20 and requires only minimum viable checks: full refund, guaranteed A access, and cutoff time. The 09:15 cancellation/start decision exhausts the five-minute window and requires the observed B status plus the deadline arithmetic. Reliance on B without A exposes a 0.4 hard-failure branch and therefore fails the required due diligence. No additional person is required by the constructed input; no claim about who should decide in a real institution is made.

## 6. Design for reversibility

1. Reserve A at 09:00 without starting it.
2. Use 09:15 as a checkpoint tied to a directly observed B-availability state.
3. If B is available, start B and cancel A no later than 09:20.
4. If B is unavailable, start reserved A immediately.
5. Do not describe time before 09:20 as reversible: only the payment/reservation is reversible, while feasibility slack declines minute by minute.

This is a staged commitment with a condition-specific exit clause already present in the input. No new contractual feature is invented.

## 7. Timing recommendation

**Reserve A at 09:00; wait for the 09:15 information; then B available → start B and refund A, B unavailable → start A. Act at 09:15 rather than consuming the remaining five-minute buffer.**

The recommendation chooses staged commitment over immediate A use and B-only reliance. Its minimum rigor is verification of the three boundary facts used in the calculation: guaranteed reservation, full refund through 09:20, and 20-minute duration.

## Verification

- Every option has a concrete regret/reversal scenario and spectrum classification.
- Financial, temporal, effort, and stipulated relationship/reputation switching costs are stated for all options.
- Preserved/eliminated options and the `$6` option value are explicit.
- Information value is compared with delay cost and both 09:20 boundaries.
- Rigor differs for the refundable reservation, conditional selection, and hard-failure exposure.
- Reservation, checkpoint, branch rule, and exit are the reversibility design.
- The recommendation is reserve now, conditionally commit at 09:15.

## Distinct later use on a changed input

Changed input fixed by the pre-registered test: A's full-refund cutoff moves from 09:20 to 09:10; B's report remains at 09:15; every other term remains fixed.

At 09:10, the $10 A charge becomes irreversible five minutes before the information exists. Because completion remains hard, A must still be reserved and the $10 accepted by 09:10; relying only on B retains a 0.4 failure branch. At 09:15, choosing free B cannot recover the already committed $10, and no earlier-completion or machine-quality benefit is stipulated. The report's monetary decision value falls from $6 to $0. The changed policy is: reserve A at 09:00, accept the $10 commitment at 09:10, and use A; do not pretend the 09:15 report can reopen the expired refund option. Thus moving only the rollback boundary from after information to before information changes the conditional-commitment rule into commitment before information.

# Result

Actual mind change: The working judgment changed from “the whole choice is reversible until 09:20” to “only A's payment/reservation is reversible through 09:20; elapsed time and deadline feasibility are not.” The operative policy became staged: reserve at 09:00, use information at 09:15, commit to a run then. On the pre-registered 09:10 cutoff variant, the policy commits before the information and assigns the later report zero monetary decision value.

Benefit or harm: Beneficial within the finite model. It prevents “refund available” from being generalized to time reversal, yields a completion-preserving $6 expected option value in the original case, and correctly removes that value when rollback expires before information. Harm was not observed. Post-start failure, transaction duration, and reservation default risk were not stipulated and remain outside scope.

Verdict: **KEEP (scoped).** The decisive evidence is the order `reservation → information → refund/latest-start boundary` in the original input and `reservation → refund boundary → information` in the changed input. The strongest contrary branch is that reservation and waiting could be treated as no commitment at all; the temporary $10 control and the irrecoverable passage of time make that exact claim false even though the final expense remains reversible.

Performative check: Not merely a new label. The procedure separated three commitments, supplied four regret scenarios with switching costs, calculated option value, changed the selected action relative to immediate A, and changed the commitment rule when one pre-registered cutoff moved.

Novelty assessment: The corpus already contains generic rollback, option-value, and latest-start ideas. The retained addition is the tested ordering relation: information has selection value only while an action capable of using it remains feasible, and a refundable payment does not make elapsed feasibility reversible. Moving a single cutoff produced a different policy without revising the objective. Corpus search found no prior machine/refund calculation or explicit comparison of information-before-rollback with rollback-before-information. This is a scoped operational finding, not proof for all reversible decisions.

Content assessment: All seven RVA steps and all seven verification requirements are present with concrete products. The original RVA source specifies no numerical 8x floor; this record expands the scope through three options, four regret cases, explicit threshold arithmetic, and a changed-input reuse but does not claim “8x certification.”

Organization assessment: `commitment object → reversal scenario → option value → timing → rigor → design → recommendation` preserved the original dependency order. Separating payment, run time, feasibility, and information in tables prevented one “reversibility” score from erasing distinct boundaries. The later-use section makes transfer visible without mixing it into the first result.

Next attempts: Give A a nonrefundable reservation fee and derive the exact fee threshold; add a 3-minute switching time and test whether B information at 09:18 is usable; add a probability that a reservation fails and compare guarantee value with refund value; let the deadline penalty be finite and test the `L = $10` boundary prospectively; introduce a post-start B failure state and test whether delaying A cancellation preserves a second-stage fallback.
