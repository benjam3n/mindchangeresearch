from pathlib import Path
import json,re,datetime
from write_records import ROOT,put
ledger_py=ROOT/'update_ledger.py'
s=ledger_py.read_text()
s=s.replace(" 'rso-03':['Status mutation changed, but the selected value-stream throughput and cycle time were not separately measured.'],\n",'')
s=s.replace("'memy-03'}", "'memy-03','enough-01','pt-02'}")
s=s.replace("'rso-03','ecal-02'}", "'rso-03','ecal-02','enough-02','pt-01'}")
ledger_py.write_text(s)
old=json.loads((ROOT/'progress.json').read_text())
(ROOT/'progress-before-correction.json').write_text(json.dumps(old,indent=2)+'\n')
p=ROOT/'write_records.py';s=p.read_text();start=s.index('def refresh():');end=s.index("if __name__",start)
s=s[:start]+'''def refresh():
 import subprocess,sys
 subprocess.run([sys.executable,str(ROOT/'update_ledger.py')],check=True,capture_output=True,text=True)
 ledger=json.loads((ROOT/'application-ledger.json').read_text())
 ids=lambda status:[f"{r['skill_id']}-{r['application_number']:02d}" for r in ledger if r['status']==status]
 records=[f"{r['skill_id']}-{r['application_number']:02d}" for r in ledger if r['status']!='pending']
 keeps=[f"{r['skill_id']}-{r['application_number']:02d}" for r in ledger if r['verdict']=='KEEP']
 consolidations=sorted(p.stem for p in ROOT.glob('consolidation-*.md'))
 counts={k:len(ids(k)) for k in ['complete','partial','blocked','pending']}
 prog={'line':'conditions','actor':'conditions subagent','allocated_applications':50,'recorded_applications':records,'completed_applications':ids('complete'),'partial_applications':ids('partial'),'blocked_applications':ids('blocked'),'pending_applications':ids('pending'),'execution_counts':counts,'keeps':keeps,'consolidations':consolidations,'status':'available_work_addressed' if not ids('pending') else 'executing','updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'completion_meaning':'Completed means original application operations executed within the declared agent/design scope. Partial and blocked procedures are separate. A verdict or a written design is not proof of human effect, delayed retention, or durable agent learning.'}
 (ROOT/'progress.json').write_text(json.dumps(prog,indent=2)+'\\n')
 print(f"{len(records)}/50 recorded; execution={counts}; {len(keeps)} KEEP; {len(consolidations)} consolidations")
''' + s[end:]
p.write_text(s)
put('pt-01','Make the working progress snapshot distinguish fully executed original applications from written records with unmet stages.','The existing progress helper calls every recorded application completed, including partial learning procedures. Its explanatory text limits the claim, but the machine-readable completed list itself does not. I need the status fields to carry the distinction.', '''Interpretation 1: repair the tracking system for the existing fifty-slot allocation. The baseline remains the exact 3/2/1 allocation; this application cannot shrink it.

1. Collection. Scan the actual application files for a single final verdict, join to the allocation and explicit source-stage gate register, and derive status serially. Save the old progress snapshot as progress-before-correction.json. The old list contains 48 records. No logged labor-hours, budget, acceptance study or calendar completion deadline is available; those fields are unavailable, not zero.

2. Metrics. Record coverage and original-procedure execution are separate denominators over the same fifty slots. The new fields are recorded_applications, completed_applications, partial_applications, blocked_applications and pending_applications. A KEEP on an executed design operation does not override an unmet required human stage. Earned value, sprint velocity and burn rate are inapplicable without their required data. Two final progress applications are still being addressed at the initial snapshot; full human/delayed completion cannot be forecast from record-writing pace.

3. Dashboard. The following tracks actual gates rather than a decorative time series.

| Milestone | Evidence at initial snapshot | Status/next event |
|---|---|---|
| Fifty allocated applications recorded | 48 existing application files | Two progress applications remain |
| Exact originals and receipts | All 25 allocated originals retained/read | Complete source load; no effect implied |
| Full required procedures | Ledger separates stage gates | Human/delayed and campaign-data gates remain |
| Latest four KEEP consolidation | Three since consolidation-05 before this repair | Consolidate after this demonstrated repair |
| Public/persistent integration | Parent owns this work | Handoff files; no publication here |

4. Blocker register. Priority one is the misleading status field; owner conditions agent, action replace it now, target before the next parent handoff, resolved by the actual helper edit. Human physical/retrieval/practice stages have no observed participant or completed encounter; owner unassigned participant, action keep exact gates visible, target event a real authorized encounter rather than an invented date, open. Spaced stages require later occasions; owner future authorized continuation, action retain protocols, target after actual exposure and elapsed intervals, open. LRS lacks a campaign dataset; owner input provider if that direction is pursued, action do not relabel corpus records as contacts, open. RSO-03 measurement is currently executable; owner conditions agent, action instrument the serial regeneration pass, target this application, addressed in the measurement addendum. These patterns justify accurate state representation, not a diagnosis of anyone's motivation.

5. Variances. The quota is unchanged. The negative variance is source-stage execution relative to the fifty applications, caused by missing physical, temporal or dataset inputs. A calendar lateness figure would require an agreed baseline date and has not been calculated. The old data-schema error is evidenced directly by partial procedure IDs appearing in completed_applications. It would compound at root integration if copied as a completed count.

6. Audience report. For the parent: current coverage and execution must be read as separate figures; the corrected ledger lists every gate and owner/action category. Finite queue and graph outcomes are usable now. Human learning and access outcomes remain unmeasured. The next locally executable work is the last progress application and the assigned handoffs.

7. Communication/follow-up. The parent was informed of this correction in the milestone message. The generated ledger is the handoff artifact. No messages to human participants or outside services are sent. Root can request a finer gate breakdown; this report already implements the explicit fields root requested.

8. Update. The helper now regenerates the central conditions ledger before deriving progress, preserves the old snapshot, and leaves the fifty-slot baseline intact. Later writes call the same helper. The measured subsequent pass and exact snapshot counts are saved separately, so one local runtime sample is not used as a forecast of human procedures.''','The conditions agent changed the actual status schema and regeneration path so partial procedures no longer appear in the completed list.','Root can read a correct machine-level completion count without first interpreting a caveat attached to a broader list. This is a local adoption of the prior evidence-stage standard, not a new global discovery.','KEEP','Compare coverage-only, chronology-only and execution-gate dashboards. The execution-gate view answers which work can still be performed and is used in pt-02 and the handoff; chronology is preserved only where it supplies actual evidence.','Instrument the regeneration pass; apply the repaired counts to the final report; use the unresolved human gate when calibrating the assigned ADEp handoff.','The original has no numerical 8x scale. All eight original stages are applied with data availability, blocker ownership/target events, variance analysis, report and actual state update; unsupported time/cost metrics are not fabricated.')
