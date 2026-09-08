"""Rebuild subject views from preserved chat material and current accounting.

This generator changes representation only. It never assigns empirical support,
recipe completeness, KEEP status, or discovery credit to a catalog entry.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources/chat-20260908'
OUT = ROOT / 'mind-change'


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + '\n')


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def rows(paths):
    result = {}
    for path in paths:
        for line in path.read_text().splitlines():
            fields = line.split('|')
            if len(fields) != 3 or not all(fields):
                raise ValueError(f'Invalid contributor row: {path}')
            key = int(fields[0])
            if key in result:
                raise ValueError(f'Duplicate target: {key}')
            result[key] = fields[1:]
    return result


def build():
    base = json.loads((SOURCE / 'mind_change_base.json').read_text())
    sources = json.loads((SOURCE / 'contributors_sources.json').read_text())
    source_ids = {s['id'] for s in sources}
    human = rows(sorted(SOURCE.glob('contributors_[0-9]*.txt')))
    ai = rows([SOURCE / 'contributors_ai.txt'])
    assert set(human) == set(range(1, 591))
    assert set(ai) == set(range(1, 27))

    def links(value, prefix='../'):
        def replace(match):
            ids = match.group(1).split(', ')
            assert set(ids) <= source_ids
            return ', '.join(f'[{i}]({prefix}evidence.md#{i.lower()})' for i in ids)
        return re.sub(r'\[(S\d{2}(?:, S\d{2})*)\]', replace, value)

    records = []
    families = []
    number = 0
    for family_number, (name, definitions) in enumerate(base['groups'], 1):
        family = {'id': f'family-{family_number:02d}', 'name': name,
                  'path': f'targets/{family_number:02d}-{slug(name)}.md', 'targets': []}
        page = [f'# {name}',
                'Candidate contributors describe possible functional relationships. '
                'Each source marker supports only its attached statement at the '
                '[specified scope](../evidence.md). '
                '[Construction](../contribution-construction.md) supplies operations for a particular use.']
        for definition in definitions:
            number += 1
            label, meaning = definition.split(': ', 1)
            contributors, conditions = human[number]
            entry = {'id': str(number), 'family': family['id'], 'label': label,
                     'definition': definition, 'bearer_scope': 'human by default',
                     'candidate_contributors': contributors, 'conditions': conditions,
                     'source_ids': sorted(set(re.findall(r'S\d{2}', contributors + conditions))),
                     'standing': 'candidate functional synthesis; source-marked claims scoped separately',
                     'recipe_status': 'not a complete intervention recipe',
                     'path': family['path'] + f'#target-{number}',
                     'provenance': f'sources/chat-20260908/Mind_Change_Inventory.md; target {number}'}
            records.append(entry)
            family['targets'].append(str(number))
            page += [f'<a id="target-{number}"></a>\n## {number}. {label}', meaning.rstrip('.') + '.',
                     '**Candidate contributors:** ' + links(contributors),
                     '**Conditions and distinctions:** ' + links(conditions)]
        page += ['[Mind-change targets](../targets.md)']
        write(OUT / family['path'], '\n\n'.join(page))
        families.append(family)

    page = ['# Functional AI self-change',
            'These targets concern working interpretations, records, conduct, and editable supporting systems. '
            'A prompt or record change does not establish a change to trained model parameters.']
    for number, definition in enumerate(base['extras']['ai'], 1):
        contributors, conditions = ai[number]
        identity = f'AI-{number}'
        records.append({'id': identity, 'family': 'functional-ai', 'label': definition.rstrip('.'),
                        'definition': definition, 'bearer_scope': 'functional AI working state or supporting system',
                        'candidate_contributors': contributors, 'conditions': conditions,
                        'source_ids': sorted(set(re.findall(r'S\d{2}', contributors + conditions))),
                        'standing': 'candidate functional synthesis',
                        'recipe_status': 'not a complete intervention recipe',
                        'path': f'ai.md#ai-{number}',
                        'provenance': f'sources/chat-20260908/Mind_Change_Inventory.md; {identity}'})
        page += [f'<a id="ai-{number}"></a>\n## {identity}. {definition.rstrip(".")}',
                 '**Candidate contributors:** ' + links(contributors, ''),
                 '**Conditions and distinctions:** ' + links(conditions, '')]
    write(OUT / 'ai.md', '\n\n'.join(page))
    write(OUT / 'targets.json', json.dumps({'schema_version': 1,
          'coverage': '590 inherited targets in 62 overlapping families plus 26 functional AI targets; open to extension',
          'families': families, 'targets': records}, ensure_ascii=False, indent=1))
    table = ['# Mind-change targets',
             'Each target retains its original identity, definition, candidate contributors, and conditions. '
             'The families overlap. Coverage of this inherited inventory does not establish a universal ontology or all causes.',
             '| Subject family | Targets |\n|---|---|']
    for family in families:
        table.append(f'| [{family["name"]}]({family["path"]}) | {family["targets"][0]}–{family["targets"][-1]} |')
    table += ['\n[Functional AI self-change](ai.md) · [Required subject systems](subject-systems.md) · '
              '[Contributor construction](contribution-construction.md) · [Machine-readable targets](targets.json)']
    write(OUT / 'targets.md', '\n'.join(table))

    relations = ['# Forms of mind change', '[Perspective construction](perspective-construction.md) supplies operative dimensions and sixty candidate perspective patterns from the preceding conversation.']
    for key, title in [('operations', 'Operations'), ('dimensions', 'Dimensions'),
                       ('routes', 'Ways a change can occur'), ('failureModes', 'Divergent effects')]:
        relations += [f'## {title}', '\n'.join(f'{i}. {v}' for i, v in enumerate(base['extras'][key], 1))]
    relations += ['These dimensions, operations, and routes can combine. They are candidate distinctions, '
                  'not independent validated factors or a compulsory sequence.']
    write(OUT / 'relations.md', '\n\n'.join(relations))
    evidence = ['# Evidence for contributor distinctions',
                'The notes preserve the earlier source checks. They are not a new systematic review. '
                'Unmarked contributor sets remain original proposals; source support never spreads automatically '
                'to a whole target, family, or recipe.']
    for source in sources:
        evidence += [f'<a id="{source["id"].lower()}"></a>\n## {source["id"]}. {source["title"]}',
                     f'[{source["evidence"]}]({source["url"]}). {source["note"]}']
    write(OUT / 'evidence.md', '\n\n'.join(evidence))

    ledger = json.loads((ROOT / 'Research_Ledger.json').read_text())
    counts = ledger['status_counts']
    cycles = ledger.get('post_allocation_cycles', [])
    status = ['# Research execution',
              'Execution accounting preserves required exposures and unresolved work. '
              'It does not rank the value of the available contributions.',
              f'Ledger timestamp: `{ledger["updated_utc"]}`. [Exact ledger](../Research_Ledger.json).',
              '| Initial application status | Count |\n|---|---:|']
    status += [f'| {state} | {counts.get(state, 0)} |' for state in ['complete', 'partial', 'blocked', 'pending']]
    status += ['\nThe frozen obligation remains 300 applications across 150 original skills and ten GOSM runs. '
               'Completion means the record’s stated scope, not certification of every original semantic requirement.',
               '## Continuations', '| Cycle | Attempts | Complete in scope | Partial | Distinct findings |\n|---|---:|---:|---:|---:|']
    for cycle in cycles:
        c = cycle['attempt_counts']
        path = cycle.get('ledger_file', cycle['cycle'] + '/cycle-ledger.json')
        status.append(f'| [{cycle["cycle"]}](../{path}) | {c.get("substantive_records", 0)} | '
                      f'{c.get("complete_within_scope", 0)} | {c.get("partial", 0)} | '
                      f'{c.get("distinct_new_keep_findings", 0)} |')
    status += ['\n[Execution instruction](../working-instruction.md) · [Source integrity](../Source_Integrity.json) · '
               '[Complete checkpoint](../checkpoint-parts/README.md)',
               'Chat integration is separate from the frozen skill quota and the distinct-finding counter. '
               '[Its record](chat-integration.md) identifies accepted requirements, candidate content, '
               'historical probes, and actual repository changes separately.']
    write(ROOT / 'research/status.md', '\n'.join(status))


if __name__ == '__main__':
    build()
