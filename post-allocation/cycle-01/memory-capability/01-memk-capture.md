# MEMK prospective capture test: exception-preserving case memory

## Intended mind change

Change my working judgment from “a complete table is probably sufficient for later retrieval” to a judgment selected by exact preservation, retrieval, transfer, and access-cost tests.

## Actual starting judgment

I expected a full-field table to win because it preserved every supplied field. I had not established whether table completeness alone would expose an exception when a new actor inherited an old trigger.

## Concrete input — frozen 2026-09-08T08:16:37Z

No case was added or revised after organization testing began.

| ID | Actor | Trigger | Action | Exception | Result | Provenance |
|---|---|---|---|---|---|---|
| C1 | analyst | checksum mismatch after deployment | roll back the release | if the schema version advanced, rebuild the read index before rollback | service restored | Incident IR-041 |
| C2 | field nurse | medication barcode unreadable | perform manual verification | if it is an emergency and two identifiers are unavailable, use the emergency protocol | dose logged | SOP MED-7 §4 |
| C3 | scheduler | overnight batch missed | rerun the batch | if the downstream ledger is already open, run reconcile-only | accounts synchronized | Operations log B-118 |
| C4 | laboratory technician | control sample out of range | quarantine the assay | if the temperature logger shows an approved transient, run one confirmatory control before quarantine | batch released after confirmation | CAPA LAB-22 |
| C5 | editor | citation URL dead | replace it with an archived copy | if the DOI resolves to a corrected version, cite the correction instead of the archive | correction cited | Review note R-16 |
| C6 | robot operator | aisle obstruction | reroute the robot | if the obstacle is a person, stop and request clearance | near miss avoided | Safety observation OBS-09 |
| C7 | data steward | duplicate customer record | merge the records | if legal-hold tags differ, do not merge and escalate for custody review | accounts preserved | Audit DQ-203 |
| C8 | logistics coordinator | cold-chain sensor gap | reject the shipment | if a redundant calibrated logger covers the full gap, inspect the secondary log before rejection | shipment accepted | QA CC-51 |

## Source fidelity

- Original procedure: `memk`, loaded through the RSI original-source reader.
- Emitted source SHA-256: `05b1f28bc00cfcd64d3275afc2af7b126120318067f73da1ae4a57314d6b9d7d`.
- Exact stdout and stderr are preserved separately in `sources/MEMK.stdout.txt` and `sources/MEMK.stderr.txt`.
- MEMK states no numerical 8× rule. Four organizations and five exact tests expand the scope; this is not an invented 8× certification.

## Step 1 — capture filter

| ID | Capture type | Worth capturing because | Expiry risk |
|---|---|---|---|
| C1 | mistake + procedure | wrong rollback order can compound a deployment failure | schema and rollback process can change |
| C2 | procedure | the ordinary identity check can be impossible during an emergency | SOP revision |
| C3 | decision + rationale | ledger state changes rerun into reconcile-only | batch architecture change |
| C4 | procedure | a permitted transient changes quarantine order | control policy revision |
| C5 | decision + rationale | a correction outranks an archive when both exist | DOI or correction status change |
| C6 | procedure | a person changes reroute into a stop | safety policy revision |
| C7 | mistake + procedure | merging across legal holds can destroy custody boundaries | legal-hold policy revision |
| C8 | decision + rationale | redundant calibrated evidence can reverse rejection | calibration or acceptance policy change |

All eight pass the filter because deleting the exception can select a different action, not merely remove context.

## Step 2 — candidate formats and exact loss tests

Candidates were instantiated from the frozen rows:

- **O1 — narrative cards:** one six-field paragraph per ID, ordered C1–C8, no secondary index.
- **O2 — actor folders:** one complete card per actor, alphabetized by actor, no trigger index.
- **O3 — compact trigger map:** only `trigger → action → exception`.
- **O4 — normalized case register:** all six fields per ID plus exact indexes `actor+trigger → ID`, `trigger → ID`, and `provenance → ID`.

Tests compared literal field strings; paraphrases did not count. “Records inspected” counts the maximum cards/rows that must be examined when the querying actor differs from the stored actor.

| Organization | T1 fields round-tripped | T2 actor+trigger exception | T3 trigger-only exception | T4 provenance trace | T5 max records inspected |
|---|---:|---:|---:|---:|---:|
| O1 narrative cards | 48/48 | 8/8 | 8/8 | 8/8 | 8 |
| O2 actor folders | 48/48 | 8/8 | 8/8 | 8/8 | 8 |
| O3 compact trigger map | 24/48 | 0/8 | 8/8 | 0/8 | 1 |
| O4 register + indexes | 48/48 | 8/8 | 8/8 | 8/8 | 1 |

O4 dominates these candidates on this input: it ties the maximum score on T1–T4 and strictly improves T5 over the other lossless organizations. O3 is faster than O1/O2 but deletes actor, result, and provenance: exactly 24 of 48 supplied cells.

### Knowledge entry (95 words)

--- KNOWLEDGE ENTRY ---

Store exception-bearing cases as a complete six-field case register, then index both `actor+trigger` and `trigger`. The first index retrieves the original case; the second supports transfer when a different actor encounters the same trigger. Preserve result and provenance in the register even when the immediate query asks only for an exception. Example: `duplicate customer record` normally maps to `merge`, but differing legal-hold tags map to `do not merge; escalate for custody review`, with `Audit DQ-203` retained for verification. A trigger-only map retrieves quickly but loses who acted, what happened, and why the record is trustworthy.

--- END ---

### Selected retrieval artifact

The frozen input table is the canonical register. Its indexes are:

- `analyst|checksum mismatch after deployment → C1`
- `field nurse|medication barcode unreadable → C2`
- `scheduler|overnight batch missed → C3`
- `laboratory technician|control sample out of range → C4`
- `editor|citation URL dead → C5`
- `robot operator|aisle obstruction → C6`
- `data steward|duplicate customer record → C7`
- `logistics coordinator|cold-chain sensor gap → C8`
- each literal trigger above independently maps to the same ID
- each literal provenance above independently maps to the same ID

## Step 3 — retrieval structure

**Tags:** exception-registry, operational-memory, changed-actor, provenance, before-action  
**Category:** Mind change > Memory and capability > Exception-bearing cases  
**Links to:** decision rationale, action gating, active recall test, provenance verification  
**Retrieval trigger:** a familiar trigger recurs, possibly under a different actor, and the ordinary action may have an exception.

## Step 4 — future-self checks

| Check | Result | Concrete basis |
|---|---|---|
| Context independence | PASS | every row contains actor, trigger, action, exception, result, and provenance |
| Actionability | PASS | each row distinguishes the ordinary action from the exception action |
| Scannability | PASS within artifact | actor+trigger and trigger indexes each return one ID on this input |
| Specificity | PASS | all 48 supplied cells are retained literally |

No rewrite was required after these four checks.

## Step 5 — review schedule

**Next review:** when any referenced procedure is next used or revised.  
**Review action:** verify the exception and provenance first; update the row and both indexes together; archive the superseded row rather than silently replacing its historical result.

## Step 6 — pruning branch

Not executed: this was new capture, not review of an existing knowledge collection. No entry was represented as stale, archived, or deleted.

## Distinct later use

A supervisor, not the stored data steward, receives the trigger `duplicate customer record`. The trigger index returns C7 without knowing the original actor. The recovered exception is: if legal-hold tags differ, do not merge and escalate for custody review. The ordinary merge action was therefore withheld pending that condition. This later use was not one of the format-selection score cells.

## Actual mind change

My judgment changed. Full-field preservation is necessary on this input but not sufficient for efficient changed-actor retrieval: O1 and O2 preserve 48/48 fields yet require inspection of as many as eight records. The selected organization must preserve the complete record and expose a trigger-only access path.

## Benefit or harm

Beneficial within the tested eight-record artifact. The later use recovered the right exception and prevented unconditional reuse of the original action. The added indexes duplicate keys and therefore create a synchronization burden; the review action retains that cost explicitly.

## Verdict

**KEEP — scoped to artifact organization and retrieval.** No human memory, model-weight change, durable model learning, or universal optimality is claimed.

## Content and organization assessment

The content is maximally lossless among the four tested candidates, not among every possible organization. The organization is more efficient than the two other lossless candidates for the tested changed-actor query. A hash index, database, or semantic retrieval system could improve larger-scale access, so global maximality remains unproved.

## Several different next attempts

1. Introduce two records with the same trigger but different actor-specific exceptions and test ambiguity handling.
2. Replace literal trigger strings with paraphrases and measure false misses without silently widening matches.
3. Add effective and expiry dates, then test retrieval when the newest rule differs from the historically correct rule.
4. Delete one secondary index entry deliberately and test whether synchronization validation catches it.
5. Compare this normalized register with an append-only event log under case revision and audit reconstruction.
