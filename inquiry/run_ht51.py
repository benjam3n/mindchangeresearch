from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json, hashlib
import numpy as np
from scipy.optimize import linprog

R=Path(__file__).resolve().parent
plan_bytes=(R/'ht51-preregistered.json').read_bytes()
plan=json.loads(plan_bytes)
A=F(4,5)
def js(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,dict): return {k:js(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [js(x) for x in v]
    if isinstance(v,np.generic): return v.item()
    return v
def segment(p): return max(F(0),p-F(1,5)),min(p,A)
def joint(p,t): return [t,p-t,F(1,5)-p+t,A-t]
def payoff(p,t,c):
    # Direct four-cell state sum; no reduced payoff formula is used here.
    gp,gm,bp,bm=joint(p,t)
    return [6*(gp+gm)-4*(bp+bm),F(0),6*gp-4*bp-c,6*gm-4*bm-c,6*(gp+gm)-4*(bp+bm)-c,-c]
names=['act_now','decline_now','buy_act_positive','buy_act_negative','buy_act_both','buy_decline_both']
def regret(p,t,c,w):
    v=payoff(p,t,c)
    return max(v)-sum(x*y for x,y in zip(v,w))
def formula(p,c):
    lo,hi=segment(p);B=max(F(0),10*p-4)
    l=2*lo+4*p-F(4,5)-c;u=2*hi+4*p-F(4,5)-c
    q=F(0) if u<=B else F(1) if l>=B else (u-B)/(u-l)
    w=[F(0)]*6;w[0 if 10*p-4>=0 else 1]=1-q;w[2]=q
    return {'p':p,'c':c,'B':B,'l':l,'u':u,'q':q,'weights':w,'worst_regret':max(regret(p,lo,c,w),regret(p,hi,c,w))}
def lp(states,allowed=None):
    # Independent full-policy optimization. The input is only joint probabilities and price.
    allowed=list(range(6)) if allowed is None else allowed
    a=[];b=[]
    for p,t,c in states:
        v=payoff(p,t,c);a.append([-float(v[i]) for i in allowed]+[-1.]);b.append(-float(max(v)))
    ans=linprog([0.]*len(allowed)+[1.],A_ub=a,b_ub=b,A_eq=[[1.]*len(allowed)+[0.]],b_eq=[1.],bounds=[(0.,1.)]*len(allowed)+[(0.,None)],method='highs')
    if not ans.success: raise RuntimeError(ans.message)
    return {'value':float(ans.fun),'weights':{names[i]:float(ans.x[j]) for j,i in enumerate(allowed)},'max_constraint_residual':float(max(np.array(a)@ans.x-np.array(b)))}
def known_lp(p,c):
    lo,hi=segment(p);return lp([(p,lo,c),(p,hi,c)])
rows=[]
def add(h,test,support,data): rows.append({'hypothesis':h,'test':test,'supports_exact_claim_in_this_case':bool(support),'data':js(data)})

for p in [F(1,4),F(2,5),F(19,40),F(3,5)]:
    f=formula(p,F(1));w=[F(0)]*6;w[0 if 10*p-4>=0 else 1]=F(1,2);w[2]=F(1,2)
    lo,hi=segment(p);half=max(regret(p,lo,F(1),w),regret(p,hi,F(1),w));opt=known_lp(p,F(1))
    add('H1',f'p={p}',abs(float(half)-opt['value'])<1e-10,{'formula':f,'half_regret':half,'full_policy_lp':opt})

for p in [F(1,5),F(7,20),F(13,20),F(4,5)]:
    lo,hi=segment(p);points=[lo,(lo+hi)/2,hi];inside=[joint(p,t) for t in points]
    valid=all(min(x)>=0 and sum(x)==1 and x[0]+x[3]==A and x[0]+x[1]==p for x in inside)
    outside=[joint(p,lo-F(1,1000)),joint(p,hi+F(1,1000))]
    add('H2',f'p={p}',valid and all(min(x)<0 for x in outside),{'inside':inside,'outside':outside,'segment':[lo,hi]})

for p in [F(1,5),F(1,4),F(3,4),F(4,5)]:
    lo,_=segment(p);v=payoff(p,lo,F(0));maps=v[2:]
    add('H3',f'p={p},lower endpoint',maps[0]==max(maps),{'joint':joint(p,lo),'gross_signal_response_values':dict(zip(names[2:],maps)),'best_maps':[names[i+2] for i,x in enumerate(maps) if x==max(maps)]})

mixes=[[F(1,6)]*6,[F(1,5),F(0),F(4,5),F(0),F(0),F(0)],[F(0),F(2,5),F(0),F(3,5),F(0),F(0)],[F(0),F(0),F(0),F(0),F(1,4),F(3,4)]]
for p in [F(3,10),F(9,20),F(11,20),F(7,10)]:
    lo,hi=segment(p);checks=[]
    for w in mixes:
        ends=max(regret(p,lo,F(1),w),regret(p,hi,F(1),w));grid=[regret(p,lo+(hi-lo)*F(i,100),F(1),w) for i in range(101)]
        checks.append({'weights':w,'endpoint_max':ends,'grid_max':max(grid),'grid_points':len(grid)})
    add('H4',f'p={p}',all(x['grid_max']==x['endpoint_max'] for x in checks),checks)

for p in [F(13,40),F(19,40),F(21,40),F(7,10)]:
    f=formula(p,F(1));opt=known_lp(p,F(1))
    add('H5',f'p={p}',abs(float(f['worst_regret'])-opt['value'])<1e-10,{'formula':f,'full_policy_lp':opt})

for p,c in [(F(1,5),F(0)),(F(2,5),F(1,10)),(F(3,5),F(1)),(F(4,5),F(2))]:
    lo,hi=segment(p);states=[(p,lo,c),(p,hi,c)];allpol=lp(states);i=0 if 10*p-4>=0 else 1;reduced=lp(states,[i,2])
    witnesses=[]
    for t in [lo,(lo+hi)/2,hi]:
        v=payoff(p,t,c);witnesses.append({'t':t,'payoffs':dict(zip(names,v)),'immediate_best':max(v[:2]),'removed_map_max':max(v[3:])})
    add('H6',f'p={p},c={c}',abs(allpol['value']-reduced['value'])<1e-10,{'full':allpol,'reduced':reduced,'witnesses':witnesses})

corners=[(F(2,5),F(1,5),F(1)),(F(2,5),F(2,5),F(1)),(F(3,5),F(2,5),F(1)),(F(3,5),F(3,5),F(1))]
w=[F(1,2),F(0),F(1,2),F(0),F(0),F(0)]
for (p,t,c),expected in zip(corners,[F(1,10),F(3,10),F(3,10),F(1,10)]):
    actual=regret(p,t,c,w);add('H7',f'p={p},t={t}',actual==expected,{'joint':joint(p,t),'values':dict(zip(names,payoff(p,t,c))),'regret':actual,'expected':expected})
interval_lp=lp(corners)

# A separately written posterior-branch evaluator cross-checks direct cell sums.
conditional=[]
for p,t,c in [(F(1,5),F(0),F(1)),(F(1,4),F(1,20),F(1)),(F(3,4),F(11,20),F(1)),(F(4,5),F(3,5),F(1)),(F(19,40),F(3,10),F(1)),(F(21,40),F(1,2),F(1))]:
    gp,gm,bp,bm=joint(p,t);plus=gp+bp;minus=gm+bm
    val_plus=F(0) if plus==0 else plus*(10*(gp/plus)-4)
    val_minus=F(0) if minus==0 else minus*(10*(gm/minus)-4)
    derived=[10*p-4,F(0),val_plus-c,val_minus-c,val_plus+val_minus-c,-c]
    conditional.append({'p':p,'t':t,'zero_probability_branch':plus==0 or minus==0,'conditional_values':derived,'joint_values':payoff(p,t,c),'matches':derived==payoff(p,t,c)})

out={'preregistered_sha256':hashlib.sha256(plan_bytes).hexdigest(),'test_rows':rows,'tests_per_hypothesis':{h:sum(x['hypothesis']==h for x in rows) for h in ['H1','H2','H3','H4','H5','H6','H7']},'interval_full_policy_lp':interval_lp,'conditional_probability_cross_checks':conditional,'conditional_checks_all_match':all(x['matches'] for x in conditional),'total_primary_tests':len(rows),'numeric_lp_tolerance':1e-10,'no_sampling_inference':True}
(R/'ht51-results.json').write_text(json.dumps(js(out),indent=2)+'\n')
print(json.dumps({'tests':len(rows),'per_hypothesis':out['tests_per_hypothesis'],'falsifications':[(x['hypothesis'],x['test']) for x in rows if not x['supports_exact_claim_in_this_case']],'interval_lp':interval_lp,'conditional_checks_all_match':out['conditional_checks_all_match']},indent=2))
