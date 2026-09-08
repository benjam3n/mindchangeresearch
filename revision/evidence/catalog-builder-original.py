from pathlib import Path
import json
import re

root = Path('/workspace/scratch/070f7012578e')
base = json.loads((root / 'mindchange_base.json').read_text())
attempts = []
targets = []
for path in sorted(root.glob('recipes-*.json')):
    attempts.extend(json.loads(path.read_text()))
for path in sorted(root.glob('targets-*.json')):
    targets.extend(json.loads(path.read_text()))
attempts.sort(key=lambda x: x[0])
targets.sort(key=lambda x: x[0])
assert [x[0] for x in attempts] == list(range(1, 101))
assert [x[0] for x in targets] == list(range(1, 73))
assert all(len(a) == 4 and len(a[3]) == 3 for a in attempts)
assert all(len(t) == 6 for t in targets)
assert all(len(v) == 4 and all(v) for a in attempts for v in a[3])

variant_names = {
    f'A{a[0]}{chr(97+i)}': v[0]
    for a in attempts for i, v in enumerate(a[3])
}
for t in targets:
    assert all(k in variant_names for k in t[3]), t

source_ids = {f'S{i}' for i in range(1, 24)}
assert all(set(a[2]) <= source_ids for a in attempts)
assert all(set(t[5]) <= source_ids for t in targets)

def evidence(ids):
    if not ids:
        return '**Evidence status:** Design proposal.'
    links = ', '.join(f'[{s}](#{s.lower()})' for s in ids)
    return f'**Evidence status:** Proposed composition; ingredient or boundary evidence: {links}.'

out = [(root / 'mindchange-introduction.md').read_text().rstrip()]
target_index = ['| Domain | Change targets |', '|---|---|']
for offset in range(0, 72, 6):
    chunk = base['targets'][offset:offset+6]
    target_index.append('| ' + chunk[0]['group'] + ' | ' + '; '.join(
        f'[T{t["id"]}: {t["name"]}](#t{t["id"]})' for t in chunk
    ) + ' |')
out.append('\n'.join(target_index))
last_group = None
for t, original in zip(targets, base['targets']):
    n, improvement, procedure, routes, check, ids = t
    assert n == original['id']
    if original['group'] != last_group:
        last_group = original['group']
        out.append(f'### {last_group}')
    out.append(f'<a id="t{n}"></a>\n#### T{n}. {original["name"]}')
    out.append(f'**Improvement sought:** {improvement}')
    out.append(f'**Protocol:** {procedure}')
    out.append('**Choose by condition:** ' + '; '.join(
        f'[{key}: {variant_names[key]}](#{key.lower()})' for key in routes
    ) + '.')
    out.append(f'**Outcome check and redirect:** {check}')
    out.append(evidence(ids))

out.append('<a id="attempts"></a>\n## The 100 attempts and 300 recipe variants')
out.append('The adverse route on each card is preserved verbatim from the prior catalog. These routes include plausible failure mechanisms as well as studied examples; their presence is not a claim that each is frequent or experimentally established. In particular, factual-correction backfire is not a routine result ([S4](#s4)). The outcome condition is separate from recipe completion. Read each variant as **use when → ordered operations → redirect if needed**, under the execution standard above.')
groups = [
    'Attention and presentation', 'Evidence, confidence, and interpretation',
    'Problem representation and possibility', 'Trust, identity, and social interpretation',
    'Motivation, values, and emotion', 'Choices and action',
    'Learning, memory, and skill', 'Readiness and self-regulation',
    'Conversation and joint work', 'Optimization and evaluation'
]
attempt_index = ['| Attempt family | Start |', '|---|---|']
for i, group in enumerate(groups):
    start = i * 10 + 1
    attempt_index.append(f'| {group} | [A{start}–A{start+9}](#a{start}) |')
out.append('\n'.join(attempt_index))
for a, original in zip(attempts, base['attempts']):
    n, outcome, ids, variants = a
    assert n == original['id']
    if (n-1) % 10 == 0:
        out.append(f'### {groups[(n-1)//10]} · A{n}–A{n+9}')
    out.append(f'<a id="a{n}"></a>\n#### A{n}. {original["name"]}')
    out.append(f'**Adverse route:** {original["adverse"]}')
    out.append(f'**Intended effect, evaluated separately:** {outcome}')
    for i, (name, condition, steps, redirect) in enumerate(variants):
        key = f'A{n}{chr(97+i)}'
        out.append(f'<a id="{key.lower()}"></a>\n**{key}. {name}**')
        out.append(f'**Use when:** {condition}')
        pieces = [s.strip() for s in steps.split(';')]
        if len(pieces) != 4:
            raise ValueError((key, len(pieces), steps))
        out.append('\n'.join(f'{j+1}. {step[0].upper()+step[1:]}' for j, step in enumerate(pieces)))
        out.append(f'**Redirect:** {redirect}')
    out.append(evidence(ids))

out.append((root / 'mindchange-closing.md').read_text().rstrip())

old_register = base['original'].split('**Primary research used**', 1)[1].strip()
for block in re.split(r'\n\n+', old_register):
    match = re.match(r'\*\*(S\d+) —', block)
    assert match, block[:80]
    out.append(f'<a id="{match.group(1).lower()}"></a>\n{block}')
for sid, title, url, scope in json.loads((root / 'mindchange-sources-new.json').read_text()):
    scope = scope.replace('https://hamsabastani.github.io/education_llm.pdf.', '[the authors’ manuscript](https://hamsabastani.github.io/education_llm.pdf).')
    out.append(f'<a id="{sid.lower()}"></a>\n**{sid} — [{title}]({url}).** {scope}')

document = '\n\n'.join(out) + '\n'
anchors = re.findall(r'<a id="([^"]+)"', document)
assert len(anchors) == len(set(anchors)), 'Duplicate anchors'
for target in re.findall(r'\]\(#([^\)]+)\)', document):
    assert target in anchors, f'Broken link: {target}'
for original in base['attempts']:
    assert f'**Adverse route:** {original["adverse"]}' in document
assert len(re.findall(r'^#### T\d+\.', document, re.M)) == 72
assert len(re.findall(r'^#### A\d+\.', document, re.M)) == 100
assert len(re.findall(r'^\*\*A\d+[abc]\.', document, re.M)) == 300
assert document.count('**Use when:**') == 300
assert document.count('**Redirect:**') == 300
assert document.count('**Outcome check and redirect:**') == 72
assert len(re.findall(r'^4\. ', document, re.M)) >= 300
assert 'old_benefit' not in document
(root / 'mind-change-science.md').write_text(document)
print(json.dumps({
    'targets': 72, 'attempts': 100, 'variants': 300,
    'ordered_recipe_operations': 1200,
    'adverse_routes_preserved': 100,
    'sources': 23, 'anchors': len(anchors),
    'words': len(document.split()), 'bytes': len(document.encode()),
    'checks': 'Counts, fields, four operations per variant, target mappings, source IDs, internal links, and preserved adverse routes passed.'
}, indent=2))
