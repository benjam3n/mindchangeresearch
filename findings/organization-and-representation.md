# An organization is adequate for the questions it preserves

Let X be a set of objects, r:X→Z their representation, and Q a family of questions, with q(x) the correct answer to question q about object x. Assume the meanings of r and q are specified.

**Every question in Q can be answered exactly from r(x) if and only if r never merges objects that differ on an answer in Q.** Formally:

\[
r(x)=r(y)\ \Longrightarrow\ \forall q\in Q,\ q(x)=q(y).
\]

Necessity: a decoder receiving one identical representation cannot return two different answers to the same question. Sufficiency: for a represented value z, choose any x with r(x)=z and return q(x). The condition makes that answer independent of which preimage is chosen. This is an existence result; efficient computation of the decoder is an additional requirement.

For a finite specified Q, the answer vector `(q1(x),...,qk(x))` induces the coarsest exact partition: objects belong together exactly when all their answers agree. Any adequate representation must separate every pair separated by this vector. It may retain extra distinctions for other purposes. This establishes a minimum in distinguishable classes, not a universal minimum in prose length, human reading time, or interface complexity.

## The earlier graph result extends beyond its eight nodes

The [compression record](../gosm/03-representation-and-loss.md) compares a forward-complete ordered graph with its adjacent-edge chain. For n nodes, both give the same reachability answer on all n(n−1) ordered pairs of distinct nodes. In the complete graph every forward pair has distance one; in the chain only the n−1 adjacent pairs retain that distance. Therefore exactly

\[
\frac{n(n-1)}2-(n-1)=\frac{(n-1)(n-2)}2
\]

forward distances change. At n=8 this gives 21, reproducing the earlier result. The failure is determined by the omitted answer family, not by a vague amount of lost information.

Keeping the chain plus the rule “every earlier node directly connects to every later node” reconstructs the complete graph. Keeping the chain alone does not. A link to a recoverable source can play a similar role in a research index, but only if the reader can actually follow it and recover the required distinction.

## Application to the repository

At baseline commit `07e6af64c65f`, the original repository index contained 48 relative file-link occurrences. Thirty-six occurrences, referring to 35 distinct files, had no corresponding exposed repository path. The bytes existed in the checkpoint archive. That established recoverability, but clicking those links could not supply the cited result. The archive was hash-verified and expanded during this work; concurrent accepted commits also exposed its native paths. The final integration preserves that newer native tree and its additional inquiries and inventories.

The 72-target view answers “what dimensions might change?” The 100-attempt view answers “what operations might be tried?” Skill order answers “what source procedure was used?” Chronology answers “what changed after what?” None is sufficient for all the others. A completed-consequence index answers the additional question the front page previously obscured: “what can I now infer or do because of this research?”

These views should share the same underlying records. Duplicating every claim under every category creates an update problem: one changed qualification can leave several apparently authoritative copies. Generating the target and attempt views from one catalog data file gives them a shared update source, while the imported original remains an explicitly historical snapshot.

## Efficiency includes the reader's reconstruction

For a specified workload, total effort includes creation, retrieval, reconstruction, application, and maintenance. A shorter stored representation can increase retrieval or reconstruction effort. The theorem above checks whether an answer survives at all; a separate cost comparison decides whether the representation is preferable for that workload.

There is consequently no demonstrated universal “best hierarchy” here. There is an exact preservation condition and a concrete organization chosen for the current questions. When the question family changes, the coarsest sufficient partition can change too. The adequate response is a different view over the retained distinctions, not a forced reinterpretation of the new question to fit the old tree.
