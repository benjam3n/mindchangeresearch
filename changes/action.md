# Action

## Prerequisite order

Possessing every required component does not make an action executable when its prerequisites arrive too late.

1. List the actual operations and the result each dependent operation consumes.
2. Place each producer before its dependent operation; retain unrelated operations as unordered until another condition determines their order.
3. If dependencies form a cycle, identify the unavailable starting condition instead of inventing a valid sequence.
4. Check availability at the handoff and distinguish the ordered plan from completed execution.

When rollback depends on a rebuilt read index, {rebuild, rollback} and {rollback, rebuild} contain the same operations but only the first order satisfies that dependency. A completed plan still does not establish that either operation occurred.

The ordering relation is explicit in the existing finite retrieval case. No real rollback is requested or reported here.

[Conditional retrieval and changed-actor transfer](../post-allocation/cycle-01/memory-capability/02-acr-retrieval.md).

## Starting and stopping

Initiation, continuation, interruption, and termination are different controls. A strong intention supplies none of their execution receipts by itself.

1. For the named action, separate the condition that permits starting from the event that actually starts it.
2. Identify the condition that requires continuation and the condition that requires interruption or termination.
3. Locate the actor or mechanism able to issue each control, including a missing control rather than calling it low motivation.
4. Record whether the control occurred and whether the intended process responded; a command and its effect can differ.

A model can produce a relocation instruction while lacking an actuator. Adding a more emphatic instruction leaves that missing execution edge unchanged. Within a process that is executable, a start command also does not imply that a stop command is available.

Capability distinctions and a nonexecution boundary are established in the records. Reliable control of a particular human action requires that action's actual mechanisms and observations.

[Recipe specification and execution](../post-allocation/cycle-03/capability/01-spg-near-guarantee.md).
