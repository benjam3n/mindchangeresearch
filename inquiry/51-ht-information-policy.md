Intended mind change: Stop carrying the AV50 half-immediate/half-information policy beyond its proved p=1/2,c=1 case, and choose a policy from tests that preserve the full equal-accuracy joint-distribution family.

Actual starting judgment: `50-av-regret-family.md` establishes q=1/2 only at prior p=1/2 and observation price c=1. Before the staged tests, I treated q=1/2 as a live candidate at changed priors but did not regard its generalization, the six-policy reduction, the prior-segment parameterization, or the interval-prior optimum as established. The preregistration records this uncertainty and includes extensions assigned low prior confidence; it does not invent a prior belief that the extensions were true.

Concrete input: a stipulated binary good/bad state and positive/negative signal; P(good)=p; overall correct classification probability 4/5; act payoff +6 in good and −4 in bad; decline payoff 0; observation price c; linear expectation; and a fixed randomized policy chosen before the hidden joint matrix. The actor is the current inquiry model. No person buys information or supplies preferences, and no market, behavioral, emotional, bodily, or durable-learning effect is observed.

Original HT: `../sources/inquiry-ht-resume.original.md`; requirements: `../sources/inquiry-ht-resume.requirements.txt`. Required EMV: `../sources/inquiry-emv-resume.original.md`; requirements: `../sources/inquiry-emv-resume.requirements.txt`. Current `read_original.py` outputs match all four verified files byte for byte. HT and EMV are executed at 8x: seven hypotheses, four preregistered primary tests per hypothesis, six competing explanations, seven falsification attempts; twenty-eight primary tests; five independent check forms; six conditional-probability cross-checks; at least six edge cases; and seven confidence calibrations.

## Context and variant

Time pressure NORMAL; consequences LOW outside the stipulated model and material within the next policy calculation; tests CHEAP and exactly reproducible; domain expertise INTERMEDIATE because the algebra is inspectable but translation errors remain possible. Selected variant: HT-Full. Universal claims, a changed policy set, and a later-use requirement warrant all seven stages plus replication rather than a quick numerical spot check.

## 1. Claims, scope, and competing claims

Write the joint cells as (good+, good−, bad+, bad−). “Accuracy 4/5” means good+ + bad− = 4/5, not fixed sensitivity or specificity. A policy is a distribution over six maps chosen before the hidden joint matrix: act now; decline now; buy then act only on positive; buy then act only on negative; buy then act after either signal; buy then decline after either signal. Worst regret is the maximum, over admitted hidden matrices, of best pure-policy payoff minus the fixed mixture payoff.

The scope excludes unknown signal accuracy, more than two signals, nonlinear utility, endogenous price, an adversary observing the random draw, human risk attitude, deadlines, and empirical signal performance. Those changes reopen the result.

Competing explanations retained from the frozen preregistration:

- E1: q=1/2 is a symmetry artifact at p=1/2; changing p destroys it.
- E2: apparent prior effects come from invalid matrices that fail the fixed overall-accuracy constraint.
- E3: apparent gains let the response map depend on the hidden matrix.
- E4: apparent gains are coarse-grid or floating-point artifacts.
- E5: q=1/2 remains best under prior uncertainty but its guarantee worsens.
- E6: the result comes from unobserved human utility or real signal performance.

E1–E5 make different exact predictions below. E6 cannot account for the stipulated arithmetic because no human or market observation enters it; this does not reject E6 as an account of real-world choices outside the model.

## 2–3. Hypotheses, falsifiers, and priors

The plan was frozen in `ht51-preregistered.json` before execution, SHA-256 `0617e3de9120cc6246bdfa485e46bcb5dfc1f97abb920c1943350a9762f7c804`.

| H | Exact hypothesis and decisive falsifier | Prior and sensitivity | Prediction before results |
|---|---|---|---|
| H1 | At c=1, q=1/2 minimizes worst regret for every known p∈[1/5,4/5] over all six maps. One admitted p with a strictly better policy rejects it. | .25 [.10,.50] | p=1/4 and p=3/5 reject; optimum need not vary monotonically. |
| H2 | For every p∈(0,1), every and only accuracy-4/5 joint matrix is (t,p−t,1/5−p+t,4/5−t), max(0,p−1/5)≤t≤min(p,4/5). One valid matrix outside or invalid point inside rejects it. | .95 [.70,.99] | endpoints/midpoints valid; one rational step outside has a negative cell. |
| H3 | For every p∈[1/5,4/5] and admitted matrix, buy-act-positive has maximal gross purchased-signal payoff. One matrix with a strictly better response rejects it. | .35 [.10,.70] | high-prior lower endpoints reject via act-after-both. |
| H4 | For fixed p,c and fixed six-map mixture, worst regret over the complete t segment is attained at an endpoint. An interior t with strictly greater regret rejects it. | .90 [.50,.99] | grids agree; convexity supplies the continuum result. |
| H5 | At c=1, with B=max(0,10p−4), l=2lo+4p−9/5, u=2hi+4p−9/5, a minimax policy buys act-positive with q=0 if u≤B, q=1 if l≥B and u>B, otherwise q=(u−B)/(u−l), mixing with the immediate action attaining B. A lower-regret six-map mixture or failed boundary rejects it. | .85 [.40,.99] | four exact cases agree with the full LP. |
| H6 | For every known p∈[1/5,4/5] and c≥0, deleting buy-both, buy-neither, buy-act-negative, and the inferior immediate action preserves the minimax value. One improved deleted-policy mixture rejects it. | .80 [.30,.95] | full and reduced LP values agree; c=0 permits ties. |
| H7 | With p∈[2/5,3/5], c=1, fixed q=1/2 between immediate act and buy-act-positive has minimax regret 3/10 over all admitted (p,t), and no six-map mixture is better. A regret above 3/10 or lower full-policy optimum rejects it. | .65 [.20,.90] | corner regrets 1/10,3/10,3/10,1/10; full LP value 3/10. |

No empirical base rate exists for this exact family. The priors are subjective pre-test assessments of formulas and translations, not population frequencies. Because the decisive evidence is logical or exact within stipulated premises, prior sensitivity affects translation confidence but does not rescue a universal claim after a valid counterexample.

## 4. Severe test and preregistration

Decision rule frozen before results:

- Reject a universal on one exact admitted counterexample.
- Validate a continuum statement only with a complete derivation; a passing finite grid is a check, not the proof.
- Compute payoffs once by direct four-cell state sums and again through conditional positive/negative branches.
- Compare exact rational candidate values with a separately constructed floating-point linear program over all six policies.
- Preserve every failure and boundary tie.
- Use no alpha, power, p-value, empirical effect size, or numerical Bayes factor: there is no random sample. A logically impossible counterexample has likelihood zero under its exact universal, while implementation and translation risk remain outside that identity.

Falsification attempts: move p below the act threshold; move it above the old symmetric point; include all fixed response maps; probe feasibility boundaries and just-outside points; search 101 interior t values per mixture against endpoint maxima; admit an interval of priors; vary c from zero to larger values.

## 5. Evidence

`ht51-results.json` preserves all twenty-eight primary rows and the adverse results. Re-execution of `run_ht51.py` reproduces the same preregistration hash, test counts, failure list, interval LP, and six matching conditional cross-checks.

| H | Primary rows | Result | Decisive evidence |
|---|---:|---|---|
| H1 | 4 | 0 support the universal | p=1/4: q=0 has regret 0 versus 7/20 for q=1/2. p=2/5: q=1 has 0 versus 3/10. p=19/40: q=3/4 has 3/40 versus 3/20. p=3/5: q=0 has 0 versus 3/10. |
| H2 | 4 | 4 match | At p=1/5,7/20,13/20,4/5, endpoints and midpoints are valid; one step outside either bound makes a cell negative. |
| H3 | 4 | 2 match, 2 reject universal | At p=3/4 lower endpoint, act-both gives 7/2 versus 33/10 for act-positive. At p=4/5 lower endpoint, act-both gives 4 versus 18/5. |
| H4 | 4 | 4 match | Four mixtures at each of four p values have grid maximum equal to endpoint maximum across 101 t values. The grid checks the implementation; the proof is below. |
| H5 | 4 | 4 match | Exact q and rational regret agree with the full six-policy LP at p=13/40,19/40,21/40,7/10, including mixed and pure boundaries. |
| H6 | 4 | 4 match | Full and reduced LP values agree at (p,c)=(1/5,0),(2/5,1/10),(3/5,1),(4/5,2). c=0 retains ties rather than claiming strict dominance. |
| H7 | 4 | 4 corner regrets match | The fixed half policy gives 1/10,3/10,3/10,1/10. Full six-policy LP value is 0.3 with residual at floating precision. |

Exact derivations bearing on the universals:

1. H2: Set good+=t. The good marginal gives good−=p−t; accuracy gives bad−=4/5−t; total probability gives bad+=1/5−p+t. Nonnegativity yields t≥0, t≤p, t≥p−1/5, t≤4/5, exactly the stated interval. Conversely every t in that interval makes the four cells nonnegative, sum to one, preserve p, and preserve accuracy.
2. H4: Each pure payoff is affine in t. The best pure payoff is the maximum of finitely many affine functions and is convex. A fixed mixture payoff is affine, so regret is convex. A convex function on the closed t segment has a maximum at an endpoint; an interior tie can coexist but cannot strictly exceed both endpoints.
3. H6: Buy-both equals act-now−c and buy-neither equals decline-now−c, so c≥0 weakly dominates both. For p>2/5, act-now exceeds buy-act-negative because their difference is 4p+2t+c−4/5>0. For p≤2/5, nonnegativity bounds make buy-act-negative≤0, so decline dominates it. The inferior immediate action is dominated by the other immediate action. Pointwise deletion cannot reduce any state's attainable best payoff or mixture optimum.
4. H5: After H6, the immediate baseline is B and buy-act-positive ranges affinely from l to u. If u≤B choose q=0; if l≥B and u>B choose q=1. When l<B<u, endpoint regrets are q(B−l) and (1−q)(u−B); equalizing them gives q=(u−B)/(u−l). H4 places the worst case at an endpoint.
5. H7: The admitted polygon has the four preregistered corners. The half policy attains maximum regret 3/10. For a lower bound, put adversarial weight 1/2 on corner (p,t)=(2/5,2/5) and 1/2 on (3/5,2/5). Expected regrets for the six pure policies are respectively 3/10,13/10,3/10,33/10,13/10,23/10. Every mixture therefore has maximum regret at least its adversarial average, at least 3/10. The half policy attains that bound.

Six independent conditional-branch cross-checks at p/t=(1/5,0),(1/4,1/20),(3/4,11/20),(4/5,3/5),(19/40,3/10),(21/40,1/2) exactly match the direct four-cell payoff vector. The first includes a zero-probability positive branch; no undefined conditional is smuggled into its state sum.

### EMV 8x

Minimum viable test: rerun the frozen script before using the policy family. Success requires the preregistration hash, 28 rows, declared failures, six direct/conditional matches, exact formula/LP agreement on H5, and interval value 3/10. Failure of any check reopens the relevant hypothesis. The test is cheaper than carrying a wrong policy and is run first; it passed within the stated numerical tolerance.

Twelve validation tests, selected without dropping the remaining sixteen rows:

1. H1 p=1/4 rejects q=1/2 with regret gap 7/20.
2. H1 p=2/5 rejects it with gap 3/10.
3. H1 p=19/40 rejects it with gap 3/40.
4. H1 p=3/5 rejects it with gap 3/10.
5. H2 p=1/5 checks a boundary with a zero cell and two outside negatives.
6. H2 p=7/20 checks an interior asymmetric prior.
7. H2 p=13/20 checks its reflected asymmetric prior.
8. H2 p=4/5 checks the upper boundary.
9. H3 p=3/4 exhibits act-both as strictly better than act-positive.
10. H4 p=9/20 checks four unequal mixtures across 101 t values; the symbolic convexity result supplies continuum scope.
11. H5 p=19/40 checks q=3/4 and regret 3/40 against all six policies.
12. H7 uses the four corners plus the exact primal/dual 3/10 certificate.

Five independent check forms: algebraic feasibility identities; direct four-cell rational payoff sums; posterior-branch conditional evaluation; symbolic convexity/dominance/balancing proofs; and a separately constructed six-policy numerical LP. Agreement is evidence against the named translation and implementation errors, not five independent empirical samples.

Edge cases: p=1/5 with zero positive-signal probability at one endpoint; p=4/5 upper prior boundary; c=0 weak-dominance ties; c=2 high price; p=2/5 immediate-action tie; t just below/above feasibility bounds; p∈[2/5,3/5] rather than known p; and the H3 high-prior matrix where act-both wins.

Confidence calibration after the exact evidence:

| H | Pre-test | Post-test scoped judgment |
|---|---:|---|
| H1 | .25 | <.01 for the universal; exact counterexamples reject it. |
| H2 | .95 | .99 conditional on the stated definitions and algebra; no empirical generalization. |
| H3 | .35 | <.01 for the universal; two exact counterexamples reject it. |
| H4 | .90 | .99 conditional on fixed policy, fixed p/c, and affine payoffs; convexity proves it. |
| H5 | .85 | .99 within c=1 and the stated six-map family; derivation plus four LP checks. |
| H6 | .80 | .99 within c≥0 and the stated maps; pointwise dominance proof plus boundary checks. |
| H7 | .65 | .99 within the declared polygon and randomization; exact primal/dual certificate. |

The .99 values are subjective confidence in the translation and execution, not empirical posteriors from a sampling model. Setting them to 1 would hide file, implementation, or statement-transcription risk.

Prediction log, 2026-09-08: H1's predicted p=1/4 and p=3/5 failures CONFIRMED; H2 boundary validity CONFIRMED; H3 high-prior failure CONFIRMED; H4 endpoint pattern CONFIRMED and proved; H5 formula agreement CONFIRMED; H6 deletion equality CONFIRMED and proved; H7 corner regrets and 3/10 optimum CONFIRMED. “Confirmed” is scoped to these mathematical propositions, not future calibration accuracy.

## 6–7. Belief update, conclusion, and use

H1 and H3 are rejected. H2, H4, H5, and H6 are established within their exact stipulated domains by derivation with independent implementation checks. H7 is established for the stated prior polygon by a matching upper policy and lower adversarial certificate. E1 survives and is sharpened: q depends on p and c through the endpoint balance. E2 is controlled by H2 before payoff evaluation. E3 is controlled by fixed policies and the six-policy LP. E4 is controlled by exact derivations and rational sums; the LP is a cross-check. E5 is rejected by the exact H7 optimum rather than merely receiving a worse guarantee. E6 remains outside the mathematical causal scope and receives no human claim.

The saved later-use case `ht51-later-use-results.json` changes p to 7/20 and c to 11/10 and selects q=1/2 with worst regret 1/10. That is an adverse boundary for the operational claim “changed input always changes q.” It does not restore H1.

`inquiry-resume-ht51-later-use-tests.json` performs three further uses:

- p=7/20,c=1 selects q=3/4, regret 3/40, versus 3/20 for carried q=1/2.
- p=1/4,c=0 selects pure buy-act-positive, regret 0, versus 7/20 for carried q=1/2.
- p=3/5,c=4/5 selects immediate act, regret 0, versus 1/5 for carried q=1/2.

The next model policy is therefore computed from the current p,c and endpoint values; q=1/2 is retained when it solves that input, not as a default inherited from AV50. No real purchase or human action follows from these calculations.

Replication plan: rerun exact state tables and the full LP after any payoff, accuracy, policy-timing, uncertainty-set, or randomization change; require a fresh symbolic reduction for a new signal alphabet; preserve every changed-input later use beside the original test rather than counting it as another primary preregistered row.

Actual mind change: The old half mixture is no longer the default beyond p=1/2,c=1. The current model selects q=3/4, q=1, and q=0 on three distinct changed inputs, while retaining the q=1/2 changed-price boundary where the formula genuinely returns it.

Benefit: On those three later uses, the selected policies reduce worst regret from 3/20 to 3/40, 7/20 to 0, and 1/5 to 0. The benefit is a changed model policy within the stipulated family; it is not a human preference, purchase, or transfer effect.

Verdict: KEEP. The universal half-policy and universal act-positive-response claims are REJECTED; H2/H4/H5/H6/H7 are retained only in their declared mathematical scopes.

Organization: Preregistered hypotheses and all twenty-eight results remain untouched; exact derivations, numerical cross-checks, calibration, adverse cases, and later uses are separate. A numbered test row is not an independent finding unless it supplies a distinct countercase, derivation, or implementation check.

Next attempts: Change signal accuracy and rederive the segment; test nonlinear utility; remove randomization and compare the deterministic optimum; add observation expiry and cost timing; test a three-signal response map; compare against an independently implemented exact LP solver.
