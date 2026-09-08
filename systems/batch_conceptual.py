from write_records import save,BASE
import json,itertools
save('045-gd-3','gd','Decompose an exploratory goal without preselecting its destination',
'Change the first action when the benefit of exploration is to discover an omitted possibility.',
'I would normally identify a problem and desired outcome before choosing an intervention. That is reasonable when the goal is already settled; the input here expressly permits discovering it.',
'''Original target: "An unfamiliar starting point can be explored before the problem or destination is settled."

Concrete input: the assistant has three representations of a fixed six-item set—chronological, categorical and relational. The task is to find a consequential relationship the first two omit. Six items are A source, B example, C criterion, D output, E feedback and F future choice. Relations are A→D, B→D, C→D, D→E and E→F. Chronology alone orders A,B,C,D,E,F; categories separate input, output and learning.

Expanded goal: encounter and compare available representations, identify a missing relation, decide whether it changes a next choice, retain the actual relationship even if no preconceived problem is diagnosed. This is the same exploratory goal; a replacement goal "prove that a graph is best" would be substitution.

Subgoals: expose the six items (perception); construct three representations (format); compare what each reveals (relation); test one later use (operation); retain a failed discovery if nothing changes (evidence). Dependencies are item access→representations→difference→later use. Predetermining the winning relation conflicts with open selection and is excluded.

Actual products: chronology supports event-order reconstruction; categories support item lookup; adjacency supports answering "what could change a future choice?" by path D→E→F. The target F has no incoming connection from C without passing through D and E. The graph changes the next operation from revising C alone to asking for or generating feedback on D before revising F. This is an actual representation-based inference in the declared graph, not evidence that all future decisions require feedback.

Integrity test: producing all three representations without applying any difference would leave the user's exploration program incomplete. The later path query is performed; it discovers that a criterion edit has no represented direct path to F. The absence is about the stipulated graph, not a universal causal claim.

Tradeoff: graph construction costs more than a simple list. On an exact date-order question chronology remains preferable. The three representations remain candidates rather than forcing all later tasks through a graph.''',
'The next action for the graph instance is to obtain feedback on D before altering F; the initial problem-first sequence has been replaced by a performed exploratory comparison.',
'The path query identifies a prerequisite relation absent from the first two representations. Benefit is a corrected inference within a supplied graph.',
'KEEP','Relational adjacency answers the dependency question; chronology and categories retain their distinct uses.','Add a direct C→F edge; compare a visual encounter; investigate a case with no useful discovered difference.')
save('046-gsr-3','gsr','Reconstruct the claim that a faster answer is always better',
'Change whether elapsed effort acts as an objective or a constraint in a consequential choice.',
'Time cost is relevant to choosing an answer. My starting preference is to avoid extra work unless it changes a material result; that does not yet justify treating time as the sole criterion.',
'''Conclusion under reconstruction: "Choose answer A because it takes fewer work units."

Concrete inputs: A takes 2 units and leaves one required distinction unresolved. B takes 5 and resolves it with a known countercase. The decision deadline allows 6 units. Chain one: less work→less burden→more available attention→useful interaction. Chain two: adequate answer before deadline→usable distinction→the expressed decision goal. Chain one serves the goal only if the shortened answer still supplies what the decision needs.

Story one: burden matters; additional work sometimes adds no value; time becomes a proxy for burden; the conclusion selects A. Story two: the distinguishing countercase matters; 6 units are available; B supplies it at cost 5; the conclusion selects B. A new criterion "always minimize time" substitutes a different optimization problem for satisfying the required distinction.

Link checks: 2<5 is true; 5≤6 is true; A's unresolved distinction is given; neither number establishes how a person feels. B serves the concrete request under its constraint. If the deadline were 3, B would be infeasible and A with explicit uncertainty would be the available partial contribution. If both answers resolved the distinction, A could win without this chain.

Applied output: the assistant records B as the present choice with margin one unit before deadline, and A as the deadline-3 fallback with the missing distinction visible. The conclusion "faster is always better" is rejected by this finite instance; the prior policy of avoiding unproductive cost remains intact.

Journey necessity: this reconstruction earns its work only at the live tradeoff. A routine one-fact answer does not need a goal chain. Terminal intrinsic values remain the user's to state; the practical target is already sufficient for this choice.''',
'Time is now treated as a six-unit feasibility constraint before comparing adequacy in this case; B is selected.',
'The decision uses a feasible answer that resolves the stipulated required distinction. No human satisfaction or universal value function is inferred.',
'KEEP','The two goal chains plus deadline boundary distinguish cost relevance from sole-objective substitution.','Examine quality-equivalent answers; add interruption cost; test whether a partial answer preserves a later opportunity.')
save('047-grf-2','grf','Refine durable change into a testable continuation',
'Change a durability claim into an explicit unresolved continuation condition.',
'A saved correction seems a sensible way to preserve a useful change. I do not yet have evidence that a later system will retrieve and apply it.',
'''Original target: "Preserve the conditions, scope, evidence, and trigger for reuse, including a case where the correction should not apply."

Refined goal: retain this condition-bearing correction in the authorized persistent handoff, then at the next matching recurrence inspect whether it is retrieved, accepted and applied; test the boundary at a nonmatching recurrence. This clarifies the requested persistence requirement without substituting "write a file" for later uptake.

SMART: specific correction is the lookup-only eligibility rule; measurable events are retrieval, accepted eligibility and changed operation; achievable now are record construction and local replay; external future retrieval is unavailable; relevant concern is continuity; time is the next actual matching recurrence, not an invented promised date.

Questions ranked: Will another session retrieve the handoff? high, unknown. Is the next task a lookup with given criteria? high, decided by its actual input. How long should retention last? medium, no declared expiry; invalidated by evidence or superseding instruction. Filename aesthetics? low.

Assumptions: root persists the supplied artifact (authorized parent role, not yet observed here); saved state guarantees retrieval (rejected); a local replay equals cross-session transfer (rejected). Dependencies are saved bytes→later access→retrieval→fit decision→operation. A missing access step breaks the chain even when all later statements are well specified.

Primary criteria include preserved trigger, boundary, source and observed example now; durability completion additionally requires the future event. Secondary is low retrieval burden. Stretch is repeated successful transfer over changed settings.

Actual product: the record's reusable entry is `{trigger: lookup with given options and criteria; boundary: open-ended discovery; action: reuse table eligibility; evidence: scope-bridge.json; future_status: untested}`. A local replay accepts the exact trigger and rejects the boundary, but there is no future recurrence evidence. The original durable-change objective remains open rather than silently narrowed.''',
'The current durability judgment changes from an appealing saved-record candidate to a condition-bearing candidate with transfer explicitly pending.',
'The representation is more precise, but no new beneficial behavior beyond the already kept scope rule is demonstrated. This application preserves a needed uncertainty.',
'UNRESOLVED','A continuation chain retains the missing retrieval event that a saved-file label loses.','Inspect an actual later recurrence; test a stale trigger; compare retention cost against reconstructing from source.')
save('047-grf-3','grf','Refine a change of criteria without retroactively changing the winner',
'Change how a revised criterion is recorded when it reverses a method choice.',
'If the user changes the priority, I would recompute the choice. The material risk is treating the new winner as if it had always won the old comparison.',
'''Original target: "If a criterion itself changes, preserve the earlier comparison and justify the revised criterion separately."

Concrete input: A scores fidelity 5, speed 2; B scores fidelity 3, speed 5 on declared illustrative 1–5 scales. Original weights are fidelity .8 and speed .2. Revised weights .3 and .7 express a new task with a close deadline; they are stipulated case inputs, not inferred user values.

Clarification goal: calculate and retain both decisions with their criterion version and reason before using the revised one. This preserves criterion change as a possible intended operation. A replacement goal "prove the chosen option is best" would invite post-hoc weighting and is excluded.

SMART: specific decision A/B; measurable totals and versioned result; achievable arithmetic; relevant protection of meaning under change; time before the revised selection. Question priority: did the concern actually change? high; here it is given in the constructed case. Are scores measured? high; no, declared assumptions. Are the alternatives mutually exclusive? yes for this single slot.

Dependencies: preserve v1→state revision reason→compute v2→select for v2. Primary success is both results with exact weights and explicit scope. Secondary is sensitivity; stretch is obtaining actual preference evidence, not available.

Actual arithmetic: v1 A=.8×5+.2×2=4.4; B=.8×3+.2×5=3.4. v2 A=.3×5+.7×2=2.9; B=.3×3+.7×5=4.4. The crossover is fidelity weight .6, found from 2+3w=5−2w. A wins above .6, B below .6. Both historical comparisons remain valid under their assumptions.

Applied choice: B is selected for the revised task, while A remains the prior-task winner. The statement "B was the best method all along" is rejected: it changes the criterion attached to the original claim.''',
'The revised case selects B with criterion version 2 and retains A as the winner of version 1.',
'The finite comparison no longer erases a legitimate earlier result when a declared priority changes; the crossover quantifies exactly when the recommendation reverses.',
'KEEP','Two versioned comparison rows preserve criterion history; one overwritten score would lose it.','Test score changes with fixed criteria; examine a hidden hard constraint; compare a noncompensatory criterion.')
