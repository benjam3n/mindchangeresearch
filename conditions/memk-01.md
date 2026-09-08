Intended mind change: Capture the infeasibility result in a form that supports the next constraint-change decision without replaying every permutation.

Starting working judgment: The six-order table establishes impossibility for one case. A later reader deciding what to change needs the forcing bound and its scope more than the full chronology of the calculation.

Original source: ../sources/conditions-memk.original.md. Exact stdout and separate requirements receipt: ../sources/conditions-memk.requirements.txt; byte checks are in source-receipts.json.

Execution scope and depth: No numerical 8x floor exists. A sub-200-word entry, tags, hierarchy, links, future-reader review, actual next-use derivation and maintenance trigger were produced; no future review claimed.

CAPTURE TYPE: hard-won finite result and decision rationale. EXPIRY RISK: immediate if durations, release times, deadlines, processor count or preemption change. The entry must retain those conditions.

--- KNOWLEDGE ENTRY ---
For A(0,3,6), B(1,1,2), C(2,2,4), no one-processor nonpreemptive schedule meets every deadline with zero switching cost. B is forced into 1–2 and C into 2–4; A then finishes no earlier than 7, past 6. All six job orders were checked in fresh-task-feedback.json. Reordering unchanged jobs is settled for this case. Change a declared constraint if the goal must become feasible. Example: extending only A’s deadline to 7 permits B1–2, C2–4, A4–7; a smaller extension cannot beat A’s forced earliest finish of 7. Do not apply this result to preemptible work or a different release/deadline set without recalculation. Tuple fields are release, duration, deadline.
--- END ---

The entry is under 200 words. Tags: schedule-infeasible, forced-interval, change-constraint, conditions. Parent category: time/opportunity. Links: ld-01, rva-01, fresh-task.json, fresh-task-feedback.json. Retrieval trigger: repeated schedule search on a set whose forced intervals already establish a bound.

Future-reader check: context is self-contained, tuple meanings explicit, the next available change is concrete, the example supplies both a lower bound and a feasible witness, and the exception is retained. Next review is triggered by changed inputs or the next use of the result; no timed reminder is created.

Actual immediate use: the new query is “what is the minimum extension of A’s deadline if every other condition stays fixed?” The forcing bound gives A finish≥7; the displayed witness attains 7. Therefore the minimum extension is 1 unit. This is a derived use of the captured result, not a fresh claim of human retention. The old scenario remains valid history and is not deleted when the feasible variant is written.

Pruning: no old entry is removed; the new entry names its expiry conditions so a future different-input case cannot silently inherit the result.

Actual mind change: The conditions agent captured the forcing relation and used it to answer a new minimum-deadline-extension query with a lower bound and feasible witness.

Benefit: The retained result now directs a concrete permissible change without enumerating the unchanged cases again. This is current artifact-supported use, not delayed memory evidence.

Verdict: KEEP

Organization: A short conditional decision entry is more useful for the next constraint question than either a bare “infeasible” label or a replay of all six rows.

Next attempts: Change preemption instead of the deadline; add a switching cost; revisit the entry whenever any tuple changes.
