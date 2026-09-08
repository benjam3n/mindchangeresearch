Intended mind change: Determine how delayed evidence, effort, selection and evaluation goals interact when the system chooses its next mind-change attempt.

# CMPLX 01 — the controller can prefer what is easiest to observe

Actual starting judgment: The user wants repeated beneficial changes and increasingly useful organization. Required exposure counts are already separate from KEEP counts. What remains unresolved in this specific comparison is whether choosing from immediately visible positive-event counts serves the fixed value-by-horizon objective.

Original: ../sources/root-cmplx.md; separate requirements: ../sources/root-cmplx.requirements.txt. There is no numerical 8x scale in the original. All five operations are performed through eight complexity-source dispositions, four interacting parts, a complete SYSK dependency, two executed schedules, three boundary analyses and a later controller disposition. The bounded simulation does not claim to solve the full human/model research problem.

The substantive problem is an adaptive selection loop in which opportunities differ in duration, observation delay and useful consequence. Many variables matter: available action, start time, execution duration, observation time, value, remaining time, selection proxy, eligibility and retained pending state. Feedback is present by definition when observed outcomes affect later selection. Uncertainty is absent in the two stipulated deterministic payoffs but remains unknown in real use. Conflicting objectives appear if a controller optimizes event count while evaluation asks for total value. Nonlinearity enters at the horizon: a release just before versus just after time 4 changes whether it counts. Time dynamics are explicit. Measurement difficulty enters because an unobserved delayed effect and a true null effect look identical to a store that records only completed observations. No unpredictable human emergent behavior is asserted.

The primary complexity is feedback coupled to delayed observation and a mismatched proxy. The selected primary tool is SYSK, executed in cmplx-sysk-dependency.md. Supporting tools are exact event enumeration for the declared schedules, horizon sensitivity and explicit comparison of the count proxy with the fixed outcome criterion. The broader system contains more uncertainty than this finite model; the calculation isolates one interaction rather than claiming a complete forecast.

Four parts are not independent. P1, exposure allocation, determines which actions can later generate observations. P2, execution and observation timing, determines when the outcome store can see them. P3, evaluation, determines whether a visible event counts as useful by the goal's horizon. P4, future selection, converts that comparison into later exposure. P1→P2→P3→P4→P1 is a feedback path. Time consumed in P2 also changes P1's remaining feasible set. The evaluation horizon affects P3 and the value of alternative starts in P1.

Analyzing the parts separately loses two things: a low current visible count can result from observation delay rather than low value, and a high visible count can result from short repeated actions rather than greater total benefit. These are distinct mechanisms; neither establishes a real skill's quality without suitable observations.

The finite inputs, held fixed across both policies, are A duration 1/value 2 at completion and B duration 2/value 12 released at time 4. Total available time is 4. The evaluated criterion is realized value by time 4, not report count. A count-seeking comparator schedules A,A,A,A; a schedule retaining delayed value is B,A,A.

| Policy | Execution schedule | Positive events visible by 4 | Value by 4 |
| --- | --- | ---: | ---: |
| Immediate event count | A 0–1; A 1–2; A 2–3; A 3–4 | 4 | 8 |
| Delayed value retained | B 0–2, released at 4; A 2–3; A 3–4 | 3 | 16 |

These are designed comparators, not a claim that the current system actually chose the first policy. The code produces both traces. The comparison shows that a higher count can coexist with a lower value under the fixed criterion.

Cross-cutting concerns: the horizon affects eligibility and credit; pending-state retention affects both evaluation and duplicate allocation; and source scope determines whether an old effect estimate applies to a new task. A second-order path is visible in the defined count policy: an early A result increases its future count weight, causing another A exposure and another early result. The alternative retains B until its release, so the absence of an early B report does not erase its declared future contribution.

Three boundaries constrain the finding. If B releases at time 7, only the two A results contribute by time 4, totaling 4; the all-A policy then wins with 8. If B's value is 4 at time 4, B,A,A ties the all-A policy at 8; if it is less than 4, it loses. If the goal itself is the number of independently valuable events, counting can be appropriate, but that is a new evaluated criterion and must not be silently substituted for total value.

Synthesis: the original complexity map identified the feedback path; the event calculation established the count/value reversal; horizon sensitivity established its boundary. A useful controller needs observation time and evaluated horizon wherever delayed effects influence comparison. It does not need every pending event to receive optimistic credit. Confidence is high in the declared traces and inequalities; real benefit magnitudes and response delays are unknown.

Actual later application: a new candidate C has completed its execution but no outcome is yet observed, and its effect size is unknown. The revised record is “executed; outcome pending; value unknown; observation condition retained.” It is neither zero-benefit evidence against the method nor a positive KEEP. A separate candidate D has an observed null result under the specified observation window; that result remains a null. The controller representation therefore distinguishes two superficially empty outcome records without inventing a payoff for C.

Additional comparison before the verdict: repeatability of B was unspecified in the initial two-policy input. Exhaustive duration-feasible enumeration now preserves both extensions. If B is independently repeatable, B,B yields 24 and improves on B,A,A. If B is a one-off experiment, the best value is 16, achieved by B,A,A, A,B,A or A,A,B. The original two-policy comparison remains valid, but B,A,A is not a proven global optimum under unspecified repeatability. The exact enumeration is in root-delayed-feedback-repeatability.json. No new constraint was inserted merely to preserve a preferred schedule.

Actual mind change: My working adaptive-selection model now preserves observation time and the evaluation horizon when it compares methods. It produces different pending-versus-null dispositions for C and D and different schedule choices across the time-4/time-7 boundary.

Benefit: The finite case prevents immediate report count from standing in for the fixed value criterion, while the later case preserves genuine lack of evidence. It does not establish that a particular delayed human intervention is worth pursuing.

Verdict: KEEP — scoped controller result and a concrete later disposition. The SYSK dependency and this parent share the finding rather than earning duplicate global credit.

Organization: Keep exposure, execution, observation and value as linked fields with distinct times; use a compact event view for present selection and retain the loop view for diagnosing selection effects. A single score loses the timing boundary; separate unlinked files lose the dependency.

Next attempts: Compare an uncertain delayed payoff against a known immediate one; measure how a real observation window changes which outcomes are visible; test whether a method's benefit survives a change in target activity.
