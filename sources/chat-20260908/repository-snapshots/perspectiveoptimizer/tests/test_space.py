from copy import deepcopy
import json
from pathlib import Path
import unittest

from perspectiveoptimizer.core import ContractError
from perspectiveoptimizer.space import enumerate_space, expand_space, route_studies, transition_reachability

ROOT = Path(__file__).resolve().parents[1]
def fixture(name):
    return json.loads((ROOT / 'cases' / name).read_text())


class ConstructionTests(unittest.TestCase):
    def test_all_assignments_retained_with_exclusion_reasons(self):
        result = enumerate_space(fixture('learning-space.json'))
        self.assertEqual((result['assignment_count'], result['open_count']), (12, 5))
        self.assertEqual(len({c['id'] for c in result['candidates']}), 12)
        excluded = [c for c in result['candidates'] if c['status'] != 'open_candidate']
        self.assertEqual(len(excluded), 7)
        self.assertTrue(all(c['exclusions'] for c in excluded))

    def test_expansion_preserves_start_and_adds_distinct_contribution(self):
        source = fixture('learning-space.json')
        before = deepcopy(source)
        result = expand_space(source, fixture('application-condition-extension.json'))
        self.assertEqual(source, before)
        self.assertEqual((result['before_count'], result['after_count']), (12, 16))
        self.assertEqual(result['enumeration']['open_count'], 7)
        self.assertEqual(len(result['space']['construction_history']), 1)

    def test_new_dimension_can_expand_the_construction_basis(self):
        result = expand_space(fixture('learning-space.json'), {
            'kind': 'add_dimension', 'dimension': 'activation_condition',
            'values': [
                {'id': 'wording', 'description': 'Familiar wording supplies the cue.', 'contribution': 'Examine recognition after wording changes.'},
                {'id': 'relation', 'description': 'The governing relation supplies the cue.', 'contribution': 'Examine recognition across varied wording.'}],
            'contrast': {'old_case': 'The same method is chosen now.', 'new_case': 'Only one cue survives altered wording.',
                         'consequential_difference': 'Later recognition differs while present choice agrees.'}})
        self.assertEqual(result['after_count'], 24)

    def test_duplicate_value_identity_is_rejected(self):
        extension = fixture('application-condition-extension.json')
        extension['value']['id'] = 'missing_content'
        with self.assertRaises(ContractError):
            expand_space(fixture('learning-space.json'), extension)

    def test_unknown_rule_reference_is_not_silently_ignored(self):
        source = fixture('learning-space.json')
        source['incompatibilities'][0]['when']['absent_dimension'] = 'x'
        with self.assertRaises(ContractError):
            enumerate_space(source)

    def test_missing_consequential_contrast_rejects_extension(self):
        extension = fixture('application-condition-extension.json')
        del extension['contrast']
        with self.assertRaises(ContractError):
            expand_space(fixture('learning-space.json'), extension)

    def test_execution_bound_does_not_return_false_completeness(self):
        source = fixture('learning-space.json')
        source['dimensions']['large'] = [
            {'id': str(i), 'description': 'Explicit value ' + str(i), 'contribution': 'Bound check.'}
            for i in range(400)]
        with self.assertRaises(ContractError):
            enumerate_space(source)

    def test_nonconscious_bearer_has_no_goal_or_choice_requirement(self):
        source = fixture('nonconscious-space.json')
        self.assertNotIn('goal', source)
        self.assertNotIn('consciousness', source)
        self.assertEqual(enumerate_space(source)['assignment_count'], 2)


class RelevanceTests(unittest.TestCase):
    def test_unobserved_conditions_remain_unresolved(self):
        result = route_studies(fixture('learning-routes.json'), {})
        self.assertTrue(all(r['status'] == 'unresolved_condition' for r in result['routes']))

    def test_two_routes_can_be_relevant_without_forced_diagnosis(self):
        result = route_studies(fixture('learning-routes.json'), fixture('learning-observations.json'))
        statuses = {r['id']: r['status'] for r in result['routes']}
        self.assertEqual(statuses, {'content': 'unresolved_condition', 'retrieval': 'conditions_met',
                                   'representation': 'unresolved_condition', 'application-condition': 'conditions_met'})

    def test_contradicted_condition_is_retained_with_reason(self):
        observed = fixture('learning-observations.json')
        observed['cued_execution'] = False
        result = route_studies(fixture('learning-routes.json'), observed)
        retrieval = next(r for r in result['routes'] if r['id'] == 'retrieval')
        self.assertEqual(retrieval['status'], 'contradicted_condition')
        self.assertEqual(retrieval['contradicted'], ['cued_execution'])

    def test_numeric_zero_is_not_an_observed_false(self):
        with self.assertRaises(ContractError):
            route_studies(fixture('learning-routes.json'), {'cued_execution': 0})


class ReachabilityTests(unittest.TestCase):
    def test_unknown_path_conditions_are_not_reported_as_established(self):
        result = transition_reachability(fixture('perspective-transitions.json'))
        self.assertEqual(set(result['reachable']), {'transfer-failure', 'cue-comparison', 'application-question'})
        self.assertEqual(set(result['conditional_only']), {'contrast-construction', 'application-condition'})
        self.assertEqual(set(result['no_path_in_declared_graph']), {'missing-operation', 'unavailable-destination'})

    def test_contradictory_unknown_assumptions_do_not_create_a_path(self):
        result = transition_reachability({'states': ['a', 'b', 'c'], 'start': 'a', 'observations': {},
            'transitions': [
                {'id': 'ab', 'from': 'a', 'to': 'b', 'when': {'x': True}, 'operation': 'Require x.'},
                {'id': 'bc', 'from': 'b', 'to': 'c', 'when': {'x': False}, 'operation': 'Require not x.'}]})
        self.assertEqual(result['conditional_only'], ['b'])
        self.assertEqual(result['no_path_in_declared_graph'], ['c'])

    def test_cycles_finish_without_inventing_new_states(self):
        result = transition_reachability({'states': ['a', 'b'], 'start': 'a', 'observations': {},
            'transitions': [
                {'id': 'ab', 'from': 'a', 'to': 'b', 'operation': 'Use the other representation.'},
                {'id': 'ba', 'from': 'b', 'to': 'a', 'operation': 'Return to the original representation.'}]})
        self.assertEqual(result['reachable'], ['a', 'b'])
        self.assertEqual(len(result['paths']), 2)

    def test_undeclared_destination_is_rejected(self):
        graph = fixture('perspective-transitions.json')
        graph['transitions'][0]['to'] = 'not-declared'
        with self.assertRaises(ContractError):
            transition_reachability(graph)


if __name__ == '__main__':
    unittest.main()
