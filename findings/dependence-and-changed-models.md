# A changed model needs a recomputed answer

## Partial dependence is not halfway between one update and two

The [alarm record](../post-allocation/cycle-02/belief/01-pbr-correlated-evidence.md) has prior defect probability 1/10, sensitivity 4/5, and false-positive rate 1/5 for each of two alarm fields. Perfect copies yield posterior 4/13; conditional independence yields 16/25. It leaves partial dependence for another attempt.

Write u=P(both HIGH | defective) and v=P(both HIGH | not defective). After both alarms are high,

\[
P(D\mid HH)=\frac{u}{u+9v}.
\]

The supplied single-alarm marginals require 3/5≤u≤4/5 and 0≤v≤1/5. These bounds are sufficient as well as necessary: the other conditional cells are s−j, s−j, and 1−2s+j, where s is the relevant single-alarm probability and j its joint-high probability. Every pair u,v in the indicated rectangle defines valid conditional tables.

The posterior increases with u and decreases with v. Its exact identified range is therefore **[1/4,1]**, attained at (u,v)=(3/5,1/5) and any valid (u,0). Marginals alone do not even locate the answer between the copied and independent cases. The replacement threshold 1/2 is crossed exactly when **u>9v**. That is the missing dependency-sensitive decision rule, already derived without inventing a particular correlation.

For an explicitly different, one-parameter mechanism, suppose the second alarm copies the first with probability λ in both defect states, and otherwise is independently redrawn with the same conditional marginal. Then u=(16+4λ)/25, v=(1+4λ)/25, and the posterior is

\[
\frac{16+4\lambda}{25+40\lambda}.
\]

It falls from 16/25 to 4/13 as λ goes from zero to one; replacement is selected exactly when λ<7/32. This completes a genuine partial-copy model. It does not license treating every possible dependence process as this mixture.

## The machine-reservation extensions have numerical answers

The [TD](../post-allocation/cycle-01/time-reversibility/TD-prospective.md) and [RVA](../post-allocation/cycle-01/time-reversibility/RVA-prospective.md) records specify A costing $10, B free with availability probability 0.6 revealed at 09:15, twenty-minute processing, a 09:40 completion deadline, and a guaranteed refundable A reservation through 09:20.

| Earlier proposed extension | Completed consequence under the stated change |
|---|---|
| Increase duration to 21 minutes | Latest start becomes 09:19. The 09:15 report still permits waiting and completion at 09:36. Increasing duration by one minute does **not** invalidate all waiting. |
| Add setup of σ minutes after choosing either machine | Waiting remains feasible exactly when 15+σ+d≤40, with refund cancellation also completed by its cutoff. For d=20, σ≤5. |
| Reveal B at 09:18 and require three minutes before B can begin | B finishes at 09:41, so the report cannot support that B branch under the hard deadline. This changes if setup can validly be completed in advance; the timing operation must be specified. |
| Add a nonrefundable fee r paid only for the reserve-and-wait route | Expected cost becomes r+4, versus 10 for immediate A. Waiting is cheaper exactly when r<6, ties at 6, and costs more above 6, assuming completion feasibility remains. |
| Pay v dollars per minute of earlier completion | Immediate A finishes fifteen minutes earlier than waiting at 09:15. With the preceding fee convention, waiting's net advantage is 6−r−15v. Its sign, rather than cost alone, determines this two-route comparison. |
| Replace guaranteed reservation by failure probability f conditional on B being unavailable | Waiting's completion probability becomes 1−0.4f, if failed reservation leaves no other route. Any f>0 defeats a probability-one requirement. A weaker reliability requirement ε on failure allows f≤ε/0.4. |
| Compare B-only with reserved fallback under failure penalty L instead of a hard requirement | B-only expected cost is 0.4L; reserved fallback costs 4 in the original zero-fee model. Reserved fallback is preferable exactly when L>10, ties at 10, and loses below 10. |

The changed timing and fee questions are closed within their supplied models. Actual reservation reliability and the value of early completion are inputs, not reasons to postpone these formulas. A fee charged to both routes cancels in their comparison; that is a different charging rule from the table.

## More controls and unequal costs

The [two-control XOR result](../methods/mtcg-02.md) uses A=110 and B=011. Both preserve even parity of the displacement. Their span is exactly the four even-parity vectors. Adding a third three-bit control C expands reachability to all eight displacements exactly when C has odd parity. If C has even parity, reachability stays unchanged.

For arbitrary finite XOR controls, a displacement is reachable exactly when it is in their binary linear span. Any word reduces to a subset of controls because pairs cancel. With nonnegative per-use costs, a minimum-cost word can therefore be chosen with each control used at most once: removing a repeated pair preserves the endpoint and cannot increase cost. Enumerating the 2^m subsets constructs the least-cost witness for m supplied controls. This is an exact finite algorithm; it is not a claim that exponential enumeration is efficient for large m.

For A=110, B=011, C=101, costs 1,1,3, the displacement 101 is achieved by AB at cost 2 rather than C at cost 3. With C cost 1, C is preferable. Equal reachability does not imply equal capability cost. For noncommutative transitions, pair cancellation and reordering need new justification and this reduction cannot simply be carried over.
