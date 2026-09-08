Intended mind change: Change a whole-system acceptance decision by actually combining producer inputs and control conditions.

# Integrate retention packet boundaries

Starting judgment: Separately valid producer fields look promising, but their combination has not yet been tested against authority, revision and environment conditions.

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-sysintegration.md`; current requirements are retained separately in `../sources/systems-sysintegration.requirements.txt`.

Depth: Original 8x floors: 21 components, 25 integration steps, 50 executed integration tests, 20 issue scenarios; rollback and dependency order are specified.

Integration goal: twenty distinct producer responsibilities supply one coherent retained-result packet to a commitment consumer. These are implemented validation rules in `build_interfaces.py`, not a production service fleet. Producer maturity is constructed-fixture; consumer maturity is locally executed. Root is the actual integration owner. External human data remains unavailable and cannot be replaced by fixtures in a real action.

Strategy comparison: big-bang input obscures which producer is absent; bottom-up validates fields but can miss cross-field inconsistency; top-down stubs ease interface discovery but do not prove real values; incremental plus risk-first whole-packet checks is selected. The first twenty steps integrate one field responsibility at a time, then five steps test combined constraints. Dependencies are an acyclic prefix; field checks can be evaluated independently but final acceptance depends on all producers.

Twenty-five integration steps:

| Step | Components | Predecessor | Tests | Rollback |
|---|---|---|---|---|
| S2-01 | result_id, acceptance | None | IT2-01, IT2-02 | restore preceding fixture and accepted state |
| S2-02 | creation_context, acceptance | S2-01 | IT2-03, IT2-04 | restore preceding fixture and accepted state |
| S2-03 | actor_type, acceptance | S2-02 | IT2-05, IT2-06 | restore preceding fixture and accepted state |
| S2-04 | original_goal, acceptance | S2-03 | IT2-07, IT2-08 | restore preceding fixture and accepted state |
| S2-05 | source_edition, acceptance | S2-04 | IT2-09, IT2-10 | restore preceding fixture and accepted state |
| S2-06 | helped_condition, acceptance | S2-05 | IT2-11, IT2-12 | restore preceding fixture and accepted state |
| S2-07 | negative_case, acceptance | S2-06 | IT2-13, IT2-14 | restore preceding fixture and accepted state |
| S2-08 | evidence_kind, acceptance | S2-07 | IT2-15, IT2-16 | restore preceding fixture and accepted state |
| S2-09 | reuse_trigger, acceptance | S2-08 | IT2-17, IT2-18 | restore preceding fixture and accepted state |
| S2-10 | original_evidence, acceptance | S2-09 | IT2-19, IT2-20 | restore preceding fixture and accepted state |
| S2-11 | criterion_version, acceptance | S2-10 | IT2-21, IT2-22 | restore preceding fixture and accepted state |
| S2-12 | observed_date, acceptance | S2-11 | IT2-23, IT2-24 | restore preceding fixture and accepted state |
| S2-13 | validity_window, acceptance | S2-12 | IT2-25, IT2-26 | restore preceding fixture and accepted state |
| S2-14 | environment_version, acceptance | S2-13 | IT2-27, IT2-28 | restore preceding fixture and accepted state |
| S2-15 | retention_cost, acceptance | S2-14 | IT2-29, IT2-30 | restore preceding fixture and accepted state |
| S2-16 | recurrence_count, acceptance | S2-15 | IT2-31, IT2-32 | restore preceding fixture and accepted state |
| S2-17 | reader_version, acceptance | S2-16 | IT2-33, IT2-34 | restore preceding fixture and accepted state |
| S2-18 | pending_owner, acceptance | S2-17 | IT2-35, IT2-36 | restore preceding fixture and accepted state |
| S2-19 | retirement_state, acceptance | S2-18 | IT2-37, IT2-38 | restore preceding fixture and accepted state |
| S2-20 | historical_result, acceptance | S2-19 | IT2-39, IT2-40 | restore preceding fixture and accepted state |
| S2-21 | combined interface check, acceptance | S2-20 | IT2-41, IT2-42 | restore preceding fixture and accepted state |
| S2-22 | combined interface check, acceptance | S2-21 | IT2-43, IT2-44 | restore preceding fixture and accepted state |
| S2-23 | combined interface check, acceptance | S2-22 | IT2-45, IT2-46 | restore preceding fixture and accepted state |
| S2-24 | combined interface check, acceptance | S2-23 | IT2-47, IT2-48 | restore preceding fixture and accepted state |
| S2-25 | combined interface check, acceptance | S2-24 | IT2-49, IT2-50 | restore preceding fixture and accepted state |

Fifty executed cross-component cases:

| Test | Input→consumer stimulus | Expected acceptance | Actual acceptance | Result |
|---|---|---|---|---|
| IT2-01 | missing result_id | False | False | PASS |
| IT2-02 | null result_id | False | False | PASS |
| IT2-03 | missing creation_context | False | False | PASS |
| IT2-04 | null creation_context | False | False | PASS |
| IT2-05 | missing actor_type | False | False | PASS |
| IT2-06 | null actor_type | False | False | PASS |
| IT2-07 | missing original_goal | False | False | PASS |
| IT2-08 | null original_goal | False | False | PASS |
| IT2-09 | missing source_edition | False | False | PASS |
| IT2-10 | null source_edition | False | False | PASS |
| IT2-11 | missing helped_condition | False | False | PASS |
| IT2-12 | null helped_condition | False | False | PASS |
| IT2-13 | missing negative_case | False | False | PASS |
| IT2-14 | null negative_case | False | False | PASS |
| IT2-15 | missing evidence_kind | False | False | PASS |
| IT2-16 | null evidence_kind | False | False | PASS |
| IT2-17 | missing reuse_trigger | False | False | PASS |
| IT2-18 | null reuse_trigger | False | False | PASS |
| IT2-19 | missing original_evidence | False | False | PASS |
| IT2-20 | null original_evidence | False | False | PASS |
| IT2-21 | missing criterion_version | False | False | PASS |
| IT2-22 | null criterion_version | False | False | PASS |
| IT2-23 | missing observed_date | False | False | PASS |
| IT2-24 | null observed_date | False | False | PASS |
| IT2-25 | missing validity_window | False | False | PASS |
| IT2-26 | null validity_window | False | False | PASS |
| IT2-27 | missing environment_version | False | False | PASS |
| IT2-28 | null environment_version | False | False | PASS |
| IT2-29 | missing retention_cost | False | False | PASS |
| IT2-30 | null retention_cost | False | False | PASS |
| IT2-31 | missing recurrence_count | False | False | PASS |
| IT2-32 | null recurrence_count | False | False | PASS |
| IT2-33 | missing reader_version | False | False | PASS |
| IT2-34 | null reader_version | False | False | PASS |
| IT2-35 | missing pending_owner | False | False | PASS |
| IT2-36 | null pending_owner | False | False | PASS |
| IT2-37 | missing retirement_state | False | False | PASS |
| IT2-38 | null retirement_state | False | False | PASS |
| IT2-39 | missing historical_result | False | False | PASS |
| IT2-40 | null historical_result | False | False | PASS |
| IT2-41 | valid | True | True | PASS |
| IT2-42 | wrong schema | False | False | PASS |
| IT2-43 | other schema | False | False | PASS |
| IT2-44 | old reader | False | False | PASS |
| IT2-45 | new reader | False | False | PASS |
| IT2-46 | retired | False | False | PASS |
| IT2-47 | changed environment | False | False | PASS |
| IT2-48 | old environment | False | False | PASS |
| IT2-49 | no recurrence | True | True | PASS |
| IT2-50 | empty negative case retained | True | True | PASS |

Each case starts with a complete fixture, changes one producer or combined condition, sends the whole packet to acceptance, and compares the returned decision. This tests end-to-end input propagation and error behavior, not semantic truth of field contents. The twenty issue scenarios are missing/null values for each producer; all have owner, blocker severity, detection and supplied-input recovery in the artifact. No production MTTR or schedule performance is invented.

Environment: local Python and JSON fixtures are available; no network is required; staging and production environments are not present. Test monitoring is the result log. Primary risk is fixture fidelity: a contract-valid packet can contain an unsupported claim. Timing requirement is completed producers before acceptance; no measured latency guarantee exists. Shared-state contention is avoided in the fixture by copied packets, not proven absent for a real concurrent host.

Actual changed operation: a historically valid retained result with a changed reader or environment is withheld from current reuse, while the historical record remains intact.

All 50 expected decisions are executed and the actual count is 50/50. This is a finite contract result. Semantic usefulness, human benefit and future reliability remain unresolved.

Actual mind change: Whole-packet acceptance now rejects the declared conflicting cross-component cases.

Benefit: Fifty local integration cases per target distinguish missing data and boundary conflicts; no production claim follows.

Verdict: UNRESOLVED

Organization: The sequence plus cross-field tests preserves dependencies absent from a field-by-field success list.

Next attempts: Add semantic truth checks; test concurrent writers; compare a partially available packet policy.
