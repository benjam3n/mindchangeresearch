Intended mind change: Change the planned component boundary after testing whether expanded decomposition actually helps.

# Decompose retained evidence responsibilities and test depth

Starting judgment: A fine functional split seems inspectable, but I have no evidence that every discovered responsibility should become a separately deployed component.

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-sysdecomp.md`; current requirements are retained separately in `../sources/systems-sysdecomp.requirements.txt`.

Depth: Original 8x exploration supplies 83 registered nodes, 50 operational leaf components, 5 levels, 50 defined interfaces, 82 mapped interactions and 9 criteria. The source depth assessment rejects deploying all fifty leaves.

Primary decomposition is functional with a secondary distinction between positive and boundary paths. System scope is later retention/retrieval; external human experience and host capability remain inputs, not fabricated internal services. Single-process deployment and one current worker are hard constraints.

Five-level registry: system→domain→category→capability→operational leaf. The complete artifact contains 83 nodes, including fifty leaf candidates. Their purposes are exact operational requirements, with one owner and no hidden actor.

| ID | Parent | Level | Responsibility |
|---|---|---|---|
| D2-0 | None | 0 | produce a useful scoped contribution |
| D2-domain0 | D2-0 | 1 | coordinate input and choice |
| D2-domain1 | D2-0 | 1 | coordinate evidence and revision |
| D2-cat0 | D2-domain0 | 2 | own retention identity |
| D2-cat0-cap0 | D2-cat0 | 3 | construct retention identity |
| D2-cat0-cap1 | D2-cat0 | 3 | restrict retention identity |
| D2-cat0-leaf0 | D2-cat0-cap0 | 4 | Assign stable identity to a retained result |
| D2-cat0-leaf1 | D2-cat0-cap0 | 4 | Preserve result creation context |
| D2-cat0-leaf2 | D2-cat0-cap0 | 4 | Retain actor type with result |
| D2-cat0-leaf3 | D2-cat0-cap1 | 4 | Retain original goal wording |
| D2-cat0-leaf4 | D2-cat0-cap1 | 4 | Preserve source edition identity |
| D2-cat1 | D2-domain0 | 2 | own future retrieval |
| D2-cat1-cap0 | D2-cat1 | 3 | construct future retrieval |
| D2-cat1-cap1 | D2-cat1 | 3 | restrict future retrieval |
| D2-cat1-leaf0 | D2-cat1-cap0 | 4 | Index by a concrete reuse trigger |
| D2-cat1-leaf1 | D2-cat1-cap0 | 4 | Return original evidence with retrieved result |
| D2-cat1-leaf2 | D2-cat1-cap0 | 4 | Return scope before reapplication |
| D2-cat1-leaf3 | D2-cat1-cap1 | 4 | Return criterion version |
| D2-cat1-leaf4 | D2-cat1-cap1 | 4 | Allow a query to return no match |
| D2-cat2 | D2-domain0 | 2 | own temporal validity |
| D2-cat2-cap0 | D2-cat2 | 3 | construct temporal validity |
| D2-cat2-cap1 | D2-cat2 | 3 | restrict temporal validity |
| D2-cat2-leaf0 | D2-cat2-cap0 | 4 | Retain the observation date |
| D2-cat2-leaf1 | D2-cat2-cap0 | 4 | State a validity window when known |
| D2-cat2-leaf2 | D2-cat2-cap0 | 4 | Represent unknown durability |
| D2-cat2-leaf3 | D2-cat2-cap1 | 4 | Flag a changed environment |
| D2-cat2-leaf4 | D2-cat2-cap1 | 4 | Flag a changed goal |
| D2-cat3 | D2-domain0 | 2 | own long-term resources |
| D2-cat3-cap0 | D2-cat3 | 3 | construct long-term resources |
| D2-cat3-cap1 | D2-cat3 | 3 | restrict long-term resources |
| D2-cat3-leaf0 | D2-cat3-cap0 | 4 | Count recurring maintenance separately |
| D2-cat3-leaf1 | D2-cat3-cap0 | 4 | Retain setup versus per-use cost |
| D2-cat3-leaf2 | D2-cat3-cap0 | 4 | Retain the recurrence crossover |
| D2-cat3-leaf3 | D2-cat3-cap1 | 4 | Represent retention capacity |
| D2-cat3-leaf4 | D2-cat3-cap1 | 4 | Represent restoration cost |
| D2-cat4 | D2-domain0 | 2 | own learning evidence |
| D2-cat4-cap0 | D2-cat4 | 3 | construct learning evidence |
| D2-cat4-cap1 | D2-cat4 | 3 | restrict learning evidence |
| D2-cat4-leaf0 | D2-cat4-cap0 | 4 | Record the next actual recurrence |
| D2-cat4-leaf1 | D2-cat4-cap0 | 4 | Record whether retrieval happened |
| D2-cat4-leaf2 | D2-cat4-cap0 | 4 | Record whether eligibility was accepted |
| D2-cat4-leaf3 | D2-cat4-cap1 | 4 | Record the performed operation at recurrence |
| D2-cat4-leaf4 | D2-cat4-cap1 | 4 | Record the observed recurrence consequence |
| D2-cat5 | D2-domain1 | 2 | own criteria evolution |
| D2-cat5-cap0 | D2-cat5 | 3 | construct criteria evolution |
| D2-cat5-cap1 | D2-cat5 | 3 | restrict criteria evolution |
| D2-cat5-leaf0 | D2-cat5-cap0 | 4 | Preserve earlier criterion weights |
| D2-cat5-leaf1 | D2-cat5-cap0 | 4 | Retain the reason a criterion changed |
| D2-cat5-leaf2 | D2-cat5-cap0 | 4 | Name who authorized criterion revision |
| D2-cat5-leaf3 | D2-cat5-cap1 | 4 | Recompute old options under new criteria separately |
| D2-cat5-leaf4 | D2-cat5-cap1 | 4 | Preserve old comparison results |
| D2-cat6 | D2-domain1 | 2 | own interface evolution |
| D2-cat6-cap0 | D2-cat6 | 3 | construct interface evolution |
| D2-cat6-cap1 | D2-cat6 | 3 | restrict interface evolution |
| D2-cat6-leaf0 | D2-cat6-cap0 | 4 | Record reader format version |
| D2-cat6-leaf1 | D2-cat6-cap0 | 4 | Maintain an explicit migration mapping |
| D2-cat6-leaf2 | D2-cat6-cap0 | 4 | Reject unknown incompatible versions |
| D2-cat6-leaf3 | D2-cat6-cap1 | 4 | Preserve original bytes during migration |
| D2-cat6-leaf4 | D2-cat6-cap1 | 4 | Retain semantic exceptions across conversion |
| D2-cat7 | D2-domain1 | 2 | own coordination continuity |
| D2-cat7-cap0 | D2-cat7 | 3 | construct coordination continuity |
| D2-cat7-cap1 | D2-cat7 | 3 | restrict coordination continuity |
| D2-cat7-leaf0 | D2-cat7-cap0 | 4 | Name the current accountable owner |
| D2-cat7-leaf1 | D2-cat7-cap0 | 4 | Transfer pending status explicitly |
| D2-cat7-leaf2 | D2-cat7-cap0 | 4 | Retain work already performed |
| D2-cat7-leaf3 | D2-cat7-cap1 | 4 | Retain blocked prerequisites |
| D2-cat7-leaf4 | D2-cat7-cap1 | 4 | Reject late work for obsolete goals |
| D2-cat8 | D2-domain1 | 2 | own reliability and recovery |
| D2-cat8-cap0 | D2-cat8 | 3 | construct reliability and recovery |
| D2-cat8-cap1 | D2-cat8 | 3 | restrict reliability and recovery |
| D2-cat8-leaf0 | D2-cat8-cap0 | 4 | Keep a recoverable previous accepted state |
| D2-cat8-leaf1 | D2-cat8-cap0 | 4 | Detect a damaged evidence reference |
| D2-cat8-leaf2 | D2-cat8-cap0 | 4 | Distinguish copy redundancy from independent evidence |
| D2-cat8-leaf3 | D2-cat8-cap1 | 4 | Represent common-cause failure |
| D2-cat8-leaf4 | D2-cat8-cap1 | 4 | Separate repair time from waiting time |
| D2-cat9 | D2-domain1 | 2 | own agency and retirement |
| D2-cat9-cap0 | D2-cat9 | 3 | construct agency and retirement |
| D2-cat9-cap1 | D2-cat9 | 3 | restrict agency and retirement |
| D2-cat9-leaf0 | D2-cat9-cap0 | 4 | Allow a user to decline reuse |
| D2-cat9-leaf1 | D2-cat9-cap0 | 4 | Allow goal change without rewriting history |
| D2-cat9-leaf2 | D2-cat9-cap0 | 4 | Avoid preserving unwanted human attributes |
| D2-cat9-leaf3 | D2-cat9-cap1 | 4 | Retire a contradicted recommendation |
| D2-cat9-leaf4 | D2-cat9-cap1 | 4 | Keep a retirement reason |

Fifty interfaces each pass one concrete leaf result to its responsible capability; protocol, data, frequency and error state are in `decomposition-2.json`. Eighty requirement allocations have exactly one primary leaf each; composite boundary leaves carry several related restrictions. An additional 32 aggregation interactions map the higher-level communication. Cross-cutting logs belong to revision/continuity; source and host interfaces have designated input owners.

Responsibility checks: specific nouns/functions pass; one accountable owner passes; data coupling is accepted; common mutable state would require conflict resolution; internal content mutation is excluded. Leaf deployment fails the size/change-impact check: fifty separately deployed services would turn simple local predicates into interface overhead. The source's depth assessment thus rejects implementation at that leaf granularity while preserving the discovered boundaries in ten category owners.

Nine criteria results: {"requirements_allocated": true, "single_primary_owner": true, "five_levels": true, "no_missing_parent": true, "interface_endpoints_exist": true, "no_cycles": true, "logging_allocated": true, "external_boundary_allocated": true, "leaf_deployment_warranted": false}. All eighty requirements are allocated, but allocation does not prove their satisfaction. The final operational grouping merges leaf implementation into the ten meaningful category owners; it does not delete their distinct conditions.

Actual application: historical truth, current fit and future retrieval remain separate state dimensions inside one retained-result module, so migration does not create three independent writers of the same result identity.

The explored fifty-leaf decomposition earns no recommendation to deploy fifty components. Its negative finding is that this granularity fails the source's own depth criterion for the current system. The two applications differ in target and ownership conflict, not merely component names.

Actual mind change: The fifty-leaf deployment candidate is rejected; operational predicates remain grouped under ten accountable owners.

Benefit: Boundary coverage is preserved, but the attempted deployment decomposition adds unearned coordination cost. The negative result remains visible.

Verdict: REJECT

Organization: Five-level design reveals responsibilities; ten-owner operational grouping is actually used in the prototype that follows.

Next attempts: Test a genuinely independent deployment need; compare data ownership decomposition; inspect one leaf that deserves a separate component.
