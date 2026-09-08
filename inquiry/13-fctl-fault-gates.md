Intended mind change: Determine whether the original RCA source’s fault-tree intervention advice can be used when selecting which modeled causes to remove.

# FCTL 02 — AND and OR intervention advice

Original source claim, in RCA Step 5 benefits: “AND gates need all causes fixed; OR gates need any one.” Precise interpretation: for a failure event F=A AND B with both causes active, removing the failure requires fixing both A and B; for F=A OR B with both active, fixing any one cause suffices. “Fix A” means setting A false while leaving B unchanged. This is a definitional claim about the source’s stated gate semantics, not a statistical claim about a real incident.

Starting working judgment: I know the usual Boolean definitions, but had not checked this source-specific intervention sentence against the definitions the same source provides. I therefore had no verified basis for following its intervention advice. Actor: the current model selecting corrective actions for a stipulated fault tree. Source: ../sources/inquiry-rca.original.md; procedure: ../sources/inquiry-fctl.original.md; separate receipts retained for both. No numerical 8x FCTL definition is given. Scope: both gate types, all four valuations, both single fixes and both-fix case, seven error checks, and a later action selection.

True if the advice matches the Boolean gate truth conditions on every stated intervention. False if a single intervention gives a different result. Ambiguous if “need all causes fixed” means eliminate all future pathways under unspecified configurations instead of stop the defined present event; that stronger/different objective is not silently substituted.

| A | B | F=A AND B | F=A OR B |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Starting from A=B=1: fixing only A gives (0,1), stopping AND failure and leaving OR failure active. Fixing only B gives (1,0), the same respective outcomes. Fixing both gives (0,0), stopping both events. Therefore either single cause removal is sufficient for this two-input AND event; every active sufficient branch must be disabled for this OR event.

Evidence for the source advice: its published sentence says so; this establishes authorship of the assertion only. Evidence against: the four-row table follows directly from the AND/OR definitions in the source’s own preceding bullets. Expected missing support: no alternative gate definition is supplied that would make the advice true. The source’s correct gate definitions are retained; its intervention sentence is contradicted under the precise local-event interpretation.

Error checks: Selection—all valuations are included. Survivorship—both failed and successful fixes remain. Currency—Boolean definitions are stable; source pin/receipt identifies the inspected sentence. Ecological fallacy—no real-world causal prevalence is inferred. Base rate—none needed for a finite truth table. Conflation—present event suppression differs from eliminating every future cause. Precision—the conclusion covers these declared Boolean models and deterministic interventions only.

Verdict on the source sentence under the defined interpretation: FALSE, high confidence. Strongest contrary reading: a preventive policy could demand every contributory hazard removed even after the event is stopped. That changes the objective from gate failure suppression to comprehensive hazard removal; it does not validate the quoted gate advice. What would change the verdict: a different explicit event semantics or intervention semantics, requiring a fresh model and table.

Distinct later application: For the stipulated access failure F=(missing local copy AND no connector retrieval), the present actor need not repair both conditions to obtain access. Connector retrieval of the repository’s authentic exports already made “no connector retrieval” false while the original local data/questions path remained absent. For F=(wrong graph node OR missing source scope), correcting only the node would leave the scope failure; both active error branches must be addressed before declaring that OR event stopped. The first case is observed at the described access level; the second is a stipulated decision model.

Certificate: exact AND advice; decisive row (0,1) has F=0; a single fixed cause suffices, contradicting necessity of fixing both. Exact OR advice; the same row has F=1; one fix does not suffice. The alternative comprehensive-prevention reading is preserved separately. The graph-export access example supports a local use, not a claim that all real causal systems obey these simple gates.

Actual mind change: The source’s specific intervention sentence is rejected for the declared gate semantics; its definitions remain usable. The local-access plan accepts a successful alternate channel without demanding reconstruction of the absent original path.
Benefit: A concretely unnecessary second repair is excluded in the AND access case, while the OR case retains its unfixed branch. No original archive text is modified.
Verdict: KEEP
Organization: Definitions, source advice, intervention objective, and truth-table outcomes are adjacent. The corrected result is a finding about the original source, not a silently rewritten version of that source.
Next attempts: Apply the distinction to a mixed AND/OR tree; test a preventive objective separately; inspect minimal sufficient cut sets; look for shared causes that invalidate naive branch independence.
