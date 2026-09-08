# Preserve the thing an instruction refers to

The [edit record](../representation/047-wre-2.md) supplies `[A:alpha, B:beta, C:gamma]`, requests deletion of original A and tagging of original B, and checks that reordering the list does not change those targets. Its remaining content-precondition case can be resolved directly.

Stable identity does not prove unchanged content. A live record can retain ID B while its text changes from beta to another value. If the requested edit depends on the original text, matching B alone is insufficient. The adequate condition is unique identity plus the relevant expected content, or a revision token whose maintained semantics guarantees that content has not changed. A token that is not reliably updated supplies no such guarantee.

The completed finite edit operation checks every required identity and expected content against one snapshot before mutating anything. If a required record is missing, duplicated, or content-mismatched, it returns the unchanged snapshot. Otherwise it deletes A and tags B by identity. In the implementation, a B-content mismatch leaves the entire input unchanged. This closes the deferred case; it does not claim a general distributed transaction system.

For concurrent writers, a correct preflight can become stale before the write. Preventing that race requires the comparison and mutation to share an atomic boundary or an equivalent enforced version check at commit. Merely storing a version number in a JSON record is not the mechanism. This is the same distinction between a specified field and an implemented operation that the recipe compiler missed.

## Cancellation of one timer need not cancel another

The [timer record](../representation/048-wre-3.md) specifies that the first READY starts a five-second round, duplicates leave its deadline unchanged, CANCEL clears it, and a later READY can start a fresh round. To support independent concurrent rounds, store the active deadline by round identity.

READY(A,3) establishes deadline A=8. READY(B,4) establishes B=9. CANCEL(A,5) removes A's deadline and leaves B=9. A new READY(A,10) establishes A=15. B remains due at time 9. These are performed finite operations in the accompanying implementation.

The independence proof is exact. Let the state be a product XA×XB and let an A-only operation be fA×identityB. Then the B projection of the result equals its original value. An analogous B-only operation commutes with it. The proof requires that the operations truly leave the other component and any shared validity conditions untouched; shared resources or a global stop condition would change the model.

A session-global “READY has already been seen” flag violates the required restart behavior. A global cancellation bit violates the independent-round behavior. More careful use of those representations cannot supply the distinctions they erased.

## The same issue appears in research claims

An observation under criterion C0 remains an observation under C0. If C1 is later adopted, the old raw data may be reevaluated under C1 when they contain the needed information. The previous verdict cannot simply be relabeled as if C1 governed the earlier evaluation. Preserving identity makes legitimate revision possible; it does not require keeping the old criterion forever.

Likewise, identical final documents do not establish identical histories of authorized operations. A process can pass through a prohibited intermediate state and later restore the same final bytes. A final-state check establishes final-state equality; a trajectory requirement needs evidence about the trajectory.
