Intended mind change: Change a concrete system behavior by comparing state and responsibility architectures.

# Architecture for request boundary and downstream change

Starting judgment: I would begin with a shared action list; it is simpler, but its response to the present changed-state case has not been specified.

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-sysarch.md`; current requirements are retained separately in `../sources/systems-sysarch.requirements.txt`.

Depth: Original 8x floors met by 16 named subsystems, 25 specified interfaces, 10 quality attributes, 5 candidate architectures and 5 views; twenty weight perturbations are computed.

System: human/model/tool encounter coordinator. Purpose is a useful conditional contribution under the current request. Interpretation is design/refactor. Drivers: goal fidelity, actor scope, recoverability, bounded resources and revisability. External human experience and future host availability remain outside the implemented design; inputs must not be invented.

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
| Fidelity | 3 | 5 | 4 | 3 | 5 |
| Scope clarity | 2 | 4 | 4 | 3 | 5 |
| Recoverability | 2 | 4 | 5 | 3 | 5 |
| Modifiability | 2 | 4 | 5 | 5 | 4 |
| Traceability | 2 | 4 | 5 | 3 | 5 |
| Simplicity | 5 | 3 | 2 | 4 | 2 |
| Prompt delivery | 5 | 3 | 2 | 4 | 3 |
| Portability | 3 | 4 | 4 | 3 | 4 |
| Resource control | 2 | 4 | 4 | 3 | 5 |
| Agency | 3 | 4 | 4 | 3 | 5 |
| Weighted total | 101 | 148 | 149 | 122 | 167 |

Selected: actor contracts. Twenty sensitivity calculations vary each weight ±1; all totals are in the artifact. Accepted risk is additional interface/record overhead. Mitigation is retaining one accountable owner per responsibility and only the relevant view for a live choice. Simplicity and prompt delivery favor the mutable-document candidate; recoverability and scope favor the selected design. No universal architectural winner is claimed.

Sixteen responsibilities have one owned output each; none is a claim of sixteen deployed services:

| ID | Subsystem | Owned output / function | Owner / deployment |
|---|---|---|---|
| A3-01 | Request boundary | current target | assistant / local artifact |
| A3-02 | Actor map | responsible roles | assistant / local artifact |
| A3-03 | Setting inventory | available conditions | assistant / local artifact |
| A3-04 | Encounter options | possible interaction | assistant / local artifact |
| A3-05 | Attention budget | remaining attention | assistant / local artifact |
| A3-06 | Pace controller | timing window | assistant / local artifact |
| A3-07 | Representation builder | candidate medium | assistant / local artifact |
| A3-08 | Consent boundary | declared permission | assistant / local artifact |
| A3-09 | Shared context | common inputs | assistant / local artifact |
| A3-10 | Tool adapter | actual capability | assistant / local artifact |
| A3-11 | Action queue | ordered work | assistant / local artifact |
| A3-12 | Interruption control | cancellation state | assistant / local artifact |
| A3-13 | Human response intake | reported response | assistant / local artifact |
| A3-14 | Evidence separation | actor-specific effect | assistant / local artifact |
| A3-15 | Goal revision | new target version | assistant / local artifact |
| A3-16 | Next encounter | bounded continuation | assistant / local artifact |

Twenty-five interfaces:

| ID | From | To | Type / protocol | Data | Frequency | Criticality |
|---|---|---|---|---|---|---|
| I3-01 | A3-01 | A3-02 | versioned data packet / JSON-file contract | current target | per relevant transition | HIGH |
| I3-02 | A3-02 | A3-03 | versioned data packet / JSON-file contract | responsible roles | per relevant transition | HIGH |
| I3-03 | A3-03 | A3-04 | versioned data packet / JSON-file contract | available conditions | per relevant transition | HIGH |
| I3-04 | A3-04 | A3-05 | versioned data packet / JSON-file contract | possible interaction | per relevant transition | HIGH |
| I3-05 | A3-05 | A3-06 | versioned data packet / JSON-file contract | remaining attention | per relevant transition | HIGH |
| I3-06 | A3-06 | A3-07 | versioned data packet / JSON-file contract | timing window | per relevant transition | HIGH |
| I3-07 | A3-07 | A3-08 | versioned data packet / JSON-file contract | candidate medium | per relevant transition | HIGH |
| I3-08 | A3-08 | A3-09 | versioned data packet / JSON-file contract | declared permission | per relevant transition | HIGH |
| I3-09 | A3-09 | A3-10 | versioned data packet / JSON-file contract | common inputs | per relevant transition | HIGH |
| I3-10 | A3-10 | A3-11 | versioned data packet / JSON-file contract | actual capability | per relevant transition | HIGH |
| I3-11 | A3-11 | A3-12 | versioned data packet / JSON-file contract | ordered work | per relevant transition | HIGH |
| I3-12 | A3-12 | A3-13 | versioned data packet / JSON-file contract | cancellation state | per relevant transition | HIGH |
| I3-13 | A3-13 | A3-14 | versioned data packet / JSON-file contract | reported response | per relevant transition | HIGH |
| I3-14 | A3-14 | A3-15 | versioned data packet / JSON-file contract | actor-specific effect | per relevant transition | HIGH |
| I3-15 | A3-15 | A3-16 | versioned data packet / JSON-file contract | new target version | per relevant transition | HIGH |
| I3-16 | A3-01 | A3-09 | versioned data packet / JSON-file contract | current target | per relevant transition | MED |
| I3-17 | A3-03 | A3-06 | versioned data packet / JSON-file contract | available conditions | per relevant transition | MED |
| I3-18 | A3-04 | A3-08 | versioned data packet / JSON-file contract | possible interaction | per relevant transition | MED |
| I3-19 | A3-05 | A3-10 | versioned data packet / JSON-file contract | remaining attention | per relevant transition | MED |
| I3-20 | A3-06 | A3-13 | versioned data packet / JSON-file contract | timing window | per relevant transition | MED |
| I3-21 | A3-07 | A3-11 | versioned data packet / JSON-file contract | candidate medium | per relevant transition | MED |
| I3-22 | A3-08 | A3-12 | versioned data packet / JSON-file contract | declared permission | per relevant transition | MED |
| I3-23 | A3-09 | A3-14 | versioned data packet / JSON-file contract | common inputs | per relevant transition | MED |
| I3-24 | A3-13 | A3-15 | versioned data packet / JSON-file contract | reported response | per relevant transition | MED |
| I3-25 | A3-15 | A3-16 | versioned data packet / JSON-file contract | new target version | per relevant transition | MED |

Critical contract: packet contains origin, target, schema_version, target_revision, payload and evidence_scope. A malformed or obsolete packet yields HOLD with reason; its dependent action is not committed. Version migration is an explicit new packet. SLA here is causal ordering—consumer reads a completed producer packet—not an invented millisecond guarantee. Security/authority is current-task-scoped; no external credential or recipient is invented. External interfaces are user request inbound, original source inbound, actual host capability inbound and authorized result outbound; root owns publication.

Five architectural views: Functional—sixteen capabilities grouped by intake/choice/action/evidence/revision. Physical—one local filesystem and assistant process, external user and tool host; no invented redundant production deployment. Behavioral—input captures revision, choice consumes it, result returns, acceptance rechecks it. Information—immutable identities with evidence scope; selected pattern defines whether views or packets are authoritative. Evolution—criterion or schema changes create a new revision; previous results remain historical.

Decision log: adopt contracts that separate actor, permission and target version; retain prior evidence; reject unversioned shared updates for this target; keep open whether implementation overhead earns its cost at larger scale.

Actual transformed case: a request to describe a human action is followed by a tool result proposing execution. The contract has description-only authority, so the execution proposal is refused while the useful description remains eligible. The design transition is executed as the explicit input/output example in `architecture-3-case.json`. The advantage is a defined decision under the constructed state transition, not field reliability or a deployed system.

Actual mind change: The design now uses contracts that separate actor, permission and target version.

Benefit: The transformed case has an explicit scope-preserving outcome: a request to describe a human action is followed by a tool result proposing execution. The contract has description-only authority, so the execution proposal is refused while the useful description remains eligible.

Verdict: KEEP

Organization: Five views retain behavior, ownership and evolution together; the source-skill list alone does not express these interfaces.

Next attempts: Implement only the critical transition; challenge a scoring premise; test a common-cause state loss.
