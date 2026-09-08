# VCD — privacy and auditability without scalar compensation

Intended mind change: Replace a single weighted score with a navigable policy when privacy and auditability impose different noncompensatory constraints.

Actual starting judgment: I expected one weighted retention score to rank the records; I had not decided whether high audit value could compensate for unnecessary named medical data.

Concrete input: `frozen-inputs.md`, VCD case with R1–R4 and later R5.

## Conflict detection and name

Conflict present: yes.

Named conflict: reproducible auditability versus exposure-minimizing privacy.

- Auditability requires enough decision input, rationale, rejection history, and provenance to reproduce or challenge a conclusion.
- Privacy requires removing identity and sensitive attributes not necessary for that reproduction or an authorized follow-up.

## Conflict analysis

The values conflict only where a field is both identity-bearing/sensitive and causally necessary for audit or an authorized follow-up. Whole-record retention versus deletion is a false dichotomy because content, identity, contact route, and custody can be transformed separately.

The tension is partly temporal: follow-up contact may be needed briefly; decision rationale may need durable retention. It is also authority-dependent: a future desire to contact someone does not by itself authorize durable contact-data retention.

## Navigation strategies evaluated

| Strategy | Result |
|---|---|
| Weighted sum `audit − privacy risk` | rejected for policy use; can let high audit value compensate for avoidable sensitive exposure |
| Delete every risky record | rejected; destroys necessary evidence and dissent history |
| Retain every high-audit record unchanged | rejected; preserves unnecessary identity fields |
| Field separation + minimization + time-bounded contact escrow | selected |

## Concrete policy

1. Separate decision content, identity, contact route, and custody metadata.
2. Retain decision content only when needed to reproduce, contest, or explain the decision.
3. Remove identity and sensitive attributes unless they are necessary for that retained function.
4. Keep contact data only under an explicit follow-up purpose, authority, and expiry; otherwise delete it.
5. Keep a provenance pointer that proves which transformation occurred without reintroducing the removed personal data.

Application:

| Record | Decision |
|---|---|
| R1 public rationale | retain as supplied |
| R2 named irrelevant medical detail | delete the detail; retain only a tombstone stating that irrelevant personal data was excluded if exclusion itself must be auditable |
| R3 pseudonymous necessary evidence | retain pseudonymous content and transformation provenance |
| R4 contact data for possible follow-up | do not retain absent authorized purpose and expiry; if authorized, escrow separately until expiry |

Success criteria: a reviewer can reproduce the accepted decision using retained content; unnecessary named medical information is absent; every retained identity/contact field has purpose, authority, and expiry; deletion and transformation actions are traceable.

Risks and mitigations: over-redaction is tested by reproduction; re-identification is tested by combination review; function creep is constrained by expiry and purpose; provenance leakage is checked before release.

Pivot triggers: reproduction fails; legal/contractual retention duty is supplied; a named person authorizes follow-up; pseudonymous content remains identifying when combined with other fields.

Check-in points: immediately after transformation, before release, at contact-data expiry, and when the decision is challenged.

## Distinct later use

R5 is anonymous dissent whose content is required to understand a rejected option. The policy retains the dissent content and its relation to the rejected option, not an identity it never had. A whole-record “privacy risk” score would add no useful decision; field/function separation directly answers the case.

## Outcome

Actual mind change: I changed from scalar record ranking to a field-level, purpose-and-expiry policy. The two values were not averaged; their conflict was reduced by transforming the object and separating time horizons.

Benefit or harm: The policy preserves R1, R3, and R5’s audit function while excluding R2’s unnecessary named detail and gating R4’s contact data. No real retention or deletion occurred.

Verdict: KEEP — useful within the constructed record set; legal sufficiency and stakeholder acceptance remain unresolved.

Content assessment: Both values, incompatibility, false dichotomy, strategies, decisions, criteria, risks, and pivots are explicit.

Organization assessment: `function → field → authority → expiry` prevented compensatory scoring from hiding a hard privacy boundary.

Next attempts: Add a lawful-retention requirement that conflicts with deletion; test re-identification across multiple benign fields; compare field-level policy with differential-access controls; obtain stakeholder review before claiming human value alignment.
