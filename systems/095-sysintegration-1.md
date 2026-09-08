Intended mind change: Change a whole-system acceptance decision by actually combining producer inputs and control conditions.

# Integrate action packet boundaries

Starting judgment: Separately valid producer fields look promising, but their combination has not yet been tested against authority, revision and environment conditions.

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-sysintegration.md`; current requirements are retained separately in `../sources/systems-sysintegration.requirements.txt`.

Depth: Original 8x floors: 21 components, 25 integration steps, 50 executed integration tests, 20 issue scenarios; rollback and dependency order are specified.

Integration goal: twenty distinct producer responsibilities supply one coherent present action packet to a commitment consumer. These are implemented validation rules in `build_interfaces.py`, not a production service fleet. Producer maturity is constructed-fixture; consumer maturity is locally executed. Root is the actual integration owner. External human data remains unavailable and cannot be replaced by fixtures in a real action.

Strategy comparison: big-bang input obscures which producer is absent; bottom-up validates fields but can miss cross-field inconsistency; top-down stubs ease interface discovery but do not prove real values; incremental plus risk-first whole-packet checks is selected. The first twenty steps integrate one field responsibility at a time, then five steps test combined constraints. Dependencies are an acyclic prefix; field checks can be evaluated independently but final acceptance depends on all producers.

Twenty-five integration steps:

| Step | Components | Predecessor | Tests | Rollback |
|---|---|---|---|---|
| S1-01 | goal, acceptance | None | IT1-01, IT1-02 | restore preceding fixture and accepted state |
| S1-02 | actor, acceptance | S1-01 | IT1-03, IT1-04 | restore preceding fixture and accepted state |
| S1-03 | object, acceptance | S1-02 | IT1-05, IT1-06 | restore preceding fixture and accepted state |
| S1-04 | time_horizon, acceptance | S1-03 | IT1-07, IT1-08 | restore preceding fixture and accepted state |
| S1-05 | constraints, acceptance | S1-04 | IT1-09, IT1-10 | restore preceding fixture and accepted state |
| S1-06 | interpretation, acceptance | S1-05 | IT1-11, IT1-12 | restore preceding fixture and accepted state |
| S1-07 | source_version, acceptance | S1-06 | IT1-13, IT1-14 | restore preceding fixture and accepted state |
| S1-08 | units, acceptance | S1-07 | IT1-15, IT1-16 | restore preceding fixture and accepted state |
| S1-09 | options, acceptance | S1-08 | IT1-17, IT1-18 | restore preceding fixture and accepted state |
| S1-10 | evidence_scope, acceptance | S1-09 | IT1-19, IT1-20 | restore preceding fixture and accepted state |
| S1-11 | budget, acceptance | S1-10 | IT1-21, IT1-22 | restore preceding fixture and accepted state |
| S1-12 | prerequisites, acceptance | S1-11 | IT1-23, IT1-24 | restore preceding fixture and accepted state |
| S1-13 | criteria_version, acceptance | S1-12 | IT1-25, IT1-26 | restore preceding fixture and accepted state |
| S1-14 | authority, acceptance | S1-13 | IT1-27, IT1-28 | restore preceding fixture and accepted state |
| S1-15 | target_revision, acceptance | S1-14 | IT1-29, IT1-30 | restore preceding fixture and accepted state |
| S1-16 | output_contract, acceptance | S1-15 | IT1-31, IT1-32 | restore preceding fixture and accepted state |
| S1-17 | endpoint, acceptance | S1-16 | IT1-33, IT1-34 | restore preceding fixture and accepted state |
| S1-18 | status, acceptance | S1-17 | IT1-35, IT1-36 | restore preceding fixture and accepted state |
| S1-19 | consequence, acceptance | S1-18 | IT1-37, IT1-38 | restore preceding fixture and accepted state |
| S1-20 | baseline, acceptance | S1-19 | IT1-39, IT1-40 | restore preceding fixture and accepted state |
| S1-21 | combined interface check, acceptance | S1-20 | IT1-41, IT1-42 | restore preceding fixture and accepted state |
| S1-22 | combined interface check, acceptance | S1-21 | IT1-43, IT1-44 | restore preceding fixture and accepted state |
| S1-23 | combined interface check, acceptance | S1-22 | IT1-45, IT1-46 | restore preceding fixture and accepted state |
| S1-24 | combined interface check, acceptance | S1-23 | IT1-47, IT1-48 | restore preceding fixture and accepted state |
| S1-25 | combined interface check, acceptance | S1-24 | IT1-49, IT1-50 | restore preceding fixture and accepted state |

Fifty executed cross-component cases:

| Test | Input→consumer stimulus | Expected acceptance | Actual acceptance | Result |
|---|---|---|---|---|
| IT1-01 | missing goal | False | False | PASS |
| IT1-02 | null goal | False | False | PASS |
| IT1-03 | missing actor | False | False | PASS |
| IT1-04 | null actor | False | False | PASS |
| IT1-05 | missing object | False | False | PASS |
| IT1-06 | null object | False | False | PASS |
| IT1-07 | missing time_horizon | False | False | PASS |
| IT1-08 | null time_horizon | False | False | PASS |
| IT1-09 | missing constraints | False | False | PASS |
| IT1-10 | null constraints | False | False | PASS |
| IT1-11 | missing interpretation | False | False | PASS |
| IT1-12 | null interpretation | False | False | PASS |
| IT1-13 | missing source_version | False | False | PASS |
| IT1-14 | null source_version | False | False | PASS |
| IT1-15 | missing units | False | False | PASS |
| IT1-16 | null units | False | False | PASS |
| IT1-17 | missing options | False | False | PASS |
| IT1-18 | null options | False | False | PASS |
| IT1-19 | missing evidence_scope | False | False | PASS |
| IT1-20 | null evidence_scope | False | False | PASS |
| IT1-21 | missing budget | False | False | PASS |
| IT1-22 | null budget | False | False | PASS |
| IT1-23 | missing prerequisites | False | False | PASS |
| IT1-24 | null prerequisites | False | False | PASS |
| IT1-25 | missing criteria_version | False | False | PASS |
| IT1-26 | null criteria_version | False | False | PASS |
| IT1-27 | missing authority | False | False | PASS |
| IT1-28 | null authority | False | False | PASS |
| IT1-29 | missing target_revision | False | False | PASS |
| IT1-30 | null target_revision | False | False | PASS |
| IT1-31 | missing output_contract | False | False | PASS |
| IT1-32 | null output_contract | False | False | PASS |
| IT1-33 | missing endpoint | False | False | PASS |
| IT1-34 | null endpoint | False | False | PASS |
| IT1-35 | missing status | False | False | PASS |
| IT1-36 | null status | False | False | PASS |
| IT1-37 | missing consequence | False | False | PASS |
| IT1-38 | null consequence | False | False | PASS |
| IT1-39 | missing baseline | False | False | PASS |
| IT1-40 | null baseline | False | False | PASS |
| IT1-41 | valid | True | True | PASS |
| IT1-42 | wrong schema | False | False | PASS |
| IT1-43 | other schema | False | False | PASS |
| IT1-44 | stale | False | False | PASS |
| IT1-45 | future unknown | False | False | PASS |
| IT1-46 | execution not authorized | False | False | PASS |
| IT1-47 | empty authority | False | False | PASS |
| IT1-48 | over budget | False | False | PASS |
| IT1-49 | budget boundary | True | True | PASS |
| IT1-50 | zero cost | True | True | PASS |

Each case starts with a complete fixture, changes one producer or combined condition, sends the whole packet to acceptance, and compares the returned decision. This tests end-to-end input propagation and error behavior, not semantic truth of field contents. The twenty issue scenarios are missing/null values for each producer; all have owner, blocker severity, detection and supplied-input recovery in the artifact. No production MTTR or schedule performance is invented.

Environment: local Python and JSON fixtures are available; no network is required; staging and production environments are not present. Test monitoring is the result log. Primary risk is fixture fidelity: a contract-valid packet can contain an unsupported claim. Timing requirement is completed producers before acceptance; no measured latency guarantee exists. Shared-state contention is avoided in the fixture by copied packets, not proven absent for a real concurrent host.

Actual changed operation: a producer with all labels present but unauthorized execute action is refused at the integrated authority boundary; the description action is accepted under the same input fields.

All 50 expected decisions are executed and the actual count is 50/50. This is a finite contract result. Semantic usefulness, human benefit and future reliability remain unresolved.

Actual mind change: Whole-packet acceptance now rejects the declared conflicting cross-component cases.

Benefit: Fifty local integration cases per target distinguish missing data and boundary conflicts; no production claim follows.

Verdict: KEEP

Organization: The sequence plus cross-field tests preserves dependencies absent from a field-by-field success list.

Next attempts: Add semantic truth checks; test concurrent writers; compare a partially available packet policy.
