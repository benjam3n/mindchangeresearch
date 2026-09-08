from pathlib import Path
from fractions import Fraction
import datetime
import hashlib
import itertools
import json
import sys

BASE = Path(__file__).resolve().parent
FROZEN = BASE / 'systems-handoff-inputs-before.json'
INPUTS = json.loads(FROZEN.read_text())


def read(name):
    return json.loads((BASE / name).read_text())


def save(name, data):
    data['executed_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    data['input_sha256'] = hashlib.sha256(FROZEN.read_bytes()).hexdigest()
    (BASE / name).write_text(json.dumps(data, indent=2) + '\n')


def step(s):
    return ''.join(str(int(s[i]) ^ int(s[(i + 1) % len(s)])) for i in range(len(s)))


def orbit(s):
    seen, states = {}, []
    while s not in seen:
        seen[s] = len(states)
        states.append(s)
        s = step(s)
    return {'states': states, 'transient': seen[s], 'period': len(states) - seen[s], 'repeat': s}


def membership(boxes):
    return [{'box': b['id'], 'low_weight': b['weight'] <= 3, 'light_color': b['color'] == 'white'} for b in boxes]


HYPOTHESES = {
    'red': lambda r, s: r,
    'square': lambda r, s: s,
    'red_and_square': lambda r, s: r and s,
    'red_xor_square': lambda r, s: r != s,
}


def candidates(observations, hs):
    return [h for h in hs if all(HYPOTHESES[h](o['red'], o['square']) == o['output'] for o in observations)]


def orders(jobs):
    rows = []
    for order in itertools.permutations(jobs):
        end, trace = 0, []
        for j in order:
            start = max(end, j['release'])
            end = start + j['duration']
            trace.append({'job': j['id'], 'start': start, 'finish': end, 'deadline': j['deadline'], 'meets': end <= j['deadline']})
        rows.append({'order': [j['id'] for j in order], 'trace': trace, 'feasible': all(t['meets'] for t in trace)})
    return rows


def build():
    first = read('systems-handoff-mrc-01-cases.json')
    save('systems-handoff-mrc-01-products.json', {
        'memberships': membership(INPUTS[0]['input']['boxes']),
        'unconditional_object_membership': first['common_plan'],
        'conditional_plans': first['conditional_routes'],
        'undecided_membership': first['meaning_sensitive_boxes'],
        'selected_organization': 'box membership matrix plus meaning-specific plan',
        'physical_execution': False,
        'meaning_confirmed': False,
        'later_input': [
            {'id': 'E', 'weight': 3, 'color': 'gray'},
            {'id': 'F', 'weight': 4, 'color': 'white'},
            {'id': 'G', 'weight': 3, 'color': 'white'},
            {'id': 'H', 'weight': 4, 'color': 'dark'},
        ],
    })
    first = read('systems-handoff-mrc-02-first.json')
    observations = [dict(INPUTS[1]['input']['already_observed']), {'red': True, 'square': False, 'output': False}]
    before = candidates(observations, first['hypotheses'])
    observations.append({'red': False, 'square': True, 'output': True})
    after = candidates(observations, first['hypotheses'])
    save('systems-handoff-mrc-02-products.json', {
        'hypotheses': first['hypotheses'],
        'truth_table': [{'red': r, 'square': s, **{h: f(r, s) for h, f in HYPOTHESES.items()}} for r, s in itertools.product([False, True], repeat=2)],
        'before_second_query': before,
        'second_query': observations[-1],
        'after_second_query': after,
        'predictions': [{'red': r, 'square': s, 'output': HYPOTHESES[after[0]](r, s)} for r, s in itertools.product([False, True], repeat=2)],
        'selected_organization': 'observation path with surviving hypotheses',
        'query_policy': {'first': [True, False], 'if_first_false': [False, True]},
        'identification_scope': 'stipulated finite hypotheses, noiseless observations; oracle known to author, not a blind experiment',
    })
    first = read('systems-handoff-mrc-03-first.json')
    all_orbits = {format(n, '05b'): orbit(format(n, '05b')) for n in range(32)}
    cycle = first['states'][first['transient_length']:]
    preimages = {format(n, '05b'): [] for n in range(32)}
    for s in all_orbits:
        preimages[step(s)].append(s)
    save('systems-handoff-mrc-03-products.json', {
        'all_32_orbits': all_orbits,
        'nonzero_cycle': cycle,
        'preimages': preimages,
        'classification': {
            'fixed_zero': ['00000'],
            'one_step_to_zero': ['11111'],
            'period_15_no_transient': [s for s, o in all_orbits.items() if o['period'] == 15 and o['transient'] == 0],
            'period_15_one_step_transient': [s for s, o in all_orbits.items() if o['period'] == 15 and o['transient'] == 1],
        },
        'selected_organization': 'transient/cycle map with parity proof; full traces retained',
        'later_queries': [{'seed': '10000', 'time': 1000000}, {'seed': '11111', 'time': 1000000}, {'seed': '01100', 'time': 19}],
        'later_width_countercase': {'seed': '1000', 'width': 4},
    })
    jobs = INPUTS[3]['input']['jobs']
    comparison = orders(jobs)
    save('systems-handoff-mtcg-01-products.json', {
        'all_orders': comparison,
        'selected_order': next(row for row in comparison if row['feasible']),
        'forced_interval': {'job': 'B', 'start': 1, 'finish': 2},
        'preemptive_countercase': [{'job': 'A', 'start': 0, 'finish': 1}, {'job': 'B', 'start': 1, 'finish': 2}, {'job': 'A', 'start': 2, 'finish': 5}],
        'selected_organization': 'forced interval and feasibility conditions plus full timeline',
        'later_cases': [
            {'name': 'A_deadline_5', 'jobs': [{**j, **({'deadline': 5} if j['id'] == 'A' else {})} for j in jobs]},
            {'name': 'A_duration_1', 'jobs': [{**j, **({'duration': 1} if j['id'] == 'A' else {})} for j in jobs]},
        ],
    })
    first = read('systems-handoff-mtcg-02-first.json')
    save('systems-handoff-mtcg-02-products.json', {
        'closed_reachable_set': first['reachable'],
        'controls': INPUTS[4]['input']['controls'],
        'formula': 'delta=(a,a XOR b,b); reachable iff delta[1]=delta[0] XOR delta[2]; a=delta[0], b=delta[2]',
        'coefficient_map': [{'a': a, 'b': b, 'delta': f'{a}{a ^ b}{b}', 'word': 'A' * a + 'B' * b} for a, b in itertools.product([0, 1], repeat=2)],
        'selected_organization': 'control-guarded displacement formula plus four-word map',
        'later_queries': [{'start': '000', 'target': '101'}, {'start': '001', 'target': '111'}, {'start': '110', 'target': '000'}, {'start': '011', 'target': '111'}],
        'changed_control_case': {'start': '000', 'target': '011', 'available_controls': ['A']},
    })
    inp = INPUTS[5]['input']
    a, b = inp['source_A'], inp['source_B']
    natural = Fraction(a['red'], a['red'] + b['red'])
    prior_a = Fraction(a['tokens'], a['tokens'] + b['tokens'])
    likelihood_a, likelihood_b = Fraction(a['red'], a['tokens']), Fraction(b['red'], b['tokens'])
    bayes = prior_a * likelihood_a / (prior_a * likelihood_a + (1-prior_a) * likelihood_b)
    equal_source = likelihood_a / (likelihood_a + likelihood_b)
    save('systems-handoff-mtcg-03-products.json', {
        'sampling': inp['sampling'],
        'frequency_table': [{'source': 'A', **a}, {'source': 'B', **b}],
        'natural_frequency_answer': str(natural),
        'bayes_answer': str(bayes),
        'enumeration_answer': str(Fraction(sum(1 for source in ['A'] * a['red'] + ['B'] * b['red'] if source == 'A'), a['red'] + b['red'])),
        'equal_source_probability_countercase': str(equal_source),
        'selected_organization': 'sampling mechanism then weighted red counts',
        'posterior_by_source_A_prior': {'numerator': '9*p', 'denominator': '2+7*p'},
        'later_queries': [{'p': '1/10', 'sampling': 'uniform combined tokens'}, {'p': '1/2', 'sampling': 'equal probability of source then uniform token within source'}, {'p': None, 'sampling': 'source selection unspecified'}],
    })


def later():
    results = {}
    p = read('systems-handoff-mrc-01-products.json')
    m = membership(p['later_input'])
    results['mrc-01'] = {
        'consumed_file': 'systems-handoff-mrc-01-products.json',
        'later_memberships': m,
        'conditional_plans': {k: [r['box'] for r in m if r[k]] for k in ('low_weight', 'light_color')},
        'shared_members': [r['box'] for r in m if r['low_weight'] and r['light_color']],
        'clarification_received': False,
        'physical_execution': False,
        'all_eight_membership_facts_preserved_by_selected_matrix': len(m) * 2,
    }
    p = read('systems-handoff-mrc-02-products.json')
    runs = []
    for oracle in ('square', 'red_and_square', 'red_or_square'):
        f = HYPOTHESES.get(oracle, lambda r, s: r or s)
        observations = [{'red': True, 'square': True, 'output': True}]
        r, s = p['query_policy']['first']
        answer = f(r, s)
        observations.append({'red': r, 'square': s, 'output': answer})
        survivors = candidates(observations, p['hypotheses'])
        if len(survivors) > 1:
            r, s = p['query_policy']['if_first_false']
            observations.append({'red': r, 'square': s, 'output': f(r, s)})
            survivors = candidates(observations, p['hypotheses'])
        before_holdout = survivors[:]
        # This extra query tests the fixed-hypothesis boundary; it is not needed to distinguish surviving in-set rules.
        holdout = {'red': False, 'square': True, 'output': f(False, True)}
        after_holdout = candidates(observations + [holdout], p['hypotheses'])
        runs.append({'oracle': oracle, 'observations': observations, 'identified_in_set': before_holdout, 'holdout': holdout, 'after_holdout': after_holdout})
    results['mrc-02'] = {'consumed_file': 'systems-handoff-mrc-02-products.json', 'runs': runs, 'human_observations': False}
    p = read('systems-handoff-mrc-03-products.json')
    answers = []
    for q in p['later_queries']:
        o = p['all_32_orbits'][q['seed']]
        index = q['time'] if q['time'] < len(o['states']) else o['transient'] + (q['time'] - o['transient']) % o['period']
        answers.append({**q, 'index_after_cycle_reduction': index, 'answer': o['states'][index], 'period': o['period'], 'transient': o['transient']})
    results['mrc-03'] = {
        'consumed_file': 'systems-handoff-mrc-03-products.json',
        'answers': answers,
        'width_4_countercase': orbit(p['later_width_countercase']['seed']),
        'period_5_seed_exists_in_5_cells': any(o['period'] == 5 for o in p['all_32_orbits'].values()),
    }
    p = read('systems-handoff-mtcg-01-products.json')
    results['mtcg-01'] = {'consumed_file': 'systems-handoff-mtcg-01-products.json', 'changed_cases': [{'name': c['name'], 'all_orders': orders(c['jobs'])} for c in p['later_cases']], 'real_jobs_scheduled': False}
    p = read('systems-handoff-mtcg-02-products.json')
    answers = []
    for q in p['later_queries']:
        d = [int(a) ^ int(b) for a, b in zip(q['start'], q['target'])]
        feasible = d[1] == d[0] ^ d[2]
        word = 'A' * d[0] + 'B' * d[2] if feasible else None
        actual = int(q['start'], 2)
        if word is not None:
            for action in word:
                actual ^= int(p['controls'][action], 2)
        answers.append({**q, 'delta': ''.join(map(str, d)), 'feasible': feasible, 'word': word, 'executed_end': format(actual, '03b') if word is not None else None})
    changed = p['changed_control_case']
    changed_reachable = [changed['start'], format(int(changed['start'], 2) ^ int(p['controls']['A'], 2), '03b')]
    results['mtcg-02'] = {
        'consumed_file': 'systems-handoff-mtcg-02-products.json',
        'queries': answers,
        'changed_controls': {**changed, 'two_control_formula_applicable': False, 'sole_control_reachable': changed_reachable, 'target_reachable': changed['target'] in changed_reachable},
    }
    p = read('systems-handoff-mtcg-03-products.json')
    answers = []
    for q in p['later_queries']:
        prior = Fraction(q['p']) if q['p'] is not None else None
        answer = str(9 * prior / (2 + 7 * prior)) if prior is not None else 'UNRESOLVED: source-selection prior missing'
        answers.append({**q, 'answer': answer})
    results['mtcg-03'] = {'consumed_file': 'systems-handoff-mtcg-03-products.json', 'later_answers': answers, 'original_answer_changed': False, 'empirical_calibration': False}
    save('systems-handoff-later-use-results.json', results)
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    {'build': build, 'later': later}[sys.argv[1]]()
