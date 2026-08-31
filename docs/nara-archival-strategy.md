# NARA archival strategy for the federal fiscal thesis

## Finding

NARA is the route from published compilations toward originating federal records, but its holdings do not support a simple download-and-analyze workflow. Most relevant series are described at record-group or series level and require item, volume, box, or other container identification before the evidence can be examined.

The highest-value target is **Record Group 217, Office of the Register, Receipts and Expenditures Division**. NARA describes:

- ledgers beginning in 1776;
- journals through 1799;
- daybooks beginning in 1789;
- abstracts of United States receipts and expenditures beginning in 1789.

If the 1789–1803 run survives with usable classifications, it is the best candidate for constructing the federal denominator and reconciling the American State Papers tables. It outranks port-level transcription.

## Archives I response — 2026-08-31

NARA responded to request **RR1R-26-86199** and supplied concrete catalog routes for the central series:

- **Daybooks, 1789–1894:** Catalog ID **2517180**;
- **Abstracts of receipts and expenditures, 1789–1889:** RG 217 catalog search for `abstracts`; NARA notes that the Abstracts are broken into several series;
- **Journals, 1776–1799:** Catalog ID **2517189**;
- **Blotters, 1782–1810:** Catalog IDs **16614774** and **2635545**;
- **Ledgers, 1776–1923:** RG 217 series-level catalog search for `ledgers`; NARA notes that the Ledgers are broken into several series.

This is a meaningful source-discovery advance but not an evidentiary validation. NARA did not provide Inventory 14 entries, container lists, microfilm crosswalks, digitization status, sample volumes, or confirmation of the accounting fields needed for the project. The response points to onsite inspection or an independent researcher for item-level examination and copying.

### T964 access target

NARA microfilm publication T964 is a single roll titled *Day Book of the Register’s Office of the Treasury, 1789–1791*. It remains the fastest potential route into the opening transaction chronology. The 2026-08-31 Archives I response did **not** confirm whether T964 reproduces Catalog ID 2517180 or identify its relationship to the original series. That crosswalk must therefore remain unresolved until established from an authoritative finding aid, catalog relation, or inspection. See `docs/nara-t964-source-assessment.md`.

## Priority order

1. **Resolve the supplied RG 217 catalog routes to item/container level.** Start with Daybooks ID 2517180, then the Abstract series, Journals ID 2517189, Blotters IDs 16614774/2635545, and the Ledger series. Capture exact dates, entry/container identifiers, access status, and any digitized images.
2. **RG 217 central receipts and expenditures inspection.** Determine period conventions and whether customs, internal taxes, land/incidental receipts, loans, opening balances, debt service, and adjustments are separately identifiable.
3. **RG 217 debt audit reports and RG 53 debt accounts.** Separate principal, interest, commissions, exchange, borrowing proceeds and stock transactions.
4. **RG 56 collector correspondence.** Explain reporting lags, remittance problems, bonding, defaults and disruptions identified in the central accounts. M178 spans 39 rolls for 1789–1833, but it was assembled after the 1833 Treasury fire from multiple surviving sources. It is a reconstruction, not a complete original series; use it only for targeted mechanism tests. See `docs/nara-m178-source-assessment.md`.
5. **RG 36 customhouse records.** Test physical commodity, merchant, voyage, bonding, drawback and enforcement mechanisms only after a survival matrix prevents opportunistic port selection.
6. **RG 26 cutter and lighthouse records.** Use for specified infrastructure or enforcement claims, not for the federal customs-share denominator.
7. **RG 50 Treasurer records.** Defer: the described surviving series largely begin after the project period, and NARA warns that many pre-1829 records were destroyed in the 1833 Treasury fire.

## Why port records come later

RG 36 includes impost books, manifests, entrances and clearances, drawback and bond records, and other customhouse material. Coverage is uneven across districts and series. A sample built around whichever famous ports are easiest to access would bias the mechanism evidence toward large surviving collections.

Before selecting ports, create a survival matrix containing:

- district;
- exact series;
- inclusive dates;
- gaps;
- level of aggregation;
- commodity detail;
- merchant and vessel identifiers;
- duty, drawback and bond fields;
- physical location;
- digitization or reproduction status.

Port sampling should then be precommitted from that frame.

## Evidence-level treatment

The guide pages and the 2026-08-31 Archives I response establish that series exist and provide routes to them; they are **source-discovery evidence**, not evidence for a historical amount. A record becomes E1 only after the specific archival item is identified and inspected. Until then, every NARA entry remains an E1 candidate.

## Request status and next action

The first inquiry at `docs/requests/nara-rg217-reference-inquiry.md` was sent August 26 and answered August 31, 2026. The response is logged in `sources/archival-request-log.csv`.

Do **not** send another broad request for all early Treasury material. The immediate task is catalog and finding-aid reconnaissance against the identifiers NARA supplied. Escalate to a targeted follow-up only for a specific unresolved item-level question that cannot be answered from those routes.

No purchase, copying order, independent-researcher engagement, or research visit is authorized by the response log.

## Repository files

- `sources/nara-federal-record-groups.csv`: source-routing map;
- `sources/p1-asp-finance-1789-1800-census.csv`: published-document census to reconcile against NARA records;
- `data/p1-federal-fiscal-observations.csv`: canonical analytical observation table retaining source, accounting-state, and admission distinctions;
- `data/p1-endpoint-staging.csv`: noncanonical endpoint staging only; records must pass the reconciliation and admission rules before migration into the canonical table;
- `docs/requests/nara-rg217-reference-inquiry.md`: request and 2026-08-31 response disposition.

## Current access conclusion

The original online search problem is now partly resolved: Archives I supplied direct catalog IDs for the Daybooks, Journals, and Blotters and search routes for the multi-series Abstracts and Ledgers. The remaining bottleneck is no longer discovering whether the record families exist. It is resolving those catalog routes to the exact 1789–1803 items and establishing what fields and accounting periods the records actually contain.
