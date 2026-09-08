Intended mind change: Change a concrete system behavior by comparing state and responsibility architectures.

# Architecture for goal capture and downstream change

Starting judgment: I would begin with one mutable current plan; it is simpler, but its response to the present changed-state case has not been specified.

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-sysarch.md`; current requirements are retained separately in `../sources/systems-sysarch.requirements.txt`.

Depth: Original 8x floors met by 16 named subsystems, 25 specified interfaces, 10 quality attributes, 5 candidate architectures and 5 views; twenty weight perturbations are computed.

System: present action selector. Purpose is a useful conditional contribution under the current request. Interpretation is design/refactor. Drivers: goal fidelity, actor scope, recoverability, bounded resources and revisability. External human experience and future host availability remain outside the implemented design; inputs must not be invented.

Ten quality attributes are ranked by the declared analyst design weights below. They are transparent design judgments, not measured user utility. Each scenario asks whether a changed input is preserved and receives a definite response. A score 5 means a pattern directly represents the condition, 3 means an explicit added convention is required, 1 means the pattern omits it. The weights were declared before this calculation; actual stakeholder approval is not inferred.

| Quality | Weight | Stimulus / response / measure |
|---|---|---|
| Fidelity | 5 | Changed fidelity condition / explicit current response / condition and result both retained |
| Scope clarity | 5 | Changed scope clarity condition / explicit current response / condition and result both retained |
| Recoverability | 4 | Changed recoverability condition / explicit current response / condition and result both retained |
| Modifiability | 3 | Changed modifiability condition / explicit current response / condition and result both retained |
| Traceability | 4 | Changed traceability condition / explicit current response / condition and result both retained |
| Simplicity | 3 | Changed simplicity condition / explicit current response / condition and result both retained |
| Prompt delivery | 2 | Changed prompt delivery condition / explicit current response / condition and result both retained |
| Portability | 2 | Changed portability condition / explicit current response / condition and result both retained |
| Resource control | 4 | Changed resource control condition / explicit current response / condition and result both retained |
| Agency | 5 | Changed agency condition / explicit current response / condition and result both retained |

Five candidates share the sixteen required responsibilities but materially differ in state ownership, event ordering and coordination:

| Architecture | Structure and tradeoff | Development cost | Operational cost |
|---|---|---|---|
| single mutable document | All sixteen responsibilities live in one shared mutable document; every update can replace context. Low setup cost, wide change impact. | LOW | LOW |
| layered immutable packets | Sixteen responsibilities retain separate immutable input/output packets in five layers: intake, choice, commitment, assessment, revision. Layer changes require explicit version edges. | MED | LOW |
| event log plus views | All sixteen responsibilities append events to one ordered log; functional views are derived projections. Historical revisions remain reconstructable, but rebuilding views adds work. | HIGH | MED |
| shared blackboard | Sixteen responsibilities publish to a common blackboard and read each other’s latest facts. Flexible discovery, but conflicting writers require conflict resolution. | MED | MED |
| actor contracts | Sixteen responsibility contracts use explicit sender, receiver, authority and target revision. Independent responsibilities are clear; interface count and handoff cost rise. | HIGH | HIGH |

| Quality | single mutable document | layered immutable packets | event log plus views | shared blackboard | actor contracts |
|---|---|---|---|---|---|
| Fidelity | 3 | 5 | 5 | 3 | 4 |
| Scope clarity | 2 | 5 | 4 | 3 | 4 |
| Recoverability | 2 | 4 | 5 | 3 | 4 |
| Modifiability | 2 | 4 | 5 | 5 | 4 |
| Traceability | 2 | 5 | 5 | 3 | 4 |
| Simplicity | 5 | 3 | 2 | 4 | 2 |
| Prompt delivery | 5 | 3 | 2 | 4 | 2 |
| Portability | 5 | 4 | 4 | 3 | 3 |
| Resource control | 2 | 5 | 4 | 3 | 4 |
| Agency | 3 | 5 | 4 | 3 | 5 |
| Weighted total | 105 | 166 | 154 | 122 | 141 |

Selected: layered immutable packets. Twenty sensitivity calculations vary each weight ±1; all totals are in the artifact. Accepted risk is additional interface/record overhead. Mitigation is retaining one accountable owner per responsibility and only the relevant view for a live choice. Simplicity and prompt delivery favor the mutable-document candidate; recoverability and scope favor the selected design. No universal architectural winner is claimed.

Sixteen responsibilities have one owned output each; none is a claim of sixteen deployed services:

| ID | Subsystem | Owned output / function | Owner / deployment |
|---|---|---|---|
| A1-01 | Goal capture | requested action | assistant / local artifact |
| A1-02 | Interpretation set | candidate meanings | assistant / local artifact |
| A1-03 | Source access | readable original | assistant / local artifact |
| A1-04 | Input normalization | typed values | assistant / local artifact |
| A1-05 | Option generation | candidate operations | assistant / local artifact |
| A1-06 | Evidence matching | scope matches | assistant / local artifact |
| A1-07 | Prerequisite graph | required order | assistant / local artifact |
| A1-08 | Budget model | feasible bundles | assistant / local artifact |
| A1-09 | Criterion store | versioned standards | assistant / local artifact |
| A1-10 | Option comparison | conditional choice | assistant / local artifact |
| A1-11 | Authority check | authorized action | assistant / local artifact |
| A1-12 | Dispatcher | task revision | assistant / local artifact |
| A1-13 | Result acceptance | current result | assistant / local artifact |
| A1-14 | Consequence assessment | observed difference | assistant / local artifact |
| A1-15 | Revision propagation | invalidated descendants | assistant / local artifact |
| A1-16 | Presentation | usable answer | assistant / local artifact |

Twenty-five interfaces:

| ID | From | To | Type / protocol | Data | Frequency | Criticality |
|---|---|---|---|---|---|---|
| I1-01 | A1-01 | A1-02 | versioned data packet / JSON-file contract | requested action | per relevant transition | HIGH |
| I1-02 | A1-02 | A1-03 | versioned data packet / JSON-file contract | candidate meanings | per relevant transition | HIGH |
| I1-03 | A1-03 | A1-04 | versioned data packet / JSON-file contract | readable original | per relevant transition | HIGH |
| I1-04 | A1-04 | A1-05 | versioned data packet / JSON-file contract | typed values | per relevant transition | HIGH |
| I1-05 | A1-05 | A1-06 | versioned data packet / JSON-file contract | candidate operations | per relevant transition | HIGH |
| I1-06 | A1-06 | A1-07 | versioned data packet / JSON-file contract | scope matches | per relevant transition | HIGH |
| I1-07 | A1-07 | A1-08 | versioned data packet / JSON-file contract | required order | per relevant transition | HIGH |
| I1-08 | A1-08 | A1-09 | versioned data packet / JSON-file contract | feasible bundles | per relevant transition | HIGH |
| I1-09 | A1-09 | A1-10 | versioned data packet / JSON-file contract | versioned standards | per relevant transition | HIGH |
| I1-10 | A1-10 | A1-11 | versioned data packet / JSON-file contract | conditional choice | per relevant transition | HIGH |
| I1-11 | A1-11 | A1-12 | versioned data packet / JSON-file contract | authorized action | per relevant transition | HIGH |
| I1-12 | A1-12 | A1-13 | versioned data packet / JSON-file contract | task revision | per relevant transition | HIGH |
| I1-13 | A1-13 | A1-14 | versioned data packet / JSON-file contract | current result | per relevant transition | HIGH |
| I1-14 | A1-14 | A1-15 | versioned data packet / JSON-file contract | observed difference | per relevant transition | HIGH |
| I1-15 | A1-15 | A1-16 | versioned data packet / JSON-file contract | invalidated descendants | per relevant transition | HIGH |
| I1-16 | A1-01 | A1-09 | versioned data packet / JSON-file contract | requested action | per relevant transition | MED |
| I1-17 | A1-03 | A1-06 | versioned data packet / JSON-file contract | readable original | per relevant transition | MED |
| I1-18 | A1-04 | A1-08 | versioned data packet / JSON-file contract | typed values | per relevant transition | MED |
| I1-19 | A1-05 | A1-10 | versioned data packet / JSON-file contract | candidate operations | per relevant transition | MED |
| I1-20 | A1-06 | A1-13 | versioned data packet / JSON-file contract | scope matches | per relevant transition | MED |
| I1-21 | A1-07 | A1-11 | versioned data packet / JSON-file contract | required order | per relevant transition | MED |
| I1-22 | A1-08 | A1-12 | versioned data packet / JSON-file contract | feasible bundles | per relevant transition | MED |
| I1-23 | A1-09 | A1-14 | versioned data packet / JSON-file contract | versioned standards | per relevant transition | MED |
| I1-24 | A1-13 | A1-15 | versioned data packet / JSON-file contract | current result | per relevant transition | MED |
| I1-25 | A1-15 | A1-16 | versioned data packet / JSON-file contract | invalidated descendants | per relevant transition | MED |

Critical contract: packet contains origin, target, schema_version, target_revision, payload and evidence_scope. A malformed or obsolete packet yields HOLD with reason; its dependent action is not committed. Version migration is an explicit new packet. SLA here is causal ordering—consumer reads a completed producer packet—not an invented millisecond guarantee. Security/authority is current-task-scoped; no external credential or recipient is invented. External interfaces are user request inbound, original source inbound, actual host capability inbound and authorized result outbound; root owns publication.

Five architectural views: Functional—sixteen capabilities grouped by intake/choice/action/evidence/revision. Physical—one local filesystem and assistant process, external user and tool host; no invented redundant production deployment. Behavioral—input captures revision, choice consumes it, result returns, acceptance rechecks it. Information—immutable identities with evidence scope; selected pattern defines whether views or packets are authoritative. Evolution—criterion or schema changes create a new revision; previous results remain historical.

Decision log: adopt an immutable plan packet bound to budget and criterion versions; retain prior evidence; reject unversioned shared updates for this target; keep open whether implementation overhead earns its cost at larger scale.

Actual transformed case: a budget changes from 60 to 40 while a 55-unit bundle is pending. The old packet remains historical and is rejected for commitment under the new budget; recomputation selects S+C at cost 35 and value 40. The design transition is executed as the explicit input/output example in `architecture-1-case.json`. The advantage is a defined decision under the constructed state transition, not field reliability or a deployed system.

Actual mind change: The design now uses an immutable plan packet bound to budget and criterion versions.

Benefit: The transformed case has an explicit scope-preserving outcome: a budget changes from 60 to 40 while a 55-unit bundle is pending. The old packet remains historical and is rejected for commitment under the new budget; recomputation selects S+C at cost 35 and value 40.

Verdict: KEEP

Organization: Five views retain behavior, ownership and evolution together; the source-skill list alone does not express these interfaces.

Next attempts: Implement only the critical transition; challenge a scoring premise; test a common-cause state loss.
