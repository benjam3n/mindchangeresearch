# Recover evidence lineage before updating confidence

Use when multiple signals may be descendants of one observation. The sought change is from counting reports to interpreting what independent information they carry. This route assumes a probabilistic question is appropriate; it does not govern all disagreement.

## Operations

1. For each signal, record the underlying observation identifier, who observed it, and any copying or transformation. A different filename or messenger is not evidence of a different event.
2. Draw or list the parent relation. Copies with no additional conditional information share their originating event. Distinct events still require a dependence assumption; different IDs alone do not establish independence.
3. Where the prior and a defensible joint likelihood are supplied, update once using that joint likelihood. Multiply separate likelihood ratios only under the required conditional-independence assumptions under both hypotheses.
4. Where lineage or dependence is unknown, keep that uncertainty explicit. Compute named conditional cases if useful. Do not silently choose the case that produces the desired action.
5. Apply the resulting confidence to the declared decision rule. If the decision criterion is itself disputed, preserve the numerical result and open that separate dispute.

## Worked case and boundary

Stipulate prior probability 1/10 and likelihood ratio 4 for one underlying observation. Prior odds are 1/9; posterior odds are 4/9; posterior probability is 4/13. A copied second report carrying no further information leaves 4/13 unchanged.

If there are instead two observations that are conditionally independent under both hypotheses, each with likelihood ratio 4, posterior odds are 16/9 and probability is 16/25 = 0.64. At a stipulated action threshold of 1/2, these cases lead to different actions. If lineage is unknown, these two calculations are conditional alternatives, not a proved exhaustive interval for all dependence structures.

The strongest simple alternative—count every source separately—is correct under the second set of assumptions and wrong under the first. The repair is to establish information structure, not universally discount corroboration.

## Outcome and limits

The [existing belief case](../post-allocation/cycle-02/belief/01-pbr-correlated-evidence.md) and [later compiler comparison](../post-allocation/cycle-03/consolidation-03-recipe-compiler.md) support this local distinction. The arithmetic can be guaranteed under its supplied assumptions. Neither the likelihood ratios nor an actual person's confidence change are established by the arithmetic.

If the report's identity or meaning changes during examination, rebuild the observation description before reusing the update. A probabilistic answer can remain correct while the larger question becomes inadequate.
