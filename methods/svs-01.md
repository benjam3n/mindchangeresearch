Intended mind change: Represent unknown route conditions as available observation and branch operations instead of comparative adjectives.

Actual starting judgment: The prose note captures the broad trade-off, but it does not specify an operation for each observed state; I would keep the map in working context and choose manually.

Original: ../sources/methods-svs.original.md. Separate requirements receipt: ../sources/methods-svs.requirements.txt.

Depth: No numerical 8x rule in SVS. Original minimum two variations per operation is exceeded with four per each of seven operations; all twenty-eight receive feasibility/value/exploration assessments and a selected artifact is used.

CURRENT SOLUTION: “North is shorter; East is dependable.” Components: route labels, comparative descriptions, unknown bridge state outside the note, one-minute sign observation, route durations. Concrete input is the same finite map preserved in wsib-01.

Twenty-eight distinct transformations, four per SCAMPER operation; compilation removes no duplicates because each changes a distinct component/use/order.

| ID | Operation | Variation | Feasible | Valuable | Explore | Assessment |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Substitute | Replace route adjectives with state/action pairs | yes | yes | yes | Preserves bridge condition. |
| 2 | Substitute | Replace prose with one unconditional North arrow | yes | no | no | Loses closed-bridge branch. |
| 3 | Substitute | Replace unknown with 50% open | yes | no | no | Invents a probability. |
| 4 | Substitute | Replace route names with N/E labels | yes | no | no | Shorter but adds decoding. |
| 5 | Combine | Join sign-reading action to two route outcomes | yes | yes | yes | Includes the evidence acquisition step. |
| 6 | Combine | Join travel times to every branch | yes | yes | yes | Makes total time 9 or 13 visible. |
| 7 | Combine | Blend North/East into average 10 | yes | no | no | No physical route has that duration. |
| 8 | Combine | Pair decision rule with stale-sign exception | yes | yes | yes | Keeps trust boundary at the action. |
| 9 | Adapt | Use a dispatch table keyed by sign state | yes | yes | yes | Can drive a later operation exactly. |
| 10 | Adapt | Use a traffic-light color code only | yes | no | no | Colors omit what is being observed. |
| 11 | Adapt | Use a map legend for B-open/B-closed | yes | yes | yes | Makes states explicit but still needs action. |
| 12 | Adapt | Use an insurance premium metaphor | yes | no | no | No premium or probability is given. |
| 13 | Modify | Magnify unknown bridge state as first line | yes | yes | yes | Moves attention from speed to unresolved condition. |
| 14 | Modify | Shrink to “Read B sign; open→N, closed→E” | yes | yes | yes | Preserves full operative rule. |
| 15 | Modify | Make guaranteed East outcome bold | yes | maybe | no | Useful when sign cannot be trusted. |
| 16 | Modify | Add ten confidence levels | yes | no | no | Unsupported granularity. |
| 17 | Put to other use | Use branch map to check a later route choice | yes | yes | yes | A North recommendation under closed becomes detectable. |
| 18 | Put to other use | Use table as a sensor interface | yes | yes | yes | Machine-readable state can select an action. |
| 19 | Put to other use | Use it as a real walking recommendation | no | no | no | This is a constructed map, not a real location. |
| 20 | Put to other use | Use timings to estimate human stress | yes | no | no | No stress observations exist. |
| 21 | Eliminate | Remove comparative adjectives | yes | yes | yes | No loss after exact conditions are present. |
| 22 | Eliminate | Remove the sign-reading step | yes | no | no | Then the state used by the branch is absent. |
| 23 | Eliminate | Remove unsupported probability field | yes | yes | yes | Avoids pretending a prior was supplied. |
| 24 | Eliminate | Remove the closed branch | yes | no | no | Unknown cannot safely become open. |
| 25 | Reverse | Place observation before route choice | yes | yes | yes | Information acquisition becomes the first action. |
| 26 | Reverse | Start from failure: B closed means East | yes | yes | yes | Exposes the safety fallback first. |
| 27 | Reverse | Choose North then inspect sign | yes | no | no | The chosen route precedes its needed information. |
| 28 | Reverse | State exception before normal branch | yes | maybe | no | Best if sign trust is the live concern. |

Shortlist, by current impact: 9 dispatch table + 5 observation step; 14 compact branching sentence; 8 stale-sign exception. Variations 7 and 3 are rejected because averaging routes or inventing a probability changes the problem. All other decisions are retained in the table.

Selected artifact, constructed now:

```json
{"first_action":"read_bridge_sign","observation_cost_minutes":1,"branches":{"open":{"route":"North","travel_minutes":8},"closed":{"route":"East","travel_minutes":12}},"unavailable_or_untrusted_sign":{"route":"East","travel_minutes":12}}
```

The fallback is supported by East’s independence from B. It adds no claim that the sign is actually unreliable; it defines a branch for a distinct input. With the supplied reliable sign, total duration is 9 minutes if open or 13 if closed. Without reading, East is 12. Therefore observation is not uniformly faster: it gains 3 minutes when open and costs 1 when closed. The current input does not provide a prior or criterion that makes reading categorically optimal in expectation. This trade-off remains explicit rather than calling every information step beneficial.

Actual later operation: route-dispatch.json was read as a state/action object. On closed it returns East/12 travel minutes; on open it returns North/8; on unavailable it returns East/12 without claiming to have read anything. A second model task changes the letters and times (West 6 if gate G open; South 10 regardless); the representation yields W when open and S when closed. The structured branch is now an available operation that the initial two-adjective note did not define. The goal “minimize expected total time” remains unresolved without a prior.

Certificate: changed artifact supports exact state-conditioned dispatch; decisive evidence is the three executed table lookups and the renamed-map application. Strongest contrary result: no unconditional advantage of reading the sign, because closed costs a minute. That defeats an information-is-always-beneficial claim, not the value of retaining the branches.

Actual mind change: The route note became a reusable state/action object. Uncertainty remains a branch variable; it is no longer an unstated condition beneath “shorter.”

Benefit: The actual artifact supports three exact later lookups and a renamed-map application. This is a narrow representation/capability benefit. It does not establish that observing is always optimal or that a human travelled faster.

Verdict: KEEP

Organization: The compact policy is used operationally; the full variation register remains for provenance. A one-line unconditional arrow loses the boundary and is rejected.

Next attempts: Vary uncertainty where evidence has a cost; test a creative representation with no action goal; compare a non-numeric ambiguity map.
