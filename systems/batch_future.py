from write_records import save,BASE
import json
save('048-lpd-3','lpd','Find option value in keeping a currently dominated-looking route',
'Change whether a slow preparation route is removed from a future option set.',
'For the immediate task, a short available route is preferable. I would ordinarily leave the slower route out of the next-action recommendation, without deciding whether to retain it for changed conditions.',
'''Landscape: current task→available methods→resource budget→future task. Route A is immediately available and costs 2; route B requires a reusable preparation P costing 6, then costs 1 per matching use. Future matching uses are not known. Information, reusable setup and effort flow between current and future work.

Between-system search finds a timing gap: P's cost occurs now while its potential saving occurs later. An access gap exists if P creates a usable input that was otherwise unavailable. No price, geographic or commercial asymmetry is claimed. Inside-flow search finds repeated setup friction; simple caching can remove it only where the input remains valid.

Other leverage: compounding is limited—savings add linearly, not exponentially; automation removes repeated setup; aggregation spreads setup across uses; standardization supports reuse; optionality retains B without executing P. Trust and data require actual validity checks. Scarcity is the present effort budget, not an opportunity to control people.

| Candidate | Value and sustainability | Feasibility and risk |
|---|---|---|
| Use A now, retain B's prerequisites | no setup cost now; preserves later option | immediately feasible; small metadata burden |
| Pay P now | net saving after enough matching uses | consumes 6; worthless if no recurrence |
| Delete B because it is slower now | simplest present set | loses condition for later crossover |

Actual calculation: A over n uses costs 2n; prepared B costs 6+n. B becomes cheaper exactly when n>6, ties at n=6. At n=1, A costs 2 versus B's 7; at n=10, A costs 20 versus B's 16. If setup expires after five uses, B never reaches the crossover in that validity window.

Applied action: choose A for the current one-use task; retain B with trigger "more than six valid matching uses expected within setup lifetime" and expiry condition. No forecast of recurrence is inserted. This avoids paying speculative setup while preserving a mathematically justified future option.

Ranking: deferred optionality first under unknown recurrence; P now requires additional evidence; deletion loses a relevant conditional candidate. Defensibility is irrelevant to this internal information decision and is explicitly not scored as commercial advantage.''',
'The assistant selects A now but retains B with the exact crossover and validity trigger instead of treating current inferiority as permanent.',
'The computed n>6 boundary preserves a route that is cheaper in a specified future case without spending the six-unit setup cost now.',
'KEEP','A conditional option entry preserves horizon dependence; a present-only ranking does not.','Add setup decay; consider discounting; compare an information-gathering action about recurrence.')
# Consolidate immediately after the fourth new keep (gd3, gsr3, grf3, lpd3).
save('consolidation-03','gd','Preserve path, deadline, criteria version and crossover',
'Change how later opportunity choices retain time and meaning.',
'A single ranked method list looks compact, but the four new results depend on different conditions and cannot safely share one permanent rank.',
'''Inputs only: gd3's D→E→F path, gsr3's six-unit deadline, grf3's criterion-version crossover .6, lpd3's recurrence crossover n>6. Four source records retain provenance and scope.

Organizations compared: A permanent winner list would name graph, B, B and A; it loses the conditions under which each wins. B condition table preserves task relation, deadline, criterion version and recurrence window. C source-skill grouping preserves provenance but makes the changing condition indirect. B is selected; C remains the appendix.

Actual later use: a constructed future task has deadline 3, fidelity weight .8, eight valid matching recurrences, and direct C→F relation newly present. Applying the four retained boundaries: the six-unit case's B cannot be imported because this deadline differs; old criterion v1 favors A; prepared route becomes cheaper over eight uses (14 versus 16); the original missing-direct-path inference no longer applies after C→F is present. The arrangement thus preserves three context changes and one profitable recurrence calculation without forcing a single prior winner.

No new substantive claim is added: each result is substitution into a previously established boundary. The combined scenario is itself a replay, not evidence of a real future recurrence.

Content repair: all four entry labels explicitly name the actor and stipulated nature of scores/costs. Organization repair: "winner" is replaced by "condition→choice"; source identity remains in each row.''',
'The four findings are now used as conditional choice relations rather than permanent method ranks.',
'The later altered scenario does not misapply its earlier deadline, graph or criterion result; the retained recurrence formula evaluates the new n=8 case.',
'KEEP','Condition table wins altered-context replay; source order remains history.','Test contradictory conditions; inspect a case with missing criterion version; compare a decision graph when branches overlap.')
subjects=[
('043','fut',1,'Preservation effort over an accumulating record horizon','retained records',
'Keeping every useful record seems prudent, but maintenance costs accumulate even when each individual save is small.',
'Initial stock is 20 retained entries. A matching entry costs one maintenance unit each year. Values of retained content are unknown; this model addresses only maintenance exposure.',
[(1,25,30,20),(2,30,40,20),(5,45,70,20),(10,70,120,20),(25,145,270,20)],
'Continuation adds 5 entries/year; acceleration adds 10/year; disruption freezes additions and leaves 20. These are stipulated scenario definitions, not predictions about people or AI.',
'Use a validity/retention review trigger tied to actual entry count. Preserve provenance for retained entries; do not infer that all old entries should be deleted.',
'The near-term maintenance decision now depends on the stock and validity window, not merely on the small cost of saving one entry.'),
('044','fut',2,'Future criterion drift in a reused decision','criterion-dependent recommendation',
'A retained recommendation is easy to reuse. My starting expectation is that storing its scores is sufficient, unless a later result directly contradicts it.',
'Current A/B scores are A=(5 fidelity,2 speed), B=(3,5), with fidelity weight .8. The current winner is A. Future weights are unknown.',
[(1,.8,.7,.3),(2,.8,.6,.3),(5,.8,.5,.3),(10,.8,.4,.3),(25,.8,.2,.3)],
'Continuation holds w=.8; acceleration gradually increases speed priority as explicitly tabulated; disruption changes w to .3 immediately. No population preference forecast is made.',
'Retain the decision function A wins if w>.6, tie at .6, B below .6. Recompute when the criterion version changes.',
'The future plan now preserves the crossover function and awaits actual weights rather than projecting the current winner indefinitely.'),
('045','fut',3,'Future availability of a coordination mechanism','continuation after host changes',
'An available local handoff mechanism seems a reasonable foundation for current work, but treating its future availability as certain would exceed the evidence.',
'Current work can write a file and pass a path. Future host access, identity persistence and dispatch facilities are unknown. The scenario choice is among a host-specific command, plain artifact contract, and unactioned prose promise.',
[(1,'same host','more endpoints','no dispatch'),(2,'same host','more endpoints','no dispatch'),(5,'compatible host','new protocols','read-only archive'),(10,'compatible host','new protocols','manual retrieval'),(25,'compatible reader','heterogeneous readers','unknown reader')],
'Continuation preserves a compatible reader; acceleration introduces heterogeneous endpoints; disruption removes dispatch. These enumerate cases, not capability forecasts.',
'Build a plain artifact contract with explicit target, inputs, endpoint and completion evidence. Current dispatch remains tied to actually available tools; future execution stays unknown.',
'The continuation plan now separates a portable task specification from a host-dependent executable continuation.')]
for _,skill,n,title,subject,start,current,data,scenarios,action,change in subjects:
 rows='\n'.join('| '+ ' | '.join(map(str,row))+' |' for row in data)
 body=f'''Subject: {subject}. Current state: {current}

Key drivers are explicitly defined by the three scenarios. Scheduled real-world events are unknown. Timeframes retain the original four ranges: near 1–2 years; medium 3–7; long 8–20; far 20+. No unsupported technology or human forecast is added.

{scenarios}

| Year | Continuation | Acceleration | Disruption |
|---|---|---|---|
{rows}

Across near-term cases, the input already in motion is the current retained state; continuation reuses it, acceleration increases the declared driver, disruption changes availability or purpose. In the medium term, repeated exposure compounds maintenance or mismatch through repeated use; new capabilities exist only where stated as scenario assumptions. In the long term, old infrastructure/criteria become conditionally obsolete if the scenario changes their compatibility. Far-term worlds include continued readable evidence, larger incompatible collections, and no authorized execution environment. A future actor could find today's unversioned assumptions surprising; there is no measured consensus to attribute.

Winners and losers are conditional roles: a later user benefits from compatible evidence, a maintainer bears accumulated cost, a controller loses an executable path when its host disappears. Opportunities are re-evaluation and portable evidence; threats are obsolete scope and unsupported persistence promises. The obsolete object is an unconditional recommendation or command under changed prerequisites, not necessarily the original evidence.

Robustness: every defined scenario preserves the historical fact of the current computation. That shared property is a conditional invariant of this model; inclusion in three hand-authored scenarios does not establish a high-confidence empirical prediction. Signals are actual entry count, actual criterion version, actual host contract as relevant to this subject. Those observations distinguish scenarios without guessing which will arrive.

Applied action now: {action} The declared future tables are retained in `future-{n}-scenarios.json`; subsequent choice uses the trigger rather than a date-based forecast. Opportunity remains distinct from realized human benefit.

Most surprising relative to the starting judgment: disruption can leave a perfectly correct historical result whose future use is unavailable or misaligned. The original result need not have been wrong. This conclusion is limited to the supplied scenario transitions.'''
 save(f'044-fut-{n}',skill,title,'Change a present choice by preserving the relevant future conditions without forecasting unsupported capability.',start,body,change,'A concrete scenario table now changes what is retained or conditioned for later use; real future outcomes are untested.','KEEP' if n==1 else 'UNRESOLVED','Four time horizons plus scenario columns preserve variations that one extrapolated future loses. Only the performed present representation change is observed.','Observe the next actual condition change; test a discontinuous loss; add an omitted scenario that defeats the apparent invariant.')
 (BASE/f'future-{n}-scenarios.json').write_text(json.dumps({'subject':subject,'assumptions':scenarios,'rows':data,'action':action},indent=2))
