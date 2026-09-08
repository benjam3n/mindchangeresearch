Intended mind change: Replace an underspecified “wait five seconds” instruction with the assumptions needed for one restartable timer to have a determinate deadline.

# AEX dependency — restart timer

Input claim: “Within one active round, accept the first READY as the anchor, ignore duplicate READY events, clear the anchor on CANCEL, and let a later READY start a fresh five-second interval.” Interpretation: audit assumptions in a proposed technical writing artifact. Actor: this model; evidence: stipulated event traces; no participant response.

Core claims: C1 the policy assigns one deadline per active round; C2 cancel and later restart do not reuse the old anchor; C3 readiness anchoring gives a human more useful thinking time.

| ID | Assumption | Type | Hiddenness | Risk if wrong | Test |
|---|---|---|---|---|---|
| A1 | READY, CANCEL and POLL are distinct event types. | existence | surface | high | inspect trace schema |
| A2 | Each event has a timestamp in one clock domain. | knowledge | deep | critical | offset countercase |
| A3 | Duration is exactly five seconds. | knowledge | shallow | high | deadline arithmetic |
| A4 | “First READY” is scoped to an active round. | timing | buried | critical | cancel/restart fixture |
| A5 | A duplicate READY within an active round does not restart. | stability | deep | critical | duplicate-ready fixture |
| A6 | CANCEL clears the active anchor. | causal | deep | critical | cancel/restart trace |
| A7 | A later READY after cancellation creates a new round. | causal | buried | critical | cancel/restart trace |
| A8 | Deadline equals accepted-ready-time plus five. | causal | deep | high | held-out trace |
| A9 | Remaining time is clamped at zero. | knowledge | deep | medium | late-poll trace |
| A10 | Due time and observed delivery time are distinct. | knowledge | buried | high | sparse-poll trace |
| A11 | A retry can carry the same round identity. | existence | deep | high | retry fixture needed |
| A12 | Concurrent rounds require separate identities. | existence | buried | high | equal-countdown countercase |
| A13 | The system can retain the accepted timestamp. | capability | deep | high | state inspection |
| A14 | The recipient can signal READY and CANCEL. | access | shallow | high | interface check |
| A15 | The system has permission to restart only after cancellation. | permission | deep | medium | policy assertion |
| A16 | A response’s receipt time does not identify its choice time. | timing | buried | high | transport-delay case |
| A17 | “Useful thinking time” is the valued human outcome. | value | buried | high | ask participant |
| A18 | That human outcome can be compared only with observed behavior or report. | access | buried | critical | deferred participant study |

Dependency chains: A4 → active-round identity → accepted READY → retained timestamp → unique deadline (five layers; locally tested). A6 → cleared anchor → inactive state → eligible later READY → fresh deadline (five layers; locally tested). A18 → participant access → paired timer conditions → observed use/report → comparative human benefit (five layers; deferred).

Categories represented: causal, existence, stability, access, capability, value, knowledge, permission, timing. Hidden assumptions: A2, A4–A13 and A15–A18 exceed the six-assumption floor.

Immediately/already tested: A1–A13 and A16 via `finish-fixture-results.json`, `resume-wre-local-tests.json` and stipulated ARAW cases. Round A keeps anchor 3 after its duplicate while independent round B receives anchor 4. Interface/external inputs: A14–A15. Deferred: A17–A18 require a real participant. Priority: A2, A4–A8 determine the timer state; A18 blocks any human-effect upgrade.

Ten-question coverage by claim:

| Claim | Causal | Existence | Stability | Access | Capability | Value | Knowledge | Resources | Permission | Timing |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | A8 | A1,A11,A12 | A5 | A14 | A13 | state determinacy | A2,A3,A9,A10 | no distinct resource beyond event/state store | A15 | A4 |
| C2 | A6,A7 | A1 | old anchor does not persist | A14 | A13 | fresh-round policy | A2 | no distinct resource dependency | A15 | A4,A16 |
| C3 | proposed anchor→human outcome | participant/task exists within A18 | readiness regime held fixed | A18 | A14 | A17 | outcome definition in A17 | paired timer conditions are part of deferred A18 | participant permission belongs to deferred study | paired-condition timing belongs to deferred study |

Summary: 3 claims; 18 assumptions; types—existence 3, knowledge 4, timing 2, stability 1, causal 3, capability 1, access 2, permission 1, value 1. Hiddenness—surface 1, shallow 2, deep 8, buried 7; 15 deep/buried assumptions. High/critical assumptions: 16; priority assumptions: A2, A4–A8, A18.

Assumption map: C1 depends on A1–A5, A8–A13; C2 depends on A4, A6–A8, A15; C3 depends on A14, A17–A18. C1 and C2 survive the supplied traces. C3 remains unresolved.

Actual mind change: The timer artifact now scopes duplicate suppression to an active round and separates deadline, remaining time and observed delivery.

Benefit: The assumptions determine the supplied restart traces. Human useful-time benefit remains unobserved.

Verdict: KEEP as a completed AEX dependency; repeated event/scope rules receive no separate discovery credit.

Organization: Claims → eighteen assumptions → five-layer dependencies → testability and priority.

Next attempts: Execute a round-ID retry fixture; obtain a participant comparison before making a useful-time claim.
