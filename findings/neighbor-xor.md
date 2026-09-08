# Exactly which neighbor-XOR rings erase every starting state

The [five-cell exploration](../methods/mrc-03.md) studies the synchronous rule `next[i] = current[i] XOR current[(i+1) mod n]`. It derives the five-cell image and its fifteen-state nonzero cycle, then leaves even widths for later work.

**Every starting state eventually reaches zero if and only if the ring width n is a power of two.** When n=2^k, every state reaches zero in at most n updates. For any other positive n, some starting state eventually enters a nonzero cycle.

Write S for the cyclic shift on n-bit vectors over the field with two elements. The update is T=I+S, where addition is XOR and S^n=I. In characteristic two, `(I+S)^(2^k)=I+S^(2^k)`: the intervening binomial coefficients vanish modulo two, or the identity follows by repeated squaring. If n=2^k, T^n=I+S^n=I+I=0. This proves the sufficient direction for every state, not just a tested seed.

For necessity, represent the cyclic shift by multiplication by x in the quotient ring F2[x]/(x^n−1). If every vector is eventually erased, finite dimension gives a common exponent m with T^m=0: choose the maximum erasure time of a basis, then use linearity. Thus x^n−1 must divide (1+x)^m.

Write n=2^k d with d odd. Over F2,

\[
x^n-1=(x^d-1)^{2^k}.
\]

If d>1, x^d−1=(x+1)q(x), where q is nonconstant and q(1)=1 because d is odd. Hence q has no factor x+1 and cannot divide any power of x+1. This contradicts the required divisibility. Therefore d=1 and n is a power of two.

If n is not a power of two, T is not nilpotent, so at least one state is never erased. The state space is finite and the update deterministic; that trajectory eventually repeats away from zero. A nonzero fixed point is impossible: T(x)=x implies Sx=0, and the shift is invertible. The surviving cycle consequently has length greater than one.

The bound n for a power-of-two width is tight. For a single-bit basis seed e, T^(n−1)e is nonzero: `(1+x)^(n−1)=1+x+...+x^(n−1)` over F2, since n is a power of two. Thus that seed has not vanished before update n. Width one is included: every one-bit seed is erased in one update.

The finite checks in [deductions.py](../tools/deductions.py) enumerate all states for widths one through eight. They check the implemented rule and display nonzero cycles for widths three, five, six, and seven. The algebra, rather than that finite enumeration, establishes the claim for all positive widths.

This result changes the exploratory classification from odd versus even to power-of-two versus other widths. An even width alone does not determine extinction: four and eight erase every seed; six does not. The stronger distinction arose from following the object, without requiring a prior claim about a reader's productivity, interest, or behavior.
