Intended mind change: Replace the judgment “the hard deadline requires immediate use of the certain machine” with a timing policy that separates reserving capacity, receiving information, committing money, starting work, and completing work—if the original TD products show that the separation preserves certain completion.

Actual starting judgment: Choose and start machine A at 09:00 because the hard deadline makes the certain machine the temporal priority.

Actor: the model's explicit scheduling policy. No human belief, behavior, learning, emotion, or model-weight change is tested or claimed.

Concrete input: Frozen before evaluation in `../frozen-inputs.md` at 2026-09-08T08:12:00Z and reproduced in `source-receipts/prospective-input.freeze.json` (SHA-256 `15a8f05cbec87702182fec349d483066b2b79959e7173591db28261b4b23bbd4`). At 09:00, A costs $10 and can be reserved with a full refund only through 09:20; B costs $0, its availability is revealed at 09:15, and its stipulated availability is 0.6. Either run takes 20 minutes. Completion by 09:40 is hard. A reservation guarantees A's use; no switching/setup time or unpriced reservation cost is stipulated. Those last two boundary assumptions are explicit rather than hidden.

# TD products

## Deadlines and convergence points

| Time | Event | Temporal effect |
|---|---|---|
| 09:00 | Decision opens | A can be reserved without yet selecting the machine that will run. |
| 09:15 | B's availability is revealed | The information can select B or A while both remain deadline-feasible. |
| 09:20 | A's refund closes | A changes from refundable reservation to a $10 commitment. |
| 09:20 | Latest feasible start on either machine | A 20-minute run started later misses 09:40. |
| 09:40 | Hard completion deadline | Any unfinished branch fails the stipulated requirement. |

The refund cutoff and latest-start boundary converge at 09:20, but the information event occurs five minutes earlier. Information timing and option expiry are therefore different events even though they influence the same decision.

## Dependencies

`Reserve A at 09:00 → preserve guaranteed A capacity → observe B at 09:15 → choose and start a machine → complete by 09:40.`

The B branch depends on B being reported available. The A branch depends on retaining its reservation. Cancellation of A depends on selecting B and occurs no later than 09:20. Starting either run depends on selection and must occur no later than 09:20.

## Backward schedule

| Branch | Deadline | Duration | Latest start | Decision available | Slack if started when information arrives |
|---|---:|---:|---:|---:|---:|
| B available | 09:40 | 20 min | 09:20 | 09:15 | 5 min |
| B unavailable, use reserved A | 09:40 | 20 min | 09:20 | 09:15 | 5 min |

At 09:15: if B is available, cancel A and start B; if B is unavailable, retain and start A. Both finish at 09:35. The five minutes belong at the project end as a common buffer, not as avoidable delay inside each branch.

## Time-critical path

The fallback path becomes critical only if selection/start is deferred to 09:20: `09:20 start A → 20-minute run → 09:40 finish`, with zero slack. Under the selected 09:15 action rule, both branches finish at 09:35 and the project buffer is five minutes. Reserving A at 09:00 is a predecessor that preserves the fallback; it is not equivalent to starting A.

## Option regions

| Region | Feasible policy | Foreclosed policy |
|---|---|---|
| 09:00–before 09:15 | Reserve A and wait for the stipulated information. | Selecting B from observed availability; the information does not yet exist. |
| 09:15–09:20 | Use the observation: B available → refund A and start B; B unavailable → start A. | None of the stipulated completion branches, provided action occurs by 09:20. |
| exactly 09:20 | A can still be refunded under “through 09:20,” and either run can finish exactly at 09:40. | Any positive unmodeled transaction/setup duration would defeat this equality boundary. |
| after 09:20 | No new 20-minute start can satisfy 09:40. | Both fresh-start branches. |

The conditional policy completes with probability 1 under the frozen assumptions. Its expected monetary cost is `0.6($0) + 0.4($10) = $4`, versus $10 for starting A immediately. No value for completion earlier than 09:40 was stipulated; none is invented.

## Distinct later use on a changed input

Changed input fixed by the pre-registered test: B's availability is revealed at 09:25; every other term remains fixed.

Backward scheduling still gives 09:20 as the latest start. A B start at 09:25 completes at 09:45 and fails. B's information now arrives outside the feasible-action region, so it has no value for the hard-deadline selection. The changed policy is: reserve A at 09:00 and start A no later than 09:20; do not wait for the 09:25 report. This policy differs from the original-input policy, which waits until 09:15 and conditions the machine choice on the report.

# Result

Actual mind change: The working judgment changed from “start A at 09:00” to “reserve A at 09:00, wait only until the 09:15 information event, then start B if available and otherwise A.” It also changed from treating 09:15 as the deadline to treating 09:20 as the converged option-expiry/latest-start boundary, with a 09:15 action rule that preserves a five-minute end buffer.

Benefit or harm: Beneficial within the stipulated case. It preserves certain completion, reduces expected cost from $10 to $4, and makes the changed 09:25 input reverse the wait policy. Harm was not observed. The result depends on the explicit guarantee, full-refund, and zero-switch-time assumptions; weakening them reopens the comparison.

Verdict: **KEEP (scoped).** The decisive evidence is the backward schedule plus the branch calculation. The strongest contrary branch is that immediate A use finishes earlier; no benefit for finishing before 09:40 exists in the frozen input, so that branch does not defeat the scoped cost-and-deadline result.

Performative check: Not merely relabeling. The procedure changed the selected action, produced two exact latest-start calculations, located a five-minute common buffer, calculated a $6 expected-cost difference, and generated a different policy on the pre-registered 09:25 reuse.

Novelty assessment: The general facts that early preparation can preserve options and that durations imply latest starts already occur elsewhere in the corpus. The retained addition is narrower: the information event, refundable reservation, monetary commitment, latest start, and completion deadline occupy distinct positions, and moving only the information event across the latest-start boundary changes the selected policy. Corpus search found no prior machine/refund instance or this five-boundary configuration. This is configuration-level novelty, not a new universal scheduling law.

Content assessment: All five TD application products and all four verification items are present. The original TD source specifies no numerical 8x floor; this record expands the scope with four option regions and a changed-input reuse but does not claim “8x certification.”

Organization assessment: The order `deadlines → dependencies → backward schedule → critical path → option regions → changed-input reuse` made the selected action recoverable without mixing calendar facts with reversibility claims. A single timeline table alone would hide branch dependencies; branch prose alone would hide the equality boundary. Both are retained.

Next attempts: Move only the task duration from 20 to 21 minutes and test whether all waiting becomes infeasible; add a positive switching time and locate the new latest decision boundary; give earlier completion a specified monetary value and test whether immediate A use can win; replace the single B report with sequential noisy reports and test buffer consumption; test two tasks competing for A under earliest-deadline-first rather than one task with two machine options.
