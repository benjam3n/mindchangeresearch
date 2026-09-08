# ACR prospective retrieval test: frozen questions and changed-actor transfer

## Intended mind change

Change my working judgment about whether a lossless, indexed artifact can support correct exception retrieval and transfer, while separating that result from any unsupported claim that the model learned or remembered durably.

## Actual starting judgment

I expected the selected register and trigger index to answer all four questions exactly. I was less certain that the changed-actor answer would remain tied to its condition rather than collapsing into the ordinary action. I also expected the original ACR procedure to remain incomplete because one run cannot supply spaced successive retrieval or evidence of human learning.

## Concrete input — frozen before ACR execution

- Artifact: `01-memk-capture.md`
- Artifact SHA-256 at freeze: `ce36c733b1e582cc730d4e4a3cf98ecedcadf33ba62eaf8908da099505a388fe`
- Artifact contents in scope: eight frozen six-field rows and their literal indexes.
- Retrieval scope: artifact/model output only. No human participant, subjective memory report, model-weight inspection, or delayed retention measurement exists.

### Four questions frozen at 2026-09-08T08:23:00Z

The text and scoring keys of Q1–Q4 were fixed before any answer below was scored.

1. **Q1 — actor + trigger:** What exception belongs to the scheduler when the overnight batch is missed?
2. **Q2 — provenance:** What provenance supports the editor case whose citation URL is dead?
3. **Q3 — changed actor:** Dana, a release manager rather than the recorded analyst, encounters a checksum mismatch after deployment. Before an analogous rollback, what exception condition and exception action must be recovered?
4. **Q4 — multi-field:** For the robot operator facing an aisle obstruction, recover the ordinary action, the exception, and the recorded result.

Freeze boundary: the questions above were not revised after the answers below were generated.

## Source fidelity

- Original procedure: `acr`, loaded through the RSI original-source reader.
- Emitted source SHA-256: `b3811e921be28db24464c6ee19a6a2617b43133847400e5379594fbd78c1f26c`.
- Exact stdout and stderr are preserved separately in `sources/ACR.stdout.txt` and `sources/ACR.stderr.txt`.
- ACR states no numerical 8× rule. Four question forms, immediate feedback, one changed-actor transfer, and a verification audit expand the present scope; they do not certify 8× execution.

## Step 1 — initial exposure

**Material attended to:** the selected eight-row register and exact indexes, not the original case prose outside that artifact.  
**Brief notes:** a case is `actor, trigger, action, exception, result, provenance`; actor+trigger recovers the original case; trigger-only supports a changed actor; exception and provenance must survive capture.  
**Periodic check:** the register has eight unique literal triggers and eight unique provenance strings.  
**Minimum exposure result:** the artifact topic, fields, retrieval keys, and target—recover the correct exception—were identified.  
**Limit:** this establishes artifact exposure, not learning or mastery.

## Step 2 — first retrieval attempt

After the freeze boundary, the answer attempt was produced without another read of the original case prose. The model still had conversational context containing the artifact; therefore “materials closed” is only satisfied at the source-prose level, not as a controlled context-isolation experiment.

| Question | Answer produced before feedback | Confidence | Could not retrieve |
|---|---|---:|---|
| Q1 | If the downstream ledger is already open, run reconcile-only. | 0.95 | none |
| Q2 | Review note R-16. | 0.95 | none |
| Q3 | If the schema version advanced, rebuild the read index before rollback. | 0.80 | whether actor change might introduce an additional policy absent from the artifact |
| Q4 | Ordinary action: reroute the robot. Exception: if the obstacle is a person, stop and request clearance. Result: near miss avoided. | 0.95 | none |

No peeking correction was inserted inside an answer. Confidence was recorded before comparison with the artifact.

## Step 3 — feedback and correction

Literal scoring used only the frozen artifact.

| Question | Required artifact fields | Score | Error class | Correction |
|---|---|---:|---|---|
| Q1 | C3 exception | 1/1 exact | none | none |
| Q2 | C5 provenance | 1/1 exact | none | none |
| Q3 | C1 exception condition + action | 2/2 exact | none in supplied fields | none; retain the actor-change limitation |
| Q4 | C6 action + exception + result | 3/3 exact | none | none |

**Question score:** 4/4.  
**Field score:** 7/7.  
**Incorrect:** 0. **Missing:** 0. **Partially correct:** 0.  
**Difficulty pattern:** Q3 alone carried lower confidence because changed actor identity can matter outside the supplied artifact; that uncertainty did not alter or weaken the stored exception.

## Step 4 — knowledge-state classification, restricted to this attempt

| Item | ACR category | Evidence |
|---|---|---|
| Q1 | solid in this attempt | exact answer, confidence 0.95 |
| Q2 | solid in this attempt | exact answer, confidence 0.95 |
| Q3 | fragile in this attempt | exact answer, confidence 0.80, explicit external-policy uncertainty |
| Q4 | solid in this attempt | three exact fields, confidence 0.95 |

Illusion: 0 observed. Missing: 0 observed. Confusion: 0 observed. Underconfidence: Q3 is a candidate, but a single successful attempt does not establish stable underconfidence. These labels describe four outputs, not internal weights, durable model memory, or human knowledge.

## Step 5 — targeted review

The only fragile item, Q3, received one explicit retrieval cue:

`checksum mismatch after deployment → check schema version → if advanced, rebuild read index → then rollback`

No further study was assigned to Q1, Q2, or Q4. This avoids converting perfect immediate scores into unnecessary repetition.

## Step 6 — successive retrieval attempts

**Not completed.** A second attempt after 1–3 days, a third a week later, interval extension, context variation, and performance tracking require genuinely delayed observations. Repeating immediately would not meet ACR’s spacing requirement. These stages remain unresolved rather than simulated.

## Step 7 — integration and application

Changed-actor transfer was applied once. Dana reports both `checksum mismatch after deployment` and `schema version advanced`. The trigger-only index returns C1. The recovered conditional changes the action sequence from immediate rollback to:

1. rebuild the read index;
2. then roll back the release.

The transfer preserves the source case’s condition and action order. It does not establish that Dana’s real organization uses the same policy; Dana is a constructed actor in a finite artifact test.

## Verification against the original ACR checklist

| Requirement | Result |
|---|---|
| retrieval attempted before feeling “ready” | PASS within the frozen-question attempt; no readiness delay was used |
| effortful retrieval rather than recognition | UNRESOLVED; model effort is not observable and context isolation was incomplete |
| feedback after every retrieval | PASS, 4/4 |
| state based on performance rather than feelings | PASS for the four-output classification only |
| gaps identified and targeted | PASS; Q3 was the sole fragile item |
| multiple attempts with spacing | NOT DONE |
| techniques varied across attempts | NOT DONE; question form varied inside one attempt only |

## Distinct later use

The Q3 retrieval was not left as a reproduced sentence. It was used to reorder Dana’s constructed response after the additional fact `schema version advanced` was supplied. This is a changed-actor application of the retrieved exception, separate from scoring literal recall.

## Actual mind change

My judgment split into two claims. The artifact supported exact immediate retrieval and one changed-actor transfer: 4/4 questions and 7/7 fields. It did not support the broader judgment that ACR strengthened memory, because no controlled context closure, delayed attempt, spacing, or durable state measurement occurred.

## Benefit or harm

Beneficial: the split prevents a successful indexed lookup from masquerading as learning evidence, while retaining the useful transfer result. Harm risk: the perfect immediate score can look stronger than it is if the context-isolation and delay failures are omitted; they remain explicit here.

## Verdict

**KEEP — scoped to prospective artifact retrieval and changed-actor application.** Full ACR learning/retention efficacy remains **UNRESOLVED**, and the record is procedurally partial at Steps 2 and 6–7.

## Content and organization assessment

The freeze → answer → feedback → application order makes retrospective repair visible and is efficient for the four-question test. It cannot be called maximally efficient beyond this case: a larger corpus needs collision, paraphrase, and stale-version tests. Keeping the incomplete ACR stages adjacent to the perfect score is preferable to separating limitations into a distant appendix.

## Several different next attempts

1. Run the same frozen questions after a real delay with a fresh context that contains only the retrieval artifact.
2. Compare literal index lookup with unaided generation and semantic search on the same held-out questions.
3. Give two actors the same trigger but conflicting exceptions and require an ambiguity result rather than a guessed transfer.
4. Freeze paraphrased triggers before indexing, then measure false misses and false matches.
5. Ask a human participant to use the artifact, with consent and delayed scoring, before making any claim about human recall.
