#!/usr/bin/env python3
"""Execute the supplied constructed examples and save their scoped results."""
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from perspectiveoptimizer.space import enumerate_space,expand_space,route_studies,transition_reachability

def read(name):return json.loads((ROOT/'cases'/name).read_text())
def save(name,data):
 p=ROOT/'results'/name;p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
base=enumerate_space(read('learning-space.json'))
expanded=expand_space(read('learning-space.json'),read('application-condition-extension.json'))
routes=route_studies(read('learning-routes.json'),read('learning-observations.json'))
reach=transition_reachability(read('perspective-transitions.json'))
for name,result in [('learning-space.json',base),('learning-space-expanded.json',expanded),('learning-routes.json',routes),('perspective-transitions.json',reach)]:save(name,result)
summary={'assignments_before':base['assignment_count'],'open_before':base['open_count'],'assignments_after':expanded['after_count'],'open_after':expanded['enumeration']['open_count'],
 'route_statuses':{r['id']:r['status'] for r in routes['routes']},'reachable':reach['reachable'],'conditional_only':reach['conditional_only'],
 'standing':'Executed constructed examples. Counts and routes are relative to supplied definitions and observations; no empirical capability improvement is established.'}
save('summary.json',summary)
print(json.dumps(summary,indent=2))
