# When a recipe can compensate for its executor

Let S be the possible starting situations admitted by a task, A the available actions, and K(s) the actions adequate in situation s. Let e(s) be the information available to the recipe. A recipe selecting an action from that information is a function f with output f(e(s)). This model assumes the adequacy relation and observation map are specified; it does not pretend that arbitrary human situations arrive with those relations known.

**A universally adequate selector exists exactly when every set of situations with the same available information has at least one commonly adequate action.** In symbols:

\[
\forall z\in e(S),\qquad \bigcap_{s:e(s)=z}K(s)\ne\varnothing.
\]

Necessity: every situation in one such set gives f the same input z, so f returns the same action. That action must belong to every K(s). If the intersection is empty, no possible output can satisfy all the situations.

Sufficiency: choose one member of the nonempty intersection for each z. Returning that action when z is observed is adequate in every situation represented by z. For finite supplied sets, computing these intersections constructs the selector; the conclusion does not depend on a talented executor guessing the missing distinction.

This strengthens the earlier [equal-confidence example](../gosm/06-uncertainty-and-next-query.md). The same confidence 1/2 can require reading a report in one situation and calibrating its source in another. Confidence is then an insufficient input for choosing the observation. It is not intrinsically a bad representation: it remains sufficient for some immediate decisions whose consequences depend only on that probability.

It also locates the implementation gap in the [near-guarantee record](../post-allocation/cycle-03/capability/01-spg-near-guarantee.md). “Diagnose the controlling locus” names an output needed by the rest of the procedure. It does not establish that the received information identifies that locus or give an algorithm for finding it. A programmer can implement a field named `locus` while having no implementation of its value.

## More than pairwise compatibility is required

Consider three observationally indistinguishable situations:

| Situation | Adequate actions |
|---|---|
| s1 | a, b |
| s2 | b, c |
| s3 | a, c |

Every pair has a shared adequate action. The intersection across all three is empty. Therefore passing every pairwise compatibility comparison does not establish that one recipe works across the entire admitted class. This directly matters when consolidating independently useful methods into one general instruction.

A distinguishing question can repair the example. First separate s1 from {s2,s3}. Return a or b for s1 and c for {s2,s3}. There is no need to identify s2 versus s3: the shared adequate action c already settles the task. **Diagnosis should distinguish what changes the appropriate operation; complete psychological classification is unnecessary.**

## An executable finite recipe

The implementation in [deductions.py](../tools/deductions.py) receives explicit situations, adequate-action sets, candidate questions, the outcome each question returns in each situation, and a positive question cost.

It computes the intersection. If nonempty, it returns an adequate action immediately. Otherwise it partitions the current situations by each candidate question's answers. Questions that make no distinction are discarded. It recursively constructs a valid continuation for every possible answer, rejects a question if an answer has no valid continuation, and selects the remaining question with minimum worst-case total cost. If none exists, it returns the unresolved situation set and its empty common-action intersection.

Termination follows because every retained question produces strictly smaller nonempty situation sets. Correctness follows by induction on the size of the set: action leaves satisfy all their situations; each question leads only to correct child policies. Minimum worst-case cost follows from enumerating the admissible first questions and choosing the least cost plus the largest child cost. These guarantees apply to the finite specified model and truthful stipulated observations. Unknown human responses do not become known by entering them as fields.

## Why superior execution cannot repair some instructions

Let R_I(s) be the states reachable from s using only transitions permitted by instruction set I, and let G be the states satisfying the worthwhile goal. If R_I(s)∩G is empty, every executor that obeys I fails to reach G. Proof: every state it can reach belongs to R_I(s), none of which belongs to G.

The relevant defect may therefore precede execution. Requiring the destination to be fixed can exclude a needed destination-discovery operation. Requiring a fixed number of steps can exclude a needed additional operation. These are not reasons to reject all constraints: if an adequate path remains, the constraint may improve reliability or reduce needless search.

“A bad recipe always produces bad food” needs this distinction. A recipe can be poor on average yet succeed on some inputs. The noncompensable case is narrower and exact: the allowed trajectories contain no adequate outcome, or the input does not distinguish situations with incompatible required actions. Improving the cook while preserving those limitations cannot supply the missing route or information.

## What this changes in the catalog

The 300 imported variants remain useful candidate procedures. Their shared four-step form is a historical formatting choice, not a proof of adequate operations. Selecting among them requires the present obstruction and evidence about it. A variant containing an unresolved central judgment remains a procedure outline until that judgment is supplied by evidence, a performed derivation, or an explicit executable subprocedure.

The remedy is not to add more confidence language. It is to supply the distinguishing information, construct a common adequate action, enlarge the allowed route where justified, or state the exact conditional answer. Abstaining can be the correct selector result without being the successful mind change originally sought.
