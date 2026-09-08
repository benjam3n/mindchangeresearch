from pathlib import Path
import json
b=Path('/workspace/scratch/78b838bd97fc/mind-change-research/values')
alloc=json.loads((b/'allocation.json').read_text())
idx={(r['skill'],r['application']):r for r in json.loads((b/'index.json').read_text())}
missing={
'vcl':['Actual seven-day human audit, unrestricted trade-off choices and personal sacrifice ceilings are unavailable; case/working-role analysis only.'],
've':['Live answers, confirmed circular intrinsic termini, and respondent confirmation that no additional goals remain are unavailable.'],
'pre':['Real-user choices across the scenario pairs are not collected; supplied-task or explicitly stipulated profiles only.'],
'grfr':['No real actor selects a new nontrivial reframe; substituted goals remain proposals and the authorized original is preserved.'],
'mp':['Human energy/motivation and subsequent response to ordering are unobserved; actual scheduling comparisons are scoped to constructed inputs.'],
'ig':['Broader human causal effects are unobserved; required AR 8x is executed, and IG-2 EXD design is complete but its trial is unperformed.'],
'gu':['Required ARAW 8x is executed; live VE answers/circular termini remain absent. Full personally grounded journey is not ready; conditional GJS/EMV route is not executed or claimed.'],
'hf':['Repeated human execution, daily tracking and weekly review are unobserved.'],
'eqi':['Human regulation practice and two-week development outcomes are unobserved; reported emotions are constructed.'],
'al':['Live conversation, confirmation, nonverbal cues and recipient feeling-heard evidence are unavailable.'],
'gdm':['Independent participant submissions, discussion, actual group decision and support commitments are unavailable.'],
'tfac':['No actual group session or participant engagement has occurred; agenda and output design only.'],
'fd':['Live feedback delivery, recipient reply, joint agreement and follow-up are unavailable.'],
'cfr':['Actual dialogue, mutual resolution and subsequent repair are unavailable.'],
'rlg':['Real reciprocal response and /ve elicitation termini are unavailable.']}
rows=[]
for a in alloc:
 for n in range(1,a['applications']+1):
  r=idx.get((a['id'],n));m=missing.get(a['id'],[])
  row={'skill_id':a['id'],'application_number':n,'file':r['file'] if r else None,'status':('partial' if m else 'complete') if r else 'pending','source_fidelity':'Exact original and separate receipt preserved; case-specific products inspectable; missing live stages not reported as observed.' if r else 'Original loaded; application pending','depth_status':r['depth'] if r else 'Pending execution','missing_requirements':m if r else ['Application not yet written.'],'verdict':r['verdict'] if r else None,'novelty':('local_adoption' if r and r['verdict']=='KEEP' else 'repeated' if r and ('repeat' in r['change'].lower() or 'already' in r['change'].lower()) else 'unresolved'),'later_use':r['transfer'] if r else None}
  rows.append(row)
(b/'application-ledger.json').write_text(json.dumps(rows,indent=2))
print({s:sum(r['status']==s for r in rows) for s in ['complete','partial','blocked','pending']})
