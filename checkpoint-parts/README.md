Intended mind change: Preserve every corpus byte in the repository despite the bootstrap transport's single-object size limit.

# Complete checkpoint parts

The eleven files `part-000` through `part-010` are consecutive binary pieces of `Mind_Change_Research_Checkpoint.zip`.

From the repository root, run:

```bash
python3 checkpoint-parts/reassemble.py
```

Expected SHA-256:

`7ba425b197be8d38ba9715873464dd0ba2eca43e2da3aeb985ab5ffda83fba6b`

The ZIP contains 1,465 files and must pass a complete ZIP integrity test. `Checkpoint_Manifest.sha256` inside and outside the ZIP hashes the extracted corpus paths.

Actual mind change: The archive is transferred as verified parts rather than omitted or falsely described as a single committed object.

Benefit: The repository contains the complete accumulated corpus, not only a summary.

Verdict: KEEP after remote part hashes and reconstruction are verified.

Organization: Keep the parts immutable for this checkpoint; replace them together for a later rolling checkpoint.

Next attempts: Verify remote blob hashes; reconstruct locally from repository data; replace with one archive if direct git transport becomes available.
