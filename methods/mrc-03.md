Intended mind change: Let a concrete mathematical surprise change which question is pursued next, then use the resulting structure to answer a different orbit question.

Actual starting judgment: “A circular neighbor-XOR rule is a compact object I can inspect without guessing a reader's tastes. I have not computed its five-cell orbit; a finite cycle or extinction is expected, but its actual structure is unresolved.” The judgment and seed were frozen in `systems-handoff-inputs-before.json` before the first run.

Actor and scope: The systems workers perform an actual finite mathematical exploration and use its saved results in this session. “Surprise” below means a newly exposed feature not specified in the frozen judgment, not a claim about a felt emotional response. Human interest, enjoyment, retention, and future behavior are unobserved.

Original source: `systems-handoff-mrc.original.md`, with requirements preserved separately in `systems-handoff-mrc.requirements.txt`. Reader emissions, hashes, and before-continuation reload evidence are in `systems-handoff-reload-integrity.json`. MRC defines no numerical 8x floor and imposes no subordinate invocation here. The full execution includes all three questions, a changed inquiry after the first result, complete five-cell state classification, a proof of the structural reduction, three later queries, and a changed-width countercase. The original is not replaced by eight headings.

The input is a ring of five bits. All cells update simultaneously by `next[i] = current[i] XOR current[(i+1) mod 5]`. The first seed is `10000`. The synchronous rule and ring boundary are essential premises.

## What is being achieved?

Surface operation: follow the seed's orbit. Immediate goal: find the actual behavior of this finite rule. Upstream goal: pursue a mathematically specified object into a question not already answered by the input. Within this exercise, exploration itself is the chosen activity; it need not be renamed preparation for a human productivity intervention.

There are only 32 states. Determinism therefore guarantees eventual repetition, but this cardinality fact does not determine the period or extinction behavior. The goal cannot be completed merely by restating eventual repetition. It requires the actual orbit and whatever further question that result makes productive.

## Is this the best method?

| Candidate | Actual result it can supply | Limitation for the present question |
|---|---|---|
| Iterate the selected seed and stop at its first repeated state | Exact transient and period for `10000` | Leaves other seeds unresolved |
| Enumerate all 32 starting states immediately | Complete finite classification | More work than the single initial orbit needs |
| Derive algebraic properties of the map | Kernel, image, and restrictions on cycles | Those restrictions alone do not identify the nonzero cycle length |
| Change the rule or width before evaluating the seed | A different mathematical object | Does not answer the frozen input |

The selected first operation is direct iteration of the supplied seed, with a visited-state map. The strongest argument against it is that state enumeration can become mere listing. Here the stopping condition is a repeated state, so the first pass has an exact useful endpoint. Algebra is reserved for a question that the first result actually leaves open.

`systems-handoff-mrc-03-first.json` records:

`10000 → 10001 → 10010 → 10111 → 11000 → 01001 → 11011 → 01100 → 10100 → 11101 → 00110 → 01010 → 11110 → 00011 → 00101 → 01111 → 10001`.

The first state is outside the eventual cycle; the next fifteen are distinct and the update of `01111` is `10001`. The transient is one step and the period is fifteen.

## Is progress occurring, and what changes next?

The result settles the seed's orbit and exposes a specific new question: why does a one-step transient feed a cycle containing exactly fifteen states? Decision: stop extending the same trace; return to the goal question and examine the entire image of the update. The new target is the structure relating this seed to the other 31 states.

Let T be the stipulated update and let ⊕ denote XOR. XORing all five output bits gives `(x0⊕x1)⊕(x1⊕x2)⊕…⊕(x4⊕x0)=0`, because each input appears twice. Every output has even parity. This follows from the exact rule; it is not evidence that arbitrary cellular rules preserve this property.

If T(x)=0, then every adjacent pair is equal. Around the ring all five bits are equal, so the kernel contains exactly `00000` and `11111`. Since T is linear under XOR, T(x)=T(y) exactly when x⊕y is one of those two kernel states. Every output thus has two complementary preimages, and the image has 32/2=16 states. There are exactly sixteen even-parity five-bit states, so the image equals that set E.

The nonzero kernel state `11111` has odd parity. Consequently the restriction of T to E has trivial kernel and is one-to-one. Because E is finite, this restriction permutes E. Zero is fixed. The observed fifteen-cycle consists of nonzero even-parity states, so it contains every other member of E. This closes the proposed structural question without guessing a general period theorem.

The complete 32-seed calculation in `systems-handoff-mrc-03-products.json` agrees with the derivation:

| Class | Count | Behavior |
|---|---:|---|
| `00000` | 1 | Fixed zero |
| `11111` | 1 | Reaches zero in one step |
| Nonzero even-parity states | 15 | Already on the single fifteen-cycle |
| Other odd-parity states | 15 | Reach that cycle in one step |

These counts exhaust the 32-state input space. They are complete finite coverage, not thirty-two independent beneficial findings.

Claim C1: Every nonzero five-bit seed reaches the fifteen-cycle. Assume C1 right: `11111` must eventually enter it. Direct updating gives `11111 → 00000 → 00000`, contradicting C1. The derived alternative is that every seed except the two constant seeds reaches the fifteen-cycle. The table and the kernel argument establish this alternative. Its strongest remaining boundary is a change in width or update semantics, which is outside the claimed five-cell synchronous map.

Claim C2: After the first step, the five-cell evolution is reversible on E. Assume C2 right: an even state has a unique even predecessor. The kernel calculation shows that its two full-space predecessors are complements; with five cells, exactly one has even parity. Thus the needed unique predecessor exists. The apparent contrary example—two complementary states having the same output—does not falsify C2 because one predecessor is outside E. It does falsify reversibility on the full 32-state space, which is not claimed.

Decision after the complete classification: stop searching these 32 states for additional cycle types. A seed of period five cannot exist in this state space because every state lies in one of the four exhausted classes. A different width is a different branch, not more evidence required for this finite answer.

## Later use and organization comparison

The saved transient/cycle map was read in a later invocation, which answered new time queries without extending each orbit step by step. For a saved orbit with transient t and period p, an index n beyond the stored prefix maps to `t + ((n-t) mod p)`.

| Later input | Reduction actually used | Answer |
|---|---|---|
| `10000`, time 1,000,000 | `1 + ((1,000,000−1) mod 15) = 10` | `00110` |
| `11111`, time 1,000,000 | Transient 1, period 1, index 1 | `00000` |
| `01100`, time 19 | Transient 0, period 15, index 4 | `01010` |

These exact outputs appear in `systems-handoff-later-use-results.json`. The zero exception is actually consumed, not left as unused prose.

The later changed-width branch uses four cells with seed `1000`: `1000 → 1001 → 1010 → 1111 → 0000 → 0000`. The transient is four and the period one. This directly rejects the stronger cross-width assertion that a single-one seed must reach a fifteen-cycle. It leaves the exact five-cell classification intact.

| Organization | Later million-step query | Exception handling | Selected use |
|---|---|---|---|
| Raw first-seed chronological trace | Requires recognizing and applying repetition | Says nothing about other seeds by itself | Retained as first-pass evidence |
| Transient/cycle map plus parity classification | Supplies the index formula and seed class | Separates zero and all-ones seeds | Used for all three later queries |
| Parity statement alone | Excludes odd outputs after one step | Does not supply period or exact phase | Retained as proof support, insufficient as the sole query view |

The selected map serves exact future-state questions; the trace serves audit; the parity derivation accounts for the coverage. No measured wall-time advantage, generalized mathematical expertise, or human enjoyment is claimed.

Verdict certificate: The exact five-cell map has one nonzero fifteen-cycle, a zero fixed point, and the specified one-step feeders. The first orbit, kernel/image derivation, and complete finite enumeration jointly establish that claim. The all-ones countercase is retained in the classification, and the width-four countercase defeats only the cross-width generalization. The later consumer uses the resulting structure to produce exact large-index answers and retain both boundaries. This is a new useful mathematical representation within this case, not another credit for the generic instruction to change representations.

Actual mind change: The working inquiry changed from following one seed to classifying the update's image; the resulting model now distinguishes its cycle, transient states, and constant-state exception. That model was used for three different time queries.

Benefit: The actual later queries have exact answers obtained from the newly established cycle structure, including an exception that a single-seed extrapolation would miss. The benefit is confined to this model's mathematical exploration and local reuse.

Verdict: KEEP

Organization: The transient/cycle map with its parity proof is selected for orbit queries, while the original trace and all-seed outputs preserve provenance. The width condition stays attached to every reuse.

Next attempts: Classify an even-width ring without importing the odd-width proof; replace XOR with another specified operation; test asynchronous updates as a new rule; ask an actual reader whether this exploration is interesting before making any claim about human interest.
