from pathlib import Path
import json,itertools,datetime,hashlib
from fractions import Fraction

BASE=Path(__file__).resolve().parent
INPUTS=json.loads((BASE/'systems-handoff-inputs-before.json').read_text())
def save(name,obj):
    obj['executed_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    obj['input_artifact_sha256']=hashlib.sha256((BASE/'systems-handoff-inputs-before.json').read_bytes()).hexdigest()
    (BASE/name).write_text(json.dumps(obj,indent=2))

def orbit(seed):
    seen={};states=[];x=seed
    while x not in seen:
        seen[x]=len(states);states.append(x)
        x=''.join(str(int(x[i])^int(x[(i+1)%len(x)])) for i in range(len(x)))
    return {'seed':seed,'states':states,'repeated_state':x,'transient_length':seen[x],'period':len(states)-seen[x]}

def run_first():
    boxes=INPUTS[0]['input']['boxes']
    weight=[x['id'] for x in boxes if x['weight']<=3]
    color=[x['id'] for x in boxes if x['color']=='white']
    save('systems-handoff-mrc-01-cases.json',{'weight_plan':weight,'color_plan':color,'common_plan':sorted(set(weight)&set(color)),'meaning_sensitive_boxes':sorted(set(weight)^set(color)),'excluded_by_both':sorted({x['id'] for x in boxes}-set(weight)-set(color)),'conditional_routes':[{'meaning':'low_weight','move':weight},{'meaning':'light_color','move':color}],'physical_actions_executed':False})
    hypotheses={'red':lambda r,s:r,'square':lambda r,s:s,'red_and_square':lambda r,s:r and s,'red_xor_square':lambda r,s:r!=s}
    remaining=[h for h,f in hypotheses.items() if f(True,True)]
    partitions=[]
    for r,s in itertools.product([False,True],repeat=2):
        parts={str(v):[h for h in remaining if hypotheses[h](r,s)==v] for v in [False,True]}
        partitions.append({'red':r,'square':s,'partitions':parts,'worst_remaining':max(map(len,parts.values()))})
    chosen=(True,False);observed=hypotheses['square'](*chosen)
    after=[h for h in remaining if hypotheses[h](*chosen)==observed]
    save('systems-handoff-mrc-02-first.json',{'hypotheses':list(hypotheses),'after_existing_red_square':remaining,'query_partitions':partitions,'first_query':{'red':chosen[0],'square':chosen[1],'observed':observed},'remaining_after_first':after,'oracle_is_stipulated':True})
    save('systems-handoff-mrc-03-first.json',orbit('10000'))
    jobs=INPUTS[3]['input']['jobs'];time=0;timeline=[]
    for j in jobs:
        start=max(time,j['release']);time=start+j['duration'];timeline.append({'job':j['id'],'start':start,'finish':time,'deadline':j['deadline'],'meets':time<=j['deadline']})
    save('systems-handoff-mtcg-01-first.json',{'policy':'start A immediately, then run B','timeline':timeline,'all_deadlines_met':all(t['meets'] for t in timeline)})
    controls={'A':6,'B':3};frontier=[0];seen={0:''};layers=[]
    while frontier:
        layers.append([format(x,'03b') for x in frontier]);nxt=[]
        for x in frontier:
            for action,mask in controls.items():
                y=x^mask
                if y not in seen:seen[y]=seen[x]+action;nxt.append(y)
        frontier=nxt
    save('systems-handoff-mtcg-02-first.json',{'layers':layers,'reachable':{format(k,'03b'):v for k,v in sorted(seen.items())},'target':'111','target_reached':7 in seen,'closure_checked':all(x^m in seen for x in seen for m in controls.values())})

if __name__=='__main__':run_first()
