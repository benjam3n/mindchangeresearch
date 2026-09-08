**Subject Systems, Perspective Optimizer, and recursive self-improvement**

Research and repository assessment, 8 September 2026.

**The current implementations are insufficient for autonomous recursive self-improvement. Their central idea is compatible with it, and there is now direct empirical precedent for improving an agent’s improvement procedure.** What remains unestablished is whether these particular projects make a capable model better at discovering, validating, retaining, and producing further improvements across unfamiliar cases.

The important transition is from an improved answer or repository entry to an improved cause of future work. A perspective that helps resolve one question provides a local benefit. A retained operation that helps discover useful perspectives provides a reusable capability. A retained change that makes the system better at discovering and testing those operations provides the recursive benefit you are seeking.

This assessment concerns the present implementations, their intended architecture, and the evidence required to establish the stronger capability. It does not treat a complete theory of perspectives as a prerequisite for beginning. It also does not treat an instruction to improve, an expanding inventory, or a successful demonstration as proof that the capability exists.

| Claim | Assessment |
| --- | --- |
| The two repositories currently run an autonomous recursive improvement process | No. The inspected executable paths do not close that loop. |
| Their existing distinctions and operations can support such a process | Yes. Several directly address the relevant failure conditions. |
| A frozen language model rules out meaningful recursive improvement of the surrounding system | No. The surrounding programs, instructions, memory, and improvement procedures can change. |
| A complete subject inventory would itself make the system sufficient | No. Describing the required work does not cause it to occur correctly. |
| Bounded recursive improvement is a credible development target | Yes, supported by relevant experimental precedents. It still requires a demonstration in these projects. |
| Reliable transfer across arbitrary subjects has been established | No. Neither the repositories nor the reviewed studies establish that universal claim. |
| Recursive improvement implies accelerating or unlimited improvement | No. Recursive benefit can be small, costly, intermittent, or eventually exhausted. |
| These repositories are necessary for recursive improvement in general | No. Other implementations demonstrate relevant mechanisms without this ontology. Their specific contribution needs an ablation against a strong alternative. |

**The assessment uses the latest repository versions available when the inspection began.**

Subject Systems was inspected at [8605d44181fab127087ba27c60448f24cdc3b1c7](https://github.com/benjam3n/subjectsystems/tree/8605d44181fab127087ba27c60448f24cdc3b1c7), committed on 8 September 2026. Perspective Optimizer was inspected at [7277935d3e9267b6103f7188ed65a95a3f0dc6c2](https://github.com/benjam3n/perspectiveoptimizer/tree/7277935d3e9267b6103f7188ed65a95a3f0dc6c2), also committed on 8 September.

Both complete repository trees were retrieved. A working snapshot of 145 files—80 from Perspective Optimizer and 65 selected Subject Systems files—was checked byte for byte against the corresponding Git blob identities. The Subject Systems construction script and the preserved source involved in a replay failure were also inspected. This was a focused implementation and sufficiency assessment, not a semantic validation of all 471 subject definitions.

The earlier Repository Construction Design, Perspective Structure and Process 001, and Contribution Selection Study 001 were consulted for the intended mechanism and prior experiments. Their descriptions of older versions were not treated as evidence of current code behavior. The public research review includes primary papers through August 2026. Published model experiments were examined, not independently rerun here.

**Several useful components already exist.**

The current Subject Systems catalog has 471 subjects. Perspective Optimizer contains 60 perspective patterns and imports subject bindings pinned to the exact Subject Systems commit above. Its definitions distinguish a configuration’s existence, activation, enactment, modification, retention, and transfer. These distinctions matter because a system can possess a description without using it, use an operation once without retaining it, or retain a rule that damages a new case. [Subject catalog](https://github.com/benjam3n/subjectsystems/blob/8605d44181fab127087ba27c60448f24cdc3b1c7/subjects/catalog.json), [theory manifest](https://github.com/benjam3n/perspectiveoptimizer/blob/7277935d3e9267b6103f7188ed65a95a3f0dc6c2/sources/theory-manifest.json), [perspective operations](https://github.com/benjam3n/perspectiveoptimizer/blob/7277935d3e9267b6103f7188ed65a95a3f0dc6c2/perspective/operation.md).

Subject Systems also already specifies that improvement requires a baseline, relevant comparison conditions, attention to costs, and a distinction between a favorable selection and established benefit. Its improvement system explicitly allows reconsidering an inadequate criterion while preserving what changed in the comparison. These are substantive ingredients, not merely missing items to add to a checklist. [Improvement candidate revision](https://github.com/benjam3n/subjectsystems/blob/8605d44181fab127087ba27c60448f24cdc3b1c7/systems/improvement-candidate-revision.md).

The main executable capabilities are narrower:

| Existing component | What it actually supplies | What it leaves to another process |
| --- | --- | --- |
| Subject identities, targets, exclusions, and relations | A stable vocabulary for identifying different determinations | Recognizing which determination matters now |
| Subject-specific systems and method descriptions | Explicit operations that a model or person can attempt | Reliable selection, execution, and assessment across cases |
| Finite candidate generation | Enumeration of supplied finite domains | Discovery of the domains and relevant omitted distinctions |
| Boolean inference checking | Exhaustive validity checks for supplied formulas within bounds | Justifying the translation from a real question into those formulas |
| Required-condition assessment | Distinguishes achieved, failed, and unresolved supplied conditions | Establishing whether the actual conditions hold |
| Perspective space expansion | Adds a supplied value or dimension and enumerates its consequences structurally | Establishing semantic novelty or usefulness |
| Conditional study routing | Reports which authored route conditions are satisfied, contradicted, or unknown | Discovering the route, collecting observations, or conducting the study |
| Transition reachability | Finds paths through declared transitions under fixed observation meanings | Implementing and successfully performing those transitions |
| Candidate execution and comparison | Executes seven registered operations and checks specified results | Constructing a new operation, adequate criterion, or improvement experiment |
| Pinned source records and generated results | Preserve identities and some reproducible findings | Selecting and activating those findings in later model runs |
| Self-improvement controller | No complete controller found in the inspected executable paths | The recurring connection from experience to an adopted improvement to a better next improvement |

The seven registered core operations are projection, row selection, descriptive rates, group composition, Cartesian enumeration, threshold branching, and required-condition assessment. They are useful finite tools. Their registry is not an implementation of arbitrary perspective construction or a model-driven learning process. The broader operation descriptions can be enacted by a capable model, but that enactment is an additional causal component. [Execution kernel](https://github.com/benjam3n/perspectiveoptimizer/blob/7277935d3e9267b6103f7188ed65a95a3f0dc6c2/perspectiveoptimizer/core.py), [construction and routing module](https://github.com/benjam3n/perspectiveoptimizer/blob/7277935d3e9267b6103f7188ed65a95a3f0dc6c2/perspectiveoptimizer/space.py), [finite study methods](https://github.com/benjam3n/subjectsystems/blob/8605d44181fab127087ba27c60448f24cdc3b1c7/tools/study_methods.py).

**The executed checks establish a clear boundary between working components and demonstrated improvement.**

Perspective Optimizer’s existing suite passed all 16 tests. Its checker passed 78 local links, 60 perspective patterns, and 471 pinned subject bindings. Those tests cover meaningful properties such as preserving unknown observations, retaining exclusions, rejecting undeclared references, respecting execution bounds, and avoiding contradictory conditional paths. They do not compare independent model runs or measure improvement of the improvement procedure.

Three additional probes were run against the pinned code:

| Probe | Observed result | What the result establishes |
| --- | --- | --- |
| Add a punctuation dimension whose own description says the interpretation, operation, and outcome do not change | Accepted; assignments increased from 12 to 24 | The expansion function checks structure and recorded contrasts, not actual contribution |
| Declare a transition from “initial” to “improved” with an operation that has no implementation | “Improved” is reachable in the declared graph | Symbolic reachability is not actual ability to produce the transition |
| Recompare the two current assessment interfaces across all 54 declared combinations | Direct native input rejected 54 times; truthiness changed 18 statuses; exact conversion preserved all 54 statuses and complete assessments | Correct translation is a real, scoped contribution; it is not yet autonomously learned or generalized |

The first two results are consistent with the functions’ stated scope. They are not evidence that the finite algorithms malfunction. They show why those algorithms cannot serve as evidence that a proposed perspective is useful or that a named improvement operation has been performed.

The interface experiment uses two required observations, one optional observation, and an abandonment flag. Each observation has three states and the flag has two: 3 × 3 × 3 × 2 = 54. The reference results are 6 achieved, 30 not achieved, and 18 undetermined. This is complete coverage of that declared finite domain, not a statistical estimate of general reliability.

A separate, actual reproducibility defect was found in Subject Systems. The current study runner reads:

~~~python
gate = (D/'sources/gosm_outcome.txt').read_text()
~~~

Here D is the studies/system directory. The complete commit tree contains no file at that requested path. The preserved file is at sources/studies/gosm_outcome.txt. Running the current script raised FileNotFoundError. In a temporary copy, changing the reference to:

~~~python
gate = (R/'sources/studies/gosm_outcome.txt').read_text()
~~~

restored the existing run: 54 achievement cases, six inference cases, the source-rule gap, order dependence, support preservation, and three input-boundary checks completed successfully. This temporary repair was verified without changing either remote repository. [Current study runner](https://github.com/benjam3n/subjectsystems/blob/8605d44181fab127087ba27c60448f24cdc3b1c7/tools/run_study_cases.py), [preserved source](https://github.com/benjam3n/subjectsystems/blob/8605d44181fab127087ba27c60448f24cdc3b1c7/sources/studies/gosm_outcome.txt).

The defect is locally simple. Its relevance is larger: improving repository presentation can break the machinery that reestablishes earlier findings. Recursive improvement needs to detect such losses because they can silently weaken the next improvement cycle.

**The strongest version of the idea concerns the system’s ability to change what it can recognize and do next.**

The current general definition treats a perspective as a configuration through which specified differences become consequential for an entity or interaction. Under that definition, the relevant bearer can be the whole model–program–memory–environment arrangement. There is no need to locate improvement exclusively inside neural weights, conscious reflection, or verbal self-description. [Perspective definition](https://github.com/benjam3n/subjectsystems/blob/8605d44181fab127087ba27c60448f24cdc3b1c7/studies/perspective/definition.md).

For your projects, a useful change could alter:

- Which conditions the system notices.
- Which question it investigates.
- Which subject’s result it recognizes as relevant.
- Which representations or distinctions it constructs.
- Which operations it can perform.
- Which outcomes would change its next action.
- Which evidence it obtains.
- Which earlier findings it can retrieve and use.
- Which failures it attributes to the task, method, representation, evaluator, or environment.
- How it allocates effort among exploitation, alternatives, verification, and further learning.

Some of these changes can directly improve the process that generates later changes. For example, discovering that apparently different failures share an information-loss mechanism can improve future diagnosis, test generation, and memory compression. That is a plausible route to recursive benefit even when the initial discovery concerns an ordinary task.

The important empirical question is whether the discovered relation becomes an operative change. A new explanation may remain inert. A changed prompt may be ignored. A revised code path may never be called. An accurate memory may be retrieved in the wrong circumstances. Each is a different failure requiring a different intervention.

**The projects’ own subjects provide a sharper sufficiency test than a generic feature inventory.**

| Existing subject | Application to this assessment |
| --- | --- |
| System identity specification | Distinguish the repositories from the complete running model–tool–memory system |
| System composition description sufficiency | Ask whether two implementations can satisfy the same description while differing in recursive improvement |
| System implementation correspondence | Identify which described operations actually run |
| Perspective adoption correspondence | Compare declared improvement principles with observable choices and operations |
| Discovery contribution dependence | Identify which earlier discovery enabled a later improvement |
| Perspective candidate dimension construction | Require an omitted consequential distinction to become available |
| Perspective result interpretation rule | Check whether different results produce appropriate different continuations |
| Learning correction uptake | Determine whether a correction changes the next applicable conduct |
| Learning correction overgeneralization | Include cases where the learned correction should not be used |
| Improvement effect attribution | Separate gains from extra computation, new information, stronger models, or human intervention |
| Perspective improvement retention | Test persistence across a fresh run or interruption |
| Perspective improvement transfer | Test benefit under changed task conditions |
| Criterion modification and Criterion justification | Permit justified changes to evaluation while examining their grounds |
| Intelligence regression | Detect losses of previously demonstrated adaptive ability |

These are exact subjects in the current catalog. Applying them leads to a specific result: the projects contain many of the determinations needed to investigate recursive improvement, but the existence of those determinations does not establish a successful implementation of them. [Subject catalog](https://github.com/benjam3n/subjectsystems/blob/8605d44181fab127087ba27c60448f24cdc3b1c7/subjects/catalog.json).

A counterexample makes the point. Two systems could possess the same complete subject catalog, the same perspective patterns, and the same written improvement procedure. One retains a newly established distinction only as an unused note. The other inserts the distinction into its future proposal and evaluation behavior. Their inventories match; their later capabilities differ. Therefore inventory completeness is not sufficient for the required property.

A second counterexample concerns perfect selection within an incomplete construction. A flawless selector cannot choose an effective operation absent from its candidates. More exhaustive enumeration within the original dimensions does not necessarily expose the missing dimension. The current punctuation probe additionally shows that a larger space can add no useful distinction at all.

**Published results support several parts of the mechanism, with materially different strengths.**

The following are primary research findings. Their implications for these projects are my assessment, not claims made by the authors about Subject Systems or Perspective Optimizer.

| Research | Relevant result | Implication and limit |
| --- | --- | --- |
| STOP, COLM 2024 | A language-model-assisted program improver was applied to itself; an evolved improver transferred to five other downstream tasks. Results depended on the base model and were not uniformly monotonic. | Direct precedent for improving an improver. Its limited domains, finite runs, and unchanged language model do not establish unrestricted improvement. [Paper](https://arxiv.org/pdf/2310.02304) |
| Darwin Gödel Machine, 2025; revised March 2026 | Agents modified their own coding machinery while an archive preserved alternative lineages; reported coding scores rose substantially. | Supports persistent agent-level self-modification. Coding-task improvement is used as a proxy for self-modification ability, and some directing machinery remains fixed. [Paper](https://arxiv.org/html/2505.22954v3) |
| Hyperagents, 2026 | Task and improvement procedures share an editable program. Experiments examine improvement-procedure transfer across domains and continued improvement. | The closest precedent for your desired recursion. It directly tests more than ordinary task performance, while retaining fixed parts of the outer experiment. [Paper](https://arxiv.org/html/2603.19461v1) |
| GEPA, ICLR 2026 | Reflective prompt mutation and selection from complementary candidates improve held-out task performance. | Natural-language operations can be a real adaptation mechanism. Optimizing task prompts with a fixed optimizer does not by itself demonstrate an improving optimizer. [Paper](https://arxiv.org/pdf/2507.19457) |
| A Self-Improving Coding Agent, 2025 | A coding agent edited its own implementation; gains were reported on coding benchmarks. | Implements the connection from agent behavior to successor agent. Gains include practical execution efficiency, and early ideas can constrain later proposals. [Paper](https://arxiv.org/html/2504.15228) |
| Agentic Context Engineering, 2025 | Incremental context updates preserve useful details and improve agent performance in the tested settings. | Retained natural-language learning can matter without weight changes. Accumulation needs controlled revision and removal; more text is not itself evidence of benefit. [Paper](https://arxiv.org/html/2510.04618v1) |
| AlphaEvolve, 2025 | Evaluator-guided program search produced useful algorithms and changes to computational infrastructure, including components used in model training. | Improvement of enabling tools and infrastructure is a legitimate route. Specific engineered evaluations and resources remain essential. [Paper](https://arxiv.org/abs/2506.13131) |
| Absolute Zero, 2025 | A pretrained model proposes and solves executable tasks, using program execution for training feedback. | Human-authored examples need not supply every learning opportunity. “Zero data” does not remove pretraining, the executor, or the chosen learning objective. [Paper](https://arxiv.org/html/2505.03335v1) |
| SIA, May 2026 | An agent alternates changes to the surrounding software and task-model weights; combined adaptation beats software-only adaptation in its experiments. | Weight updates are an additional option if evidence identifies a limitation they address. The update selector is still frozen; the paper leaves learning that selector as future work. [Paper](https://arxiv.org/html/2605.27276v2) |

Hyperagents deserves especially careful interpretation. It tests transferred improvers over 50 iterations and includes repeated runs. However, some initial agents score zero because their output format is invalid; transfer includes both the task agent and the meta agent; task distributions and main outer selection/evaluation procedures remain fixed. These details limit the claim of generality and motivate a stronger shared-starting-agent experiment for your projects. The study reports bounded transferable improvement, not a proof of unlimited capability. [Methods, transfer experiments, and limitations](https://arxiv.org/html/2603.19461v1).

The DGM study also illustrates why counting iterations is insufficient for comparing progress: its reported SWE-bench run cost about $22,000, versus about $10,000 for each ablation baseline, and stronger discovered agents can cost more at inference. Those historical costs are not an estimate for your project. They show why equal-generation comparisons should be supplemented by equal-resource comparisons. [DGM cost analysis](https://arxiv.org/html/2505.22954v3).

GEPA’s six-task Qwen3-8B table reports an aggregate score of 54.85 versus 48.91 for GRPO, but GRPO does better on AIME-2025 in that table. Its result supports effectiveness in the tested comparisons, not universal superiority of prompting over training. This is precisely the kind of conditional conclusion a perspective optimizer should preserve. [GEPA evaluation](https://arxiv.org/pdf/2507.19457).

**The negative evidence concerns reliability of the loop, not a blanket impossibility of self-correction.**

Huang and colleagues found that the models they tested often failed to improve reasoning through intrinsic self-correction and could become worse. That result is specific to tested models and setups. SCoRe subsequently showed that training can substantially improve self-correction behavior. Together they support evaluating the actual correction procedure; neither “reflection always helps” nor “models cannot correct themselves” is justified. [Intrinsic self-correction study](https://arxiv.org/abs/2310.01798), [SCoRe](https://arxiv.org/abs/2409.12917).

An August 2026 re-evaluation of Agent Workflow Memory and ReasoningBank is especially relevant. Across web-agent experiments, memory-based improvement often increased variation between runs. ReasoningBank’s reported average gain under the default task order became a loss under shuffled orders. The study used a stronger starting system than earlier work and identified plausible but inapplicable memories as one contributor. It studied these methods and domains, not every form of recursive improvement. [On the Fragility of Self-Improving Agents](https://arxiv.org/html/2608.18066v1).

Your requirement to avoid repeated corrections therefore has a concrete experimental counterpart: test multiple task orders, strong starting agents, and cases where a previously useful rule should not apply. Otherwise the system may learn the order of the demonstration or an overgeneralized instruction.

Evaluation by a language model is useful but fallible. The original MT-Bench work documented position, verbosity, and self-enhancement biases alongside substantial agreement with human preferences. Agreement is evidence about a specified comparison, not a universal truth detector. [Judging LLM-as-a-Judge](https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html).

Repeatedly tuning against a supposedly held-out set also changes its role. Once its results influence future selection, it is part of development. Adaptive-data-analysis research establishes why repeated feedback can lead to overfitting even without directly exposing every answer. [Generalization in Adaptive Data Analysis and Holdout Reuse](https://arxiv.org/abs/1506.02629).

**The decisive design requirement is to make the system’s own improvement activity an ordinary object of its operations.**

A new special hierarchy of “meta” projects is unnecessary. The same machinery can investigate its own source selection, formulation, retrieval, candidate construction, experimentation, interpretation, and revision. The distinction is what the operation changes.

For example:

| Change target | Possible retained change | What subsequent evidence would establish its value |
| --- | --- | --- |
| Task execution | A correct three-state interface adapter | New valid inputs are handled without losing uncertainty |
| Problem formulation | Compare representation failure with rule failure before replacing a working rule | Fewer repairs target the wrong component on unfamiliar failures |
| Candidate construction | Generate a contrast where final verdicts match but downstream information differs | More otherwise hidden contract defects are discovered |
| Evaluation | Check complete result contracts when later consumers depend on them | Fewer incomplete transformations pass acceptance |
| Memory retrieval | Activate a transfer rule from producer–consumer structure instead of shared vocabulary | The rule helps in differently named domains |
| Memory revision | Preserve application limits while removing redundant explanation | Later uses retain distinctions and cost less to retrieve |
| Improvement selection | Favor investigations that discriminate competing causes | More validated improvements are found within the same resources |
| Improvement evaluation | Compare evolved and earlier improvers on the same starting agents | The evolved procedure has greater capacity to produce useful successors |

The first row is ordinary capability improvement. Several later rows can improve the means of improvement. Whether they do so is an empirical question. Calling every retained rule “meta” would erase the distinction the experiment needs.

The current design has an additional strength: it need not force every inquiry through an existing failure diagnosis. Trying a different representation can expose a problem the current detector could not recognize. The improvement process should therefore have both result-driven correction and deliberate exploration of plausible alternatives. Which balance works best should itself remain testable.

**The missing work can be expressed as operations with observable consequences.**

| Required operation | Concrete behavior | Failure that blocks recursive improvement |
| --- | --- | --- |
| Establish the current system | Load the actual instructions, code, retained findings, source versions, environment capabilities, and resource limits | Improvements are proposed against an imagined or obsolete system |
| Choose a useful investigation | Use current work, repeated costs, disagreements, opportunities, or fresh probes to select what to examine | The user still supplies every intellectual transition |
| Construct a candidate change | Produce a new distinction, operation, representation, retrieval condition, tool, or decision rule | The process can only score pre-invented alternatives |
| Make the change operative | Run the changed procedure on a real or controlled case | A persuasive description is mistaken for enacted behavior |
| Discriminate consequences | Obtain results that would differ between the relevant explanations or candidates | The experiment cannot tell whether the change matters |
| Assess the original concern | Compare benefit, errors, losses, and cost using evidence appropriate to the claim | The system improves a convenient proxy |
| Retain with applicability | Preserve what changed, its grounds, conditions, countercases, and executable dependency | A finding becomes an inert note or universal command |
| Install in later execution | Load the retained change into a fresh relevant run | Apparent learning disappears when the conversation ends |
| Revisit its own procedure | Apply the same operations to the machinery producing improvements | Task progress never improves future discovery |
| Attribute recursive benefit | Compare new and earlier improvers under matched conditions | Extra resources, context, or task familiarity explain the gain |
| Maintain recovery | Preserve usable earlier versions and recheck affected consumers after changes | Improvements disable checking, retention, or continuation |
| Expand learning opportunities | Seek fresh cases, information, representations, and feasible operations when current ones are exhausted | The process repeatedly polishes a saturated task family |

No column requires the user to fill in a form at each use. The system should recover standing requirements and infer routine choices from context. When a missing preference or inaccessible fact changes the correct action, that uncertainty should remain explicit. Eliminating needless specification does not grant access to genuinely unavailable information.

Nor does every operation need to be a deterministic Python function. A model can construct distinctions, derive implications, or judge a proposed explanation. The requirement is an actual invocation, a result that can be examined, and a correction route. Deterministic tools should settle the parts they can settle exactly.

**Evaluation must remain connected to the purpose while allowing the system to discover that its current criterion is wrong.**

A fixed scorer is valuable for a controlled comparison. Making that scorer the complete definition of a perfected perspective would unnecessarily restrict the project. A system might satisfy all listed checks while investigating the wrong matter, preserving an inadequate representation, or optimizing a property the user does not need.

The solution is to retain two distinguishable questions:

1. Did this candidate improve performance under the current comparison?
2. Is that comparison adequate to the underlying concern?

A criterion revision should have its own evidence. The system should identify the original concern, produce a case where the old criterion rewards an inadequate result, propose a better distinction, and reassess the earlier and new candidates. Retaining the earlier comparison prevents revision from becoming a way to erase an inconvenient result.

For your actual interface case, checking only the achievement status was inadequate when the consumer also needed optional observations and activity state. A complete-contract comparison is justified by the consumer’s use. Conversely, adding irrelevant fields to every output would impose cost without a corresponding requirement. The criterion should follow the actual dependency.

Different claims need different evidence:

| Claimed improvement | Suitable evidence |
| --- | --- |
| Preserves declared logical states | Exact finite enumeration, type checks, or a proof |
| Repairs a software transformation | Execution on independent inputs and downstream checks |
| Adds a useful distinction | A separating case where a prediction, operation, inference, or decision changes |
| Improves factual reasoning | Sources, consistency checks, and new questions with independently established answers |
| Improves empirical prediction | Outcomes obtained after the prediction, with uncertainty recorded beforehand |
| Improves open-ended explanation | Case coverage, counterexamples, inferential consequences, and comparison with alternatives |
| Better serves the user’s intent | Relevant prior instructions and judgments on concrete outcomes, with human effort counted |
| Improves the improvement method | Superior production of validated successors from matched starting conditions |

The same model may contribute to proposing and evaluating a change. That alone neither invalidates nor validates the result. Independence should come from evidence and comparison conditions, not merely different role names. Separate model calls can still share a blind spot. A simple execution result can sometimes discriminate a claim more decisively than a more elaborate verbal judgment.

Some philosophical questions lack a presently decisive test. The appropriate output may be a clarified dependency, a counterexample to one claim, or competing accounts with different consequences. Preserving that unresolved status is part of reliable improvement. It does not prevent useful work on what can be settled.

**Persistent learning needs controlled activation and controlled revision.**

Saving a finding does not establish its availability in practice. A later run must retrieve it, recognize its applicability, perform the relevant operation, and preserve its important conditions. Each step should be tested using unfamiliar surface wording and interrupted contexts.

For example, the lesson “preserve unknown” must not become “always return unknown.” The lesson “compare complete contracts” must not become “include every field everywhere.” The lesson “anticipate before responding” must not become a rigid preamble that adds cost without changing the response. Negative applicability cases are therefore part of the learned rule’s evidence.

A useful record should contain the smallest amount of material needed to reconstruct the operation and its grounds: the change, the condition that makes it relevant, an observed comparison, a countercase or boundary, and any dependency needed to run it. That amount may be one paragraph or a larger executable artifact. Word count is not the criterion.

Retention should also operate at the source of recurring behavior. If a generator repeatedly inserts unwanted framing, revising one generated page will not reliably change the next page. If a retrieval rule repeatedly misses a relevant distinction, adding another copy of the distinction may not help. The system should revise the mechanism producing the repeated error.

Some learning can be corrective deletion. An established rule can lose its grounds. Two rules can interfere. A former shortcut can become inappropriate after an environment change. A successful memory process must support narrowing, withdrawal, and restoration as well as addition.

**A direct test of recursive benefit should hold the starting task agent constant.**

Let A denote a task-solving system, U an improvement procedure, and B an improvement resource budget. Run U from A using development evidence, select the resulting candidate using validation evidence, then assess it on fresh test tasks. Define the improvement yield as:

\[
I_B(U;A,D)
=
\mathbb{E}\!\left[Q_D\!\left(\operatorname{Select}_{\mathrm{validation}}(U(A;B))\right)\right]
-
Q_D(A).
\]

Here D is the held-out task distribution. The expectation includes stochastic model behavior. Q is a declared task-family measure; separate constraints and additional quality dimensions remain visible. This notation does not impose a universal scalar definition of perspective quality.

The critical comparison is:

\[
I_B(U_{\mathrm{new}};A^\*,D_{\mathrm{new}})
>
I_B(U_{\mathrm{old}};A^\*,D_{\mathrm{new}}).
\]

Both improvers begin with the same A*. They receive the same admissible evidence, environment, model version, and resource allowance. The new improver must have arisen from the system’s own earlier improvement activity. This tests whether it became better at producing improvements.

Additional comparisons matter. Removing only the retained improvement-method change should reduce the recursive gain if that change caused it. Giving the baseline extra time or an equally long but irrelevant context should not explain the result. Fresh evaluation should distinguish a general improvement method from recognition of a previously solved example.

The inequality is an experimental target, not an established result for your projects. Improvement on one downstream benchmark, a more impressive rationale, or more output does not establish it.

**The first experiment should directly test the additional contribution of these projects.**

A strong language-model agent already supplies reasoning, coding, retrieval, and ordinary revision. Beating an intentionally weak baseline would tell little about whether Subject Systems and Perspective Optimizer add value.

Use four initial conditions:

| Condition | Available machinery | Question answered |
| --- | --- | --- |
| Strong baseline | A capable agent with the same tools, task information, persistence facilities, and resource allowance | What can the underlying system already do? |
| Subject Systems | Baseline plus relevant catalog and subject-specific systems | Does the theoretical organization improve relevance and construction? |
| Perspective Optimizer | Baseline plus perspective operations and its minimal required bindings, without the full Subject Systems development material | Do the applied operations contribute independently? |
| Combined system | Both projects, with explicit incorporation of validated changes | Does their composition add value beyond the components? |

The Perspective Optimizer condition cannot be made literally independent of its imported bindings without changing the project’s identity. Record that overlap. Also compare raw retrieval with condition-sensitive use: loading the files and making their distinctions operative are different interventions.

Within the combined system, compare a frozen improvement procedure with an editable one. Initially this can be a staged comparison, avoiding an expensive full factorial experiment before any basic gain appears.

Use task families connected to the intended capability:

| Task family | Required discrimination | Important control |
| --- | --- | --- |
| Interface preservation | Distinguish incompatible encoding from a defective underlying rule | Include inputs already in the correct representation |
| Completion assessment | Distinguish satisfying a visible output check from preserving what a later consumer needs | Include cases where extra information is irrelevant |
| Repository correction | Change the mechanism that regenerates a defect and preserve replay paths | Include a defect isolated to a single output |
| Perspective construction | Add a missing distinction that changes a relevant operation | Include ornamental differences with no contribution |
| Evidence and formulation | Decide whether to retrieve evidence, derive a consequence, change representation, or reformulate the question | Include questions whose original formulation is adequate |
| Criterion revision | Repair an inadequate evaluator with a concrete countercase | Include tempting revisions that merely make a failed candidate pass |

These families should be developed into executable tasks wherever appropriate and source-backed comparisons where execution is insufficient. The known 54-case interface study belongs in development, because this investigation already knows its solution. Renaming its variables would not create a genuinely fresh transfer test.

The experiment proceeds through discriminating stages:

1. **Basic contribution.** Compare the four conditions on fresh task instances. Record correct outcomes, consequential omissions, unnecessary changes, costs, and human corrections. If the combined system provides no material gain, locate whether retrieval, selection, enactment, or interference explains that result.
2. **Retention.** Start fresh executions with the validated update but without the original conversation. Verify that the relevant behavior persists and that invalid applications do not increase.
3. **One recursive change.** Let the system identify and modify an improvement operation. Preserve the exact preceding version and the evidence that motivated the change.
4. **Shared-starting-agent comparison.** Test the old and new improvers on the same fresh agent versions and problem families. Choose successors on validation results; reserve final tasks from both.
5. **Attribution.** Remove the specific meta-level change, retain task-level fixes, and rerun the necessary comparisons. This distinguishes an improved improver from a simply better starting task solver.
6. **Repeated recursion.** Allow descendants to produce further improvement-method changes, measuring both gains and regressions across independent lineages.
7. **Transfer and order stress.** Change task families, surface representations, task order, and relevant environment conditions. Test retention under interruption and retirement of obsolete rules.

A pilot might use three task families, several independent lineages, and a small fixed number of improvement opportunities. Those numbers are engineering starting points, not evidentiary thresholds. Set the final sample size and stopping rule from the smallest improvement that matters and the observed variability. Report the whole distribution of runs, including stagnation and failure, instead of selecting a striking lineage.

Resources must include model input and output, tool execution, evaluation, elapsed time, storage and retrieval overhead, and human intervention. Generation counts alone are inadequate because later agents may spend much more per generation. Compare quality at a fixed resource allowance and resources required to reach a fixed acceptable quality.

Keep an untouched final test stream or use a justified protocol for adaptive reuse. Do not select the best successor on final test scores. When fresh test results become the basis for later improvement, classify those cases as development evidence for subsequent claims.

**The existing interface study offers a concrete sequence from ordinary repair to recursive improvement.**

At the first level, a system observes that the two interfaces use different encodings for the same three logical states. It constructs the exact translation and preserves the complete required output. The current deterministic experiment already supports that local repair.

At the second level, the system recognizes that matching a final verdict can conceal a lost distinction required downstream. It retains an operation: compare the producer’s complete result against the consumer’s actual needs, then construct a case where a proposed simplification changes the downstream behavior. This is broader than the adapter.

At the third level, the system applies that operation to its own improvement process. It discovers, for example, that its memory compression preserves “this worked” while deleting the condition that made it work. It revises memory construction and the test used to accept compressed findings.

At the fourth level, the revised memory process helps a later run distinguish a real rule failure from an information-loss failure, find a more appropriate improvement, and avoid a previously repeated mistake. Compare that process against the earlier one at the same resource allowance.

At the fifth level, the later run improves how applicability countercases are generated, and that change further increases the usefulness of subsequent retained discoveries.

Only the first level is established by the current executed interface comparison. The rest is a proposed, testable lineage. It illustrates the kind of recursion that would validate the central ambition without requiring the system to solve every theory of perspectives first.

A similarly concrete sequence begins with the replay defect: repair the path; add dependency-sensitive replay verification; use that verification to detect a later change that would otherwise weaken the improvement process. Repairing the path alone is a useful engineering correction. The latter steps would establish more of the recursive mechanism.

**The hardest remaining problem is reliable judgment of which improvement opportunity is worth pursuing.**

A system can have an excellent evaluator but spend its entire budget proposing irrelevant changes. It can generate useful ideas but fail to choose the test that would reveal their value. It can verify a local gain while losing a more valuable future capability. These are distinct bottlenecks.

Subject Systems could contribute by distinguishing the kind of result needed: a missing fact, a new representation, a validity result, an applicability condition, a criterion justification, a construction, or evidence of transfer. Perspective Optimizer could use those distinctions to choose and revise the work. Their potential advantage is improved direction of computation.

That potential is not established by the ontology’s elegance. It must appear in observable behavior: fewer irrelevant investigations, more productive alternatives, better separating cases, faster recovery from misleading results, and more useful retained changes. A generic capable agent with the same budget is the relevant comparison.

Early success can create its own limitation. A profitable frame can dominate retrieval and candidate generation until every new problem is interpreted through it. The system needs to maintain a route for examining its own categories, exposing what they hide, and departing from a successful method. The goal is conditional competence across matters, not universal compulsory use of every perspective.

Exploratory candidates may deserve retention before they improve the current task. A different representation may enable a later tool or reveal a previously inaccessible comparison. Such candidates should carry evidence of their distinct contribution or a specific unresolved opportunity. Retaining every mutation indefinitely would consume resources without establishing option value.

**The theory can support bounded guarantees without supporting universal perfection.**

In a finite domain, with an exact evaluator, a known finite set of feasible systems, sufficient resources to compare them, and a selection rule that preserves the best result, one can establish optimality relative to that domain and ordering. This follows from exhaustive comparison. It does not establish that the domain contains every relevant perspective, that the ordering expresses every concern, or that the selected system improves the process of selection.

For an open-ended system, those assumptions become substantive research problems. The relevant task distribution can change. An evaluator can omit a consequential distinction. A proposed operation can be physically unavailable or computationally impractical. Two purposes can favor different results. A useful optimum may not be attained, or further improvement may require resources unavailable to the agent.

Gödel-machine theory makes the dependence on assumptions explicit: self-rewrites are justified relative to formal axioms about the system, environment, and utility, when the relevant benefit is provable. It is a formal construction, not a practical guarantee that an open-ended language-model system will find proofs for all useful changes. [Schmidhuber’s original paper](https://arxiv.org/abs/cs/0309048).

There are simpler obstacles to a universal claim. If two possible environments are indistinguishable from the information currently available but require incompatible responses, the system cannot guarantee the correct response in both without some additional distinguishing basis. A more sophisticated perspective can identify this limitation or seek the needed observation; it cannot manufacture the unavailable fact.

Nor does recursive improvement imply increasing speed. A sequence of scores approaching a ceiling can improve at every step while yielding progressively smaller gains. Even a better improvement procedure can face harder remaining problems, more expensive evaluation, or exhausted accessible interventions. Indefinite progress requires continuing opportunities and resources; accelerating progress requires gains that outweigh those growing costs.

For this project, “perfected perspective” becomes operational when it means that the system identifies and meets the warranted requirements of the matter, preserves important distinctions, finds consequential omissions, and revises appropriately when new evidence changes the situation. Universal infallibility over every possible matter is a substantially stronger claim. No reviewed result establishes it, and the present architecture does not supply a proof.

**The initial model needs enough capability to get the loop started, but it need not already solve every later problem.**

A capable model may recognize an improvement when given a relevant contrast, execute a procedure it would not have selected unaided, or write a tool whose results exceed what it can reliably calculate internally. Persistent organization can make those contributions available to later work.

This is a plausible source of large early gains for your projects: correcting activation, representation, task formulation, and reuse can expose capabilities already present but poorly directed. New tools and new evidence can then expand the whole system’s abilities.

The extent of that expansion must be measured. It is not justified to infer a hard system ceiling directly from frozen weights, because software, memory, interaction, and computation can change. It is equally unjustified to infer unlimited capability from the ability to write arbitrary code. Expressing a candidate and discovering an effective candidate within a budget are different properties.

Weight adaptation is appropriate when experiments identify a limitation that instruction, representation, tools, and retrieval do not adequately address at the required cost. It is not a prerequisite for the first recursive demonstration. If introduced, its training data, version, compute, regression behavior, and contribution should be measured separately from software and memory changes.

**Anticipation should become a tested preparation operation.**

Before changing a procedure, the system can identify the results that would distinguish the candidate from its baseline, the likely sources of misleading apparent success, and the next action corresponding to each important result. This can expose an inadequate experiment before resources are spent.

For this investigation, the decisive anticipated objections were substantive: a code audit alone would not settle conceptual sufficiency; a list of missing features would not demonstrate recursion; fixed model weights would not justify dismissing the idea; benchmark gains would not establish an improving improver; and a universal perfection claim would require far more than local success.

The corresponding operations were to inspect current code, reproduce scoped behavior, review direct precedents, distinguish ordinary from recursive gains, and specify a shared-starting-agent comparison. These are observable research decisions, not a claim of complete introspective access to model reasoning.

Your current anticipation method already connects different possible outcomes to discriminating observations and continuations. Its effect should be compared against the same system without that preparation, including preparation cost and cases where a direct operation is sufficient. If it reliably improves subsequent investigation design and its own refinement, it can participate in the recursive process. [Anticipation outcome branching](https://github.com/benjam3n/perspectiveoptimizer/blob/7277935d3e9267b6103f7188ed65a95a3f0dc6c2/methods/anticipation-outcome-branching.md).

**The next implementation should close one complete, inspectable cycle inside the existing projects.**

Perspective Optimizer needs a callable improvement process that can consume actual cases and prior results, construct and enact a candidate change, obtain comparison evidence, retain a validated change, and load it into subsequent execution. The proposal, retrieval, interpretation, and revision operations used by that process must themselves be eligible for examination and modification.

Subject Systems should continue supplying precise subjects, boundary conditions, and systems that contribute to the active investigation. Applied failures should be able to revise those accounts. A new subject or theoretical relation should be added when it resolves an actual identification or construction problem, with its role preserved in the evidence.

The initial engineering sequence is:

1. Restore the verified study replay path and connect executable replay checks to changes that affect their dependencies.
2. Establish a strong, correctly functioning baseline with a stable task interface and recorded resource use.
3. Implement one complete model-performed improvement cycle, including a fresh-run retention check.
4. Use the cycle on one of its own improvement operations.
5. Run the controlled comparison of old and new improvers from a shared starting system.
6. Extend only after the preceding result identifies the remaining limitation or a supported opportunity.

The visible interface can stay simple. The system can perform these investigations internally and present the consequential result, evidence, and unresolved question. The user should not have to organize its candidate explanations, supply every operation, or repeatedly restate established constraints.

**The verdict should change when the following evidence exists.**

A bounded self-improvement claim becomes justified when the running system creates a persistent change that improves relevant fresh-task performance under an adequate comparison.

A bounded recursive self-improvement claim becomes justified when a system-produced change improves the ability to generate further validated improvements, with that ability demonstrated from matched starting conditions and retained across new executions.

A transferable recursive improvement claim requires that benefit in additional task families, with appropriate applicability limits, stable performance across orders and repetitions, and evidence that gains are not supplied by extra human direction or uncounted resources.

A sustained improvement claim requires longer runs that preserve earlier capabilities while continuing to find useful changes. A claim of acceleration additionally requires increasing improvement yield or decreasing resources per meaningful gain under a comparison that accounts for task difficulty.

The projects presently support the investigation and construction of these capabilities. They have not demonstrated them. Their strongest development path is to turn their own distinctions about relevance, enactment, evidence, retention, and transfer into the actual behavior of a running improver—and then establish that this behavior helps it build a better improver.

