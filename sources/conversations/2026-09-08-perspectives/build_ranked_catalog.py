from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'Perspectives_3000.json'
source_bytes = SOURCE.read_bytes()
source = json.loads(source_bytes)
original = source['perspectives']
assessment_rows = [
    line.split() for line in (ROOT / 'ranking-assessment.txt').read_text().splitlines()
    if line.startswith('S')
]
assert len(assessment_rows) == 150
assert [r[0] for r in assessment_rows] == [s['id'] for s in source['subjects']]
assert all(len(r) == 21 for r in assessment_rows)
codes = [code for row in assessment_rows for code in row[1:]]
assert len(codes) == len(original) == 3000
assert set(codes) <= set('ABCDEFGHI')
leaders = json.loads((ROOT / 'ranking-leaders.json').read_text())
leader_numbers = [x['number'] for x in leaders]
assert len(leader_numbers) == len(set(leader_numbers)) == 60
assert all(codes[n - 1] == 'A' for n in leader_numbers)
leader_map = {x['number']: x for x in leaders}
leader_set = set(leader_numbers)
counts = Counter(codes)

profile_specs = [
    ('A', 'High', 'Low'),
    ('B', 'High', 'Moderate'),
    ('C', 'Moderate', 'Low'),
    ('D', 'High', 'High'),
    ('E', 'Moderate', 'Moderate'),
    ('F', 'Limited', 'Low'),
    ('G', 'Moderate', 'High'),
    ('H', 'Limited', 'Moderate'),
    ('I', 'Limited', 'High'),
]
profiles = []
position = 1
for priority, (code, benefit, effort) in enumerate(profile_specs, 1):
    profiles.append({
        'profile': code,
        'priority': priority,
        'expected_benefit': benefit,
        'expected_effort': effort,
        'entry_count': counts[code],
        'list_position_start': position,
        'list_position_end': position + counts[code] - 1,
    })
    position += counts[code]
profile_map = {p['profile']: p for p in profiles}

criterion = (
    'Expected reusable beneficial mind change relative to the effort needed to '
    'understand, recognize the relevance of, and make a first consequential use '
    'of the perspective as written.'
)
assumption = (
    'The relevant distinction is not already reliably usable by the recipient. '
    'The default is broad usefulness across thinking, learning, action, '
    'self-understanding, relationships, and inquiry, rather than immediate '
    'novelty to one particular reader.'
)
epistemic_status = (
    'Prospective editorial judgments, not measured psychological effects. '
    'All 3,000 statements received an individually assigned benefit/effort '
    'profile. The 60 leaders received a further provisional comparative '
    'ordering and individual rationales. Other entries are tied within their '
    'profile; source order inside a tie is for lookup only.'
)
benefit_definitions = {
    'High': 'Potential to change a recurring or foundational discrimination, '
            'interpretation, evaluative rule, available operation, or capacity '
            'across a broad range of relevant situations.',
    'Moderate': 'A useful change within a more specific question, domain, or '
                'interpretive task, with less broad immediate reuse.',
    'Limited': 'The formulation alone supplies little identifiable practical '
               'or interpretive gain for this general purpose; much of its '
               'value is descriptive, specialized, or dependent on further '
               'justification.',
}
effort_definitions = {
    'Low': 'The statement supplies a readily usable distinction, comparison, '
           'or diagnostic question with relatively little additional conceptual '
           'construction. Carrying out the resulting action may still be hard.',
    'Moderate': 'Relevant cases, mechanisms, or implications need further '
                'reconstruction before the statement changes a consequential '
                'judgment or operation.',
    'High': 'Substantial method construction, conceptual development, or '
            'justification of disputed commitments is needed to obtain a '
            'usable benefit from the formulation.',
}
ordering_note = (
    'The profile order is an explicit practical tradeoff judgment, not a '
    'numerical benefit/effort ratio. It favors high reusable benefit with low '
    'or moderate effort, then moderate benefit available at low effort. A '
    'reader prioritizing maximum depth regardless of effort could reasonably '
    'move high-benefit/high-effort entries upward.'
)
context_note = (
    'A concrete target or recipient can reverse this order. For an execution '
    'difficulty, capability and control distinctions may come first; for '
    'conflict, differences in meaning and concern may come first. Perspectives '
    'on art, metaphysics, religion, or mortality may matter much more within '
    'their own inquiries than this broad practical ranking suggests.'
)
evidence_note = (
    'Reported understanding can exceed what a person can actually explain: '
    'Rozenblit and Keil studied this as an illusion of explanatory depth. '
    'That finding supports checking achieved understanding separately from '
    'confidence. It does not validate the profile assignments or the '
    'comparative ranking in this catalog.'
)
evidence_source = {
    'title': 'Rozenblit & Keil (2002), The misunderstood limits of folk science: '
             'an illusion of explanatory depth',
    'url': 'https://pubmed.ncbi.nlm.nih.gov/21442007/',
    'role': 'Background for distinguishing reported confidence from assessed '
            'understanding; not evidence for relative efficacy of these entries.',
}

ranked = []

def add_entry(number, rank, tie_size):
    entry = dict(original[number - 1])
    profile = profile_map[codes[number - 1]]
    record = {
        'rank': rank,
        'rank_span_start': rank,
        'rank_span_end': rank + tie_size - 1,
        'tie_size': tie_size,
        'list_position': len(ranked) + 1,
        'profile': profile['profile'],
        'expected_benefit': profile['expected_benefit'],
        'expected_effort': profile['expected_effort'],
        **entry,
    }
    if number in leader_map:
        record['change_enabled'] = leader_map[number]['change_enabled']
        record['ranking_reason'] = leader_map[number]['reason']
    ranked.append(record)

for rank, number in enumerate(leader_numbers, 1):
    add_entry(number, rank, 1)
tie_groups = []
for profile in profiles:
    numbers = [
        entry['number'] for entry, code in zip(original, codes)
        if code == profile['profile'] and entry['number'] not in leader_set
    ]
    if not numbers:
        continue
    rank = len(ranked) + 1
    tie_groups.append({
        'profile': profile['profile'],
        'rank': rank,
        'rank_span_end': rank + len(numbers) - 1,
        'entry_count': len(numbers),
    })
    for number in numbers:
        add_entry(number, rank, len(numbers))

payload = {
    'title': '3,000 Perspectives Ranked for Beneficial and Efficient Mind Change',
    'created': date(2026, 9, 8).isoformat(),
    'entry_count': len(ranked),
    'subject_count': source['subject_count'],
    'individually_ordered_leaders': len(leaders),
    'ranking_criterion': criterion,
    'recipient_assumption': assumption,
    'epistemic_status': epistemic_status,
    'benefit_definitions': benefit_definitions,
    'effort_definitions': effort_definitions,
    'profile_ordering_note': ordering_note,
    'context_note': context_note,
    'beneficial_change': 'Gain for the person whose mind changes, in warranted '
                         'understanding, usable distinctions, attention, '
                         'capability, agency, considered priorities, or '
                         'relations with others. Agreement or confidence '
                         'alone does not establish that gain.',
    'independent_potential_note': 'Each entry is rated for its independent '
                                  'potential. Related entries can have much '
                                  'less marginal benefit after their shared '
                                  'distinction has already been learned.',
    'truth_note': 'The source includes contested and mutually incompatible '
                  'positions. Ranking does not establish their truth. '
                  'Unsupported premises reduce credited benefit or increase '
                  'the work needed to justify a useful application.',
    'rank_convention': 'Competition ranking: tied entries share the first '
                       'position occupied by their group; the next rank skips '
                       'the remaining positions in the tie. list_position is '
                       'a unique display index and does not break a tie.',
    'source': {
        'filename': SOURCE.name,
        'sha256': hashlib.sha256(source_bytes).hexdigest(),
        'original_text_preserved': True,
    },
    'evidence_note': evidence_note,
    'sources': [evidence_source],
    'profiles': profiles,
    'tie_groups': tie_groups,
    'subjects': source['subjects'],
    'perspectives': ranked,
}

lines = [
    '# 3,000 perspectives ranked for beneficial and efficient mind change',
    '',
    '**Complete ranking of the original 3,000 entries: 60 provisionally ordered '
    'leaders, followed by tied benefit/effort bands. Original IDs, names, '
    'subjects, and statements are preserved.**',
    '',
    criterion + ' ' + assumption,
    '',
    'Benefit belongs to the person whose mind changes. It includes better '
    'understanding, attention, usable distinctions and operations, agency, '
    'considered priorities, and understanding of others. Agreement or '
    'confidence alone does not establish a beneficial change.',
    '',
    epistemic_status,
    '',
    '## How to read the ranking',
    '',
    'The first 60 places are a reasoned, provisional ordering; close positions '
    'should not be read as precise efficacy differences. Every later group '
    'shares a rank. For example, the 660 entries after the leaders are tied at '
    'rank 61 and occupy positions 61–720; the next group starts at rank 721. '
    'No further superiority is claimed for the source order inside a tie.',
    '',
    ordering_note,
    '',
    '| Priority band | Expected benefit | Expected effort | Entries | List positions |',
    '|---|---|---|---:|---|',
]
for p in profiles:
    lines.append(f"| {p['profile']} | {p['expected_benefit']} | {p['expected_effort']} "
                 f"| {p['entry_count']:,} | {p['list_position_start']:,}–{p['list_position_end']:,} |")
lines += ['', '**Benefit definitions**', '']
for label, definition in benefit_definitions.items():
    lines.append(f'- **{label}:** {definition}')
lines += ['', '**Effort definitions**', '']
for label, definition in effort_definitions.items():
    lines.append(f'- **{label}:** {definition}')
lines += [
    '',
    'These are ordinal judgments, without measured effect sizes, probabilities, '
    'or time estimates. Each formulation was assessed for what it actually '
    'makes available; a grand aim receives no automatic credit for a method '
    'that would still need to be invented.',
    '',
    payload['independent_potential_note'],
    '',
    context_note,
    '',
    payload['truth_note'],
    '',
    'Reported understanding can exceed what a person can actually explain: '
    'Rozenblit and Keil studied this as an illusion of explanatory depth. '
    '[Rozenblit & Keil (2002)](https://pubmed.ncbi.nlm.nih.gov/21442007/). '
    'That finding supports checking achieved understanding separately from '
    'confidence. It does not validate this catalog’s profile assignments or '
    'comparative ordering.',
    '',
    '## Leading perspectives: ranks 1–60',
    '',
    'All 60 have the high-benefit, low-effort profile under the definitions '
    'above. Each statement is followed by the change it could enable and '
    'the reason for its placement.',
    '',
]
for entry in ranked[:60]:
    lines += [
        f"### {entry['rank']}. {entry['name']} — {entry['id']}",
        '',
        f"**Subject:** {entry['subject']}",
        '',
        entry['statement'],
        '',
        f"**Change enabled:** {entry['change_enabled']}",
        '',
        f"**Why it ranks highly:** {entry['ranking_reason']}",
        '',
    ]
for group in tie_groups:
    p = profile_map[group['profile']]
    lines += [
        f"## Band {group['profile']}: {p['expected_benefit'].lower()} benefit, "
        f"{p['expected_effort'].lower()} effort — tied rank {group['rank']:,}",
        '',
        f"**{group['entry_count']:,} entries; positions {group['rank']:,}–"
        f"{group['rank_span_end']:,}.** Entries in this group share a rank. "
        'They appear in original catalog order for lookup.',
        '',
    ]
    entries = [e for e in ranked if e['rank'] == group['rank']]
    assert len(entries) == group['entry_count']
    for entry in entries:
        lines.append(f"- **{entry['id']} · {entry['name']}** ({entry['subject']}) — "
                     f"{entry['statement']}")
    lines.append('')
lines += [
    '---',
    '',
    f"Source: `{SOURCE.name}`. All 3,000 original entries retained exactly once. "
    'The accompanying JSON contains rank, tie size, unique list position, '
    'benefit, effort, source identity, and the 60 individual rationales.',
    '',
]

# Verify preservation and ranking integrity before producing deliverables.
assert len(ranked) == 3000
assert len({e['id'] for e in ranked}) == 3000
assert {e['id'] for e in ranked} == {e['id'] for e in original}
original_by_id = {e['id']: e for e in original}
for entry in ranked:
    for key, value in original_by_id[entry['id']].items():
        assert entry[key] == value, (entry['id'], key)
assert [e['list_position'] for e in ranked] == list(range(1, 3001))
assert [e['rank'] for e in ranked] == sorted(e['rank'] for e in ranked)
assert all(e['rank_span_start'] <= e['list_position'] <= e['rank_span_end'] for e in ranked)
assert sum(p['entry_count'] for p in profiles) == 3000

md_path = ROOT / 'Perspectives_3000_Ranked.md'
json_path = ROOT / 'Perspectives_3000_Ranked.json'
md_path.write_text('\n'.join(lines), encoding='utf-8')
json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for path in (md_path, json_path):
    print(f'{path.name}: {path.stat().st_size:,} bytes')
print('Verified 3,000 unique, unchanged original entries; 60 leaders; 9 tied groups.')
print('Source SHA-256:', hashlib.sha256(source_bytes).hexdigest())
print('Tied groups:', json.dumps(tie_groups))
