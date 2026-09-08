"""Finite execution kernel. Model-generated perspective proposals enter as data.

The kernel checks execution and declared result requirements. It does not infer
intent, discover adequate criteria, or turn a model's self-rating into evidence.
"""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from math import isfinite, prod

LIMIT = 4096

class ContractError(ValueError):
    pass

def canonical(value):
    try:
        return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
    except (ValueError, TypeError) as exc:
        raise ContractError('Only finite JSON data are admitted.') from exc

def fingerprint(value):
    return sha256(canonical(value).encode()).hexdigest()

def seal(case):
    return fingerprint({k:case[k] for k in ('task','artifacts','evaluation')})

def bounded_rows(value):
    if not isinstance(value,list) or len(value)>LIMIT or any(not isinstance(r,dict) for r in value):
        raise ContractError('Supply at most 4096 explicit row objects.')
    return value

def project_rows(inputs,args):
    rows=bounded_rows(inputs[0]);fields=args['fields']
    if not isinstance(fields,list) or any(not isinstance(k,str) for k in fields) or len(set(fields))!=len(fields):
        raise ContractError('Projection fields must be distinct strings.')
    if any(any(k not in row for k in fields) for row in rows):
        raise ContractError('Projection cannot manufacture a missing field.')
    return [{k:row[k] for k in fields} for row in rows]

def select_rows(inputs,args):
    rows=bounded_rows(inputs[0]);field=args['field'];value=args['equals']
    if any(field not in row for row in rows):raise ContractError('Filter field is missing.')
    return [deepcopy(row) for row in rows if row[field]==value]

def rates(inputs,args):
    rows=bounded_rows(inputs[0]);group_field=args.get('group_field');groups={}
    for row in rows:
        n,d=row[args['numerator']],row[args['denominator']]
        if type(n) not in (int,float) or type(d) not in (int,float) or not isfinite(n) or not isfinite(d) or d<=0 or not 0<=n<=d:
            raise ContractError('Rates require finite counts with 0 <= numerator <= positive denominator.')
        group=row[group_field] if group_field else 'all';option=row[args['option_field']]
        if not isinstance(group,str) or not isinstance(option,str):raise ContractError('Group and option identities must be strings.')
        pair=groups.setdefault(group,{}).setdefault(option,[0,0]);pair[0]+=n;pair[1]+=d
    return {'groups':{g:{k:{'numerator':n,'denominator':d,'rate':n/d} for k,(n,d) in options.items()} for g,options in groups.items()},
            'interpretation':'Descriptive rates within the declared rows; causal attribution is not supplied.'}

def combine_groups(inputs,args):
    result={}
    for value in inputs:
        for key,group in value['groups'].items():
            if key in result and result[key]!=group:raise ContractError('Composition has conflicting group contents.')
            result[key]=deepcopy(group)
    return {'groups':result,'interpretation':'Jointly available descriptive comparisons; grouping assumptions remain explicit.'}

def cartesian_rows(inputs,args):
    domains=inputs[0]
    if not isinstance(domains,dict) or any(not isinstance(k,str) for k in domains):raise ContractError('Domains must be a named object.')
    for values in domains.values():
        if not isinstance(values,list) or any(not isinstance(v,str) for v in values) or len(values)!=len(set(values)):
            raise ContractError('Each finite domain must contain distinct strings.')
    if prod(len(v) for v in domains.values())>LIMIT:raise ContractError('Cartesian domain exceeds 4096 cases.')
    return [dict(zip(domains,values)) for values in product(*domains.values())]

def threshold_gate(inputs,args):
    rows=bounded_rows(inputs[0]);out=[]
    for row in rows:
        matches=[]
        for branch in args['branches']:
            holds=True
            for field,op,value in branch['conditions']:
                if field not in row:raise ContractError('A branch condition lacks its input field.')
                actual=row[field]
                if op=='eq':ok=actual==value
                elif op in ('ge','le','lt','gt'):
                    if type(actual) not in (int,float) or type(value) not in (int,float) or not isfinite(actual) or not isfinite(value):
                        raise ContractError('Ordered comparisons need finite numbers.')
                    ok={'ge':actual>=value,'le':actual<=value,'lt':actual<value,'gt':actual>value}[op]
                else:raise ContractError('Unregistered comparison operation.')
                holds=holds and ok
            if holds:matches.append(branch['label'])
        out.append({'input':deepcopy(row),'matches':matches,'coverage':'missing' if not matches else 'overlap' if len(matches)>1 else 'single'})
    return out

def required_gate(inputs,args):
    rows=bounded_rows(inputs[0]);fields=args['required_fields']
    if not isinstance(fields,list) or not fields or any(not isinstance(k,str) for k in fields) or len(set(fields))!=len(fields):
        raise ContractError('Required fields must be a nonempty distinct string list.')
    out=[]
    for row in rows:
        if any(k not in row or row[k] not in ('true','false','unknown') for k in fields):raise ContractError('Required observations must be true, false or unknown.')
        failed=[k for k in fields if row[k]=='false'];unknown=[k for k in fields if row[k]=='unknown']
        out.append({'input':deepcopy(row),'status':'not_achieved' if failed else 'undetermined' if unknown else 'achieved','failed':failed,'unknown':unknown})
    return out

OPERATIONS={
    'project_rows':(1,1,project_rows), 'select_rows':(1,1,select_rows),
    'rates':(1,1,rates), 'combine_groups':(2,16,combine_groups),
    'cartesian_rows':(1,1,cartesian_rows), 'threshold_gate':(1,1,threshold_gate),
    'required_gate':(1,1,required_gate),
}

def execute(case,candidate):
    if candidate.get('basis')!=seal(case):raise ContractError('Task, evidence or criterion basis changed; construct a separate comparison.')
    if not isinstance(candidate.get('change'),str) or not candidate['change'].strip():raise ContractError('State the particular perspective change.')
    program=candidate.get('program')
    if not isinstance(program,list) or not 1<=len(program)<=32:raise ContractError('A program needs 1 to 32 specified steps.')
    values={'source:'+k:deepcopy(v) for k,v in case['artifacts'].items()};trace=[]
    for step in program:
        identity=step.get('id');op=step.get('op');refs=step.get('inputs');args=step.get('args',{})
        if not isinstance(identity,str) or not identity or identity.startswith('source:') or identity in values:raise ContractError('Step identity is missing, duplicated or reserved.')
        if op not in OPERATIONS:raise ContractError('Operation is not admitted: '+str(op))
        lo,hi,fn=OPERATIONS[op]
        if not isinstance(refs,list) or not lo<=len(refs)<=hi or any(not isinstance(k,str) or k not in values for k in refs):raise ContractError('Inputs must refer to available artifacts with the required arity.')
        if not isinstance(args,dict):raise ContractError('Operation arguments must be a JSON object.')
        try:output=fn([deepcopy(values[k]) for k in refs],args)
        except (KeyError,TypeError,IndexError) as exc:raise ContractError('Operation inputs or parameters do not satisfy its contract.') from exc
        canonical(output);values[identity]=output
        trace.append({'id':identity,'op':op,'input_ids':refs,'input_hashes':[fingerprint(values[k]) for k in refs],'args':deepcopy(args),'output_hash':fingerprint(output)})
    result_id=candidate.get('result')
    if result_id not in values or result_id.startswith('source:'):raise ContractError('Result must refer to a produced artifact.')
    return {'candidate':candidate['id'],'basis':candidate['basis'],'result':values[result_id],'trace':trace,
            'operations_executed':len(program),'result_fingerprint':fingerprint(values[result_id])}

def at(value,path):
    if not isinstance(path,list):raise ContractError('Evaluation paths must be explicit key/index lists.')
    try:
        for key in path:value=value[key]
    except (KeyError,IndexError,TypeError) as exc:raise ContractError('Required result distinction is absent.') from exc
    return value

def assess(result,checks):
    records=[]
    for check in checks:
        kind=check['kind']
        if kind not in ('equals','greater','length'):raise ContractError('Evaluation operation is not specified.')
        try:
            actual=at(result,check['path'])
            if kind=='equals':passed=actual==check['expected']
            elif kind=='greater':
                other=at(result,check['other_path'])
                if type(actual) not in (int,float) or type(other) not in (int,float):raise ContractError('Comparison requires numeric observations.')
                passed=actual>other
            else:passed=len(actual)==check['expected']
            records.append({'id':check['id'],'passed':passed,'actual':actual})
        except (ContractError,TypeError):records.append({'id':check['id'],'passed':False,'reason':'Required result distinction is absent or ill-typed.'})
    return records

def run_case(case):
    canonical(case)
    checks=case['evaluation']['checks'];candidates=case['candidates']
    if not checks or not isinstance(checks,list):raise ContractError('A trial needs actual result checks.')
    ids=[r.get('id') for r in candidates]
    if not ids or any(not isinstance(k,str) or not k for k in ids) or len(ids)!=len(set(ids)):raise ContractError('Candidates need distinct identities.')
    runs=[]
    for candidate in candidates:
        try:
            run=execute(case,candidate);run['checks']=assess(run['result'],checks);run['passes_required']=all(c['passed'] for c in run['checks']);runs.append(run)
        except ContractError as exc:runs.append({'candidate':candidate['id'],'execution_error':str(exc),'passes_required':False})
    eligible=[r for r in runs if r['passes_required']]
    best=[]
    if eligible:
        minimum=min(r['operations_executed'] for r in eligible)
        best=[r['candidate'] for r in eligible if r['operations_executed']==minimum]
    return {'case':case['task']['id'],'basis':seal(case),'runs':runs,'eligible': [r['candidate'] for r in eligible],
            'least_operation_candidates':best,'selection_rule':'Satisfy every declared result check; among these, minimize executed operation count. This count is not a universal cost or quality measure.',
            'standing':'Executed on this declared finite fixture; no held-out LLM capability improvement or global optimum is established.'}

def frontier(rows,objectives,limits=None):
    """Pareto comparison of fully supplied metrics; unknown observations stay open.

    All dimensions retain units and provenance in caller records. A model's own
    estimate is not accepted here as observed performance. No weights are invented.
    """
    if not objectives or any(d not in ('max','min') for d in objectives.values()):raise ContractError('Declare each objective direction.')
    if len(rows)>LIMIT:raise ContractError('Comparison exceeds the finite bound.')
    ids=[r['id'] for r in rows]
    if len(ids)!=len(set(ids)):raise ContractError('Duplicate candidate identity.')
    limits={} if limits is None else limits
    for k,cap in limits.items():
        if k not in objectives or type(cap) not in (int,float) or not isfinite(cap):raise ContractError('Caps must be finite objective values.')
    eligible=[];unresolved=[];excluded=[]
    for row in rows:
        m=row['metrics']
        if row.get('basis') not in ('executed_fixture','stipulated_example','external_observation') or any(k not in m or m[k] is None for k in objectives):
            unresolved.append(row['id']);continue
        if any(type(m[k]) not in (int,float) or not isfinite(m[k]) for k in objectives):raise ContractError('Metrics must be finite numbers or explicit unknowns.')
        if any(m[k]>cap for k,cap in limits.items()):excluded.append(row['id']);continue
        eligible.append(row)
    def dominates(a,b):
        deltas=[(a['metrics'][k]-b['metrics'][k])*(1 if direction=='max' else -1) for k,direction in objectives.items()]
        return all(d>=0 for d in deltas) and any(d>0 for d in deltas)
    pairs=[{'better':a['id'],'worse':b['id']} for a in eligible for b in eligible if a is not b and dominates(a,b)]
    return {'nondominated':[r['id'] for r in eligible if not any(p['worse']==r['id'] for p in pairs)],'dominance':pairs,
            'unresolved':unresolved,'excluded_by_declared_cap':excluded,'comparison_complete':not unresolved,
            'standing':'Relative to supplied candidates, metrics, directions and caps. An undominated candidate need not be a unique best or globally optimal.'}
