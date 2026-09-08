Intended mind change: Make the design of reading, listening and recall encounters account for different actual access conditions before treating a single presentation as adequate for everyone.

Starting working judgment: The research records are text-first. That is a useful default, but their existence does not establish usability for small screens, assistive output, different language needs, interruption, or an audio-only encounter.

Original source: ../sources/conditions-hsi.original.md. Exact stdout and separate requirements receipt: ../sources/conditions-hsi.requirements.txt; byte checks are in source-receipts.json.

Execution scope and depth: 8x floors met in design products: 8 overlapping user populations, 40 interaction points, 40 distinct candidate human-factors issues (minimum 35), 20 training requirements and 15 accessibility checks. Human characteristics, rendered-interface tests, training and workload measurements remain unperformed; no empirical completion is claimed.

System boundary: a proposed interaction for selecting an encounter, accessing a source, comparing/retrieving, recording a result and resuming or stopping. The system is a design under assessment, not a deployed interface. No actual user populations have been surveyed, and no physical attributes or cognitive capacities are inferred about the current user. Counts, ages, body measurements, strengths, endurance, proficiency and interaction rates are unknown. Populations below are overlapping use-condition groups, not eight fabricated cohorts.

| Population | Role/use condition | Physical/sensory characteristics | Cognitive/design implication |
|---|---|---|---|
| P1 | Desk reader | Stable reading/note workspace; actual body dimensions, age, vision, strength and endurance unknown | Expertise and reading preference unknown; task criterion must remain visible |
| P2 | Small-screen reader | Small viewport by scenario; grip, reach and posture unknown | Navigation and note switching can compete for one view; no measured capacity assumption |
| P3 | Screen-reader user | Sequential spoken output required by scenario; sensory/physical profile otherwise unknown | Relations must survive linearization; expertise and listening rate unknown |
| P4 | Magnification user | Larger text or magnified view required by scenario; exact range unknown | Reduced visible context needs preserved labels; no inferred diagnosis |
| P5 | Audio-first participant | Visual material unavailable during the chosen encounter; actual setting unknown | Pause/seek and equivalent content matter; processing rate unknown |
| P6 | Keyboard/switch participant | Pointer interaction unavailable or not chosen; force/reach capabilities unknown | Focus route and control operation must be explicit; proficiency unknown |
| P7 | Reader using a second language | Language preference differs from source; sensory/physical needs unknown | Terminology and exactness need clarity; no assumption of low education or domain skill |
| P8 | Participant with interruptions | Availability changes during the encounter; fatigue/body state not inferred | Resume state and changed conditions matter; memory/capacity not measured |

Forty interaction points and forty distinct candidate human-factors issues follow. Each task is an input/output/monitor/decision/maintenance event named by its interface. Proposed frequency is once or several times per encounter, not a measured rate; duration is unknown until tested. Source selection, access, response/feedback timing, save state and safe resumption are high consequence for the stated task; presentation preferences are consequential when they block the selected population. Every issue is a candidate failure to test, not a claim that the current host exhibits it.

| Interaction/population | Task | Interface | Candidate issue | Design response |
|---|---|---|---|---|
| H01 / P1 | Choose encounter goal | Goal text/input | I01: Unstated purpose lets completion replace understanding | State the concrete task before presenting options |
| H02 / P1 | Set completion criterion | Task prompt | I02: Criterion drifts from experience to a count | Keep criterion attached to the response |
| H03 / P1 | Identify exact source | Source label | I03: Wrong version is compared | Show source/version alongside excerpt |
| H04 / P1 | Compare two excerpts | Paired text | I04: Misaligned passages produce a false difference | Name the compared passage boundaries |
| H05 / P1 | Classify the result | Result note | I05: Design, attempt and effect collapse together | Expose the observed-result field |
| H06 / P2 | Open material on phone | Small viewport | I06: Desktop layout hides a required control | Provide a usable linear entry route |
| H07 / P2 | Read past a fixed header | Scroll view | I07: Task/source label disappears from context | Retain a recoverable task/source anchor |
| H08 / P2 | Read a wide comparison | Table | I08: Two-axis navigation loses row meaning | Supply a compact row-by-row alternative |
| H09 / P2 | Switch to note input | Editor | I09: Unsaved source-specific note is dropped | Preserve draft and source association |
| H10 / P2 | Continue after network loss | Local file | I10: Online pointer becomes unavailable | Verify actual offline opening beforehand |
| H11 / P3 | Navigate section structure | Headings | I11: Unstructured text requires full serial replay | Use meaningful section labels in the intended interface |
| H12 / P3 | Choose a source link | Link text | I12: Ambiguous link names obscure destination | Use destination-specific link labels |
| H13 / P3 | Interpret table relations | Spoken table | I13: Missing header associations change the relation | Provide explicit row/column labels or linear text |
| H14 / P3 | Read a formula | Math text | I14: Symbol-only expression lacks a usable reading | Give a precise linear statement of the equation |
| H15 / P3 | Use a dependency diagram | Graph alternative | I15: Diagram-only relations are inaccessible | Supply the exact edge list as text |
| H16 / P4 | Increase text size | Zoom/resize | I16: Clipped text hides a condition | Permit readable resizing without lost content |
| H17 / P4 | Follow long lines | Text width | I17: Line tracking burden rises in the chosen view | Allow a manageable reading width |
| H18 / P4 | Distinguish text/background | Contrast | I18: Low contrast makes content hard to perceive | Check actual rendered contrast |
| H19 / P4 | Read verdict status | Status label | I19: Color alone hides the result category | Include the status in words |
| H20 / P4 | Track focused content while zoomed | Focused region | I20: Overlay hides the currently operated item | Check focused content remains visible |
| H21 / P5 | Start audio | Playback control | I21: Unexpected autoplay interrupts another task | Make playback a deliberate action |
| H22 / P5 | Pause before response | Pause control | I22: Fixed progression removes the response opportunity | Allow user-controlled pause where task permits |
| H23 / P5 | Replay one span | Seek/rewind | I23: No return route prevents checking a missed relation | Provide a locatable segment marker |
| H24 / P5 | Change playback pace | Speed control | I24: Unlabeled pace changes the tested exposure | Show the selected pace and preserve it in evidence if relevant |
| H25 / P5 | Switch to text equivalent | Transcript | I25: Audio/text omit different material without notice | Identify equivalence and material omissions |
| H26 / P6 | Reach all task controls | Keyboard route | I26: Pointer-only action blocks the task | Provide an operable sequential route |
| H27 / P6 | Locate current focus | Focus indicator | I27: Focus has no visible indicator | Verify a discernible current-focus state |
| H28 / P6 | Activate the intended target | Control target | I28: Small or crowded targets invite wrong activation | Check target size/spacing or equivalent control |
| H29 / P6 | Save a response | Save feedback | I29: Silent save failure creates false completion | Expose actual saved/failed state |
| H30 / P6 | Reverse a local edit | Undo/history | I30: Unrecoverable deletion destroys the working note | Preserve a reversible edit or prior version |
| H31 / P7 | Choose language | Language setting/text | I31: Default language is misidentified | State language and offer an available alternative |
| H32 / P7 | Resolve an unfamiliar term | Glossary/definition | I32: Jargon hides the operative distinction | Give a concrete term definition at point of need |
| H33 / P7 | Interpret figurative wording | Instruction text | I33: Idiom changes the task’s apparent meaning | Use literal task wording |
| H34 / P7 | Separate quote from paraphrase | Source boundary | I34: Assistant wording is mistaken for original text | Mark source and generated wording distinctly |
| H35 / P7 | Report exact versus approximate recall | Answer criterion | I35: Gist is scored as exact wording | State the required precision before the attempt |
| H36 / P8 | Suspend a session | Pause/save | I36: No checkpoint loses a useful partial state | Save source position and unfinished action |
| H37 / P8 | Resume after interruption | Resume cue | I37: Stale cue resumes the wrong task/version | Display the retained task/version before resuming |
| H38 / P8 | Change setting or device | Access check | I38: Old resource assumptions fail in the new location | Recheck the changed resource before proceeding |
| H39 / P8 | Return for later review | Continuation state | I39: A written date is mistaken for a scheduled event | Show whether an actual continuation exists |
| H40 / P8 | Stop or decline the encounter | Exit/export | I40: All-or-nothing flow pressures unwanted continuation | Allow stop with retained useful work |

Cognitive-load assessment of critical interactions: H04 compares two excerpts plus criterion plus note (four information objects, one selection); H08 adds row/column context (at least two relations to retain); H09 changes views while preserving one unfinished note; H13 requires header associations in serial output; H22 preserves the interval before a response; H29 distinguishes attempted save from confirmed save; H35 retains an exactness criterion; H37 restores task, version and position. These are object counts from the design, not measured memory capacity or Bedford workload ratings. Time pressure is user/setting dependent. A numerical overload rating would be unsupported.

Error analysis: H03 wrong-version selection is a source-identification mistake; H09 dropped draft is a state-loss failure; H14 swapped mathematical relation is a representation error; H22 early feedback is an exposure-order error; H28 wrong target activation is an input slip; H29 false save belief is inadequate feedback; H34 source/paraphrase confusion is an attribution error; H37 stale resume is a context mismatch. The table supplies prevention; recovery is to reopen the correct source/state, preserve the failed attempt and resume from a verified checkpoint. None requires pressuring a person to keep going.

Feedback/situation awareness: normal state should show current task/source and available action; degraded state should identify unavailable material or save failure; completed action should show the actual saved result; unperformed later action should stay visibly unscheduled. Perception: current state is explicit in the design. Comprehension: the state’s effect on the task is stated. Projection: the next required event is named. Actual UI latency and modality behavior are untested.

Workload/staffing design: at encounter start the participant selects task/medium; during comparison they handle sources/criterion/notes; at interruption they preserve a checkpoint; at return they verify changed resources. Peak demand is the simultaneous compare-plus-note transition, not merely total document length. The current proposal uses one participant with optional assistance if actually needed; no second person is assigned or contacted. Staffing count, shift length and capacity are unknown, so no labor estimate or fatigue threshold is fabricated. A support person’s availability is an external condition, not evidence that the participant lacks ability.

Twenty concrete training requirements follow. Current proficiency is unknown in every row. Required proficiency is the observable demonstration named, not an expert identity. Training durations are design estimates only.

| Requirement | Population | Knowledge/skill | Demonstrated target | Method/time |
|---|---|---|---|---|
| T01 | P1 | State task and criterion | Choose the criterion for one sample encounter | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T02 | P1 | Check source/version | Locate the exact source for one note | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T03 | P1 | Compare bounded excerpts | Identify both passage spans correctly | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T04 | P2 | Recover a mobile source anchor | Return to the intended passage after a note | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T05 | P2 | Verify offline material | Open the required file with network unavailable | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T06 | P2 | Read a compact table alternative | Recover one correct row relation | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T07 | P3 | Navigate meaningful headings | Reach a named section through the available route | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T08 | P3 | Read an exact edge list | Recover predecessor and successor without swapping | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T09 | P3 | Interpret linearized formula | Apply the stated expression to one input | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T10 | P4 | Set usable text presentation | Read the target without omitted conditions | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T11 | P4 | Find status beyond color | Identify verdict from text alone | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T12 | P5 | Pause at a response boundary | Stop exposure before producing the chosen response | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T13 | P5 | Resume a named audio span | Return to the specified segment | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T14 | P5 | Identify pace as part of exposure | State selected speed when reporting the task | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T15 | P6 | Follow the actual focus route | Reach and activate the needed control | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T16 | P6 | Verify save and undo | Recover one edited note and its saved state | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T17 | P7 | Resolve an unfamiliar term | Use the provided definition in a concrete case | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T18 | P7 | Separate exact and gist criteria | Score one answer under the declared precision | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T19 | P8 | Create and use a resume cue | Return to the same task/version after a real interruption | Demonstration on actual interface; estimated 1–5 min, unperformed |
| T20 | P8 | Stop with retained partial work | Recover the saved partial result without completing the whole task | Demonstration on actual interface; estimated 1–5 min, unperformed |

Training program: initial orientation uses the participant’s chosen medium and one task; qualification is the relevant row’s actual demonstration on the real interface; continuation is triggered by a changed device, interface or recurring observed error. No training session, simulator, instructor appointment or annual recertification has been created. A broken control is an interface remediation target, not a reason to demand more practice.

Fifteen accessibility checks:

| Check | Domain | Requirement being checked | Present evidence/status |
|---|---|---|---|
| A01 | Text alternatives | Exact graph/image content also available as text | Graph edge lists exist in these records; host media behavior untested |
| A02 | Meaningful sequence | Reading order preserves premise before result | Markdown source order inspectable; rendered assistive route untested |
| A03 | Table labels | Headers and row meanings remain associated | Text tables supplied; renderer associations untested |
| A04 | Resize | Larger text does not drop a qualification | Actual zoom behavior untested |
| A05 | Reflow | Narrow view remains usable without losing row relations | Wide tables need a linear alternative; no host conformance claim |
| A06 | Contrast | Actual text/status is discernible | Rendered colors unknown |
| A07 | Color independence | Verdict has a text label | Present in all application records |
| A08 | Keyboard operation | Every required action is reachable without pointer | Host controls untested |
| A09 | Focus order | Sequential route preserves meaning and operation | Task design specifies order; actual interface untested |
| A10 | Visible focus | Operated item can be found | Host UI untested |
| A11 | Unobscured focus | Overlay does not hide current control | Host UI untested |
| A12 | Adjustable timing | Reading/response interval is not needlessly fixed | No artificial timeout in these text records; host timing untested |
| A13 | Target size/spacing | Activation targets meet relevant size/spacing or exception | Actual CSS/layout unavailable |
| A14 | Audio equivalent | Required content is available in chosen usable medium | Audio/video production not performed |
| A15 | Language/terms | Language and key terms are explicit | English text and tuple meanings supplied; localization untested |

External-standard comparison: meaningful sequential focus is supported by [WCAG 2.2, Focus Order](https://www.w3.org/TR/WCAG22/#focus-order); the need to preserve readable content under narrow/zoomed layouts is grounded in [W3C Reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow). Timing flexibility and activation size have specific conditions and exceptions, so this design does not claim blanket conformance from a text checklist. See [W3C Timing Adjustable](https://www.w3.org/WAI/WCAG21/Understanding/timing-adjustable.html) and [Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html). Actual rendering, keyboard routes and assistive technologies have not been tested.

Inclusivity: left/right handedness, varied body size and temporary impairments are not assigned values; the design leaves input and physical placement selectable. Reduced sensory load, language choice and a retained partial state are options tied to concrete access conditions. No cultural or neurodivergent profile is inferred from a user label.

Priority changes: first preserve usable source access and actual save/feedback state; second preserve task criteria and permitted stop/resume; third provide alternative representations for relations; fourth test display/navigation preferences on actual devices. Risks remaining: the proposed linear alternatives may still omit context; host controls may not meet the proposed route; training may target a nonproblem; timing preferences may conflict with a strict unaided assessment. The latter conflict is resolved by declaring assisted-work versus assessment purpose before cue/feedback exposure, rather than forcing one flow on both.

Downstream-source dispositions: requirements, ram, riskmgmt, testplan, tradestudy and conops originals were loaded and read. Their “Next Steps” form a cyclic engineering program, not prerequisite invocations inside this assessment. Requirements drafting would be a separate system-specification task; RAM prediction lacks component failure data; a live risk program lacks an implemented system and owners; testplan would require actual interface/environment access; trade-study weighting lacks stakeholder priorities; ConOps development would require an agreed deployment scope. None is falsely counted as an executed 8x downstream program. The assessment’s actual required products and numerical floors are all present; empirical population validation and UI testing remain open.

Actual mind change: The conditions agent expanded the design from a single text-first flow to concrete access-condition choices, alternative representations, and stop/resume paths with forty explicit interaction risks.

Benefit: The design is inspectable and more inclusive in scope, but no human usability, training, accessibility-conformance or workload effect has been measured.

Verdict: UNRESOLVED

Organization: Population→interaction→candidate issue→observable target is more useful for this assessment than one average-user profile. The representation retains overlapping populations and unknown measurements rather than inventing demographic ranges.

Next attempts: Test one actual chosen access route; inspect narrow-screen and assistive reading of the tables; resolve assisted-work versus assessment purpose before hiding cues.
