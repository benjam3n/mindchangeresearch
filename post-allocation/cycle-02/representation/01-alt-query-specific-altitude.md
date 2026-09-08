# ALT — different queries need different altitudes

Intended mind change: Stop treating one maximally compressed representation as best for both action and audit.

Actual starting judgment: A six-line summary seemed more efficient than the 24-row event record.

Concrete input: `frozen-inputs.md`, ALT case, completed by the pre-execution `event-record-fixture.md`.

## Interpretation and goal type

Interpretation: altitude adjustment. The immediate task has two goals: decide what to do now and understand what caused a prior rollback. Section B is applied to Q1; Section A is applied to Q2.

## Candidate representations

L0 is the 24-row event record.

L1 is the state-transition table:

| Transition | Time | From | To | Trigger |
|---|---|---|---|---|
| T1 | 10:04 | draft | review | row 5 |
| T2 | 10:08 | review | accepted | row 9 |
| T3 | 10:13 | accepted | rollback_pending | row 13: compatibility false because O0 basis C0 ≠ C1 |
| T4 | 10:19 | rollback_pending | review | rows 17–20 restored C0/O0 |

L2 is the six-line narrative: “A record moved from draft to review and then acceptance. A compatibility problem was found. The export was quarantined and notice canceled. A prior snapshot was restored. The record returned to review. Recalculation was assigned.”

## Q1 — decide

B1. Decision: choose the authorized next action at 10:23.

B2. Natural level: middle. The decision concerns the record’s current state and the next dependent action, not every event row or the whole program.

B3. One level up: the larger goal is a semantically valid accepted record. This rules out publishing the existing O0 as though computed under C1.

B4. One level down: rows 20–24 show current status review, recomputation requested, B assigned, deadline 11:00. The immediate executable action is recompute the outcome under the intended criterion before acceptance.

B5. Use L1 plus the current tail rows 20–24. L2 alone omits criterion identities; L0 works but requires scanning 24 rows.

Answer to Q1: B is authorized to recompute; publication is not yet authorized.

## Q2 — understand

A1. Question: which prior field caused the rollback?

A2. Pain: L2 supplies a general compatibility problem but no field identity; it is too abstract.

A4. Zoom in. The observable prediction is a row where compatibility changes and a basis mismatch is named. L0 row 13 contains `compatibility: unknown → false` and names `O0 basis C0 ≠ C1`; row 7 supplies the preceding criterion change.

Answer to Q2: the rollback transition was triggered by row 13’s compatibility field, whose value recorded the conflict introduced by row 7’s C0→C1 criterion change while O0 remained computed under C0.

## Information-loss test

| Required fact | L0 | L1 | L2 |
|---|---:|---:|---:|
| current state review | yes | yes | yes |
| recomputation assignee B | yes | no without tail | no |
| criterion identities C0/C1 | yes | yes | no |
| exact trigger field row 13 | yes | yes | no |
| full chronology | yes | transitions only | no |

No one representation dominates. Q1 uses L1 plus the current action tail; Q2 uses L0 anchored by L1’s trigger pointer. The six-line narrative is a communication view, not an audit or execution view.

## Distinct later use

When asked “why was the notice canceled?”, L1 identifies T3 but not the notice event; its trigger pointer narrows L0 to rows 13–16, where quarantine precedes cancellation. This hybrid answers in four inspected rows rather than scanning all 24, while preserving the exact cause chain.

## Outcome

Actual mind change: I changed from one-summary preference to query-specific altitude with explicit bridges between transition and event levels.

Benefit or harm: The selected views answered both frozen queries without losing criterion identity or forcing a full-table scan for each. Inspection counts are structural here, not measured human time.

Verdict: KEEP — useful within the finite fixture; no universal best altitude is claimed.

Content assessment: The natural level, one-up/one-down checks, information-loss test, actions, and reuse are explicit.

Organization assessment: A transition index pointing into canonical events is better on these queries than either a flat raw log or a narrative alone. This is later support for the prior query-conditioned location and retrieval-cost findings, not a new discovery credit.

Next attempts: Test a query requiring every event; compare expert and novice audiences; measure lookup time with independent readers; test whether trigger pointers survive event-log edits.
