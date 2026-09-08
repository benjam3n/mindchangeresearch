from pathlib import Path
from collections import Counter
import json,hashlib,re,zipfile,datetime

ROOT=Path(__file__).parent
lines=['inquiry','representation','values','conditions','methods','systems']
allocation=json.loads((ROOT/'allocation.json').read_text())['skills']
slots=[]
for line in lines:
    entries=json.loads((ROOT/line/'application-ledger.json').read_text())
    entries={(x['skill_id'],x['application_number']):x for x in entries}
    for s in [s for s in allocation if s['line']==line]:
        for n in range(1,s['applications']+1):
            entry=dict(entries.get((s['id'],n),{'skill_id':s['id'],'application_number':n,'status':'pending','missing_requirements':['No application entry yet']}))
            entry.update({'line':line,'rank':s['rank'],'slot_id':f"{s['id']}-{n:02d}",'integration_review':'not individually certified by root; see review records'})
            f=entry.get('file')
            if f:
                p=Path(f)
                if not p.is_absolute():p=ROOT/p if p.parts[0]==line else ROOT/line/p
                entry['file']=str(p.relative_to(ROOT))
                entry['record_exists']=p.exists()
                if p.exists():entry['record_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
            slots.append(entry)
assert len(slots)==300 and len({x['slot_id'] for x in slots})==300
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
run_state_path=ROOT/'run-state.json'
run_state=json.loads(run_state_path.read_text())
if run_state.get('status')=='ready_for_continuation':
    run_state['base_ledger_updated_utc']=now
    run_state_path.write_text(json.dumps(run_state,indent=2)+'\n')
counts=Counter(x['status'] for x in slots)
post_cycles=[]
for f in sorted(ROOT.glob('post-allocation/cycle-*/cycle-ledger.json')):
    cycle=json.loads(f.read_text())
    cycle['ledger_file']=str(f.relative_to(ROOT))
    post_cycles.append(cycle)
post_attempts=sum(c.get('attempt_counts',{}).get('substantive_records',0) for c in post_cycles)
post_complete=sum(c.get('attempt_counts',{}).get('complete_within_scope',0) for c in post_cycles)
post_partial=sum(c.get('attempt_counts',{}).get('partial',0) for c in post_cycles)
post_distinct=sum(c.get('attempt_counts',{}).get('distinct_new_keep_findings',0) for c in post_cycles)
ledger={'intended_mind_change':'Preserve exact remaining obligations and distinguish recorded attempts from completed original operations.',
 'updated_utc':now,'required_applications':300,'status_counts':dict(counts),'status_basis':'Per-line source-aware execution ledger. These are scoped reported statuses, not independent certification that every semantic edge is valid.',
 'gosm':json.loads((ROOT/'gosm/progress.json').read_text()),'applications':slots,
 'post_allocation_cycles':post_cycles,
 'actual_mind_change':'Missing original requirements survive aggregation instead of disappearing behind a document count; post-allocation applications, distinct findings and later uptake are counted separately.',
 'benefit':'Unperformed human and dependency stages remain retrievable, while continuing inquiry cannot inflate the frozen quota or discovery count.','verdict':'KEEP for this concrete accounting; no discovery credit for ordinary persistence.',
 'organization':'Frozen skill quotas with independent execution, depth, evidence and review fields, followed by separately frozen post-allocation cycles.','next_attempts':['Resume gated original stages only when their inputs exist','Add genuinely diverse prospective cycles','Consolidate only each next group of four distinct findings']}
(ROOT/'Research_Ledger.json').write_text(json.dumps(ledger,indent=2))

mds=list((ROOT/'sources').glob('*.md'));hashes={}
for f in mds:hashes.setdefault(hashlib.sha256(f.read_bytes()).hexdigest(),[]).append(str(f.relative_to(ROOT)))
receipts=[]
for f in (ROOT/'sources').glob('*.txt'):
    t=f.read_text();m=re.search(r'original-source: skills/([^/]+)/SKILL.md',t);h=re.search(r'original-sha256: ([0-9a-f]+)',t)
    if m and h:receipts.append({'skill_id':m.group(1),'requirements':str(f.relative_to(ROOT)),'source_sha256':h.group(1),'matching_emitted_sources':hashes.get(h.group(1),[])})
audit={'scope':'Original reader receipt identities versus preserved emitted byte hashes. Does not certify procedure execution or findings.','receipts':receipts,'selected_skills_without_verified_source':[s['id'] for s in allocation if not any(r['skill_id']==s['id'] and r['matching_emitted_sources'] for r in receipts)]}
(ROOT/'Source_Integrity.json').write_text(json.dumps(audit,indent=2))
byline={line:Counter(x['status'] for x in slots if x['line']==line) for line in lines}
table='\n'.join(['| Line | Complete in stated scope | Partial | Blocked | Pending |','| --- | ---: | ---: | ---: | ---: |']+['| '+line+' | '+' | '.join(str(byline[line][s]) for s in ['complete','partial','blocked','pending'])+' |' for line in lines])
index=f'''Intended mind change: Make this ongoing research usable through its supported findings, exact remaining work and tested selection views.

# Mind change research

Updated {now}. The initial allocation is 150 distinct original Reasoningtool skills, with 50×3 + 50×2 + 50×1 = 300 required applications, plus ten GOSM runs. Every allocated slot now has an application record, but the obligation remains open wherever an original, human, delayed, external, or source-specific stage is partial or blocked.

Current reported initial-application states: **{counts['complete']} complete within their stated scopes, {counts['partial']} partial, {counts['blocked']} blocked, {counts['pending']} pending**. Ten GOSM variants are written: eight Explore and two After, with nine scoped keeps and one rejected benefit claim. GOSM's original has no numerical 8x definition; the records disclose their expanded work. Do not read this as certification that all 300 original 8x procedures are complete.

Post-allocation continuation: **{post_attempts} substantive attempts, {post_complete} complete within scope, {post_partial} partial, and {post_distinct} distinct new KEEP findings after deduplication**. These do not alter the frozen 300-slot counts.

{table}

## Start here

- [Improved research prompt](methods/improved-research-prompt.txt), with original prompt tests in [SP 01](methods/sp-01.md).
- [Full 150-skill assessment](methods/given-01.md), including contextual priority, negative-now candidates and interactions. [allocation.json](allocation.json) preserves the exposure obligation when readiness changes.
- [Research ledger](Research_Ledger.json) records every required slot, its exact file and missing operations. [Source integrity](Source_Integrity.json) checks preserved source bytes separately.
- [First selection consolidation](consolidations/root-01.md) handles timing, location, representation and values. [Second consolidation](consolidations/root-02.md) adds uncertainty, operation order, capability and exact review. [Third consolidation](consolidations/root-03.md) orders state, reachability, sampling measure and utility, and actually uses that order on a changed finite case.
- [Completion audit](continuation/completion-audit.md) checks all 300 slot identities, reflection blocks, source receipts, proposal schemas and remaining gates. Its pre-integration snapshot is preserved; the ledger below is the accepted normalized state.
- [Post-allocation cycle 01 review](post-allocation/cycle-01/integration-review.md) separates twelve scoped KEEPs into seven distinct findings and five reuse/refinement results. Its [cycle ledger](post-allocation/cycle-01/cycle-ledger.json) retains exact dispositions, and [prospective freeze](post-allocation/cycle-01/frozen-inputs.md) prevents retrospective criterion fitting.
- [Transition-gate consolidation](post-allocation/cycle-01/consolidation-01-transition-gates.md) compares source-order retrieval with transition-first selection and uses the latter on a separately frozen mixed case.
- [Post-allocation cycle 02 review](post-allocation/cycle-02/integration-review.md) records nine scoped KEEPs as three distinct findings and six uptake/refinement results, with one SATRDA dependency left partial. Its [ARAW 8x record](post-allocation/cycle-02/belief/03-araw-8x-transition-first.md) rejects the unqualified order-effect universal.
- [Query-to-evidence consolidation](post-allocation/cycle-02/consolidation-02-query-evidence-card.md) combines the three waiting cycle-01 findings with evidence-dependence-before-aggregation and uses the selected card on copied, independent, and missing-lineage cases.
- [Post-allocation cycle 03 review](post-allocation/cycle-03/integration-review.md) records eight attempts as two distinct findings and six applications/refinements, with one physical interface left partial. PERSUA, INSD and SDC meet their actual numerical 8x floors; the other originals have no numerical 8x rule.
- [Transition recipe compiler](post-allocation/cycle-03/consolidation-03-recipe-compiler.md) consolidates the two waiting cycle-02 findings with locus diagnosis and transition-shape verification, then uses the selected arrangement on four fixed cases and two boundaries.
- [Repository synchronization policy](repository-sync.md) makes `mindchangeresearch` part of the accepted checkpoint sequence while keeping persistence distinct from completion.
- The complete archive preserves the individual documents, original sources, receipts, finite cases and continuation files in their relative folders.

## Substantive findings available now

- [Timing](gosm/01-time-and-options.md): waiting for accurate information can lose an expiring option; the constructed case has distinct commit/reserve/wait regions.
- [Location](gosm/02-location-and-observation.md): equally informative locations can reveal different query-relevant features.
- [Representation](gosm/03-representation-and-loss.md): a graph compressed from 28 to seven edges preserves 56 reachability answers but changes 21 distances.
- [Values](gosm/04-motivation-and-plural-values.md): a changed feasible activity set need not imply changed motivation or values.
- [Uncertainty](gosm/06-uncertainty-and-next-query.md): equal confidence about a truth can require opposite next queries.
- [Negative control](gosm/05-trust-and-duplication.md): an 8/8 retrospective routing result does not establish an independently useful trust improvement.
- [Original source correction](inquiry/13-fctl-fault-gates.md): the RCA AND/OR intervention sentence is reversed for its own present-failure semantics; the original is preserved alongside the exact countercase.
- [Information policy](inquiry/51-ht-information-policy.md): for a stated binary prior and cost, the tested policy can reserve, buy information, or act immediately; three changed inputs alter the selected policy without claiming a human purchase.
- [Recovered-source audit](inquiry/10-spd-uncertainty.md): a recovered design-decision source contained 492 actual entries rather than its declared 512; gap filling and question selection were executed before later uncertainty routing.
- [Finite dynamics](methods/mrc-03.md): classifying all 32 states into transient/cycle structure answers million-step queries directly and retains changed-width and constant-state boundaries.
- [Reachability and measure](methods/mtcg-02.md): an exact coefficient witness replaces blind operation search; [MTCG 03](methods/mtcg-03.md) retains different probabilities for token sampling, equal-source sampling and unspecified source priors.
- [Drafting repairs](representation/044-draft-1.md): the quantitative draft now states the common-mixture formula and its boundary; [DRAFT 02](representation/045-draft-2.md) distinguishes prepared-to-send from actually sent and retains the failed event check that forced repair.
- [Utility and option order](methods/uf-01.md): twelve uses, nine failures and all 36 pairwise switches constrain utility-form selection; [BOC 01](methods/boc-01.md) scores all 24 base orders and five changed 24-order cases.
- [Typed two-stage belief transition](post-allocation/cycle-02/belief/03-araw-8x-transition-first.md): select state variable, locus, criterion and admissibility constraints before a technique; let evidence determine belief direction and record downstream action separately. This repairs, rather than repeats, cycle 01's transition-first rule.
- [Evidence dependence](post-allocation/cycle-02/belief/01-pbr-correlated-evidence.md): two HIGH display fields copied from one event yield posterior `4/13`, not `.64`; linking the second field to an independent event changes the decision from inspect to replace.
- [Noncompensatory value navigation](post-allocation/cycle-02/values/01-vcd-privacy-auditability.md): privacy and auditability are handled by separating content, identity, contact route, authority and expiry, not by allowing high audit value to compensate for avoidable sensitive exposure.
- [Semantic merge compatibility](post-allocation/cycle-01/tools-coordination/01-col-semantic-merge-protocol.md): an outcome evaluated under C0 cannot silently become the outcome of a newly accepted C1; all six proposal orders preserved the same result.
- [Lossless retrieval](post-allocation/cycle-01/memory-capability/01-memk-capture.md): two organizations can preserve the same 48/48 fields while requiring eight inspections versus one indexed access. Immediate ACR retrieval is retained separately from unobserved learning.
- [Reversibility and motivation boundaries](post-allocation/cycle-01/time-reversibility/RVA-prospective.md): refundable payment, elapsed time and deadline feasibility are different; [MP](post-allocation/cycle-01/motivation-emotion/01-mp-action-order.md) orders actions from stated constraints without inventing a motivational state.
- [Actual locus before message](post-allocation/cycle-03/recipient/01-persua-locus-before-message.md): identical nonpublication routes to permission when belief is already corrected and back to evidence only when a later belief dispute appears.
- [Transition-shape witnesses](post-allocation/cycle-03/insight/01-insd-transition-shape.md): numeric update, attention narrowing, representation substitution, reindexing, enablement, reorder, value constraint and relocation require different preserved invariants and observations.
- [Constrained efficiency](post-allocation/cycle-03/values/01-ncl-efficiency-subordinate.md): optimize time only inside the supported benefit, harm, autonomy, authority and feasibility boundary; a 10-minute saving loses when severe-harm risk rises to 2% and wins when the increase becomes zero.
- [Recipe capability boundary](post-allocation/cycle-03/capability/01-spg-near-guarantee.md): the vague near-guarantee is rejected; a text-only model emits a handoff rather than claiming physical relocation.

These include constructed calculations and observed source/review operations. They do not establish changed human beliefs, durable human learning, model-weight changes, or a globally optimal organization. A KEEP remains limited to its stated demonstrated consequence. The six lines contain additional findings and negative results; the ledger links the exact records.

## Continuing work

No initial slot is merely unstarted. Resume partial or blocked original operations only when their exact missing input becomes available: human response and transfer observations, semantic-depth certification, external readers or stakeholders, delayed/campaign evidence, missing dependencies, or the blocked LRS campaign-specific source. Preserve those gates rather than substituting model simulations. Continue frozen post-allocation cycles across different mind-change loci. After every four distinct demonstrated keeps, consolidate only established findings, test reuse and a nonapplication boundary, and use the better view. All twelve post-allocation distinct findings are now assigned to three four-finding consolidations; the next consolidation waits for four genuinely new findings. Retain the strong current alternative and the original evidence; do not count repeated prior standards as new discoveries.

The active instruction is [working-instruction.md](working-instruction.md). The user's exact request is preserved unchanged in sources/user-request.txt. The recurring task prompt is automation-prompt.txt. Source originals are preserved evidence rather than rewritten personal skills.

Actual mind change: The working corpus now separates a required exposure, a complete original operation, a scoped useful consequence, a distinct finding and demonstrated later reuse. Before a message, technique, tool or handoff is selected, the recipe compiler now checks admissibility, diagnoses the controlling locus, specifies the transition operator and invariant, and freezes a shape-specific witness. Source, schema, novelty and semantic defects caused actual reclassification and repair.

Benefit: The index exposes useful selection conditions and exact remaining gates while preserving rejected and incomplete outcomes. Cycle 03 prevented an evidence message from being aimed at a permission gate, distinguished unchanged content from changed retrieval, rejected raw KEEP frequency as benefit evidence, and refused to call a plan a physical relocation. Human benefit and measured navigation speed remain unobserved.

Verdict: KEEP for the demonstrated local organization and continuity; no universal optimality claim.

Organization: Use selection views for choosing, the ledger for progress and provenance, and individual records for derivations. Alternative organizations and boundaries remain in consolidation documents.

Next attempts: Resume exact partial gates when their inputs exist; obtain SATRDA's missing clarity dependency; measure timed recipe-compiler versus source-order executions; begin a diverse cycle 04; wait for four genuinely new findings before the next consolidation.
'''
index=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:m.group(0) if '://' in m.group(2) or m.group(2).startswith('sandbox:') else '['+m.group(1)+'](sandbox:'+str((ROOT/m.group(2)).resolve())+')',index)
(ROOT/'Mind_Change_Research_Index.md').write_text(index)
manifest=[]
for f in sorted(ROOT.rglob('*')):
    if not f.is_file() or '__pycache__' in f.parts or any(x in f.parts for x in ['node_modules','.git']) or f.name in {'Mind_Change_Research_Checkpoint.zip','Checkpoint_Manifest.sha256','library-folders.json'}:continue
    manifest.append(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+str(f.relative_to(ROOT)))
(ROOT/'Checkpoint_Manifest.sha256').write_text('\n'.join(manifest)+'\n')
with zipfile.ZipFile(ROOT/'Mind_Change_Research_Checkpoint.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(ROOT.rglob('*')):
        if not f.is_file() or '__pycache__' in f.parts or f.suffix.lower() not in {'.md','.json','.txt','.py','.pptx','.pdf','.png','.svg','.html','.csv','.js','.mjs','.yaml','.yml','.jpg','.jpeg','.webp','.sha256'} or any(x in f.parts for x in ['node_modules','.git']) or f.name in {'library-folders.json'}:continue
        b=f.read_bytes()
        if not b:continue
        if f.suffix=='.json':
            try:json.loads(b)
            except (json.JSONDecodeError,UnicodeDecodeError):continue
        z.writestr(str(f.relative_to(ROOT)),b)
print(json.dumps({'updated_utc':now,'applications':dict(counts),'verified_selected_source_missing':audit['selected_skills_without_verified_source'],'archive_bytes':(ROOT/'Mind_Change_Research_Checkpoint.zip').stat().st_size}))
