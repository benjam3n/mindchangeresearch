"""Reproduce the declared finite examples, not psychological efficacy claims."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import deque
import json

out = {}
ps = [F(x, 8) for x in range(9)] + [F(2,3), F(4,5)]
out['time'] = []
for p in sorted(set(ps)):
    values = {'commit_now':F(5), 'wait':8*p-1, 'reserve_and_wait':3*p+3}
    best = max(values.values())
    out['time'].append({'p':str(p),'values':{k:str(v) for k,v in values.items()},'winners':[k for k,v in values.items() if v==best]})

worlds = list(product([0,1], repeat=3))
def partitions(observation):
    d={}
    for w in worlds:d.setdefault(str(observation(w)),[]).append(''.join(map(str,w)))
    return d
out['location']={'worlds':[''.join(map(str,w)) for w in worlds],
 'entrance':partitions(lambda w:()),'west':partitions(lambda w:(w[0],w[1])),
 'east':partitions(lambda w:(w[1],w[2])),'both':partitions(lambda w:w)}

nodes=list('ABCDEFGH')
full={(nodes[i],nodes[j]) for i in range(8) for j in range(i+1,8)}
chain={(nodes[i],nodes[i+1]) for i in range(7)}
def distances(edges,start):
    d={start:0};q=deque([start])
    while q:
        u=q.popleft()
        for a,b in sorted(edges):
            if a==u and b not in d:d[b]=d[u]+1;q.append(b)
    return d
comparisons=[]
for a in nodes:
    x,y=distances(full,a),distances(chain,a)
    for b in nodes:
        if a!=b:comparisons.append({'from':a,'to':b,'before':x.get(b),'after':y.get(b)})
out['representation']={'full_edges':sorted(full),'chain_edges':sorted(chain),
 'pairs':comparisons,'reachability_preserved':all((r['before'] is None)==(r['after'] is None) for r in comparisons),
 'distance_changes':sum(r['before']!=r['after'] for r in comparisons)}

options={'Explore':(8,1),'Apply':(1,8),'Blend':(5,5),'Busywork':(3,3)}
out['motivation']={'options':options,'weights':[]}
for w in [F(0),F(1,4),F(3,7),F(1,2),F(4,7),F(3,4),F(1)]:
    values={k:w*a+(1-w)*b for k,(a,b) in options.items()};best=max(values.values())
    out['motivation']['weights'].append({'interest_weight':str(w),'values':{k:str(v) for k,v in values.items()},'winners':[k for k,v in values.items() if v==best]})

truth=[('color',0),('color',1),('color',0),('color',1),('shape',1),('shape',0),('shape',1),('shape',0)]
out['trust']={'rows':[]}
for i,(kind,v) in enumerate(truth):
    a=v if kind=='color' else 1-v;b=v if kind=='shape' else 1-v
    out['trust']['rows'].append({'id':i+1,'kind':kind,'truth':v,'A':a,'B':b,'three_copies_of_A':[a,a,a],'domain_route':a if kind=='color' else b})
out['trust']['correct']={k:sum(r[k]==r['truth'] for r in out['trust']['rows']) for k in ['A','B','domain_route']}

small=list(product([0,1],repeat=2)) # (truth, source inversion)
k1=[(x,r) for x,r in small if x^r==0]
k2=[(x,r) for x,r in small if r==0]
def query_classes(knowledge,query):
    result={}
    for x,r in knowledge:result.setdefault(str(query(x,r)),[]).append({'x':x,'r':r})
    return result
out['uncertainty']={name:{'worlds':k,'probability_x1':str(F(sum(x for x,r in k),len(k))),
 'query_A':query_classes(k,lambda x,r:x^r),'query_r':query_classes(k,lambda x,r:r)} for name,k in [('observed_A0_unknown_r',k1),('known_r0_unobserved_A',k2)]}

def round_half_up(x):return (x+F(1,2)).numerator//(x+F(1,2)).denominator
amounts=[[F(49,100)]*7+[F(51,100)], [F(51,100)]*8,[F(49,100)]*8,[F(1,3)]*3,
         [F(3,2),F(3,2)],[F(1,4)]*4,[F(1),F(2),F(3)],[F(49,100),F(51,100)]]
out['order']=[{'input':[str(x) for x in xs], 'sum_exact':str(sum(xs)),
 'round_each_then_sum':sum(round_half_up(x) for x in xs), 'sum_then_round':round_half_up(sum(xs))} for xs in amounts]

def reach(flips):
    d={'000':[]};q=deque(['000'])
    while q:
        s=q.popleft()
        for i in flips:
            t=s[:i]+str(1-int(s[i]))+s[i+1:]
            if t not in d:d[t]=d[s]+[i];q.append(t)
    return d
out['capability']={'before':reach([0,1]),'after':reach([0,1,2]),'relabel_only':reach([0,1])}
Path(__file__).with_name('finite-cases.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'time_cases':len(out['time']),'location_worlds':len(worlds),
 'representation_pairs':len(comparisons),'distance_changes':out['representation']['distance_changes'],
 'trust_correct':out['trust']['correct'],'rounding_differences':sum(x['round_each_then_sum']!=x['sum_then_round'] for x in out['order']),
 'reachable_before':len(out['capability']['before']),'reachable_after':len(out['capability']['after'])}))
