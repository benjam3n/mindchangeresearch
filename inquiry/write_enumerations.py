from pathlib import Path
import itertools,json,collections,math
R=Path('/workspace/scratch/78b838bd97fc/mind-change-research/inquiry')
def sample(axes,n=60,seeds=()):
 combos=list(itertools.product(*axes.values()));chosen=list(dict.fromkeys(seeds));seen=set((i,v) for row in chosen for i,v in enumerate(row))
 while len(seen)<sum(map(len,axes.values())):
  row=max((r for r in combos if r not in chosen),key=lambda r:sum((i,v) not in seen for i,v in enumerate(r)))
  chosen.append(row);seen.update(enumerate(row))
 # Deterministic dispersed strata, not a claim of all pairwise coverage.
 for k in range(len(combos)):
  row=combos[(k*37)%len(combos)]
  if row not in chosen:chosen.append(row)
  if len(chosen)==n:break
 return chosen

def write(name,title,start,axes,origins,seeds,calc,edge_notes,later,limitations):
 rows=sample(axes,seeds=seeds);table=[];outputs=[]
 for i,row in enumerate(rows,1):
  d=dict(zip(axes,row));out=calc(d);outputs.append({'id':i,'input':d,**out});table.append('| '+str(i)+' | '+' | '.join(str(x) for x in row)+' | '+out['result']+' |')
 cov={k:{str(v):sum(r[j]==v for r in rows) for v in values} for j,(k,values) in enumerate(axes.items())}
 total=math.prod(map(len,axes.values()))
 text=f'''Intended mind change: {title}

Starting working judgment and concrete input: {start}

Original: ../sources/inquiry-se.original.md and separate receipt. Interpretation 3: find omissions in an already mapped space. Dimensions originate in the prior DD records and the exact features below; these are not an ungrounded textbook taxonomy. Granularity is REPRESENTATIVE: sixty distinct tuples are enumerated from a nominal {total}-cell grid. This is exhaustive only for the displayed tuples, not the whole grid. Hierarchical strata separate the central semantic/operational conditions, cover every declared value, then disperse remaining samples deterministically. Dependencies are pruned explicitly as N/A, not silently counted as viable options.

| Dimension | Values | Concrete input feature that generated it |
|---|---|---|
'''
 for (k,v),origin in zip(axes.items(),origins):text+=f'| {k} | {", ".join(map(str,v))} | {origin} |\n'
 text+='\n| # | '+' | '.join(axes)+' | Computed or qualified result |\n|---|'+'---|'*(len(axes)+1)+'\n'+'\n'.join(table)+'\n\n'
 text+='Cross-dimensional check: each row has all nine axes. The primary organization follows the first operational axis; remaining coordinates remain visible. A row can be semantically invalid even when every individual coordinate is allowed. N/A is a relation among coordinates, not an “Other” category that hides the condition. The calculation is a declared finite model and never an observed human response.\n\nTen explicitly inspected edge cases: '+ '; '.join(f'E{i+1}: {x}' for i,x in enumerate(edge_notes))+'.\n\n'
 text+='Coverage by dimension/value (actual counts):\n\n| Dimension | Values and item counts | Gap |\n|---|---|---|\n'
 for k,c in cov.items():text+=f'| {k} | '+', '.join(f'{v}: {n}' for v,n in c.items())+' | no missing declared value |\n'
 text+='''
Five completeness checks performed: (1) every declared axis appears in every tuple; (2) all declared values have nonzero representation; (3) sixty tuple keys are unique; (4) ten boundary questions are inspected against the stated calculation and examples; (5) nominal product size is compared with the actual sixty, retaining the unsampled-cross-interaction gap. No claim of full pairwise coverage or real-world completeness is made. “Other” count is zero within the declared fixture; unmodeled real-world variables remain outside it. The source floor is met by sixty items, nine dimensions, ten boundary cases and five actual checks, not by sixty paraphrases of one recommendation.

'''+limitations+'\n\nDistinct later application: '+later+'''

Actual mind change: The next investigation consumes the displayed conditional cases rather than only the central example. Already established parent findings remain unchanged.
Benefit: Coverage and boundary retention are demonstrated in the finite output. No independent new useful change or human effect is established merely by enumerating more cases.
Verdict: UNRESOLVED
Organization: Coordinate tables support comparisons; exact JSON inputs and outputs preserve retrieval without losing the qualified/N/A cases.
Next attempts: Test an unsampled cross-interaction that matters to the next question; change one declared criterion explicitly; inspect an actual observation before transferring the model to a person.
'''
 (R/name).write_text(text);(R/(name[:-3]+'.json')).write_text(json.dumps({'axes':axes,'coverage':cov,'nominal_product':total,'rows':outputs},indent=2)+'\n')
 assert len(rows)==60 and len(set(rows))==60 and all(n for c in cov.values() for n in c.values())
# 35 — semantic compatibility
axes={'p_left':[0,.5,1],'p_right':[0,.5,1],'proposition':['same','different'],'time':['same','different'],'actor':['same','different'],'maybe_sense':['positive','strict'],'sure_sense':['probability','expression'],'scope':['specified','unknown'],'use':['filter','navigation']}
def sem(d):
 same=all(d[x]=='same' for x in ['proposition','time','actor'])
 if same and d['p_left']!=d['p_right']:return {'result':'N/A: one aligned probability assigned two values'}
 if d['scope']=='unknown':return {'result':'source-scope verdict unresolved; fixture values retained'}
 left=d['p_left']==1 if d['sure_sense']=='probability' else True
 right=d['p_right']>0 if d['maybe_sense']=='positive' else 0<d['p_right']<1
 both=left and right
 return {'result':('joint witness' if both else 'not a joint witness')+('; keep as route candidate' if d['use']=='navigation' else '; this instance only'),'left':left,'right':right,'joint':both}
seeds=[(1,1,'same','same','same','positive','probability','specified','filter'),(1,1,'same','same','same','strict','probability','specified','filter'),(0,0,'same','same','same','positive','probability','specified','filter'),(.5,.5,'same','same','same','strict','expression','specified','filter'),(1,.5,'different','same','same','strict','probability','specified','filter'),(1,.5,'same','different','same','strict','probability','specified','filter'),(1,.5,'same','same','different','strict','probability','specified','filter'),(1,.5,'same','same','same','strict','probability','specified','filter'),(1,1,'same','same','same','positive','probability','unknown','filter'),(1,1,'same','same','same','strict','probability','specified','navigation')]
write('35-se-semantic-boundaries.md','Retain the full declared range of certainty/possibility cases, especially endpoint and operand-alignment exceptions.', 'AEX33 established one overlap at p=1 and prepared paired-semantic-instances.json. I had not enumerated how that overlap interacts with actor, time, source scope or a quoted confidence expression. The exact sure/maybe exports and DD03/04 uncertainty and representation axes are the inputs.',axes,['AEX33 sure probability','AEX33 maybe probability','RLCL14 different objects','RLCL14 different times','Source leaves speaker unspecified','AEX33 chance versus strict uncertainty','FCTL12 factive versus confidence expression','Methods overlay has null scope','SPD08 navigation versus semantic exclusion'],seeds,sem,['p=0 fails both probability predicates','p=1 satisfies sure and positive possibility','p=1 fails strict uncertainty','.5 with confidence expression can satisfy strict uncertainty','different propositions allow unequal probabilities','different times allow changed probabilities','different actors allow different assigned probabilities','same actor/object/time with unequal assigned p is N/A','unknown source scope does not become specified through a fixture','a non-witness can still be a navigation candidate'],'U38 receives row1 and row2 as two genuinely different senses; QAF46 treats the source-intent question separately from their exact arithmetic. Row1 is retained, fulfilling AEX33’s prepared-input change.','A non-witness at one p is not a proof of universal incompatibility. For the aligned probability/strict pair, emptiness follows from p=1 and p<1, independently of sample count. For source intent no number of stipulated rows supplies missing context.')
# 36 — timing and price
axes={'p':[.4,.75,.9],'cost':[0,1,4],'arrival':['before','after'],'choice':['contingent','forced-act'],'criterion':['expected','worst-state'],'channel':['present','absent'],'quality':['perfect','unspecified-noisy'],'budget':['sufficient','insufficient'],'status':['current','future-unobserved']}
def timing(d):
 if d['status']=='future-unobserved':return {'result':'future execution unobserved; no performed-value claim'}
 if d['channel']=='absent' or d['budget']=='insufficient':return {'result':'wait infeasible; compare feasible current choices'}
 if d['quality']=='unspecified-noisy':return {'result':'need observation likelihood; price alone insufficient'}
 p=d['p'];c=d['cost'];act=10*p-4
 if d['criterion']=='worst-state':
  now=max(-4,0);wait=-c if d['arrival']=='after' or d['choice']=='contingent' else -4-c
 else:now=max(act,0);wait=-c if d['arrival']=='after' else (6*p-c if d['choice']=='contingent' else act-c)
 return {'result':f'best-now={now:g}; wait={wait:g}; '+('wait better' if wait>now else 'tie' if wait==now else 'now better'),'best_now':now,'wait':wait}
seeds=[(.9,1,'before','contingent','expected','present','perfect','sufficient','current'),(.75,1,'before','contingent','expected','present','perfect','sufficient','current'),(.4,1,'before','contingent','expected','present','perfect','sufficient','current'),(.9,0,'before','contingent','expected','present','perfect','sufficient','current'),(.4,1,'after','contingent','expected','present','perfect','sufficient','current'),(.9,1,'before','forced-act','expected','present','perfect','sufficient','current'),(.4,1,'before','contingent','worst-state','present','perfect','sufficient','current'),(.9,1,'before','contingent','expected','absent','perfect','sufficient','current'),(.9,1,'before','contingent','expected','present','unspecified-noisy','sufficient','current'),(.9,1,'before','contingent','expected','present','perfect','insufficient','current')]
write('36-se-timing-boundaries.md','Compare information price, decision flexibility and opportunity timing across the declared decision space.','AEX34 showed act dominates paid perfect information on [.8,.9] under expected payoff. That result assumes timely delivery and a contingent action. The source timing map and actual capsule distinguish active execution from an unobserved future event; no scheduling event is supplied.',axes,['AEX34 tested values and tie','AEX34 observation price','Capsule expiry invalidation','Perfect information requires ability to decline','Declared expected payoff versus robust alternative','DD05 initiating channel','Perfect versus uncalibrated observation','Resource constraint for observation','Actual capsule status'],seeds,timing,['high-p paid information loses','p=.75 gives exact tie at cost1','p=.4 paid information improves current zero payoff','zero-cost information weakly improves expected choice','late information loses the opportunity','forced act prevents contingent value','worst-state criterion may prefer decline','absent channel blocks wait','noisy signal without likelihood is unresolved','insufficient budget blocks purchase'],'FRQ42 asks for the precise price/quality/choice inputs before recommending delay. It uses row9’s missing-likelihood result as a live gap and row2 as an exact tie boundary.','The worst-state comparison uses a different explicitly declared objective, not uncertainty about which arithmetic is true. Constant p and fixed payoffs are held throughout the base calculation; real preference or expiry observations are absent.')
# 37 — source-clause access
axes={'clauses':[3,6,12],'window':[1,3,6],'critical':['first','middle','last'],'view':['prefix','targeted'],'force':['mandatory','suggested'],'exception':['present','absent'],'overlap':[0,1],'source':['current','stale'],'actor':['model-fixture','human-proposal']}
def attention(d):
 n=d['clauses'];critical={'first':0,'middle':n//2,'last':n-1}[d['critical']];w=min(d['window'],n)
 shown=list(range(w)) if d['view']=='prefix' else list(range(max(0,min(critical,n-w)),max(0,min(critical,n-w))+w))
 exception=max(0,critical-1) if d['exception']=='present' else None
 if d['overlap'] and shown[0]>0:shown=[shown[0]-1]+shown
 visible=critical in shown;ex=exception is None or exception in shown
 if d['actor']=='human-proposal':result='display computed; human notice/use unobserved'
 elif d['source']=='stale':result='visible bytes do not establish current requirement'
 elif not visible:result='critical clause absent from shown indices'
 elif not ex:result='clause visible; limiting exception missing'
 else:result=f'qualified {d["force"]} clause visible in fixture'
 return {'result':result,'shown_indices':shown,'critical_index':critical,'exception_index':exception,'clause_visible':visible,'exception_visible':ex}
seeds=[(12,1,'last','prefix','mandatory','present',0,'current','model-fixture'),(12,1,'last','targeted','mandatory','present',0,'current','model-fixture'),(12,1,'last','targeted','mandatory','present',1,'current','model-fixture'),(3,6,'last','prefix','mandatory','present',0,'current','model-fixture'),(6,3,'middle','prefix','suggested','absent',0,'current','model-fixture'),(6,3,'middle','targeted','suggested','absent',0,'current','model-fixture'),(3,1,'first','prefix','mandatory','absent',0,'current','model-fixture'),(12,6,'last','targeted','mandatory','present',0,'stale','model-fixture'),(12,1,'last','targeted','mandatory','absent',0,'current','human-proposal'),(6,1,'middle','targeted','suggested','present',1,'current','model-fixture')]
write('37-se-clause-access.md','Distinguish a visible instruction from a visible instruction together with its limiting exception.','DD04 observed a genuinely truncated combined read and repaired it with smaller reads. That shows access to a source is different from the displayed segment. The new finite input is a sequence of clauses in which an exception precedes a selected mandatory/suggested clause; this is a designed retrieval fixture, not an experiment on human attention.',axes,['Actual source lengths vary','Tool output has bounded visible segments','Required invocation can appear late','Separate targeted reads repaired truncation','Original source distinguishes INVOKE from Next Steps','RCA13/SDC31 have limiting conditions','Adjacent clause can be lost at chunk boundary','Capsule hash check identifies version role','No human attention observation'],seeds,attention,['late clause outside prefix','targeted one-clause read can omit preceding exception','one-clause overlap restores that exception','window longer than file covers all indices','middle clause may lie just past prefix boundary','targeted window includes middle clause','first clause with no exception fits one slot','stale source remains stale when visible','computed human display is not observed attention','suggested clause stays suggested after added overlap'],'U40 receives the exact row2/3 distinction: selecting the critical clause alone can still remove its preceding qualifier. It will compare qualified-clause units with raw clause counts; no human benefit is assumed.','The finite retrieval function reports visibility only. It does not infer comprehension, correctness of the source or adherence by any reader. The new adjacent-exception case is evaluated later before any independent KEEP; mere visibility counts are insufficient.')
print('Wrote three enumerations: 60 unique tuples each, nine dimensions and all declared values covered.')
