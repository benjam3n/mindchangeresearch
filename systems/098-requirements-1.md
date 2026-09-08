Intended mind change: Change a system design by surfacing previously implicit boundary requirements.

# Present action requirements at system boundaries

Starting judgment: I would begin with the central successful path. The initial design does not yet specify behavior for every missing, changed or expired condition.

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-requirements.md`; current requirements are retained separately in `../sources/systems-requirements.requirements.txt`.

Depth: Original 8x floors: 80 requirements, 10 categories, 10 stakeholder roles, 8 conflict checks. The record supplies these; roles are design perspectives rather than fabricated consultations.

System boundary: a present intervention selector from goal to revised action. Inputs are stated goals, evidence and resource conditions. Outputs are eligible choices, rejected transfers and explicit unresolved states. Human preferences are not inferred as measurements; external execution requires its actual host. This is a design specification applied to a constructed case, not an assertion a production system exists.

Stakeholders are ten distinct design roles, not ten interviewed people: requester, current operator, source owner, evidence reviewer, action executor, affected person, tool host, maintainer, future operator, integrator. Requester retains direction; operator needs feasible work; source owner needs source integrity; reviewer needs assessable evidence; executor needs a contract; affected person needs agency; host limits actions; maintainer needs recovery; future operator needs fit; integrator needs explicit dependencies. Interests follow from each role's function and remain revisable.

Eighty specific requirements across ten categories:

| ID | Category | Role | Priority | Required behavior |
|---|---|---|---|---|
| R1-01 | Goal identity | requester | MUST | Preserve the exact requested action |
| R1-02 | Goal identity | requester | MUST | Retain the named actor |
| R1-03 | Goal identity | requester | MUST | Retain the requested object |
| R1-04 | Goal identity | requester | MUST | Retain the declared time horizon |
| R1-05 | Goal identity | requester | SHOULD | Retain hard constraints |
| R1-06 | Goal identity | requester | SHOULD | Label an inferred purpose |
| R1-07 | Goal identity | requester | SHOULD | Keep alternative interpretations separately |
| R1-08 | Goal identity | requester | SHOULD | Reject an unauthorized goal substitution |
| R1-09 | Input availability | current operator | MUST | Detect a missing source |
| R1-10 | Input availability | current operator | MUST | Distinguish inaccessible from nonexistent input |
| R1-11 | Input availability | current operator | MUST | Retain source version |
| R1-12 | Input availability | current operator | MUST | Retain units on numeric inputs |
| R1-13 | Input availability | current operator | SHOULD | Represent unknown inputs explicitly |
| R1-14 | Input availability | current operator | SHOULD | Reject malformed dates before sequencing |
| R1-15 | Input availability | current operator | SHOULD | Preserve provided counterexamples |
| R1-16 | Input availability | current operator | SHOULD | Separate user statements from assistant assumptions |
| R1-17 | Option creation | source owner | MUST | Include the strongest ordinary continuation |
| R1-18 | Option creation | source owner | MUST | Include a no-change candidate where feasible |
| R1-19 | Option creation | source owner | MUST | Include a preparation candidate |
| R1-20 | Option creation | source owner | MUST | Include a representation change candidate |
| R1-21 | Option creation | source owner | SHOULD | Include a timing change candidate |
| R1-22 | Option creation | source owner | SHOULD | Include a resource change candidate |
| R1-23 | Option creation | source owner | SHOULD | Include a coordination change candidate |
| R1-24 | Option creation | source owner | SHOULD | Preserve an unconventional derived alternative |
| R1-25 | Evidence fit | evidence reviewer | MUST | State each option input conditions |
| R1-26 | Evidence fit | evidence reviewer | MUST | State evidence population or constructed scope |
| R1-27 | Evidence fit | evidence reviewer | MUST | Separate observation from prediction |
| R1-28 | Evidence fit | evidence reviewer | MUST | Separate performance from explanation |
| R1-29 | Evidence fit | evidence reviewer | SHOULD | Retain negative evidence |
| R1-30 | Evidence fit | evidence reviewer | SHOULD | Reject transfer beyond measured setting as unproven |
| R1-31 | Evidence fit | evidence reviewer | SHOULD | Preserve unresolved causal attribution |
| R1-32 | Evidence fit | evidence reviewer | SHOULD | Link a consequence to its performed operation |
| R1-33 | Action constraints | action executor | MUST | Represent an explicit budget |
| R1-34 | Action constraints | action executor | MUST | Include preparation cost in bundle cost |
| R1-35 | Action constraints | action executor | MUST | Represent resource exclusivity |
| R1-36 | Action constraints | action executor | MUST | Represent required authority |
| R1-37 | Action constraints | action executor | SHOULD | Represent task deadline |
| R1-38 | Action constraints | action executor | SHOULD | Preserve prerequisites in order |
| R1-39 | Action constraints | action executor | SHOULD | Detect a cycle in action dependencies |
| R1-40 | Action constraints | action executor | SHOULD | Reject a missing prerequisite at commitment |
| R1-41 | Choice criteria | affected person | MUST | Retain criterion version |
| R1-42 | Choice criteria | affected person | MUST | Retain criterion owner |
| R1-43 | Choice criteria | affected person | MUST | Distinguish threshold from maximization |
| R1-44 | Choice criteria | affected person | MUST | Keep unmeasured intangibles visible |
| R1-45 | Choice criteria | affected person | SHOULD | Prevent double counting identical effects |
| R1-46 | Choice criteria | affected person | SHOULD | Retain the comparison under previous criteria |
| R1-47 | Choice criteria | affected person | SHOULD | Calculate dominance only on declared dimensions |
| R1-48 | Choice criteria | affected person | SHOULD | Expose the crossover of a weighted decision |
| R1-49 | Execution interface | tool host | MUST | Transmit task revision |
| R1-50 | Execution interface | tool host | MUST | Transmit exact operation input |
| R1-51 | Execution interface | tool host | MUST | Name output contract |
| R1-52 | Execution interface | tool host | MUST | Name endpoint owner |
| R1-53 | Execution interface | tool host | SHOULD | Return explicit error state |
| R1-54 | Execution interface | tool host | SHOULD | Reject an obsolete returned revision |
| R1-55 | Execution interface | tool host | SHOULD | Deduplicate repeated returned identity |
| R1-56 | Execution interface | tool host | SHOULD | Retain an interrupted action state |
| R1-57 | Consequence assessment | maintainer | MUST | Compare expected with actual consequence |
| R1-58 | Consequence assessment | maintainer | MUST | Keep the initial baseline visible |
| R1-59 | Consequence assessment | maintainer | MUST | Separate repair success from first-pass success |
| R1-60 | Consequence assessment | maintainer | MUST | Preserve an unchanged result |
| R1-61 | Consequence assessment | maintainer | SHOULD | Classify a harmful result explicitly |
| R1-62 | Consequence assessment | maintainer | SHOULD | Do not infer human benefit from model agreement |
| R1-63 | Consequence assessment | maintainer | SHOULD | Do not infer weight updates from context change |
| R1-64 | Consequence assessment | maintainer | SHOULD | Retain limits on measurement |
| R1-65 | Revision control | future operator | MUST | Reopen a rejected inference |
| R1-66 | Revision control | future operator | MUST | Invalidate descendants of a removed premise |
| R1-67 | Revision control | future operator | MUST | Retain useful incompatible alternatives |
| R1-68 | Revision control | future operator | MUST | Preserve original sources unchanged |
| R1-69 | Revision control | future operator | SHOULD | Limit automatic retries |
| R1-70 | Revision control | future operator | SHOULD | Allow the current requester to stop |
| R1-71 | Revision control | future operator | SHOULD | Avoid committing an unreviewable irreversible action |
| R1-72 | Revision control | future operator | SHOULD | Record the reason a selected option changed |
| R1-73 | Usability and maintenance | integrator | MUST | Give a direct answer at the relevant level |
| R1-74 | Usability and maintenance | integrator | MUST | Keep useful scope next to recommendation |
| R1-75 | Usability and maintenance | integrator | MUST | Provide a readable local artifact |
| R1-76 | Usability and maintenance | integrator | MUST | Separate provenance from live decision view |
| R1-77 | Usability and maintenance | integrator | SHOULD | Retain an empty-state explanation |
| R1-78 | Usability and maintenance | integrator | SHOULD | Make missing evidence visible in handoff |
| R1-79 | Usability and maintenance | integrator | SHOULD | Provide a boundary case for reuse |
| R1-80 | Usability and maintenance | integrator | SHOULD | Do not turn method bookkeeping into the product flow |

All MUST requirements name a specific retained object, operation or rejection. Their test is an input with and without the named condition, followed by inspection of the output. They are technically implementable within a constructed local selector; human preference validity and future retrieval remain external unresolved conditions. Forty are MUST and forty SHOULD. Optional interface styling is COULD; unauthorized substitution, invented human outcomes and automatic future execution without a mechanism are WON'T.

Eight material conflict checks and resolutions:

| A | B | Tension | Resolution |
|---|---|---|---|
| R1-01 | R1-07 | identity versus ambiguous interpretation | retain alternatives without replacing exact wording |
| R1-09 | R1-10 | missing versus inaccessible | use separate unavailable states |
| R1-17 | R1-24 | ordinary continuation versus unusual option | compare both on input fit |
| R1-25 | R1-30 | reusable fit versus transfer restriction | carry conditions with reuse |
| R1-33 | R1-35 | budget versus exclusivity | joint schedule includes both |
| R1-41 | R1-46 | new criteria versus historical comparison | version the decision |
| R1-49 | R1-54 | dispatch versus obsolete return | recheck revision on return |
| R1-73 | R1-76 | direct answer versus provenance | direct decision view plus source links |

Hidden-input prompts applied: missing input→explicit unavailable state; malformed input→reject before sequencing; 10× scale→bounded index and capacity condition; dependency down→retained blocked state; unexpected user change→new goal revision; first interaction→current goal capture; last interaction→pending handoff; day two→recheck validity; error→reason and prior state; empty→no eligible result; worst-fit user→unseen preference preserved as unknown; embarrassing failure→asserted human outcome without evidence withheld; ordinary competitor→direct useful answer included; hated burden→attention cost counted; stopping→requester can decline. These are design conditions, not outcome observations.

Actual transformation: the concrete plan S+C+E now carries prerequisite S, 55-unit total, exact criterion version and return revision. The earlier output-only candidate lacked these interface obligations. The requirement for resource exclusivity additionally rules out simultaneous use of one exclusive tool by S and E.

The change is applied to the design object. Whether all eighty requirements are worth implementation remains open; the original depth floor broadens discovery but does not mandate a bloated production product.

Actual mind change: The concrete design now has an explicit resource-exclusivity rejection.

Benefit: The changed case now has a definite outcome under the specified boundary. Eighty listed requirements alone are not evidence of an implemented system.

Verdict: KEEP

Organization: Category tables expose missing boundaries; the next architecture groups these conditions by owner rather than reproducing eighty independent services.

Next attempts: Prototype one boundary; remove a low-value requirement; obtain missing stakeholder preference evidence.
