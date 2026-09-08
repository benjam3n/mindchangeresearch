# Complete checkpoint recovery

The `part-NNN` files are consecutive binary pieces of the complete research checkpoint. [metadata.json](metadata.json) gives the exact count, sizes, per-part hashes, aggregate archive hash and corpus count for this version.

From the repository root, run:

```bash
python checkpoint-parts/reassemble.py
```

The script verifies every part, the joined archive, every corpus file against the archived manifest, and the archive's exact path set before writing `Mind_Change_Research_Checkpoint.zip`. All research files are also available as native repository paths.

Rebuild the complete accepted checkpoint with `python checkpoint.py`; validate it with `python checkpoint.py --check`. Commit parts and metadata together with the corresponding corpus changes. The transport directory is excluded from the archive to prevent recursive packaging; its integrity is checked separately. See [repository-sync.md](../repository-sync.md).
