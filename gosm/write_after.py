from write_records import write,table
from pathlib import Path
import json

write(9,'review-and-exact-defects','A review concern must be tested against the actual application',
 'Replace a broad suspected source mismatch with exact dispositions about what should be accepted, repaired or rejected.',
 'A portfolio review identified that /orgn means organizational analysis and raised a concern about its placement in the representation line. That concern alone did not establish that its actual applications substituted file sorting for the original procedure.',
 '''Expected versus actual: the source-title concern suggested checking whether the two completed ORGN records addressed a human or agent organization. Inspection of the original and both application bodies showed that they do. The first analyzes the present seven-role distributed research task; the second analyzes knowledge-stewardship responsibilities and handoff authority. A representation-focused subject can still contain a genuine organizational analysis.

The emitted ORGN source contains six operations. Its SHA-256, independently compared with the reader receipt, is 866a4ee702de6bb2b176d82a37d9ff443cb7a5ef4dc1d6f10feeccd017589d95. The checked records are representation/001-orgn-1.md and representation/004-orgn-2.md.

| Original operation | Actual record evidence | Review disposition |
| --- | --- | --- |
| Identify organization and goal | Seven-role research task; local author/root/future reader stewardship | Applicable objects are supplied |
| Map structure | Strategic and operational authority, local versus integrating responsibilities | Organizational structure is present |
| Assess incentives and culture | Stated values, observed count requirement, explicit limits on inferred motives | No actual reward system is invented |
| Evaluate resources and processes | Source access, local editing, saving responsibility and unobserved human outcomes | Present resources and absent evidence are distinguished |
| Assess organizational capability | Local traceability versus unsupported durable human transfer | Capability claims are scoped |
| Recommend changes | Evidence-qualified handoff and reuse-state ledger | Original operation yields concrete local structures |

This inspection does not establish that all details are correct or globally novel. It defeats the blanket allegation that these two records merely applied an organization-sounding name to file sorting. Their early evidence distinctions were already in the shared standard and retain local-uptake, not global-discovery, status.

A genuine defect was present in record 004's first version: its path paragraph described a supposed change from the same path to itself, then concluded the path was correct. That narrative did not establish a repair. Root requested a concise replacement preserving the actual check: the relative path resolved, no repair occurred, and the suspected defect was rejected. The requested repair concerns the report, not an invented broken link.

Updated model: review has at least three different dispositions here. A routing concern can be refuted by valid application products; a substantive result can be useful locally without being new; and a contradictory report can need repair while the underlying path is valid. These outcomes cannot be collapsed into either “the agent was right” or “the skill was misused.”

Strongest contrary case: a record could include six original headings yet contain no actual organizational facts. The two inspected bodies supply actors, authority and resources, so this counter does not describe them. A different application must still be read; source identity and field presence alone cannot certify it.

Later application: the inquiry line reported RCA's instruction about fixing causes in AND/OR fault gates. Here the original advice, under its own present-failure semantics, is contradicted by a concrete truth-table row: after fixing A alone, (A,B)=(0,1), AND failure is false and OR failure remains true. Root read inquiry/13-fctl-fault-gates.md and accepted that precise source-error finding. The review therefore accepts the ORGN applicability evidence while rejecting RCA's exact intervention sentence under the stated semantics. It does not defend or distrust every original uniformly.

Next action taken: the ORGN report repair was sent to its author, the correctly scoped RCA finding was accepted for integration, and no original archive was rewritten. Verification remains the exact revised paragraph and the retained truth table. Open issues: other ORGN facts, downstream use quality and broader causal models are not settled by this inspection.''',
 'My review now accepts these ORGN applications as organizational analyses, withholds novelty credit for repeated standards, and targets the contradictory path report for repair. It separately accepts the demonstrated RCA source correction.',
 'The dispositions avoid discarding two applicable procedures and avoid laundering a source’s exact error through source authority. Repair success of the report is distinct from a first-pass success.',
 'KEEP — observed improvement in these specific review dispositions; no universal reviewer-reliability claim.',
 'Store concern → inspected proposition → decisive evidence → disposition, with source and application judgments separate. A single pass/fail per skill would lose the contrast between ORGN fit, repeated novelty and RCA error.',
 'Review a correct source executed incorrectly; review an incorrect source claim whose surrounding procedure remains useful; test a genuinely new content finding that has no later uptake yet.',variant='After',scope='Observed source and application inspection; primary assistant review state')

p=Path(__file__).parent.parent/'inquiry'
exports=json.loads((p/'questionroute-original-exports.json').read_text())
sure=next(x for x in exports if x['data']['question']['id']=='sure')
rows=[[r['targetId'],r['type'],r['weight'],r['reason']] for r in sure['data']['outgoing']]
write(10,'resource-recovery','A missing local representation did not require inventing its content',
 'Move a source-dependent investigation from unavailable local inputs to verified accessible originals, and distinguish successful retrieval from completed analysis.',
 'The local RSI bundle lacked the questionroute graph paths required by the original QR procedure. At that point the needed graph was unavailable locally; no claim that it did not exist elsewhere was justified.',
 '''Expected versus actual: the original skill referred to graph data and related chains. A local search did not provide those inputs. An authorized repository search then located benjam3n/questionroute. Its current tree did not contain the old data/questions and data/routes directories, but it did contain repository-owned exports in public/compare-data. The inquiry line retrieved all 438 exports and the nine original chains/sequences relevant to its selected roots.

The recovery retained repository tree 17dbbe3fea812c0cf3ed065be413ec18e6ea7ffd, source paths, original returned text, and Git blob identities. Root independently recomputed Git blob SHA-1 as the hash of the Git blob header plus each exact returned byte string. All 438 matched their recorded identities. There are 438 unique question IDs. The check is saved in questionroute-integrity-check.json; raw content remains in inquiry/questionroute-fetch-receipts.json. These are source-integrity results, not graph-semantic approval.

One actual recovered object is [sure.json](https://github.com/benjam3n/questionroute/blob/17dbbe3fea812c0cf3ed065be413ec18e6ea7ffd/public/compare-data/sure.json), blob ae3886ae8bac8c109cda8566498234ea9946969e. Its question is “Sure?”, definition “Certainty,” semantic type certainty, with the following original outgoing routes:

'''+table(['Target','Type','Weight','Original reason'],rows)+'''

The export also preserves four incoming route references, two chain references and a truth-seeking sequence reference. Full chain bodies were retrieved separately where required. This distinction matters: a chain ID and display text do not automatically supply every procedure step.

What the result reveals: the failed local lookup concerned a location and representation of the data. It was not evidence that the conceptual graph had to be invented. A source owner's exported representation can supply real operations when the required fields are present, while missing fields remain missing. A return-code or matching hash cannot supply an omitted semantic relation.

Updated model: the QR dependency is now accessible through exact repository exports and retained chain sources. Its analysis can proceed on original content. The graph's own route “sure→true” remains a proposition to examine; confidence-expression and factive-certainty readings differ. Authenticity does not decide which reading is correct.

Strongest contrary branch: an export could omit fields needed by the original procedure. That concern is valid and is not resolved by a byte match. For this selected work, question definitions and outgoing route reasons/weights are present; chain and sequence bodies have separate source evidence. Any still-required absent field would keep the corresponding operation incomplete.

Later application: root retrieved the separate able object from the preserved exports. It contains the definition of capability, routes to can/how/ready and a spiral-able-how-can chain reference. The recovered store therefore answered a new original-source lookup without reconstructing those routes from a skill name. No claim is made that root performed all QR operations merely by reading the object.

Next action taken: the verified source paths and integrity result were sent to the inquiry line, which can now perform its source-dependent QR operations. The remaining completion gate is the actual neighborhood, route and chain analysis with semantic review. Open issues: a future repository version, missing export fields and the validity of individual graph reasons each require their own checks.''',
 'My working resource state changed from a missing local QR dependency to a verified set of accessible source objects, and the recovered store supplied a distinct able lookup.',
 'The original-source investigation can continue without invented graph content or rebuilding an absent path. The benefit is observed access and reuse; source retrieval is not counted as QR execution.',
 'KEEP — actual source-access and reuse result, with semantic and field-completeness limits retained.',
 'Use source ID → original object → pinned path/blob → dependent analysis. Preserve both raw bytes and parsed objects so an easy lookup does not erase provenance. The alternate export location belongs in the continuation record, not in a rewritten archived skill.',
 'Check a future source version for field loss; inspect a semantically invalid route despite valid provenance; compare graph-neighborhood retrieval with an alternative question representation.',variant='After',scope='Observed authorized source recovery and a later source lookup; primary assistant resource state')
