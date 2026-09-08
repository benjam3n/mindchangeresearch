# Timing can determine which improvements remain possible

For two nonpreemptive tasks on one processor, let A release at zero with duration a and deadline dA; let B release at r≥0 with duration b and deadline dB. There are two possible task orders. Their earliest schedules suffice to determine feasibility: delaying a task further cannot help either deadline within its fixed order.

| Order | Completion times | Necessary and sufficient feasibility conditions |
|---|---|---|
| A then B | a; max(a,r)+b | a≤dA and max(a,r)+b≤dB |
| B then A | r+b; r+b+a | r+b≤dB and r+b+a≤dA |

This is complete for the declared two-task, nonpreemptive model. It does not require guessing a scheduling heuristic. In the [existing queue case](../conditions/qs-02.md), a=4, b=2, r=1, dA=7, dB=3. A-first fails B. B-first, including an initial idle unit, meets both deadlines exactly. “Always do available work immediately” excludes the only feasible schedule in this model.

## The deferred switching-cost question

Now permit A to be preempted at r, assume 0<r<a, and charge a specified σ≥0 for each switch between A and B. There is no initial setup charge. Starting A immediately, switching to B at r, and switching back gives:

\[
C_B=r+\sigma+b,\qquad C_A=a+b+2\sigma.
\]

Therefore this route meets the deadlines exactly when

\[
\sigma\le d_B-r-b\quad\text{and}\quad2\sigma\le d_A-a-b.
\]

The B-first route has one inter-task switch, so C_B=r+b and C_A=r+b+σ+a. With the original deadlines, every positive σ invalidates both this route and the specific preempt-at-release route. **That does not prove the problem infeasible. It only disproves those two routes.**

The omitted possibility is to finish switching before B's release. Work on A for r−σ units, switch during [r−σ,r], run B during [r,r+b], switch back, and finish A. For 0≤σ<r<a this yields C_B=r+b and C_A=a+b+2σ. In the original case, every 0≤σ≤1/2 is feasible. At σ=1/2 the exact schedule is A 0–0.5, switch 0.5–1, B 1–3, switch 3–3.5, A 3.5–7.

The bound is also necessary for this case. B must occupy [1,3] because its release is 1, duration 2, and deadline 3. With positive σ, doing no A work before B would finish A at 7+σ, too late. Doing A both before and after B requires at least two switches, so total processor time is at least 4+2+2σ. Deadline 7 therefore requires σ≤1/2. The displayed schedule attains that bound. We now have necessity and sufficiency, rather than a conclusion extrapolated from two failed candidates.

If the deadlines change to dA=8 and dB=4, the original preempt-at-release route and B-first route are both feasible for 0≤σ≤1. Their A completion times are 6+2σ and 7+σ, respectively. The former is faster when σ<1 and ties at σ=1. This comparison is explicitly between those routes; it is not an unproved optimum over every possible schedule.

For an indivisible task of length L across separated available intervals w1,...,wk, feasibility requires max wi≥L. If the task is freely divisible and there is no restart cost, Σwi≥L suffices. With a specified cost c for each restart, a chosen set of k used intervals provides at most Σwi−(k−1)c useful time, with each used interval also needing enough time for its assigned restart and work. A final indivisible integration step adds its own contiguous-window requirement. Total available minutes alone cannot settle all these models.

## Cost of a reusable perspective or representation

Under a declared effort-only criterion, an aid costing C to create and saving si on use i has net benefit Σsi−C over those uses. Constant saving s>0 yields a strict break-even condition n>C/s. Expected use counts give expected saving, not a guarantee that a particular realization reaches break-even.

If the aid expires before some uses, only valid uses contribute. If constructing it is itself valued, that value belongs in the evaluation; setting it to zero is a substantive assumption. If creating it displaces a time-limited opportunity, that lost opportunity is also a cost. Moving preparation outside a local session changes feasibility but does not erase its total effort.

These statements explain why a shorter answer, a smaller file, and fewer mental transitions are not interchangeable measures of efficiency. The relevant numerator is the endorsed benefit and the relevant denominator includes the costs incurred to obtain and use it. If several benefits cannot be reduced to an agreed scalar, retain the trade-offs rather than invent a numerical ranking.

## A biased research loop can obey its immediate metric perfectly

The [delayed-feedback case](../methods/cmplx-01.md) already shows four short positive events yielding value 8 while three events including a delayed result yield 16. The additional conclusion for research selection is conditional: a controller rewarding visible result count can repeatedly choose easy-to-observe changes even when the governing criterion values a different portfolio. Perfect optimization of the proxy does not repair a mismatch between proxy and purpose.

The appropriate correction is to keep unobserved outcomes unobserved, retain their observation conditions, and choose work using the supported value and opportunity model. It is not to credit all delayed proposals optimistically or to stop doing exact local work because it is easy to verify.
