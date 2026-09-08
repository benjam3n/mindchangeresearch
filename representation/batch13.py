from write_record import record, progress, ROOT
import itertools,json

def rank_case(n,run,title,intent,start,items,dims,weights,shift,detail,conclusion):
 scores={k:sum(v*w for v,w in zip(x['s'],weights)) for k,x in items.items()};alt={k:sum(v*w for v,w in zip(x['s'],shift)) for k,x in items.items()}
 order=sorted(items,key=lambda k:(-scores[k],list(items).index(k)));aorder=sorted(items,key=lambda k:(-alt[k],order.index(k)))
 body=f'''R1–R6. Original list: {' → '.join(items)}. Six existing items; objective: {intent} The list is a priority/preference ranking, not a mandatory execution sequence. No fixed positions. Context is the current model's finite local comparison; human preferences, reading speed and learning are unmeasured.

R7. Six independent scoring questions, on a 1–5 ordinal scale. Higher is preferable for the declared objective; weights are deliberative priorities, not fitted empirical effects.

| Dimension | Weight | Why it matters |
|---|---:|---|
'''+ '\n'.join(f'| D{i+1}: {d[0]} | {weights[i]} | {d[1]} |' for i,d in enumerate(dims))+'''

Scores and every cell's justification:

| Item | Concrete object | D1 | D2 | D3 | D4 | D5 | D6 | Total |
|---|---|---|---|---|---|---|---|---|
'''+ '\n'.join('| '+ ' | '.join([k,x['name']]+[f"{v}: {r}" for v,r in zip(x['s'],x['why'])]+[str(scores[k])])+' |' for k,x in items.items())+'''

Full pairwise review (15/15 unordered pairs):

| Pair | Baseline preference | Trade-off retained |
|---|---|---|
'''
 for a,b in itertools.combinations(items,2):
  pref=a if scores[a]>scores[b] else b if scores[b]>scores[a] else 'tie'
  da=[i for i in range(6) if items[a]['s'][i]>items[b]['s'][i]];db=[i for i in range(6) if items[b]['s'][i]>items[a]['s'][i]]
  adv=lambda who,ix: who+' leads '+','.join('D'+str(i+1) for i in ix) if ix else who+' has no higher dimension score'
  body+=f'| {a} / {b} | {pref} ({scores[a]} / {scores[b]}) | {adv(a,da)}; {adv(b,db)}. |\n'
 body+='\nReordered output and movements:\n\n| Rank | Item | Original position | Score | Reason |\n|---|---|---:|---:|---|\n'
 for pos,k in enumerate(order,1):body+=f"| {pos} | {k} | {list(items).index(k)+1} | {scores[k]} | {items[k]['reason']} |\n"
 body+=f'''\nAlternative weights {shift} produce {' → '.join(aorder)} with scores {', '.join(k+'='+str(alt[k]) for k in aorder)}. Exact alternative ties use the baseline order as a stable tiebreak; this is a coding convention, not a revealed preference. This tests how priorities change rather than pretending an ordinal sum establishes objective utility.

{detail}

Certificate: the complete six-dimension and fifteen-pair calculation makes this particular ranking inspectable, but does not turn model judgments into human effect estimates. {conclusion}
'''
 record(n,'ro',run,title,intent,start,body,
 'I constructed the complete ranking, compared all pairs and shifted weights, then performed the concrete later-use checks described above.',
 'The ranking is auditable and locally usable; no additional independent improvement over the strong existing representation was established.',
 'REJECT — no new independent KEEP; the inspected ranking remains available with its conditions.',
 'Keep the ranked entry for the declared objective and the alternative order for the changed criterion; retain original order and all score grounds.',
 'Replace judgmental weights with a real reader preference if supplied; test one new item without refitting old scores; check whether a prerequisite changes the ranking into an execution sequence.',
 'Original 8x floors met: six dimensions, every item scored with a reason on every dimension, all 15 pairs, full reordered/movement output, dependency and sanity checks, confidence map, alternative order and explicit weight-shift analysis.')
 (ROOT/f'ro-{run}-scores.json').write_text(json.dumps({'weights':weights,'alternative_weights':shift,'items':items,'scores':scores,'order':order,'alternative_scores':alt,'alternative_order':aorder},indent=2))

items={
'E':{'name':'Empty domain []','s':[4,2,3,3,5,2],'why':['changes vacuous truth','current task has observed member','adds domain convention','needs convention stated','one empty vector','does not isolate value versus membership'],'reason':'Boundary convention matters, but is not the live unknown-value question.'},
'P':{'name':'Positive singleton [1]','s':[2,2,1,5,5,1],'why':['confirms familiar agreement','no missing value','already implicit in positive anchor','self-contained value','one value','one obvious interpretation'],'reason':'Useful anchor, lowest new discrimination for this target.'},
'N':{'name':'Negative singleton [0]','s':[3,3,2,5,5,2],'why':['contrasts every with none','negative anchor is relevant','removes unknown rather than tests it','self-contained value','one value','isolates known negative'],'reason':'Cheap negative anchor; less direct than the unknown cases.'},
'U':{'name':'Negative plus unknown [0,?]','s':[5,5,4,5,4,3],'why':['every settled while some open','exact current missing-data issue','opposite anchor from slide','two explicit completions','two completions','distinguishes false from unknown'],'reason':'Highest live-query fit and direct separating completions.'},
'Q':{'name':'Only unknown [?]','s':[4,4,3,4,5,3],'why':['neither quantifier fixed','missing result without anchor','removes known evidence','two completions need notation','one missing value','tests lack of any fixed result'],'reason':'Removes the anchor and checks both unresolved claims.'},
'M':{'name':'Uncertain membership of known zero','s':[5,4,5,2,2,5],'why':['denominator can flip every','live scope issue','different uncertainty source','eligibility definition needed','two domains plus known value','separates membership from value uncertainty'],'reason':'Best source-of-uncertainty distinction, with greater setup.'}}
rank_case(37,2,'Prioritize six logical probes under an explicit question','Prioritize probes that distinguish which proposition remains unresolved in an incomplete-result task.',
 'The gap analysis already prioritizes negative-plus-unknown, uncertain membership and only-unknown cases. The six gaps can also be listed in inventory order; a more elaborate rank may or may not improve the next choice.',items,
 [('Inference discrimination','Can it overturn a plausible wrong conclusion?'),('Current-question fit','Does it directly answer the live missing-data issue?'),('Distinct relation','Does it add a relation absent from the current slide?'),('Self-contained setup','Can its terms be specified without another lesson?'),('Construction economy','How little finite construction is needed?'),('Alternative separation','Does it distinguish competing sources of uncertainty?')],[3,3,2,2,1,2],[1,1,1,2,5,1],
 '''Dependency check: no probe logically requires completion of another; each has its own explicit domain. M does require the definition of eligibility, supplied in its prompt, so its setup score is lower. This is not a reason to place another probe before M by force.

Sanity: top three U/M/Q directly vary the live uncertainty; bottom N/E/P are anchors or a different boundary convention. N/E are only two points apart and may swap when empty domains are the actual concern. U/M can swap when denominator ambiguity is the known problem. No adjacent total tie exists under baseline weights. Under economy weights U/Q tie, retained U-first because it matches the original live question. High confidence: P is not first for this objective; U is in the leading group. Low confidence: M can move from second to last when setup burden dominates, E/N can switch, Q can move to first. Most debatable M.

Actual top-three transfer probes: [0,?,?] yields every=false in all four completions, some unresolved; [1] versus [1,0] under changed membership yields some=true and every unresolved; [?] yields every and some unresolved. These were explicitly enumerated from the finite definitions. The selected leading probes match the earlier category-gap priorities. The added ranking did not change which probe was used first or the answer it produced.''',
 'The same first choice and known scope cautions were already obtained by 036. Extra dimensional scoring has no demonstrated incremental benefit here.')

items={
'S':{'name':'One complete sentence','s':[4,4,5,3,4,3],'why':['states both criteria','common counts stated','serial prose','comparison clauses separated','small text block','criteria recoverable after full read'],'reason':'Compact serial reading with a full-sentence commitment.'},
'B':{'name':'Two parallel bullets plus shared input','s':[5,5,4,5,4,4],'why':['both conditions explicit','shared input precedes bullets','three serial units','parallel comparison','short units','each condition beside verdict'],'reason':'Easy aligned comparison when both conditions are in view.'},
'T':{'name':'Two-row criterion table','s':[5,5,3,5,5,5],'why':['conditions in row labels','shared counts in caption','header context required','parallel rows','six cells','one row gives criterion and verdict'],'reason':'Strong direct lookup for a reader who knows the criterion.'},
'C':{'name':'Paired self-contained cards','s':[5,5,5,4,2,5],'why':['each condition explicit','counts repeated on each card','each card serial','cross-card comparison','repeats common counts','excerpt carries complete case'],'reason':'Best independent extraction at the cost of repeated input.'},
'F':{'name':'Formal predicate pair','s':[5,4,2,4,5,3],'why':['criteria mathematically specified','legend contains counts','notation knowledge needed','two compact formulas','few tokens','excerpt needs legend'],'reason':'Compact for a notation-fluent reader, legend-dependent otherwise.'},
'D':{'name':'Two-branch decision rule','s':[5,4,4,3,3,5],'why':['each branch states condition','counts in root clause','if/else serial','branch selection beats overview','more words than table','chosen branch includes condition'],'reason':'Useful for taking one criterion-conditioned action.'}}
rank_case(38,3,'Rank six exact encodings for criterion lookup','Choose an encoding that lets a model reviewer recover the verdict for a stated coverage criterion without losing the common observations.',
 'The four-field card already preserves observations, criteria and reuse boundaries. The next input asks for a verdict under a named criterion; six viable encodings can express the same constructed comparison.',items,
 [('Condition preservation','Does it keep both scope conditions explicit?'),('Common-input visibility','Can the unchanged counts be found?'),('Serial independence','How well can it be read without cross-column context?'),('Comparison alignment','How directly can the two conditions be compared?'),('Economy','How little repeated material is needed?'),('Criterion lookup','Can a known criterion retrieve its verdict locally?')],[3,2,1,2,1,3],[2,2,4,1,1,4],
 '''The actual six encodings are:

S. “A includes two cases and B three; B meets a three-case requirement, while A uses fewer cases when only the two shared cases are required.”

B. Shared input: A has two cases, B three. • Three required: B. • Shared two required: both sufficient; A uses fewer.

T. Shared input: A=2, B=3 cases.

| Requirement | Sufficient choice | Size comparison |
|---|---|---|
| All three | B | A lacks one required case |
| Shared two | Both | A uses fewer cases |

C. Card 1: A has two cases and B three. If all three are required, B is sufficient and A is not. Card 2: A has two cases and B three. If only their shared two are required, both suffice and A uses fewer cases.

F. Let cases(A)={a,b}, cases(B)={a,b,c}. If R={a,b,c}, R⊆cases(B) and R⊄cases(A). If R={a,b}, both contain R and |cases(A)|<|cases(B)|.

D. With A's two cases contained in B's three: if all three are required, choose B; if the shared two suffice, both qualify and A uses fewer cases. A different required set reopens this rule.

Dependencies: all encodings require the definitions of A/B and the criterion; each supplies them locally or through the declared shared input. No encoding must be read before another. The formal pair needs set notation; this explains a score, not a mandatory training sequence.

Sanity: T/B/C form the leading group for named-criterion lookup; S/F/D remain strong for other encounters. C loses economy while preserving independent excerpts, so its high lookup score does not imply overall brevity. Closely scored T/C/B can reverse under serial/excerpt weights; the explicit alternate calculation shows the change. High confidence: no encoding's score proves human preference, and the formal pair needs its notation convention. Low confidence: all top-three placements; most debatable C because repetition is either useful self-containment or burden. No score-based tie overrides a dependency; exact ties retain original order.

Five actual retrieval checks were performed on all six outputs: retrieve A=2 and B=3; answer the all-three case; answer the shared-two case; identify that the observation counts stay fixed; reject an unstated fourth required case. All six preserve these answers when read with their declared input/legend. An isolated table cell “B” loses the criterion; a whole row does not. An isolated formal verdict without the legend also loses the observed counts. The paired card survives its declared whole-card extraction. These differences are real encoding boundaries, but criterion-bearing excerpts and common-input preservation were already established in 019/021/023. The new table is used for the known-criterion lookup; it does not establish a new independent finding.''',
 'The prior card remains a strong answer and all six full encodings answer the finite questions correctly. Changing the entry representation here is local reuse, not new evidence that one organization is universally better.')
progress()
