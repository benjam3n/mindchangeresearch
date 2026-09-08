Intended mind change: Replace an unresolved forward search with an exact reachability certificate for the two available XOR controls and use it on later start/target pairs.

Actual starting judgment: Forward search is a sound initial method for the three-bit toggle problem. I do not yet have a certificate that target `111` can or cannot be reached using only controls A=`110` and B=`011`.

Actor and scope: The current model operates on a stipulated three-bit XOR system. `systems-handoff-inputs-before.json` freezes the start, target, and controls; `systems-handoff-mtcg-02-first.json`, `systems-handoff-mtcg-02-products.json`, and `systems-handoff-later-use-results.json` preserve the search, formula, and later queries. No physical tool access, human capability, or persistent model capability is claimed.

Original source: `systems-handoff-mtcg.original.md`; separate requirements: `systems-handoff-mtcg.requirements.txt`. Fresh reader stdout and stderr hashes match those retained files. MTCG has seven stages and no numerical 8x floor. All seven stages are performed; no integration item is a mandatory subordinate invocation here.

## 1. Current strategy

CURRENT STRATEGY: Breadth-first forward search from `000` under A and B.

CHOSEN OR DEFAULT: Deliberate; the state space has only eight states and the controls are reversible.

TIME INVESTED: Closure of the reachable component, not a measured duration.

WHAT TRIGGERED THIS APPROACH: The target's reachability was unresolved and complete finite closure is available.

The search layers are `{000}`, `{110,011}`, `{101}`. Applying either control to any of those states remains in the same four-state set. Target `111` is absent after closure.

## 2. Assessment

ASSESSMENT:

- Progress: advancing; the initial target is proved unreachable by finite closure.
- Clarity: increasing; the reachable set is exactly `{000,110,011,101}`.
- Effort: productive, with diminishing value if every later query requires another traversal.
- Output so far: useful for `000→111`, partially useful for arbitrary starts and targets.
- VERDICT: strategy needs adjustment.

The forward search answers the frozen question. It does not yet expose the invariant that determines new pairs without rebuilding a graph.

## 3. Alternative strategies

| Strategy | Concrete product | Cost of switching | Disposition |
|---|---|---|---|
| Keep a four-state route map | Witness words for each displacement from `000` | Low | Retain for execution |
| Reduce every control word to parity coefficients `(a,b)` | Four possible displacements | Low | Selected derivation |
| Search backward from each target | Same component because XOR controls are self-inverse | Low | Valid check, redundant after closure |
| Add a third control | Can expand the component | Inapplicable to the frozen capability | Changed-control boundary only |

Any control word reduces to whether A and B occur an odd number of times. With `a,b∈{0,1}`,

`a·110 XOR b·011 = (a, a XOR b, b)`.

Therefore a displacement `d` is reachable exactly when `d[1]=d[0] XOR d[2]`; when reachable, `a=d[0]` and `b=d[2]` supply a witness word. The four coefficient cases yield `000:""`, `110:A`, `011:B`, and `101:AB`.

## 4. Bias check

ACTIVE BIASES:

- Availability: forward enumeration was easy, so it risked becoming the default for every later query.
- Anchoring: the initial `000→111` failure could have been mistaken for a property of target `111` rather than of the start-target displacement.
- Confirmation: checked by deriving all four coefficient cases and matching them to the closed search set.
- Framing: state labels alone obscure that reachability depends on `start XOR target`.

CORRECTION: Store the control-guarded displacement formula with the four witness words; apply it only when both A and B remain available.

## 5. Decision

DECISION: adjust the current strategy from per-query traversal to formula-first classification with route lookup.

REASONING: The formula is necessary for every control word because repeated XOR controls cancel in pairs, and sufficient because its coefficients directly construct A, B, AB, or the empty word.

ADJUSTMENT: Compute `d=start XOR target`, test `d[1]=d[0] XOR d[2]`, then use `(a,b)=(d[0],d[2])` as the route.

CHECKPOINT: Reassess whenever the control set or operation changes.

## 6. Comprehension map

- CLEAR: The complete four-displacement component, the necessary-and-sufficient parity relation, and a witness word for every reachable displacement.
- PARTIAL: Larger linear systems would need a generalized elimination procedure; this record proves only the supplied two-control case.
- CONFUSED: None for the frozen XOR semantics.
- UNKNOWN UNKNOWNS: Real interface permissions, costs, faulty controls, or irreversible operations are not represented.

## 7. Metacognitive summary

WHAT I WAS DOING: Enumerating states forward from one start.

WHAT I FOUND: The target is outside a four-state component described exactly by `d1=d0 XOR d2`.

WHAT I'M DOING NOW: Using the displacement formula to classify and construct later queries.

BIASES CAUGHT: Enumeration availability, start-state anchoring, and label framing.

COMPREHENSION LEVEL: High for the stated three-bit XOR system.

NEXT CHECKPOINT: Any control-set or operation change.

## Later use and organization comparison

The formula and word map were consumed on four new pairs:

| Start→target | Displacement | Result | Witness |
|---|---|---|---|
| `000→101` | `101` | Reachable | AB |
| `001→111` | `110` | Reachable | A |
| `110→000` | `110` | Reachable | A |
| `011→111` | `100` | Unreachable | none |

Each witness was executed by XOR and reached the stated target. In the changed-control case where only A remains, the two-control formula is explicitly inapplicable; from `000`, only `{000,110}` is reachable, so `011` is not.

A raw BFS trace is strongest as first-pass evidence. The formula is strongest for classification across starts. The four-word map is strongest for constructing a route. The selected organization keeps the control guard, then formula, then word map; omitting the guard would falsely import B into the changed-control case.

`../gosm/08-capability-and-reachable-states.md` already established the broad distinction between naming a state and possessing a transition. This application does not claim that distinction again. Its new result is the exact invariant and constructive word map for a different paired-control system, used on four later queries and one control-removal boundary.

Verdict certificate: Exact claim—under controls A=`110`, B=`011`, a start-target pair is reachable iff its XOR displacement satisfies `d1=d0 XOR d2`. Decisive premise—every word reduces to parity coefficients `(a,b)`, yielding exactly `(a,a XOR b,b)`, and every such pair has a witness word. Inference—the criterion is necessary and sufficient. Strongest contrary branch—removing B changes the span and defeats reuse of the two-control formula; that case is retained and does not refute the guarded claim. Unresolved dependency—no result extends to other operations or real control access.

Actual mind change: The initial one-target uncertainty became a necessary-and-sufficient displacement rule with constructive routes and an explicit control-set guard.

Benefit: Four later reachability questions were answered and three routes executed from the new formula without rebuilding the original search; the changed-control case did not inherit an unavailable operation.

Verdict: KEEP

Organization: Control set → displacement criterion → witness map → boundary. This supports both classification and execution while the original layers preserve provenance.

Next attempts: Add a third specified XOR control and recompute the span; assign unequal move costs; replace XOR with a noncommutative operation and test where parity reduction fails.
