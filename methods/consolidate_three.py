from write_support import *
q=json.loads((D/'instruction-difference-observations.json').read_text());v=json.loads((D/'single-step-unreadable-traces.json').read_text());r=json.loads((D/'route-criterion-results.json').read_text());s=json.loads((D/'sequence-localization-results.json').read_text())
uses=[
{'query':'Is reordered B physically invalid?','keep':'MD-01','answer':q['B_check']['physical_power_constraint'],'boundary':'A prerequisite must be supplied before physical validity is settled.'},
{'query':'What does unreadable then PASS do?','keep':'PV-02','answer':[t['next'] for t in v['unreadable_pass']],'boundary':'Missing observation differs from missing current state.'},
{'query':'At p=.10, under expected duration, which policy?','keep':'MD-02','answer':r['probability_cases'][1]['expected_choice'],'boundary':'Unknown p still does not yield a unique expected-time policy.'},
{'query':'Can ABAB→AB localize one missing pair?','keep':'FOHT-03','answer':len(s['repeated_reference']['all_deletion_only_explanations']),'boundary':'ABAC→ABC has exactly one witness, so ambiguity is not universal.'}]
(D/'consolidation-03-uses.json').write_text(json.dumps(uses,indent=2))
rows=[['By chronology','MD→PV→MD→FOHT','Preserves provenance order.','Route and instruction derivation share a skill label but require distinct triggers; query requires reading several prior records.'],['Under one uncertainty heading','All four avoid unsupported certainty.','Captures a shared constraint.','Does not name whether to type a relation, pause, compute a threshold or enumerate histories.'],['By observed question and next operation','Prerequisite? absent observation? criterion? ambiguous history?','All four exact saved results were retrieved in consolidation-03-uses.json.','Keep source links and boundaries because short triggers do not contain full evidence.']]
body='''Intended mind change: Make the next four established changes retrievable by the concrete question they answer.

Actual starting judgment: A broad “preserve uncertainty” heading is accurate but does not specify the different next operations already demonstrated.

Inputs are only established MD-01, PV-02, MD-02 and FOHT-03 findings plus prior K1–K8. No new substantive rule is inferred. Organization comparison:

'''+table(['Organization','Grouping','Benefit in these uses','Cost/boundary'],rows)+'''

The comparison actually loaded four saved products and answered four subsequent queries in consolidation-03-uses.json. Outputs: B’s physical prerequisite remains unspecified; unreadable→PASS goes paused→start; p=.10 under expectation selects East; ABAB→AB has three histories. The negative cases remain attached: a supplied check-before-start violation is definite; unreadable is not unknown state; unknown p is not p=.5; ABAC→ABC is uniquely localizable.

Chosen arrangement: question→operation→answer family→boundary→source. This preserves the different operations that a shared uncertainty slogan would hide. It is used immediately to append K9–K12 to active-keeps.md. The full records remain accessible for arguments and exact inputs; the trigger view does not replace original depth records.

Actual mind change: The four established findings are now retrieved by operational questions instead of one generic uncertainty label.

Benefit: Four exact artifact queries succeeded with their material boundaries retained. This is organizational uptake, not four new substantive KEEP findings and not a human retrieval-time experiment.

Verdict: KEEP

Organization: Question-based trigger view was better for these four uses; chronological provenance is retained as a secondary path. No claim that no superior organization exists.

Next attempts: Query a case without a matching trigger; retain a result that conflicts only after changing scope; compare a future group after four more demonstrated keeps.
'''
(D/'consolidation-03.md').write_text(body)
p=D/'active-keeps.md';txt=p.read_text();pos=txt.index('\nActual mind change:');txt=txt[:pos]+ '\n\n'+table(['Keep','Question/trigger','Established operation','Evidence','Boundary'],[
['K9','Did an instruction change a prerequisite?','Separate lexical edit, descriptive precedence and declared causal condition.','md-01','Unspecified physical rule stays unresolved; declared check-before-start can be violated.'],
['K10','Is the observation unreadable?','Pause and re-observe; invalidate old result after setup change.','pv-02','No claim that a human or device eventually supplies a readable value.'],
['K11','Is an observation worth its cost?','Use payoff vector and declared criterion; compute conditional threshold.','md-02','Unknown probability does not become 1/2; worst-time and expectation differ.'],
['K12','Does one edit script identify history?','Enumerate valid histories or find a second witness before localizing.','foht-03','A unique witness can localize; no witness may reject only the chosen edit model.']])+'''\n\nActual mind change: Twelve established triggers now expose their scoped operations.

Benefit: Actual retrieval and boundary use are recorded in consolidations01–03.

Verdict: KEEP

Organization: Question/trigger view with source provenance; full records preserve evidence.

Next attempts: Use the relevant trigger, retain a missing match, add only established findings after their later use.
''';p.write_text(txt)
progress=json.loads((D/'progress.json').read_text());progress['consolidations']=progress.get('consolidations',[])+[{'file':'consolidation-03.md','after_keeps':['md-01','pv-02','md-02','foht-03'],'new_benefit_credit':False}];progress['established_own_keep_findings']=12;(D/'progress.json').write_text(json.dumps(progress,indent=2))
