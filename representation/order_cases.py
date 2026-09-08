from collections import defaultdict,deque
from pathlib import Path
import json
cases={
 '23':{'nodes':['freeze claim','capture outcomes','define criterion','classify applicability','compare outcomes','write scoped result','make reusable excerpt'],'hard':[['freeze claim','capture outcomes'],['freeze claim','define criterion'],['freeze claim','classify applicability'],['capture outcomes','compare outcomes'],['define criterion','compare outcomes'],['classify applicability','compare outcomes'],['compare outcomes','write scoped result'],['write scoped result','make reusable excerpt']],'soft':[['define criterion','capture outcomes']]},
 '24':{'nodes':['read source A','read source B','draft one shared card','check logic','check serial reading','revise shared card','finalize card'],'hard':[['read source A','draft one shared card'],['read source B','draft one shared card'],['draft one shared card','check logic'],['draft one shared card','check serial reading'],['check logic','revise shared card'],['check serial reading','revise shared card'],['revise shared card','finalize card']],'soft':[]}}
for key,c in cases.items():
 adj=defaultdict(list); indeg={n:0 for n in c['nodes']};depth={n:0 for n in c['nodes']}; paths={n:[n] for n in c['nodes']}
 for a,b in c['hard']:adj[a].append(b);indeg[b]+=1
 q=deque(n for n in c['nodes'] if indeg[n]==0);out=[]
 while q:
  a=q.popleft();out.append(a)
  for b in adj[a]:
   if depth[a]+1>depth[b]:depth[b]=depth[a]+1;paths[b]=paths[a]+[b]
   indeg[b]-=1
   if indeg[b]==0:q.append(b)
 groups=defaultdict(list)
 for n,d in depth.items():groups[d].append(n)
 c.update(order=out,cycle=len(out)!=len(c['nodes']),depth=depth,groups=dict(groups),longest_chain=max(paths.values(),key=len),edge_checks=[dict(before=a,after=b,satisfied=out.index(a)<out.index(b)) for a,b in c['hard']])
Path('mind-change-research/representation/order-case-results.json').write_text(json.dumps(cases,indent=2))
print(json.dumps(cases,indent=2))
