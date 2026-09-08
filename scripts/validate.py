"""Check imported data integrity, source links, attribution, and retained accounting."""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'sources/conversations/2026-09-08-perspectives'
HISTORY = ROOT / 'sources/repository/07e6af64c65f'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def require(condition, detail):
    if not condition:
        raise ValueError(detail)

def blob_sha(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()

def links(path):
    return re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)', path.read_text(encoding='utf-8'))

def resolve_link(base, link):
    parts = urlsplit(link)
    if parts.scheme or parts.netloc:
        return None, None
    path = (base.parent / unquote(parts.path)).resolve() if parts.path else base
    require(path.is_relative_to(ROOT), f'Link leaves repository: {base.name}: {link}')
    return path, unquote(parts.fragment)

def validate():
    manifest = read(SOURCE / 'manifest.json')
    for item in manifest['files']:
        raw = (SOURCE / item['path']).read_bytes()
        require(len(raw) == item['bytes'], 'Source size changed: ' + item['path'])
        require(hashlib.sha256(raw).hexdigest() == item['sha256'], 'Source hash changed: ' + item['path'])
    for link in manifest['current_views']:
        path, _ = resolve_link(SOURCE / 'manifest.json', link)
        require(path.exists(), 'Missing current catalog: ' + link)

    tree = read(HISTORY / 'tree.json')
    tree_files = {e['path']: e for e in tree['files'] if e['type'] == 'blob'}
    preserved = []
    concurrent_history = ROOT / 'sources/repository/2a7c6d920bf9'
    for history in [HISTORY, concurrent_history]:
        inventory = {e['path']: e for e in read(history / 'tree.json')['files'] if e['type'] == 'blob'}
        for path in history.rglob('*'):
            if not path.is_file():
                continue
            rel = path.relative_to(history).as_posix()
            if rel in inventory:
                require(blob_sha(path.read_bytes()) == inventory[rel]['sha'], 'Historical record changed: ' + rel)
                preserved.append((history.name, rel))

    originals = read(SOURCE / 'Perspectives_3000.json')['perspectives']
    perspectives = read(ROOT / 'perspectives/catalog.json')['perspectives']
    operations = read(ROOT / 'operations/catalog.json')['operations']
    original_operations = read(SOURCE / 'Perspective_Modifications_3000.json')['operations']
    ranked_source = read(SOURCE / 'Perspectives_3000_Ranked.json')['perspectives']
    ranked = read(ROOT / 'perspectives/ranked.json')['perspectives']
    require(perspectives == [{k: v for k, v in p.items() if k != 'name'} for p in originals], 'Perspective content or identity changed')
    require(operations == original_operations, 'Modification content or identity changed')
    removed = {'name', 'change_enabled', 'ranking_reason'}
    require(ranked == [{k: v for k, v in p.items() if k not in removed} for p in ranked_source], 'Ranks, ties, source order, or statements changed')
    pmap = {p['id']: p for p in perspectives}
    omap = {p['id']: p for p in operations}
    require(set(pmap) == {f'P{i:04d}' for i in range(1, 3001)}, 'Perspective ID coverage differs')
    require(set(omap) == {f'PM{i:04d}' for i in range(1, 3001)}, 'Operation ID coverage differs')
    require(len(perspectives) == len(operations) == len(ranked) == 3000, 'Catalog size differs')
    require({p['id'] for p in ranked} == set(pmap), 'Ranking ID coverage differs')

    recipes = read(ROOT / 'recipes.json')
    recipe_ids = [r['id'] for r in recipes['recipes']]
    require(len(recipe_ids) == len(set(recipe_ids)), 'Duplicate procedure ID')
    for recipe in recipes['recipes']:
        require(recipe['procedure'] and recipe['case'] and recipe['support'], 'Missing procedure, case, or evidence scope')
        for pid in recipe['perspectives']:
            require(pid in pmap, 'Unknown perspective reference: ' + pid)
        for oid in recipe['operations']:
            require(oid in omap, 'Unknown operation reference: ' + oid)
        for path in recipe['records']:
            require((ROOT / path).is_file(), 'Missing source record: ' + path)
            require(path in recipes['record_titles'], 'Missing descriptive source title: ' + path)

    old_index = HISTORY / 'Mind_Change_Research_Index.md'
    original_links = [link for link in links(old_index) if not urlsplit(link).scheme]
    formerly_absent = []
    for link in original_links:
        path, _ = resolve_link(ROOT / old_index.name, link)
        require(path.exists(), 'Original index target still unavailable: ' + link)
        if path.relative_to(ROOT).as_posix() not in tree_files:
            formerly_absent.append(link)

    active = [ROOT / p for p in ['README.md', 'Mind_Change_Research_Index.md', 'research.md',
        'working-instruction.md', 'repository-sync.md', 'checkpoint-parts/README.md',
        'perspectives/catalog.md', 'perspectives/ranked.md', 'operations/catalog.md',
        'post-allocation/cycle-03/capability/01-spg-near-guarantee.md']]
    active.extend(sorted((ROOT / 'changes').glob('*.md')))
    checked_links = 0
    for file in active:
        body = file.read_text(encoding='utf-8')
        require(not re.search(r'^(?:#+\s*)?(?:Intended mind change|Actual mind change|Organization assessment|Content assessment|Next attempts):', body, re.M), 'Repeated reflection scaffold: ' + str(file.relative_to(ROOT)))
        for link in links(file):
            path, anchor = resolve_link(file, link)
            if path is None:
                continue
            require(path.exists(), 'Missing current link: ' + str(file.relative_to(ROOT)) + ': ' + link)
            if anchor and path.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+?)\s*$', path.read_text(), re.M)
                anchors = {re.sub(r'[^\w -]', '', h.lower()).replace(' ', '-') for h in headings}
                require(anchor in anchors, 'Missing heading: ' + link)
            checked_links += 1

    baseline = read(HISTORY / 'Research_Ledger.json')
    ledger = read(ROOT / 'Research_Ledger.json')
    concurrent = read(concurrent_history / 'Research_Ledger.json')
    require(ledger['chat_integrations'] == concurrent['chat_integrations'], 'Concurrent integrations were overwritten')
    for key in ['required_applications', 'status_counts', 'status_basis', 'applications', 'gosm']:
        require(ledger[key] == baseline[key], 'Frozen allocation changed: ' + key)
    require(len(ledger['post_allocation_cycles']) == len(baseline['post_allocation_cycles']), 'Integration unexpectedly added a cycle')
    correction = None
    for old, current in zip(baseline['post_allocation_cycles'], ledger['post_allocation_cycles']):
        require(old['attempt_counts'] == current['attempt_counts'], 'Integration altered attempt or finding credit')
        require([r['id'] for r in old['records']] == [r['id'] for r in current['records']], 'Integration altered research record identities')
        for prior, record in zip(old['records'], current['records']):
            if record['id'] == 'PAC03-SPG-01':
                require(record['historical_verdict'] == prior['verdict'], 'Original verdict was not retained')
                correction = record['assessment_correction']
                require(correction['recipe_implementation_status'] == 'UNRESOLVED', 'General implementation incorrectly asserted')
                require(correction['finding_credit_added'] == 0, 'Correction awarded finding credit')
            else:
                require(prior == record, 'Unrelated research record changed: ' + record['id'])
    local = read(ROOT / 'post-allocation/cycle-03/cycle-ledger.json')
    local_record = next(r for r in local['records'] if r['id'] == 'PAC03-SPG-01')
    require(local_record['assessment_correction'] == correction, 'Local and root corrections differ')
    integration = next(r for r in ledger['repository_integrations'] if r['id'] == 'perspective-catalog-2026-09-08')
    require(integration['initial_application_credit_added'] == integration['distinct_finding_credit_added'] == 0, 'Import incorrectly credited as a finding')

    return {'source_files_verified': len(manifest['files']), 'historical_repository_files_verified': len(preserved),
        'perspectives': len(perspectives), 'operations': len(operations), 'ranked_entries': len(ranked),
        'individually_ranked_leaders': sum(r['tie_size'] == 1 for r in ranked),
        'procedures': len(recipe_ids), 'subjects': len({r['subject'] for r in recipes['recipes']}),
        'original_index_links': len(original_links), 'formerly_absent_targets_now_exposed': len(formerly_absent),
        'current_links_checked': checked_links, 'original_allocation_and_finding_credit': 'unchanged',
        'scope': 'Data identity, attribution, references, and accounting. No human efficacy or optimality inference.'}

if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
