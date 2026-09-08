from pathlib import Path
import json,hashlib
ROOT=Path(__file__).parent
data=json.loads((ROOT/'finite-cases.json').read_text())
SOURCE='4224530e1b14958cd0e2921a173c4772406f7673fa561ee8c27dac548e362f4b'
assert hashlib.sha256((ROOT.parent/'sources/root-gosm.md').read_bytes()).hexdigest()==SOURCE

def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(str,row))+' |' for row in rows])

def write(n,slug,title,intent,start,body,change,benefit,verdict,organization,next_attempts,variant='Explore',scope='Finite constructed case; primary assistant working state'):
    path=ROOT/f'{n:02d}-{slug}.md'
    text=f'''Intended mind change: {intent}

# GOSM {n:02d} — {title}

Starting working judgment: {start}

Actor and scope: {scope}. The numerical worlds and utilities below are stipulated inputs. They are not measurements of this user or human psychology. No training-weight change is claimed.

Original procedure: GOSM, source ../sources/root-gosm.md, SHA-256 {SOURCE}. Original reader requirements are preserved separately. Context: NORMAL urgency, LOW immediate experimental stakes with broader design relevance, INTERMEDIATE topic familiarity, CHEAP reversible computation, RICH information inside the declared case and SPARSE information about external transfer. Variant: {variant}. The source defines no numerical 8x floor; this record expands the actual variant through the displayed distinctions, complete finite comparisons, countercases, and a later application. It does not claim an invented 8x certification.

{body.strip()}

Actual mind change: {change}

Benefit: {benefit}

Verdict: {verdict}

Organization: {organization}

Next attempts: {next_attempts}
'''
    path.write_text(text)
    ledger=ROOT/'progress.json'
    current=json.loads(ledger.read_text()) if ledger.exists() else {'required':10,'records':[]}
    current['records']=[x for x in current['records'] if x['id']!=n]+[{'id':n,'file':path.name,'variant':variant,'verdict':verdict,'completed_variant':True,'depth_status':'expanded_original_no_numeric_8x_definition','benefit_scope':scope}]
    current['records'].sort(key=lambda r:r['id'])
    current['completed']=len(current['records'])
    ledger.write_text(json.dumps(current,indent=2))
    return path

if __name__=='__main__':
    rows=[[r['p'],r['values']['commit_now'],r['values']['wait'],r['values']['reserve_and_wait'],', '.join(r['winners'])] for r in data['time']]
    write(1,'time-and-options','Waiting changes the option set',
     'Resolve when a delay for information improves a choice and when preserving an expiring option is the useful change.',
     'The existing standard already treats time as a possible intervention. It does not yet contain the crossover boundaries for this three-option timing case; the best continuation is therefore unresolved.',
     '''The underlying question is which future decisions remain available while information arrives. A change in when a thought occurs can alter its useful consequences even if the eventual conclusion is identical.

Input: at t=0, a guaranteed task pays 5 units. It expires before a test result arrives at t=2. A test costs 1. After the test, a favorable world, with stipulated probability p, offers a task paying 8; an unfavorable world offers 0. A reservation costs a further 1 and preserves the guaranteed task until t=2. Costs are additive, no other tasks exist, the test perfectly identifies the world, and the agent maximizes expected net units. These assumptions define this case, not a factual recommendation about spending money.

The three available policies have values: commit now = 5; test without reservation = 8p−1; reserve and test = 8p+5(1−p)−2 = 3p+3. Without the expiration, testing and retaining the free fallback would instead yield 3p+4. Expiration is therefore doing actual work in the comparison.

'''+table(['p','Commit now','Wait','Reserve and wait','Best'],rows)+'''

The distinctions are information arrival versus option expiry; information value versus reservation value; expected outcome versus realized outcome; time cost versus effort cost; known p versus unknown p; perfectly discriminating versus noisy tests; a protected fallback versus an imagined fallback; and a later belief versus a later feasible policy.

The boundaries follow directly: reservation beats commitment only when p>2/3; unreserved waiting beats reservation when p>4/5. The winning regions are commitment below 2/3, reservation between 2/3 and 4/5, and unreserved waiting above 4/5, with ties at the boundaries. At p=3/4, waiting alone only ties the present value at 5, while reservation yields 5.25. The useful change is the reservation combined with delay.

Position: a timing intervention in this class must be evaluated on the options surviving the delay. The strongest counter is the p=1 world, where the fallback has no value and the reservation wastes a unit. That counter defeats a universal reservation rule; it does not defeat the stated middle interval.

The tension is that more accurate eventual knowledge can accompany a worse available action. The worlds are identical in a model with and without expiry, but an expired action cannot be recovered by thinking more accurately.

Later application: change only the favorable probability from 3/4 to 7/8. The retained timing rule selects unreserved waiting: 6 versus 45/8=5.625 for reservation and 5 for commitment. At 3/4 it selects reservation. The same rule therefore changes the intervention when the input crosses its declared boundary; it does not always recommend delay or always recommend preserving options.

Specific next action: use the surviving-option calculation before scheduling a delayed attempt when a real deadline is supplied. Verify the deadline and costs first; the constructed numbers are not substitutes for them. Open threads: imperfect information, multiple deadlines, unpriced exploration enjoyment, and an unknown p are not settled by this case.''',
     'My working timing model now includes the three exact winning intervals and the protected-option policy; I used it on a distinct probability input.',
     'It resolves which of three policies wins within the declared case and prevents the reservation rule from being applied at p=7/8. External human benefit is unmeasured.',
     'KEEP — scoped finite decision result; not evidence that waiting generally improves cognition.',
     'A table of policy boundaries answers a new p input directly. Chronological prose retains causal context but hides the crossover lookup. Keep the boundary table linked to assumptions; neither representation dominates every use.',
     'Replace perfect information with a noisy test; compare a change of location that changes information arrival; examine a motivation change that alters the value of the guaranteed task.')

    parts=data['location']
    rows=[[name,len(parts[name]),', '.join(str(len(v)) for v in parts[name].values())] for name in ['entrance','west','east','both']]
    write(2,'location-and-observation','A location can change what is distinguishable',
     'Represent a change of location as a change in accessible observations, and determine exactly which uncertainty it resolves.',
     'Location is already in the target space. I have not yet distinguished which of the three hidden features each observation point can reveal in this declared environment.',
     '''The interesting question is whether a spatial change changes the evidence available to the thinker, the interpretation of unchanged evidence, or both. These are different operations.

Input: a constructed environment has three hidden binary features x,y,z and all eight worlds 000 through 111 remain possible. The entrance reveals none. The west observation point reveals x and y. The east point reveals y and z. Visiting both reveals all three. Movement is available and costs one unit per point visited. Observations are exact. No physical person was moved; this is a finite access model.

At the entrance, every world has the same observation. At west, the observation 00 leaves worlds 000 and 001; 01 leaves 010 and 011; 10 leaves 100 and 101; 11 leaves 110 and 111. East groups worlds by the last two bits instead. The full partitions are saved in finite-cases.json.

'''+table(['Access','Distinct observations','Worlds in each class'],rows)+'''

The useful distinctions are a world feature versus its observation; available movement versus a proposed movement; more observations versus the right observations; a place name versus its access relation; identical confidence versus identical possible worlds; one query versus all possible queries; an access improvement versus a measured performance improvement; and a reversible visit versus a location that removes other options.

Position: for the query “what is x?”, west supplies enough evidence and east does not; for “what is z?”, east supplies enough and west does not. Both locations produce four observation classes, so ranking them solely by the number of classes loses the query-relevant difference. At west with observation 00, saying z=0 would still exclude world 001 without evidence.

The strongest counter to changing location is a query about y. Either single visit suffices and visiting both adds a unit of movement without improving that answer. The counter establishes redundant movement for this query, not that location never matters. If the entrance already displayed the entire world, all visits would be informationally redundant; that is a different declared observation relation.

The tension is that two contexts can offer equal information counts yet enable different inferences. A numerical summary of uncertainty cannot replace the mapping from observations to possible worlds.

Later application: for the query x XOR z, west alone leaves both answers possible within every class: 000 and 001 yield 0 and 1. East alone also leaves both answers possible: 000 and 100 yield 0 and 1. Visiting both resolves the query. For the new query y, either one-point policy suffices. I used the same partition representation to distinguish both-point necessity from redundant second movement.

Specific next action: when evaluating a proposed context change, write its actual observation mapping for the target question and test whether answer-disagreeing worlds remain indistinguishable. In real rooms, attention, comfort and interruptions introduce additional effects whose sizes are currently unknown. Open threads: noisy observation, inaccessible locations, social observation, and privacy costs remain open.''',
     'My working representation now records which questions each location can resolve, rather than using a single “more informative” rank. It produced different routes for x XOR z and y.',
     'The later query comparison avoids both an unsupported answer after a one-point visit and an unnecessary second visit for y in this constructed environment. It does not establish a room change improved a human mind.',
     'KEEP — exact information-access result with a demonstrated second use.',
     'Query → observation partition → sufficient locations supports selection; location → visible features supports navigation. Retain both views of one eight-world object. A location-only list required reconstructing the query relationship.',
     'Add noisy observations without changing movement; replace spatial access with social permission; test an attention cue that selects among already visible features.')
