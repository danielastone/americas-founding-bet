# NARA archival strategy for the federal fiscal thesis

## Finding

NARA is the route from published compilations toward originating federal records, but its holdings do not support a simple download-and-analyze workflow. Most relevant series are described at record-group level and require inventory, entry, volume or box identification before the evidence can be examined.

The highest-value target is **Record Group 217, Office of the Register, Receipts and Expenditures Division**. NARA describes:

- ledgers beginning in 1776;
- journals through 1799;
- daybooks beginning in 1789;
- abstracts of United States receipts and expenditures beginning in 1789.

If the 1789–1803 run survives with usable classifications, it is the best candidate for constructing the federal denominator and reconciling the American State Papers tables. It outranks port-level transcription.

### T964 access target

NARA microfilm publication T964 is a single roll titled *Day Book of the Register’s Office of the Treasury, 1789–1791*. It is the fastest potential route into the opening transaction chronology. It is not confirmed online, and a public catalog search does not establish that LOC holds a service copy. Because T-publications may reproduce only a selected segment of a series and may lack the descriptive pamphlet supplied with a full M-publication, the reel must be tied back to Inventory 14 and the original RG 217 series before analytical use. See `docs/nara-t964-source-assessment.md`.

## Priority order

1. **RG 217 central receipts and expenditures.** Establish exact series identifiers, physical location, volumes, period conventions and reproduction feasibility.
2. **RG 217 debt audit reports and RG 53 debt accounts.** Separate principal, interest, commissions, exchange, borrowing proceeds and stock transactions.
3. **RG 56 collector correspondence.** Explain reporting lags, remittance problems, bonding, defaults and disruptions identified in the central accounts. M178 spans 39 rolls for 1789–1833, but it was assembled after the 1833 Treasury fire from multiple surviving sources. It is a reconstruction, not a complete original series; use it only for targeted mechanism tests. See `docs/nara-m178-source-assessment.md`.
4. **RG 36 customhouse records.** Test physical commodity, merchant, voyage, bonding, drawback and enforcement mechanisms only after a survival matrix prevents opportunistic port selection.
5. **RG 26 cutter and lighthouse records.** Use for specified infrastructure or enforcement claims, not for the federal customs-share denominator.
6. **RG 50 Treasurer records.** Defer: the described surviving series largely begin after the project period, and NARA warns that many pre-1829 records were destroyed in the 1833 Treasury fire.

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

The guide pages establish that a series exists; they are **source-discovery evidence**, not evidence for a historical amount. A record becomes E1 only after the specific archival item is identified and inspected. Until then, every NARA entry remains an E1 candidate.

## Immediate archival request

The first inquiry is drafted at `docs/requests/nara-rg217-reference-inquiry.md` and was sent on August 26, 2026, as recorded in `sources/archival-request-log.csv`. Await the logged response window before sending a duplicate inquiry.

The request remains narrow:

> Please provide the Inventory 14 entry or current series-level catalog identifiers, physical location, volume or box list, and reproduction/digitization options for the Office of the Register of the Treasury, Receipts and Expenditures Division: daybooks beginning in 1789 and abstracts of receipts and expenditures of the United States for 1789–1803. We are specifically trying to determine annual or quarterly accounting periods, revenue-source classifications, and whether loans, opening balances, and asset proceeds are separately identified.

Do not request all early Treasury material. That would produce an expensive, unfocused research queue.

## Repository files

- `sources/nara-federal-record-groups.csv`: source-routing map;
- `sources/p1-asp-finance-1789-1800-census.csv`: published-document census to reconcile against NARA records;
- `data/p1-federal-fiscal-observations.csv`: canonical analytical observation table retaining source, accounting-state, and admission distinctions;
- `data/p1-endpoint-staging.csv`: noncanonical endpoint staging only; records must pass the reconciliation and admission rules before migration into the canonical table.

## Online-resolution result

The National Archives Catalog search did not expose usable series-level identifiers for the early daybooks or abstracts. NARA's Record Group Explorer reports that approximately 0.39% of RG 217 textual pages are scanned online. Inventory 14 is cited by NARA but is not provided as a searchable official online finding aid. Reference-staff resolution is therefore the efficient next step.

Archives I is the appropriate initial contact for these executive-branch records: `archives1reference@nara.gov`. NARA currently advises allowing 10–12 business days for a response and not sending duplicate inquiries during that interval.
