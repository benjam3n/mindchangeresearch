"""Exact finite constructions accompanying findings/. Run with Python 3.

These computations check the stated models, not human persuasion or the
empirical adequacy of a caller's model. No third-party packages are needed.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path


def adequate_policy(states, adequate, questions):
    """Minimum worst-case question cost, given finite truthful observations.

    questions = {name: {'cost': positive number, 'outcomes': {state: answer}}}.
    Returns an adequate action, a branching policy, or an unresolved witness.
    """
    states = tuple(sorted(states))
    if not states:
        raise ValueError('At least one situation is required')
    for name, question in questions.items():
        if F(question['cost']) <= 0:
            raise ValueError('Question costs must be positive')
        if not set(states) <= question['outcomes'].keys():
            raise ValueError(f'Missing outcomes for {name}')

    @lru_cache(None)
    def solve(current):
        common = set.intersection(*(set(adequate[s]) for s in current))
        if common:
            return {'kind': 'action', 'action': sorted(common)[0], 'cost': F(0)}
        candidates = []
        for name, question in questions.items():
            parts = {}
            for state in current:
                parts.setdefault(question['outcomes'][state], []).append(state)
            if len(parts) == 1:
                continue
            branches = {answer: solve(tuple(part)) for answer, part in parts.items()}
            if any(child['kind'] == 'unresolved' for child in branches.values()):
                continue
            cost = F(question['cost']) + max(c['cost'] for c in branches.values())
            candidates.append({'kind': 'question', 'question': name, 'cost': cost,
                               'branches': branches})
        if candidates:
            return min(candidates, key=lambda p: (p['cost'], p['question']))
        return {'kind': 'unresolved', 'states': list(current), 'common_actions': [],
                'reason': 'No available question has adequate continuations for every answer'}
    return solve(states)


def execute_policy(policy, state, questions):
    while policy['kind'] == 'question':
        answer = questions[policy['question']]['outcomes'][state]
        policy = policy['branches'][answer]
    return policy.get('action')


def signal_minimax(p, alpha, cost):
    """Exact minimax regret among all mixtures of the six binary policies."""
    p, alpha, cost = map(F, (p, alpha, cost))
    if not (0 <= p <= 1 and 0 <= alpha <= 1 and cost >= 0):
        raise ValueError('Require probabilities in [0,1] and nonnegative cost')
    lo, hi = max(F(0), p+alpha-1), min(p, alpha)
    def payoffs(t):
        return {'immediate': 10*p-4, 'decline': F(0),
                'positive': 2*t+4*p+4*alpha-4-cost,
                'negative': 6*p-2*t-4*alpha-cost,
                'both': 10*p-4-cost, 'neither': -cost}
    endpoints = [payoffs(lo), payoffs(hi)]
    best = [max(v.values()) for v in endpoints]
    names = list(endpoints[0])
    regrets = {name: tuple(best[k]-endpoints[k][name] for k in range(2))
               for name in names}
    candidates = [(max(regrets[name]), {name: F(1)}) for name in names]
    for a, b in combinations(names, 2):
        ra, rb = regrets[a], regrets[b]
        denominator = (ra[0]-rb[0])-(ra[1]-rb[1])
        if denominator:
            weight = (rb[1]-rb[0])/denominator
            if 0 < weight < 1:
                value = max(weight*ra[k]+(1-weight)*rb[k] for k in range(2))
                candidates.append((value, {a: weight, b: 1-weight}))
    optimum = min(value for value, _ in candidates)
    return {'t_interval': [lo, hi], 'endpoint_payoffs': endpoints,
            'endpoint_regrets': regrets, 'worst_regret': optimum,
            'optimal_candidates': [mix for value, mix in candidates if value == optimum]}


def minimal_repairs(faults, fails):
    """All inclusion-minimal removals that repair an explicit Boolean model."""
    faults = set(faults)
    result = []
    for size in range(len(faults)+1):
        for chosen in combinations(sorted(faults), size):
            chosen = set(chosen)
            if not any(previous <= chosen for previous in result) and not fails(faults-chosen):
                result.append(chosen)
    return [sorted(r) for r in result]


def representation_collisions(objects, encode, answer):
    """Witnesses to failure of exact answer recovery from a representation."""
    fibers, collisions = {}, []
    for obj in objects:
        key, value = encode(obj), answer(obj)
        if key in fibers and fibers[key][1] != value:
            collisions.append([fibers[key][0], obj])
        else:
            fibers[key] = (obj, value)
    return collisions


def xor_step(state, width):
    mask = (1 << width)-1
    rotated = (state >> 1) | ((state & 1) << (width-1))
    return state ^ rotated


def xor_orbit(seed, width):
    seen, sequence = {}, []
    state = seed
    while state not in seen:
        seen[state] = len(sequence)
        sequence.append(state)
        state = xor_step(state, width)
    return {'zero_reached': 0 in seen, 'first_zero': seen.get(0),
            'period': len(sequence)-seen[state], 'cycle': sequence[seen[state]:]}


def atomic_edit(records, delete_id, target_id, expected_text, tag):
    """Validate all operands before constructing a changed result.

    This is atomic within the supplied immutable snapshot; a real shared
    store still needs a transactional compare-and-swap at commit time.
    """
    matches = lambda ident: [r for r in records if r['id'] == ident]
    if delete_id == target_id or len(matches(delete_id)) != 1 or len(matches(target_id)) != 1:
        return {'applied': False, 'records': records, 'reason': 'Ambiguous or conflicting identity'}
    if matches(target_id)[0]['text'] != expected_text:
        return {'applied': False, 'records': records, 'reason': 'Content precondition failed'}
    edited = []
    for record in records:
        if record['id'] == delete_id:
            continue
        copy = dict(record)
        if copy['id'] == target_id:
            copy['tag'] = tag
        edited.append(copy)
    return {'applied': True, 'records': edited}


def apply_timer_event(state, event, delay=5):
    """Round-indexed deadlines; no cross-round cancellation."""
    new = dict(state)
    kind, round_id, time = event
    if kind == 'READY':
        new.setdefault(round_id, time+delay)
    elif kind == 'CANCEL':
        new.pop(round_id, None)
    else:
        raise ValueError('Unknown event')
    return new


def cheapest_xor_word(controls, costs, displacement):
    if any(cost < 0 for cost in costs):
        raise ValueError('Subset reduction requires nonnegative costs')
    candidates = []
    for bits in range(1 << len(controls)):
        result, cost, word = 0, 0, []
        for i, control in enumerate(controls):
            if bits & (1 << i):
                result ^= control
                cost += costs[i]
                word.append(i)
        if result == displacement:
            candidates.append((cost, word))
    return min(candidates) if candidates else None


def model_variation_examples():
    posterior = lambda u, v: u/(u+9*v)
    corners = [posterior(u,v) for u in (F(3,5), F(4,5)) for v in (F(0), F(1,5))]
    assert (min(corners), max(corners)) == (F(1,4), F(1))
    partial_copy = []
    for lam in (F(0), F(7,32), F(1)):
        u, v = (16+4*lam)/25, (1+4*lam)/25
        value = posterior(u,v)
        assert value == (16+4*lam)/(25+40*lam)
        partial_copy.append({'copy_probability': lam, 'posterior': value})
    assert partial_copy[1]['posterior'] == F(1,2)
    controls = []
    for c in range(8):
        reached = [d for d in range(8) if cheapest_xor_word([6,3,c], [1,1,1], d) is not None]
        assert (len(reached) == 8) == (c.bit_count() % 2 == 1)
        controls.append({'third_control': format(c, '03b'), 'reachable_displacements': reached})
    expensive = cheapest_xor_word([6,3,5], [1,1,3], 5)
    cheap = cheapest_xor_word([6,3,5], [1,1,1], 5)
    assert expensive == (2, [0,1]) and cheap == (1, [2])
    return {'alarm_posterior_range': [min(corners), max(corners)], 'partial_copy': partial_copy,
            'third_control_cases': controls, 'unequal_cost_witnesses': [expensive, cheap],
            'machine': {'21_minute_duration_finish': '09:36', 'latest_start': '09:19',
                        '18_minute_report_plus_3_setup_plus_20_work': 18+3+20,
                        'reserve_fee_break_even': 10-F(2,5)*10,
                        'failure_penalty_break_even': F(4)/F(2,5)}}


def completed_examples():
    adequate = {'s1': {'a', 'b'}, 's2': {'b', 'c'}, 's3': {'a', 'c'}}
    assert all(adequate[a] & adequate[b] for a, b in combinations(adequate, 2))
    unresolved = adequate_policy(adequate, adequate, {})
    assert unresolved['kind'] == 'unresolved'
    questions = {'is_s1': {'cost': 1, 'outcomes': {'s1': 'yes', 's2': 'no', 's3': 'no'}},
                 'full_identity': {'cost': 3, 'outcomes': {s: s for s in adequate}}}
    policy = adequate_policy(adequate, adequate, questions)
    assert policy['cost'] == 1
    for state in adequate:
        assert execute_policy(policy, state, questions) in adequate[state]
    common = adequate_policy(['u', 'v'], {'u': {'a'}, 'v': {'a', 'b'}}, {})
    assert common['action'] == 'a' and common['cost'] == 0

    signal = {str(alpha): signal_minimax(F(1,2), alpha, 1)
              for alpha in (F(4,5), F(1,5), F(0))}
    assert signal['4/5']['worst_regret'] == F(1,10)
    assert {'immediate': F(1,2), 'positive': F(1,2)} in signal['4/5']['optimal_candidates']
    assert {'immediate': F(1,2), 'negative': F(1,2)} in signal['1/5']['optimal_candidates']
    assert signal['0']['optimal_candidates'] == [{'negative': F(1)}]
    # Independently calculate the four state/signal cells and conditional payoffs.
    matrices_checked = 0
    for p in (F(0), F(1,4), F(1,2), F(3,4), F(1)):
        for alpha in (F(0), F(1,5), F(1,2), F(4,5), F(1)):
            result = signal_minimax(p, alpha, F(1,3))
            for t in result['t_interval']:
                gp, gn, bp, bn = t, p-t, 1-p-alpha+t, alpha-t
                assert min(gp, gn, bp, bn) >= 0 and gp+gn+bp+bn == 1
                formula = result['endpoint_payoffs'][0 if t == result['t_interval'][0] else 1]
                assert formula['positive'] == 6*gp-4*bp-F(1,3)
                assert formula['negative'] == 6*gn-4*bn-F(1,3)
                matrices_checked += 1

    repairs = minimal_repairs({'a', 'b', 'c'}, lambda f: 'a' in f and bool({'b','c'} & f))
    assert repairs == [['a'], ['b', 'c']]
    graph = []
    for n in range(2, 13):
        changed = sum(1 for i in range(n) for j in range(i+1, n) if j-i != 1)
        assert changed == (n-1)*(n-2)//2
        graph.append({'vertices': n, 'reachable_ordered_pairs': n*(n-1)//2,
                      'changed_distances_after_edge_reduction': changed})
    collisions = representation_collisions(['complete', 'chain'], lambda _: 'same reachability',
                                           lambda name: 1 if name == 'complete' else 7)
    assert collisions == [['complete', 'chain']]

    schedules = []
    for sigma in (F(0), F(1,4), F(1,2), F(3,4)):
        completion = 6+2*sigma
        feasible = completion <= 7
        intervals = [['A', 0, 1-sigma], ['switch', 1-sigma, 1],
                     ['B', 1, 3], ['switch', 3, 3+sigma], ['A', 3+sigma, completion]]
        assert sum(F(end)-F(start) for name,start,end in intervals if name == 'A') == 4
        assert intervals[2][2]-intervals[2][1] == 2
        assert all(end >= start for _,start,end in intervals)
        assert all(intervals[i][2] == intervals[i+1][1] for i in range(len(intervals)-1))
        schedules.append({'switch_cost': sigma, 'schedule': intervals, 'feasible': feasible,
                          'necessary_time_bound': completion})
    assert [r['feasible'] for r in schedules] == [True, True, True, False]

    xor = []
    for width in range(1, 9):
        orbits = [xor_orbit(seed, width) for seed in range(1 << width)]
        universal = all(o['zero_reached'] for o in orbits)
        assert universal == (width & (width-1) == 0)
        if universal:
            assert max(o['first_zero'] for o in orbits) == width
            assert xor_orbit(1, width)['first_zero'] == width
        witness = next(((seed, o) for seed, o in enumerate(orbits) if not o['zero_reached']), None)
        xor.append({'width': width, 'seeds_checked': len(orbits), 'all_extinct': universal,
                    'nonextinct_witness': witness})

    records = [{'id':'A','text':'alpha'}, {'id':'B','text':'beta'}, {'id':'C','text':'gamma'}]
    correct = atomic_edit(records, 'A', 'B', 'beta', 'chosen')
    changed_order = atomic_edit(list(reversed(records)), 'A', 'B', 'beta', 'chosen')
    failed = atomic_edit(records, 'A', 'B', 'wrong', 'chosen')
    assert correct['applied'] and failed['records'] == records and not failed['applied']
    assert all(r.get('tag') == 'chosen' for r in changed_order['records'] if r['id'] == 'B')
    assert records == [{'id':'A','text':'alpha'}, {'id':'B','text':'beta'}, {'id':'C','text':'gamma'}]
    state, trace = {}, []
    for event in [('READY','A',3), ('READY','B',4), ('CANCEL','A',5), ('READY','A',10)]:
        state = apply_timer_event(state, event)
        trace.append({'event': event, 'deadlines': state})
    assert trace[2]['deadlines'] == {'B': 9} and state == {'A': 15, 'B': 9}
    assert apply_timer_event({'A': 8}, ('READY', 'A', 4)) == {'A': 8}
    ab = apply_timer_event(apply_timer_event({}, ('READY','A',3)), ('READY','B',4))
    ba = apply_timer_event(apply_timer_event({}, ('READY','B',4)), ('READY','A',3))
    assert ab == ba
    return {'scope': 'Exact finite model checks; not human outcomes or whole-recipe reliability',
            'selection': {'unresolved': unresolved, 'minimum_cost_policy': policy, 'common_action': common},
            'signal': signal, 'independent_signal_matrices_checked': matrices_checked,
            'minimal_repairs': repairs, 'graph_reduction': graph, 'representation_collision': collisions,
            'switching_cost_schedules': schedules, 'xor': xor,
            'atomic_edit': {'success': correct, 'reordered': changed_order, 'failed': failed},
            'timer_trace': trace}


if __name__ == '__main__':
    result = completed_examples()
    result['model_variations'] = model_variation_examples()
    destination = Path(__file__).resolve().parents[1]/'revision'/'deduction-results.json'
    destination.write_text(json.dumps(result, indent=2, default=str)+'\n')
    print('Completed finite checks; results written to '+str(destination))
