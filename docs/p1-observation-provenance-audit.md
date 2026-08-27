# P1 observation provenance-linkage audit

**Audit date:** 2026-08-27  
**Observation file:** `data/p1-federal-fiscal-observations.csv`  
**Observations tested:** 80

## Finding and correction

The observation table originally used two local source-ID namespaces—`AFB-P1SRC-*` and `AFB-P1S*`—without a direct foreign key to the canonical `AFB-S*` source register. Three legacy IDs also lacked rows in the P1 source inventory. That made the evidence readable to a person but not referentially sound.

Corrections:

- Added `canonical_source_id` to all 80 observations.
- Added `canonical_source_id` to the P1 federal source inventory.
- Added inventory rows for `AFB-P1SRC-0001` through `AFB-P1SRC-0003`.
- Registered the 1897 retrospective Table K screening source as AFB-S095.
- Preserved the original local IDs as aliases rather than destroying lineage.
- Added an explicit `evidence_state` field rather than treating overloaded verification labels as analytical admission.
- Classified only the admitted 1797 Q4 and 1798 Q1 control-group observations as `analysis_ready`; all other observations remain conservatively `normalized`, including provisional 1792.

## Integrity results

| Test | Result |
|---|---:|
| Observation rows | 80 |
| Observation columns | 23 |
| Unique observation IDs | 80 |
| Orphaned local source IDs | 0 |
| Orphaned canonical source IDs | 0 |
| Missing period start/end/basis | 0 |
| Missing accounting state or gross/net field | 0 |
| Missing amount or original unit | 0 |
| Missing item identifier | 0 |
| Missing table or statement | 0 |
| Missing page or frame | 0 |
| Missing transcription method | 0 |
| Missing verification status | 0 |
| Missing evidence state | 0 |
| Analysis-ready observations | 9 |
| Normalized but not analysis-ready observations | 71 |

## Canonical mappings used

| Observation source | Canonical source |
|---|---|
| FRASER 5631 | AFB-S015 |
| FRASER 5636 | AFB-S060 |
| FRASER 5637 | AFB-S087 |
| FRASER 5641 | AFB-S089 |

## Scope limit

This is a provenance and schema audit, not a claim that all observations are admissible in the P1 ratio. Evidence state controls analytical maturity; verification status records the source-specific check or limitation and does not independently establish analytical admission. Accrual, assessed, estimated, mixed-period, proxy, opening-balance, accounting-loop, discrepancy, and quarterly-only rows remain excluded or limited according to their recorded status.

P1 remains `insufficient_coverage`. The audit improves traceability; it does not create missing annual evidence.
