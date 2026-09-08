"""Check this integration's navigation, source integrity and finite worked cases.

This is not a certification of all historical studies or human effects.
"""
from fractions import Fraction
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import checkpoint


def validate():
    ledger = checkpoint.validate_ledger()
    source = ROOT / 'sources/perspective-inquiries-25'
    manifest = json.loads((source / 'import-manifest.json').read_text())
    for entry in manifest['files']:
        data = (source / entry['path']).read_bytes()
        assert len(data) == entry['bytes'], entry['path']
        assert hashlib.sha256(data).hexdigest() == entry['sha256'], entry['path']

    canonical = (source / 'Perspective_Inquiries_25.md').read_text()
    marks = list(re.finditer(r'^\*\*(\d+)\. (.+?)\*\*[ \t]*$', canonical, re.M))
    assert [int(m[1]) for m in marks] == list(range(1, 26))
    end = canonical.index('**What follows when the inquiries constrain one another**')
    counts = []
    for i, mark in enumerate(marks):
        body = canonical[mark.start():marks[i+1].start() if i < 24 else end].strip() + '\n'
        view = (ROOT / f'inquiries/perspective-25/{i+1:02d}.md').read_text()
        assert view.endswith(body), f'Inquiry {i+1} differs from its source'
        counts.append(len(re.findall(r'^\d+(?:\.\d+)?\. ', body, re.M)))
        if i == 6:
            assert not re.search(r'\b(?:perspectiv\w*|system\w*|optimi[sz]\w*|problem\w*|solution\w*)\b', body, re.I)
    assert counts == [14]*7 + [15]*8 + [16]*5 + [15]*5, counts
    assert sum(counts) == 373
    conclusion = (ROOT / 'inquiries/perspective-25/cross-inquiry-and-method.md').read_text()
    assert conclusion.endswith(canonical[end:])

    current = [ROOT / name for name in ['README.md', 'Mind_Change_Research_Index.md', 'intent.md', 'working-instruction.md', 'repository-sync.md', 'progress.md']]
    for directory in ['changes', 'recipes', 'inquiries/perspective-25', 'reviews', 'studies']:
        current.extend((ROOT / directory).glob('*.md'))
    current.append(source / 'README.md')
    checked = 0
    errors = []
    for path in current:
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)', path.read_text()):
            target = unquote(target)
            url = urlsplit(target)
            if url.scheme in {'http', 'https', 'mailto'} or target.startswith('#'):
                continue
            if url.scheme or target.startswith('/'):
                errors.append(f'{path.relative_to(ROOT)}: nonportable link {target}')
                continue
            dest = (path.parent / url.path).resolve()
            if not dest.is_relative_to(ROOT) or not dest.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing link {target}')
            checked += 1
    assert not errors, '\n'.join(errors)

    # Derive the published confidence examples using joint event probabilities,
    # not report count. Choose P(E|H)=4/5 and P(E|not H)=1/5.
    prior = Fraction(1, 10)
    def posterior(lh, ln):
        return prior * lh / (prior * lh + (1-prior) * ln)
    copied = posterior(Fraction(4, 5), Fraction(1, 5))
    independent = posterior(Fraction(4, 5)**2, Fraction(1, 5)**2)
    assert copied == Fraction(4, 13) < Fraction(1, 2)
    assert independent == Fraction(16, 25) > Fraction(1, 2)

    # Verify the stated policy regions against all three policies, including ties.
    def best(p):
        values = {'commit': Fraction(5), 'reserve': 3*p+3, 'wait': 8*p-1}
        return {k for k, v in values.items() if v == max(values.values())}
    assert best(Fraction(1, 2)) == {'commit'}
    assert best(Fraction(2, 3)) == {'commit', 'reserve'}
    assert best(Fraction(3, 4)) == {'reserve'}
    assert best(Fraction(4, 5)) == {'reserve', 'wait'}
    assert best(Fraction(1)) == {'wait'}

    # Same person-hour totals, different simultaneous availability.
    a, b = [(9, 13), (9, 13)], [(9, 13), (13, 17)]
    def total(intervals):
        return sum(end-start for start, end in intervals)
    def overlap(intervals):
        return max(0, min(end for _, end in intervals)-max(start for start, _ in intervals))
    assert total(a) == total(b) == 8
    assert overlap(a) == 4 and overlap(b) == 0
    throughput, recovery = {'A': 10, 'B': 8}, {'A': 2, 'B': 6}
    assert max(throughput, key=throughput.get) == 'A'
    assert max(recovery, key=recovery.get) == 'B'

    return {'imported_artifacts_verified': len(manifest['files']), 'inquiries': 25,
            'options': 373, 'current_navigation_links_checked': checked,
            'application_records_hash_verified': sum(bool(x.get('record_sha256')) for x in ledger['applications']),
            'worked_cases': ['copied/independent evidence', 'timing policy regions and ties', 'equal totals/different overlap', 'criterion-dependent rankings'],
            'scope': 'Source, navigation, accounting and finite calculations; no human-effect or general-perfection certification'}


if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
