Intended mind change: Make the next inspected case depend on which surviving rules it can distinguish, and stop interpreting repeated compatible evidence as rule identification.

Actual starting judgment: “Inspecting the present red square in more detail is a plausible next step, but it does not yet discriminate the three surviving rules. I need a case choice with a stated effect on this finite uncertainty.” This is the preserved judgment in `systems-handoff-inputs-before.json`; the starting state already recognizes the need for discrimination.

Actor and scope: The systems workers construct and consume a noiseless finite rule exercise. The hidden-rule language denotes a stipulated oracle known to the author, not a blinded experiment. There is no measured human attention shift, inferred perceptual experience, or claim that the hypothesis list exhausts real-world rules.

Original source: `systems-handoff-mrc.original.md`, with `systems-handoff-mrc.requirements.txt` separately retained. Reloaded reader streams and matching hashes are in `systems-handoff-reload-integrity.json`. MRC provides no numerical 8x floor and requires no subordinate invocation here. All three questions are applied to the complete four-rule/four-input table, the actual two-query sequence, alternative observations, a progress checkpoint, and later cases including a rule outside the list. The finite branches stop when settled rather than being padded to an invented depth.

The four hypotheses are R: output is red; S: output is square; AND: red and square; XOR: exactly one of red and square. The initial observation is a red square with output true.

| Red | Square | R | S | AND | XOR |
|---|---|---|---|---|---|
| False | False | False | False | False | False |
| False | True | False | True | False | True |
| True | False | True | False | False | True |
| True | True | True | True | True | False |

## What is being achieved?

Surface operation: choose the next case to inspect. Immediate goal: reduce the surviving rule set. Upstream goal: make correct predictions on other permitted feature combinations. The terminal value within this supplied task is warranted prediction under the declared oracle, rather than accumulating inspected examples.

The initial true output eliminates XOR and leaves `{R,S,AND}`. Repeating the red square returns true for all three. Inspecting an object that is neither red nor square returns false for all three. Neither query reduces this specific uncertainty. A red nonsquare or a nonred square partitions the three hypotheses into groups of sizes one and two.

The request for further inspection therefore serves the predictive goal only when the chosen case separates live rules or tests the completeness of the rule list. These are distinct goals. The first query is selected for within-list discrimination; the later out-of-list probe tests a broader boundary.

## Is this the best method?

| Candidate next operation | Possible surviving sets | Worst remaining count | Disposition |
|---|---|---:|---|
| Repeat the red square | `{R,S,AND}` after true | 3 | No discrimination under exact repeatable observations |
| Query neither feature | `{R,S,AND}` after false | 3 | No discrimination among surviving rules |
| Query a red nonsquare | True gives `{R}`; false gives `{S,AND}` | 2 | Selected; ties the next option before observing the result |
| Query a nonred square | True gives `{S}`; false gives `{R,AND}` | 2 | Equally good under the stated worst-case count criterion |

A diagnostic-design alternative works backward from the rules that disagree: R and S require discordant features, and either discordant case distinguishes AND from one of them. This yields the same two tied candidate queries. No expert was consulted; this is the concrete alternative generated from a different disciplinary framing.

The selection criterion is worst-case remaining hypothesis count with equal query cost. There is no supplied prior permitting an expected-value preference between the tied cases. The actual first computation selected red nonsquare and received false from the stipulated S oracle. The saved result is `{S,AND}` in `systems-handoff-mrc-02-first.json`.

The strongest argument against the selected query is that a nonred square would have identified S in one step for this particular oracle. That is true after using the known oracle identity. It does not establish a better worst-case choice before consulting that identity: if the oracle were R, the red nonsquare would identify it in one step instead. The exercise records the tie and does not report a foresighted optimal guess.

Claim C1: One false answer to a red nonsquare uniquely identifies S within the original four rules after the initial observation. Assume C1 right: every remaining non-S rule must contradict one of those observations. AND returns true on the initial red square and false on the red nonsquare, so it contradicts neither. This exact countercase rejects C1. The derived alternative is `{S,AND}` as the current version space. Under that alternative, a nonred square separates the two because S returns true and AND false.

Claim C2: Another red-square observation can distinguish S from AND under the exact repeatable oracle. Assume C2 right: the same feature pair must elicit different outputs under S and AND. Both output true on that pair. C2 is false in the supplied table. The alternative is a discordant-feature query, not greater inspection detail on the same allowed feature pair.

## Is progress occurring?

The first query reduced three candidates to two. Decision: continue, with an adjusted case. The second query is nonred square. The stipulated oracle returns true; `{S}` remains. `systems-handoff-mrc-02-products.json` records this second query, the surviving set, and all four predictions.

At this checkpoint the within-list identification goal is achieved. Repeating the same identification sequence would not add a new result. The upstream predictive goal now has a stated scope: all inputs in the four-row table, conditional on the true noiseless rule belonging to the admitted set. The original hypothesis-space assumption is not replaced with certainty about arbitrary real rules.

The observed change in candidate count is ordinary expected progress, not a report of felt surprise. The initial working judgment already asked for a case with a discriminating effect. The method confirms and executes that judgment rather than demonstrating a newly acquired attention strategy.

## Later use and organization comparison

The saved observation-path policy was subsequently read by `systems-handoff-finish.py later`. With the S oracle it follows false→true and identifies S. With the AND oracle it follows false→false and identifies AND. These are separate constructed oracle settings, not independent human trials.

An additional OR oracle exposes the list boundary. Its red-square output is true, and its red-nonsquare output is true, so the fixed-list policy initially selects R. A subsequent nonred-square probe returns true, contradicting R and leaving no listed hypothesis. This probe is new in the OR run. In the S and AND runs that same probe repeats a previously queried input and supplies no extra independent evidence.

| Organization | Next query after first false | Answer after false→false | Outside-list failure |
|---|---|---|---|
| Single confidence number | Not specified | Not specified | A number alone contains no prediction to contradict |
| Complete truth table | Derivable from S/AND rows | AND | Can check every named rule against OR's observations |
| Observation path plus surviving-rule names | Nonred square is explicit | AND is explicit | Empty survivor set is explicit after the OR probe |

The path is selected for choosing the next query and was used in the later runs; the truth table is retained for auditing eliminations. `systems-handoff-later-use-results.json` preserves the actual observations and survivors. The confidence-only comparison is a representation comparison, not an assertion that the real starting strategy contained only a confidence number.

Verdict certificate: The rule-space calculation and two-query procedure settle the finite identification task. The OR countercase rejects the stronger claim that a singleton in this incomplete list identifies any possible oracle. The existing result in `../gosm/06-uncertainty-and-next-query.md` already established choosing observations by how they separate live possibilities, including a cost boundary. The frozen starting judgment also already recognizes that operation. The present case therefore supplies execution and boundary evidence without another novel KEEP.

Actual mind change: The current rule set changed from `{R,S,AND}` to `{S,AND}` to `{S}`, and the later OR run changed an apparent in-list identification to an empty version space after a contradicting observation. No human attentional effect is inferred.

Benefit: The selected cases resolved the declared finite uncertainty and preserved the model-list boundary. The attention-selection principle repeats a prior established result and earns no new KEEP credit.

Verdict: REJECT

Organization: The observation path directs the later operation; the full truth table verifies it. Both retain hypothesis names so a contradictory observation can invalidate the current answer rather than merely lower an uninterpretable score.

Next attempts: Add unequal query costs with an explicit budget; admit a noisy oracle with a specified noise model; compare two out-of-list rules that agree on the current probes; use real observations only when actual inputs and outputs are available.
