from pathlib import Path
import itertools,json

ROOT=Path(__file__).resolve().parent
inputs=json.loads((ROOT/'conditions-handoff-inputs-before.json').read_text())
case=inputs['boc_input']
jobs={r['id']:r for r in case['jobs']}

def evaluate(order,setup=2,deadline_override=None):
    t=0;family=case['initial_family'];switches=0;timeline=[];completion={};misses=[]
    for name in order:
        job=jobs[name]
        if family!=job['family']:
            timeline.append({'kind':'setup','from':family,'to':job['family'],'start':t,'finish':t+setup})
            t+=setup;switches+=1;family=job['family']
        start=t;t+=job['duration'];completion[name]=t
        deadline=(deadline_override or {}).get(name,job['deadline'])
        timeline.append({'kind':'job','id':name,'start':start,'finish':t,'deadline':deadline})
        if t>deadline:misses.append(name)
    return {'order':list(order),'timeline':timeline,'completions':completion,'makespan':t,'sum_completion':sum(completion.values()),'mean_completion':sum(completion.values())/len(jobs),'switches':switches,'setup_occupancy':switches*setup,'deadline_misses':misses,'admissible':not misses}

def compare(setup=2,deadline_override=None):
    rows=[evaluate(p,setup,deadline_override) for p in itertools.permutations(jobs)]
    feasible=[r for r in rows if r['admissible']]
    best_make=min((r['makespan'] for r in feasible),default=None)
    best_mean_by_make={
        makespan:min(r['mean_completion'] for r in feasible if r['makespan']==makespan)
        for makespan in {r['makespan'] for r in feasible}
    }
    min_setup=min((r['setup_occupancy'] for r in feasible),default=None)
    for r in rows:
        # Match indicators supplement, never override, the declared lexicographic preference.
        r['preference_matches']=[r['admissible'],r['admissible'] and r['makespan']==best_make,r['admissible'] and r['mean_completion']==best_mean_by_make.get(r['makespan']),r['admissible'] and r['setup_occupancy']==min_setup,True]
        r['match_score']=sum(r['preference_matches'])
    ranked=sorted(rows,key=lambda r:(not r['admissible'],r['makespan'] if r['admissible'] else len(r['deadline_misses']),r['mean_completion'],r['setup_occupancy'],r['order']))
    for i,r in enumerate(ranked,1):r['rank']=i
    return {'setup':setup,'deadline_override':deadline_override or {},'all_orders':ranked,'feasible_count':len(feasible),'best_orders':[r['order'] for r in feasible if r['makespan']==best_make and r['mean_completion']==best_mean_by_make.get(best_make)]}

base=compare()
later=[compare(0),compare(1),compare(3),compare(2,{'B1':5}),compare(2,{'R2':9})]
out={'input_file':'conditions-handoff-inputs-before.json','base':base,'later_cases':later}
(ROOT/'conditions-handoff-boc-results.json').write_text(json.dumps(out,indent=2)+'\n')

def round_robin(durations,retained,horizon,quantum):
    remaining=dict(durations);ready=list(durations);t=0;trace=[];done={};allocated={j:0 for j in durations}
    while ready and t<horizon:
        j=ready.pop(0)
        need=remaining[j] if retained else durations[j]
        length=min(quantum,need,horizon-t)
        finish=t+length;allocated[j]+=length
        valid=length==need
        trace.append({'job':j,'start':t,'finish':finish,'progress_retained':retained,'completed':valid})
        if valid:done[j]=finish
        else:
            remaining[j]=need-length if retained else durations[j]
            ready.append(j)
        t=finish
    return {'trace':trace,'completions':done,'allocated_service':allocated,'valid_completions':len(done)}

u=inputs['uf_later_input'];whole=[];t=0
for j in u['initial_order']:
    whole.append({'job':j,'start':t,'finish':t+u['jobs'][j],'completed':True});t+=u['jobs'][j]
uf={'input':u,'discard_on_switch':round_robin(u['jobs'],False,u['horizon'],u['quantum']),'retain_on_switch':round_robin(u['jobs'],True,u['horizon'],u['quantum']),'whole_requests':{'trace':whole,'valid_completions':2},'selected_routes':{'discard_on_switch':'qs FIFO over whole requests; no time slicing','retain_on_switch_with_first_response_at_most_1':'qs round robin q=1','base_boc_input':'rso setup comparison inside td deadline admissibility; boc enumerates full finite space'}}
(ROOT/'conditions-handoff-uf-later-use.json').write_text(json.dumps(uf,indent=2)+'\n')
print(json.dumps({'base_feasible':base['feasible_count'],'base_best':base['best_orders'],'base_current':next(r for r in base['all_orders'] if r['order']==case['current_choice']),'later':[{k:r[k] for k in ('setup','deadline_override','feasible_count','best_orders')} for r in later],'uf_valid_completions':{'discard':uf['discard_on_switch']['valid_completions'],'retain':uf['retain_on_switch']['valid_completions'],'whole':2}},indent=2))
