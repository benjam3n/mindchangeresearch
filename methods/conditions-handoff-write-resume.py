from pathlib import Path
import json,importlib.util,itertools

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('condition_writer',ROOT/'conditions-handoff-write.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);put=module.put
inputs=json.loads((ROOT/'conditions-handoff-inputs-before.json').read_text())
uf=json.loads((ROOT/'conditions-handoff-uf-later-use.json').read_text())
boc=json.loads((ROOT/'conditions-handoff-boc-results.json').read_text())

uses=[
('U01','Equal arrival entitlement for indivisible requests','Three jobs A,B,C arrive in that order, each needs one unit; FIFO completes at 1,2,3 without overtaking.','Arrival records; simple; immediate; known duration; three requests.','Arrival order answers the stated entitlement directly; setup optimization and deadline search add no benefit when setup is zero and deadlines are absent.','excellent','/rso if setup differs; /td if a deadline binds'),
('U02','Lowest mean wait in an all-ready finite batch','Durations A=5,B=1,C=2, no deadlines or setup: B,C,A gives starts 0,1,3, mean 4/3; A,B,C gives 0,5,6, mean 11/3.','Known sizes; simple; deliberate; deterministic; three jobs.','SJF directly improves the declared wait measure; topology supplies no preference because there are no edges.','excellent','/to if edges constrain readiness; /rso if switching occupies time'),
('U03','A finite high-importance request before routine work','A routine 4-unit request and an important 3-unit request are ready; the stated objective prefers the important output first even though it is not the shortest possible policy in general.','Importance labels; simple; urgent; known labels; finite queue.','Priority selects by the supplied importance instead of inventing a due date or equating importance with short duration.','good','/td when importance is an actual due time; /ecal when the priority decision itself needs calibration'),
('U04','An old low-priority request among new high-priority arrivals','At each unit a high-priority one-unit job appears; an older low-priority job has waited 10 units. A declared age promotion at wait=10 makes it eligible for the next slot; unmodified strict priority continues postponing it.','Arrival and age log; moderate; online; known age; open stream.','The source explicitly adds aging to priority; batching alone does not set an age promotion. The finite trace verifies the promotion only, not every infinite stream.','good','/rso if capacity is below admitted demand; /enough if old work has become unnecessary'),
('U05','Equal service shares for resumable active consumers','A and B both have at least four units pending; q=1 alternates A,B,A,B and gives each two units in the first four.','Retained progress; simple; online; exact service units; two saturated consumers.','Round robin implements equal service directly; a whole-job FIFO lets one long request occupy the entire prefix.','excellent','/rso if each switch has cost; /lt if resumability is only an analogy'),
('U06','A declared 2:1 service entitlement','Two saturated consumers have weights 2 and 1. The repeated service cycle A,A,B allocates 4 and 2 units over six service units.','Fixed positive weights; moderate; online; known entitlement; two queues.','Weighted fair queuing represents both unequal priority and positive service, whereas strict priority can allocate the whole prefix to A.','good','/tobd if weights await a decision; /rso if service units consume unequal resource amounts'),
('U07','Category fairness despite unequal request counts','Category A supplies 100 one-unit items and B supplies one. Cycling categories serves B in the second unit; FIFO over all A arrivals first serves B at 101.','Category membership; moderate; immediate; known membership; 101 jobs in two categories.','The source permits item/category time slices, so the entitlement unit can be a category instead of one submitted record.','good','/de if categories have output prerequisites; /rso if category switches require setup'),
('U08','A valid ready frontier after prerequisite completion','D is ready only after A, while B is independent. After A completes, B and D have the same priority; FIFO or SJF can select within that now-valid frontier.','Completed dependency state; moderate; online; known graph; small workflow.','Queue discipline selects among eligible jobs after topology has done its different job; it does not rebuild the graph for each tie.','good','/to while dependencies still determine eligibility; /de if the dependencies have not been extracted'),
('U09','Prompt first service rather than earliest complete output','Checkpointable X=5,Y=3, q=1, both ready: Y first receives service at 1. Whole X-first service starts Y at 5. The declared response bound is one unit.','Resumable tasks; simple; urgent; exact durations; two jobs.','Round robin meets the stated first-service bound; shortest complete-job time and makespan are different criteria.','excellent','/td for a completion deadline instead; /enough if the response itself is already sufficient'),
('U10','Unknown sizes with a defensible arrival-order commitment','A,B,C arrived in that order and remaining sizes are not known. FIFO supplies a determinate next choice without a fictitious shortest-job ranking.','Arrival order only; simple; urgent; uncertain sizes; three jobs.','FIFO uses known inputs; SJF requires a missing quantity. This establishes a feasible tie policy, not minimum expected wait.','good','/tobd when acquiring sizes would change a consequential choice; /ecal when deciding the effort to estimate them'),
('U11','Equal entitlement to completed indivisible requests','X needs five consecutive units and Y three; interruption discards partial output. X 0–5 then Y 5–8 completes one request for each. q=1 produces no completion by 8.','Continuity requirement; simple; deliberate; exact reset rule; two requests.','FIFO over whole requests preserves the completion unit. Equal time allocation is not equal useful output in this stated case.','excellent','/rso when continuous blocks must fit a resource window; /lt when a target domain does not share the reset rule'),
('U12','Priority between classes and fairness inside the surviving class','A declared urgent finite request finishes first. Two remaining resumable routine categories then receive alternating slices; strict priority within routine work has no stated justification.','Two-level entitlement; moderate; online; known classes and resumability; one urgent plus two routine categories.','The queue mechanisms can be combined after the urgent obligation; a single global rank would discard the separate routine fairness requirement.','good','/td if repeated urgent arrivals have hard due dates; /rso if routine service capacity is then insufficient')
]
use_table='\n'.join('| '+' | '.join(row)+' |' for row in uses)

failures=[
('F01','q=1 time slicing of X=5,Y=3 whose partial output resets','Every visit is shorter than the required uninterrupted duration; the eight-unit trace has eight partial visits and zero valid completions.','Allocated time is positive while valid completion count stays zero.','/rso for contiguous-block feasibility; within /qs, whole-request FIFO once feasible.'),
('F02','SJF over ready jobs with a future urgent release','A: release0,duration4,deadline7; B: release1,duration2,deadline3. Starting A makes B finish6; reserving1–3 permits both. This is imported from qs-02, not a new discovery.','A ready-list ranking ignores the known future interval.','/td for the due interval and release-aware feasibility; /qs only after that guard.'),
('F03','Priority applied before a known prerequisite','The highest-priority output B needs completed A. B-first cannot consume its required input because A has not produced it.','The selected item has an unsatisfied incoming hard edge.','/to over the known graph before the queue tie choice.'),
('F04','A complete-looking queue whose inputs have never been enumerated','The queue contains analyze,write,export but export requires an unavailable converter. Ranking those words never produces the converter.','A task has no available producer for a necessary input.','/de to expose the external input, then /to; the queue is downstream.'),
('F05','Tiny fair slices with positive family setup occupancy','Four alternating one-unit visits with three one-unit switches consume seven elapsed units for four units of service. A zero-switch-cost prediction of four is false.','Switch intervals occupy the same processor.','/rso to compare batching and switching occupancy; retain /td if any due date binds.'),
('F06','Continuing an obsolete item because it is next','The requested output is an exact sum; the verified result already exists. A next-in-queue second derivation adds no required product.','The declared completion criterion is already satisfied.','/enough against that criterion; queue order cannot establish a need for more work.'),
('F07','A long queue-policy search for a reversible indifferent tie','Two independent one-unit temporary files are both needed, no due time differs, and either order is acceptable. Comparing twenty priorities does not change the resulting pair.','Every surviving choice meets the sole goal and can be reversed.','/ecal minimum-effort path for the selection decision.'),
('F08','Importing CPU slice behavior into human reading without a state mapping','The CPU example retains exact state at every pause. A human target has no measured restart behavior or continuity requirement. The CPU trace therefore supplies neither the human duration nor retention outcome.','Target resumption semantics are unstated rather than known.','/lt to map relations and test the missing target premise; no human benefit follows yet.'),
('F09','Assigning weighted shares before entitlement is resolved','A receives two slices and B one, but no actor has supplied a 2:1 entitlement. The arithmetic executes an unsupported preference.','The weight is an unresolved choice, not an input observation.','/tobd to resolve the entitlement dependency before weighted queuing.')
]
failure_table='\n'.join('| '+' | '.join(row)+' |' for row in failures)

pairs=[
('qs','td','Ready eligible requests have no binding due interval: choose their service discipline.','A known completion deadline or future release excludes an otherwise attractive queue order; temporal feasibility comes first.'),
('qs','rso','Service units resume without occupied switch intervals and the target is wait or entitlement.','Family changes consume two processor units, as in BOC01; compare setup occupancy before accepting a discipline.'),
('qs','to','The eligible ready set is already valid; choose between its competing requests.','Known A→B excludes B from the ready set even when B has higher priority.'),
('qs','de','Every selected task already has its required input.','A converter, authorization or producer is missing from the task description; extract that dependency before ranking.'),
('qs','ecal','The work is an ongoing queue with a supplied goal.','The open decision is how much effort a one-off indifferent queue choice warrants.'),
('qs','lt','The actual target has declared retained progress or reset behavior.','Resumable CPU service is only a proposed analogy for a different activity with unknown restart behavior.'),
('qs','enough','Several still-required products compete for service.','The acceptance criterion is already met and the issue is whether another queued item is needed.'),
('qs','tobd','Priorities, weights and resources are available inputs.','The entitlement weight or resource access decision remains unmade; order the needed resolutions.'),
('td','rso','Changing an order can violate a due time; retain deadline admissibility even if another order has fewer setups.','Every relevant due time is slack and occupied setup or bottleneck capacity controls the comparison. With both present, feasibility precedes resource optimization.'),
('td','to','A valid dependency order still needs actual start/finish positions relative to a deadline.','Only predecessor-before-successor validity is required and there is no duration or deadline objective.'),
('td','de','Durations, due times and required predecessors are known.','A supposed starting task needs an unlisted input; the temporal plan cannot be formed until that input relation exists.'),
('td','ecal','A schedule must place actual work before a known closing time.','The question is whether to spend two minutes or a longer effort budget selecting a schedule; timing arithmetic alone does not choose that budget.'),
('td','lt','The due time and nonpreemption relation are actual target inputs.','A source due-time example is being carried into a domain where the meaning of completion differs.'),
('td','enough','All listed deliverables remain mandatory and must fit before the closing time.','The candidate way to fit is dropping or stopping a deliverable; sufficiency must establish whether that changes the required result.'),
('td','tobd','The closing time is fixed and available.','Access duration and the decision to change location await answers that determine which deadlines exist.'),
('rso','to','Tasks without logical edges still share one mutable file or one occupied processor.','Separate resources are genuinely available and only hard task predecessors prevent parallel work.'),
('rso','de','Resource occupancy and all task inputs are known; calculate bottlenecks and setups.','The apparent resource problem is actually an unlisted producer/consumer input relation.'),
('rso','ecal','The object is the operating stream: service, switching and waits.','The object is the effort invested in choosing an optimization; another pass has no decision-changing result.'),
('rso','lt','The capacity, setup and reset semantics are specified for this target.','An engineering bottleneck is being treated as a person’s attention limit without a tested correspondence.'),
('rso','enough','Required tasks are fixed, so waste is occupied overhead around those tasks.','A proposed efficiency gain deletes a substantive required output; evaluate sufficiency before calling it waste.'),
('rso','tobd','The processor and current family are known, enabling the BOC setup calculation.','Availability of a second resource is unconfirmed and would remove the present bottleneck.'),
('to','de','The supplied graph already states each input dependency; generate a valid sequence.','The input contains only task names or ambiguous arrows; establish which output feeds which task first.'),
('to','ecal','The required graph has a meaningful readiness problem.','Two independent interchangeable tasks have no ordering consequence; the decision warrants only a minimal choice.'),
('to','lt','The dependency relation is native to the workflow and already established.','A chess or CPU ordering relation is being proposed for a different target; establish its mapping before sorting.'),
('to','enough','Every graph node is still part of the necessary output.','A whole subgraph is optional and the open question is whether the achieved result is sufficient without it.'),
('to','tobd','Nodes are executable tasks with settled specifications.','Nodes are unresolved decisions; one answer changes or eliminates the options of another.'),
('de','ecal','A missing prerequisite blocks an actual output, so its input/output relation must be found.','Nothing is blocked and the choice is an indifferent reversible tie; an exhaustive dependency inventory changes no action.'),
('de','lt','The work is within one workflow: identify which artifact or state a task consumes.','The work compares source and target relationships, including disanalogies between domains.'),
('de','enough','The question is what an unfinished task requires to start.','The question is whether the already-built result meets its purpose across breadth, depth, quality, validation and robustness.'),
('de','tobd','Task prerequisites are missing from the representation.','The unresolved decisions and their possible cascades are already the objects to be sequenced.'),
('ecal','lt','The transfer question is already definite and the pending choice concerns the effort budget.','The mapping itself is unsupported; a fast decision cannot supply missing correspondences or a target test.'),
('ecal','enough','No substantial analysis exists yet; choose an effort level from stakes and reversibility.','An existing analysis can be compared with its declared purpose and specific remaining gaps.'),
('ecal','tobd','One definite decision needs a proportionate effort level.','Several unresolved decisions constrain each other’s possible answers and need an operational resolution order.'),
('lt','enough','A source principle has not yet been validated in the new target; derive and test a transfer hypothesis.','The target application exists and the issue is whether its evidence covers the intended scope.'),
('lt','tobd','The correspondence between domains is the uncertain substantive relation.','The missing item is a supplied user rating, access decision or assigned choice; mapping cannot invent that external input.'),
('enough','tobd','A finished candidate is being compared with a fixed acceptance standard.','Specific missing decisions already prevent completion and must be assigned in an order that respects cascades.')
]
names=['qs','td','rso','to','de','ecal','lt','enough','tobd']
assert len(pairs)==36 and {frozenset(p[:2]) for p in pairs}=={frozenset(p) for p in itertools.combinations(names,2)}
pair_table='\n'.join(f'| /{a} ↔ /{b} | {left} | {right} |' for a,b,left,right in pairs)
(ROOT/'conditions-handoff-uf-switches.json').write_text(json.dumps({'target':'qs','alternatives':names[1:],'pairs':[{'left':a,'right':b,'left_when':left,'right_when':right} for a,b,left,right in pairs]},indent=2)+'\n')

uf_body=f'''TARGET: /qs, Queue Scheduling Orderings. Its operative choice is between FIFO, priority with aging, SJF, round robin and weighted fair queuing. CORE FUNCTION for this input: select a service discipline among eligible competing requests to express the declared wait, priority or entitlement objective. INPUT: release/arrival records, eligibility, service units, preemption semantics and the objective. OUTPUT: an executable service order plus the measure that can disconfirm its fit. No claim that /qs is universally superior to the eight alternatives is supported.

The exact target and all eight mapped alternatives were reloaded through the reader. conditions-handoff-reload-integrity.json records the emitted bytes, separate requirements and agreement with the existing originals. Alternative mappings below describe their source operations; they are not claimed as eight fresh standalone executions. The underlying source's unqualified optimization phrases are scoped here to the actual finite calculations. In particular, this record does not repeat the source's EDF optimality, universal SJF or human choice-overload claims as general facts.

| ID | Specific use case | Concrete consequence | Input, complexity, urgency, certainty, scale | Why this target fits the stated case | Fit | Alternative and switch |
|---|---|---|---|---|---|---|
{use_table}

| ID | Scoped bad application | Exact failure | Signal | Alternative route |
|---|---|---|---|---|
{failure_table}

F01 defeats the proposition “one-unit equal time slices complete at least one valid request in eight units for the declared reset-on-interruption X=5,Y=3 queue.” Every occupied visit has length one; neither reaches its required consecutive duration. Positive allocated service therefore does not imply a valid completed request. It does not defeat FIFO, all /qs operations, or round robin on resumable inputs. The alternative derived from this failure preserves each request until completion: X occupies 0–5, Y 5–8. Both valid outputs then exist. The strongest contrary route preserves progress across switches; that changed premise is tested separately below and restores the usefulness of time slicing.

LIMITS: a q-unit slice provides no completed indivisible request whose minimum valid contiguous duration exceeds q. If a switch occupies s units, the declared alternating n-visit trace occupies sum(service)+(n−1)s when every adjacent visit changes family; no universal acceptable ratio is supplied. A single-processor ordering cannot establish a multi-resource makespan until allocation and shared access are known. A finite four-visit fairness trace demonstrates that prefix, not an infinite-horizon starvation guarantee. Unknown job sizes prevent an exact SJF order; arrival-order selection remains possible without claiming minimum expected wait.

ANTI-PATTERNS: reporting allocated units as completed outputs hides F01; recording both quantities exposes it. Calling B “higher priority” does not remove A→B in F03; eligibility precedes queue choice. Copying a computed wait into an input with setup cost hides F05; occupied setup enters the timeline. Treating a known CPU checkpoint as a human memory observation hides F08; the missing target premise remains unresolved. Recounting F02 and the existing resource/dependency guards earns no new KEEP.

The eight alternatives are /td (temporal feasibility), /rso (resource occupancy), /to (valid order from established edges), /de (input/output dependency extraction), /ecal (effort allocation for a definite decision), /lt (source-to-target relation and test), /enough (purpose-relative sufficiency), and /tobd (operational order for unresolved decisions). The following comparison covers all 36 unordered pairs among target plus alternatives, with both directions stated. If both sides apply, the known hard prerequisite is retained rather than choosing away a constraint.

| Pair | First member when | Second member when |
|---|---|---|
{pair_table}

LATER USE U-L1 is the fresh X=5,Y=3 case saved before the comparator in conditions-handoff-inputs-before.json. The performed simulator records eight alternating visits A-style as X,Y,X,Y,X,Y,X,Y. Each gets four allocated units, but neither completes under reset-on-interruption. The whole-request trace records X 0–5 and Y 5–8: one valid completion per consumer. The selected route is whole-request FIFO because the declared entitlement concerns completed requests. It accepts unequal 5:3 occupied service for equal one-request completion. The comparison resolves a previously unsettled choice; it is not a repair of a fabricated prior belief that all slicing works.

LATER USE U-L2 retains the same durations but changes the declared progress rule and objective. With saved partial progress and first service required by time1, q=1 starts Y at1 and finishes Y at6, X at8. Whole-request X-first starts Y at5 and fails that first-service bound. The route now selects round robin. The opposite choice on this changed case preserves the continuity exception instead of converting the first result into a universal preference for long blocks.

LATER USE U-L3 is BOC01's separate four-job family setup input. The pair /qs↔/rso sends occupied family changes into its timelines, while /td↔/rso preserves every deadline. All 24 complete orders are compared there. The selected route changes from the initial earliest-deadline candidate to R1,B1,B2,R2 only under the base setup/deadline conditions. U-L3 is subsequent use of this map, not a second independent finding attributed to UF. The source/case-order arrangement and a one-line “fairness→round robin” arrangement were compared against U-L1/U-L2; the latter omits the reset rule and selects an invalid first route. The adopted record binds objective → continuity/eligibility → discipline → exact trace, and both later choices are saved in conditions-handoff-uf-later-use.json.

Certificate: the exact supported claim is that adding the declared continuity and output-unit distinction resolves the agent's discipline selection differently for U-L1 and U-L2. The eight-visit trace and whole-request trace establish the opposing completion results for U-L1; the retained-state trace establishes the first-response advantage for U-L2. The strongest contrary case is therefore retained as an actual switch condition. Unresolved dependencies are human reset behavior, open-stream arrival behavior, and any causal claim that this method improves durable learning; none is needed for the two finite route selections.'''

uf_body += '''\n\nReflection:\n- Expected: round robin would remain the fairness route across both two-request cases.\n- Observed: it yields equal occupied slices but zero valid outputs under reset-on-interruption; whole-request FIFO yields two valid completions. With retained progress and a first-service bound, the choice reverses.\n- Attribution boundary: the changed choice is the agent's finite model decision. No human preference, retention effect, or durable transfer was observed.\n- Remaining uncertainty: mixed continuity classes, positive switch cost with latency bounds, and open arrivals are untested.'''

put('uf-01','Resolve which queue discipline to use when fairness can mean equal occupied service or equal valid completed requests, then carry the distinction into a different setup case.',inputs['uf_starting_judgment'],uf_body,'The agent resolved the previously unsettled continuity case by selecting whole-request FIFO for discarded partial progress, and selected round robin for retained progress with a one-unit first-response bound. It added the output unit and continuity premise to its usable queue map.','The two performed traces support different usable choices: two valid completions replace zero in the indivisible case, while the resumable case preserves prompt first service. No observed person, durable learning or universal fairness improvement is claimed.','KEEP','The adopted objective → continuity/eligibility → discipline → trace arrangement keeps the exception that the name-only fairness mapping loses. It is used for both U-L1/U-L2 and the setup/deadline handoff to BOC01. Existing deadline and dependency distinctions remain imported, not new credits.','Test mixed resumable and indivisible requests; test a positive setup charge with a response bound; test a finite burst followed by continuing arrivals; obtain actual target resumption data before any human transfer claim.','Original UF 8x floors met: 12 typed use cases, 9 concrete failure cases, 8 exact-source alternatives, and both switch directions for all 36 pairs among target plus alternatives; limits, anti-patterns and three later uses supplied. Source floor concerns applicability coverage, not recursive heading count.',novelty='new_within_case',later_use='conditions-handoff-uf-later-use.json records opposing selected disciplines for fresh reset/retain cases; BOC01 uses setup/deadline switch conditions.')

rows=boc['base']['all_orders']
def match(r):return ' / '.join('✓' if x else '✗' for x in r['preference_matches'])
option_table='\n'.join(f"| {r['rank']} | {','.join(r['order'])} | {','.join(r['deadline_misses']) or 'none'} | {r['makespan']} | {r['mean_completion']:g} | {r['setup_occupancy']} | {match(r)} | {r['match_score']}/5 |" for r in rows)
feasible=[r for r in rows if r['admissible']]
later_table=[]
for n,r in enumerate(boc['later_cases'],1):
    chosen=r['all_orders'][0] if r['feasible_count'] else None
    condition=f"setup={r['setup']}"+(('; '+','.join(f"{j} deadline={d}" for j,d in r['deadline_override'].items())) if r['deadline_override'] else '')
    later_table.append(f"| B-L{n} | {condition} | {r['feasible_count']}/24 | {'; '.join(','.join(p) for p in r['best_orders']) or 'No admissible order'} | {str(chosen['makespan'])+', '+str(chosen['mean_completion']) if chosen else 'n/a'} |")
later_table='\n'.join(later_table)

boc_body=f'''INTERPRETATION: choice validation of the agent's initial scheduling candidate. CURRENT CHOICE: B1,R1,R2,B2. COMMITMENT: LEANING, not an executed human plan. Evidence is the starting record in conditions-handoff-inputs-before.json and the declared earliest-deadline order. Its known attraction is meeting all four deadlines. A global optimum and the threshold for switching are not known at that starting point.

Concrete input: R1 requires3 and is due8; R2 requires2 and is due14; B1 requires1 and is due6; B2 requires2 and is due18. All release at0. One nonpreemptive processor starts configured for R. Each family change occupies2 processor units. There are no dependencies, no added processors, no intentional idle and no release uncertainty. Units are scenario units, not measured minutes or human effort. The option space is every complete ordering of these four indivisible jobs under those assumptions: 4!=24. Arbitrary idle cannot improve any completion time when all jobs are available and no changeover becomes cheaper by waiting; removing such idle weakly advances every later completion. Changes to preemption, resource count or job contents are outside this finite category, not silently claimed absent from all imaginable solutions.

Preferences belong to this explicit analytical task. P1: meet every deadline (hard admissibility, STRONG). P2: minimize makespan within the admissible set (STRONG). P3: minimize mean completion among makespan ties (STRONG). P4: reduce occupied setup (STRONG, diagnostic here because fixed service sum links it to makespan). P5: use the declared capacity without intentional idle (STRONG). The initial choice supports an inference that deadline feasibility matters; it does not reveal a human preference for a particular waiting-time distribution. Emotional attachment, sunk cost, social pressure and ignorance of alternatives have no supporting evidence here and receive no invented diagnosis.

Common recognizable candidates include EDF B1,R1,R2,B2 and shortest-job B1,R2,B2,R1. Pure family batches include R1,R2,B1,B2 and B1,B2,R1,R2. Hybrid candidates split one family to protect a deadline while reducing later switches; R1,B1,B2,R2 and R1,B1,R2,B2 are in this class. The remaining permutations vary within-family and between-family order. Every one appears below. There is no factual basis for claiming which permutations the human user knows; the agent had not computed their relative results before this application.

The match columns instantiate P1–P5: P1 is deadline feasibility; P2 equals the best admissible makespan; P3 equals the best mean at that makespan; P4 equals the minimum admissible setup occupancy; P5 retains the declared no-idle single-processor resource arrangement. A ✓ is an exact match, not a probability. Infeasible rows cannot win by score. Rank first separates feasible from infeasible, then applies the declared makespan/mean/setup order. Ranks among infeasible options only keep the record inspectable; they are not recommendations.

| Rank | Complete option | Missed deadlines | Makespan | Mean completion | Setup occupancy | P1 / P2 / P3 / P4 / P5 | Match |
|---|---|---|---|---|---|---|---|
{option_table}

The current candidate has timeline setupR→B 0–2; B1 2–3; setupB→R 3–5; R1 5–8; R2 8–10; setupR→B 10–12; B2 12–14. It is admissible, makespan14, mean completion8.75 and occupied setup6. Its match is2/5. The top option R1,B1,B2,R2 has R1 0–3; setupR→B 3–5; B1 5–6; B2 6–8; setupB→R 8–10; R2 10–12. Its completions 3,6,8,12 meet due times 8,6,18,14; makespan12, mean7.25 and setup4 give5/5. The second admissible alternative R1,B1,R2,B2 has makespan14 and mean8.75, tying the current choice on the declared criteria. It moves who finishes first; no unstated distributional preference breaks that tie. Consequently exactly one option ranks substantively above the current choice. There are two alternatives to present, not a fabricated third.

WHY THE INITIAL CANDIDATE IS SUBOPTIMAL HERE: its EDF order includes three family changes. The comparison establishes an admissible two-change order that completes the same four jobs and reduces both makespan and mean completion. The evidence supports incomplete option comparison in the agent's initial state; it does not establish a psychological bias. Whole-family R1,R2,B1,B2 finishes in10 but makes B1 finish8>6. Thus “batch all similar work” is not the retained result. The result is a specific admissible split-family order. The strongest reason to prefer the initial candidate is an unmodeled desire for B1 at3 instead of6; the supplied deadline requires only≤6. If first-response utility, uncertainty buffer or a tighter B1 deadline is actually required, the declared objective changes and the choice must be reopened.

BEFORE COMMITTING: prioritized alternative1 is R1,B1,B2,R2, because it preserves all specified deadlines and improves the two declared efficiency criteria. Alternative2 is the tied feasible R1,B1,R2,B2, retained as a distributional comparison but not called better. The current choice sacrifices two units of makespan,1.5 units of mean completion and two units of setup relative to alternative1. Initial recommendation: EXPLORE_ALTERNATIVES through the original required /cta verification of these candidates; a numerical rank is not a feasibility certificate.

/cta dependency, CATEGORY: feasibility and fit of candidate service orders; TYPE: METHOD with explicit CONSTRAINT checks. GUESS C1: R1,B1,B2,R2 is executable with every required input and deadline. Observable implication1 is exactly one completed occurrence of each job with durations3,1,2,2. Implication2 is two occupied changes of2 and no overlapping intervals. Counter-evidence would be any missing job, wrong duration, shared interval, pre-release start or finish after its due time. The saved timeline contains all four jobs exactly once, occupied intervals0–12 without overlap, and finish values3≤8,6≤6,8≤18,12≤14. VERDICT: LIKELY, HIGH confidence within the declared exact inputs; verified as finite arithmetic. No measured execution time or external resource observation is inferred.

GUESS C2: R1,B1,R2,B2 fits the same resources and deadlines. Its four completions are3,6,10,16? That trial completion is wrong: after R1 0–3, change3–5, B1 5–6, change6–8, R2 8–10, change10–12, B2 12–14, the final completion is14. The corrected exact list is3,6,10,14 and mean8.25, as the saved exhaustive result shows. The initial prose tie claim above must be compared against this exact output; the actual score and ranking below are derived from the saved rows. This explicit check prevents an attractive summary from substituting for its operands.

GUESS C3: pure R-family batching R1,R2,B1,B2 meets all deadlines. Its B1 completion8 exceeds6, so the guess is UNLIKELY, HIGH confidence; this candidate is eliminated despite its lower makespan10. Constraints: one processor exists by construction, nonpreemption is absolute within the category, family setup is2, deadlines are absolute, and job durations are exact declared inputs. Resources and prerequisites for C1/C2 are met in the model; they have not been observed in a real service setting. Preference fit is ranked by the explicit task objective above, not a /pre profile supposedly obtained from the user.

Clusters: C1 and C2 both place R1 before B1 and meet the zero-slack B1 completion6; their completion6 is supported by the common R1→change→B1 prefix. C1 keeps B1/B2 adjacent, reducing a change that C2 still incurs. C3 violates the same B1 bound because it adds R2 before that prefix finishes. Discriminating questions, answered from the input: Is interruption allowed? No; a preemptive option therefore leaves this category. Is the B1 due time6 or5? The base input says6; the5 variant is executed later. Is setup2 or3? It is2 in the base,3 in B-L3. These are concrete options with different conclusions, not unknown human guesses. No UNKNOWN guess with unresolved preference options remains in this finite dependency, so the /pre trigger does not fire.

The /cta better-option trigger returns to /boc with C1 as the revised current choice. The same complete 24-option category, stated preference profile, match scores, suboptimality checks and retained exceptions remain its inputs. No option outranks C1 in the admissible set. Second /boc recommendation: PROCEED with C1 in the base finite case. This closes the BOC→CTA→BOC dependency without inventing a new option category or treating the first recommendation as final.

LATER USE: the executable comparison is actually rerun on five changed inputs below. Results are in conditions-handoff-boc-results.json; every later case again enumerates24 complete permutations. The selected option is changed to each reported optimum, or withheld when no admissible order exists. These are performed model computations, not promises to test later.

| Later case | Changed condition | Admissible orders | Selected order(s) | Makespan, mean completion |
|---|---|---|---|---|
{later_table}

The setup0 case admits shortest-duration orderings with makespan8, mean4.25; the two equal-duration middle jobs can exchange places. At setup1, B1,B2,R1,R2 becomes the selected order. At setup3, no ordering can meet all base deadlines: all24 fail, so the record returns infeasible rather than adding an unapproved second processor. At B1 deadline5, the original EDF choice is the only admissible order. At R2 deadline9, no order is admissible. These cases refute a context-free claim that the base C1 order is always better and exhibit actual switches in allocation and verdict.

Organization comparison: source order/EDF names make it easy to retrieve the initial candidate but hide occupied setup; a score-only table also permits an infeasible low-makespan batch to look attractive. The adopted view places input version → hard admissibility → exact timeline → ordered metrics → invalidation condition. It is used in all five later calculations: the tighter B1 case restores EDF and both infeasible cases retain failure. The complete24-row audit remains available while the recommendation presents only the genuinely better candidate and a meaningful surviving comparison.

Certificate: exact claim—under the base declared four-job model and lexicographic task preferences, C1 is better than the original current choice. Decisive evidence—both meet every deadline, while C1 has makespan12<14 and mean7.25<8.75. Inference—the hard condition is retained and the first soft criterion improves, so the preference order selects C1. Strongest contrary branch—B1 first completion at3 is earlier in the current order; it matters only if a new utility/buffer/deadline condition is supplied, and the supplied deadline5 countercase actually restores the current order. Remaining dependency—real durations, setup uncertainty and human preferences are unmeasured and cannot inherit this result.'''

boc_body += '''\n\nReflection:\n- Expected: the feasible earliest-deadline candidate might remain preferred after setup was included.\n- Observed: exhaustive base enumeration selected R1,B1,B2,R2, while changed setup/deadline inputs selected different orders or no admissible order.\n- Attribution boundary: these are arithmetic consequences of the declared model and agent-authored objective, not observed human scheduling outcomes.\n- Remaining uncertainty: measured durations, stochastic setup, alternate capacity, preemption, and the user's actual trade-offs are unavailable.'''

# Correct the drafted C2 paragraphs from actual inspected arithmetic before delivery.
c2=next(r for r in rows if r['order']==['R1','B1','R2','B2'])
boc_body=boc_body.replace('The second admissible alternative R1,B1,R2,B2 has makespan14 and mean8.75, tying the current choice on the declared criteria. It moves who finishes first; no unstated distributional preference breaks that tie. Consequently exactly one option ranks substantively above the current choice. There are two alternatives to present, not a fabricated third.',f"The second admissible alternative R1,B1,R2,B2 has makespan{c2['makespan']} and mean{c2['mean_completion']:g}. It improves mean completion from8.75 to8.25 while tying makespan14 and setup6; it therefore also ranks above the current choice, although C1 still wins on makespan. Exactly two options rank substantively above the current choice, so there are two alternatives to present, not a fabricated third.")
boc_body=boc_body.replace('Alternative2 is the tied feasible R1,B1,R2,B2, retained as a distributional comparison but not called better.','Alternative2 is R1,B1,R2,B2, which preserves makespan14 and improves mean completion by0.5. It ranks second because C1 also improves makespan.')
start=boc_body.index('GUESS C2:');end=boc_body.index('\n\nGUESS C3:',start)
boc_body=boc_body[:start]+'''GUESS C2: R1,B1,R2,B2 fits the same resources and deadlines and improves the original mean completion. Its timeline is R1 0–3, change3–5, B1 5–6, change6–8, R2 8–10, change10–12, B2 12–14. Completions3,6,10,14 give mean8.25, while all four deadlines remain met. Counter-evidence would be a missed deadline or a mean at least8.75; neither occurs in this declared timeline. VERDICT: LIKELY, HIGH confidence within the exact input, verified as finite arithmetic. C2 is a better alternative to the initial choice and ranks below C1 because makespan14 exceeds12.''' +boc_body[end:]

put('boc-01','Change a feasible initial queue choice only if a complete option comparison supplies a better admissible setup schedule, then discover conditions that reverse or eliminate that choice.',inputs['boc_starting_judgment'],boc_body,'The agent replaced its initial EDF candidate with R1,B1,B2,R2 for the base case, then changed the selected ordering at setup0/setup1, restored EDF for a tighter B1 deadline and withheld a schedule for two infeasible later variants.','The base model preserves every deadline and reduces makespan14→12 and mean completion8.75→7.25. Later computations retain the exact conditions under which that gain disappears. Benefits are calculated consequences in a constructed model, not measured human performance or a causal attribution to durable learning.','KEEP','Input version → hard admissibility → exact timeline → ordered metrics → invalidation condition is used for five later comparisons. The full24-option record supplies provenance; the short recommendation contains only the two actually better alternatives.','Add uncertain setup intervals; allow a real preemption rule and compare the enlarged space; change the objective to first-response latency; supply an actual service dataset before attributing operational benefit.','No numerical BOC 8x floor exists. Its 20+ option floor is met by the complete24-permutation base space; all scored. Original BOC→CTA→BOC conditional dependencies are executed distinctly on the actual better candidates; five later inputs each enumerate24 orders. CTA has no numerical8x floor and no unresolved preference guess requiring /pre.',novelty='new_within_case',later_use='conditions-handoff-boc-results.json records five performed changed-input comparisons, including two infeasible outcomes and restoration of the original EDF choice.')

# ADEP pre-calibration work: inventory and read the available local sample without
# fabricating Phase 0 answers or any triage scores.
import hashlib
conditions_root=ROOT.parent/'conditions'
conditions_ledger=json.loads((conditions_root/'application-ledger.json').read_text())
sample=[]
for row in conditions_ledger:
    file_name=Path(row['file']).name
    local_path=conditions_root/file_name
    content=local_path.read_text()
    excerpt=content[:2000]
    sample.append({
        'skill_id':row['skill_id'],
        'application_number':row['application_number'],
        'file':f'../conditions/{file_name}',
        'status':row['status'],
        'verdict':row['verdict'],
        'novelty':row['novelty'],
        'content_characters':len(content),
        'sample_span':'first 2000 characters' if len(content)>=2000 else 'entire file',
        'sample_characters':len(excerpt),
        'sample_sha256':hashlib.sha256(excerpt.encode()).hexdigest()
    })
manifest={
    'purpose':'ADEP Phase 1 available-source inventory and content-sample receipt; not a calibrated triage or ranking',
    'actor':'methods utility/options handoff agent',
    'collection':'conditions application records present in this handoff workspace',
    'available_items':len(sample),
    'target_items_approximately':100,
    'target_met':len(sample)>=90,
    'distinct_skill_ids':sorted({r['skill_id'] for r in sample}),
    'content_types':['reasoning application Markdown'],
    'items':sample
}
(ROOT/'conditions-handoff-adep-sample-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')

adep_body='''PHASE 0 — extraction profile. The original four question groups are preserved exactly as gates: weighting among procedure density, uniqueness, direct relevance or balance; preferred procedure types; current priority domains; and the skip threshold. The required `question_generation` dependency was requested through the original reader and returned `filename 'skills/question_generation/SKILL.md' not found`. No response from the human user is present. Therefore no weighting mode, procedure-type preference, priority domain or skip threshold is selected. The default-looking “balanced” formula is one allowed answer, not permission to impute that answer to this user.

PHASE 1 — available broad sample. The local conditions ledger names 50 application records across 25 skill IDs. Every named local Markdown file exists. The first 2,000 characters of each item (or its entire text if shorter) were read; `conditions-handoff-adep-sample-manifest.json` records the item identity, status, verdict, full character count, sampled character count and sample hash. The available set has 33 complete, 16 partial and one blocked record; its recorded verdicts are 24 KEEP, eight REJECT and 18 UNRESOLVED. Those labels describe the existing research records and are not extraction-value ratings.

The original Phase 1 target is approximately 100 items mixed across sources, content types and topics. This set has 50 items, one content type and one research line, so it is a half-size convenience census, not the required broad calibration sample. Adding consolidation or state files merely to reach a count would duplicate derived material and would not create source diversity.

STEP 3 / INITIAL TRIAGE — exact gate. Density, uniqueness and relevance require substantive 1–5 judgments; relevance also depends on the unanswered priority-domain question, and the composite weights depend on the unanswered weighting question. Expected-procedure estimates are likewise absent. Consequently there are no item scores, composite values or ranking. Existing KEEP/REJECT verdicts are not substituted: a useful mind-change application can be sparse in extractable procedures, and a rejected application can still expose a reusable failure case.

STEPS 4–5 / USER RATINGS AND CALIBRATION — exact gate. No randomized set of approximately 20 items has been presented to the user, no 1–10 extraction-value ratings exist, and no prediction/user pairs exist. Pearson correlation is therefore undefined, not zero and not “below 0.7.” There is no supported bias adjustment or calibrated model.

STEPS 6–9 / DOWNSTREAM GATES. Scaling to all sources requires a calibrated model plus complete Tier 1–3 source lists and samples; none is present. Target selection requires the resulting global ranking and a supplied extraction budget; neither exists. Phase 3 three-pass extraction requires selected targets. Yield monitoring requires actual extracted procedures and predictions. Evolution requires prediction-versus-yield observations. Each stage remains unexecuted rather than being simulated from this corpus.

Executable endpoint: the available pre-calibration endpoint is the 50-item identity/content-sample manifest and the frozen unanswered profile questions. The next executable operation requires (1) an available exact `question_generation` procedure or direct human answers to the four question groups and (2) roughly 50 additional source-diverse items with content samples. Triage can then score all approximately 100 items. The later gates are sequential: user rates a randomized approximately-20 subset → correlation and divergence analysis → adjust and rerun if below 0.7 or accept if at least 0.7 → full-source triage → budgeted queue → selective extraction → yield-based update.

Certificate: the exact supported claim is that only inventory and sampling, not triage or calibration, are executable from the supplied artifacts. The 50 verified files establish an available half-size sample. Missing profile answers prevent relevance weights and skip rules; missing user ratings prevent calibration. A contrary proposal to use existing verdicts as ratings changes the measured construct from extraction value to application disposition and is rejected. Remaining dependencies are the original question-generation operation or direct answers, diverse additional sources, human ratings, budget, and actual yield.

Reflection:
- Expected: an initial triage might be possible from the frozen portfolio alone.
- Observed: the portfolio supports a verified 50-item sample manifest, but not the required profile-dependent scores or approximately-100-item diverse calibration set.
- Attribution boundary: the only changed state is the agent's readiness assessment and the new sample manifest; no user preference, calibration, extraction quality, or learning effect was observed.
- Remaining uncertainty: all ranking quality and downstream return-on-extraction claims remain unresolved.'''

adep_missing=[
    'question_generation original dependency unavailable and Phase 0 human answers absent',
    'approximately 100-item source-diverse sample not available; 50 single-type local records sampled',
    'initial triage scores and composite ranking unavailable because profile weights/domains and item judgments are absent',
    'approximately 20 actual user extraction-value ratings unavailable',
    'calibration correlation/divergence analysis unavailable',
    'calibrated full-source triage, budgeted target queue, selective extraction, actual yield, and model evolution unavailable'
]
put('adep-01','Determine the furthest defensible point of the adaptive extraction pipeline from the supplied corpus, without turning portfolio labels into user extraction ratings.',inputs['adep_starting_judgment'],adep_body,'The agent withdrew its tentative expectation that it could build an initial triage from this portfolio. It established a 50-item content-sample manifest and an exact dependency chain, but retained every preference-dependent and calibrated stage as unavailable.','The manifest makes the next input gap inspectable and prevents existing KEEP/REJECT labels from being misused as extraction-value ratings. No extraction ROI, ranking quality, user learning, or calibrated prediction benefit is claimed.','UNRESOLVED','Profile questions → diverse sample → triage → randomized human ratings → calibration gate → scaled ranking → extraction queue → actual yield is retained as the source sequence. The manifest supplies provenance for the only executed data step; downstream sections name their exact gates.','Obtain direct answers to the four Phase 0 question groups or restore the exact question_generation dependency; add roughly 50 source-diverse items and samples; then perform triage, collect approximately 20 randomized user ratings and calculate Pearson correlation before any scaled ranking.','ADEP defines no numerical 8x floor. Phase 0 questions are frozen but unanswered; Phase 1 is partial with 50 locally available single-type items sampled against an approximately-100 diverse target; every later phase is gated explicitly.',status='partial',missing=adep_missing,novelty='unresolved',later_use='No calibrated later use exists. Next executable gate is direct Phase 0 answers or the missing question_generation dependency plus a source-diverse sample expansion.')

results=json.loads((ROOT/'conditions-handoff-results.json').read_text())
owned=[r for r in results if r['skill_id'] in {'uf','boc','adep'}]
assert len(owned)==3
proposal={
    'owner':'methods utility/options handoff',
    'base_ledger':'../methods/application-ledger.json (read-only; root integration required)',
    'slots':owned,
    'changed_files':[
        'methods/uf-01.md',
        'methods/boc-01.md',
        'methods/adep-01.md',
        'methods/conditions-handoff-uf-switches.json',
        'methods/conditions-handoff-adep-sample-manifest.json',
        'methods/conditions-handoff-boc-results.json',
        'methods/conditions-handoff-uf-later-use.json',
        'methods/conditions-handoff-results.json',
        'methods/conditions-handoff-evaluate.py',
        'methods/conditions-handoff-write.py',
        'methods/conditions-handoff-write-resume.py',
        'continuation/utility-proposal.json'
    ],
    'integration_instruction':'Root must semantically review these records and apply accepted slot metadata; this proposal does not mutate any ledger, progress, index, or run-state file.'
}
(ROOT.parent/'continuation'/'utility-proposal.json').write_text(json.dumps(proposal,indent=2)+'\n')

print('UF, BOC, and partial ADEP written; C2 inspected:',c2['mean_completion'])
