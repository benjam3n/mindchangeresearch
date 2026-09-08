# Repository synchronization and recovery

`benjam3n/mindchangeresearch` is the canonical versioned home of accepted work. The research corpus is expanded into native repository paths. The complete rolling checkpoint is also committed as verified binary parts, avoiding a second large unsplit copy in Git.

For each accepted research run:

1. Integrate substantive records, original source receipts, null/rejected/partial results and current instructions. Deliberately reconcile the authoritative research ledger with reviewed proposals and line records; file existence cannot promote status.
2. Update the relevant change, recipe and inquiry entry points. Preserve source history, scope, exceptions and useful disagreement.
3. Run `python tools/check_mind_change.py --integration-baseline` when validating this import (omit the integration-only flag after actual later research changes), `python scripts/validate.py` for the 6,000 catalog entries, original rankings, source references and preserved accounting, and `python tools/validate_repository.py` for current navigation, imported-source integrity and meaningful worked-case checks. This does not certify all historical research.
4. Run `python checkpoint.py`. It validates ledger counts and recorded application hashes, regenerates the inherited inventory views, `research/status.md` and `progress.md`, creates a complete corpus manifest and ZIP, and updates transport parts and metadata. It never overwrites README, the curated index, instructions or research statuses.
5. Run `python checkpoint.py --check`. Commit all changed native corpus files, the manifest, transport parts and metadata together. Use the current remote parent; preserve concurrent changes and never force-overwrite another run.
6. Verify the resulting remote tree or relevant file hashes. Report the commit and supported findings, keeping repository persistence separate from completion or efficacy. The next run can record that accepted commit as provenance.

Run `python checkpoint-parts/reassemble.py` from a downloaded repository to reconstruct and verify `Mind_Change_Research_Checkpoint.zip`. The archive contains the whole research corpus plus its SHA-256 manifest. Its own generated ZIP, the transport directory, Git internals and runtime caches are excluded to prevent recursion. Empty files, binary artifacts and original source bytes are included. Transport integrity is verified separately by per-part and aggregate hashes. A clone includes the transport tooling; extraction provides the corpus and the builder can recreate transport parts.

The original verified archive at commit `07e6af64c65fb682305659b2ec830e21743c0f15` had SHA-256 `7ba425b197be8d38ba9715873464dd0ba2eca43e2da3aeb985ab5ffda83fba6b`. Its contents are now directly available, with newer native controls taking precedence. Historical originals remain unchanged except controls explicitly replaced by this repair, whose reviewed versions are separately preserved.

The saved [automation-prompt.txt](automation-prompt.txt) now begins from the current repository. This policy and prompt update do not claim that an independently configured scheduled task was edited.

The earlier `tools/checkpoint_archive.py` interface delegates to this same builder. Both transport metadata schemas are refreshed together for compatibility with the preserved recovery script. The inventory generator preserves imported identities and never writes README or the curated inquiry index.
