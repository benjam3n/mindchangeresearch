import json
from pathlib import Path
REPO=Path(__file__).resolve().parent.parent
SRC=REPO/'sources/conversations/2026-09-08-perspectives'
perspectives=json.loads((SRC/'Perspectives_3000.json').read_text())
operations=json.loads((SRC/'Perspective_Modifications_3000.json').read_text())
ranking=json.loads((SRC/'Perspectives_3000_Ranked.json').read_text())
(REPO/'perspectives').mkdir(exist_ok=True)
(REPO/'operations').mkdir(exist_ok=True)

ps={
    'scope':'3,000 constructed statements of perspectives. Subjects overlap; the catalog is open and is not an enumeration of every perspective actually held.',
    'source':'../sources/conversations/2026-09-08-perspectives/Perspectives_3000.json',
    'entry_count':3000,
    'subjects':perspectives['subjects'],
    'perspectives':[{k:v for k,v in p.items() if k!='name'} for p in perspectives['perspectives']],
}
(REPO/'perspectives/catalog.json').write_text(json.dumps(ps,ensure_ascii=False,indent=2)+'\n')
lines=['# Perspectives','','3,000 statements, arranged by subject. Competing positions coexist. Inclusion establishes neither truth nor completeness. Original names and construction files remain in the [conversation archive](../sources/conversations/2026-09-08-perspectives/manifest.json).','']
for subject in ps['subjects']:
    lines += ['## '+subject['name'],'']
    for p in ps['perspectives']:
        if p['subject_id']==subject['id']:
            lines.append(f"- {p['statement']} (`{p['id']}`)")
    lines.append('')
(REPO/'perspectives/catalog.md').write_text('\n'.join(lines))

op={**operations,'source':'../sources/conversations/2026-09-08-perspectives/Perspective_Modifications_3000.json'}
(REPO/'operations/catalog.json').write_text(json.dumps(op,ensure_ascii=False,indent=2)+'\n')
lines=['# Perspective modification','','3,000 operations, arranged by the distinction or relation they change. An operation becomes part of a usable recipe only when its inputs, conditions, sequence, and consequences are supplied.','']
for category in op['categories']:
    lines += ['## '+category['name'],'']
    for item in op['operations']:
        if item['category_id']==category['id']:
            lines.append(f"- {item['operation']} (`{item['id']}`)")
    lines.append('')
(REPO/'operations/catalog.md').write_text('\n'.join(lines))

rk={
    'scope':'Provisional editorial priority of statements considered independently. No recipe efficacy, recipient-specific benefit, or causal effect was measured.',
    'ranking_criterion':ranking['ranking_criterion'],
    'recipient_assumption':ranking['recipient_assumption'],
    'rank_convention':ranking['rank_convention'],
    'source':'../sources/conversations/2026-09-08-perspectives/Perspectives_3000_Ranked.json',
    'entry_count':3000,
    'profiles':ranking['profiles'],
    'perspectives':[{k:v for k,v in p.items() if k not in ['name','change_enabled','ranking_reason']} for p in ranking['perspectives']],
}
(REPO/'perspectives/ranked.json').write_text(json.dumps(rk,ensure_ascii=False,indent=2)+'\n')
lines=['# Perspective rankings','','The first 60 statements were individually ordered by estimated reusable benefit relative to effort. The rest share benefit/effort bands. These judgments concern statements as written; they do not establish which recipe will benefit a particular recipient. The [original assessment](../sources/conversations/2026-09-08-perspectives/Perspectives_3000_Ranked.md) preserves every rationale and assumption.','','| Rank | Perspective |','|---:|---|']
for p in rk['perspectives'][:60]:
    lines.append(f"| {p['rank']} | {p['statement']} (`{p['id']}`) |")
for group in ranking['tie_groups']:
    example=next(p for p in rk['perspectives'] if p['rank']==group['rank'])
    lines += ['',f"## {example['expected_benefit']} benefit, {example['expected_effort'].lower()} effort",'',f"{group['entry_count']:,} statements tied at rank {group['rank']:,}. Source order within the tie carries no additional priority.",'']
    lines += [f"- {p['statement']} ({p['subject']}; `{p['id']}`)" for p in rk['perspectives'] if p['rank']==group['rank']]
(REPO/'perspectives/ranked.md').write_text('\n'.join(lines)+'\n')
