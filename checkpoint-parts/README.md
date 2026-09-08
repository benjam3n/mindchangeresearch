# Complete research checkpoint

The numbered parts reconstruct the complete current corpus, including original sources, receipts, ledgers, rejected and unresolved records, chat material, current subject views, and generators.

Run `python3 checkpoint-parts/reassemble.py` from the repository root. The command verifies every part, the complete ZIP, every archived file hash, and archive coverage.

Archive SHA-256: `de280269cfb40b8eadcafa8b6a4b8c35d1d9ed5928e2ac7d662733f443110ff1`. Files: 1732. [Exact part specification](manifest.json).

Checkpoint parts and their transport metadata are outside the corpus to prevent recursive packaging. The reconstruction program is also preserved as `tools/reassemble_checkpoint.py` inside the archive. A checkpoint preserves work without changing its evidential standing.
