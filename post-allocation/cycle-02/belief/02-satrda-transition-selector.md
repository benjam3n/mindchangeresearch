# SATRDA — two-run transition-selector divergence

Intended mind change: Find whether the current transition-gate card has a repeatability defect on a fixed belief input.

Actual starting judgment: The card was concise and useful, but “smallest supported transition” did not define whether a belief transition names a representation, an action, or a direction.

Concrete input: the exact fixed case and output contract in `frozen-inputs.md`; target `post-allocation/cycle-01/consolidation-01-transition-gates.md`; independent outputs `satrda-run-a.md` and `satrda-run-b.md`.

## Run definition

Held fixed: alarm data, decision threshold, card, seven output fields, and stop rule. Audit stop: two runs, one comparison, one rewrite queue.

## Concrete divergences

| Field | Run A | Run B | Likely text cause |
|---|---|---|---|
| target transition | belief representation becomes calibrated posterior | immediate action becomes inspect | “transition” has no typed output interface |
| locus | working belief representation | decision-output action | “controlling locus” does not state whether upstream epistemic state or downstream action wins |
| unresolved dependency | parameter/copy validity outside finite model | real-world applicability of all case parameters | no required dependency taxonomy |

No divergence occurred in evidence count, chosen skill, posterior, or action. Thus the ambiguity changed the declared state and locus but did not change the finite decision.

## Dependency gate

The original SATRDA Step 5 requires `library/procedures/core/goal_analysis/analysis_protocol_clarity_and_validity.yaml`. That dependency is not present in the RSI archive available to this run and was not obtained through the original reader. I do not invent or silently replace it. The following rewrite queue is derived only from Steps 1–4 and is provisional, not a completed protocol-clarity application.

## Rewrite queue

1. Define `transition_type ∈ {epistemic-representation, attention, action, artifact-state, communication, human-state-unobserved}`.
2. Require separate fields for `upstream_state_transition` and `downstream_action_transition`; allow both when one causally controls the other.
3. For belief updates, require `state_variable`, `evaluation_criterion`, and `admissible_direction`; an evidential direction cannot be selected before the evidence gate supports it.
4. Define locus precedence: choose the earliest state whose correction is necessary and sufficient to settle the downstream action; preserve downstream action as output, not as the same transition.
5. Type unresolved dependencies as model-parameter, evidence-lineage, authority, delayed observation, or external-world transfer.
6. Make “done” checkable: required fields filled, inference verified, action rule applied, and remaining dependencies typed.

## Distinct later use

Applied provisionally to the same case: upstream transition is `epistemic-representation`; state variable is `P(D|evidence)`; criterion is Bayesian consistency under the supplied joint structure; admissible direction is whichever posterior the calculation yields; downstream action is inspect. This removes the Run A/Run B naming conflict while retaining both states.

## Outcome

Actual mind change: I changed from treating the card’s single transition/locus fields as determinate to treating them as under-specified for belief-to-action chains.

Benefit or harm: The rewrite queue preserves the same correct posterior and action while preventing representation change and action change from being collapsed into one field. The missing required clarity procedure prevents full SATRDA completion.

Verdict: KEEP for the observed two-run divergence and provisional repair; PARTIAL for original-procedure completion because the named Step-5 dependency is unavailable.

Content assessment: Two fresh runs, fixed fields, concrete divergences, causes, and rewrite queue are present. No claim of cross-model repeatability is made.

Organization assessment: Keeping both run artifacts beside one comparison makes divergence auditable without overwriting either run.

Next attempts: Obtain the exact clarity YAML and execute Step 5; repeat with independent executors; test a case where locus divergence changes the action; define transition types without assuming this provisional enum is exhaustive.
