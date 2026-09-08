from write_record import record,progress,ROOT
record(23,'op',1,'Preserving an exploratory route without comparing before criteria exist',
'Change a single fixed research sequence into a dependency-correct order that permits criteria discovery while preventing an ungrounded benefit comparison.',
'The strong ordinary sequence is claim→criterion→outcomes→comparison→result. It protects against changing criteria to favor an outcome, but some exploratory tasks first reveal which criterion is relevant.',
'''
Input steps: freeze claim, capture outcomes, define criterion, classify applicability, compare outcomes, write scoped result, make reusable excerpt. Inputs/outputs: the frozen task supplies domain and predicate; outcome capture supplies observations; criterion definition supplies the meaning of better; applicability supplies the included set; comparison consumes all three; result consumes the comparison; excerpt consumes the scoped result. Resource: one local author; independent reads can be batched, judgments remain explicit.

Eight hard edges are in [the executed graph result](order-case-results.json), case 23. The criterion→outcome edge is soft: prior criteria can guide observation, but a raw observation can exist before a criterion is chosen. The criterion→comparison edge is hard for a statement of benefit. No mutual exclusion is intrinsic between observation and criterion discovery; changing criteria silently after comparison is excluded by the record requirement, not by pretending criteria can never change.

Cycle check: the apparent cycle “observe to discover criteria; criteria needed before observing” dissolves when “capture raw outcome” is separated from “compare benefit”. The former can precede criteria; the latter cannot. Kahn’s algorithm returned all seven nodes, no cycle. The valid order is freeze claim→capture outcomes→define criterion→classify applicability→compare outcomes→write scoped result→make reusable excerpt. Every hard edge was checked against actual order positions.

Parallel-eligible wave after freezing: capture outcomes, define criterion, classify applicability. This is dependency eligibility, not a claim that this single model performs simultaneous independent thought. The longest dependency chain has five nodes (four edges). All three wave-one branches feed comparison at equal graph depth, so there is no depth slack among them; durations are not measured, so no critical elapsed-time claim is made. Actual order honors the soft criterion-first edge when criteria are already known; exploration may choose outcome-first while preserving the later comparison gate.

Concrete use: a specimen pair has unchanged raw completion counts A=2, B=3. First criterion “minimize represented items” prefers A; revised criterion “include all three required cases” prefers B. Both observations existed before either ranking. The result states the changed criterion and preserves both comparisons rather than rewriting the old observation. The excerpt carries “B for complete three-case coverage; A for fewer items.” A criterion-first alternative remains preferred when the user’s goal is already explicit.

Certificate: exact claim—a dependency structure can allow outcome capture before criterion selection while still requiring a criterion before benefit comparison—is supported by the acyclic graph and concrete two-ranking specimen. Strong contrary—outcome-first exploration permits hindsight bias; the record of both criteria/comparisons makes the change inspectable but does not prove absence of bias. The adopted rule is conditional on exploration, not a universal preferred ordering.
''',
'I split raw observation from benefit comparison, softened only the unnecessary edge, and used the resulting order to preserve two criterion-dependent rankings of one unchanged input.',
'The local sequence can represent a genuine criterion change without claiming that the data changed or that comparison is possible without a criterion.',
'KEEP — exploratory dependency order with a hard comparison prerequisite.',
'The graph is stored as exact edges and checked order; the compact working distinction is raw observation versus criterion-dependent comparison.',
'Test a criterion fixed by the user; test criteria that change after an adverse result; test whether preserving two rankings becomes too burdensome on a trivial choice.',
'No numerical 8x floor exists. All eight operations were performed: seven input/output/resource maps, hard/soft/mutual-exclusion assessment, an apparent cycle resolved semantically, executed topological sort, every edge checked, parallel eligibility, longest dependency path and depth slack, optimization and actual use.')
progress()
