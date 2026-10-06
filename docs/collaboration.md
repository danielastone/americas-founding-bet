# Claim-based collaboration pilot

Start with [AFB-C001](../collaboration/c001-pilot.json). Its two tests preserve the existing parent claim and P1/P3 gates. This reference layer does not recalculate observations, admit evidence, or decide the thesis.

## Find a bounded task

- **AFB-TASK-001:** resolve RG 217 annual source-frame feasibility. The August 31 NARA response already supplies catalog routes; do not repeat a generic inquiry.
- **AFB-TASK-002:** identify timing records for the 1797 Q4 liquidity question. Quarter totals do not establish timely payment or default.

Open a [research submission](https://github.com/danielastone/americas-founding-bet/issues/new?template=research-submission.yml), include the task ID, and supply the capture fields. Assignment and work in progress belong in the issue; the canonical task remains OPEN until submission. A collaborator need not understand the complete ontology.

## Contribution path

1. Submit records or a documented search result through an issue or PR. Record exact provenance, pages, originals, restrictions, researcher identity and retrieval date. An index or catalog lead is not historical evidence.
2. Add an immutable submission record to the pilot with its task ID and issue/PR URL. Move the task to SUBMITTED.
3. Record an attributable review using the template below. Check source identity, claim fit, chronology, ancestry, contradictions and reproducibility. Never invent an independent reviewer.
4. If accepted, propose a PR containing the reviewed link and a change record connecting task, submission and review. Move the task to INCORPORATED only in the same change. Incorporation means the reviewed contribution entered the reference layer; analytical admission remains governed by the existing dictionary and claim gates.
5. If unusable, preserve the submission and review and close as REJECTED. A completed bounded search without relevant records may close as CLOSED_NO_CHANGE with a review and reason. Neither establishes that the historical proposition is false.

Canonical task states: OPEN, SUBMITTED, REVIEWED, INCORPORATED, REJECTED, CLOSED_NO_CHANGE. Review outcomes: accept, reject, no_change. Claim decisions in this pilot stay untested. Any later decision engine requires its own implementation and validation.

## Review template

Record review_id, submission_id, reviewer, reviewed_at (ISO date), outcome, and rationale. The rationale must address authenticity, exact claim fit, period/accounting compatibility, shared source ancestry, contradictions, limitations and whether analytical admission is warranted under existing gates. Explicitly distinguish independent verification from a same-person recheck.

Record submissions as submission_id, task_id, contributor, submitted_at (ISO date), url and summary. Record changes as change_id, task_id, submission_id, review_id, changed_at (ISO date), rationale and affected_link_ids. Preserve prior records; amendments use new IDs and explain the superseded decision in their rationale. Git commits and PRs preserve the file-level history; this is not a cryptographically sealed transaction engine.

## Validate

Run `python3 scripts/validate_collaboration.py` and `python3 -m unittest discover -s tests`. Validation checks record identity, foreign keys, observation/source/locator agreement, reviewed-link provenance and lifecycle consistency. It cannot establish archival authenticity or historical truth.

The seeded links are proposed interpretations of legacy repository observations. No source images were newly inspected for this migration. All original observation states and seven parent claim statuses are preserved.
