Intended mind change: Test the clock writing choices before deriving the final requirements.

# Original ARAW dependency — clock

Interpretation: design-position stress test. Actor: this model examining stipulated fixtures. The model authors both candidates and checks and is not an independent evaluator. No real reader response is available.

Source: [original ARAW](../sources/representation-araw.md), with [separate requirements](../sources/representation-araw.requirements.txt). The current source reload is checked in finish-source-reload-check.json.

Meta-ARAW: the unresolved design claim concerns a prospective reader; the local questions concern which information the proposed wording preserves. States vary by initial frame, item mutation, or event history. The ordinary complete baseline is retained as a serious alternative. Human superiority is not inferred from symbolic success. These candidate universals were never adopted as the starting baseline.

Phase 1 — exact claims and exploration

### C1 — A readiness-anchored invitation gives the prospective reader more useful thinking time than a display-anchored invitation.

Type: explicit candidate; category: analytical; VOI: high.

- F1 AR; parent C1: With the same five-second duration, the reader’s useful interval must increase after the wording change. [Necessary conditional commitment] 
- F2 AW; parent C1: A reader ready immediately gets the same interval; another ignores the timer entirely. No usefulness response exists. [Deferred countermodel] BEDROCK-TEST-DEFERRED: actual reader unavailable
- F3 ALT; parent F2: Keep the timing alternatives as candidates and ask for the reader’s actual use and preference. [Alternative derived from the specific wrongness/countermodel] 
- F4 AR; parent F3: The defined deadline difference can be measured locally without inferring useful attention. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C2 — Wait five seconds specifies one deadline without naming a starting event.

Type: analytical candidate; category: analytical; VOI: high.

- F5 AR; parent C2: The display at t=0 and readiness at t=3 must imply the same deadline. [Necessary conditional commitment] 
- F6 AW; parent C2: Display anchoring gives t=5; readiness anchoring gives t=8. [Fatal countercase] BEDROCK-TEST/LOGIC: clock.anchor_difference
- F7 ALT; parent F6: Name the event from which the five-second interval is measured. [Alternative derived from the specific wrongness/countermodel] 
- F8 AR; parent F7: The readiness-anchored version chooses t=8 in this event trace. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C3 — Repeating READY has no effect under a policy that restarts on every READY.

Type: analytical candidate; category: analytical; VOI: high.

- F9 AR; parent C3: READY at t=3 and t=6 must leave the original t=8 deadline unchanged. [Necessary conditional commitment] 
- F10 AW; parent C3: The restart policy sets the anchor to 6; at t=8 three seconds remain. [Fatal countercase] BEDROCK-TEST/LOGIC: clock.duplicate_ready
- F11 ALT; parent F10: Accept the first READY per active round if repeats must not restart it. [Alternative derived from the specific wrongness/countermodel] 
- F12 AR; parent F11: The first-event policy is due at t=8 on the same trace. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C4 — A canceled interval remains active until its original deadline under a cancel-clears-active policy.

Type: analytical candidate; category: analytical; VOI: high.

- F13 AR; parent C4: READY at 3 then CANCEL at 4 must still complete the same round at 8. [Necessary conditional commitment] 
- F14 AW; parent C4: Clearing active removes the anchor; only a new READY at 10 creates a deadline of 15. [Fatal countercase] BEDROCK-TEST/LOGIC: clock.cancel_and_restart
- F15 ALT; parent F14: Make cancellation terminate the old interval and require a fresh event for restart. [Alternative derived from the specific wrongness/countermodel] 
- F16 AR; parent F15: The resumed round has its own start and deadline. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C5 — A timer due at t=8 necessarily delivers output at t=8 when the next poll is t=10.

Type: analytical candidate; category: analytical; VOI: high.

- F17 AR; parent C5: A sparse polling trace must contain a delivery event at 8. [Necessary conditional commitment] 
- F18 AW; parent C5: The only recorded poll after readiness is 10; due is true there, but no output at 8 occurred. [Fatal countercase] BEDROCK-TEST/LOGIC: clock.late_poll
- F19 ALT; parent F18: Distinguish scheduled deadline from observed delivery time. [Alternative derived from the specific wrongness/countermodel] 
- F20 AR; parent F19: The record can preserve due=8 and delivered=10 without calling the duration seven seconds. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C6 — Two clocks with different offsets can be subtracted directly to recover elapsed time.

Type: analytical candidate; category: analytical; VOI: high.

- F21 AR; parent C6: A start reading 100 and current reading 108 on a clock offset by +5 must mean eight elapsed seconds. [Necessary conditional commitment] 
- F22 AW; parent C6: With the current clock five units ahead, the same underlying time interval is three seconds. [Fatal countercase] BEDROCK-TEST/LOGIC: stipulated clock offset arithmetic
- F23 ALT; parent F22: Use one clock domain or a known offset conversion. [Alternative derived from the specific wrongness/countermodel] 
- F24 AR; parent F23: Elapsed time becomes a difference between commensurate readings. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C7 — A negative remaining time must be displayed after a late poll.

Type: analytical candidate; category: analytical; VOI: medium.

- F25 AR; parent C7: At current 10 and deadline 8, the countdown must read -2. [Necessary conditional commitment] 
- F26 AW; parent C7: The declared countdown is max(0,deadline-current), which returns 0. [Fatal countercase] BEDROCK-TEST/LOGIC: clock.late_poll plus max definition
- F27 ALT; parent F26: Separate nonnegative remaining duration from positive lateness. [Alternative derived from the specific wrongness/countermodel] 
- F28 AR; parent F27: The record can show remaining=0 and late_by=2 without conflating them. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C8 — Pausing and canceling have the same continuation rule in every timer.

Type: analytical candidate; category: analytical; VOI: medium.

- F29 AR; parent C8: After two elapsed seconds, either event must leave the same remaining time on restart. [Necessary conditional commitment] 
- F30 AW; parent C8: A preserve-remainder pause leaves 3 seconds; a fresh-round cancel/restart assigns 5. [Fatal countercase] BEDROCK-TEST/LOGIC: two explicitly defined timer policies
- F31 ALT; parent F30: Name whether a stop preserves the remainder or discards the round. [Alternative derived from the specific wrongness/countermodel] 
- F32 AR; parent F31: The restart instruction can select 3 or 5 rather than hiding the difference in stop. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C9 — An invitation sent twice necessarily represents two intended rounds.

Type: analytical candidate; category: analytical; VOI: medium.

- F33 AR; parent C9: Two identical transmissions must create two timers. [Necessary conditional commitment] 
- F34 AW; parent C9: The stipulated retry repeats one message with the same round ID. [Fatal countercase] BEDROCK-TEST/LOGIC: one-round retry fixture
- F35 ALT; parent F34: Bind retries to a round identity and separate a new-round action. [Alternative derived from the specific wrongness/countermodel] 
- F36 AR; parent F35: A retry is idempotent within that identity while a new ID can start another round. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C10 — Ignoring every READY after the first remains correct after explicit cancellation and a new-round request.

Type: analytical candidate; category: analytical; VOI: medium.

- F37 AR; parent C10: A new READY at 10 after cancellation must be ignored forever. [Necessary conditional commitment] 
- F38 AW; parent C10: The new round has no active anchor; accepting READY creates the intended deadline 15. [Fatal countercase] BEDROCK-TEST/LOGIC: clock.cancel_and_restart
- F39 ALT; parent F38: Scope first-only behavior to an active round, not the whole session. [Alternative derived from the specific wrongness/countermodel] 
- F40 AR; parent F39: Deduplication preserves legitimate later starts. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C11 — A displayed timestamp alone reveals whether it marks sending, receiving, or readiness.

Type: analytical candidate; category: analytical; VOI: medium.

- F41 AR; parent C11: The number 3 must identify one event type without a field label. [Necessary conditional commitment] 
- F42 AW; parent C11: Each of the three event types can occur at 3 in distinct stipulated histories. [Fatal countercase] BEDROCK-TEST/LOGIC: event-type ambiguity
- F43 ALT; parent F42: Keep the event name with its timestamp. [Alternative derived from the specific wrongness/countermodel] 
- F44 AR; parent F43: Ready_at=3 cannot be mistaken for sent_at=3 by the declared record decoder. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C12 — Equal duration values guarantee equal opportunities to respond.

Type: analytical candidate; category: analytical; VOI: medium.

- F45 AR; parent C12: Both five-second policies must allow response at t=7 when readiness was t=3. [Necessary conditional commitment] 
- F46 AW; parent C12: The display-anchored interval ended at 5; the readiness-anchored interval ends at 8. [Fatal countercase] BEDROCK-TEST/LOGIC: clock.anchor_difference
- F47 ALT; parent F46: Compare actual allowed intervals as well as duration values. [Alternative derived from the specific wrongness/countermodel] 
- F48 AR; parent F47: The overlap and extra interval become explicit rather than inferred from a shared numeral. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C13 — A response received after the deadline proves the reader chose it after the deadline.

Type: analytical candidate; category: analytical; VOI: medium.

- F49 AR; parent C13: Receipt at 10 for a deadline of 8 must locate choice time after 8. [Necessary conditional commitment] 
- F50 AW; parent C13: The stipulated response was chosen at 7 and transported for three seconds. [Fatal countercase] BEDROCK-TEST/LOGIC: stipulated transport delay
- F51 ALT; parent F50: Separate choice time, send time, and receipt time when available. [Alternative derived from the specific wrongness/countermodel] 
- F52 AR; parent F51: A late receipt alone leaves the internal choice time unresolved. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C14 — The absence of READY is a negative answer to the lesson’s content question.

Type: analytical candidate; category: analytical; VOI: medium.

- F53 AR; parent C14: No readiness event must encode the proposition answer false. [Necessary conditional commitment] 
- F54 AW; parent C14: The declared readiness field has no truth-value answer mapping; no event is compatible with either later content answer. [Fatal countercase] BEDROCK-TEST/LOGIC: field-domain definitions
- F55 ALT; parent F54: Keep readiness and content response as different fields. [Alternative derived from the specific wrongness/countermodel] 
- F56 AR; parent F55: The empty readiness record cannot supply an answer key entry. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C15 — A shared countdown numeral alone identifies which of two concurrent rounds is active.

Type: analytical candidate; category: analytical; VOI: medium.

- F57 AR; parent C15: Remaining=3 must select one round. [Necessary conditional commitment] 
- F58 AW; parent C15: Round A started at 1 and round B at 2; at their respective polls 3 and 4 both show 3. [Fatal countercase] BEDROCK-TEST/LOGIC: two explicit round histories
- F59 ALT; parent F58: Include round identity when concurrent records are combined. [Alternative derived from the specific wrongness/countermodel] 
- F60 AR; parent F59: Equal remaining values cease to merge different event histories. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C16 — Replacing seconds with beats preserves every deadline without stating beat duration.

Type: analytical candidate; category: analytical; VOI: medium.

- F61 AR; parent C16: Five beats must equal five seconds for all beat rates. [Necessary conditional commitment] 
- F62 AW; parent C16: At two beats per second five beats take 2.5 seconds; at one per second they take 5. [Fatal countercase] BEDROCK-TEST/LOGIC: unit conversion arithmetic
- F63 ALT; parent F62: State the unit or rate conversion. [Alternative derived from the specific wrongness/countermodel] 
- F64 AR; parent F63: A numeric count becomes a duration only after its unit is fixed. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C17 — Canceling a timer also deletes every response already recorded in that round.

Type: analytical candidate; category: analytical; VOI: medium.

- F65 AR; parent C17: CANCEL after a recorded answer must erase that answer under a timer-only cancellation rule. [Necessary conditional commitment] 
- F66 AW; parent C17: The specified cancellation changes only active; the separate response store is untouched. [Fatal countercase] BEDROCK-TEST/LOGIC: separate state-variable definition
- F67 ALT; parent F66: State the scope of cancellation when stored responses exist. [Alternative derived from the specific wrongness/countermodel] 
- F68 AR; parent F67: Terminating future delivery does not silently rewrite historical input. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C18 — A named event is enough to compute a deadline when that event’s time was never observed.

Type: analytical candidate; category: analytical; VOI: medium.

- F69 AR; parent C18: Ready_at=unknown must produce a unique numerical value for ready_at+5. [Necessary conditional commitment] 
- F70 AW; parent C18: Readiness at 3 and readiness at 11 are both compatible, yielding deadlines 8 and 16. [Fatal countercase] BEDROCK-TEST/LOGIC: clock.anchor_difference and held_out
- F71 ALT; parent F70: Keep the deadline unresolved until the event time is supplied, or choose a new observable anchor. [Alternative derived from the specific wrongness/countermodel] 
- F72 AR; parent F71: The invitation can wait for an explicit restart event instead of inventing the earlier timestamp. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

Dependent continuation. Nodes retained below repeat base findings where needed; they do not earn additional independent finding credit. The eight-edge path is a candidate dependency path and is not certified merely by its length.

- F73 AW; parent C2: An unnamed start permits deadlines 5 and 8 from the same display/readiness trace. [Fatal] BEDROCK-TEST/LOGIC: clock.anchor_difference
- F74 ALT; parent F73: Name READY as the start and retain its timestamp. [Derived alternative] 
- F75 AR; parent F74: The deadline becomes ready_at+5 within the selected clock domain. [Necessary] 
- F76 AR; parent F75: A second READY timestamp supplies a different candidate deadline unless an acceptance rule selects one. [Necessary] 
- F77 AW; parent F76: Accepting every READY restarts the first trace from 3 to 6 and leaves three seconds at time 8. [Fatal] BEDROCK-TEST/LOGIC: clock.duplicate_ready
- F78 ALT; parent F77: Accept only the first READY of an active round, while cancellation clears that active round. [Derived alternative] 
- F79 AR; parent F78: A new READY after cancellation is now eligible and sets a fresh five-second deadline. [Necessary] BEDROCK-TEST/LOGIC: clock.cancel_and_restart
- F80 AR; parent F79: The held-out READY=11/duplicate=13 trace is due at 16, with one second remaining at 15. [Necessary] BEDROCK-TEST/LOGIC: clock.held_out

Phase 2 — complete registry and compact verdict certificates

The JSON registry lists every C and F entry with its actual parent. No additional finding enters this compilation.

| Claim | Exact countercase or dependency | Verdict and inference | Strongest contrary branch / unresolved dependency |
|---|---|---|---|
| C1 | F2; human useful-time comparison | UNCERTAIN: neither reader regime was observed. | F1 retains the exact candidate as an assumption, not evidence for it. F3→F4 is a separately scoped replacement; it does not rescue the rejected universal. |
| C2 | F6; clock.anchor_difference | REJECTED: one permitted countercase falsifies the universal candidate. | F5 retains the exact candidate as an assumption, not evidence for it. F7→F8 is a separately scoped replacement; it does not rescue the rejected universal. |
| C3 | F10; clock.duplicate_ready | REJECTED: one permitted countercase falsifies the universal candidate. | F9 retains the exact candidate as an assumption, not evidence for it. F11→F12 is a separately scoped replacement; it does not rescue the rejected universal. |
| C4 | F14; clock.cancel_and_restart | REJECTED: one permitted countercase falsifies the universal candidate. | F13 retains the exact candidate as an assumption, not evidence for it. F15→F16 is a separately scoped replacement; it does not rescue the rejected universal. |
| C5 | F18; clock.late_poll | REJECTED: one permitted countercase falsifies the universal candidate. | F17 retains the exact candidate as an assumption, not evidence for it. F19→F20 is a separately scoped replacement; it does not rescue the rejected universal. |
| C6 | F22; stipulated clock offset arithmetic | REJECTED: one permitted countercase falsifies the universal candidate. | F21 retains the exact candidate as an assumption, not evidence for it. F23→F24 is a separately scoped replacement; it does not rescue the rejected universal. |
| C7 | F26; clock.late_poll plus max definition | REJECTED: one permitted countercase falsifies the universal candidate. | F25 retains the exact candidate as an assumption, not evidence for it. F27→F28 is a separately scoped replacement; it does not rescue the rejected universal. |
| C8 | F30; two explicitly defined timer policies | REJECTED: one permitted countercase falsifies the universal candidate. | F29 retains the exact candidate as an assumption, not evidence for it. F31→F32 is a separately scoped replacement; it does not rescue the rejected universal. |
| C9 | F34; one-round retry fixture | REJECTED: one permitted countercase falsifies the universal candidate. | F33 retains the exact candidate as an assumption, not evidence for it. F35→F36 is a separately scoped replacement; it does not rescue the rejected universal. |
| C10 | F38; clock.cancel_and_restart | REJECTED: one permitted countercase falsifies the universal candidate. | F37 retains the exact candidate as an assumption, not evidence for it. F39→F40 is a separately scoped replacement; it does not rescue the rejected universal. |
| C11 | F42; event-type ambiguity | REJECTED: one permitted countercase falsifies the universal candidate. | F41 retains the exact candidate as an assumption, not evidence for it. F43→F44 is a separately scoped replacement; it does not rescue the rejected universal. |
| C12 | F46; clock.anchor_difference | REJECTED: one permitted countercase falsifies the universal candidate. | F45 retains the exact candidate as an assumption, not evidence for it. F47→F48 is a separately scoped replacement; it does not rescue the rejected universal. |
| C13 | F50; stipulated transport delay | REJECTED: one permitted countercase falsifies the universal candidate. | F49 retains the exact candidate as an assumption, not evidence for it. F51→F52 is a separately scoped replacement; it does not rescue the rejected universal. |
| C14 | F54; field-domain definitions | REJECTED: one permitted countercase falsifies the universal candidate. | F53 retains the exact candidate as an assumption, not evidence for it. F55→F56 is a separately scoped replacement; it does not rescue the rejected universal. |
| C15 | F58; two explicit round histories | REJECTED: one permitted countercase falsifies the universal candidate. | F57 retains the exact candidate as an assumption, not evidence for it. F59→F60 is a separately scoped replacement; it does not rescue the rejected universal. |
| C16 | F62; unit conversion arithmetic | REJECTED: one permitted countercase falsifies the universal candidate. | F61 retains the exact candidate as an assumption, not evidence for it. F63→F64 is a separately scoped replacement; it does not rescue the rejected universal. |
| C17 | F66; separate state-variable definition | REJECTED: one permitted countercase falsifies the universal candidate. | F65 retains the exact candidate as an assumption, not evidence for it. F67→F68 is a separately scoped replacement; it does not rescue the rejected universal. |
| C18 | F70; clock.anchor_difference and held_out | REJECTED: one permitted countercase falsifies the universal candidate. | F69 retains the exact candidate as an assumption, not evidence for it. F71→F72 is a separately scoped replacement; it does not rescue the rejected universal. |

CRUX points (eight):

1. Does C1 hold for its specified comparison? Evidence: human useful-time comparison; addressed by F1, F2, F3, F4. Blocked by the absent real reader.
2. Does C2 hold for its specified comparison? Evidence: clock.anchor_difference; addressed by F5, F6, F7, F8. The countercase settles this candidate in its declared universal scope.
3. Does C3 hold for its specified comparison? Evidence: clock.duplicate_ready; addressed by F9, F10, F11, F12. The countercase settles this candidate in its declared universal scope.
4. Does C4 hold for its specified comparison? Evidence: clock.cancel_and_restart; addressed by F13, F14, F15, F16. The countercase settles this candidate in its declared universal scope.
5. Does C5 hold for its specified comparison? Evidence: clock.late_poll; addressed by F17, F18, F19, F20. The countercase settles this candidate in its declared universal scope.
6. Does C6 hold for its specified comparison? Evidence: stipulated clock offset arithmetic; addressed by F21, F22, F23, F24. The countercase settles this candidate in its declared universal scope.
7. Does C7 hold for its specified comparison? Evidence: clock.late_poll plus max definition; addressed by F25, F26, F27, F28. The countercase settles this candidate in its declared universal scope.
8. Does C8 hold for its specified comparison? Evidence: two explicitly defined timer policies; addressed by F29, F30, F31, F32. The countercase settles this candidate in its declared universal scope.

Phase 3 — synthesis from the registry

- C1: F2 leaves the reader advantage unresolved; F3 and F4 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F1.
- C2: F6 rejects the candidate universal; F7 and F8 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F5.
- C3: F10 rejects the candidate universal; F11 and F12 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F9.
- C4: F14 rejects the candidate universal; F15 and F16 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F13.
- C5: F18 rejects the candidate universal; F19 and F20 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F17.
- C6: F22 rejects the candidate universal; F23 and F24 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F21.
- C7: F26 rejects the candidate universal; F27 and F28 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F25.
- C8: F30 rejects the candidate universal; F31 and F32 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F29.
- C9: F34 rejects the candidate universal; F35 and F36 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F33.
- C10: F38 rejects the candidate universal; F39 and F40 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F37.
- C11: F42 rejects the candidate universal; F43 and F44 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F41.
- C12: F46 rejects the candidate universal; F47 and F48 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F45.
- C13: F50 rejects the candidate universal; F51 and F52 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F49.
- C14: F54 rejects the candidate universal; F55 and F56 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F53.
- C15: F58 rejects the candidate universal; F59 and F60 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F57.
- C16: F62 rejects the candidate universal; F63 and F64 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F61.
- C17: F66 rejects the candidate universal; F67 and F68 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F65.
- C18: F70 rejects the candidate universal; F71 and F72 retain the concrete replacement and its limited consequence. The exact assumed commitment remains in F69.

Foreclosures: the universal candidates C2–C18 cannot be used as unconditional writing shortcuts. Their replacements cost additional state, wording, or a narrower promise. C1 forecloses an immediate superiority verdict because the decisive comparison is missing.

Weakest link: C1 depends on an actual reader; its countermodel is a possible state, not a fabricated observation. Independent verification is limited to the declared symbolic fixtures. Several base alternatives restate closely related state-preservation ideas, so 72 numbered base findings are not automatically 72 independent findings.

Depth verdict: PARTIAL. Eighteen analytical candidates and 80 tracked nodes exist; multiple live tests ran. The continued eight-edge presentation reuses base findings, and it contains transitions between related claims whose necessity is not established merely by proximity. No full original 8x certification is claimed. Completing that certification requires additional independently derived findings and semantically valid recursive branches, not relabeling this registry.

Actual mind change: The tested universal shortcuts were rejected or left unresolved; the ordinary complete baseline remains available.

Benefit: The concrete replacements expose lost route, item, or event information in the specified fixtures. This dependency alone does not establish reader benefit.

Verdict: UNRESOLVED — original 8x dependency remains partial; local countercases are retained.

Organization: Exact claim table, full parent registry, executed fixtures, and explicitly uncounted continuation nodes.

Next attempts: Extend only a substantively unresolved branch; obtain a real reader comparison; independently audit the proposed recursive dependencies.
