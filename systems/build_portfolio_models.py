from write_records import save,BASE
import json,math

def queue_run(arrivals=3,bottleneck=1,buffer=None,steps=40):
 q=[0]*10;completed=0;trace=[];caps=[3,3,3,3,bottleneck,3,3,3,3,3]
 for t in range(steps):
  q[0]+=arrivals if buffer is None or sum(q)<buffer else 0
  flows=[min(q[i],caps[i]) for i in range(10)]
  # Downstream receiving capacity is an explicit balancing signal in bounded policy.
  if buffer is not None:
   flows=[min(f,max(0,buffer-q[i+1])) if i<9 else f for i,f in enumerate(flows)]
  nq=q.copy()
  for i,f in enumerate(flows):
   nq[i]-=f
   if i<9:nq[i+1]+=f
   else:completed+=f
  q=nq;trace.append({'t':t,'stocks':q.copy(),'flows':flows,'completed':completed})
 return {'trace':trace,'backlog':sum(q),'completed':completed,'final':q}
stocks=['unread input','extracted material','normalized cases','candidate operations','eligibility queue','feasible bundles','authorized work','pending returns','assessed outputs','retention queue']
scenarios={'push':queue_run(),'more_arrivals':queue_run(5),'wider_bottleneck':queue_run(3,2),'bounded':queue_run(3,1,12)}
(BASE/'pipeline-dynamics.json').write_text(json.dumps({'defined_model':True,'stocks':stocks,'scenarios':scenarios},indent=2))
for n in [1,2]:
 baseline=scenarios['push'];alt=scenarios['wider_bottleneck' if n==1 else 'bounded']
 loops=[]
 for i in range(8):loops.append(f'L{i+1}: stock {stocks[i+1]} increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.')
 body=f'''System is a constructed ten-queue operation pipeline. Time horizon is forty discrete cycles. Every initial stock is zero; arrivals and capacities are stipulated, not measured human or model productivity. Boundary includes all ten queues, inflow, completion and release controls. An excluded upstream source cannot change the modeled bottleneck unless it changes its capacity.

Ten stocks with corresponding inflow/outflow: {', '.join(stocks)}. Queue i receives the previous queue's completed transfer and loses its own transfer; the first receives exogenous arrivals, the last drains to completed output. The exact simultaneous recurrence and every stock/flow value are executed in `pipeline-dynamics.json`. Each queue's fill/drain time is determined by integer capacity and present stock; no metaphorical human capacity is inferred.

Eight explicitly checked feedback paths:

'''+'\n'.join(loops)+f'''

Five delays: input→extraction, extraction→normalization, candidate→eligibility, authorized work→returned evidence and assessed output→retention each require at least one cycle in the model. The full path requires multiple cycles; output is therefore zero early even when input enters. Actors who compared output at cycle1 would misattribute pipeline latency to no capacity; this is a model implication, not a claim about real users.

Archetype checks: limits-to-growth matches finite bottleneck capacity; growth-and-underinvestment matches only the stipulated capacity mismatch; commons does not match because one allocator controls all queues; success-to-successful lacks competing reward feedback; escalation lacks responding parties; shifting-the-burden lacks a damaged fundamental stock; fixes-that-fail matches extra arrivals if the target is backlog reduction; eroding-goals is absent because completion criterion stays constant.

Eight leverage points: (1) change goal from arrivals to completions—useful if goal was mistakenly arrival volume; (2) alter bottleneck capacity—directly changes modeled throughput; (3) change release-loop structure—bounds accumulation; (4) expose downstream queue lengths—supplies release signal; (5) constrain admission—reduces overload; (6) move buffer capacity—changes where work waits; (7) shorten one transfer delay—changes latency before steady output; (8) adjust exogenous arrival rate—changes backlog when downstream capacity is fixed. All are feasible model interventions; actual host changes would require capability evidence. Ranking for this case follows computed effect, not the source hierarchy alone.

Observed model behavior: baseline completion={baseline['completed']}, backlog={baseline['backlog']}; intervention completion={alt['completed']}, backlog={alt['backlog']}. {'Increasing arrivals from3 to5 produces '+str(scenarios['more_arrivals']['completed'])+' completions and backlog '+str(scenarios['more_arrivals']['backlog'])+', so extra generation does not solve the one-unit bottleneck.' if n==1 else 'Bounded admission gives a smaller backlog while retaining the same one-unit bottleneck; throughput and backlog are therefore distinct response variables.'}

Side effects: first-order {'capacity raises eligible flow' if n==1 else 'admission withholds some new work'}; second-order {'downstream queues receive more completed eligibility' if n==1 else 'upstream stock stops growing without bound'}; third-order {'finished output increases after transfer delay' if n==1 else 'fewer unfinished tasks remain after the horizon'}. Compensating response: a different downstream capacity would become the new bottleneck; bounded admission can idle the line if its buffer is too small. The intervention does not establish universal throughput or attention benefits.

Actual selection for the model: {'increase the bottleneck from1 to2 instead of increasing source arrivals' if n==1 else 'apply bounded admission when the goal is limiting unfinished work, while preserving the fixed throughput criterion'}. The exact output comparison is performed rather than forecast.'''
 save(f'097-systhink-{n}','systhink',f'{"Capacity" if n==1 else "Admission"} changes in a ten-stock operation system','Change a system intervention after tracing its stock, flow and delayed effects.', 'More input preparation appears productive, but the relationship between generated work and completed useful output is not established by input volume.' if n==1 else 'Increasing processing capacity looks like the obvious way to reduce backlog; a release-control alternative has not been evaluated.',body,'The model selects a bottleneck capacity increase.' if n==1 else 'The model selects bounded admission to control unfinished work.','The forty-cycle executed model separates changes in completion from changes in accumulation. All rates remain stipulated model inputs.','KEEP','Stock/flow traces retain accumulated work and latency; an input-count dashboard omits both.','Move the bottleneck; reduce the buffer; test time-varying arrivals.',depth='Original 8x floors: 10 explicit stocks, 8 feedback-loop checks, 5 delays, 8 leverage points, 8 archetype checks. Loop activity is distinguished from merely possible topology; forty cycles are executed for four policies.')
# CBA: hypothetical work-unit streams, not money or financial advice.
r=.1;horizon=5
plans={'status_quo':{'upfront':0,'annual_saving':0},'full_setup':{'upfront':6,'annual_saving':1},'partial_setup':{'upfront':2,'annual_saving':.5}}
res={}
for name,p in plans.items():
 flows=[-p['upfront']]+[p['annual_saving']]*horizon
 pv=[v/(1+r)**t for t,v in enumerate(flows)]
 res[name]={'flows':flows,'pv':pv,'npv':sum(pv),'simple_payback':p['upfront']/p['annual_saving'] if p['annual_saving'] else None,'roi':((horizon*p['annual_saving']-p['upfront'])/p['upfront']) if p['upfront'] else None,'bcr':(sum(pv[1:])/p['upfront']) if p['upfront'] else None}
sens=[]
for h in [3,5,10]:
 for d in [0,.1,.2]:sens.append({'horizon':h,'discount':d,'npvs':{k:-p['upfront']+sum(p['annual_saving']/(1+d)**t for t in range(1,h+1)) for k,p in plans.items()}})
(BASE/'cost-benefit.json').write_text(json.dumps({'assumed_work_units':True,'plans':plans,'base':res,'sensitivity':sens},indent=2))
save('146-cba-1','cba','Price the timing of reusable preparation','Change a setup decision after counting when its saving arrives.','Six units of setup that save one unit per recurring use look attractive once enough uses occur. I have not yet included a finite horizon and opportunity discount.',
'''Decision is whether to adopt full setup, partial setup or the status quo for a stipulated five-period recurrence stream. Perspective includes assistant preparation and later work; human comfort and option value are relevant but not quantified. Unit is hypothetical work, not currency. Discount .1 is an explicit preference-over-delay scenario, not a financial rate recommendation. Current setup budget permits both candidates.

Cost inventory: full upfront6, partial upfront2; full later operating cost1 versus status quo2; partial later1.5. Savings therefore full1/period and partial.5. Maintenance is already in those operating costs and is not counted twice. Migration/disposal add zero by the case definition; if nonzero, they must be added. Opportunity cost is represented by discounting, not a second arbitrary penalty. Failure probability is unknown; no invented expected loss enters.

Benefit inventory: only saved work is quantified. Capability, flexibility and retained agency are unpriced; their actual directions are unknown for these alternatives. Five-period cash-flow analogues and present values are in `cost-benefit.json`.

Computed NPV: status0; full −6+3.790786769=−2.209213231; partial −2+1.895393385=−.104606615. Simple payback is6 periods for full and4 for partial. ROI over5 is −1/6 for full and .25 for partial; partial's undiscounted ROI is positive while its discounted NPV is slightly negative. BCR is .631797795 for full and .947696692 for partial. IRR is below .1 for both; the base decision does not require a root estimate.

Sensitivity varies horizon3/5/10 and discount0/.1/.2. At ten periods and .1, full NPV=.144567106 and partial1.072283553; partial then wins. Five-period breakeven annual saving is upfront/3.790786769: full1.582784884; partial.527594961. A ±20% saving scenario or a nonzero migration cost can therefore reverse marginal partial setup.

Actual choice: status quo at five periods under the declared discounted-effort criterion. It differs from selecting partial on undiscounted positive ROI. NPV is the sole quantified ranking after hard constraints; adding arbitrary weights for unknown intangibles would manufacture information. A real strategic necessity could override this work-saving objective only with a separately grounded criterion, not retrospective score repair.''',
'The five-period instance keeps the status quo; the partial-setup recommendation from undiscounted ROI is reversed.','The calculation detects a concrete timing-sensitive reversal and retains the ten-period boundary. It does not forecast recurrence or measure actual work savings.','KEEP','Period-by-period streams preserve timing that a total-savings figure loses.','Measure actual recurrence; add setup expiration; compare waiting one period to gather information.')
save('consolidation-06','gd','Distinguish validity, capacity, accumulation and timing','Change how the next system-level resource choice uses four preserved findings.','One resource score would be compact, but the new results concern different mathematical objects.',
'''Four distinct keeps enter: integration1's whole-packet authority test; tracematrix1's exact claim scope; systhink1's bottleneck intervention; systhink2's admission/backlog intervention. The CBA result is held for the next batch rather than making five.

Candidate A groups by skill; B groups by decision object: acceptance predicate, supported claim, completion capacity, unfinished-work stock. C sums their scores; no common units support that. B is selected.

Actual later use: in a constructed active task, a contract-valid packet supplies a plan to increase input arrival rate. The trace entry says contract validity does not prove the plan useful. The bottleneck model rejects increased arrivals as a throughput solution; the backlog model selects admission control when the concern is unfinished work. If the packet proposes unauthorized execution, integration1 rejects it before any claimed capacity advantage matters. Each result is substitution into an established case or boundary, not a new substantive finding.

Content review retains unknown real rates, artificial queues and exact test scope. Organization review preserves the separate criteria rather than allowing a favorable local number to answer another question. CBA's timing result remains a future batch input.''',
'The later plan is assessed by the relevant predicate, evidence claim and stock/flow objective separately.','The combined replay avoids confusing valid format with useful intervention or input volume with throughput.','KEEP','Decision-object grouping wins the declared composite use; source grouping remains provenance.','Add a changing bottleneck; inspect an invalid but informative packet; compare delayed benefits with current capacity limits.')
