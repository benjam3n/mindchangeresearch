# What incomplete evidence can already settle

For a finite set of possible worlds S and a question q, the supplied premises determine the answer exactly when q has the same value in every world satisfying those premises. If two admitted worlds give different answers, those worlds are an explicit witness of the missing determination. If all admitted worlds agree, requesting more information for that answer is unnecessary. This follows directly from what it means for a conclusion to hold in every model of the premises.

The conclusion can be a conditional function or a set of remaining answers. An unknown parameter does not force the output to be “investigate later” when its effect can be derived symbolically.

## Generalizing the repository's signal family

The [information-policy record](../inquiry/51-ht-information-policy.md) uses P(good)=p, overall signal accuracy 4/5, act payoff +6 in a good state and −4 in a bad state, decline payoff zero, and observation price c. Replace the fixed accuracy by a specified α in [0,1]. Let t=P(good,+). The four joint cells must be:

| Cell | Probability |
|---|---:|
| good, + | t |
| good, − | p−t |
| bad, + | 1−p−α+t |
| bad, − | α−t |

These preserve both the good-state marginal p and accuracy α. Nonnegativity is equivalent to

\[
\max(0,p+\alpha-1)\le t\le\min(p,\alpha).
\]

Conversely every t in this interval supplies nonnegative cells summing to one with the required marginal and accuracy. Thus the interval characterizes every compatible binary joint matrix; no unknown sensitivity or specificity has been silently supplied.

The six available policy payoffs follow by summing state payoffs:

| Policy | Expected payoff |
|---|---:|
| Act immediately | 10p−4 |
| Decline immediately | 0 |
| Buy, act only on + | 2t+4p+4α−4−c |
| Buy, act only on − | 6p−2t−4α−c |
| Buy, act after either signal | 10p−4−c |
| Buy, decline after either signal | −c |

The original policy reduction cannot simply be copied to every α. At p=1/2, α=0, and c=1, the only compatible t is zero. The signal is perfectly inverted. Buying and acting on the negative signal yields 2; acting immediately yields 1; following the positive signal yields −3. Deleting the negative-response policy, as was valid in the original narrower family, now deletes the optimum.

This closes the request to change accuracy: the complete new family and its six payoffs are available, and an exact counterexample identifies the old reduction's failure. “Use a different accuracy and test it” is no longer the result.

## The worst-regret calculation remains finite

For fixed p, α, and c, every policy payoff is affine in t. The best policy payoff is a maximum of finitely many affine functions, hence convex. Subtracting a fixed mixture's affine payoff leaves convex regret. A convex function on a closed interval attains a maximum at an endpoint, possibly also elsewhere in a tie. Therefore the two endpoint matrices suffice to evaluate worst regret for any fixed mixture over these six policies.

Each pure policy has a two-dimensional endpoint-regret vector. Random mixtures give their convex hull. Minimizing the larger coordinate reaches a boundary edge or vertex of that hull, so an optimal mixture can be represented by at most two pure policies. The implementation enumerates pure policies and pairs, then checks pair endpoints and the point where the two endpoint regrets are equal. It uses exact fractions. This constructs a minimax answer for each supplied p, α, c in the stated finite policy class without assuming the old two-policy reduction.

For p=1/2, α=4/5, c=1, the implementation recovers the earlier half-immediate/half-positive policy with worst regret 1/10. For α=1/5 it returns a corresponding half-immediate/half-negative policy with the same worst regret. For α=0 it selects the negative policy outright. These are exact model consequences, not estimated behavior or advice about a real purchase.

## More than two signals and changed utility

If signal y has an explicitly supplied joint distribution with state s and utility u(a,s), the best expected value after observing y is

\[
V_{\mathrm{obs}}=\sum_y\max_a\sum_sP(s,y)u(a,s)-c.
\]

The best immediate value is

\[
V_{\mathrm{now}}=\max_a\sum_sP(s)u(a,s).
\]

The formula covers any finite signal alphabet. Without cost and with the same available actions, observation cannot reduce the attainable optimum: the post-observation policy can always ignore y and use the immediate action. This proof does not imply that a particular person will use information well, that obtaining it has no cost, or that actions remain available while waiting.

Nonlinear utility of a final consequence can be included by evaluating u before expectation. If value depends on the whole sequence, its history belongs in the state or policy; substituting a one-period utility silently changes the problem.

## Expiration changes the available policy

Let u_y be the expected payoff of a live risky action after y, and let a fallback yield g≥0. Waiting without a protected fallback gives ΣP(y)max(0,u_y)−c. Preserving the fallback for cost r gives ΣP(y)max(g,u_y)−c−r. Reservation is preferable to unprotected waiting exactly when

\[
\sum_yP(y)\,[\max(g,u_y)-\max(0,u_y)]>r.
\]

The gross protection value lies between zero and g. It is zero when the risky action already exceeds g in every possible observation; it is g when every risky continuation is nonpositive. Commitment now must still be compared separately. This generalizes the [three-policy timing case](../gosm/01-time-and-options.md) without pretending that information accuracy alone determines the value of waiting.
