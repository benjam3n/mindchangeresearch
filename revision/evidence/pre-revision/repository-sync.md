Intended mind change: Make `mindchangeresearch` the durable, inspectable home of the complete program rather than leaving results only in transient checkpoints.

# Repository synchronization policy

Actual starting judgment: Saving the latest index and checkpoint in persistent files was sufficient continuity.

Concrete input: the user directed that everything completed so far be added to `benjam3n/mindchangeresearch` and that every future result be added there.

For every accepted run:

1. Finish integration and validation before declaring the run complete.
2. Commit the readable index, ledgers, active prompt/instruction, new substantive documents, consolidations, source requirements and execution receipts, negative/null/partial/blocked records, and a complete checkpoint archive.
3. Preserve relative paths in the archive and a SHA-256 manifest so the extracted corpus is verifiable.
4. Mark in-progress work as in progress; repository presence must never promote status.
5. Keep the frozen 300-application obligation and post-allocation cycles distinct.
6. Use one accepted checkpoint per repository commit when feasible; record the commit in the next run’s provenance.
7. Never remove unresolved gates merely to make the repository appear complete.

Bootstrap limitation: the initial repository commit includes the complete corpus as a verified checkpoint archive plus its main readable control files. The archive is authoritative for the 1,000+ preserved source, receipt, application, and support files. Later commits should add the new cycle’s readable files and replace the rolling complete archive and control files.

Actual mind change: Repository synchronization is now part of the acceptance sequence rather than an optional handoff.

Benefit: The whole state can be recovered from one versioned location while the readable control files expose current status without extracting the archive.

Verdict: KEEP after the first commit succeeds; UNRESOLVED until then.

Content assessment: The policy preserves all result classes and separates persistence from validation.

Organization assessment: Rolling control files plus a complete versioned archive avoid 1,000-file bootstrap API fragmentation while retaining every byte and a path manifest.

Next attempts: Verify the first commit; test archive extraction; add commit SHA to run provenance; unpack frequently used new documents; migrate the historical corpus to fully expanded paths if a direct git transport becomes available.

