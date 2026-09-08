# DWT — stop checking and preserve execution time

Intended mind change: Stop analysis using an external decision criterion instead of a feeling of completeness.

Actual starting judgment: A third integrity check felt safer even though two independently implemented checks already agreed.

Concrete input: `frozen-inputs.md`, DWT case. Now 09:20; release deadline 09:32; release takes four minutes; remote third check takes ten minutes.

## Interpretation and branch

Interpretation: completeness check under a hard deadline. Section A applies.

A1. Deadline: 09:32.

A2. Time remaining: 12 minutes.

A3. Current best option: begin the four-minute release now using the archive whose two independent SHA-256 implementations match the expected digest.

A4. I would switch from release to stop if I learned that the two checks share an implementation or byte-source failure, or if any digest mismatched.

A5. No supplied evidence answers that crux. The only proposed remote test takes ten minutes; waiting for it leaves two minutes for a four-minute release and guarantees deadline failure. The specific evidence is not obtainable by that route while preserving feasibility.

A7. The current option is acceptable under the stated criterion: two independent implementations match the expected digest, and no mismatch or shared-failure evidence is present. Spend remaining time on execution.

Written decision: begin release no later than 09:28; do not run the ten-minute remote check first.

Rationale: the proposed information route cannot improve the release decision before the decision ceases to be executable. This is not a claim that two hashes prove archive correctness; it is a deadline-bounded stop.

## Distinct later use and boundary

Later input: an observed build log shows both hash implementations read the same stale cached file rather than the release archive. That is the exact A4 trigger. The action changes to stop release despite expiry; the newly observed shared byte-source failure defeats the evidential independence assumed by the current decision.

Second boundary: if the remote check took two minutes instead of ten, it could complete at 09:22 and still leave ten minutes for release. Then obtain the check first because it can answer the crux without destroying feasibility.

## Outcome

Actual mind change: I changed from “one more check is safer” to “only a check that can arrive before the executable-action boundary belongs in the pre-action queue.”

Benefit or harm: The decision preserves eight minutes of schedule margin in the frozen case and retains a concrete stop trigger. No real release was performed.

Verdict: KEEP — complete for the constructed time-pressured decision; archive correctness outside the supplied checks remains unresolved.

Content assessment: The deadline, leading option, mind-change evidence, learnability, acceptability, decision, and two boundaries are explicit.

Organization assessment: `crux → acquisition duration → remaining execution duration` was more discriminating than a generic completeness checklist.

Next attempts: Add asymmetric failure costs; test uncertain check duration; compare this rule when the deadline is soft; measure whether execution margin actually reduces failures on real tasks.
