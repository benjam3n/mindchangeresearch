Intended mind change: Choose the next observation from the structure of what is unknown rather than from a confidence number alone.

# GOSM 06 — Equal belief can require different evidence

Starting working judgment: I have not yet resolved which query is useful in two contexts that share P(x=1)=1/2. The current confidence value alone supplies no distinction between them.

Actor and scope: Finite constructed case; primary assistant working state. The numerical worlds and utilities below are stipulated inputs. They are not measurements of this user or human psychology. No training-weight change is claimed.

Original procedure: GOSM, source ../sources/root-gosm.md, SHA-256 4224530e1b14958cd0e2921a173c4772406f7673fa561ee8c27dac548e362f4b. Original reader requirements are preserved separately. Context: NORMAL urgency, LOW immediate experimental stakes with broader design relevance, INTERMEDIATE topic familiarity, CHEAP reversible computation, RICH information inside the declared case and SPARSE information about external transfer. Variant: Explore. The source defines no numerical 8x floor; this record expands the actual variant through the displayed distinctions, complete finite comparisons, countercases, and a later application. It does not claim an invented 8x certification.

The underlying question is what a belief summary leaves out about the way further evidence will change it.

Input: truth x is binary; a source's inversion bit r is binary; its report A=x XOR r. Context K1 has observed A=0 but does not know r, leaving worlds (x,r)=(0,0),(1,1). Context K2 knows r=0 but has not observed A, leaving (0,0),(1,0). Each context assigns equal probability to its two worlds. The available unit-cost queries are “read A” and “calibrate r.” Queries are exact and can be repeated, but a repeated query returns the same bit.

| Context | P(x=1) | Classes after reading A | Classes after calibrating r | Possible (x,r) |
| --- | --- | --- | --- | --- |
| observed_A0_unknown_r | 1/2 | 1 | 2 | [[0, 0], [1, 1]] |
| known_r0_unobserved_A | 1/2 | 2 | 1 | [[0, 0], [1, 0]] |

In K1, reading A again returns 0 in both worlds, so x remains unresolved. Calibrating r distinguishes the worlds: r=0 implies x=0 and r=1 implies x=1. In K2, calibrating r again returns 0 in both worlds, while reading A reveals x directly. The useful first queries are therefore opposite even though their current truth probabilities agree.

The distinctions are uncertainty about the world versus uncertainty about an observation process; an unobserved value versus a observed but ambiguous value; a posterior over x versus a joint state over x,r; confidence sufficient for a fixed action versus information sufficient to select an experiment; a new report versus a repeated report; evidence acquisition versus source calibration; identical marginal distributions versus different conditional dependencies; and an informative operation versus an operation that merely consumes effort.

Position: selecting the next cognitive operation requires enough of the uncertainty structure to predict how candidate observations separate live possibilities. P(x=1) is insufficient for that selection in this exact case.

The strongest counter is a fixed immediate action whose payoff depends only on x, with no further query allowed. Then the two contexts yield the same expected payoff for every such action; retaining r adds no decision value for that restricted problem. This boundary preserves the usefulness of compact probabilities when they are sufficient for the actual operation.

The tension is that a compressed belief can be completely adequate for deciding now and inadequate for deciding how to learn. A “more accurate probability” objective alone does not select the right next query if both start at the same probability.

Later application: increase the calibration cost to 3 while leaving the report cost at 1 and allowing both. In K1, a report costs less but never resolves x; calibration still supplies the answer at cost 3. In K2, reading A resolves x at cost 1 and calibration is redundant. Under a budget of 2, K1 must preserve unresolved x while K2 can resolve it. I used the joint-state representation to distinguish an affordable answer from an affordable but useless repetition.

Specific next action: when the next attempt concerns uncertainty, identify at least one pair of live worlds and compare what each available observation returns in those worlds. Stop at the actual information boundary rather than treating repeated text as new evidence. Open threads: noisy calibration, uncertain query cost, multiple relevant truths and emotional responses to ambiguity remain outside this calculation.

Actual mind change: My working query choice now differs between K1 and K2 despite identical marginal confidence. The same representation produced different budget-feasible outcomes in the later case.

Benefit: It avoids an uninformative one-unit repetition in K1 and a redundant calibration in K2. This is an exact information-selection improvement within the declared model, not a measured effect on human uncertainty.

Verdict: KEEP — distinct finite evidence-selection result with a cost boundary.

Organization: Keep the marginal belief for fixed immediate action and the joint possibilities for inquiry selection. Replacing either with the other everywhere adds needless complexity or loses necessary structure; the view is selected by the later operation.

Next attempts: Add a noisy source while retaining known calibration; compare confidence changes caused by representation alone; test motivation that changes the willingness to pay for the informative query.
