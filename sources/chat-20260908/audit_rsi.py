from pathlib import Path
from itertools import product
from collections import Counter
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parent
PO = ROOT / 'repository-snapshots/perspectiveoptimizer'
SS = ROOT / 'repository-snapshots/subjectsystems'
sys.path.insert(0, str(PO))
from perspectiveoptimizer.core import ContractError, required_gate, OPERATIONS
from perspectiveoptimizer.space import expand_space, transition_reachability

spec = importlib.util.spec_from_file_location('study_methods', SS / 'tools/study_methods.py')
methods = importlib.util.module_from_spec(spec)
spec.loader.exec_module(methods)

space = json.loads((PO / 'cases/learning-space.json').read_text())
extension = {
    'kind': 'add_dimension',
    'dimension': 'punctuation',
    'values': [
        {'id': 'period', 'description': 'End the description with a period.',
         'contribution': 'No substantive change to the interpretation or operation.'},
        {'id': 'exclamation', 'description': 'End the description with an exclamation mark.',
         'contribution': 'No substantive change to the interpretation or operation.'},
    ],
    'contrast': {'old_case': 'The same description ends with a period.',
                 'new_case': 'The same description ends with an exclamation mark.',
                 'consequential_difference': 'None: meaning, operation, and task outcome are unchanged.'},
}
expanded = expand_space(space, extension)

graph = {'states': ['initial', 'improved'], 'start': 'initial', 'observations': {},
         'transitions': [{'id': 'declared_only', 'from': 'initial', 'to': 'improved',
                          'operation': 'Improve the system using an operation that has no implementation.'}]}
reach = transition_reachability(graph)

outcomes = Counter()
statuses = Counter()
mapping = {True: 'true', False: 'false', None: 'unknown'}
for a, b, optional, abandoned in product([True, False, None], [True, False, None], [True, False, None], [False, True]):
    required = {'a': a, 'b': b}
    reference = methods.achievement_status(required, {'optional': optional}, abandoned)
    statuses[reference['achievement']] += 1
    try:
        required_gate([[required]], {'required_fields': ['a', 'b']})
    except ContractError:
        outcomes['direct_rejected'] += 1
    naive = {key: 'true' if value else 'false' for key, value in required.items()}
    naive_result = required_gate([[naive]], {'required_fields': ['a', 'b']})[0]
    outcomes['truthiness_status_mismatch'] += naive_result['status'] != reference['achievement']
    exact = {key: mapping[value] for key, value in required.items()}
    exact_result = required_gate([[exact]], {'required_fields': ['a', 'b']})[0]
    outcomes['exact_status_match'] += exact_result['status'] == reference['achievement']
    full = {'achievement': exact_result['status'], 'failed_required': exact_result['failed'],
            'unknown_required': exact_result['unknown'], 'optional_observations': {'optional': optional},
            'activity': 'abandoned' if abandoned else 'not_marked_abandoned'}
    outcomes['exact_full_match'] += full == reference

report = {
    'source_commits': {'subjectsystems': '8605d44181fab127087ba27c60448f24cdc3b1c7',
                       'perspectiveoptimizer': '7277935d3e9267b6103f7188ed65a95a3f0dc6c2'},
    'nonconsequential_extension': {'accepted': True, 'before': expanded['before_count'],
                                  'after': expanded['after_count'],
                                  'standing': expanded['space']['construction_history'][-1]['standing']},
    'unimplemented_declared_transition': {'reachable': reach['reachable'], 'standing': reach['standing']},
    'current_interface_comparison': {'domain_size': 54, 'reference_statuses': dict(statuses), **dict(outcomes)},
    'registered_core_operations': sorted(OPERATIONS),
    'interpretation': 'These probes establish finite behavior and its semantic boundaries; they do not measure LLM self-improvement.'
}
(ROOT / 'audit_results.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
