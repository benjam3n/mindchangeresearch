# DIFR — equal feature counts, different decision compositions

Intended mind change: Replace my count-based comparison of the three locations with a differentiation that identifies which exact feature compositions change the decision under two prospectively fixed queries.

Actual starting judgment: Because L1, L2, and L3 each reveal two properties, I expected their information yield to be equal unless an external value judgment was added. I had not separated equal quantity from query-complete composition.

Concrete input: The prospectively frozen locations are L1={surface crack, serial identity}, L2={surface crack, internal void}, and L3={internal void, serial identity}. Queries alternate from structural safety to chain of custody. Before comparing, structural completion was fixed as `{surface crack, internal void}` and custody completion as `{internal void, serial identity}`. No human observer, perception report, or behavioral outcome exists.

Prospective boundary: The observation matrix, query order, completion predicates, and selection rule were fixed before classification. Selection rule: choose a location containing both current-query features; if none does, choose the greatest predicate overlap and then the lowest label.

Source fidelity: Original `difr` stdout SHA-256 `fe682b61e708658424de624ef735e41e012675f74e1cd5c93afb4186304bb4e8`; current-requirements stderr is preserved separately. The original source contains no numerical 8x rule. Every original step, output-summary field, and failure-mode check is executed at expanded scope; no 8x certification is claimed.

## 1. Items and comparison context

ITEM A: L1 = {surface crack, serial identity}

ITEM B: L2 = {surface crack, internal void}

ADDITIONAL ITEM: L3 = {internal void, serial identity}

COMPARISON CONTEXT: Select one inspection location for structural safety, then make a later selection after the decision query changes to chain of custody. The comparison must identify factual differences before judging relevance.

## 2. Similarities

1. Every location reveals exactly two properties — DIMENSION: output quantity.
2. Every location omits exactly one of the three possible properties — DIMENSION: incompleteness.
3. Every property appears at exactly two locations — DIMENSION: property frequency.
4. Every pair of locations shares exactly one property — DIMENSION: pairwise overlap.
5. Every pair differs by one property substitution — DIMENSION: set distance.
6. No location contains a property outside `{surface crack, internal void, serial identity}` — DIMENSION: observation vocabulary.
7. No access cost, latency, reliability, or human-response difference is supplied — DIMENSION: evidential boundary.

## 3. Differences

1. Surface-crack availability
   - L1 IS: present.
   - L2 IS: present.
   - L3 IS: absent.
   - DIMENSION: surface structural evidence.
2. Internal-void availability
   - L1 IS: absent.
   - L2 IS: present.
   - L3 IS: present.
   - DIMENSION: internal structural evidence and the fixed custody predicate.
3. Serial-identity availability
   - L1 IS: present.
   - L2 IS: absent.
   - L3 IS: present.
   - DIMENSION: identity evidence.
4. Structural-predicate completion
   - L1 IS: one of two required features.
   - L2 IS: two of two required features.
   - L3 IS: one of two required features.
   - DIMENSION: structural query sufficiency.
5. Custody-predicate completion
   - L1 IS: one of two required features.
   - L2 IS: one of two required features.
   - L3 IS: two of two required features.
   - DIMENSION: custody query sufficiency.
6. Property omitted
   - L1 IS: omits internal void.
   - L2 IS: omits serial identity.
   - L3 IS: omits surface crack.
   - DIMENSION: missing evidence.

“L2 is better” and “L3 is better” are excluded as differences; they are context-indexed judgments derived below.

## 4. Classification

| Difference | Structural-safety level | Chain-of-custody level | Basis |
|---|---|---|---|
| Surface-crack availability | significant | trivial | It changes structural predicate overlap but not the fixed custody predicate. |
| Internal-void availability | significant | significant | It is a member of both fixed predicates. |
| Serial-identity availability | trivial | significant | It is absent from the structural predicate and present in the custody predicate. |
| Structural-predicate completion | significant | trivial | It determines the first decision and is not the second decision's target. |
| Custody-predicate completion | trivial | significant | It determines the second decision and is not the first decision's target. |
| Omitted property | significant | significant | Which property is absent determines whether the current predicate can be completed. |

No observed difference is fundamental: changing one observed property would not make L1, L2, or L3 cease to be an inspection location. No cosmetic feature was supplied. “Trivial” here means decision-irrelevant within the named context, not absent or universally unimportant.

## 5. Contextual relevance

CONTEXT A: structural safety.

DIFFERENCES THAT MATTER:

1. L2 contains both surface crack and internal void — WHY IT MATTERS: it alone completes the structural predicate. WEIGHT: high.
2. L1 lacks internal void — WHY IT MATTERS: it cannot complete the structural predicate. WEIGHT: high.
3. L3 lacks surface crack — WHY IT MATTERS: it cannot complete the structural predicate. WEIGHT: high.

DIFFERENCES THAT DO NOT MATTER:

1. Serial identity — WHY IRRELEVANT: it is not a member of the fixed structural predicate.
2. Equal output count — WHY IRRELEVANT: two features at every site creates a three-way tie and cannot select a site.

CONTEXT B: chain of custody.

DIFFERENCES THAT MATTER:

1. L3 contains both internal void and serial identity — WHY IT MATTERS: it alone completes the custody predicate. WEIGHT: high.
2. L1 lacks internal void — WHY IT MATTERS: identity alone cannot complete the custody predicate. WEIGHT: high.
3. L2 lacks serial identity — WHY IT MATTERS: void alone cannot complete the custody predicate. WEIGHT: high.

DIFFERENCES THAT DO NOT MATTER:

1. Surface crack — WHY IRRELEVANT: it is not a member of the fixed custody predicate.
2. Equal output count — WHY IRRELEVANT: the tie in quantity persists while composition determines completion.

## Output summary

DIFFERENTIATION ANALYSIS

COMPARING: L1 vs L2 vs L3.

CONTEXT: Current structural selection followed by a changed custody selection.

SHARED: two observed properties, one omitted property, one property shared by every pair, equal set size, equal pairwise set distance, and no supplied cost or reliability difference.

KEY DIFFERENCES, ranked by relevance:

1. Query-predicate completion — L2 alone completes structural safety; L3 alone completes chain of custody.
2. Identity of the omitted property — L2 omits identity; L3 omits crack; L1 omits void.
3. Individual property availability — crack changes only structural relevance, identity changes only custody relevance, and void changes both.

FUNDAMENTAL DIFFERENCES: none in the supplied case.

TRIVIAL DIFFERENCES: serial identity under the structural query; surface crack under the custody query; equal output count under both because it cannot discriminate.

BOTTOM LINE: Equal information quantity does not produce equal decision value; feature composition selects L2 for structural safety and L3 for chain of custody.

## Distinct later use

The first selection was executed under the structural context: L2, with two-of-two predicate coverage. The query was then changed to chain of custody while the observations and selection rule remained fixed. The classifications were re-indexed by the new context: surface crack moved from significant to trivial, serial identity moved from trivial to significant, internal void remained significant, and the selection changed to L3. L1 was not selected merely because it also had serial identity; its missing internal void left it at one-of-two custody coverage.

## Failure-mode audit

- Similarities precede differences and expose the misleading equal-count symmetry.
- Zero differences are labeled fundamental.
- Every relevance judgment names either structural safety or chain of custody.
- No “better” judgment is presented as a factual difference.
- Each absence is recorded explicitly, including L2's missing identity and L3's missing crack.

## Closing assessment

Actual mind change: My comparison changed from “all three locations yield two features, so they are informationally equal” to “their quantities are equal but their compositions complete different predicates; structural selection is L2 and later custody selection is L3.”

Benefit or harm: Beneficial within the frozen case. The differentiation discarded a non-discriminating count and changed the later location selection without changing the evidence. Harm was limited to added table length; a production selector could compress the result to predicate coverage after this derivation is retained.

Verdict: **KEEP** as a prospective model-side differentiation and later-use result. The exact composition-over-count result is new within this case; the broader claim that differences depend on context overlaps prior work and receives no duplicate novelty credit.

Performative check: Not performative. A formerly decisive-seeming equality became irrelevant, two difference classifications changed when the query changed, and the selected location changed from L2 to L3. No claim is made about human sight, attention, belief, memory, or action.

Content assessment: Complete for three deterministic locations and the two fixed predicates. It does not establish weights for real structural damage, the evidential validity of serial numbers or voids, sensor accuracy, or chain-of-custody law.

Organization assessment: Similarities establish the symmetry before precise differences break it; one classification table retains both contexts; the later use follows the summary so it is visibly uptake rather than a restatement of the procedure.

Next attempts: Hold composition fixed and vary sensor reliability; hold query fixed and add unequal travel cost; compare feature count with expected decision loss over noisy observations; add a fourth location that completes neither predicate but maximizes novelty; reverse the query order and test whether inspection history adds a different selection criterion.
