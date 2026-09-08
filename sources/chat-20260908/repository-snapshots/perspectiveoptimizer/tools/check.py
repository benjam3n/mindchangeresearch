from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(condition, message):
    if not condition: errors.append(message)
def read(path): return json.loads((ROOT/path).read_text())
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

links = 0
for path in ROOT.rglob('*.md'):
    text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    for label, destination in re.findall(r'\[([^\]\n]+)\]\(([^)\n]+)\)', text):
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc: continue
        target = (path.parent/unquote(parsed.path)).resolve() if parsed.path else path.resolve()
        require(target == ROOT or ROOT in target.parents, f'Link outside repository: {path.relative_to(ROOT)}: {destination}')
        require(target.exists(), f'Missing link: {path.relative_to(ROOT)}: {destination}')
        links += 1
    for block in re.findall(r'(?:^\|[^\n]*\n?)+', text, re.M):
        rows = [re.split(r'(?<!\\)\|', line.strip().strip('|')) for line in block.strip().splitlines()]
        require(len(rows)>1 and all(re.fullmatch(r'\s*:?-+:?\s*',c) for c in rows[1]), f'Missing table separator: {path.relative_to(ROOT)}')
        require(all(len(r)==len(rows[0]) for r in rows), f'Table columns differ: {path.relative_to(ROOT)}')

clarification=read('sources/clarification-source.json')
require(digest(ROOT/'sources/perspective-clarification-2026-09-07.txt')==clarification['extracted_text_sha256'],'User note digest differs')
patterns=read('perspective/patterns.json')['patterns']
require(len({r['id'] for r in patterns})==len(patterns),'Duplicate perspective pattern identity')
for row in patterns:
    require(all(row.get(k) for k in ['id','name','interpretation','contribution']),'Incomplete perspective description')
manifest=read('sources/theory-manifest.json');bindings=read('sources/subject-bindings.json')
require(bool(re.fullmatch('[a-f0-9]{40}',manifest.get('commit',''))),'Theory commit missing')
require(manifest['repository']=='benjam3n/subjectsystems','Unexpected theory repository')
require(digest(ROOT/'sources/subject-bindings.json')==manifest['projection_sha256'],'Theory projection digest differs')
require(bindings['source_commit']==manifest['commit'],'Theory projection commit differs')
records=bindings['subjects'];ids={r['id'] for r in records}
require(len(ids)==len(records)==manifest['subject_count'],'Theory identity or count differs')
for route in read('cases/learning-routes.json')['routes']:
    require(set(route['subjects'])<=ids,'Unknown subject in route '+route['id'])
for row in records:require(all(row.get(k) for k in ['id','name','target','excludes']),'Incomplete subject binding')
if errors: raise SystemExit('\n'.join(errors))
print(f'PASS: {links} local links; {len(patterns)} perspective patterns; {len(ids)} pinned subject bindings')
