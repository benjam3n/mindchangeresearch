Intended mind change: Change a system design by surfacing previously implicit boundary requirements.

# Long-term reuse requirements at system boundaries

Starting judgment: I would begin with the central successful path. The initial design does not yet specify behavior for every missing, changed or expired condition.

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-requirements.md`; current requirements are retained separately in `../sources/systems-requirements.requirements.txt`.

Depth: Original 8x floors: 80 requirements, 10 categories, 10 stakeholder roles, 8 conflict checks. The record supplies these; roles are design perspectives rather than fabricated consultations.

System boundary: a retained-result system from creation through reuse and retirement. Inputs are stated goals, evidence and resource conditions. Outputs are eligible choices, rejected transfers and explicit unresolved states. Human preferences are not inferred as measurements; external execution requires its actual host. This is a design specification applied to a constructed case, not an assertion a production system exists.

Stakeholders are ten distinct design roles, not ten interviewed people: requester, current operator, source owner, evidence reviewer, action executor, affected person, tool host, maintainer, future operator, integrator. Requester retains direction; operator needs feasible work; source owner needs source integrity; reviewer needs assessable evidence; executor needs a contract; affected person needs agency; host limits actions; maintainer needs recovery; future operator needs fit; integrator needs explicit dependencies. Interests follow from each role's function and remain revisable.

Eighty specific requirements across ten categories:

| ID | Category | Role | Priority | Required behavior |
|---|---|---|---|---|
| R2-01 | Retention identity | requester | MUST | Assign stable identity to a retained result |
| R2-02 | Retention identity | requester | MUST | Preserve result creation context |
| R2-03 | Retention identity | requester | MUST | Retain actor type with result |
| R2-04 | Retention identity | requester | MUST | Retain original goal wording |
| R2-05 | Retention identity | requester | SHOULD | Preserve source edition identity |
| R2-06 | Retention identity | requester | SHOULD | Preserve condition under which result helped |
| R2-07 | Retention identity | requester | SHOULD | Preserve observed negative case |
| R2-08 | Retention identity | requester | SHOULD | Distinguish a retained proposal from observed benefit |
| R2-09 | Future retrieval | current operator | MUST | Index by a concrete reuse trigger |
| R2-10 | Future retrieval | current operator | MUST | Return original evidence with retrieved result |
| R2-11 | Future retrieval | current operator | MUST | Return scope before reapplication |
| R2-12 | Future retrieval | current operator | MUST | Return criterion version |
| R2-13 | Future retrieval | current operator | SHOULD | Allow a query to return no match |
| R2-14 | Future retrieval | current operator | SHOULD | Distinguish absent from deleted entries |
| R2-15 | Future retrieval | current operator | SHOULD | Detect a missing retained artifact |
| R2-16 | Future retrieval | current operator | SHOULD | Do not claim retrieval from saving alone |
| R2-17 | Temporal validity | source owner | MUST | Retain the observation date |
| R2-18 | Temporal validity | source owner | MUST | State a validity window when known |
| R2-19 | Temporal validity | source owner | MUST | Represent unknown durability |
| R2-20 | Temporal validity | source owner | MUST | Flag a changed environment |
| R2-21 | Temporal validity | source owner | SHOULD | Flag a changed goal |
| R2-22 | Temporal validity | source owner | SHOULD | Flag a changed authority |
| R2-23 | Temporal validity | source owner | SHOULD | Flag a changed input format |
| R2-24 | Temporal validity | source owner | SHOULD | Keep historical truth separate from present fit |
| R2-25 | Long-term resources | evidence reviewer | MUST | Count recurring maintenance separately |
| R2-26 | Long-term resources | evidence reviewer | MUST | Retain setup versus per-use cost |
| R2-27 | Long-term resources | evidence reviewer | MUST | Retain the recurrence crossover |
| R2-28 | Long-term resources | evidence reviewer | MUST | Represent retention capacity |
| R2-29 | Long-term resources | evidence reviewer | SHOULD | Represent restoration cost |
| R2-30 | Long-term resources | evidence reviewer | SHOULD | Represent deletion reversibility |
| R2-31 | Long-term resources | evidence reviewer | SHOULD | Represent migration effort |
| R2-32 | Long-term resources | evidence reviewer | SHOULD | Do not assume repeated use will occur |
| R2-33 | Learning evidence | action executor | MUST | Record the next actual recurrence |
| R2-34 | Learning evidence | action executor | MUST | Record whether retrieval happened |
| R2-35 | Learning evidence | action executor | MUST | Record whether eligibility was accepted |
| R2-36 | Learning evidence | action executor | MUST | Record the performed operation at recurrence |
| R2-37 | Learning evidence | action executor | SHOULD | Record the observed recurrence consequence |
| R2-38 | Learning evidence | action executor | SHOULD | Retain competing causes of recurrence success |
| R2-39 | Learning evidence | action executor | SHOULD | Preserve a failed transfer |
| R2-40 | Learning evidence | action executor | SHOULD | Do not treat repetition of wording as transfer |
| R2-41 | Criteria evolution | affected person | MUST | Preserve earlier criterion weights |
| R2-42 | Criteria evolution | affected person | MUST | Retain the reason a criterion changed |
| R2-43 | Criteria evolution | affected person | MUST | Name who authorized criterion revision |
| R2-44 | Criteria evolution | affected person | MUST | Recompute old options under new criteria separately |
| R2-45 | Criteria evolution | affected person | SHOULD | Preserve old comparison results |
| R2-46 | Criteria evolution | affected person | SHOULD | Identify a new hard constraint |
| R2-47 | Criteria evolution | affected person | SHOULD | Test whether a new criterion is merely outcome rationalization |
| R2-48 | Criteria evolution | affected person | SHOULD | Keep disagreement about values visible |
| R2-49 | Interface evolution | tool host | MUST | Record reader format version |
| R2-50 | Interface evolution | tool host | MUST | Maintain an explicit migration mapping |
| R2-51 | Interface evolution | tool host | MUST | Reject unknown incompatible versions |
| R2-52 | Interface evolution | tool host | MUST | Preserve original bytes during migration |
| R2-53 | Interface evolution | tool host | SHOULD | Retain semantic exceptions across conversion |
| R2-54 | Interface evolution | tool host | SHOULD | Distinguish portable description from executable command |
| R2-55 | Interface evolution | tool host | SHOULD | Verify endpoint availability at execution |
| R2-56 | Interface evolution | tool host | SHOULD | Do not forecast host capability without evidence |
| R2-57 | Coordination continuity | maintainer | MUST | Name the current accountable owner |
| R2-58 | Coordination continuity | maintainer | MUST | Transfer pending status explicitly |
| R2-59 | Coordination continuity | maintainer | MUST | Retain work already performed |
| R2-60 | Coordination continuity | maintainer | MUST | Retain blocked prerequisites |
| R2-61 | Coordination continuity | maintainer | SHOULD | Reject late work for obsolete goals |
| R2-62 | Coordination continuity | maintainer | SHOULD | Retain cancellation state |
| R2-63 | Coordination continuity | maintainer | SHOULD | Avoid duplicate downstream action after retry |
| R2-64 | Coordination continuity | maintainer | SHOULD | Name a concrete escalation endpoint |
| R2-65 | Reliability and recovery | future operator | MUST | Keep a recoverable previous accepted state |
| R2-66 | Reliability and recovery | future operator | MUST | Detect a damaged evidence reference |
| R2-67 | Reliability and recovery | future operator | MUST | Distinguish copy redundancy from independent evidence |
| R2-68 | Reliability and recovery | future operator | MUST | Represent common-cause failure |
| R2-69 | Reliability and recovery | future operator | SHOULD | Separate repair time from waiting time |
| R2-70 | Reliability and recovery | future operator | SHOULD | Test recovery on a constructed missing input |
| R2-71 | Reliability and recovery | future operator | SHOULD | Retain both failure and repair evidence |
| R2-72 | Reliability and recovery | future operator | SHOULD | Expose unknown operational reliability |
| R2-73 | Agency and retirement | integrator | MUST | Allow a user to decline reuse |
| R2-74 | Agency and retirement | integrator | MUST | Allow goal change without rewriting history |
| R2-75 | Agency and retirement | integrator | MUST | Avoid preserving unwanted human attributes |
| R2-76 | Agency and retirement | integrator | MUST | Retire a contradicted recommendation |
| R2-77 | Agency and retirement | integrator | SHOULD | Keep a retirement reason |
| R2-78 | Agency and retirement | integrator | SHOULD | Retain needed provenance for retired entries |
| R2-79 | Agency and retirement | integrator | SHOULD | Compare retention against reconstruction burden |
| R2-80 | Agency and retirement | integrator | SHOULD | Do not execute an unactioned future promise |

All MUST requirements name a specific retained object, operation or rejection. Their test is an input with and without the named condition, followed by inspection of the output. They are technically implementable within a constructed local selector; human preference validity and future retrieval remain external unresolved conditions. Forty are MUST and forty SHOULD. Optional interface styling is COULD; unauthorized substitution, invented human outcomes and automatic future execution without a mechanism are WON'T.

Eight material conflict checks and resolutions:

| A | B | Tension | Resolution |
|---|---|---|---|
| R2-01 | R2-07 | identity versus ambiguous interpretation | retain alternatives without replacing exact wording |
| R2-09 | R2-10 | missing versus inaccessible | use separate unavailable states |
| R2-17 | R2-24 | ordinary continuation versus unusual option | compare both on input fit |
| R2-25 | R2-30 | reusable fit versus transfer restriction | carry conditions with reuse |
| R2-33 | R2-35 | budget versus exclusivity | joint schedule includes both |
| R2-41 | R2-46 | new criteria versus historical comparison | version the decision |
| R2-49 | R2-54 | dispatch versus obsolete return | recheck revision on return |
| R2-73 | R2-76 | direct answer versus provenance | direct decision view plus source links |

Hidden-input prompts applied: missing input→explicit unavailable state; malformed input→reject before sequencing; 10× scale→bounded index and capacity condition; dependency down→retained blocked state; unexpected user change→new goal revision; first interaction→current goal capture; last interaction→pending handoff; day two→recheck validity; error→reason and prior state; empty→no eligible result; worst-fit user→unseen preference preserved as unknown; embarrassing failure→asserted human outcome without evidence withheld; ordinary competitor→direct useful answer included; hated burden→attention cost counted; stopping→requester can decline. These are design conditions, not outcome observations.

Actual transformation: the retained lookup entry now carries three distinct states: historical result remains valid, current-fit unknown after an environment change, and future retrieval unobserved. A changed reader version marks the executable command unavailable while preserving the portable description.

The change is applied to the design object. Whether all eighty requirements are worth implementation remains open; the original depth floor broadens discovery but does not mandate a bloated production product.

Actual mind change: The retained-result design now preserves historical truth while marking present-fit and executable continuation independently.

Benefit: The changed case now has a definite outcome under the specified boundary. Eighty listed requirements alone are not evidence of an implemented system.

Verdict: UNRESOLVED

Organization: Category tables expose missing boundaries; the next architecture groups these conditions by owner rather than reproducing eighty independent services.

Next attempts: Prototype one boundary; remove a low-value requirement; obtain missing stakeholder preference evidence.
