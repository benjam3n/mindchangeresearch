Intended mind change: Find whether a broader method search adds a useful way to compare instruction versions.

Actual starting judgment: MD-01 already distinguishes wording, observed precedence and declared prerequisites; this method map must add more than that established separation.

Original: ../sources/methods-foht.original.md. Separate requirements receipt: ../sources/methods-foht.requirements.txt.

Depth: Original 8x floors met: 15 methods, 12 tested, 15 prerequisites, 159 numbered findings. All tests and surviving-method edges are actual products below.

Corruption check: no praise or audience agreement is used as evidence. Verdicts distinguish viable, conditional, eliminated and blocked; the user's desired program does not make every method effective. Findings are scoped to exact constructed records.

INPUT: A gather→connect→select→power→check→start; B gather→power→connect→select→check→start, with gather wording changed; B2 gather→connect→select→power→start→check. Explicit rule: start requires a current successful check. No physical cable/power rule is supplied.

H1 [criterion/constraint] MUST identify the exact A/B descriptive reorder.
H2 [criterion/constraint] MUST flag B2’s declared check-before-start violation.
H3 [criterion/constraint] MUST not infer unspecified device causality.
H4 [criterion/constraint] SHOULD retain wording changes for lexical queries.
H5 [criterion/constraint] CONSTRAINT actor is the local symbolic comparison.
H6 [criterion/constraint] CONSTRAINT preserve criterion and source version; no expert or human effects are observed.
H7 [method] Word diff; discovery source: direct.
H8 [prerequisite] H7: exact A/B labels available.
H9 [method] Position-by-position action comparison; discovery source: direct.
H10 [prerequisite] H9: both six-action sequences available.
H11 [method] Bag-of-actions comparison; discovery source: direct.
H12 [prerequisite] H11: action names available.
H13 [method] Typed relation projection; discovery source: category.
H14 [prerequisite] H13: lexical, precedence and declared-prerequisite classes available.
H15 [method] Counterexample construction; discovery source: inversion.
H16 [prerequisite] H15: one declared prerequisite available.
H17 [method] Replay the original state-machine audit; discovery source: adjacent success.
H18 [prerequisite] H17: SVS-02 exact transition table available.
H19 [method] Treat comparison as a query family; discovery source: reframe.
H20 [prerequisite] H19: three requested answer types separable.
H21 [method] Decompose inventory/order/outcome; discovery source: decomposition.
H22 [prerequisite] H21: actions, ordering and check outcome rule supplied.
H23 [method] Topological sorting of declared prerequisites; discovery source: cross-domain.
H24 [prerequisite] H23: check-before-start edge available.
H25 [method] Enumerate all six-action permutations; discovery source: search.
H26 [prerequisite] H25: six distinct symbolic action names available.
H27 [method] Minimize edit count; discovery source: optimization.
H28 [prerequisite] H27: A/B token sequence available.
H29 [method] Replay outcome traces; discovery source: simulation.
H30 [prerequisite] H29: symbolic pass/fail outcomes available.
H31 [method] Inspect device specification; discovery source: external evidence.
H32 [prerequisite] H31: no device/manual supplied.
H33 [method] Run a physical power-order trial; discovery source: physical experiment.
H34 [prerequisite] H33: no device or experiment performed.
H35 [method] Ask an expert to certify both versions; discovery source: social evidence.
H36 [prerequisite] H35: no expert response available.
H37 [AR consequence] H7: Finds gather wording and moved power.
H38 [AR further implication] H7: A reviewer can locate every supplied lexical edit.
H39 [foreclosed] H7: Does not assign causal significance to word count.
H40 [AW countercase] H7: Synonym-only gather edit changes text without changing action identity.
H41 [AW consequence/bedrock] H7: A large lexical edit need not violate check-before-start.
H42 [AW second countercase] H7: A single moved start in B2 violates the declared prerequisite.
H43 [AW second consequence/bedrock] H7: Small edit size can be consequential.
H44 [derived alternative] H7: Keep words, then test declared relations.
H45 [edge/cost] H7: Long labels can dominate the visible diff although order is unchanged.
H46 [verdict] H7 CONDITIONAL; AR H37,H38; AW H40–H43; prerequisite H8; alternative H44; edge H45.
H47 [AR consequence] H9: B differs at positions 2–4.
H48 [AR further implication] H9: It bounds where order changed in the exact sequence.
H49 [foreclosed] H9: Does not tell whether connect/power has a physical dependency.
H50 [AW countercase] H9: An inserted harmless annotation shifts every later position.
H51 [AW consequence/bedrock] H9: Position mismatch overstates action-order change when item alignment is lost.
H52 [AW second countercase] H9: Same positions can contain paraphrased actions with different semantics.
H53 [AW second consequence/bedrock] H9: Index equality alone is not action identity.
H54 [derived alternative] H9: Align action identities before comparing positions.
H55 [edge/cost] H9: Repeated action names make alignment ambiguous.
H56 [verdict] H9 CONDITIONAL; AR H47,H48; AW H50–H53; prerequisite H10; alternative H54; edge H55.
H57 [AR consequence] H11: A and B contain the same actions.
H58 [AR further implication] H11: No action was added or removed in this input.
H59 [foreclosed] H11: Order information is discarded.
H60 [AW countercase] H11: B2 has the same bag but starts before check.
H61 [AW consequence/bedrock] H11: The mandatory condition is violated despite bag equality.
H62 [AW second countercase] H11: Duplicating check changes multiplicity but may still omit a successful check.
H63 [AW second consequence/bedrock] H11: A count does not establish event outcome.
H64 [derived alternative] H11: Use bag only to detect inventory changes, then validate order/outcome.
H65 [edge/cost] H11: Cannot answer sequencing or causality.
H66 [verdict] H11 ELIMINATED; AR H57,H58; AW H60–H63; prerequisite H12; alternative H64; edge H65.
H67 [AR consequence] H13: B changes two precedence pairs while preserving check-before-start.
H68 [AR further implication] H13: It produces a bounded answer without inventing device physics.
H69 [foreclosed] H13: Undeclared physical validity remains unanswered.
H70 [AW countercase] H13: If connect-before-power is later supplied as mandatory, B becomes invalid.
H71 [AW consequence/bedrock] H13: The result depends on the rule set; current unresolved status is not safe-device certification.
H72 [AW second countercase] H13: If a paraphrase changes action identity, retained identity mapping may be false.
H73 [AW second consequence/bedrock] H13: The projection must preserve source wording to revisit mapping.
H74 [derived alternative] H13: Store exact text plus typed relations and rule version.
H75 [edge/cost] H13: At larger scale relation count grows quadratically; retain relevant predicate queries.
H76 [verdict] H13 VIABLE; AR H67,H68; AW H70–H73; prerequisite H14; alternative H74; edge H75.
H77 [AR consequence] H15: B2 demonstrates start-before-check failure.
H78 [AR further implication] H15: A validator accepting B2 is incomplete for the stated condition.
H79 [foreclosed] H15: A counterexample rejects a claim; it does not certify every remaining instruction.
H80 [AW countercase] H15: A physical cable/power failure cannot be constructed as fact from absent specifications.
H81 [AW consequence/bedrock] H15: A hypothetical device rule would change the supplied case.
H82 [AW second countercase] H15: Passing B2 detection alone can coexist with mishandling stale successful checks.
H83 [AW second consequence/bedrock] H15: One test is not complete input-domain validation.
H84 [derived alternative] H15: Use a declared-rule counterexample and preserve untested conditions.
H85 [edge/cost] H15: Counterexamples cost additional distinct fixtures.
H86 [verdict] H15 VIABLE; AR H77,H78; AW H80–H83; prerequisite H16; alternative H84; edge H85.
H87 [AR consequence] H17: The original table exposes check PASS→start and FAIL→connect.
H88 [AR further implication] H17: The same explicit event requirement can validate B2.
H89 [foreclosed] H17: It does not prove a new sequence is physically valid.
H90 [AW countercase] H17: Replaying an old successful setup after setup change uses a stale result.
H91 [AW consequence/bedrock] H17: A successful historical check is not a successful current check.
H92 [AW second countercase] H17: Unreadable input was absent from the old domain.
H93 [AW second consequence/bedrock] H17: An old two-value validation cannot certify a new three-value process.
H94 [derived alternative] H17: Replay only unchanged declared domains; invoke PV for new observations.
H95 [edge/cost] H17: Version drift makes unqualified replay unreliable.
H96 [verdict] H17 CONDITIONAL; AR H87,H88; AW H90–H93; prerequisite H18; alternative H94; edge H95.
H97 [AR consequence] H19: “What changed?” and “what violates a rule?” return different outputs.
H98 [AR further implication] H19: The user can obtain both without collapsing one into the other.
H99 [foreclosed] H19: No single scalar edit score is produced.
H100 [AW countercase] H19: A shortest report dropping lexical changes cannot answer exact wording questions.
H101 [AW consequence/bedrock] H19: Compression changes the answer family if its contract is unstated.
H102 [AW second countercase] H19: A report listing all words may still omit the only violated dependency.
H103 [AW second consequence/bedrock] H19: More text does not guarantee requested relation coverage.
H104 [derived alternative] H19: Declare answer types, then include the required projection for each.
H105 [edge/cost] H19: Several views require maintained links to a common source.
H106 [verdict] H19 VIABLE; AR H97,H98; AW H100–H103; prerequisite H20; alternative H104; edge H105.
H107 [AR consequence] H21: Inventory equality, precedence change and PASS requirement are checked separately.
H108 [AR further implication] H21: Each failed subclaim has a specific witness.
H109 [foreclosed] H21: A single undifferentiated validity verdict is withheld.
H110 [AW countercase] H21: Conjoining checks from different versions can validate a nonexistent combined state.
H111 [AW consequence/bedrock] H21: All checks must refer to the same exact version.
H112 [AW second countercase] H21: A check step’s presence is weaker than check success.
H113 [AW second consequence/bedrock] H21: Output event must be inspected where the rule names its value.
H114 [derived alternative] H21: Use same-version source plus actual outcome domain.
H115 [edge/cost] H21: More granular checks need explicit join keys.
H116 [verdict] H21 VIABLE; AR H107,H108; AW H110–H113; prerequisite H22; alternative H114; edge H115.
H117 [AR consequence] H23: Both A and B satisfy the one edge; B2 does not.
H118 [AR further implication] H23: Every returned topological order satisfies that declared edge.
H119 [foreclosed] H23: It makes no claim about unconstrained actions.
H120 [AW countercase] H23: Treating every A precedence as mandatory rejects B by definition.
H121 [AW consequence/bedrock] H23: A descriptive original order was silently promoted to a requirement.
H122 [AW second countercase] H23: Dropping the successful-result condition treats any check as enough.
H123 [AW second consequence/bedrock] H23: A plain action graph needs an event condition.
H124 [derived alternative] H23: Use typed conditional prerequisite, not all observed edges.
H125 [edge/cost] H23: A graph can be correct but too weak for device certification.
H126 [verdict] H23 VIABLE; AR H117,H118; AW H120–H123; prerequisite H24; alternative H124; edge H125.
H127 [AR consequence] H25: The order space has 720 permutations; half place check before start.
H128 [AR further implication] H25: It can exhaust the single precedence predicate.
H129 [foreclosed] H25: It cannot exhaust unspecified physical behaviors.
H130 [AW countercase] H25: Calling all 360 order-valid permutations safe invents device semantics.
H131 [AW consequence/bedrock] H25: Formal coverage is relative to the declared rule.
H132 [AW second countercase] H25: Check fail still appears before start in some invalid outcome traces.
H133 [AW second consequence/bedrock] H25: Permutation-only modeling omits outcomes.
H134 [derived alternative] H25: Enumerate order and outcome separately if both matter.
H135 [edge/cost] H25: 720 cases are unnecessary for the three concrete comparisons.
H136 [verdict] H25 CONDITIONAL; AR H127,H128; AW H130–H133; prerequisite H26; alternative H134; edge H135.
H137 [AR consequence] H27: Counts a compact explanation of the reorder.
H138 [AR further implication] H27: Can help a reader navigate the supplied difference.
H139 [foreclosed] H27: Does not optimize validity or physical safety.
H140 [AW countercase] H27: A one-action start move can violate a mandatory rule.
H141 [AW consequence/bedrock] H27: Minimum edit count is not minimum consequence.
H142 [AW second countercase] H27: A large benign wording rewrite has high distance.
H143 [AW second consequence/bedrock] H27: Distance alone reverses meaningful priorities.
H144 [derived alternative] H27: Use edit count only after consequence classes are preserved.
H145 [edge/cost] H27: Metric choice changes rankings without changing dependencies.
H146 [verdict] H27 ELIMINATED; AR H137,H138; AW H140–H143; prerequisite H28; alternative H144; edge H145.
H147 [AR consequence] H29: A successful check permits start; failure returns to connect in the original model.
H148 [AR further implication] H29: B2 attempting start before an observed pass can be rejected.
H149 [foreclosed] H29: No real setup behavior is learned.
H150 [AW countercase] H29: A simulator that assumes all checks pass hides the failure branch.
H151 [AW consequence/bedrock] H29: It would certify a policy under a substituted observation distribution.
H152 [AW second countercase] H29: A simulator without unreadable omits the new PV input domain.
H153 [AW second consequence/bedrock] H29: Trace completeness depends on declared event types.
H154 [derived alternative] H29: Enumerate relevant outcomes including absence where supplied.
H155 [edge/cost] H29: State explosion grows with repeated retries; use invariants for loops.
H156 [verdict] H29 VIABLE; AR H147,H148; AW H150–H153; prerequisite H30; alternative H154; edge H155.
H157 [blocked finding] H31: The physical connect/power rule cannot be verified from this input; retain unresolved.
H158 [blocked finding] H33: No actual physical outcome is available; symbolic traces are not a substitute.
H159 [blocked finding] H35: A drafted request does not establish the missing dependency; continue formal checks only.

METHOD REGISTRY INDEX (all discovery, prerequisites, tests and edges are preserved above):

| Method finding | Name | Verdict | Prerequisite | Verdict evidence |
| --- | --- | --- | --- | --- |
| H7 | Word diff | CONDITIONAL | H8 | H46 |
| H9 | Position-by-position action comparison | CONDITIONAL | H10 | H56 |
| H11 | Bag-of-actions comparison | ELIMINATED | H12 | H66 |
| H13 | Typed relation projection | VIABLE | H14 | H76 |
| H15 | Counterexample construction | VIABLE | H16 | H86 |
| H17 | Replay the original state-machine audit | CONDITIONAL | H18 | H96 |
| H19 | Treat comparison as a query family | VIABLE | H20 | H106 |
| H21 | Decompose inventory/order/outcome | VIABLE | H22 | H116 |
| H23 | Topological sorting of declared prerequisites | VIABLE | H24 | H126 |
| H25 | Enumerate all six-action permutations | CONDITIONAL | H26 | H136 |
| H27 | Minimize edit count | ELIMINATED | H28 | H146 |
| H29 | Replay outcome traces | VIABLE | H30 | H156 |
| H31 | Inspect device specification | BLOCKED | H32 | H157 |
| H33 | Run a physical power-order trial | BLOCKED | H34 | H158 |
| H35 | Ask an expert to certify both versions | BLOCKED | H36 | H159 |

Totals: 15 methods found before testing; 15 prerequisites surfaced (12 met for symbolic testing, 3 absent); 12 methods tested, each with AR, further implication, foreclosure, two distinct AW countercases with consequences, an alternative derived from those countercases, and explicit edge/cost; 159 numbered findings. The registry contains every exploration product; it is not a substituted summary of absent analysis.

SYNTHESIS (only from registry and supplied input): Typed relation projection, decomposition and conditional dependency checking survive. Word/position/replay/permutation methods are conditional. Bag equality and minimum edit count fail as complete validators. Physical evidence paths are blocked. The surviving recommendation is the same MD-01 operation; no additional optimum or physical-safety claim follows. First action: reuse instruction-difference-observations.json; unresolved item: real device rules.

Actual later application: On A2, only “Gather materials” becomes “Collect materials” and the action sequence stays A. The typed relation comparison returns a lexical edit and zero precedence changes. Both the ordinary MD-01 method and expanded search agree; no extra benefit credit.

Actual mind change: No new operation beyond MD-01 is warranted; the map confirms its scoped comparison and preserves unavailable physical evidence.

Benefit: The larger search supplies explicit alternatives and countercases, but does not improve the earlier concrete A/B/B2 decisions. Additional benefit is rejected.

Verdict: REJECT

Organization: The exact input, result and conditional method index are the retrieval surface; the numbered registry retains countercases and provenance. No claim of universal optimal organization.

Next attempts: Apply the surviving method on a different input; test the explicit boundary; retain an unresolved result when prerequisites are absent.
