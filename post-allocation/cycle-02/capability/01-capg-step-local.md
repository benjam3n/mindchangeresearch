# CAPG — capability is local to a step and its interface

Intended mind change: Replace whole-task “can/cannot do” labels with requirement-local capability classifications.

Actual starting judgment: “Validate the field report” read like one task and tempted one capability label.

Concrete input: `frozen-inputs.md`, CAPG steps (a)–(d), $0 budget, 30-minute deadline.

## Requirement and capability table

| Step | Requirements | Direct/tool check | Final category | Cost | Prerequisites |
|---|---|---|---|---:|---|
| a. Recompute CSV totals | digital bytes, arithmetic, readable schema | AI can process supplied data directly | `ai_native` | $0 | attached readable CSV and field definitions |
| b. Inspect physical seal in Chicago | location, physical observation, current time | no physical presence; delegation would cost money and exceed known budget | `infeasible` under current constraints | >$0 | human/site access, funds, custody protocol |
| c. Email named owner | verified recipient, email access, authority to send | no email connector and no verified recipient identity | `infeasible` now; potentially `ai_with_tool` after gates | unknown | configured email, recipient resolution, send authorization |
| d. Decide whether evidence warrants publication | criteria, evidence, domain judgment, publication authority | AI can assess supplied evidence; authority to publish is not supplied | `ai_native` for recommendation; publication act gated | $0 analysis | publication standard and authorized actor |

The whole task is therefore mixed-capability and cannot honestly be labeled either fully executable or fully impossible.

## Transformations and execution plan

### Step a

Method: parse the CSV, recompute each total, compare against reported totals, emit discrepancies.

Success: every row used, formulas stated, discrepancies reproducible. Fallback: if schema definitions are absent, return exact unresolved fields rather than infer them.

### Step b

Core goal: obtain evidence about seal state. Digital alternative: receive a current photograph plus timestamp and custody evidence. Under the frozen input neither exists, so physical validation remains infeasible. Do not substitute an old or unattributed image.

Success: seal feature visible, capture time relevant, location/custody supported. Fallback: mark the seal claim unresolved and exclude it from publication support.

### Step c

Core goal: obtain owner confirmation. Alternative within current constraints: draft questions and preserve them as unsent. “Prepared” is not “sent.”

Success: only a verified delivery record plus matched recipient can establish sending. Fallback: keep confirmation absent.

### Step d

Method: produce a recommendation partitioning recomputed facts, physical-seal gap, and missing owner confirmation.

Success: no gated evidence is represented as observed; publication status follows supplied criteria and authority. Fallback: recommend partial/nonpublication pending named gates.

## Result on the frozen task

Execute (a) if the attachment exists. Prepare but do not send (c). Mark (b) infeasible under budget/deadline. Perform the evidential assessment portion of (d), but do not claim authority to publish. Overall status: PARTIAL, with step-local products and gates.

## Distinct later use

Later input: a photograph of the seal becomes available, but no custody proof accompanies it.

Step b transforms from wholly physical/infeasible to `ai_with_tool` for image-feature inspection, while the claim “this is the current Chicago seal” remains gated by time/location/custody. The capability to inspect pixels does not create capability to establish provenance. Steps a, c, and d retain their prior classifications.

## Outcome

Actual mind change: I changed from one whole-task capability label to a vector of step, interface, evidence, and authority capabilities.

Benefit or harm: The classification permits valid computation and assessment without pretending to inspect a site, send an email, verify a recipient, or authorize publication.

Verdict: KEEP — complete as a capability-gate application; physical observation, communication, and publication remain unresolved where specified.

Content assessment: Requirements, categories, methods, costs, prerequisites, transformations, success criteria, and fallbacks are present.

Organization assessment: A step-local matrix is more informative than a task-level boolean. This reinforces existing human/tool gate discipline and is not counted as a new distinct finding.

Next attempts: Add a verified photo custody chain; provide email access but ambiguous recipient identity; separate recommendation authority from publication authority in a real workflow; measure handoff failures across capability boundaries.
