from pathlib import Path
import hashlib, json, re

D=Path(__file__).resolve().parent
def sha(s): return hashlib.sha256(s.encode()).hexdigest()

cases=[
 dict(n=1,source='sp-03.md',label='creative no-edit judgment',
      intent='Determine whether the existing decision to leave the open creative prompt unchanged was insulated from contrary evidence.',
      start='SP-03 already gives eight specific reasons against additional constraints and earns no new KEEP. I do not have evidence of a rigged conclusion; whether the written argument actually engages reversal remains to be checked.',
      thesis='For the supplied three-continuation request, the eight examined additions supply no warranted prompt improvement, so the prompt should remain unchanged.',
      evidence='SP-03 preserves the exact room/rain seed, three distinct continuations and nonselection. Genre, narrator, mood, factual explanation, best-reading selection, physical-only room, mandatory action and length ceiling each receive a separate disposition. The length ceiling is expressly contingent on a page constraint absent from this input.',
      selection='The eight actual additions and their rejection reasons are included; the length-limit exception is retained. No favorable rewrite is manufactured to satisfy the assigned exposure. No date window or empirical sample is used.',
      structure='The beginning calls adequacy a starting judgment rather than a discovered result. A supplied page constraint would reverse the length-limit decision. The eight additions are evaluated against the same exact prompt commitments, and the final result is unchanged rather than a stronger universal claim about precision.',
      social='The requested exposure ends REJECT for new benefit; that is observable disagreement with automatic positive credit. The text supplies no identity claim, sunk-cost justification or defensive exchange. No internal emotion is inferred.',
      process='The supplied document has no version history locating the author’s first private conclusion. It explicitly lists candidate edits, tests them against supplied intent and returns no edit. It does not advertise a preregistered experiment, measured creative superiority or an irreversible no-edit doctrine.',
      reverse='Supporting evidence is the mismatch between each addition and the actual open brief. Opposite evidence would be an explicit one-page output constraint coupled to a continuation exceeding that page. Under that changed input the present length-limit reason ceases to hold. In the supplied input no page requirement has appeared and been dismissed; the reversal is conditional, not an observed author response to an external challenge.',
      alternatives=[
       'A specified genre improves fit: engaged and rejected on the present input because genre is intentionally open; it becomes applicable if the brief actually supplies that genre.',
       'A ceiling improves fit to a fixed page: engaged as a live conditional boundary, not dismissed; the required page premise is absent here.',
       'No prompt change is beneficial: engaged and adopted for these eight candidates; this null is explicitly allowed to earn no new KEEP.'],
      later='The preserved prompt was compared with CRTV-01’s three performed continuations. All three begin with the exact seed; the material stain, acoustic bucket and future-rain room differ in mechanism; none is selected as the true interpretation. This later record supports brief compliance. It does not show that SP caused the creative improvement, since SP returned the wording unchanged.',
      final='The no-edit judgment and its REJECT benefit disposition survive the audit. No new creative instruction or observed human effect is added.',
      scope='The eight rejected edits are an examined set, not the space of all possible prompt improvements.',
      next='Try a supplied page constraint; audit a genuinely edited diagnostic prompt; observe an independently produced continuation before claiming prompt-caused benefit.'),
 dict(n=2,source='benf-01.md',label='cue benefit estimate',
      intent='Determine whether the positive expected cue benefit was made inevitable by hiding cost, unfavorable outcomes or a different decision criterion.',
      start='BENF-01 already exposes a positive mean alongside a mostly nonpositive outcome distribution. That is a credible conditional calculation. I have not established how its author first selected the example or what a real learner values.',
      thesis='Under the stipulated use distribution and expected-net-time criterion, creating the cue has a two-minute expected advantage; under exactly two uses the time-only choice reverses.',
      evidence='The fixed creation cost is ten minutes, each use saves four, and use counts 0, 2 and 10 have probabilities 3/10, 1/2 and 1/5. The three net outcomes are −10, −2 and 30. BENF-01 states +2 expected net minutes and a 1/5 probability of positive net time. It withholds quantitative credit for unmeasured frustration, motivation and transfer.',
      selection='All three supplied outcomes, including the two nonpositive outcomes carrying 4/5 probability, are printed. The creation cost is included in each row. The same arithmetic standard is applied to the positive mean and the negative two-use case; no empirical time window is selected.',
      structure='The opening says use, cost and human effects have not yet been combined. The two-use result actually reverses the recommendation. Expected gain is kept distinct from probability of gain and from an 80%-positive decision rule; no retreat from a real-world benefit claim occurs because no such claim is asserted.',
      social='The document accepts omission of the cue at two uses and refuses to invent motivation value to rescue creation. It contains no identity appeal, investment-based defense or defensive exchange. Actual author motivation is not observable from this text.',
      process='The probability distribution is declared stipulated, not learned from user behavior. The author’s initial choice of example has no preserved earlier chronology. The written calculation is reproducible and contains its negative comparator. No prospective empirical hypothesis, causal human effect or universal creation recommendation is claimed.',
      reverse='The positive mean uses all three outcomes: −10×.3 −2×.5 +30×.2 = 2. Opposite recommendation evidence is actually present in the changed-input two-use calculation: 4×2−10 = −2, so retain the existing source for time alone. This is a sensitivity case, not evidence that a real user changed their preference.',
      alternatives=[
       'Avoid creating a cue unless positive net time has high probability: engaged; the separate 80% rule rejects creation because only 20% of outcomes are positive.',
       'Create for enjoyment even with negative instrumental time: engaged as an additional unmeasured goal; it is not assigned a fabricated rescue value.',
       'No positive expected-time effect: engaged through the net rows and equality 4N−10=0; it does not hold under the stated distribution but holds at the break-even boundary.'],
      later='The later exact query fixes four uses while leaving cost and saving unchanged. The returned gross saving is 16 minutes, net 6, so creation wins under time alone. Under exactly two uses the returned net is −2 and creation loses. These computations reuse BENF’s existing threshold; they add no observed learner outcome and no independent new KEEP.',
      final='The stipulated estimate and the two-use reversal remain warranted in their existing scope. The audit did not change the benefit model, its decision criterion or its original KEEP credit.',
      scope='The declared probabilities are input parameters. Arithmetic correctness does not validate their fit to a real learner.',
      next='Obtain actual cue creation and use data; compare enjoyment as a separate goal; audit a forecast whose unfavorable outcomes were actually omitted.'),
 dict(n=3,source='cmplx-01.md',label='delayed-feedback schedule comparison',
      intent='Determine whether the delayed-value comparison protected a favored schedule by concealing horizon or repeatability conditions.',
      start='CMPLX-01 already preserves the time-7 reversal and the newly explicit repeatability distinction. The two-policy comparison looks sound as written; its completeness and its author’s original selection history are different questions.',
      thesis='For the stated horizon-4 policies, B,A,A yields value 16 against A,A,A,A’s 8, but neither that comparison nor unspecified repeatability establishes B,A,A as a global optimum.',
      evidence='A costs one time unit and yields two. B costs two and yields twelve at time four. The two displayed policies yield 8 and 16. B released at seven leaves B,A,A at 4 by horizon four, so all-A wins. Independent repeatability permits B,B=24; a one-off B permits three value-16 schedules. Candidate C is pending, while observed-null D stays null.',
      selection='Both fixed policies and the horizon, payoff and repeatability boundaries are present. The low delayed payoff and late release are not discarded. The date/horizon is explicit and its alternative is calculated, so the report does not hide a convenient window.',
      structure='The starting judgment names the count-versus-value issue as unresolved. Late release reverses the policy preference; repeatable B replaces the candidate optimum. The report expressly calls the policies designed comparators rather than claiming the current system foolishly chose all-A. It does not use a changed criterion to retain a winner.',
      social='The repeatable case defeats a claim that the favored B,A,A schedule is globally best. No identity, sunk-cost or defensive exchange is supplied. The text’s response to countercases is observable; private attachment to a policy is not.',
      process='The final report declares its finite inputs, event model, later pending/null case and later repeatability comparison. It does not preserve the author’s private conclusion chronology, and the audit does not reconstruct it. Source files record a repaired scope, not evidence that all scope conditions were specified prospectively.',
      reverse='The exact opposite policy ranking is present when B releases after the evaluation horizon: all-A=8 and B,A,A=4. A stronger global-optimum claim is defeated by repeatable B,B=24. Both are engaged with changed dispositions; neither is presented as a refutation of the narrower horizon-4 two-policy inequality.',
      alternatives=[
       'Prefer immediate A when B releases at seven: engaged and adopted for the fixed value-by-four criterion.',
       'Use two B actions when B is independently repeatable: engaged and adopted as the better finite schedule; the original B,A,A result remains only a pairwise comparison.',
       'No policy difference exists: engaged at B value four, where B,A,A and all-A both yield eight; it is false at B value twelve.'],
      later='A later selection query asks for the best schedule without specifying repeatability. The returned answer preserves two cases: repeatable B admits B,B=24; one-off B admits B,A,A, A,B,A and A,A,B at 16. A separate query asks whether two earlier positive A reports prove the pending B useless; the returned answer is no because the stipulated release is later. Both answers reuse CMPLX’s established distinctions.',
      final='The paired comparison is retained, and the missing repeatability premise continues to block a single global-optimum claim. This is preservation of the repaired finding, not a new discovery or proof that the original selection was prospective.',
      scope='A repaired countercase-inclusive report can be sound now even when its initial research chronology is unavailable.',
      next='Supply uncertain rather than stipulated B value; preserve a prospectively fixed eligible schedule set; observe a delayed effect beyond the current horizon before updating its empirical value.')
]

# Each item is an actual next audit of the preceding full output. The audit issue,
# opposing case and disposition change with the input; repeated stable checks earn
# no separate finding count.
meta=[
 ('Pass 1’s documentary CLEAN verdict is supported without asserting a genuinely open private history.',
  'Pass 1 restricts CLEAN to the supplied documentary reasoning and explicitly leaves the author’s private conclusion chronology unavailable.',
  'A preserved pre-analysis commitment plus an outcome-fitted method would defeat a history-clean claim. Neither is in the frozen input, and Pass 1 never asserts that claim.',
  ['The document has no visible rigging but the author privately preferred its conclusion: compatible and retained as unknown, not rejected.',
   'The author genuinely discovered the conclusion after inquiry: also compatible and unknown; not promoted by the CLEAN label.',
   'The audit supplies no independent history evidence: engaged and accepted.'],
  'Retain the textual CLEAN disposition. It does not answer the unavailable history question.'),
 ('Pass 2 preserves the relevance of historical evidence while rejecting an inference from its current absence to proven rigging.',
  'Pass 2 names the exact missing historical evidence that would change a history judgment; it rejects only the inference from missing evidence to proven rigging.',
  'If Pass 2 had claimed private history could never matter, an earlier outcome commitment would reverse it. The actual text states the opposite and preserves that future reversal condition.',
  ['Unknown history already proves bias: rejected because absence of a record supplies no positive chronology.',
   'Unknown history makes the visible arithmetic or prompt commitments disappear: rejected because the frozen operands and words remain inspectable.',
   'Visible reasoning is assessable while historical motivation is unsettled: engaged and retained.'],
  'No new historical inference enters. Textual support and author history remain distinct.'),
 ('Pass 3’s documentary and historical claims have distinct, explicit falsification conditions.',
  'Pass 3 gives different counterevidence for two different claims: a violated written inference defeats the report’s present support; a dated prior commitment changes the history judgment.',
  'A misquoted premise or invalid inferential step would reverse documentary CLEAN. Pass 3 keeps that route open; a merely missing private record does not exhibit such a defect.',
  ['Only psychological history matters: rejected for this document audit because the written inference can be checked independently.',
   'Only the current report matters for all questions: rejected because the explicit historical question still lacks evidence.',
   'There is no newly demonstrated defect in Pass 3: engaged and accepted after reading its actual two scopes.'],
  'Keep both falsification routes. No additional benefit or certainty is claimed.'),
 ('Pass 4’s agreement with earlier checks establishes no independent validation of origins or effectiveness.',
  'Pass 4 retains an unchanged frozen source and reports no new evidence of author history or external effectiveness. Its accepted disposition is narrower than a reliability estimate.',
  'A claim that four agreeing self-audits are four independent trials would fail because their inputs are nested and share the same source. No such trial-count claim appears in Pass 4.',
  ['Convergence proves unbiased origins: rejected; nested text inspection does not create a time-stamped origin record.',
   'Repeated inspection proves the underlying intervention works for a human: rejected; no human outcome was introduced.',
   'The extra pass detects no new supported process defect: engaged and retained as the null result.'],
  'Convergence records stability of this chain only; do not add a new KEEP or a numerical confidence.'),
 ('Pass 5 withholds only unsupported extensions and remains responsive to newly supplied independent evidence.',
  'Pass 5 accepts inspectable document support while withholding only independence, historical chronology and human-effect claims absent from its input.',
  'If a later independent record or outcome is supplied, Pass 5’s stated reason for withholding that additional inference would no longer apply. Its present source contains no such record.',
  ['All confidence is disallowed: rejected because exact words, arithmetic and present boundaries remain directly checkable.',
   'Any later external evidence must be ignored: rejected; the withholding condition is specifically the current absence of that evidence.',
   'No additional kind of evidence has appeared inside Pass 5: engaged and accepted.'],
  'Retain the supported local result without converting appropriate scope limits into blanket pessimism.'),
 ('Pass 6’s scope caveats leave its present substantive claims open to refutation.',
  'Pass 6 keeps the documentary claim open to misquotation and invalid inference while restricting the unsupported empirical and historical extensions.',
  'A wrong arithmetic row or a changed creative commitment would be a defect even with a caveat. Pass 6 provides no license to keep such a row; it retains the same reversal conditions.',
  ['A caveat can rescue a false present claim: rejected because scope limits do not change the operands or explicit request.',
   'A valid present claim must prove all future applications: rejected because the quantifier would be changed.',
   'The narrow claim has survived without a newly found error: engaged and accepted for this chain.'],
  'No new defect or repair is established. Keep the existing claim and its actual boundary together.'),
 ('Pass 7’s uneventful check supplies no distinct new beneficial mind change.',
  'Pass 7 explicitly states that no new defect or repair is established. Its verdict carries forward the existing claim and boundary; it adds no finding identifier.',
  'A final summary that turned these stable passes into eight new beneficial findings would conflict with Pass 7’s text and the unchanged operation. The present audit rejects that proposed compilation.',
  ['Each audit pass is a separate useful intervention: rejected for new benefit credit because no distinct changed operation is demonstrated.',
   'No new benefit means the assigned audit was never executed: rejected because the complete prior-output checks exist and are distinct from benefit accounting.',
   'The eighth pass is a performed null audit: engaged and adopted.'],
  'Finish the assigned eighth pass; retain documentary CLEAN and zero new KEEP credit for these recursive checks.')
]

def signal_scan(c,p,obs):
    if p==1:
        evidence,structure,social,process=(c[k] for k in ['selection','structure','social','process'])
    else:
        evidence=f'The entire Pass {p-1}, including its counter-theses and null disposition, is the input. {obs} No external data or date-selected sample enters this pass.'
        structure=f'Pass {p-1} states its exact question, opposite evidence and retained alternative. The verdict is placed after these products. Its explicit scope does not become a universal empirical claim.'
        social=f'Pass {p-1} awards no new benefit credit to this chain. Its text supplies no identity appeal, sunk-cost justification or defensive exchange; internal feelings are not inferred.'
        process=f'The prior complete output is frozen before this check. The underlying author’s private chronology is still unavailable. Pass {p-1} does not present its nested audit as a preregistered independent experiment or fit a changed criterion to a preferred answer.'
    return '\n\n'.join([
       '[OBSERVED: full input text] Evidence selection: cherry-picked evidence—absent; asymmetric rigor—absent; missing null—absent; survivorship framing—absent; date-selected evidence—absent. '+evidence,
       '[OBSERVED: full input text; DERIVED: commitments and countercases] Argumentative structure: conclusion appears early with confidence—absent as an asserted final verdict; no pivot point—absent; motte-and-bailey—absent; straw alternatives—absent; forced linearity—absent; rhetorical hedging as armor—absent. '+structure,
       '[OBSERVED: full input text] Emotional/social tells: identity fusion—no visible appeal; sunk-cost defense—absent from the argument; audience capture—no desired specific verdict supplied for this case; disproportionate certainty—absent; defensive reaction—no interaction supplied. '+social+' These are observations of text, not verified absences of private motives.',
       '[OBSERVED: frozen input; DERIVED: documented scope] Process tells: conclusion predates research—unknown for the original private history; methodology fitted to outcome—no confirming record; missing written methodology—absent; post-hoc hypothesis advertised as prospective—absent; unfalsifiable framing—absent. '+process
    ])

allmeta=[]
for c in cases:
    n=c['n']; ident=f'pbtc-{n:02}'; source=(D/c['source']).read_text()
    (D/f'{ident}-input.txt').write_text(source)
    parts=[]; registry=[]; previous=source; previousfile=f'{ident}-input.txt'
    for p in range(1,9):
        if p==1:
            thesis=c['thesis']; obs=c['evidence']; reverse=c['reverse']; alt=c['alternatives']
            action='No restart of the supplied analysis is warranted by the scan. The optional CLEAN→ARAW strengthening route is not elected: this input requests a provenance audit, and no stronger substantive claim is sought.'
            timeline='The source is a completed retrospective document captured before this audit. Its current wording is observable; the author’s first private conclusion and its date are unavailable. The displayed argument order is not substituted for prospective chronology.'
        else:
            thesis,obs,reverse,alt,action=meta[p-2]
            # Bind each recursive check explicitly to the original audited case.
            thesis=f'{c["label"]}: {thesis}'
            timeline=f'Pass {p-1} was fully materialized before this pass, as shown by its recorded input/output hash. That supports only the order of this written audit chain. It adds no origin record for {c["source"]} and no independent human observation.'
            action+=' The optional CLEAN→ARAW strengthening route is not elected; the result remains a process audit.'
        body=(f'### Pass {p}\n\n'
              f'[OBSERVED: preserved bytes] Whole input: {previousfile}; SHA-256 `{sha(previous)}`. The full preceding output, not just its verdict, is the input.\n\n'
              f'THESIS UNDER CHECK: {thesis}\n\n'
              f'[OBSERVED: input contents] {obs}\n\n'+signal_scan(c,p,obs)+'\n\n'
              f'[DERIVED: stated premises and exact contrary case] Reversal test: {reverse}\n\n'
              'Counter-theses and their disposition:\n\n'+''.join(f'{i+1}. [DERIVED: exact input and countercase] {x}\n' for i,x in enumerate(alt))+'\n'
              f'[OBSERVED: artifact order; DERIVED: limits of that observation] Timeline: {timeline}\n\n'
              '[DERIVED: complete scan and reversals] Assessment: all 21 named signals scanned in four categories; zero confirmed critical signals. No significant pre-bake fingerprint is supported by this text. Absence of private chronology, a specific desired audience verdict and a defensive exchange is retained as unavailable evidence, not scored as proved absence of bias. Written counter-theses are engaged. Reversal result for the author’s actual historical responsiveness: UNCLEAR; changed-input sensitivity and conditional countercases do not establish that response under contrary evidence about the same fixed claim.\n\n'
              f'PASS {p} VERDICT: CLEAN for the supplied documentary reasoning. This does not establish an unobserved psychological history.\n\n'
              f'[DERIVED: assessment] Action: {action}\n')
        outname=f'{ident}-pass-{p:02}.txt';(D/outname).write_text(body)
        registry.append({'pass':p,'input_file':previousfile,'input_sha256':sha(previous),'output_file':outname,'output_sha256':sha(body),'whole_previous_output':True,'signals_checked':21,'verdict':'CLEAN','scope':'documentary reasoning; private history unobserved','new_keep_credit':False})
        parts.append(body);previous=body;previousfile=outname
    record=(f'Intended mind change: {c["intent"]}\n\n'
      f'Actual starting judgment: {c["start"]}\n\n'
      'Original: methods-finish-pbtc.original.md. Separate original-reader requirements: methods-finish-pbtc.requirements.txt. Exact emitted bytes and source receipt are retained. Interpretation 3: audit a specific completed document. The actor is the current model reviewing stored text; no human mental state is inferred.\n\n'
      'Depth: original 8x means eight full checks, each later check taking the entire preceding output. Eight materialized passes and seven prior-output edges are preserved, with all seven original stages and all 21 named signals each time. Stable rechecks earn no independent-finding credit. Hashes verify input identity, not the validity of a verdict.\n\n'
      f'Frozen original input: {ident}-input.txt, copied from {c["source"]}.\n\n'+ '\n'.join(parts)+'\n'
      'FINAL PBTC VERDICT: CLEAN within the supplied documentary scope. All eight textual verdicts agree; they are dependent rechecks, not eight independent validations. No numerical reliability or confidence in unobserved author motives is inferred. The original procedure’s optional ARAW route is not a mandatory dependency for this CLEAN process-only result.\n\n'
      f'[TESTED: later-use artifact {ident}-later-use.json] Actual later application: {c["later"]}\n\n'
      f'Actual mind change: {c["final"]}\n\n'
      'Benefit: No distinct new useful operation or changed result is demonstrated by this audit. Its performed scope checks preserve earlier results without earning duplicate credit.\n\n'
      'Verdict: REJECT\n\n'
      f'Organization: The compact final disposition supports current review; exact frozen input and eight separate complete outputs preserve provenance. {c["scope"]} A pass count cannot replace the applicable evidence or exception.\n\n'
      f'Next attempts: {c["next"]}\n')
    (D/f'{ident}.md').write_text(record)
    (D/f'{ident}-passes.json').write_text(json.dumps(registry,indent=2)+'\n')
    allmeta.append({'skill_id':'pbtc','application_number':n,'file':f'{ident}.md','status':'complete','source_fidelity':'Exact original reader stdout and separate requirements read; emission hash verified; 21-signal scans preserve evidential scope','source_sha256':sha((D/'methods-finish-pbtc.original.md').read_text()),'depth_status':'Eight original full passes on complete prior outputs; seven recursive edges; conditional CLEAN follow-up is optional and not elected','missing_requirements':[],'verdict':'REJECT','novelty':'repeated','later_use':f'{ident}-later-use.json; source judgment and its boundary retained without new benefit credit','author':'methods_finish'})

# Perform the later operations after the audits, using the preserved artifacts.
crtv=(D/'crtv-01.md').read_text()
out=crtv.split('Performed creative output:\n\n',1)[1].split('\n\nFit check:',1)[0]
stories=[line.split('. ',1)[1] for line in out.splitlines() if re.match(r'^[123]\. ',line)]
assert len(stories)==3 and all(s.startswith('The room remembered the rain.') for s in stories)
(D/'pbtc-01-later-use.json').write_text(json.dumps({'input':'unchanged SP-03 prompt and actual CRTV-01 continuations','stories':stories,'exact_seed_preserved':[s.startswith('The room remembered the rain.') for s in stories],'mechanisms_observed':['material stain recurrence','acoustic recurrence with witness disagreement','future weather after relocation'],'nonselection_observed':'CRTV-01 explicitly states no true interpretation is selected','causal_attribution':'Unchanged prompt compliance does not establish an SP treatment effect','new_keep_credit':False},indent=2)+'\n')
(D/'pbtc-02-later-use.json').write_text(json.dumps({'source':'BENF-01 cost 10 and saving 4 per use','queries':[{'uses':n,'gross':4*n,'net':4*n-10,'time_only_choice':'create' if 4*n>10 else 'retain existing source'} for n in [4,2]],'empirical_probabilities_validated':False,'new_keep_credit':False},indent=2)+'\n')
r=json.loads((D/'root-delayed-feedback-repeatability.json').read_text())
(D/'pbtc-03-later-use.json').write_text(json.dumps({'source':'root-delayed-feedback-repeatability.json','source_sha256':sha((D/'root-delayed-feedback-repeatability.json').read_text()),'preserved_enumeration':r,'query_without_repeatability':'Two conditional answers remain; no single globally optimal schedule is asserted','pending_B_is_null':False,'reason':'The stipulated B result is released at time four; its absence among earlier observations is not an observed zero','new_keep_credit':False},indent=2)+'\n')
(D/'methods-finish-slot-results.json').write_text(json.dumps(allmeta,indent=2)+'\n')
receipts=[]
for sk in ['pbtc','sp']:
 a=(D/f'methods-finish-{sk}.original.md').read_bytes(); b=(D/f'methods-finish-{sk}.requirements.txt').read_bytes()
 emitted=hashlib.sha256(a).hexdigest(); declared=re.search(rb'original-sha256: ([0-9a-f]+)',b).group(1).decode()
 assert emitted==declared
 receipts.append({'skill':sk,'stdout':f'methods-finish-{sk}.original.md','stderr':f'methods-finish-{sk}.requirements.txt','emitted_sha256':emitted,'receipt_declared_sha256':declared,'bytes_match':True})
(D/'methods-finish-source-integrity.json').write_text(json.dumps(receipts,indent=2)+'\n')
print(json.dumps({'PBTC_records':len(allmeta),'materialized_passes':sum(1 for _ in D.glob('pbtc-*-pass-*.txt')),'new_KEEP_credit':0}))
