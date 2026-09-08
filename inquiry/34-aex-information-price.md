Intended mind change: Determine when waiting for perfect information is worth its cost, rather than infer a timing choice from unresolved probability alone.

Starting working judgment: Previous interval cases established action sensitivity but did not price information. Waiting remained a plausible candidate, not an endorsed universal rule. Concrete input: the DVS32 candidate B, RCI29’s omitted-cost question and the completed timing dependency’s capsule. For a hypothetical decision, acting returns +6 on success and −4 on failure, declining returns 0, and perfect information costs c=1. Probability p is initially allowed in [.4,.9]; these are declared model parameters, not human measurements or advice.

Original: ../sources/inquiry-aex.original.md and receipt, interpretation 1. Core claims: C1 perfect information is preferable throughout the stated interval; C2 its payoff formula survives delay; C3 preserving the next question is sufficient for later execution. Ten extraction questions per core follow.

| ID/core | Type | Assumption | Hiddenness/risk | Testability / actual result |
|---|---|---|---|---|
| T1/C1 | Causal | Information changes expected attainable payoff, not just confidence. | Deep/High | Compute best contingent action. |
| T2/C1 | Existence | A state S and two actions exist in the stated fixture. | Surface/Low | Declared S=success/failure, act/decline. |
| T3/C1 | Stability | Payoffs remain +6/−4 until the delayed decision. | Deep/High | Assumed fixture; expires in boundary case. |
| T4/C1 | Access | Perfect state information is obtainable at price c. | Deep/High | Stipulated experiment, not real service. |
| T5/C1 | Capability | The actor can condition its later act on the observation. | Shallow/High | Explicit decision tree. |
| T6/C1 | Value | Expected payoff is the selected criterion. | Surface/High | Declared hypothetical criterion, no user utility imputed. |
| T7/C1 | Knowledge | The success probability p is the quantity informing expectation. | Shallow/High | p remains interval-valued, no fabricated measurement. |
| T8/C1 | Resources | Cost c is paid even when the later action is decline. | Buried/High | Included in both branches; compare zero cost. |
| T9/C1 | Permission | Observation purchase is authorized within the decision model. | Shallow/Low | Hypothetical action; no external purchase. |
| T10/C1 | Timing | Information arrives before the action opportunity closes. | Deep/High | Boundary: after expiry no +6 option. |
| T11/C2 | Causal | Waiting preserves the favorable state opportunity. | Deep/High | Assumed in base model, varied in boundary. |
| T12/C2 | Existence | A future decision time exists. | Surface/Medium | Declared t1; not an actual scheduled event. |
| T13/C2 | Stability | p does not drift during the waiting interval. | Deep/High | Base assumption, not measured forecast. |
| T14/C2 | Access | A channel delivers the observation. | Shallow/High | Model perfect observation; capsule is not that channel. |
| T15/C2 | Capability | The policy can decline after observing failure. | Deep/High | Required for perfect-information payoff 6p−c. |
| T16/C2 | Value | One payoff unit has the same value before and after delay. | Deep/Medium | Declared no discounting; otherwise change formula. |
| T17/C2 | Knowledge | No hidden correlated cost is omitted. | Buried/High | Only c is specified; general claim remains conditional. |
| T18/C2 | Resources | The observation budget covers c. | Surface/Medium | Base c=1; constraint can block wait. |
| T19/C2 | Permission | No obligation forces act after buying information. | Buried/High | Base decision tree permits decline; forced act destroys information value. |
| T20/C2 | Timing | The observation duration itself has no extra penalty beyond c. | Deep/High | Base c aggregates cost; avoid double count. |
| T21/C3 | Causal | Writing a capsule does not itself generate a future execution event. | Shallow/High | Already established; imported, no new keep. |
| T22/C3 | Existence | The stored next operation has a specific source and input. | Surface/Medium | Methods v2 read; SP02 concrete. |
| T23/C3 | Stability | The same user goal survives until the resumed act. | Deep/High | Unknown future; invalidation field retained. |
| T24/C3 | Access | The restored actor can access both source and current instruction. | Deep/High | Now readable; future environment unknown. |
| T25/C3 | Capability | The consumer rechecks an invalidation condition rather than merely storing it. | Buried/High | Current hash comparison performed. |
| T26/C3 | Value | Current continuation is useful even if no later session occurs. | Surface/Medium | User’s present task authorizes actual work. |
| T27/C3 | Knowledge | The next action is still pending when selected. | Deep/Medium | Status check required; methods doing SP02 now. |
| T28/C3 | Resources | Saved state is sufficient to avoid reconstructing missing input. | Deep/High | Methods v1 failed; v2 exact input repaired. |
| T29/C3 | Permission | A saved proposal authorizes a different future external act. | Buried/High | False as universal; current task scope still governs. |
| T30/C3 | Timing | The opportunity has not expired when resumed. | Deep/High | Capsule declares invalidation; future unknown. |

Assumption map: C1=T1–T10, C2=T11–T20, C3=T21–T30. The highest-priority assumptions are T8 (cost on every observed branch), T15 (ability to decline), T10/T30 (opportunity timing) and T6 (expected-payoff criterion). Normative premises are declared rather than discovered as facts. Historical or future channel availability remains unknown; current artifact checks do not establish it.

Five-edge dependency chain for the stated perfect-information policy: executing its contingent choice requires the state observation before choice (D1); D1 requires an observation delivery before the opportunity expires (D2); D2 requires an operating delivery channel during the available window (D3); D3 requires a successful initiation with required payload (D4); D4 requires its trigger’s actual preconditions to be met (D5). This is a dependency chain under the declared host-triggered method, not proof that all conceivable methods need a capsule. The present capsule records input; it does not establish D5 for a future event. At the algebraic root, expectation follows from the declared two-state payoffs; at the temporal root, later initiation is genuinely unobserved.

Immediate tests: compute E(act)=10p−4 and E(wait)=6p−1, since after observing failure the policy declines but still pays one. Therefore wait−act=3−4p. At p=.4 the values are 0 and1.4; at .75 both are3.5; at .8 they are4 and3.8; at .9 they are5 and4.4. C1 is not uniformly true on [.4,.9]. If c=0 then perfect information weakly improves the optimally chosen current action; if the chance to act expires before observation, the stipulated wait strategy loses its +6 branch. Those are different models, not counterevidence to the arithmetic under its own premises.

Distinct later application: on a newly supplied interval [.8,.9] with the same fixed payoffs and c=1, act exceeds wait at every p by .2–.6, so the model now selects act and keeps p unresolved. This is stronger than the earlier threshold-invariance result: perfect information could change a later action, yet its net value is negative at each allowed p. timing-value-tests.json records every evaluated row. SE36 receives this cost-bearing input and both the tie p=.75 and expiry boundary. No real purchase, human urgency or scheduled future act is inferred.

Depth: thirty assumptions, ten categories, more than six Deep/Buried entries and five explicit dependency edges. Already tested items cite current artifacts or prior exact tests; parameter assumptions are conditional; future user/channel behavior has no current verification. Nothing is added solely to force waiting or acting.


Actual mind change: The current decision model separates action sensitivity from the net value of information. On [.8,.9] the performed payoff comparison selects act while uncertainty remains.
Benefit: The next timing enumeration uses a cost-bearing policy and retains its tie/expiry limits. K10 is this new local cost comparison, not another keep for the existing saved-versus-scheduled distinction.
Verdict: KEEP
Organization: Probability interval, policy, observation price, opportunity window and channel evidence remain distinct. The result is hypothetical expected-payoff logic, not a claim about the user’s preferences.
Next attempts: Enumerate price and expiry cases; test a forced-act observation; compare a risk-averse criterion only if declared; keep actual channel evidence separate from theoretical delivery.
