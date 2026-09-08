# Following the recipe is only one link in success

Let F mean the recipe was followed, T mean the intended transition occurred, and B mean a worthwhile benefit occurred. These are different events. A person can execute a recall exercise accurately without retaining it later; a belief can change toward a false conclusion; a perfectly performed instruction can preserve the wrong goal. Consequently P(F) alone puts no positive lower bound on P(B). A countermodel has F always true and B always false.

Likewise, defining “successful following” to include the desired benefit makes “successful following guarantees benefit” true by definition while providing no method. Fidelity must be assessable from the performed operations without assuming the outcome being predicted.

## What a reliability bound would actually imply

Suppose benefit requires every link in a specified chain to work: appropriate input interpretation, worthwhile destination, adequate mechanism, faithful execution, and retained effect. If each link's failure probability is at most ε_i under the **same declared deployment distribution**, and absence of these failures is sufficient for the benefit, then

\[
P(B)\ge 1-\sum_i\epsilon_i.
\]

Proof: lack of benefit is contained in the union of the modeled failures; the probability of that union is at most the sum of its members' probabilities. No independence assumption is needed. The lower bound is floored at zero. This conclusion requires exhaustive coverage of failures relevant to the sufficiency claim; leaving an important failure outside the model invalidates that claim.

If five links each have failure probability at most 1/100, the supplied premises imply at least 95% benefit probability. They do not imply that the actual catalog has those rates. If the links are independent, multiplying their success probabilities gives another calculation; the independence premise is extra evidence, not a convenient default.

For a population made of groups with weights w_g and failure rates f_g, total failure is Σw_g f_g. A 1% average failure rate permits 100% failure in a group making up 1% of the population. Therefore “near guaranteed for this person” does not follow from “near guaranteed on average.” Conversely, a rate established on a narrow eligible group cannot be transferred to all requests merely by retaining the same instructions.

## A correct refusal and a successful requested change have different denominators

An evaluator can assess correct handling of all requests, including explicit unresolved cases. It can separately assess successful beneficial changes among attempts and among all eligible requests. If a system solves ten of a hundred eligible tasks and correctly reports the other ninety unresolved, its correct-handling rate may be 100% while its task-success rate is 10%. Excluding every failure after observing it would make success rate vacuous.

This corrects a possible consequence of the old capability gate: excluding an impossible physical act is warranted, but successful exclusion must not be promoted into the very mind change the user wanted. The same holds when a model correctly identifies an unimplemented central judgment.

## Reliability can be improved before a human trial

For a specified finite task, the [adequate-policy construction](recipe-adequacy.md) can eliminate a class of selection errors by proof. The [atomic edit](reference-and-concurrency.md) can preserve a snapshot on a content mismatch. The [information-policy calculation](information-and-action.md) can return the exact optimum in its supplied policy class. These are achieved properties of actual operations, with explicit domains.

An empirical ingredient can be retained at its studied scope, while a newly assembled human recipe remains a candidate. Improving that candidate means filling the missing operation, choosing an evidence-supported ingredient where relevant, resolving an identification collision, or changing the reachable action set. Adding another aspiration such as “ensure motivation” does none of these things.

No amount of logical deduction can determine an unspecified individual's future response from premises that allow both response and nonresponse. That is an identification limit established by a countermodel, not a reason to leave entailed parts unfinished. A useful result may contain both an exact completed computation and a precisely located unobserved effect.
