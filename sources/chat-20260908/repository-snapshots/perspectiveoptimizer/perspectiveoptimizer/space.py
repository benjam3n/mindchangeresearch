"""Perspective construction operations."""
from collections import deque
from copy import deepcopy
from itertools import product
from math import prod

from .core import ContractError, LIMIT, canonical, fingerprint


def require_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ContractError(label + ' must be nonempty text.')


def value_records(values):
    if not isinstance(values, list) or not values:
        raise ContractError('A dimension requires explicit values.')
    identities = []
    for value in values:
        if not isinstance(value, dict):
            raise ContractError('A value requires an identity and definition.')
        for key in ('id', 'description', 'contribution'):
            require_text(value.get(key), 'Value ' + key)
        identities.append(value['id'])
    if len(identities) != len(set(identities)):
        raise ContractError('Dimension value identities must be distinct.')
    return identities


def validate_space(space):
    canonical(space)
    if not isinstance(space, dict):
        raise ContractError('Supply a construction space object.')
    for key in ('id', 'matter', 'scope'):
        require_text(space.get(key), 'Space ' + key)
    dimensions = space.get('dimensions')
    if not isinstance(dimensions, dict) or not dimensions:
        raise ContractError('Declare the dimensions of this finite construction.')
    domains = {}
    for name, values in dimensions.items():
        require_text(name, 'Dimension identity')
        domains[name] = value_records(values)
    count = prod(len(values) for values in domains.values())
    if count > LIMIT:
        raise ContractError('The declared space exceeds the finite execution bound; no truncated result is returned.')
    rules = space.get('incompatibilities', [])
    if not isinstance(rules, list):
        raise ContractError('Incompatibilities must be an explicit list.')
    seen = set()
    for rule in rules:
        if not isinstance(rule, dict):
            raise ContractError('An incompatibility requires an object.')
        for key in ('id', 'reason'):
            require_text(rule.get(key), 'Incompatibility ' + key)
        if rule['id'] in seen:
            raise ContractError('Incompatibility identities must be distinct.')
        seen.add(rule['id'])
        when = rule.get('when')
        if not isinstance(when, dict) or not when:
            raise ContractError('An incompatibility requires explicit assignment conditions.')
        for name, value in when.items():
            if name not in domains or value not in domains[name]:
                raise ContractError('An incompatibility refers to an undeclared dimension or value.')
    return domains, count


def enumerate_space(space):
    domains, count = validate_space(space)
    choices = {key: {v['id']: v for v in values} for key, values in space['dimensions'].items()}
    records = []
    for values in product(*domains.values()):
        assignment = dict(zip(domains, values))
        exclusions = [dict(id=r['id'], reason=r['reason']) for r in space.get('incompatibilities', [])
                      if all(assignment[key] == value for key, value in r['when'].items())]
        records.append({'id': fingerprint(assignment), 'assignment': assignment,
                        'contributions': {key: deepcopy(choices[key][value]) for key, value in assignment.items()},
                        'status': 'excluded_under_declared_rule' if exclusions else 'open_candidate',
                        'exclusions': exclusions})
    return {'space': space['id'], 'basis': fingerprint(space), 'assignment_count': count,
            'open_count': sum(r['status'] == 'open_candidate' for r in records), 'candidates': records,
            'coverage': 'Every assignment in these declared finite dimensions; excluded assignments are retained with reasons.',
            'semantic_standing': 'Open candidates require semantic examination. No universal completeness or optimality follows.'}


def expand_space(space, extension):
    validate_space(space)
    canonical(extension)
    if not isinstance(extension, dict):
        raise ContractError('Supply an explicit extension object.')
    witness = extension.get('contrast')
    if not isinstance(witness, dict):
        raise ContractError('An extension needs a consequential contrast.')
    for key in ('old_case', 'new_case', 'consequential_difference'):
        require_text(witness.get(key), 'Contrast ' + key)
    if witness['old_case'] == witness['new_case']:
        raise ContractError('The recorded contrast must distinguish its cases.')
    dimension = extension.get('dimension')
    require_text(dimension, 'Extension dimension')
    revised = deepcopy(space)
    if extension.get('kind') == 'add_value':
        if dimension not in revised['dimensions']:
            raise ContractError('Add-value requires an existing dimension.')
        value = extension.get('value')
        value_records([value])
        revised['dimensions'][dimension].append(deepcopy(value))
    elif extension.get('kind') == 'add_dimension':
        if dimension in revised['dimensions']:
            raise ContractError('Add-dimension requires a new dimension identity.')
        value_records(extension.get('values'))
        revised['dimensions'][dimension] = deepcopy(extension['values'])
    else:
        raise ContractError('Specify add_value or add_dimension.')
    revised.setdefault('construction_history', []).append({'operation': extension['kind'],
        'basis': fingerprint(space), 'dimension': dimension, 'contrast': deepcopy(witness),
        'standing': 'Authored expansion; the structural operation does not establish semantic novelty.'})
    before = validate_space(space)[1]
    after = validate_space(revised)[1]
    return {'before_count': before, 'after_count': after, 'space': revised, 'enumeration': enumerate_space(revised)}


def observations_map(observations):
    if not isinstance(observations, dict):
        raise ContractError('Observations must be a named object.')
    for key, value in observations.items():
        require_text(key, 'Observation identity')
        if type(value) is not bool and value != 'unknown':
            raise ContractError('Observations must be true, false or the explicit string unknown.')
    return observations


def requirements_map(requirements):
    if not isinstance(requirements, dict):
        raise ContractError('Requirements must be a named object.')
    for key, value in requirements.items():
        require_text(key, 'Requirement identity')
        if type(value) is not bool:
            raise ContractError('A requirement must specify a true or false observation.')
    return requirements


def condition_status(requirements, observations):
    requirements_map(requirements)
    missing = [key for key in requirements if observations.get(key, 'unknown') == 'unknown']
    contradicted = [key for key, value in requirements.items()
                   if observations.get(key, 'unknown') != 'unknown' and observations[key] != value]
    return missing, contradicted


def route_studies(specification, observations):
    observations_map(observations)
    canonical(specification)
    if not isinstance(specification, dict):
        raise ContractError('Supply a contribution-route specification.')
    routes = specification.get('routes')
    if not isinstance(routes, list) or not routes or len(routes) > LIMIT:
        raise ContractError('Supply a bounded nonempty list of contribution routes.')
    seen = set()
    results = []
    for route in routes:
        if not isinstance(route, dict):
            raise ContractError('Each route is an object.')
        for key in ('id', 'perspective', 'contribution', 'operation', 'end_condition'):
            require_text(route.get(key), 'Route ' + key)
        if route['id'] in seen:
            raise ContractError('Route identities must be distinct.')
        seen.add(route['id'])
        subjects = route.get('subjects')
        if not isinstance(subjects, list) or not subjects or any(not isinstance(s, str) or not s for s in subjects):
            raise ContractError('A route requires explicit subject identities.')
        missing, contradicted = condition_status(route.get('when'), observations)
        status = 'contradicted_condition' if contradicted else 'unresolved_condition' if missing else 'conditions_met'
        results.append({**deepcopy(route), 'status': status, 'unresolved': missing, 'contradicted': contradicted})
    return {'routes': results, 'observations': deepcopy(observations),
            'standing': 'Conditional relevance under authored rules; multiple routes may apply. This is not a diagnosis or proof of remedy effectiveness.'}


def transition_reachability(graph):
    canonical(graph)
    if not isinstance(graph, dict):
        raise ContractError('Supply a transition graph.')
    nodes = graph.get('states')
    if not isinstance(nodes, list) or not nodes or any(not isinstance(n, str) or not n for n in nodes):
        raise ContractError('Declare nonempty state identities.')
    if len(nodes) != len(set(nodes)) or len(nodes) > LIMIT:
        raise ContractError('State identities must be distinct and bounded.')
    start = graph.get('start')
    if start not in nodes:
        raise ContractError('The initial state must be declared.')
    observations = observations_map(graph.get('observations', {}))
    edges = graph.get('transitions')
    if not isinstance(edges, list) or len(edges) > LIMIT:
        raise ContractError('Declare bounded transition operations.')
    outgoing = {n: [] for n in nodes}
    seen_edges = set()
    for edge in edges:
        if not isinstance(edge, dict):
            raise ContractError('A transition requires an object.')
        for key in ('id', 'operation'):
            require_text(edge.get(key), 'Transition ' + key)
        if edge['id'] in seen_edges or edge.get('from') not in nodes or edge.get('to') not in nodes:
            raise ContractError('Transitions need distinct identities and declared endpoints.')
        seen_edges.add(edge['id'])
        requirements_map(edge.get('when', {}))
        outgoing[edge['from']].append(edge)
    queue = deque([(start, {}, [])])
    visited = {(start, canonical({}))}
    paths = []
    while queue:
        state, assumptions, path = queue.popleft()
        paths.append({'state': state, 'path': path, 'requires_observations': assumptions,
                      'status': 'conditional' if assumptions else 'reachable_under_declared_conditions'})
        for edge in outgoing[state]:
            requirements = edge.get('when', {})
            missing, contradicted = condition_status(requirements, observations)
            if contradicted:
                continue
            revised = dict(assumptions)
            consistent = True
            for key in missing:
                if key in revised and revised[key] != requirements[key]:
                    consistent = False
                    break
                revised[key] = requirements[key]
            if not consistent:
                continue
            key = (edge['to'], canonical(revised))
            if key in visited:
                continue
            if len(visited) >= LIMIT:
                raise ContractError('Conditional reachability exceeds the finite bound; no incomplete result is labeled complete.')
            visited.add(key)
            queue.append((edge['to'], revised, path + [edge['id']]))
    certain = {p['state'] for p in paths if not p['requires_observations']}
    possible = {p['state'] for p in paths}
    return {'start': start, 'reachable': sorted(certain), 'conditional_only': sorted(possible - certain),
            'no_path_in_declared_graph': sorted(set(nodes) - possible), 'paths': paths,
            'standing': 'Reachability in the supplied graph with fixed observation meanings. Conditions do not change along an edge; real execution and unknown operations are outside this result.'}
