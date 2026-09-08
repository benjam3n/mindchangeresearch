Intended mind change: Test the route writing choices before deriving the final requirements.

# Original ARAW dependency — route

Interpretation: design-position stress test. Actor: this model examining stipulated fixtures. The model authors both candidates and checks and is not an independent evaluator. No real reader response is available.

Source: [original ARAW](../sources/representation-araw.md), with [separate requirements](../sources/representation-araw.requirements.txt). The current source reload is checked in finish-source-reload-check.json.

Meta-ARAW: the unresolved design claim concerns a prospective reader; the local questions concern which information the proposed wording preserves. States vary by initial frame, item mutation, or event history. The ordinary complete baseline is retained as a serious alternative. Human superiority is not inferred from symbolic success. These candidate universals were never adopted as the starting baseline.

Phase 1 — exact claims and exploration

### C1 — Adding body-turn words to the complete compass route improves the prospective reviewer’s endpoint accuracy.

Type: explicit candidate; category: analytical; VOI: high.

- F1 AR; parent C1: With the same map and endpoint question, the reviewer must answer more accurately with the added turn words. [Necessary conditional commitment] 
- F2 AW; parent C1: A reviewer who already follows compass bearings gets the same answer from both; conflicting frame habits instead make the added words a distraction. No reviewer comparison exists. [Deferred countermodel] BEDROCK-TEST-DEFERRED: actual reader unavailable
- F3 ALT; parent F2: Retain both texts as candidates with measured endpoint accuracy as the discriminator. [Alternative derived from the specific wrongness/countermodel] 
- F4 AR; parent F3: Equal correct answers would provide no accuracy advantage to the longer candidate. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C2 — The relative command string FRFF reaches the same endpoint from every cardinal initial heading at the same start.

Type: analytical candidate; category: analytical; VOI: high.

- F5 AR; parent C2: North-facing and east-facing starts at (0,0) must end at the same coordinate. [Necessary conditional commitment] 
- F6 AW; parent C2: Executed north start ends at (2,1); east start ends at (1,-2). [Fatal countercase] BEDROCK-TEST/LOGIC: route.same_words_different_heading
- F7 ALT; parent F6: Attach the initial heading to a relative command string. [Alternative derived from the specific wrongness/countermodel] 
- F8 AR; parent F7: The anchored east instance now selects (1,-2), excluding (2,1). [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C3 — Map-right and body-right always denote the same compass direction.

Type: analytical candidate; category: analytical; VOI: high.

- F9 AR; parent C3: Facing east, a body-right turn must still point map-right, which is east on the declared north-up map. [Necessary conditional commitment] 
- F10 AW; parent C3: Facing east, a quarter-turn right points south; map-right remains east. [Fatal countercase] BEDROCK-TEST/LOGIC: cardinal rotation definition
- F11 ALT; parent F10: Name the frame of a direction word. [Alternative derived from the specific wrongness/countermodel] 
- F12 AR; parent F11: The labels map-right=east and body-right=south can coexist without contradiction. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C4 — Coordinates can replace orientation in every checkpoint for a relative walk.

Type: analytical candidate; category: analytical; VOI: high.

- F13 AR; parent C4: Two returns to coordinate (0,0) must permit the same next F command. [Necessary conditional commitment] 
- F14 AW; parent C4: The empty walk ends north-facing; FRFRFRF returns to (0,0) west-facing. The next F changes y in the first and x in the second. [Fatal countercase] BEDROCK-TEST/LOGIC: route.same_position_different_heading
- F15 ALT; parent F14: Store both position and heading for a relative-command checkpoint. [Alternative derived from the specific wrongness/countermodel] 
- F16 AR; parent F15: The two records now dispatch different next moves despite equal coordinates. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C5 — The number of forward moves and right turns determines a relative path endpoint, regardless of order.

Type: analytical candidate; category: analytical; VOI: high.

- F17 AR; parent C5: FRF and RFF, with two F tokens and one R token each, must agree. [Necessary conditional commitment] 
- F18 AW; parent C5: Executed FRF ends (1,1); RFF ends (2,0). [Fatal countercase] BEDROCK-TEST/LOGIC: route.reverse_turn_order
- F19 ALT; parent F18: Retain command order rather than only counts. [Alternative derived from the specific wrongness/countermodel] 
- F20 AR; parent F19: The sequence distinguishes moving before the turn from moving entirely after it. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C6 — Replacing R by L preserves the endpoint of every route with one quarter-turn.

Type: analytical candidate; category: analytical; VOI: high.

- F21 AR; parent C6: FRF and FLF from the same north-facing start must coincide. [Necessary conditional commitment] 
- F22 AW; parent C6: Executed endpoints are (1,1) and (-1,1). [Fatal countercase] BEDROCK-TEST/LOGIC: route.mirror
- F23 ALT; parent F22: Treat handedness as part of the route value. [Alternative derived from the specific wrongness/countermodel] 
- F24 AR; parent F23: A mirrored route requires an explicitly transformed target, not an unchanged target label. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C7 — A qualitative distance word such as nearby fixes an exact endpoint on the declared integer grid.

Type: analytical candidate; category: analytical; VOI: medium.

- F25 AR; parent C7: The word nearby must select one displacement rather than a set. [Necessary conditional commitment] 
- F26 AW; parent C7: One eastward step and two eastward steps are both allowed by the stipulated label nearby, but end at (1,0) and (2,0). [Fatal countercase] BEDROCK-TEST/LOGIC: stipulated nearby domain {1,2}
- F27 ALT; parent F26: Use an integer leg length when exact coordinates are requested. [Alternative derived from the specific wrongness/countermodel] 
- F28 AR; parent F27: The value two excludes the one-step endpoint; nearby alone does not. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C8 — A list of compass bearings determines an endpoint without leg lengths.

Type: analytical candidate; category: analytical; VOI: medium.

- F29 AR; parent C8: The one-entry list east must pick one point. [Necessary conditional commitment] 
- F30 AW; parent C8: East for one step and east for two steps share the bearing list and differ in x. [Fatal countercase] BEDROCK-TEST/LOGIC: integer-grid addition
- F31 ALT; parent F30: Represent each leg by bearing and length. [Alternative derived from the specific wrongness/countermodel] 
- F32 AR; parent F31: The pair (east,2) selects a displacement that the bearing token alone leaves open. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C9 — A printed legend makes the route decodable in a spoken excerpt that omits the legend.

Type: analytical candidate; category: analytical; VOI: medium.

- F33 AR; parent C9: The excerpt must distinguish the meanings of F and R without any other code source. [Necessary conditional commitment] 
- F34 AW; parent C9: The declared spoken excerpt contains only FRFF; codebook A makes R a right turn and codebook B makes R a reset. Both fit the received symbols. [Fatal countercase] BEDROCK-TEST/LOGIC: two explicitly different codebooks
- F35 ALT; parent F34: Carry the code definitions into the spoken route or use full words. [Alternative derived from the specific wrongness/countermodel] 
- F36 AR; parent F35: A full-word quarter-turn no longer depends on the absent R mapping. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C10 — Every compass-only route needs the walker’s initial body heading to determine its endpoint.

Type: analytical candidate; category: analytical; VOI: medium.

- F37 AR; parent C10: The endpoint of one east step must differ when the initial body heading differs. [Necessary conditional commitment] 
- F38 AW; parent C10: The compass displacement is (1,0) for all four headings by the absolute-step definition. [Fatal countercase] BEDROCK-TEST/LOGIC: absolute direction definition
- F39 ALT; parent F38: Require heading only when the selected decoding rule uses relative commands. [Alternative derived from the specific wrongness/countermodel] 
- F40 AR; parent F39: The compass-only baseline remains an exact alternative with one less state variable. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C11 — Two conflicting direction descriptions still specify one executable move without a precedence rule.

Type: analytical candidate; category: analytical; VOI: medium.

- F41 AR; parent C11: Facing north, right and west in the same instruction must identify one move. [Necessary conditional commitment] 
- F42 AW; parent C11: Right specifies east and west specifies west; no displacement satisfies both. [Fatal countercase] BEDROCK-TEST/LOGIC: east != west
- F43 ALT; parent F42: Either make the two descriptions agree or reject the inconsistent instruction. [Alternative derived from the specific wrongness/countermodel] 
- F44 AR; parent F43: The contradiction is detected before selecting a destination; silently choosing one would add an unstated rule. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C12 — Interchanging the x and y axes leaves every coordinate route unchanged.

Type: analytical candidate; category: analytical; VOI: medium.

- F45 AR; parent C12: The displacement (1,2) must remain (1,2) after axis exchange. [Necessary conditional commitment] 
- F46 AW; parent C12: Axis exchange yields (2,1), a different ordered pair. [Fatal countercase] BEDROCK-TEST/LOGIC: ordered-pair equality
- F47 ALT; parent F46: Keep axis names attached to coordinate components. [Alternative derived from the specific wrongness/countermodel] 
- F48 AR; parent F47: A transformed diagram requires transformed coordinates if it is to designate the same point. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C13 — Repeating a route’s forward commands from its endpoint necessarily returns to its start.

Type: analytical candidate; category: analytical; VOI: medium.

- F49 AR; parent C13: A one-step east route repeated from (1,0) must end at (0,0). [Necessary conditional commitment] 
- F50 AW; parent C13: The repeat ends at (2,0). [Fatal countercase] BEDROCK-TEST/LOGIC: vector addition
- F51 ALT; parent F50: A return route reverses leg order and each absolute displacement. [Alternative derived from the specific wrongness/countermodel] 
- F52 AR; parent F51: Adding (1,0) and then (-1,0) returns to (0,0). [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C14 — An unlabeled arrow uniquely identifies entrance orientation in every diagram.

Type: analytical candidate; category: analytical; VOI: medium.

- F53 AR; parent C14: An arrow pointing east must always assert that the entrant faces east. [Necessary conditional commitment] 
- F54 AW; parent C14: In the stipulated second diagram the identical arrow identifies the destination east of the viewer, while entrance orientation is north. [Fatal countercase] BEDROCK-TEST/LOGIC: two stipulated arrow roles
- F55 ALT; parent F54: Label the arrow’s role as entrance heading or destination direction. [Alternative derived from the specific wrongness/countermodel] 
- F56 AR; parent F55: The same shape can now carry two separately declared relations without the decoder conflating them. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C15 — A path index alone determines the next relative move across all route instances.

Type: analytical candidate; category: analytical; VOI: medium.

- F57 AR; parent C15: Index one must supply both origin and orientation for the next token. [Necessary conditional commitment] 
- F58 AW; parent C15: At index one, starts (0,0,north) and (2,3,east) have different states; their next F reaches different coordinates. [Fatal countercase] BEDROCK-TEST/LOGIC: route instance definitions
- F59 ALT; parent F58: Bind a cursor to its route instance and state. [Alternative derived from the specific wrongness/countermodel] 
- F60 AR; parent F59: An index with instance identity can retrieve the correct anchored state; an isolated numeral cannot. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C16 — The shortest wording always leaves the fewest unresolved route values.

Type: analytical candidate; category: analytical; VOI: medium.

- F61 AR; parent C16: Go there must constrain at least as many route values as go east two steps. [Necessary conditional commitment] 
- F62 AW; parent C16: Go there leaves the target and distance unset; east two steps supplies both direction and distance. [Fatal countercase] BEDROCK-TEST/LOGIC: declared phrase contents
- F63 ALT; parent F62: Minimize words subject to the required route values being recoverable. [Alternative derived from the specific wrongness/countermodel] 
- F64 AR; parent F63: A shorter text is rejected when it merges two destinations relevant to the requested endpoint. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C17 — A destination name alone determines coordinates even when its location map is absent.

Type: analytical candidate; category: analytical; VOI: medium.

- F65 AR; parent C17: The label Archive must identify one coordinate in every received record. [Necessary conditional commitment] 
- F66 AW; parent C17: Map A assigns Archive=(1,0); map B assigns Archive=(0,1), and the detached label is identical. [Fatal countercase] BEDROCK-TEST/LOGIC: two stipulated maps
- F67 ALT; parent F66: Carry a map/version reference or the destination coordinate. [Alternative derived from the specific wrongness/countermodel] 
- F68 AR; parent F67: The reference selects which location assignment the route must satisfy. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

### C18 — A correct endpoint guarantees the route obeyed every intermediate restriction.

Type: analytical candidate; category: analytical; VOI: medium.

- F69 AR; parent C18: Any path ending at (1,1) must avoid the forbidden point (1,0). [Necessary conditional commitment] 
- F70 AW; parent C18: East then north visits (1,0); north then east avoids it; both end at (1,1). [Fatal countercase] BEDROCK-TEST/LOGIC: two explicit paths
- F71 ALT; parent F70: Retain intermediate constraints when route compliance, rather than endpoint only, is the question. [Alternative derived from the specific wrongness/countermodel] 
- F72 AR; parent F71: An endpoint check remains sufficient for the narrower endpoint task and insufficient for the restricted-path task. [Necessary under stated replacement; no human advantage inferred] BEDROCK-LOGIC: declared replacement and fixture

Dependent continuation. Nodes retained below repeat base findings where needed; they do not earn additional independent finding credit. The eight-edge path is a candidate dependency path and is not certified merely by its length.

- F73 AW; parent C4: The same-position countercase leaves the next relative F displacement underdetermined by position alone. [Fatal] BEDROCK-TEST/LOGIC: route.same_position_different_heading
- F74 ALT; parent F73: A sufficient relative-walk checkpoint includes orientation as well as position. [Derived alternative] 
- F75 AR; parent F74: With that pair, each F token selects exactly one of four cardinal displacement vectors. [Necessary] 
- F76 AR; parent F75: A turn token updates orientation modulo four before later displacement lookup. [Necessary] 
- F77 AR; parent F76: Consequently the same multiset of tokens can select different displacement sequences when order changes. [Necessary] 
- F78 AW; parent F77: The stronger candidate that endpoint depends only on token counts fails on FRF versus RFF. [Fatal] BEDROCK-TEST/LOGIC: route.reverse_turn_order
- F79 ALT; parent F78: A checkpoint plus an ordered suffix determines the remaining walk under the declared deterministic decoder. [Derived alternative] 
- F80 AR; parent F79: At held-out start (2,3), east-facing FRFF ends (3,1), while north-facing FRFF ends (4,4). [Necessary] BEDROCK-TEST/LOGIC: route.held_out_anchored

Phase 2 — complete registry and compact verdict certificates

The JSON registry lists every C and F entry with its actual parent. No additional finding enters this compilation.

| Claim | Exact countercase or dependency | Verdict and inference | Strongest contrary branch / unresolved dependency |
|---|---|---|---|
| C1 | F2; human endpoint comparison | UNCERTAIN: neither reader regime was observed. | F1 retains the exact candidate as an assumption, not evidence for it. F3→F4 is a separately scoped replacement; it does not rescue the rejected universal. |
| C2 | F6; route.same_words_different_heading | REJECTED: one permitted countercase falsifies the universal candidate. | F5 retains the exact candidate as an assumption, not evidence for it. F7→F8 is a separately scoped replacement; it does not rescue the rejected universal. |
| C3 | F10; cardinal rotation definition | REJECTED: one permitted countercase falsifies the universal candidate. | F9 retains the exact candidate as an assumption, not evidence for it. F11→F12 is a separately scoped replacement; it does not rescue the rejected universal. |
| C4 | F14; route.same_position_different_heading | REJECTED: one permitted countercase falsifies the universal candidate. | F13 retains the exact candidate as an assumption, not evidence for it. F15→F16 is a separately scoped replacement; it does not rescue the rejected universal. |
| C5 | F18; route.reverse_turn_order | REJECTED: one permitted countercase falsifies the universal candidate. | F17 retains the exact candidate as an assumption, not evidence for it. F19→F20 is a separately scoped replacement; it does not rescue the rejected universal. |
| C6 | F22; route.mirror | REJECTED: one permitted countercase falsifies the universal candidate. | F21 retains the exact candidate as an assumption, not evidence for it. F23→F24 is a separately scoped replacement; it does not rescue the rejected universal. |
| C7 | F26; stipulated nearby domain {1,2} | REJECTED: one permitted countercase falsifies the universal candidate. | F25 retains the exact candidate as an assumption, not evidence for it. F27→F28 is a separately scoped replacement; it does not rescue the rejected universal. |
| C8 | F30; integer-grid addition | REJECTED: one permitted countercase falsifies the universal candidate. | F29 retains the exact candidate as an assumption, not evidence for it. F31→F32 is a separately scoped replacement; it does not rescue the rejected universal. |
| C9 | F34; two explicitly different codebooks | REJECTED: one permitted countercase falsifies the universal candidate. | F33 retains the exact candidate as an assumption, not evidence for it. F35→F36 is a separately scoped replacement; it does not rescue the rejected universal. |
| C10 | F38; absolute direction definition | REJECTED: one permitted countercase falsifies the universal candidate. | F37 retains the exact candidate as an assumption, not evidence for it. F39→F40 is a separately scoped replacement; it does not rescue the rejected universal. |
| C11 | F42; east != west | REJECTED: one permitted countercase falsifies the universal candidate. | F41 retains the exact candidate as an assumption, not evidence for it. F43→F44 is a separately scoped replacement; it does not rescue the rejected universal. |
| C12 | F46; ordered-pair equality | REJECTED: one permitted countercase falsifies the universal candidate. | F45 retains the exact candidate as an assumption, not evidence for it. F47→F48 is a separately scoped replacement; it does not rescue the rejected universal. |
| C13 | F50; vector addition | REJECTED: one permitted countercase falsifies the universal candidate. | F49 retains the exact candidate as an assumption, not evidence for it. F51→F52 is a separately scoped replacement; it does not rescue the rejected universal. |
| C14 | F54; two stipulated arrow roles | REJECTED: one permitted countercase falsifies the universal candidate. | F53 retains the exact candidate as an assumption, not evidence for it. F55→F56 is a separately scoped replacement; it does not rescue the rejected universal. |
| C15 | F58; route instance definitions | REJECTED: one permitted countercase falsifies the universal candidate. | F57 retains the exact candidate as an assumption, not evidence for it. F59→F60 is a separately scoped replacement; it does not rescue the rejected universal. |
| C16 | F62; declared phrase contents | REJECTED: one permitted countercase falsifies the universal candidate. | F61 retains the exact candidate as an assumption, not evidence for it. F63→F64 is a separately scoped replacement; it does not rescue the rejected universal. |
| C17 | F66; two stipulated maps | REJECTED: one permitted countercase falsifies the universal candidate. | F65 retains the exact candidate as an assumption, not evidence for it. F67→F68 is a separately scoped replacement; it does not rescue the rejected universal. |
| C18 | F70; two explicit paths | REJECTED: one permitted countercase falsifies the universal candidate. | F69 retains the exact candidate as an assumption, not evidence for it. F71→F72 is a separately scoped replacement; it does not rescue the rejected universal. |

CRUX points (eight):

1. Does C1 hold for its specified comparison? Evidence: human endpoint comparison; addressed by F1, F2, F3, F4. Blocked by the absent real reader.
2. Does C2 hold for its specified comparison? Evidence: route.same_words_different_heading; addressed by F5, F6, F7, F8. The countercase settles this candidate in its declared universal scope.
3. Does C3 hold for its specified comparison? Evidence: cardinal rotation definition; addressed by F9, F10, F11, F12. The countercase settles this candidate in its declared universal scope.
4. Does C4 hold for its specified comparison? Evidence: route.same_position_different_heading; addressed by F13, F14, F15, F16. The countercase settles this candidate in its declared universal scope.
5. Does C5 hold for its specified comparison? Evidence: route.reverse_turn_order; addressed by F17, F18, F19, F20. The countercase settles this candidate in its declared universal scope.
6. Does C6 hold for its specified comparison? Evidence: route.mirror; addressed by F21, F22, F23, F24. The countercase settles this candidate in its declared universal scope.
7. Does C7 hold for its specified comparison? Evidence: stipulated nearby domain {1,2}; addressed by F25, F26, F27, F28. The countercase settles this candidate in its declared universal scope.
8. Does C8 hold for its specified comparison? Evidence: integer-grid addition; addressed by F29, F30, F31, F32. The countercase settles this candidate in its declared universal scope.

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
