from write_records import save,BASE
import json,math

def table(h,rs):return '| '+' | '.join(h)+' |\n|'+ '|'.join(['---']*len(h))+'|\n'+'\n'.join('| '+' | '.join(str(x).replace('|','/') for x in r)+' |' for r in rs)
# 100 distinct lifecycle activities; costs are a declared unit-operation model, not empirical estimates.
req1=json.loads((BASE/'requirements-1.json').read_text());req2=json.loads((BASE/'requirements-2.json').read_text())
phases=[('concept',0,10),('development',0,20),('deployment',1,20),('operations',2,20),('support',3,20),('retirement',5,10)]
labels=[r['requirement'] for r in req1]+[r['requirement'] for r in req2[:20]]
factors={'direct':[1,0,1,5,2,1],'compiled':[2,4,2,1,2,2],'hybrid':[1,2,2,2,1,1],'batch':[1,1,1,3,3,2]}
items=[];pos=0
for pi,(phase,year,count) in enumerate(phases):
 for k in range(count):
  # One logical work unit per specified atomic activity; alternative factors represent repeated operations.
  name=labels[pos];pos+=1
  items.append({'id':f'LC-{pos:03}','phase':phase,'year':year,'element':phase+' activity: '+name,'base_operations':1,'method':'declared operation-count buildup','basis':'one activity in the finite synthetic lifecycle; repeated counts supplied per alternative','confidence':'exact within stipulated model; real cost unknown','costs':{a:fs[pi] for a,fs in factors.items()},'recurring':phase in ['operations','support']})
r=.1
def compute(mult=None):
 mult=mult or {};return {a:sum(x['costs'][a]*mult.get(x['phase'],1)*mult.get('group'+str((int(x['id'][3:])-1)%6),1)/(1+r)**x['year'] for x in items) for a in factors}
base=compute();sens=[]
for field in [p[0] for p in phases]+['group'+str(i) for i in range(6)]:
 vals=[compute({field:f}) for f in [.8,1.2]];sens.append({'factor':field,'low':vals[0],'high':vals[1],'hybrid_swing':vals[1]['hybrid']-vals[0]['hybrid']})
sens.sort(key=lambda x:x['hybrid_swing'],reverse=True)
risks=['source disappears','criterion changes','setup expires','recurrence absent','input format changes','authority changes','duplicate work','restoration needed','migration loses scope','host unavailable','maintenance ignored','retirement provenance lost']
summary={a:{p[0]:sum(x['costs'][a] for x in items if x['phase']==p[0]) for p in phases} for a in factors}
artifact={'phases':phases,'alternatives':factors,'items':items,'nominal_phase_costs':summary,'discount':r,'npv_costs':base,'sensitivities':sens,'risks':risks,'recommended_in_model':min(base,key=base.get)}
(BASE/'lifecycle-cost.json').write_text(json.dumps(artifact,indent=2))
save('147-lcca-1','lcca','Expose full-lifecycle effort behind a cheap first interaction','Change how a method-system design accounts for development, repeated use and retirement.','The direct method has low preparation effort. I have not yet compared its repeated-operation burden with setup-heavy alternatives through retirement.',
 f'''Scope is a finite synthetic lifecycle of a conditional-operation system. Service horizon is five periods, base period0, constant work units, no monetary inflation. Discount .1 is an explicitly declared opportunity scenario. Four alternatives are direct, compiled, hybrid and batch; the names describe where repeated work occurs, not external products.

Six phases: concept(0), development(0), deployment(1), operations(2), support(3), retirement(5). One hundred distinct activities are identified. Each activity costs one logical operation multiplied by the alternative's declared repetition count; this is an engineering buildup in the model, not a labor estimate or observed runtime. Exact identity, basis, timing and confidence appear in `lifecycle-cost.json`.

{table(['ID','Phase','Activity','Direct','Compiled','Hybrid','Batch'],[[x['id'],x['phase'],x['element']]+[x['costs'][a] for a in factors] for x in items])}

{table(['Alternative']+[p[0] for p in phases]+['Discounted total'],[[a]+[summary[a][p[0]] for p in phases]+[round(base[a],6)] for a in factors])}

Present value is computed as sum of each activity's cost/(1.1)^year. Recurring operations/support are distinct from one-time concept/development/deployment/retirement. Acquisition cost and total cost are therefore different comparison objects. The model's lowest total is {min(base,key=base.get)}; all alternatives preserve the same declared required activities, with no claim of equivalent real quality.

Twelve one-way sensitivity factors are executed: six phases and six disjoint activity bundles. Each varies ±20%; the top three hybrid-cost swing factors are {', '.join(x['factor'] for x in sens[:3])}. Best/worst cost scenarios apply .8/1.2 to the same declared activity counts; no probability or "most likely" label is invented. A different recurrence profile or quality requirement can change the ranking.

Twelve risk items: {', '.join(risks)}. Their impact is additional operation, loss of usable benefit or rework; likelihood and real magnitude are unknown. They are not assigned fabricated dollar expected values. Reduction opportunities are to avoid repeated normalization, preserve a valid reusable setup and retire only with provenance. Each requires actual input validity; removal of mandatory work to lower cost is disallowed.

Actual transformed choice: the design comparison now retains all six phases and shows the lowest first-stage effort is not sufficient to choose a lifecycle alternative. The conditional model selects {min(base,key=base.get)}, but a real implementation choice remains unresolved until recurring use and activity costs are observed.''',
'The candidate comparison now uses a six-phase, hundred-activity discounted model instead of acquisition effort alone.','The lifecycle model is computed and inspectable; actual cost superiority is unresolved because the operation counts and recurrence are scenario inputs.','UNRESOLVED','Phase/activity breakdown preserves maintenance and retirement; a setup-only figure loses them.','Measure one real recurrence; vary service life; test loss of setup validity.',depth='Original 8x floors: 100 cost elements, 6 phases, 4 alternatives, 12 computed sensitivity factors and 12 risk items. All costs are explicitly synthetic operation counts, not fabricated real estimates.')
# RAM: fifty distinct operational responsibilities from the decomposition.
dec=json.loads((BASE/'decomposition-1.json').read_text());leaves=[x for x in dec['nodes'] if x['level']==4]
comps=[]
for i,x in enumerate(leaves):
 lam=.002 if i==0 else .00005
 comps.append({'id':x['id'],'component':x['name'],'quantity':1,'lambda':lam,'mtbf':1/lam,'distribution':'exponential by model definition','source':'stipulated stochastic model, not field data','confidence':'mathematical conditional only'})
lam=sum(x['lambda'] for x in comps);mtbf=1/lam;mission=10
mttr=2;logistics=8;admin=1;pmrate=.01;pmtime=1
Ai=1/(1+lam*mttr);Aa=1/(1+lam*mttr+pmrate*pmtime);Ao=1/(1+lam*(mttr+logistics+admin)+pmrate*pmtime)
choices={'baseline':Ao,'repair_half':1/(1+lam*(1+logistics+admin)+pmrate*pmtime),'logistics_to2':1/(1+lam*(mttr+2+admin)+pmrate*pmtime),'lambda_minus10pct':1/(1+lam*.9*(mttr+logistics+admin)+pmrate*pmtime)}
failures=[]
for i,c in enumerate(comps):failures.append({'id':f'FM-{i+1:02}','component':c['component'],'mode':'unavailable result','effect':'series mission stops','severity':8,'occurrence':'unknown in reality','detection':'missing output observed','RPN':'not computed without ordinal occurrence evidence','mitigation':'restore required output or remain blocked'})
for i,c in enumerate(comps[:10]):failures.append({'id':f'FM-{51+i:02}','component':c['component'],'mode':'plausible but incorrect output','effect':'downstream accepts wrong premise','severity':9,'occurrence':'unknown','detection':'semantic countercase or review','RPN':'not computed','mitigation':'independent premise check and descendant invalidation'})
maint=[{'id':f'MT-{i+1:02}','task':('restore '+c['component']) if i<20 else ('review changed condition for '+c['component']),'level':'local operator' if i<20 else 'evidence reviewer','frequency':'on detected failure' if i<20 else 'on condition change','duration':'aggregate model MTTR=2; per-task real duration unknown','tools':'source/evidence access','access':'available only if source exists'} for i,c in enumerate(comps[:30])]
improvements=['reduce waiting for source access','retain recoverable previous version','prevalidate schema','separate historical and current state','detect missing mandatory output','deduplicate retries','bound repair retries','compare independent evidence','identify common-cause source','avoid unnecessary serial gate','co-locate tightly coupled predicates','make current revision explicit','separate preventive from corrective work','retain failure and repair evidence','recheck authority after recovery']
Rseries=math.exp(-lam*mission);Rparallel=(1-(1-math.exp(-.002*mission))**2)*math.exp(-49*.00005*mission)
Rcommon=math.exp(-.001*mission)*(1-(1-math.exp(-.001*mission))**2)*math.exp(-49*.00005*mission)
artifact={'components':comps,'failure_modes':failures,'maintenance_tasks':maint,'improvements':improvements,'lambda_system':lam,'mtbf':mtbf,'mission':mission,'R_series':Rseries,'R_first_redundant_independent':Rparallel,'R_redundant_commoncause':Rcommon,'Ai':Ai,'Aa':Aa,'Ao':Ao,'availability_choices':choices}
(BASE/'ram-model.json').write_text(json.dumps(artifact,indent=2))
save('148-ram-1','ram','Separate recovery work from recovery delay','Change which reliability investment is preferred when waiting dominates downtime.','Reducing repair time seems a direct way to improve availability. I have not yet separated active repair from logistics and administrative delay.',
 f'''System: fifty required operational responsibilities, on-demand mission of10 model hours, all initially available. This is a synthetic stochastic model with explicitly stipulated exponential failures. No production service, human safety deployment or empirical failure rate is claimed. Target mission reliability .99 and operational availability .98 are declared design scenarios, not external standards.

Fifty components and rates:

{table(['Component','Responsibility','lambda','MTBF','Basis'],[[c['id'],c['component'],c['lambda'],c['mtbf'],'stipulated exponential'] for c in comps])}

Series model requires all fifty outputs. System lambda={lam}, MTBF={mtbf}, R(10)={Rseries}. The .99 mission target is not met. Duplicating the largest-rate component with independent failures yields {Rparallel}; adding the declared common-cause component yields {Rcommon}. Copying the same source is therefore not automatically independent redundancy. Independence and exponential stationarity are model assumptions needing field validation.

Sixty failure modes and thirty maintenance tasks are fully listed in `ram-model.json`: fifty unavailable-output modes plus ten distinct plausible-but-wrong modes. Unavailable failures block a series path; plausible false output is a correctness failure a pure uptime model misses. Severity ordinals are design judgments. Occurrence is unknown; RPN is not invented from nonexistent evidence. The source's requested RPN field therefore remains uncomputed for real risk ranking.

Maintenance concept separates local restore, intermediate evidence review and source/host recovery. Per-task real times are unknown; the aggregate model uses corrective repair2, logistics8, administration1, preventive rate .01 and preventive duration1. Achieved/operational availability use the declared event-frequency renewal model: uptime fraction=1/(1+lambda×downtime_per_corrective_event+preventive_rate×preventive_duration).

Computed Ai={Ai}, Aa={Aa}, Ao={Ao}. Compared interventions: {json.dumps(choices)}. Reducing logistics8→2 produces a larger availability increase than halving active repair2→1 under these inputs. Fifteen improvement actions are retained: {', '.join(improvements)}. Implementation costs and monetary ROI are unknown; no payback claim is made.

Actual model choice: prioritize reducing waiting for the required source/host over shaving one hour of active repair. First detect whether the eight-hour logistics input is real before implementing a production change. The finite calculation changes the current investigation target while leaving field reliability unproven.''',
'The model selects the logistics-delay reduction as the more consequential availability lever under the given downtime decomposition.','The exact availability calculation prevents active repair time from standing in for total recovery delay. Real intervention benefit depends on observed downtime components.','KEEP','Series reliability, semantic failure and downtime decomposition remain separate views; one reliability score conflates them.','Measure actual delay distribution; test common-cause failures; compare repair investment costs.',depth='Original 8x floors: 50 analyzed components, 60 failure modes, 30 maintenance tasks, 15 improvement actions. Real rates and RPN remain unmeasured; only the stipulated mathematical model is calculated.')
