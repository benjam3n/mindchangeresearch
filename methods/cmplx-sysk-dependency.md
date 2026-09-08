Intended mind change: Map how an outcome's delay interacts with exposure, credit and later method selection before judging a research method from its visible KEEP count.

# SYSK dependency — delayed observations in an adaptive inquiry

Actual starting judgment: The current corpus already separates attempted and observed outcomes. The feedback path by which observation timing can change subsequent exposure has not yet been represented for the following finite controller comparison.

Original: ../sources/root-sysk.md, SHA-256 8a7f6eded655be9198b0b7c00ec3cf479b942d463d529125f1e3c7dace4eeb77; separate requirements in root-sysk.requirements.txt. The same current-requirements digest was read for this dependency as for CMPLX. SYSK defines no numerical 8x floor. All seven operations are addressed through ten components, fourteen connections, three loops, six intervention points, event traces and a changed-horizon boundary. This is a subordinate execution for CMPLX-01, not an extra allocated exposure slot.

Boundary: a declared adaptive inquiry controller, from available attempts to later selection. Real human psychology and actual effect sizes are outside the finite model. Attempt A takes one time unit and produces value 2 at completion. Attempt B takes two units and produces value 12 at absolute time 4. The evaluation target is total realized value by time 4. These are synthetic inputs, not estimates for named Reasoningtool skills.

Ten components: goal/horizon defines the evaluated outcome; candidate inventory holds A and B; dispatcher chooses an attempt; executor occupies time; observation calendar records when a result becomes available; outcome store preserves observed values; pending store retains unobserved outcomes; credit rule assigns comparison values; eligibility record preserves preconditions; and continuation queue carries a concrete next attempt.

| Connection | What flows | Type and direction | Structural strength |
| --- | --- | --- | --- |
| Goal → credit rule | Value target and time-4 horizon | Information, one way | Required |
| Inventory → dispatcher | Available actions A/B | Information, one way | Required |
| Eligibility → dispatcher | Feasible starts and remaining time | Dependency, one way | Required |
| Dispatcher → executor | Selected action and start | Control, one way | Required |
| Executor → observation calendar | Completion and observation times | Information, one way | Required |
| Executor → pending store | B awaiting time 4 | Information, one way | Required for delayed B |
| Observation calendar → outcome store | Released observations | Information, one way | Required |
| Pending store → outcome store | B when its time arrives | Information, one way | Required for B |
| Outcome store → credit rule | Observed count and value, kept distinct | Information, one way | Required |
| Credit rule → dispatcher | Comparison result | Influence, one way | Strong by defined policy |
| Executor → eligibility | Consumed time | Resource dependency, one way | Required |
| Dispatcher → continuation queue | Next selected action | Control, one way | Required |
| Continuation queue → inventory | Candidates for the next selection | Information, one way | Optional extension |
| Goal → eligibility | Remaining horizon | Constraint, one way | Required |

“Required” here is a property of the defined controller, not a measured causal effect strength. Direction is explicit; the cycles arise across multiple one-way edges.

Reinforcing loop R1: more exposures of an immediately reported action → more visible outcome entries → higher count-based selection weight → more exposures of that action. It amplifies exposure when the proposed rule uses counts. Its speed is the one-unit A observation delay. This is a mechanism of the stipulated rule, not evidence that the current research dispatcher actually uses it.

Balancing loop B1: more executed work → less remaining time → fewer feasible starts → less additional execution. Its set point is the fixed time-4 boundary. Balancing loop B2 in the alternative controller: more still-pending delayed work → more recorded future outcomes → less repeated allocation to an already pending attempt → lower pending duplication. B2 requires the explicit pending record; it is not inferred from a claim that all stable systems must contain it.

Six intervention points, from narrow parameter to broader rule: change a display refresh interval (low effort, no changed payoff times); buffer pending observations (low effort in this model, preserves B); carry observation time along the executor-to-calendar flow (low effort, prevents an early null classification); replace count-only comparison with the stated value/horizon criterion (low effort in the finite code, changes selection); state whether the goal is value by time 4 or value eventually (low effort to state, consequential decision difference); distinguish observable report frequency from beneficial change itself (conceptual frame, requires actual adoption rather than a new label).

Stability: the finite controller is transitioning toward termination at time 4; no equilibrium or production resilience is claimed. Removing the observation calendar prevents B from ever being recognized at its correct time in this design. Removing the pending store makes the distinction between “nothing happened” and “not yet observed” unavailable to this controller. A robust implementation could retain equivalent information elsewhere; no claim that one particular file is indispensable follows.

Bottleneck assessment: B's value cannot be observed before its stipulated time 4, regardless of faster report formatting. The system demands that value by the horizon; the temporal gap is two units after B's execution ends. Faster execution of unrelated A does not remove the gap, but can still add independent value while B is pending. Therefore the source's general bottleneck maxim is not used to conclude that every non-bottleneck improvement is worthless in this multi-output task.

Emergent result from the interaction: A,A,A,A produces four observed positive events worth 8. B,A,A produces three observed positive events worth 16 by the same horizon. Count and value disagree. The difference is produced by duration, delayed release, value aggregation and selection together; one component's event count does not supply the comparison.

The executed traces are in root-delayed-feedback.json. If B instead releases at time 7, B,A,A yields only 4 by time 4 while A,A,A,A yields 8. Retaining a pending outcome does not license crediting it before the evaluated horizon. The delayed value can still matter under a later horizon, which is a separately declared objective.

Additional comparison before the verdict: repeatability of B was unspecified in the initial two-policy input. Exhaustive duration-feasible enumeration now preserves both extensions. If B is independently repeatable, B,B yields 24 and improves on B,A,A. If B is a one-off experiment, the best value is 16, achieved by B,A,A, A,B,A or A,A,B. The original two-policy comparison remains valid, but B,A,A is not a proven global optimum under unspecified repeatability. The exact enumeration is in root-delayed-feedback-repeatability.json. No new constraint was inserted merely to preserve a preferred schedule.

Actual mind change: The working controller comparison now retains execution time, observation time and evaluation horizon as separate inputs. It changes the preferred schedule when B's release crosses the horizon.

Benefit: It prevents both a premature null verdict and premature positive credit in the finite comparison. It does not estimate the value of real delayed human learning.

Verdict: KEEP — scoped dependency model and evaluated boundary. Parent CMPLX can use it without counting a second independent discovery.

Organization: Preserve the event trace beside the loop map. A cycle diagram alone hides the absolute time at which B contributes; a raw event list alone hides how credit changes future exposure.

Next attempts: Give B an uncertain outcome; compare two observation windows with equal total exposure; introduce a source change that invalidates only future reuse.
