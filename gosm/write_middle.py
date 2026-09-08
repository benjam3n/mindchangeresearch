from write_records import write,table,data

rows=[[r['id'],r['kind'],r['truth'],r['A'],r['B'],r['domain_route']] for r in data['trust']['rows']]
write(5,'trust-and-duplication','A perfect retrospective routing result is not a new trust result',
 'Find whether a domain-sensitive source choice yields an independently useful improvement, and reject a performative success if its evaluation supplies its own answer.',
 'Source competence and correlated evidence already appear in the program’s prior standards. What remains unsettled is whether this constructed retrospective routing exercise adds demonstrated predictive benefit.',
 '''The underlying question is whether a source-selection improvement is being evaluated on information that was already used to define the source-selection rule.

Input: eight binary facts are stipulated with their truth values. Source A returns the truth on color cases and its opposite on shape cases. Source B does the reverse. Three further reports are exact copies of A. A proposed router selects A for color and B for shape. This construction intentionally makes the source functions inspectable; it is not a dataset of real people's expertise.

'''+table(['Case','Domain','Truth','A','B','Router'],rows)+'''

A and B each match four of eight truths; the router matches eight. Three copies of A still originate from one answer function and have the same four errors. An unweighted majority of A's three copies plus B agrees with A, so it matches only four truths. Equal global source scores hide the domain pattern in this declared table.

The distinctions are a source identity versus competence on a task; correctness in a supplied table versus predictive reliability; independent reports versus copies; evidence used to construct a rule versus evidence used to evaluate it; agreement versus truth; confidence in a function definition versus confidence in a person; a stable error process versus a changed domain; and repeated correct output versus additional information.

Position: the table illustrates a mechanism but does not demonstrate a newly learned trustworthy router. The domain error functions were supplied in the input, and the router is their direct transcription. The eight successes do not supply independent evidence that a real source keeps the same competence profile.

The strongest contrary branch is that a declared deterministic function does logically settle further outputs inside that declared model. That is true. For a ninth color item with truth 1, the stipulated A function returns 1. The conclusion is deductive under the function definition. It is not an observed generalization result about an unspecified source. Both scopes must remain visible.

The tension is that an impressive success rate can be entirely compatible with zero new empirical information. The exercise's actual value is exposing this attribution boundary, which was already part of the shared standard. Relabeling it as a novel discovery would add apparent improvement without new benefit.

Later application: introduce a ninth item in the new domain texture. Neither supplied function defines behavior there. The router has no supported choice. For a tenth item in color, the declared model predicts A correctly, but a real source would require evidence that the function applies. The later disposition is therefore “unresolved for texture; conditionally deduced for color,” not an unconditional ten-item success report.

Specific next action: retain the example as a negative control for retrospective success claims; obtain separate observations before claiming improved source trust. Open threads: changing expertise, shared upstream evidence, incentives, and dependence that varies by domain remain untested.''',
 'The attempted new-benefit claim was rejected. I retained the domain distinction as an illustration and withheld an unsupported answer for the new texture item.',
 'The record guards against giving this already specified router new discovery credit. No independently demonstrated trust improvement or human attitude change occurred.',
 'REJECT — as a claim of a new beneficial trust method; preserve the exact negative result and conditional model calculation.',
 'Keep this record among null and performative controls, linked from source-trust routing. Putting its 8/8 score in the KEEP table without its construction would mislead later selection.',
 'Use separate discovery and evaluation observations; examine sources with partly shared evidence; change the task domain while preserving the source identity.')

rows=[]
for name,r in data['uncertainty'].items():
    rows.append([name,r['probability_x1'],len(r['query_A']),len(r['query_r']),str(r['worlds'])])
write(6,'uncertainty-and-next-query','Equal belief can require different evidence',
 'Choose the next observation from the structure of what is unknown rather than from a confidence number alone.',
 'I have not yet resolved which query is useful in two contexts that share P(x=1)=1/2. The current confidence value alone supplies no distinction between them.',
 '''The underlying question is what a belief summary leaves out about the way further evidence will change it.

Input: truth x is binary; a source's inversion bit r is binary; its report A=x XOR r. Context K1 has observed A=0 but does not know r, leaving worlds (x,r)=(0,0),(1,1). Context K2 knows r=0 but has not observed A, leaving (0,0),(1,0). Each context assigns equal probability to its two worlds. The available unit-cost queries are “read A” and “calibrate r.” Queries are exact and can be repeated, but a repeated query returns the same bit.

'''+table(['Context','P(x=1)','Classes after reading A','Classes after calibrating r','Possible (x,r)'],rows)+'''

In K1, reading A again returns 0 in both worlds, so x remains unresolved. Calibrating r distinguishes the worlds: r=0 implies x=0 and r=1 implies x=1. In K2, calibrating r again returns 0 in both worlds, while reading A reveals x directly. The useful first queries are therefore opposite even though their current truth probabilities agree.

The distinctions are uncertainty about the world versus uncertainty about an observation process; an unobserved value versus a observed but ambiguous value; a posterior over x versus a joint state over x,r; confidence sufficient for a fixed action versus information sufficient to select an experiment; a new report versus a repeated report; evidence acquisition versus source calibration; identical marginal distributions versus different conditional dependencies; and an informative operation versus an operation that merely consumes effort.

Position: selecting the next cognitive operation requires enough of the uncertainty structure to predict how candidate observations separate live possibilities. P(x=1) is insufficient for that selection in this exact case.

The strongest counter is a fixed immediate action whose payoff depends only on x, with no further query allowed. Then the two contexts yield the same expected payoff for every such action; retaining r adds no decision value for that restricted problem. This boundary preserves the usefulness of compact probabilities when they are sufficient for the actual operation.

The tension is that a compressed belief can be completely adequate for deciding now and inadequate for deciding how to learn. A “more accurate probability” objective alone does not select the right next query if both start at the same probability.

Later application: increase the calibration cost to 3 while leaving the report cost at 1 and allowing both. In K1, a report costs less but never resolves x; calibration still supplies the answer at cost 3. In K2, reading A resolves x at cost 1 and calibration is redundant. Under a budget of 2, K1 must preserve unresolved x while K2 can resolve it. I used the joint-state representation to distinguish an affordable answer from an affordable but useless repetition.

Specific next action: when the next attempt concerns uncertainty, identify at least one pair of live worlds and compare what each available observation returns in those worlds. Stop at the actual information boundary rather than treating repeated text as new evidence. Open threads: noisy calibration, uncertain query cost, multiple relevant truths and emotional responses to ambiguity remain outside this calculation.''',
 'My working query choice now differs between K1 and K2 despite identical marginal confidence. The same representation produced different budget-feasible outcomes in the later case.',
 'It avoids an uninformative one-unit repetition in K1 and a redundant calibration in K2. This is an exact information-selection improvement within the declared model, not a measured effect on human uncertainty.',
 'KEEP — distinct finite evidence-selection result with a cost boundary.',
 'Keep the marginal belief for fixed immediate action and the joint possibilities for inquiry selection. Replacing either with the other everywhere adds needless complexity or loses necessary structure; the view is selected by the later operation.',
 'Add a noisy source while retaining known calibration; compare confidence changes caused by representation alone; test motivation that changes the willingness to pay for the informative query.')
