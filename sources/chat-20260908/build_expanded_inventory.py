import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
base = json.loads((ROOT / 'mind_change_base.json').read_text())
groups = base['groups']
extras = base['extras']
sources = json.loads((ROOT / 'contributors_sources.json').read_text())
source_by_id = {s['id']: s for s in sources}
original = (ROOT / 'Mind_Change_Inventory.original.md').read_text()
front = (ROOT / 'inventory_expansion_front.md').read_text()

def read_rows(paths):
    result = {}
    for path in paths:
        for line in path.read_text().splitlines():
            fields = line.split('|')
            assert len(fields) == 3 and all(fields), (path.name, line)
            identity = int(fields[0])
            assert identity not in result, identity
            result[identity] = fields[1:]
    return result

rows = read_rows(sorted(ROOT.glob('contributors_[0-9]*.txt')))
ai_rows = read_rows([ROOT / 'contributors_ai.txt'])
assert set(rows) == set(range(1, 591))
assert set(ai_rows) == set(range(1, 27))
assert len(groups) == 62 and sum(len(g[1]) for g in groups) == 590

def link_sources(value):
    def replace(match):
        identities = match.group(1).split(', ')
        for identity in identities:
            assert identity in source_by_id, identity
        return ', '.join(f"[{identity}]({source_by_id[identity]['url']})" for identity in identities)
    return re.sub(r'\[(S\d{2}(?:, S\d{2})*)\]', replace, value)

system_start = front.index('<a id="system-use"></a>')
index_start = front.index('<a id="target-index"></a>')
preamble = front[:system_start].rstrip()
system_section = front[system_start:index_start].rstrip()
preamble = preamble.replace(
    'Entry identities and original definitions are preserved.',
    'Entry identities and original definitions are preserved. Human experience is the default scope; the AI section describes functional changes without attributing human feelings to an AI.'
)
intro, examples = preamble.split('**Choosing the relevant contribution**', 1)
opening, scope = intro.split('\n\n“Direct”', 1)
scope = '“Direct”' + scope
scope = scope.replace(' More change is not automatically better: the direction, affected concerns, timing, duration, transfer, and cost determine what would contribute.', '')
preamble = opening.rstrip() + '\n\n**Choosing the relevant contribution**' + examples.rstrip() + '\n\n' + scope.strip()
parts = [preamble, '[Entry index](#target-index) · [Required Subject Systems use](#system-use) · [Functional AI self-change](#ai-changes) · [Source notes](#sources)', '<a id="target-index"></a>\n**Entry index**']
index = ['| Family | Entries |', '|---|---|']
identity = 1
for family_number, (name, entries) in enumerate(groups, 1):
    end = identity + len(entries) - 1
    index.append(f'| [{family_number}. {name}](#family-{family_number}) | {identity}–{end} |')
    identity = end + 1
parts.append('\n'.join(index))
parts.append('**Mind-change targets, contributors, and conditions**\n\nEach contributor set is a candidate map at the stated functional level. Only the particular source-marked statements carry the empirical or theoretical support specified in their notes. Neighboring entries can describe different components of the same event.')
identity = 0
definitions = []
for family_number, (name, entries) in enumerate(groups, 1):
    parts.append(f'<a id="family-{family_number}"></a>\n**{family_number}. {name}**')
    for entry in entries:
        identity += 1
        label, definition = entry.split(': ', 1)
        definition = definition.rstrip('.') + '.'
        definitions.append((identity, f'{label}: {definition}'))
        contributors, conditions = rows[identity]
        parts.append(f'**{identity}. {label}:** {definition}\n\nContributors: {link_sources(contributors)}\n\nConditions and distinctions: {link_sources(conditions)}')
    parts.append('[Return to entry index](#target-index)')

parts.append(system_section)

prior_general = original.split('**Operations that can apply across targets**', 1)[1].split('**Functional AI self-change**', 1)[0]
parts.append('**Operations that can apply across targets**' + prior_general.rstrip())

parts.append('<a id="ai-changes"></a>\n**Functional AI self-change: contributors and conditions**\n\nAI-1 through AI-26 preserve the original separate list. These are working interpretations, explicit records, conduct, and editable supporting systems. A record or prompt change does not establish a change to trained model parameters.')
for number, target in enumerate(extras['ai'], 1):
    contributors, conditions = ai_rows[number]
    parts.append(f'**AI-{number}. {target.rstrip(".")}.**\n\nContributors: {contributors}\n\nConditions and distinctions: {conditions}')

assessment_routes = ['R1', 'R2', 'R3', 'R5', 'R4', 'R8', 'R1', 'R1, R5, R7', 'R5', 'R7', 'R6', 'R8', 'R7', 'R6, R7, R8']
assert len(assessment_routes) == len(extras['assessment']) == 14
assessment = ['**Assistant ability: original qualitative assessment with required system routes**', 'The observations below are preserved from the preceding inventory. The route column connects every listed limitation to the standing instruction; it is not a claim that adding a route has already eliminated the weakness.', '| Ability | Available operation or observed strength | Limit or observed failure | Required route when relevant |', '|---|---|---|---|']
for record, route in zip(extras['assessment'], assessment_routes):
    assessment.append('| ' + ' | '.join(record + [f'[{route}](#system-use)']) + ' |')
assessment.append('\nThese are not comparative benchmark results. Performing an operation on text is distinct from establishing a beneficial change in its recipient.')
parts.append('\n\n'.join(assessment[:2]) + '\n\n' + '\n'.join(assessment[2:]))

failure_text = original.split('**Effects that can diverge within one encounter**', 1)[1].split('**Source-supported distinctions**', 1)[0]
parts.append('**Effects that can diverge within one encounter**' + failure_text.rstrip())

parts.append('<a id="sources"></a>\n**Source notes and support boundaries**\n\nThese are focused checks of primary research, original theoretical accounts, and one original researcher’s retrospective account. They are not a systematic review of every candidate in the inventory. Sources support the particular distinctions stated below, with observational, experimental, theoretical, and proposed relationships kept separate. Full papers, author manuscripts, or abstracts were used as identified; S01 relies on the indexed abstract. The unmarked entry-level contributor sets remain an original functional synthesis, not findings attributed wholesale to these sources.')
for s in sources:
    parts.append(f"**[{s['id']} — {s['title']}]({s['url']})**\n\n{s['evidence']}. {s['note']}")

prior_sources = original.split('**Source-supported distinctions**', 1)[1].strip()
prior_context = prior_sources.split("In Gross's 1998 experiment", 1)[0].strip()
parts.append('**Scope retained from the earlier inventory**\n\n' + prior_context)
parts.append('**Extension record**\n\nAll 590 inherited target identities and definitions, 26 AI targets, and 14 assessment rows are retained. Each target now has a contributor set and a condition/distinction field. The 62 families overlap and are not independent validated constructs. Thirty-one canonical subject identities were checked against the inspected catalog; C1–C4 remain separately identified local system specifications. No claim of universal contributor completeness, causal sufficiency, optimality, or recipient transformation follows from coverage of this list.')

result = '\n\n'.join(parts).rstrip() + '\n'
result = re.sub(r'\n{3,}', '\n\n', result)

original_target_text = original.split('**Mind-change targets**', 1)[1].split('**Operations that can apply across targets**', 1)[0]
original_definitions = [(int(m.group(1)), m.group(2)) for m in re.finditer(r'^(\d+)\. (.+)$', original_target_text, re.M)]
assert original_definitions == definitions, 'An inherited definition changed'
assert re.findall(r'^\*\*(\d+)\. [^\n]+:\*\* ', result, re.M) == [str(i) for i in range(1, 591)]
assert re.findall(r'^\*\*AI-(\d+)\.', result, re.M) == [str(i) for i in range(1, 27)]
assert result.count('\nContributors: ') == 616
assert result.count('\nConditions and distinctions: ') == 616
assert not re.search(r'\[S\d{2}(?:, S\d{2})*\](?!\()', result)
anchors = re.findall(r'<a id="([^"]+)"></a>', result)
assert len(anchors) == len(set(anchors))
assert set(re.findall(r'\]\(#([^\)]+)\)', result)).issubset(set(anchors))
canonical = {s['id'] for s in json.loads((ROOT / 'repository-snapshots/perspectiveoptimizer/sources/subject-bindings.json').read_text())['subjects']}
refs = re.findall(r'`([a-z]+(?:-[a-z]+)+)`', system_section)
assert set(refs).issubset(canonical)
assert len(refs) == 31
assert not any(token in result for token in ['TODO', 'TBD', 'turn72search', 'turn73view'])

output = ROOT / 'Mind_Change_Inventory.md'
output.write_text(result)
verification = {
    'file': str(output),
    'main_targets': len(rows),
    'ai_targets': len(ai_rows),
    'families': len(groups),
    'assessment_rows_with_routes': len(assessment_routes),
    'canonical_subject_references': len(refs),
    'source_notes': len(sources),
    'definitions_preserved': original_definitions == definitions,
    'bytes': len(result.encode()),
    'words': len(result.split()),
    'all_internal_links_resolve': True,
}
(ROOT / 'inventory_expansion_verification.json').write_text(json.dumps(verification, indent=2) + '\n')
print(json.dumps(verification, indent=2))
