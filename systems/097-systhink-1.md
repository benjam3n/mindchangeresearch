Intended mind change: Change a system intervention after tracing its stock, flow and delayed effects.

# Capacity changes in a ten-stock operation system

Starting judgment: More input preparation appears productive, but the relationship between generated work and completed useful output is not established by input volume.

Actor and scope: The assistant's current working representation and operations in this systems line. This record does not establish human effects, model-weight changes, or transfer to another session.

Source: `../sources/systems-systhink.md`; current requirements are retained separately in `../sources/systems-systhink.requirements.txt`.

Depth: Original 8x floors: 10 explicit stocks, 8 feedback-loop checks, 5 delays, 8 leverage points, 8 archetype checks. Loop activity is distinguished from merely possible topology; forty cycles are executed for four policies.

System is a constructed ten-queue operation pipeline. Time horizon is forty discrete cycles. Every initial stock is zero; arrivals and capacities are stipulated, not measured human or model productivity. Boundary includes all ten queues, inflow, completion and release controls. An excluded upstream source cannot change the modeled bottleneck unless it changes its capacity.

Ten stocks with corresponding inflow/outflow: unread input, extracted material, normalized cases, candidate operations, eligibility queue, feasible bundles, authorized work, pending returns, assessed outputs, retention queue. Queue i receives the previous queue's completed transfer and loses its own transfer; the first receives exogenous arrivals, the last drains to completed output. The exact simultaneous recurrence and every stock/flow value are executed in `pipeline-dynamics.json`. Each queue's fill/drain time is determined by integer capacity and present stock; no metaphorical human capacity is inferred.

Eight explicitly checked feedback paths:

L1: stock extracted material increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.
L2: stock normalized cases increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.
L3: stock candidate operations increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.
L4: stock eligibility queue increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.
L5: stock feasible bundles increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.
L6: stock authorized work increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.
L7: stock pending returns increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.
L8: stock assessed outputs increases → free receiving space decreases (−) → upstream release decreases (+ link from space) → that stock inflow decreases (+); one negative edge, balancing, one-cycle delay, active only in the bounded variant.

Five delays: input→extraction, extraction→normalization, candidate→eligibility, authorized work→returned evidence and assessed output→retention each require at least one cycle in the model. The full path requires multiple cycles; output is therefore zero early even when input enters. Actors who compared output at cycle1 would misattribute pipeline latency to no capacity; this is a model implication, not a claim about real users.

Archetype checks: limits-to-growth matches finite bottleneck capacity; growth-and-underinvestment matches only the stipulated capacity mismatch; commons does not match because one allocator controls all queues; success-to-successful lacks competing reward feedback; escalation lacks responding parties; shifting-the-burden lacks a damaged fundamental stock; fixes-that-fail matches extra arrivals if the target is backlog reduction; eroding-goals is absent because completion criterion stays constant.

Eight leverage points: (1) change goal from arrivals to completions—useful if goal was mistakenly arrival volume; (2) alter bottleneck capacity—directly changes modeled throughput; (3) change release-loop structure—bounds accumulation; (4) expose downstream queue lengths—supplies release signal; (5) constrain admission—reduces overload; (6) move buffer capacity—changes where work waits; (7) shorten one transfer delay—changes latency before steady output; (8) adjust exogenous arrival rate—changes backlog when downstream capacity is fixed. All are feasible model interventions; actual host changes would require capability evidence. Ranking for this case follows computed effect, not the source hierarchy alone.

Observed model behavior: baseline completion=31, backlog=89; intervention completion=62, backlog=58. Increasing arrivals from3 to5 produces 31 completions and backlog 169, so extra generation does not solve the one-unit bottleneck.

Side effects: first-order capacity raises eligible flow; second-order downstream queues receive more completed eligibility; third-order finished output increases after transfer delay. Compensating response: a different downstream capacity would become the new bottleneck; bounded admission can idle the line if its buffer is too small. The intervention does not establish universal throughput or attention benefits.

Actual selection for the model: increase the bottleneck from1 to2 instead of increasing source arrivals. The exact output comparison is performed rather than forecast.

Actual mind change: The model selects a bottleneck capacity increase.

Benefit: The forty-cycle executed model separates changes in completion from changes in accumulation. All rates remain stipulated model inputs.

Verdict: KEEP

Organization: Stock/flow traces retain accumulated work and latency; an input-count dashboard omits both.

Next attempts: Move the bottleneck; reduce the buffer; test time-varying arrivals.
