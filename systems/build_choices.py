from write_records import save,BASE
import json,itertools
# Simulated stop control and authority independence.
events=['dispatch:A','stop','return:A','dispatch:B']
active=True;accepted=[];trace=[]
for e in events:
 if e=='stop':active=False
 elif e.startswith('return:') and active:accepted.append(e.split(':')[1])
 trace.append({'event':e,'active':active,'accepted':accepted.copy(),'dispatch_allowed':active})
(BASE/'stop-transition.json').write_text(json.dumps(trace,indent=2))
save('050-ltai-2','ltai','Propagate a stop through pending work','Change how a current cancellation affects a late result and subsequent dispatch.','A visible stop status is useful, but my initial minimal design changes only the displayed status; the acceptance and dispatch transitions still need the same condition.',
'''Task suitability: state transitions, queue inspection and duplicate detection are mechanically automatable; semantic redefinition of the goal requires review; declaring a user's consent remains human-led. This local simulation creates no new agent or external message.

Handoff contract: dispatch consumes active goal identity plus active flag and produces one pending work ID; return consumes the same ID and current active flag; output is accepted result or retained cancelled return. Endpoint is the root coordinator. Quality gate is evaluated at dispatch and acceptance, not merely in the dashboard.

Error recovery: late result after stop→retain historical output with cancelled status; attempted new dispatch after stop→reject; unknown work ID→reject; duplicate return→one retained identity; exhausted retry→root receives blocked status. Retry limit is one for a malformed return and zero after cancellation. Rollback retains the last accepted result as history without claiming it still serves the cancelled request.

Oversight: current active status is authoritative; root/user can stop; each event records the resulting state; review occurs on each returned result. A local transition can stop immediately between events. The model does not claim it can interrupt an unavailable external operation already running inside a tool.

Capability evolution at 0–6, 6–18 and 18+ months is unknown. No forecast is supplied. The portable preparation is a stop flag in both action gates plus an explicit pending-work endpoint. Moving this to unattended operation requires then-current evidence, not elapsed calendar time.

Actual four-event trace: dispatch A; stop; return A; attempt dispatch B. The revised model accepts no output after stop and disallows B. A display-only baseline would still accept A and dispatch B because its transitions did not read the flag. `stop-transition.json` preserves exact states. The actor retains current control in this finite model.''',
'The stop condition now controls acceptance and dispatch, so the late A return is not accepted and B is not dispatched.','The simulated cancellation affects conduct rather than only a status display. This is a transition correction, not a production kill-switch guarantee.','KEEP','A shared control predicate at both transition points has a concrete effect; a status-only view does not.','Test stop during a partial side effect; design a compensating action; distinguish pause from cancellation.')
save('050-ltai-3','ltai','Orchestrate a human setting change without pretending it happened','Change status attribution for a proposed change of time or setting.','A described plan to pause or move location can be useful; the assistant has no direct evidence that a person follows it.',
'''Input: a proposed contribution asks a person to compare a difficult text in a quieter setting after a pause. This is a design case with no actual person participating. Agent-suitable tasks: prepare two comparable passages and a reporting prompt. Agent-assisted: interpret reported differences. Human-led: decide whether, when and where to try. Human-only here: physically relocate and report private experience; the assistant cannot perform that action.

Handoff contract: trigger is the person's voluntary start; input is the two passages and a chosen setting; output is a reported comparison and its context; endpoint is the next actual user response. Quality gate keeps reported experience distinct from observed task performance. There is no autonomous continuation mechanism in this assignment, so the status is proposed, awaiting a real trigger.

Recovery: no response→remain pending, not success; user declines→stop the branch; conditions change→revise the trial; response is ambiguous→retain both interpretations or ask one material question; report conflicts with task result→keep both evidence types. Retry is zero for an unsolicited reminder; no external message is sent.

Oversight: the person chooses whether to perform the setting change; root sees pending status; no claim of bodily state, feeling or behavior is added. The return event, if it occurs, would be reviewed once with the original input and actual context.

Capability evolution: six-month, eighteen-month and longer horizons do not supply any evidence that the assistant can perform a bodily relocation or know unreported experience. Possible future host capabilities would need actual authorization and observation. The preparation now is a clear human/assistant boundary, not a forecast.

Applied representation: action status changes from the ambiguous "setting intervention" to "assistant prepared materials; human setting action unperformed; outcome unknown." The materials could be prepared, but an actual useful setting effect has not occurred in the evidence available here. The original human benefit objective is preserved as untested.''',
'The proposed setting change is represented as human-led and unperformed rather than as an executed assistant intervention.','No new beneficial effect beyond correct scope attribution is demonstrated. A useful human setting change remains an open candidate.','UNRESOLVED','Actor-specific states preserve the missing action; one intervention-complete label would erase it.','Wait for an actual volunteered attempt; compare same-setting repetition; examine whether prepared materials alone help.')
options={'direct':{'cost':2,'coverage':2,'recoverable':1},'complete':{'cost':5,'coverage':4,'recoverable':1},'duplicate_complete':{'cost':7,'coverage':4,'recoverable':1},'ephemeral_complete':{'cost':5,'coverage':4,'recoverable':0}}
dirs={'cost':-1,'coverage':1,'recoverable':1};relations=[]
for a,b in itertools.permutations(options,2):
 ds=[dirs[k]*(options[a][k]-options[b][k]) for k in dirs]
 if all(x>=0 for x in ds) and any(x>0 for x in ds):relations.append({'dominates':a,'dominated':b,'type':'strict' if all(x>0 for x in ds) else 'weak'})
front=[x for x in options if not any(r['dominated']==x for r in relations)]
(BASE/'dominance.json').write_text(json.dumps({'input_stipulated':options,'dimensions':dirs,'relations':relations,'frontier':front},indent=2))
save('144-dom-1','dom','Remove duplicate work without pretending all tradeoffs disappear','Change the candidate set through exact dominance rather than an ungrounded universal score.','A richer answer may justify more work. I would keep the plausible fuller candidates until a concrete comparison shows one adds no supported value.',
'''Options in this constructed instance: direct (cost 2, coverage 2, recoverable 1); complete (5,4,1); duplicate complete (7,4,1); ephemeral complete (5,4,0). Cost is minimized, coverage maximized, recoverability maximized. Values are declared case inputs, not measured human utility.

Pairwise execution is in `dominance.json`. Complete weakly dominates duplicate complete by lower cost with equal coverage and recoverability. Complete weakly dominates ephemeral complete by equal cost and coverage and better recoverability. Direct and complete do not dominate each other: direct costs less, complete covers more. There is no strict dominance across every dimension for these surviving alternatives.

Near-dominance: complete loses to direct on three work units; that cannot be dismissed as trivial without the user's context. Hidden-dimension checks: if duplication independently checks a high-risk error, its coverage/evidence score is no longer equal and the elimination fails; if recoverability adds exposure cost, that dimension must be added; if the time bound is three, complete is infeasible. Coverage and recoverability are distinct here—one describes current content, the other future recovery—but their real benefits can overlap and are not summed.

Applied choice set: remove duplicate complete and ephemeral complete only under the declared equality assumptions; retain direct and complete on the Pareto frontier. At a four-distinction requirement complete is selected; at a two-distinction requirement direct remains eligible and cheaper. The source's integration suggestions do not require inventing a single winner when the frontier has a real tradeoff.

Countercase: copied output that costs less but loses an essential exception does not dominate its source, because content is no longer equal.''',
'The option set loses two conditionally dominated variants and retains the real direct-versus-complete tradeoff.','The exact pairwise calculation removes stipulated redundant work while keeping a consequential cost/coverage choice visible.','KEEP','A Pareto relation records which dimension changes; one weighted total would hide the retained tradeoff.','Add independent verification value; impose a deadline; test uncertainty in the equality assumptions.')
save('consolidation-05','gd','Separate dynamic correction, exploration, cancellation and elimination','Change how four different system responses are selected for a live failure.','A generic instruction to adjust the process would blur the very different causes in the four new cases.',
'''Only sya1, sya2, ltai2 and dom1 enter. Candidate A groups all under "improve control." Candidate B keys them to the observed structure: delayed measurement→lower tested gain; observation starvation→bounded probes; cancellation→block acceptance and dispatch; equal-value extra work→conditional dominance elimination. Candidate C ranks the four by purported universal leverage; that ranking has no common evidence base.

B is selected and actually used in a later composite replay: a cancelled task with a pending stale correction is first blocked by ltai2's active-state gate, so sya1's gain does not justify continuing it. For an active task with delayed feedback, the gain comparison remains usable. For an active portfolio, sya2's probe preserves evidence access; dom1 removes the duplicate option only when no independent-verification benefit exists. These are retained exceptions from the original records, not new findings.

Content comparison preserves the scalar model's artificial units, the sequence model's fixed outcomes, the state-machine scope and the declared equality assumptions. Organization comparison rejects one catch-all "more rigorous" response. No human outcome evidence enters this consolidation.''',
'The next failure case is routed by its demonstrated structure, with cancellation preventing otherwise useful corrective work.','The combined replay does not use a favorable correction result to override a stopped goal, or dominance to delete an informative probe.','KEEP','Structure-trigger grouping preserves the four incompatible conditions; universal leverage ranking is unsupported.','Replay concurrent cancellation and return; vary resource budget; test an informative duplicate that survives dominance.')
# MCD weights fixed before scores in this code.
weights={'adequacy':.5,'burden':.3,'revisability':.2}
scores={'direct':[2,5,4],'structured':[5,3,5],'interactive':[5,2,4],'do_nothing':[1,5,5]}
def totals(w):return {k:sum(x*y for x,y in zip(w.values(),s)) for k,s in scores.items()}
base=totals(weights);sens=[]
for k in weights:
 for f in [.8,1.2]:
  w=weights.copy();w[k]*=f;z=sum(w.values());w={k:v/z for k,v in w.items()};sens.append({'changed':k,'factor':f,'weights':w,'totals':totals(w)})
(BASE/'mcd.json').write_text(json.dumps({'weights_declared_before_scores':weights,'scores':scores,'totals':base,'sensitivity':sens},indent=2))
save('145-mcd-1','mcd','Test a recommendation against explicit priority sensitivity','Change confidence in a method recommendation when criteria weights are only provisional.','The structured option looks promising for the present distinction task, but I have not tested how much that judgment depends on placing adequacy first.',
'''Decision: one current contribution among direct, structured, interactive and no change. Requester needs useful distinctions; assistant supplies work; affected reader bears attention cost. Required authority and factual integrity are hard constraints, not compensable scores. All four are considered before screening; an unauthorized execution option is excluded.

Criteria and predeclared analyst weights: adequacy .5, lower burden .3, revisability .2. Scale 1=does not supply the needed condition, 3=partial/extra convention, 5=directly supplies it; burden reverses direction so larger means less burden. Adequacy and revisability remain distinct, although real benefits are not measured. No stakeholder alignment is invented: the weights are provisional for this constructed assistant choice, so a user-specific optimum remains unresolved.

Scores by criterion: adequacy direct2, structured5, interactive5, no-change1; burden direct5, structured3, interactive2, no-change5; revisability direct4, structured5, interactive4, no-change5. These are explicit design judgments under a required four-way distinction, not observation data. Totals are direct3.3, structured4.4, interactive3.9, no-change3.0. Structured leads by .5 over interactive.

Six calculations vary each weight ±20% and renormalize; the artifact preserves all totals. Structured remains the winner in those local perturbations. With only adequacy weight a and burden 1−a, direct scores 5−3a and structured 3+2a; they tie at a=.4. Thus a larger reprioritization of burden reverses the recommendation.

Pessimistic case: if structured adequacy falls from5 to3, its total becomes3.4, only .1 above direct. If burden is actually2 as well, total3.1 loses to direct. The recommendation is locally weight-stable but sensitive to score validity.

Applied choice: structured remains the reversible working selection; claimed confidence narrows to the stated weights/scores. Unknown user attention valuation is retained rather than hidden in a numeric total.''',
'The selected structured option is now accompanied by an exact priority crossover and a score-validity dependency.','The calculation improves the scope of the recommendation, but user-aligned superiority remains untested because weights and scores are analyst inputs.','UNRESOLVED','A sensitivity table preserves the condition that can reverse the choice; a single total does not.','Obtain actual task adequacy evidence; compare a hard threshold design; inspect a preference change beyond ±20%.')
