# COL prospective application — semantic merge protocol

Intended mind change: Replace my working assumption that proposal updates can be merged field-by-field after schema validation with the judgment that acceptance must also preserve the semantic basis under which each proposed field was produced.

Actual starting judgment: I expected version tags plus deterministic ordering to prevent most coordination errors. I had not yet tested whether a syntactically valid outcome computed under an old criterion could be silently attached to a new criterion.

Concrete frozen input: X changes `r1.criterion`; Y changes `r1.outcome` under the old criterion and `r2.provenance`; Z changes `r3.status` because external evidence is missing. The fixed success criterion is to prevent incompatible `r1` fields, retain `r2` provenance, retain `r3`'s evidence gate, and survive changed proposal order and missing provenance. These are constructed agent proposals; no claim about a human team is in scope.

## Goal

GOAL: Produce one deterministic candidate record set in which every accepted field remains valid under the criterion, evidence, and provenance versions on which it depends.

TIMELINE: One prospective cycle; freeze proposals before merging, run all six proposal orders, and emit accepted/rejected field decisions before any common-ledger integration.

CONSTRAINTS: Immutable base records; field-level proposals; no last-write-wins; missing provenance cannot be manufactured; external evidence cannot be inferred; X, Y, and Z are constructed agent roles; only artifact state is evaluated.

SUCCESS LOOKS LIKE: Every order yields the same candidate: `r1.criterion=C1`, `r1.outcome=O0` with Y's `O1@C0` rejected as basis-incompatible, `r2.provenance=P2b` when supplied, and `r3.status=PARTIAL` with gate `E3=missing_external_evidence`.

## Frozen records and proposals

| Object | Frozen value |
|---|---|
| `r1` | `{criterion:C0, outcome:O0, provenance:P1a}` |
| `r2` | `{criterion:C2, outcome:O2, provenance:P2a}` |
| `r3` | `{criterion:C3, outcome:O3, status:COMPLETE, evidence:E3-missing}` |
| X | `PX={target:r1.criterion, value:C1, base:C0, basis:[schema-v1]}` |
| Y1 | `PY1={target:r1.outcome, value:O1, base:O0, basis:[criterion:C0]}` |
| Y2 | `PY2={target:r2.provenance, value:P2b, base:P2a, basis:[receipt:Y-P2b]}` |
| Z | `PZ={target:r3.status, value:PARTIAL, base:COMPLETE, basis:[evidence:E3-missing]}` |

`C1` means that an outcome is eligible for `KEEP` only if changed-order and missing-provenance tests pass. `O1` was calculated under `C0`; it contains no judgment under `C1`. `P2b` identifies the new source receipt. `E3-missing` is an explicit absence, not evidence for completion.

## Roles

| Role | Responsible for | Decision rights | Key deliverable |
|---|---|---|---|
| X / criterion proposer | Specify the proposed criterion and its base version | May propose; may not accept its own proposal | `PX` with semantic basis |
| Y / result and provenance proposer | Specify the outcome basis and provenance receipt | May propose; may not relabel `O1@C0` as `O1@C1` | `PY1`, `PY2` |
| Z / evidence-gate proposer | Report status consequence of missing external evidence | May reduce completion status; may not invent evidence | `PZ` |
| Merge evaluator | Compare targets, bases, and semantic dependencies | Accepts independent fields; quarantines incompatible dependent fields | field decision log |
| Test evaluator | Execute order and omission fixtures | Determines whether candidate passes each frozen test | immutable test results |
| Integrator | Decide whether candidate is eligible for later ledger use | May integrate only a test-passing candidate | candidate manifest |

RACI: proposers are Responsible for proposals; merge evaluator is Accountable for field decisions; test evaluator is Responsible for fixtures; integrator is Accountable for eligibility; the other roles are Consulted through immutable artifacts and Informed through the decision log.

## Communication design

| Type | Frequency | Who | Format | Purpose |
|---|---|---|---|---|
| Proposal submission | Once per frozen proposal | X/Y/Z → merge evaluator | immutable JSON object | Preserve target, base, value, basis, and receipt |
| Conflict review | Once per collision or dependency change | merge evaluator + affected proposal artifacts | asynchronous decision record | Determine compatibility without relying on arrival order |
| Test review | Once after candidate construction | test evaluator → integrator | fixture/result table | Check six orders and the missing-provenance variant |
| Integration notice | Once per candidate | integrator → ledger query layer | candidate manifest | Expose only accepted fields and unresolved gates |

DEFAULT CHANNEL: content-addressed proposal and decision artifacts.

ESCALATION PATH: unresolved semantic compatibility → quarantine the affected field and retain the last verified base value; unresolved evidence → reduce status or preserve `UNRESOLVED`; never resolve either through arrival order.

Every touchpoint above changes an artifact or disposition; no recurring meeting is introduced.

## Decision map

| Decision type | Who decides | Must consult | Tiebreaker |
|---|---|---|---|
| Proposal well-formedness | Merge evaluator | proposal schema | Invalid proposal is rejected |
| Base-version match | Merge evaluator | frozen record | Mismatch quarantines field |
| Semantic-basis compatibility | Merge evaluator | dependency graph and proposal basis | Preserve verified base value |
| Missing-evidence status | Merge evaluator | evidence registry | Incomplete evidence forbids `COMPLETE` |
| Test result | Test evaluator | immutable fixture | Exact expected/actual comparison |
| Integration eligibility | Integrator | all required tests | Any failed required test blocks integration |

DEFAULT RULE: An unlisted decision is made by the integrator only if it cannot alter a proposal, evidence claim, or test result; otherwise it is returned to the relevant evaluator.

## Merge operation

1. Freeze the base hash and all proposal hashes.
2. Normalize proposal order only for evaluation, not acceptance.
3. Check each proposal's target, base value, evidence/provenance receipt, and explicit semantic basis.
4. Build a dependency graph. Here `r1.outcome → r1.criterion`; `r2.provenance` is independent of `r1`; `r3.status → r3.evidence`.
5. Accept a criterion update only as a criterion update. It invalidates no old outcome by itself, but marks every dependent outcome as requiring either an unchanged-basis certificate or recomputation.
6. Reject `PY1`: `O1` asserts evaluation under `C0`, while the candidate criterion is `C1`; attaching it would create a record no proposer supplied.
7. Retain `O0` only as the prior outcome, labeled `not_evaluated_under:C1`; do not call it a C1 result.
8. Accept `PY2` only when `receipt:Y-P2b` is present and resolves to `P2b`; otherwise retain `P2a` and emit `G-PROV`.
9. Accept `PZ`: missing external evidence is inconsistent with `COMPLETE`; set `PARTIAL`, retain `E3-missing`, and expose the exact gate.
10. Emit field decisions independently of arrival order, then run all required fixtures.

## Handoffs

1. X/Y/Z → merge evaluator: proposal objects.
   - FORMAT: immutable objects containing `proposal_id,target,base,value,basis,receipt`.
   - DEFINITION OF DONE: all supplied fields are explicit; absence is represented as absence.
   - ACCEPTANCE: evaluator records hash and schema result.
2. Merge evaluator → test evaluator: candidate plus decision log.
   - FORMAT: candidate JSON and one disposition per proposed field.
   - DEFINITION OF DONE: no field lacks a basis disposition; retained base values are labeled as retained.
   - ACCEPTANCE: test evaluator reproduces candidate hash from the proposal set.
3. Test evaluator → integrator: order/omission results.
   - FORMAT: expected/actual/hash/gate table.
   - DEFINITION OF DONE: six permutations and missing-provenance fixture executed.
   - ACCEPTANCE: integrator verifies all required fixture IDs and hashes.
4. Integrator → later ledger queries: eligible candidate view.
   - FORMAT: queryable field-to-decision trace references.
   - DEFINITION OF DONE: rejected proposals remain visible; no rejected value appears as current.
   - ACCEPTANCE: changed-order, provenance, status-gate, and conflict queries return fixed answers.

## Prospective uses

### Use 1 — changed order

Orders `XYZ`, `XZY`, `YXZ`, `YZX`, `ZXY`, and `ZYX` all produced the same dispositions: `PX=ACCEPT`, `PY1=REJECT_BASIS_CONFLICT`, `PY2=ACCEPT`, `PZ=ACCEPT`. Canonical key-sorted JSON for every order produced SHA-256 `d0c4acc94776542aa460092d6611d3d4d0087b0b460e89305ff384fff6b967d5`; arrival order never selected a winner. This passed the frozen changed-order criterion.

### Use 2 — missing provenance

The `Y2` variant omitted `receipt:Y-P2b`. It produced SHA-256 `ef5ccc0f6e397526166b3b2bc869efa1c327a125fdb1c10ac222ca51c2d73300`, rejected only `PY2`, retained `r2.provenance=P2a`, emitted `G-PROV`, and left the independently valid `PX` and `PZ` decisions unchanged. It did not erase provenance, infer `P2b`, or reject all of Y's distinct fields. This passed the frozen missing-provenance criterion.

## Accountability

- CHECK-IN CADENCE: once after candidate construction and once after any dependency-changing proposal.
- LEADING INDICATOR: count of proposed dependent fields whose semantic basis equals the candidate dependency version; target 100% among accepted dependent fields.
- FAILURE SIGNAL: different proposal orders yield different candidate hashes; a current field lacks provenance; a `COMPLETE` status points to missing required evidence; or a rejected value appears in a later query.
- ADJUSTMENT RULE: quarantine the smallest affected field set, retain the verified base, reopen only the failed dependency/test, and rerun all order fixtures before integration.

Actual mind change: Yes. Version matching alone is insufficient. I now judge semantic dependency compatibility to be a separate merge condition: two individually valid field edits can compose into a record that nobody proposed and no criterion evaluated.

Benefit or harm: Beneficial within the constructed artifact case. The protocol prevented the exact silent `C1 + O1@C0` combination, preserved valid independent changes, and made the evidence gate queryable. It adds decision metadata and test cost; for independent fields that cost can be bypassed after a dependency check.

Verdict: KEEP — a demonstrated tools/coordination change in model working state and artifact behavior, not evidence about human collaboration.

Content assessment: The record contains every original COL product and two prospective uses. The strongest result is field-level semantic conflict detection. The weakest boundary is that no simultaneous mutually dependent multi-record transaction was tested.

Organization assessment: The order `goal → roles → communication → decisions → handoffs → operation → uses → accountability` made the protocol executable while retaining the original COL structure. The merge operation is placed after decision rights because it instantiates them; the tests follow handoffs because they test the transferred candidate.

Next attempts: test mutually dependent edits spanning two records; test concurrent criterion rollback plus outcome recomputation; test two valid provenance receipts with incompatible scopes; compare quarantine-smallest-field against quarantine-whole-transaction; run the protocol with a deliberately cyclic dependency graph.
