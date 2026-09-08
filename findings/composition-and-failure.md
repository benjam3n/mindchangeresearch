# Repair the condition that actually makes the whole fail

The [fault-gate correction](../inquiry/13-fctl-fault-gates.md) distinguishes failure caused by an AND from failure caused by an OR. If failure is a∧b, making either failure input false prevents that conjunction. If failure is a∨b, both failure inputs must be false. Confusing the gate reverses the repair rule.

Mixed trees do not require a new intuition for every arrangement. Suppose failure is a monotone Boolean function F of component-failure variables. A repair set R forces its variables false. It is sufficient for the present state precisely when evaluating F after those assignments returns false. It is inclusion-minimal if removing any repair from R makes it insufficient.

For F=(a∧b)∨(a∧c), distributivity gives F=a∧(b∨c). When all three failure variables are true, the minimal repair sets are {a} and {b,c}. Repairing b alone leaves a∧c true; repairing c alone leaves a∧b true. Repairing a fixes both branches because it is shared. Treating the two occurrences of a as independent causes loses this structure.

Equivalently, express a monotone F as a disjunction of its inclusion-minimal sufficient failure sets. A repair must intersect every currently active sufficient failure set. Minimal repairs are minimal hitting sets of those sets. This is a logical statement: it does not assume probabilistic independence. Probability calculations over the same tree would require a separately justified joint model.

The finite implementation enumerates repair subsets in increasing size, evaluates F after the repair, and retains only sufficient subsets having no already retained sufficient subset. Every returned set is sufficient and minimal; every minimal set is encountered and retained. If repair costs are supplied, minimizing cost over the retained sets is justified only under the supplied cost model. Inclusion-minimal does not mean cheapest when different repairs have different costs.

## Success prerequisites reverse the polarity

For success S=k∧r∧o, all three necessary inputs must hold. Improving k does nothing to S while r remains false. That does not show the k intervention was ineffective at changing k; it shows k was insufficient for the whole success condition. Local effect, contribution to a conjunction, and final success are distinct propositions.

For success S=k∨r, either route can suffice. Requiring both adds an unnecessary condition. Thus the generic instruction “find all missing prerequisites” must distinguish necessary conjunctions from alternative routes. An untyped dependency diagram cannot decide that distinction.

These conclusions extend directly to the catalog. A cue cannot make an unavailable action available; additional explanation cannot replace a missing execution path; a second route can make repairing the original route unnecessary. Which statement applies follows from the declared relationship among conditions, not the psychological name of the intervention.

## Individually beneficial operations need not compose

Let B(X) be the value of a set or sequence of changes X under an explicit criterion. Knowing B({a})>B(∅) and B({b})>B(∅) does not determine B({a,b}). For a concrete countermodel, let B(∅)=0, B({a})=2, B({b})=2, and B({a,b})=−1. The individual premises hold while the composition is harmful. A different model with B({a,b})=7 has the same individual facts and a beneficial interaction. The interaction is therefore not identified by the individual facts.

When operators are specified, composition can sometimes be settled deductively. If a deletes an input needed by b, a followed by b fails that prerequisite. If both write the same field from different starting versions, independent correctness checks do not establish a compatible merged result. If they act on disjoint state components and their validity conditions do not interact, they commute. These are conditions to derive or inspect, not reasons to presume every combination dangerous.
