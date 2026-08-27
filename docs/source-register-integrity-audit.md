# Source-register structural integrity audit

**Audit date:** 2026-08-27  
**File:** `sources/source-register.csv`  
**Rows tested:** 95 source records

## Result

The source register passes its structural-integrity gate.

| Test | Result |
|---|---|
| Column count | 14 |
| Rows with incorrect field count | 0 |
| Empty source IDs | 0 |
| Duplicate source IDs | 0 |
| Numeric sequence gaps, AFB-S001 through AFB-S095 | 0 |
| Blank title, institution, source type, verification status, or readiness | 0 |
| Nonblank landing pages without HTTP/HTTPS form | 0 |
| Blank landing pages | 0 |
| Blank repository identifiers | 0 |
| Duplicate landing-page groups | 4 groups covering 11 scoped entries |
| Metadata-verification actor/date fields in schema | absent |

## Controlled values observed

Verification status:

- `needs-item-check`
- `needs-series-check`
- `verified`

Evidence readiness:

- `discovery_only`
- `item_identified`
- `source_identified`

No row is currently labeled `transcribed`, `validated`, or `analysis_ready`. That is appropriate: structural and metadata verification alone do not establish evidentiary readiness.

The register contains 89 rows labeled `verified`, four `needs-item-check`, and two `needs-series-check`. The schema does not retain who performed a metadata verification, when it was performed, or a joinable verification record. Accordingly, `verified` must be read as a legacy metadata-status label, not independently auditable verification.

## Scope limit

This audit validates CSV structure, identifiers, required-field presence, and controlled-value usage. It does not establish verification attribution or evidentiary independence.

Four landing pages are reused across multiple scoped entries: RG 36 (four entries), RG 26 (three), RG 53 (two), and RG 217 (two). The entries describe different intended uses, so they are not duplicate source IDs. They nevertheless share an underlying guide and must not be counted as independent evidentiary origins.

 It does not validate every title, date, creator, repository identifier, landing-page destination, rights statement, or item-level claim.

Those checks remain open under issue #1 and must be completed in bounded batches. The P1-priority metadata and observation-linkage batches are documented in `docs/source-register-p1-metadata-audit.md` and `docs/p1-observation-provenance-audit.md`.
