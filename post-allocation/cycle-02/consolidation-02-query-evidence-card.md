# Consolidation 02 — query-to-evidence card

Intended mind change: Reorganize four demonstrated findings so a current belief update and a historical proposal query retrieve the right material, preserve provenance, and avoid duplicate evidence aggregation.

Actual starting judgment: Source order and a query-to-inference pipeline were both plausible; the input and success criteria were frozen in `consolidation-02-freeze.md`.

Concrete input: eight-section/48-field canonical register; trigger index; L2 event representation; L3 lineage trace; proposal log with A1 and A2; both fields linked to E7; prior 0.10; LR 4; replacement threshold >0.50.

## Four retained findings

1. Query/history-conditioned location policy: retrieve representation by query and prior access history, not one scalar location rank.
2. Losslessness versus retrieval cost: canonical preservation does not determine access cost; a task index may coexist with the lossless register.
3. Proposal log versus bidirectional trace: consideration history and current/retained/rejected/gated relations serve different queries.
4. Evidence dependence before aggregation: displayed item count is not inferential event count; resolve joint lineage before multiplying likelihoods.

No transition-first repair, semantic-merge finding, value policy, perception result, or capability gate is imported as an independent consolidation premise.

## Organization A — source/finding order

1. Retrieve location-policy record; current alarm decision selects L2, custody selects L3.
2. Retrieve memory record; use trigger index while preserving canonical register.
3. Retrieve trace-matrix record; use proposal log for historical consideration and trace for current status/lineage.
4. Retrieve PBR record; count E7 once and update.

Executed current query:

- Trigger index → L2 locates A1 and A2.
- Custody subquery → L3 shows `A1→E7` and `A2→E7`.
- One event supplies one LR 4.
- Posterior is `(1/9×4)/(1+1/9×4)=4/13≈.307692`.
- Action is inspect, not replace.

Executed historical query: proposal log returns A1 and A2 as two considered display proposals. They remain two proposals even though they are one inferential event.

Required method retrievals: four. Required case-artifact accesses after routing: trigger index, L2, L3, proposal log; the canonical register remains the 48/48 authoritative store and need not be scanned for either frozen query.

## Organization B — query-to-evidence pipeline

Card:

`query/purpose → representation/location policy → task index + canonical pointer → proposal-history or current-trace view → evidence-event lineage → admissible aggregation → loss threshold/action → provenance pointer`

Executed current query:

1. Purpose is a current defect decision.
2. Trigger index selects L2 for alarm state and L3 for lineage.
3. L2 returns A1/A2; L3 maps both to E7.
4. Current trace admits one event; proposal log is not used as an independence source.
5. One LR produces `4/13`; threshold produces inspect.
6. Result points to A1, A2, E7, the prior, LR, and threshold.

Executed historical query:

1. Purpose is consideration history.
2. Select proposal log, not current trace alone.
3. Return A1 and A2 as two proposals, with the shared E7 relation retained rather than collapsing either proposal out of history.

Required consolidation lookup: one card. Required case-artifact accesses are the same four when both queries are asked. The efficiency gain is structural reuse of one routing card instead of four finding documents; it is not a measured reading-time claim.

## Boundary use

Changed input: L3 maps A2 to an independent event E8, conditionally independent of E7 given D.

Organization B now admits two LRs: posterior `(1/9×4×4)/(1+1/9×4×4)=16/25=.64`; action changes to replace. Proposal history still contains two proposals. The card therefore does not impose deduplication by field name or by finding; it makes aggregation follow lineage.

Second boundary: if L3 is absent, current posterior is unresolved rather than `4/13` or `.64`. Counting fields twice fabricates independence; counting them once fabricates dependence. The next action is retrieve lineage or use a conservative interval, not choose a convenient point.

## Organization decision and actual use

Use Organization B for repeated evidence questions. It preserves the canonical register and source provenance while joining four findings at the point where each changes an operation. Keep Organization A as the audit view showing which original application established each rule.

The selected card was actually used above on the frozen current/historical queries and the independent-E8 boundary. It returned `4/13/inspect`, two proposal-history entries, and `.64/replace` after the lineage change.

Actual mind change: I changed from a source-ordered four-document retrieval to a query-to-evidence card for operational use, while retaining source order for provenance.

Benefit or harm: The card prevented two submitted fields from becoming two likelihood factors, preserved both submissions in history, answered two different queries from different views, and changed its action when independence became supported.

Verdict: KEEP for this consolidation and three executed uses. The four findings receive no duplicate discovery credit.

Content assessment: Scope, exceptions, arithmetic, missing-lineage state, proposal/history distinction, and provenance are retained.

Organization assessment: B reduces compulsory finding lookups from four to one for this reuse pattern; A remains superior for auditing derivation. No global or measured-efficiency optimum is claimed.

Next attempts: Time independent readers using A and B; test partial correlation rather than binary shared/independent lineage; add conflicting source credibility; test canonical changes that invalidate the trigger index.
