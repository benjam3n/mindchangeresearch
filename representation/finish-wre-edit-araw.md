Intended mind change: Test the edit writing choices before deriving the final requirements.

# Original ARAW dependency — edit

Interpretation: design-position stress test. Actor: this model examining stipulated fixtures. The model authors both candidates and checks and is not an independent evaluator. No real reader response is available.

Source: [original ARAW](../sources/representation-araw.md), with [separate requirements](../sources/representation-araw.requirements.txt). The current source reload is checked in finish-source-reload-check.json.

Meta-ARAW: the unresolved design claim concerns a prospective reader; the local questions concern which information the proposed wording preserves. States vary by initial frame, item mutation, or event history. The ordinary complete baseline is retained as a serious alternative. Human superiority is not inferred from symbolic success. These candidate universals were never adopted as the starting baseline.

Phase 1 — exact claims and exploration

### C1 — Stable item names make the prospective editor’s revision more accurate than explicit original-position wording.

Type: explicit candidate; category: analytical; VOI: high.

- F1 AR; parent C1: On the same revision task, name-based wording must produce more correct target selections. [Necessary conditional commitment] 
- F2 AW; parent C1: An editor who already tracks original positions can select the same items; unfamiliar IDs can add lookup errors. No editor comparison exists. [Deferred countermodel] BEDROCK-TEST-DEFERRED: actual reader unavailable
- F3 ALT; parent F2: Keep both candidates and compare exact target selections with a real editor. [Alternative derived from the specific wrongness/countermodel] 
- F4 AR; parent F3: Equal selections support semantic equivalence for that editor without an accuracy superiority claim. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C2 — Delete the first item, then tag the second always tags the item that was second before deletion.

Type: analytical candidate; category: analytical; VOI: high.

- F5 AR; parent C2: On [A,B,C], the second operation must tag B. [Necessary conditional commitment] 
- F6 AW; parent C2: Live positional decoding deletes A, leaving [B,C], and tags C. [Fatal countercase] BEDROCK-TEST/LOGIC: edit.live_vs_initial_position
- F7 ALT; parent F6: State whether the ordinal binds before or after mutation. [Alternative derived from the specific wrongness/countermodel] 
- F8 AR; parent F7: Binding original second selects B; binding current second selects C. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C3 — Swapping deletion and tagging preserves the result of every positional edit pair.

Type: analytical candidate; category: analytical; VOI: high.

- F9 AR; parent C3: Deleting position zero then tagging position one must equal the reverse order. [Necessary conditional commitment] 
- F10 AW; parent C3: The executed first order tags C; the reverse tags B. [Fatal countercase] BEDROCK-TEST/LOGIC: edit.delete_noncommuting
- F11 ALT; parent F10: Preserve mutation order when selectors are evaluated against current positions. [Alternative derived from the specific wrongness/countermodel] 
- F12 AR; parent F11: The command sequence carries a semantic dependency that the unordered action set loses. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C4 — A stable ID remains a unique selector when two live items share that ID.

Type: analytical candidate; category: analytical; VOI: high.

- F13 AR; parent C4: Tag B must select exactly one item in [A,B,B]. [Necessary conditional commitment] 
- F14 AW; parent C4: The decoder reports two matches and refuses to select either. [Fatal countercase] BEDROCK-TEST/LOGIC: edit.duplicate_identity
- F15 ALT; parent F14: Validate uniqueness before resolving an identity selector. [Alternative derived from the specific wrongness/countermodel] 
- F16 AR; parent F15: A duplicate becomes an explicit unresolved selection, rather than an arbitrary tag. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C5 — Deleting A and tagging B fail to commute even when IDs are unique, A differs from B, and both are present.

Type: analytical candidate; category: analytical; VOI: high.

- F17 AR; parent C5: The two identity-based orders must produce different tagged survivors. [Necessary conditional commitment] 
- F18 AW; parent C5: Both executed orders yield B tagged and C unchanged. [Fatal countercase] BEDROCK-TEST/LOGIC: edit.stable_id_commuting
- F19 ALT; parent F18: Distinguish selector movement from a dependency inherent in all edits. [Alternative derived from the specific wrongness/countermodel] 
- F20 AR; parent F19: Independent targets permit this pair to commute; the positional version still fails. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C6 — Reordering items before an edit preserves the meaning of every current-position selector.

Type: analytical candidate; category: analytical; VOI: high.

- F21 AR; parent C6: Second must select the same ID in [A,B,C] and [C,A,B]. [Necessary conditional commitment] 
- F22 AW; parent C6: Second selects B in the first list and A in the second. [Fatal countercase] BEDROCK-TEST/LOGIC: edit.reordered_held_out
- F23 ALT; parent F22: Use stable identity when the task survives permutation of the list. [Alternative derived from the specific wrongness/countermodel] 
- F24 AR; parent F23: Deleting A and tagging B on the reordered fixture still tags B. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C7 — A deleted item can be selected as a live item without a tombstone or history mechanism.

Type: analytical candidate; category: analytical; VOI: medium.

- F25 AR; parent C7: Delete B then tag live B must find B. [Necessary conditional commitment] 
- F26 AW; parent C7: The live domain after deletion excludes B; there is no match. [Fatal countercase] BEDROCK-TEST/LOGIC: membership after deletion
- F27 ALT; parent F26: State whether a command addresses live items or historical records. [Alternative derived from the specific wrongness/countermodel] 
- F28 AR; parent F27: A live command fails explicitly; a historical command requires a separate retained record. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C8 — Visible text is a unique item identity even when two items have identical text.

Type: analytical candidate; category: analytical; VOI: medium.

- F29 AR; parent C8: The selector text=note must select one of two note entries. [Necessary conditional commitment] 
- F30 AW; parent C8: Items A and B both contain note and remain distinct records. [Fatal countercase] BEDROCK-TEST/LOGIC: two stipulated duplicate-text records
- F31 ALT; parent F30: Use an ID separate from display text when duplicates are allowed. [Alternative derived from the specific wrongness/countermodel] 
- F32 AR; parent F31: Editing one duplicate no longer implicitly edits or selects the other. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C9 — An ordinal retains its referent after insertion before that ordinal.

Type: analytical candidate; category: analytical; VOI: medium.

- F33 AR; parent C9: Second in [A,B,C] and [X,A,B,C] must refer to B. [Necessary conditional commitment] 
- F34 AW; parent C9: The new second item is A. [Fatal countercase] BEDROCK-TEST/LOGIC: list indexing definition
- F35 ALT; parent F34: Bind intended identity before insertion or resolve ordinals in a named snapshot. [Alternative derived from the specific wrongness/countermodel] 
- F36 AR; parent F35: Snapshot second remains B while current second becomes A. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C10 — Every deletion instruction can be safely repeated with the same positional arguments.

Type: analytical candidate; category: analytical; VOI: medium.

- F37 AR; parent C10: Delete current first twice must have the same result as deleting it once. [Necessary conditional commitment] 
- F38 AW; parent C10: One call removes A; two calls remove A and B. [Fatal countercase] BEDROCK-TEST/LOGIC: repeated deletion derivation
- F39 ALT; parent F38: Name the intended item and specify what happens when it is already absent. [Alternative derived from the specific wrongness/countermodel] 
- F40 AR; parent F39: An absent-A no-op policy preserves B on a retry; an error policy also prevents a second positional deletion. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C11 — A stable item ID proves that the item’s contents have not changed.

Type: analytical candidate; category: analytical; VOI: medium.

- F41 AR; parent C11: Item B must have identical text in every version retaining ID B. [Necessary conditional commitment] 
- F42 AW; parent C11: Version one has B=beta; version two has B=revised beta. [Fatal countercase] BEDROCK-TEST/LOGIC: two stipulated versions
- F43 ALT; parent F42: Carry a content precondition when the edit depends on old text. [Alternative derived from the specific wrongness/countermodel] 
- F44 AR; parent F43: Identity selects the same object; the precondition separately detects stale content. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C12 — A patch’s final list alone proves that only the requested operations occurred.

Type: analytical candidate; category: analytical; VOI: medium.

- F45 AR; parent C12: A final [B tagged,C] must exclude any temporary deletion and restoration of C. [Necessary conditional commitment] 
- F46 AW; parent C12: Both a direct edit and a delete/restore history yield that final list. [Fatal countercase] BEDROCK-TEST/LOGIC: two explicit histories
- F47 ALT; parent F46: Use an operation trace when forbidden intermediate actions matter. [Alternative derived from the specific wrongness/countermodel] 
- F48 AR; parent F47: Final-state equality remains adequate for a final-state-only requirement. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C13 — The phrase move it supplies a unique referent after mentioning A and B without a binding rule.

Type: analytical candidate; category: analytical; VOI: medium.

- F49 AR; parent C13: Both readers of the phrase must select the same item. [Necessary conditional commitment] 
- F50 AW; parent C13: The stipulated grammar permits nearest noun B and topic noun A; both bindings fit the phrase. [Fatal countercase] BEDROCK-TEST/LOGIC: two declared pronoun grammars
- F51 ALT; parent F50: Repeat the target ID at the operation boundary. [Alternative derived from the specific wrongness/countermodel] 
- F52 AR; parent F51: Move B selects one referent under the declared unique-ID map. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C14 — A numbered display tells the editor whether its indices are zero-based or one-based without a convention.

Type: analytical candidate; category: analytical; VOI: medium.

- F53 AR; parent C14: Delete index 1 must select the same element under both conventions. [Necessary conditional commitment] 
- F54 AW; parent C14: It selects B in zero-based [A,B,C] and A in one-based numbering. [Fatal countercase] BEDROCK-TEST/LOGIC: indexing definitions
- F55 ALT; parent F54: State the indexing convention or use unambiguous named identity. [Alternative derived from the specific wrongness/countermodel] 
- F56 AR; parent F55: An explicit convention removes this off-by-one ambiguity before mutation. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C15 — An ID-based patch applies to every document version containing the same IDs.

Type: analytical candidate; category: analytical; VOI: medium.

- F57 AR; parent C15: Delete A/tag B must remain appropriate even when the task changed from B to C. [Necessary conditional commitment] 
- F58 AW; parent C15: The later task requests tagging C while preserving the same IDs. [Fatal countercase] BEDROCK-TEST/LOGIC: two stipulated task versions
- F59 ALT; parent F58: Bind the patch to a task/version precondition as well as item IDs. [Alternative derived from the specific wrongness/countermodel] 
- F60 AR; parent F59: A matching ID no longer impersonates evidence that the old request still governs. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C16 — Checking selectors after performing the first destructive edit is equivalent to checking all selectors before it.

Type: analytical candidate; category: analytical; VOI: medium.

- F61 AR; parent C16: A missing B can be discovered after deleting A without changing the failure state. [Necessary conditional commitment] 
- F62 AW; parent C16: Preflight failure preserves [A,C]; late failure leaves [C]. [Fatal countercase] BEDROCK-TEST/LOGIC: preflight versus late-failure states
- F63 ALT; parent F62: Validate all required targets before the selected atomic revision. [Alternative derived from the specific wrongness/countermodel] 
- F64 AR; parent F63: The failure preserves the original list instead of exposing a partial edit. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C17 — Two selectors naming the same live item always denote two independent operations.

Type: analytical candidate; category: analytical; VOI: medium.

- F65 AR; parent C17: Tag B and delete B must commute because there are two separately written commands. [Necessary conditional commitment] 
- F66 AW; parent C17: Tag then delete leaves no B; delete then tag cannot find B under the live-item rule. [Fatal countercase] BEDROCK-TEST/LOGIC: live-domain operations
- F67 ALT; parent F66: Compare resolved target identity and operation semantics before declaring independence. [Alternative derived from the specific wrongness/countermodel] 
- F68 AR; parent F67: Different command lines do not establish disjoint targets. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C18 — A text-only after-state diff uniquely identifies the item changed when duplicate text records exchange positions.

Type: analytical candidate; category: analytical; VOI: medium.

- F69 AR; parent C18: The diff must recover whether A or B moved when both display note. [Necessary conditional commitment] 
- F70 AW; parent C18: Swapping A=note and B=note leaves the displayed text list unchanged. [Fatal countercase] BEDROCK-TEST/LOGIC: duplicate-text permutation
- F71 ALT; parent F70: Preserve IDs in the audit representation when object identity matters. [Alternative derived from the specific wrongness/countermodel] 
- F72 AR; parent F71: The identity diff records a permutation that the text projection erases. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

Dependent continuation. Nodes retained below repeat base findings where needed; they do not earn additional independent finding credit. The eight-edge path is a candidate dependency path and is not certified merely by its length.

- F73 AW; parent C2: After deleting A, the current second selector names C rather than B. [Fatal] BEDROCK-TEST/LOGIC: edit.live_vs_initial_position
- F74 ALT; parent F73: Resolve intended original positions to stable IDs before the deletion. [Derived alternative] 
- F75 AR; parent F74: The selected B identity remains B when A is removed. [Necessary] 
- F76 AR; parent F75: The same identity also survives the independent permutation [C,A,B]. [Necessary] BEDROCK-TEST/LOGIC: edit.reordered_held_out
- F77 AR; parent F76: That mechanism relies on ID resolution returning exactly one live item. [Necessary] 
- F78 AW; parent F77: Removing the uniqueness condition makes tag B ambiguous in [A,B,B]. [Fatal] BEDROCK-TEST/LOGIC: edit.duplicate_identity
- F79 ALT; parent F78: A preflight can require one live match for each needed ID before any mutation. [Derived alternative] 
- F80 AR; parent F79: With input [A,C], missing B then stops the revision while A remains present; late checking would already have removed A. [Necessary] BEDROCK-TEST/LOGIC: explicit preflight/late-failure states

Phase 2 — complete registry and compact verdict certificates

The JSON registry lists every C and F entry with its actual parent. No additional finding enters this compilation.

| Claim | Exact countercase or dependency | Verdict and inference | Strongest contrary branch / unresolved dependency |
|---|---|---|---|
| C1 | F2; human target-selection comparison | UNCERTAIN: neither reader regime was observed. | F1 retains the exact candidate as an assumption, not evidence for it. F3→F4 is a separately scoped replacement; it does not rescue the rejected universal. |
| C2 | F6; edit.live_vs_initial_position | REJECTED: one permitted countercase falsifies the universal candidate. | F5 retains the exact candidate as an assumption, not evidence for it. F7→F8 is a separately scoped replacement; it does not rescue the rejected universal. |
| C3 | F10; edit.delete_noncommuting | REJECTED: one permitted countercase falsifies the universal candidate. | F9 retains the exact candidate as an assumption, not evidence for it. F11→F12 is a separately scoped replacement; it does not rescue the rejected universal. |
| C4 | F14; edit.duplicate_identity | REJECTED: one permitted countercase falsifies the universal candidate. | F13 retains the exact candidate as an assumption, not evidence for it. F15→F16 is a separately scoped replacement; it does not rescue the rejected universal. |
| C5 | F18; edit.stable_id_commuting | REJECTED: one permitted countercase falsifies the universal candidate. | F17 retains the exact candidate as an assumption, not evidence for it. F19→F20 is a separately scoped replacement; it does not rescue the rejected universal. |
| C6 | F22; edit.reordered_held_out | REJECTED: one permitted countercase falsifies the universal candidate. | F21 retains the exact candidate as an assumption, not evidence for it. F23→F24 is a separately scoped replacement; it does not rescue the rejected universal. |
| C7 | F26; membership after deletion | REJECTED: one permitted countercase falsifies the universal candidate. | F25 retains the exact candidate as an assumption, not evidence for it. F27→F28 is a separately scoped replacement; it does not rescue the rejected universal. |
| C8 | F30; two stipulated duplicate-text records | REJECTED: one permitted countercase falsifies the universal candidate. | F29 retains the exact candidate as an assumption, not evidence for it. F31→F32 is a separately scoped replacement; it does not rescue the rejected universal. |
| C9 | F34; list indexing definition | REJECTED: one permitted countercase falsifies the universal candidate. | F33 retains the exact candidate as an assumption, not evidence for it. F35→F36 is a separately scoped replacement; it does not rescue the rejected universal. |
| C10 | F38; repeated deletion derivation | REJECTED: one permitted countercase falsifies the universal candidate. | F37 retains the exact candidate as an assumption, not evidence for it. F39→F40 is a separately scoped replacement; it does not rescue the rejected universal. |
| C11 | F42; two stipulated versions | REJECTED: one permitted countercase falsifies the universal candidate. | F41 retains the exact candidate as an assumption, not evidence for it. F43→F44 is a separately scoped replacement; it does not rescue the rejected universal. |
| C12 | F46; two explicit histories | REJECTED: one permitted countercase falsifies the universal candidate. | F45 retains the exact candidate as an assumption, not evidence for it. F47→F48 is a separately scoped replacement; it does not rescue the rejected universal. |
| C13 | F50; two declared pronoun grammars | REJECTED: one permitted countercase falsifies the universal candidate. | F49 retains the exact candidate as an assumption, not evidence for it. F51→F52 is a separately scoped replacement; it does not rescue the rejected universal. |
| C14 | F54; indexing definitions | REJECTED: one permitted countercase falsifies the universal candidate. | F53 retains the exact candidate as an assumption, not evidence for it. F55→F56 is a separately scoped replacement; it does not rescue the rejected universal. |
| C15 | F58; two stipulated task versions | REJECTED: one permitted countercase falsifies the universal candidate. | F57 retains the exact candidate as an assumption, not evidence for it. F59→F60 is a separately scoped replacement; it does not rescue the rejected universal. |
| C16 | F62; preflight versus late-failure states | REJECTED: one permitted countercase falsifies the universal candidate. | F61 retains the exact candidate as an assumption, not evidence for it. F63→F64 is a separately scoped replacement; it does not rescue the rejected universal. |
| C17 | F66; live-domain operations | REJECTED: one permitted countercase falsifies the universal candidate. | F65 retains the exact candidate as an assumption, not evidence for it. F67→F68 is a separately scoped replacement; it does not rescue the rejected universal. |
| C18 | F70; duplicate-text permutation | REJECTED: one permitted countercase falsifies the universal candidate. | F69 retains the exact candidate as an assumption, not evidence for it. F71→F72 is a separately scoped replacement; it does not rescue the rejected universal. |

CRUX points (eight):

1. Does C1 hold for its specified comparison? Evidence: human target-selection comparison; addressed by F1, F2, F3, F4. Blocked by the absent real reader.
2. Does C2 hold for its specified comparison? Evidence: edit.live_vs_initial_position; addressed by F5, F6, F7, F8. The countercase settles this candidate in its declared universal scope.
3. Does C3 hold for its specified comparison? Evidence: edit.delete_noncommuting; addressed by F9, F10, F11, F12. The countercase settles this candidate in its declared universal scope.
4. Does C4 hold for its specified comparison? Evidence: edit.duplicate_identity; addressed by F13, F14, F15, F16. The countercase settles this candidate in its declared universal scope.
5. Does C5 hold for its specified comparison? Evidence: edit.stable_id_commuting; addressed by F17, F18, F19, F20. The countercase settles this candidate in its declared universal scope.
6. Does C6 hold for its specified comparison? Evidence: edit.reordered_held_out; addressed by F21, F22, F23, F24. The countercase settles this candidate in its declared universal scope.
7. Does C7 hold for its specified comparison? Evidence: membership after deletion; addressed by F25, F26, F27, F28. The countercase settles this candidate in its declared universal scope.
8. Does C8 hold for its specified comparison? Evidence: two stipulated duplicate-text records; addressed by F29, F30, F31, F32. The countercase settles this candidate in its declared universal scope.

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
