# P1-priority source-register metadata audit

**Audit date:** 2026-08-27  
**Register rows added:** AFB-S087–AFB-S094  
**Scope:** Sources already used by, or immediately capable of falsifying, the P1 federal fiscal-capacity reconstruction.

## Result

Eight missing sources were added to the canonical register. The batch closes a provenance gap in the register; it does **not** close P1's evidence-coverage gap.

Red-team retest confirms that the eight rows match the IDs, identifiers, verification labels, and readiness states shown below. The six `verified` labels in this batch are legacy metadata-status labels: the source-register schema does not retain verifier identity, verification date, or a verification-record foreign key.

| ID | Source | Identifier | Verification | Readiness | Decision |
|---|---|---|---|---|---|
| AFB-S087 | American State Papers excerpts, 1798 | FRASER 5637 | verified | source_identified | Quarterly evidence only; no annual-equivalent inference |
| AFB-S088 | Gallatin finance report, 1801 | FRASER 5640 | verified | source_identified | Exact revenue figures; compatible debt denominator still missing |
| AFB-S089 | Gallatin finance report, 1802 | FRASER 5641 | verified | source_identified | Preserve rounded customs and the $166,612.50 debt-total discrepancy |
| AFB-S090 | Gallatin finance report, 1803 | FRASER 5642 | verified | source_identified | Treat incomplete customs as a lower bound; separate principal from debt service |
| AFB-S091 | American State Papers: Finance, vol. 1 | llsp009 | verified | source_identified | Retrospective selected compilation; cite document and image page |
| AFB-S092 | Treasury accounting officers records | RG 217 | verified | discovery_only | Record-group guide only; exact series and item required |
| AFB-S093 | Register's Office day book, 1789–1791 | T964; RG 217 | needs-item-check | item_identified | NARA inquiry pending; no coverage credit |
| AFB-S094 | Treasury receipts and expenditures extracts, 1784–1790 | MSS83125; shelf 24,495 | needs-item-check | item_identified | Physical LOC inspection required; no coverage credit |

## Guardrails

- A verified landing page proves source identity, not numerical validity.
- Printed compilations must be checked against page images and, where possible, underlying accounting records.
- T964 and shelf 24,495 remain candidate falsification sources until inspected.
- No collector-level, proxy, quarterly-only, or accounting-basis-mismatched observation may be promoted into an annual ratio.
- P1 remains `insufficient_coverage`.

## Next bounded batch

Reconcile the P1 evidence table against AFB-S087–AFB-S094 and verify that every observation records source ID, page, period, unit, accounting basis, transcription status, and any unresolved discrepancy.
