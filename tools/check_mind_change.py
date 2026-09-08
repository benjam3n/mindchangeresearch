"""Check imported meaning, provenance, current access, and correction uptake."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources/chat-20260908'


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--integration-baseline', action='store_true',
                        help='Also require no initial-slot status change during this integration')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'mind-change/targets.json').read_text())
    base = json.loads((SOURCE / 'mind_change_base.json').read_text())
    records = {t['id']: t for t in catalog['targets']}
    require(len(records) == len(catalog['targets']) == 616, 'Target loss or duplicate identity')
    definitions = [v for _, entries in base['groups'] for v in entries]
    expected = {str(i): d for i, d in enumerate(definitions, 1)}
    expected.update({f'AI-{i}': d for i, d in enumerate(base['extras']['ai'], 1)})
    require({k: v['definition'] for k, v in records.items()} == expected, 'Inherited definition drift')
    for path in SOURCE.glob('contributors_*.txt'):
        for line in path.read_text().splitlines():
            number, contributors, conditions = line.split('|')
            identity = 'AI-' + number if path.name == 'contributors_ai.txt' else number
            require(records[identity]['candidate_contributors'] == contributors, f'Contributor loss: {identity}')
            require(records[identity]['conditions'] == conditions, f'Condition loss: {identity}')
    source_manifest = json.loads((SOURCE / 'source-manifest.json').read_text())
    for item in source_manifest['files']:
        require(hashlib.sha256((SOURCE / item['path']).read_bytes()).hexdigest() == item['sha256'],
                f'Preserved source changed: {item["path"]}')
    refs = re.findall(r'`([a-z]+(?:-[a-z]+)+)`', (ROOT / 'mind-change/subject-systems.md').read_text())
    canonical = {s['id'] for s in json.loads((SOURCE / 'repository-snapshots/perspectiveoptimizer/sources/subject-bindings.json').read_text())['subjects']}
    require(len(refs) == 31 and set(refs) <= canonical, 'Canonical subject reference drift')

    current = [ROOT / 'README.md', ROOT / 'Mind_Change_Research_Index.md',
               ROOT / 'working-instruction.md', ROOT / 'repository-sync.md']
    current += sorted((ROOT / 'mind-change').rglob('*.md'))
    current += [ROOT / 'research' / p for p in ['intent-audit.md', 'chat-integration.md', 'status.md']]
    destinations = set()
    count = 0
    for path in current:
        text = path.read_text()
        require(not re.search(r'\]\(sandbox:', text), f'Transient repository link: {path}')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'[a-zA-Z]+://', target):
                continue
            target, _, anchor = target.partition('#')
            dest = (path.parent / target).resolve() if target else path
            require(dest.is_relative_to(ROOT), f'Link outside repository: {path}: {target}')
            require(dest.is_file(), f'Missing current destination: {path}: {target}')
            if anchor:
                content = dest.read_text()
                explicit = re.findall(r'<a id="([^"]+)"', content)
                headings = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
                            for h in re.findall(r'^#+ (.+)$', content, re.M)]
                require(anchor in explicit + headings, f'Missing anchor: {dest}#{anchor}')
            destinations.add(dest.relative_to(ROOT).as_posix())
            count += 1
    for name in ['working-instruction.md', 'methods/improved-research-prompt.txt', 'automation-prompt.txt']:
        text = (ROOT / name).read_text()
        require('mind-change/subject-systems.md' in text, f'Missing system rule: {name}')
        require('do not impose the former recipe card as a universal starting sequence' in text, f'Entry-point rule missing: {name}')
        require('realized epistemic transition' not in text, f'Reintroduced scope narrowing: {name}')
    ledger = json.loads((ROOT / 'Research_Ledger.json').read_text())
    capability_record = next(record for cycle in ledger['post_allocation_cycles']
                             for record in cycle['records'] if record['id'] == 'PAC03-SPG-01')
    # Preserve the actual assessment without requiring a rejected prose template.
    require(capability_record['assessment_correction']['recipe_implementation_status'] == 'UNRESOLVED'
            and capability_record['implementation_status'] ==
            'partial specification; locus diagnosis and mechanism construction remain unresolved',
            'Implementation-completeness correction was lost')
    require((ROOT / capability_record['file']).is_file(), 'Corrected capability record is missing')
    require('index=f' not in (ROOT / 'checkpoint.py').read_text(), 'Obsolete index generator restored')

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    for identity in ['368', 'AI-1']:
        output = subprocess.check_output([sys.executable, 'tools/mind_change.py', '--target', identity, '--json'],
                                         cwd=ROOT, env=env, text=True)
        require(json.loads(output) == [records[identity]], f'Retrieval failed: {identity}')
    bad = subprocess.run([sys.executable, 'tools/mind_change.py', '--target', '999999'],
                         cwd=ROOT, env=env, capture_output=True)
    require(bad.returncode != 0, 'Unknown target incorrectly accepted')

    with tempfile.TemporaryDirectory(prefix='mind-change-probe-') as folder:
        temp = Path(folder)
        shutil.copy2(SOURCE / 'audit_rsi.py', temp / 'audit_rsi.py')
        (temp / 'repository-snapshots').symlink_to(SOURCE / 'repository-snapshots', target_is_directory=True)
        result = subprocess.run([sys.executable, str(temp / 'audit_rsi.py')], env=env,
                                capture_output=True, text=True)
        require(result.returncode == 0, 'Historical executable probe failed: ' + result.stderr)
        replay = json.loads((temp / 'audit_results.json').read_text())
        old = json.loads((SOURCE / 'audit_results.json').read_text())
        for key in ['source_commits', 'nonconsequential_extension', 'unimplemented_declared_transition',
                    'current_interface_comparison', 'registered_core_operations']:
            require(replay[key] == old[key], f'Historical result changed: {key}')
    (ROOT / 'research/chat-probe-replay.json').write_text(json.dumps({
        'scope': 'Replay of preserved finite probes at pinned source commits. Historical source-path recovery is preserved separately and not rerun by this script.',
        'results': replay}, indent=2) + '\n')

    ledger = json.loads((ROOT / 'Research_Ledger.json').read_text())
    baseline = json.loads((ROOT / 'research/chat-integration-baseline.json').read_text())
    slots = {a['slot_id']: a['status'] for a in ledger['applications']}
    require(set(slots) == set(baseline['initial_slots']), 'Frozen allocation identities changed')
    unchanged = slots == baseline['initial_slots']
    if args.integration_baseline:
        require(unchanged, 'Integration changed an initial application status')
    integration = json.loads((ROOT / 'research/chat-integration.json').read_text())
    require(integration['initial_allocation_credit'] == integration['distinct_new_finding_credit'] == 0,
            'Imported material incorrectly awarded credit')
    report = {'status': 'passed', 'scope': 'Data, source fidelity, current access, correction uptake, executable retrieval, and finite source behavior; not human efficacy or universal recipe completeness.',
              'targets': len(records), 'families': len(catalog['families']), 'preserved_source_files': len(source_manifest['files']),
              'canonical_subject_references': len(refs), 'current_documents_checked': len(current),
              'current_link_occurrences_checked': count, 'required_direct_destinations': sorted(destinations),
              'initial_slot_statuses_unchanged_from_integration_baseline': unchanged,
              'integration_baseline_gate_applied': args.integration_baseline,
              'retrieval_cases': ['368', 'AI-1', 'unknown target rejected'],
              'historical_probe_replay': 'passed for five preserved result groups',
              'active_instruction_copies_checked': 3}
    (ROOT / 'research/chat-integration-checks.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'required_direct_destinations'}))


if __name__ == '__main__':
    main()
