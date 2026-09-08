from write_records import save,BASE
import json,math

def delayed(gain,steps=30):
 xs=[0.,0.]
 for t in range(steps):xs.append(xs[-1]+gain*(10-xs[-2]))
 return xs
curves={str(g):delayed(g) for g in [.8,.4,0]}
metrics={g:{'overshoot':max(xs)-10,'last_error':abs(xs[-1]-10),'max_abs_error_last10':max(abs(x-10) for x in xs[-10:])} for g,xs in curves.items()}
(BASE/'delayed-control.json').write_text(json.dumps({'equation':'x[t+1]=x[t]+gain*(10-x[t-1])','initial':[0,0],'target':10,'curves':curves,'metrics':metrics},indent=2))
save('096-sya-1','sya','Analyze overshoot when revision uses delayed evidence','Change the gain of a repeated corrective action when feedback describes a previous state.','A large corrective step appears efficient when the present gap is large. My initial candidate gain is .8 of the reported gap; it has not been evaluated under delayed reporting.',
'''Boundary: a synthetic scalar working-state controller with target 10, one-step delayed observation, and no external disturbances. The state is a numerical proxy in a defined model, not a person's belief or emotion. Initial x[-1]=x[0]=0. The equation is x[t+1]=x[t]+g(10−x[t−1]). Time unit is one revision cycle.

Variables: state x is the stock; correction u is a signed flow; reported gap e=10−x[t−1] is auxiliary; target is external. Links: x→gap is negative after one-step delay, gap→u positive, u→x positive. One negative edge makes the loop balancing in sign; the delay permits overshoot and oscillation. No reinforcing loop is needed for this model's oscillation.

Stock/flow: inflow max(u,0), outflow max(−u,0); change equals their difference. Fill time depends on gain and delay; initial stock is zero. The trace in `delayed-control.json` computes 30 corrections for g=.8, .4 and 0.

Archetype checks: fixes-that-fail is structurally close because a correction based on an old state can reverse a later gap; shifting-the-burden is absent because no alternate capacity stock is present; limits-to-growth is absent because there is no capacity limit; success-to-successful, commons and escalation are absent because no competing actors exist; underinvestment is absent because no investment feedback exists. These are explicit model checks, not diagnoses of humans.

Interventions: reduce gain (.8→.4), remove observation delay, add a state bound, change target, or wait. Gain changes are available now; removing delay would require a different sensor; bounding x adds nonlinear clipping and can hide overshoot; changing target substitutes the goal and is not adopted. Waiting g=0 leaves error 10 forever, so patience alone is not adequate in this model.

Actual numerical results are read from the artifact below. A smaller gain reduces peak overshoot and late error on the declared horizon. First-order effect is smaller correction; second-order effect is less opposite-sign correction after delayed crossing; third-order effect is lower alternating amplitude. The side effect is slower initial approach. The original leverage hierarchy does not prove a goal change is better than a parameter change here; the available parameter directly resolves the modeled defect.'''+f"\n\nComputed comparison: {json.dumps(metrics)}.\n\nApplied choice: g=.4 replaces .8 for the next replay; target 10 is unchanged.",
'The model uses gain .4 with the same target after the delayed-response trace shows lower overshoot.','The exact recurrence yields the reported numerical improvement on 30 cycles. No empirical human response law is inferred.','KEEP','Signed loop and recurrence expose the delay; an isolated before/after gap does not.','Vary delay length; add bounded resources; compare a predictive state estimate with lower gain.')
# Controlled allocation example: two independent fixed outcome sequences, not outcome data.
seq={'A':[1,1,1,0,1,1,1,0,1,0],'B':[1,0,1,1,1,1,1,1,1,1]}
def run(policy):
 attempts={'A':0,'B':0};success={'A':0,'B':0};log=[]
 for t in range(12):
  if t==0:k='A'
  elif t==1:k='B'
  elif policy=='count':k=max(['A','B'],key=lambda k:(success[k],k=='A'))
  else:k='B' if t%3==2 else 'A'
  outcome=seq[k][attempts[k]%len(seq[k])];attempts[k]+=1;success[k]+=outcome
  log.append({'t':t,'selected':k,'outcome':outcome,'attempts':attempts.copy(),'successes':success.copy()})
 return log
logs={k:run(k) for k in ['count','probe']}
(BASE/'allocation-feedback.json').write_text(json.dumps({'defined_sequences':seq,'traces':logs},indent=2))
save('096-sya-2','sya','Analyze observation starvation in a method portfolio','Change allocation of exploratory attempts when accumulated success counts feed future selection.','Accumulated successes are a plausible signal for reusing a method. I have not yet separated the effect of getting more attempts from the effect of succeeding more often.',
'''Boundary: two methods with fixed supplied binary outcome sequences and twelve available trials. The sequences are artificial case inputs, not human effects or measured model capabilities. Initial counts are zero. Trial 1 selects A and trial 2 selects B; later baseline selection maximizes cumulative successes, ties favor A.

Stocks: attempts_A, attempts_B, successes_A, successes_B. Flows are one attempted action and its fixed sequence result per trial. Auxiliary selection preference is based on current success count. Causal links: successes_A→selection_A positive; selection_A→attempts_A positive; attempts_A→successes_A positive when the supplied outcome is one. This reinforcing loop competes for a fixed trial budget. A balancing loop arises as remaining trials approach zero; it stops both methods.

Archetype: success-to-successful is an exact structural match because selection itself creates opportunities to add counted success. Commons is absent: total trials are centrally allocated, not individually consumed without control. Shifting-the-burden and escalation lack their necessary secondary stocks/actors. Limits-to-growth matches the finite trial budget but says nothing about comparative efficacy.

Interventions considered: select raw counts; select empirical rates; reserve periodic B probes; randomize each trial; stop. Rates address denominator imbalance but can overreact to one success in one trial. Periodic probes guarantee observation coverage without claiming B better. Randomization offers probabilistic coverage but no guarantee over twelve draws. Stopping prevents learning.

Actual traces in `allocation-feedback.json`: baseline and periodic-probe schedules are run on the same supplied sequences. The allocation policy changes attempts and therefore evidence availability. The reserved probe every third trial supplies B evidence that raw counts would starve. The choice here is to preserve a learnable alternative, not maximize an unmeasured long-run reward.

Direct effect: one in three later slots goes to B. Feedback effect: B success count can now change from new observations. Delay: comparison confidence remains unresolved until enough representative observations exist; the finite fixed sequence is not a statistical population. Cost: some currently favored A attempts are foregone. Robust action in this instance is a bounded probe schedule, with future allocation reopened after the supplied twelve trials.''',
'The twelve-trial model changes from pure cumulative-count reuse to a declared periodic probe schedule.','The executed allocation trace gives both alternatives repeated observations; it does not establish general superiority or unbiased efficacy estimates.','KEEP','Stocks of attempts and successes reveal exposure feedback that a single success ranking hides.','Use balanced randomization; add switching cost; test when exploration has no plausible informational value.')
