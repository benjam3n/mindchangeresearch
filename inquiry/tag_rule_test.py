from pathlib import Path
import json,copy
R=Path(__file__).resolve().parent
qs=[x['data']['question'] for x in json.loads((R/'questionroute-original-exports.json').read_text())]
def rule(qs,existing=()):
    out=list(existing)
    for a in qs:
        if 'certainty' not in a['tags']: continue
        for b in qs:
            if 'uncertainty' not in b['tags'] or a['id']==b['id']:continue
            e=(a['id'],b['id'],'contradiction','certainty contradicts uncertainty','medium')
            if not any(x[0]==e[0] and x[1]==e[1] and x[2]==e[2] for x in out):out.append(e)
    return out
base=rule(qs);results=[]
def trial(name,mut,existing=()):
    test=copy.deepcopy(qs);mut(test);r=rule(test,existing)
    results.append({'name':name,'edges':len(r),'sure_hope':any(x[0]=='sure' and x[1]=='hope' for x in r),'self_edges':sum(x[0]==x[1] for x in r),'added':[x for x in r if x not in base],'removed':[x for x in base if x not in r]})
trial('baseline',lambda x:None)
trial('remove uncertainty tag from hope',lambda q:next(x for x in q if x['id']=='hope')['tags'].remove('uncertainty'))
trial('change hope definition only',lambda q:next(x for x in q if x['id']=='hope').update(definition='A stipulated unrelated topic with unchanged tags.'))
trial('remove certainty tag from sure',lambda q:next(x for x in q if x['id']=='sure')['tags'].remove('certainty'))
trial('add uncertainty tag to sure',lambda q:next(x for x in q if x['id']=='sure')['tags'].append('uncertainty'))
trial('supply existing sure-hope same-type route',lambda q:None,[('sure','hope','contradiction','existing different reason','high')])
trial('remove both causal tags',lambda q:[x.update(tags=[t for t in x['tags'] if t not in ['certainty','uncertainty']]) for x in q])
(R/'tag-rule-interventions.json').write_text(json.dumps({'scope':'isolated Python transcription of inspected tag-cross-product and duplicate/self filtering, not full historical TypeScript script execution','trials':results},indent=2)+'\n')
print([(x['name'],x['edges'],x['sure_hope'],x['self_edges']) for x in results])
