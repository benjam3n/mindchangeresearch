"""Render linked catalog views; validates structure and references, not efficacy."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'catalog/data.json'

def slug(text):
    return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')

def write(path,text):
    path=ROOT/'catalog'/path
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text.rstrip()+'\n')

def render():
    data=json.loads(DATA.read_text())
    sources={s['id']:s for s in data['sources']}
    assert len(sources)==len(data['sources']), 'Duplicate source IDs'
    variants={v['id']:(a,v) for a in data['attempts'] for v in a['variants']}
    assert len(variants)==sum(len(a['variants']) for a in data['attempts']), 'Duplicate variant IDs'
    assert len({t['id'] for t in data['targets']})==len(data['targets'])
    assert len({a['id'] for a in data['attempts']})==len(data['attempts'])
    for a in data['attempts']:
        assert a['variants'], 'An attempt needs a candidate or an explicit separate unresolved record'
        assert set(a['source_ids']) <= sources.keys()
        for v in a['variants']:
            assert v['steps'] and all(isinstance(s,str) and s.strip() for s in v['steps'])
    for t in data['targets']:
        assert set(t['candidate_variants'])<=variants.keys()
        assert set(t['source_ids'])<=sources.keys()

    groups=list(dict.fromkeys(t['group'] for t in data['targets']))
    families=list(dict.fromkeys(a['family'] for a in data['attempts']))
    contents=['# Catalog contents','','[How to use this catalog](README.md) · [Completed finite recipes](worked-recipes.md) · [Source notes](sources.md)','','## What can change','']
    for group in groups:
        path='targets/'+slug(group)+'.md'
        contents.append(f'- [{group}]({path})')
        lines=[f'# {group}','','[All targets and attempts](../contents.md) · [Status and evidence](../README.md)','','These are dimensions to consider, not destinations that every inquiry must fix in advance. Each procedure below is an imported candidate outline; its checks describe the intended outcome rather than an observed result of this revision.','']
        for t in data['targets']:
            if t['group']!=group:
                continue
            links=[]
            for vid in t['candidate_variants']:
                a,v=variants[vid]
                links.append(f"[{vid}: {v['name']}](../attempts/{slug(a['family'])}.md#{vid.lower()})")
            evidence=', '.join(f'[{s}](../sources.md#{s.lower()})' for s in t['source_ids']) or 'No source assigned to this outline.'
            lines += [f'<a id="t{t["id"]}"></a>',f'## T{t["id"]}: {t["name"]}','',
                      '**Candidate improvement:** '+t['improvement'],'','**Procedure outline:** '+t['procedure_outline'],'',
                      '**Different recipes:** '+ '; '.join(links),'','**Outcome check:** '+t['outcome_check'],'',
                      '**Ingredient evidence:** '+evidence,'']
        write(path,'\n'.join(lines))
    contents += ['','## Ways to attempt a change','']
    for family in families:
        path='attempts/'+slug(family)+'.md'
        contents.append(f'- [{family}]({path})')
        lines=[f'# {family}','','[All targets and attempts](../contents.md) · [Completed finite recipes](../worked-recipes.md)','','The adverse route is retained from the original catalog. Beneficial variants are candidate assemblies. Named central judgments still require evidence or an implemented operation; filling every field does not guarantee benefit.','']
        for a in data['attempts']:
            if a['family']!=family:
                continue
            evidence=', '.join(f'[{s}](../sources.md#{s.lower()})' for s in a['source_ids']) or 'No source assigned; design inference.'
            lines += [f'<a id="a{a["id"]}"></a>',f'## A{a["id"]}: {a["name"]}','',
                      '**Failure or backfire route:** '+a['adverse'],'','**Intended beneficial effect:** '+a['intended_effect'],'',
                      '**Ingredient evidence:** '+evidence,'']
            for v in a['variants']:
                lines += [f'<a id="{v["id"].lower()}"></a>',f'### {v["id"]}: {v["name"]}','',
                          '**Use when:** '+v['use_when'],'']
                lines += [f'{i}. {s[0].upper()+s[1:]}' for i,s in enumerate(v['steps'],1)]
                lines += ['','**Redirect condition:** '+v['redirect'],'']
            related=[t for t in data['targets'] if any(v['id'] in t['candidate_variants'] for v in a['variants'])]
            if related:
                lines += ['**Linked target dimensions:** '+', '.join(f'[T{t["id"]}: {t["name"]}](../targets/{slug(t["group"])}.md#t{t["id"]})' for t in related),'']
        write(path,'\n'.join(lines))
    write('contents.md','\n'.join(contents))
    lines=['# Ingredient evidence preserved from the supplied catalog','','These notes and links were imported from the researched catalog. They describe the cited studies\' scope, not a new replication or empirical validation of the assembled recipes. The audit adds logical results and implementations; it does not upgrade these evidence levels.','']
    for s in data['sources']:
        lines += [f'<a id="{s["id"].lower()}"></a>',f'## {s["id"]}: {s["title"]}','',s['scope']+f' [{s["title"]}]({s["url"]})','']
    write('sources.md','\n'.join(lines))
    print(f'Rendered {len(groups)} target views, {len(families)} attempt views, contents, and source notes. Structural checks passed; efficacy was not assessed.')

if __name__=='__main__':
    render()
