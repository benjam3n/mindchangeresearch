# TRACEMATRIX 8x prospective application — proposal-to-query ledger

Intended mind change: Replace my judgment that an accepted/rejected proposal log is enough for audit with the judgment that every later ledger answer must be traceable backward to a frozen need, field requirement, merge control, and executed result.

Actual starting judgment: The COL decision log appeared sufficient because it preserved each proposal. I had not yet tested whether a later query could distinguish an accepted current field, a retained base field, a rejected proposal, and a field blocked by missing provenance.

Concrete frozen input: X proposes `r1.criterion:C0→C1`; Y proposes `r1.outcome:O0→O1` explicitly under `C0` and `r2.provenance:P2a→P2b`; Z proposes `r3.status:COMPLETE→PARTIAL` because required external evidence is missing. The changed-order and missing-provenance uses were fixed before execution. Interpretation 1 applies: build a matrix from scratch. Requested depth is 8x.

## Traceability architecture

Level 1 — NEED (`N`): fixed reason the candidate exists  
↓ `derived-from`  
Level 2 — REQUIREMENT (`R`): field or query obligation  
↓ `satisfied-by`  
Level 3 — DESIGN CONTROL (`D`): merge/trace mechanism  
↓ `implemented-by`  
Level 4 — IMPLEMENTATION/DECISION (`I`): concrete accepted, rejected, retained, or gate artifact  
↓ `verified-by`  
Level 5 — TEST/RESULT (`T`): executed order, omission, or later-query result

Additional link types: `depends-on` for semantic bases, `conflicts-with` for `PY1` versus `PX`, and `refines` for field-specific requirements. Seven link types are used: derived-from, satisfied-by, implemented-by, verified-by, depends-on, conflicts-with, refines.

## Item registry — exactly 100 distinct traced items

### Needs (10)

| ID | Need |
|---|---|
| N01 | Prevent a later-arriving field from silently winning |
| N02 | Prevent a new criterion from inheriting an old-criterion outcome |
| N03 | Preserve valid r2 provenance |
| N04 | Preserve r3's missing-evidence gate |
| N05 | Make proposal order irrelevant |
| N06 | Make missing provenance visible |
| N07 | Retain rejected proposals for audit |
| N08 | Answer later ledger queries from decisions rather than prose |
| N09 | Limit claims to constructed artifacts |
| N10 | Permit the smallest valid independent subset to proceed |

### Requirements (25)

| ID | Requirement |
|---|---|
| R01 | Freeze base record hash |
| R02 | Freeze proposal hashes |
| R03 | Record target field |
| R04 | Record proposed base value |
| R05 | Record proposed new value |
| R06 | Record semantic basis |
| R07 | Record provenance receipt |
| R08 | Compare base value to frozen base |
| R09 | Build field dependency graph |
| R10 | Detect criterion/outcome basis conflict |
| R11 | Accept independent valid criterion update |
| R12 | Reject incompatible outcome update |
| R13 | Label retained outcome as unevaluated under C1 |
| R14 | Accept r2 provenance only with receipt |
| R15 | Retain P2a when P2b receipt is missing |
| R16 | Reduce r3 status when required evidence is missing |
| R17 | Retain exact r3 evidence gate |
| R18 | Produce deterministic field dispositions |
| R19 | Test all six X/Y/Z orders |
| R20 | Test missing-provenance variant |
| R21 | Preserve rejected values in audit view only |
| R22 | Exclude rejected values from current-record view |
| R23 | Trace later query answers backward through five levels |
| R24 | Report gaps without manufacturing links |
| R25 | Mark the scope as artifact-only |

### Design controls (25)

| ID | Control |
|---|---|
| D01 | content-addressed base manifest |
| D02 | content-addressed proposal envelope |
| D03 | target-field schema |
| D04 | compare-and-set base check |
| D05 | explicit value payload |
| D06 | semantic-basis array |
| D07 | resolvable receipt field |
| D08 | base mismatch quarantine |
| D09 | dependency graph builder |
| D10 | basis compatibility comparator |
| D11 | criterion-only acceptance rule |
| D12 | dependent-outcome rejection rule |
| D13 | retained-value qualification rule |
| D14 | provenance-resolution rule |
| D15 | provenance fallback/gap rule |
| D16 | evidence-completeness status rule |
| D17 | evidence-gate persistence rule |
| D18 | canonical decision sorter/hash |
| D19 | six-permutation fixture |
| D20 | receipt-omission fixture |
| D21 | immutable rejection register |
| D22 | filtered current-record view |
| D23 | bidirectional query index |
| D24 | orphan/gold-plate/coverage scanner |
| D25 | claim-scope annotation |

### Implementation and decision artifacts (20)

| ID | Artifact/result |
|---|---|
| I01 | frozen base manifest `B0` |
| I02 | proposal envelope `PX` |
| I03 | proposal envelope `PY1` |
| I04 | proposal envelope `PY2` |
| I05 | proposal envelope `PZ` |
| I06 | dependency edge `r1.outcome→r1.criterion` |
| I07 | dependency edge `r3.status→r3.evidence` |
| I08 | decision `PX=ACCEPT` |
| I09 | decision `PY1=REJECT_BASIS_CONFLICT` |
| I10 | retained `r1.outcome=O0; not_evaluated_under:C1` |
| I11 | decision `PY2=ACCEPT` in complete-input run |
| I12 | current `r2.provenance=P2b` in complete-input run |
| I13 | decision `PZ=ACCEPT` |
| I14 | current `r3.status=PARTIAL` |
| I15 | gate `r3.evidence=E3-missing_external_evidence` |
| I16 | canonical complete-input candidate SHA-256 `d0c4acc94776542aa460092d6611d3d4d0087b0b460e89305ff384fff6b967d5` |
| I17 | missing-provenance decision `PY2=REJECT_MISSING_RECEIPT` |
| I18 | missing-provenance retained `r2.provenance=P2a` |
| I19 | gap artifact `G-PROV` |
| I20 | immutable rejected-proposal audit view |

### Tests and later-query results (20)

| ID | Executed check/result |
|---|---|
| T01 | order XYZ → `d0c4…67d5`, PASS |
| T02 | order XZY → `d0c4…67d5`, PASS |
| T03 | order YXZ → `d0c4…67d5`, PASS |
| T04 | order YZX → `d0c4…67d5`, PASS |
| T05 | order ZXY → `d0c4…67d5`, PASS |
| T06 | order ZYX → `d0c4…67d5`, PASS |
| T07 | query current r1 criterion → C1/PX/I08, PASS |
| T08 | query current r1 outcome → O0 qualified/I10, PASS |
| T09 | query rejected r1 proposals → O1@C0/PY1/I09, PASS |
| T10 | query current r2 provenance full run → P2b/PY2/I12, PASS |
| T11 | query current r3 status → PARTIAL/PZ/I14, PASS |
| T12 | query r3 gate → E3-missing/I15, PASS |
| T13 | omit PY2 receipt → I17+I18+I19, PASS |
| T14 | query current r2 provenance omission run → P2a/I18, PASS |
| T15 | query missing receipt → G-PROV/I19, PASS |
| T16 | query current view excludes O1 → none/I09, PASS |
| T17 | query audit view retains O1 → O1@C0/I20, PASS |
| T18 | query scope → constructed artifact only/D25, PASS |
| T19 | query smallest valid subset in omission run → PX+PZ accepted, PASS |
| T20 | backward trace T08→I10→D13→R13→N02, PASS |

Counts: 10 needs + 25 requirements + 25 controls + 20 implementation/decision artifacts + 20 tests = **100 distinct traced items**, five levels, seven link types.

## Forward traceability matrix

| Need | Requirement | Design | Implementation | Verification | Status |
|---|---|---|---|---|---|
| N01 | R01 | D01 | I01 | T01–T06 | COMPLETE |
| N01 | R02 | D02 | I02–I05 | T01–T06 | COMPLETE |
| N01 | R03 | D03 | I02–I05 | T07–T12 | COMPLETE |
| N01 | R04 | D04 | I08,I09,I11,I13 | T01–T06 | COMPLETE |
| N01 | R05 | D05 | I08–I15 | T07–T12 | COMPLETE |
| N02 | R06 | D06 | I03,I06 | T08,T09,T20 | COMPLETE |
| N03 | R07 | D07 | I04,I11,I17 | T10,T13–T15 | COMPLETE |
| N01 | R08 | D08 | I08,I09,I11,I13 | T01–T06 | COMPLETE |
| N02 | R09 | D09 | I06,I07 | T08,T11,T20 | COMPLETE |
| N02 | R10 | D10 | I09 | T08,T09,T16,T17 | COMPLETE |
| N02 | R11 | D11 | I08 | T07,T19 | COMPLETE |
| N02 | R12 | D12 | I09 | T09,T16,T17 | COMPLETE |
| N02 | R13 | D13 | I10 | T08,T20 | COMPLETE |
| N03 | R14 | D14 | I11,I12 | T10 | COMPLETE |
| N06 | R15 | D15 | I17–I19 | T13–T15,T19 | COMPLETE |
| N04 | R16 | D16 | I13,I14 | T11 | COMPLETE |
| N04 | R17 | D17 | I15 | T12 | COMPLETE |
| N05 | R18 | D18 | I16 | T01–T06 | COMPLETE |
| N05 | R19 | D19 | I16 | T01–T06 | COMPLETE |
| N06 | R20 | D20 | I17–I19 | T13–T15,T19 | COMPLETE |
| N07 | R21 | D21 | I20 | T09,T17 | COMPLETE |
| N08 | R22 | D22 | I08,I10,I12,I14,I15 | T07,T08,T10–T12,T16 | COMPLETE |
| N08 | R23 | D23 | I08–I20 | T07–T20 | COMPLETE |
| N10 | R24 | D24 | I19 | T13,T15,T19 | COMPLETE |
| N09 | R25 | D25 | scope annotation | T18 | COMPLETE |

Refinement links: R10 refines R09 for criterion/outcome edges; R14 and R15 refine R07 for present/absent receipts; R16 and R17 refine R09 for evidence/status edges; R19 and R20 refine R18 for order and omission determinism. Dependency links: R12 depends on R10; R13 depends on R12; R15 depends on R07; R16 depends on R17. Conflict link: PY1/I03 conflicts with PX/I02 at the candidate semantic-basis layer.

## Backward traceability matrices

### Tests → needs

| Test | Verifies implementation | Design | Requirement | Need | Status |
|---|---|---|---|---|---|
| T01 | I16 | D18,D19 | R18,R19 | N05 | LINKED |
| T02 | I16 | D18,D19 | R18,R19 | N05 | LINKED |
| T03 | I16 | D18,D19 | R18,R19 | N05 | LINKED |
| T04 | I16 | D18,D19 | R18,R19 | N05 | LINKED |
| T05 | I16 | D18,D19 | R18,R19 | N05 | LINKED |
| T06 | I16 | D18,D19 | R18,R19 | N05 | LINKED |
| T07 | I08 | D11,D23 | R11,R23 | N02,N08 | LINKED |
| T08 | I10 | D13,D23 | R13,R23 | N02,N08 | LINKED |
| T09 | I09,I20 | D12,D21,D23 | R12,R21,R23 | N02,N07,N08 | LINKED |
| T10 | I12 | D14,D23 | R14,R23 | N03,N08 | LINKED |
| T11 | I14 | D16,D23 | R16,R23 | N04,N08 | LINKED |
| T12 | I15 | D17,D23 | R17,R23 | N04,N08 | LINKED |
| T13 | I17–I19 | D20 | R20 | N06 | LINKED |
| T14 | I18 | D15,D23 | R15,R23 | N06,N08 | LINKED |
| T15 | I19 | D15,D23,D24 | R15,R23,R24 | N06,N08,N10 | LINKED |
| T16 | I09 | D22,D23 | R22,R23 | N08 | LINKED |
| T17 | I20 | D21,D23 | R21,R23 | N07,N08 | LINKED |
| T18 | scope annotation | D25 | R25 | N09 | LINKED |
| T19 | I08,I13,I17 | D15,D20 | R15,R20,R24 | N06,N10 | LINKED |
| T20 | I10 | D13,D23 | R13,R23 | N02,N08 | LINKED |

### Implementation → needs

| Implementation | Design | Requirement | Need | Status |
|---|---|---|---|---|
| I01 | D01 | R01 | N01 | LINKED |
| I02 | D02,D03,D05,D06 | R02,R03,R05,R06 | N01,N02 | LINKED |
| I03 | D02,D03,D05,D06 | R02,R03,R05,R06 | N01,N02 | LINKED |
| I04 | D02,D03,D05,D07 | R02,R03,R05,R07 | N01,N03 | LINKED |
| I05 | D02,D03,D05,D06 | R02,R03,R05,R06 | N01,N04 | LINKED |
| I06 | D09 | R09 | N02 | LINKED |
| I07 | D09 | R09 | N04 | LINKED |
| I08 | D11 | R11 | N02 | LINKED |
| I09 | D10,D12 | R10,R12 | N02 | LINKED |
| I10 | D13 | R13 | N02 | LINKED |
| I11 | D14 | R14 | N03 | LINKED |
| I12 | D14 | R14 | N03 | LINKED |
| I13 | D16 | R16 | N04 | LINKED |
| I14 | D16 | R16 | N04 | LINKED |
| I15 | D17 | R17 | N04 | LINKED |
| I16 | D18,D19 | R18,R19 | N05 | LINKED |
| I17 | D15,D20 | R15,R20 | N06 | LINKED |
| I18 | D15 | R15 | N06 | LINKED |
| I19 | D15,D24 | R15,R24 | N06,N10 | LINKED |
| I20 | D21 | R21 | N07 | LINKED |

No design or implementation item is untraced. `scope annotation` is a deliberate non-code implementation artifact and is not gold-plating.

## Twelve gap checks

| Gap check | Result | Evidence/disposition |
|---|---|---|
| G01 need without requirement | 0 | all N01–N10 have ≥1 R link |
| G02 requirement without need | 0 | all R01–R25 appear forward |
| G03 requirement without design | 0 | all R01–R25 have D links |
| G04 design without requirement | 0 | all D01–D25 appear forward |
| G05 design without implementation | 0 | all controls have an artifact, decision, fixture, index, scanner, or annotation |
| G06 implementation without design | 0 | all I01–I20 appear backward |
| G07 requirement without test | 0 | all R01–R25 are covered directly or through linked fixture/query results |
| G08 test without requirement | 0 | all T01–T20 appear backward |
| G09 accepted dependent field with stale basis | 0 | PY1 is rejected; O0 is qualified rather than relabeled |
| G10 current provenance without receipt | 0 full run; 1 proposed mutation in omission run | PY2 rejected in omission run; P2a retained; G-PROV open |
| G11 complete status with missing required evidence | 0 | r3 reduced to PARTIAL and gate retained |
| G12 order-dependent candidate hash | 0 | six orders produce H-full |

The one omission-run gap is an intentionally exposed missing link, not silently closed traceability.

## Coverage report

| Metric | Target | Actual | Status |
|---|---:|---:|---|
| Needs → requirements | 100% | 10/10 = 100% | PASS |
| Requirements → design | 100% | 25/25 = 100% | PASS |
| Design → implementation/decision | 100% | 25/25 = 100% | PASS |
| Requirements → tests/results | 100% | 25/25 = 100% | PASS |
| Tests/results → requirements | 100% | 20/20 = 100% | PASS |
| MUST obligations fully traced | 100% | 25/25 = 100% | PASS |

Complete-input traceability health is GREEN. The missing-provenance variant is YELLOW by design: the missing receipt is reported and the proposed mutation is not current.

## Report 1 — executive summary

10 needs, 25 requirements, 25 design controls, 20 implementation/decision artifacts, and 20 executed test/query results are traced across five levels. All 100 items have upward and downward links. The complete-input candidate passes six order tests. The omission variant preserves the prior provenance and emits one open receipt gap. Overall: GREEN for the complete-input candidate; YELLOW for the intentionally incomplete variant.

## Report 2 — gap report

| Gap ID | Type | Item | Missing link | Priority | Owner | Disposition |
|---|---|---|---|---|---|---|
| G-PROV | missing receipt | PY2 in omission variant | no resolvable evidence for P2b | HIGH | provenance proposer role | retain P2a; block PY2 until receipt exists |

No orphan need, requirement, design, implementation item, or test exists. No additional requirement should be created merely to turn the omission variant green.

## Report 3 — requirement traces

`R12 Reject incompatible outcome update` ← N02 → D12 → I09 (`PY1=REJECT_BASIS_CONFLICT`) → T09/T16/T17 PASS.  
`R14 Accept r2 provenance only with receipt` ← N03 → D14 → I11/I12 → T10 PASS.  
`R15 Retain P2a when P2b receipt is missing` ← N06 → D15 → I17/I18/I19 → T13/T14/T15 PASS.  
`R16 Reduce r3 status when evidence is missing` ← N04 → D16 → I13/I14 → T11 PASS.  
`R23 Trace later query answers backward` ← N08 → D23 → I08–I20 → T07–T20 PASS.

## Report 4 — change impact

Changing `r1.criterion` affects D09/D10, I06/I08/I09/I10, and queries T07–T09/T16/T17/T20; it does not affect r2 or r3 fields. Adding a recomputed `r1.outcome@C1` would reopen R10–R13 and require new verification without altering the historical PY1 rejection. Removing `PY2`'s receipt affects R07/R14/R15/R20/R24, I11/I12/I17–I19, and T10/T13–T15/T19. Supplying r3 external evidence would reopen R16/R17, I13–I15, and T11/T12; until then, the gate and PARTIAL status remain.

## Required prospective uses

Changed order: T01–T06 all returned `d0c4acc94776542aa460092d6611d3d4d0087b0b460e89305ff384fff6b967d5`. Forward traces remained identical, and backward query T08 still reached the qualified O0 path. The order change therefore altered neither acceptance nor traceability.

Missing provenance: T13–T15 and T19 returned omission candidate `ef5ccc0f6e397526166b3b2bc869efa1c327a125fdb1c10ac222ca51c2d73300`. The matrix exposed `G-PROV`, rejected PY2, retained P2a, preserved PX and PZ, and gave the later query an exact backward route rather than an inferred answer.

Actual mind change: Yes. A proposal log records what was considered; a trace matrix establishes why a later answer is current, retained, rejected, or gated. I now distinguish those functions and require the second for integration-sensitive queries.

Benefit or harm: Beneficial in this finite artifact case. The matrix caught no new semantic conflict beyond COL, but it prevented the missing-provenance variant from becoming an untraceable blank or an invented P2b value. Cost: 100-item 8x tracing is inefficient for the routine three-record case; its justified use is audit/high-impact change, while ordinary reuse should query the compact index it generated.

Verdict: KEEP for audit-sensitive tool coordination; reject a universal requirement to build a fresh 8x matrix for every small merge.

Content assessment: All original 8x floors are met without claiming global reliability: 100 distinct items, five levels, twelve gap checks, four reports, and seven link types. The execution covers six proposal orders and one missing-receipt variant. It does not cover cyclic dependencies, receipt authenticity, or a newly recomputed C1 outcome.

Organization assessment: The full registry precedes the forward/backward matrices so ID meanings are fixed before links. Gap and coverage reports follow both directions, and compact audience reports follow the evidence. For later reuse, the best organization is the bidirectional query index, not rereading this report.

Next attempts: inject a forged but syntactically resolvable receipt; add a valid `O2@C1` and check historical rejection retention; trace a two-record atomic transaction; create a cycle in the dependency graph and test explicit non-resolution; compare compact incremental tracing against full rebuild on the same change set.
