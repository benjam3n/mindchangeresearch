# Change when an option remains available

Use when waiting for information changes what can subsequently be done. The object of inquiry is the policy over time, not just the accuracy of the eventual belief.

## Operations and exact example

1. Record when information arrives and when each action expires. Include reservations or other actions that alter those dates.
2. Write the available policies as actual action sequences. Do not give a waiting policy a fallback it will have lost.
3. Evaluate each sequence under the declared outcome criterion, including information and reservation costs. If that criterion changes, retain the old comparison and investigate the new one separately.
4. Select or retain ties within the supplied model. Where relevant probabilities or available reservations are unknown, seek those inputs or state conditional decisions.

The [existing timing case](../gosm/01-time-and-options.md) stipulates a current guaranteed payoff of 5, a later favorable payoff of 8 with probability p, a test costing 1, and an additional reservation costing 1 that preserves the guaranteed fallback. The test perfectly identifies the outcome; the agent compares expected net units.

| Policy | Expected net units | Winning region |
| --- | --- | --- |
| Commit now | 5 | p < 2/3 |
| Reserve and test | 3p + 3 | 2/3 < p < 4/5 |
| Test without reservation | 8p − 1 | p > 4/5 |

There are ties at the boundaries. At p = 3/4, the values are 5, 21/4 and 5 respectively: reservation changes the best available policy. At p = 1, reservation wastes a unit: the strongest alternative defeats a universal rule to preserve every option.

The derivation is exact within this constructed case. It neither guarantees a realized payoff nor establishes a universal human preference for the supplied criterion. A new possibility such as creating another fallback would change the policy set; the old optimum would then be an answer about the earlier set.
