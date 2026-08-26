# American State Papers Finance census: 1789–1800 evidence

## Scope

This census inventories the Class III Finance documents in volume 1 that could bear on P1: whether customs cash dominated usable federal receipts and supported debt service through the Louisiana Purchase endpoint.

“1789–1800” refers to observation coverage. Several reports transmitted in 1801 or 1802 are included because they contain the first compiled statements for 1799 or 1800.

The source file is the Library of Congress scan of *American State Papers, Finance, Volume I*, covering 1789–1802:

- `sources/p1-asp-finance-1789-1800-census.csv`
- Library of Congress resource: https://tile.loc.gov/storage-services/service/ll/llscd/llsp009/llsp009.pdf

## What the census does not establish

The American State Papers are a nineteenth-century selected compilation. A document reproduced here remains evidence of a dated Treasury or congressional communication, but the compilation itself is not the originating ledger.

The census therefore does not:

- treat a table of duties accrued as cash received;
- treat an estimate or appropriation as an expenditure;
- treat a Treasury balance as revenue;
- treat loan proceeds or Bank-share sales as operating receipts;
- assume that overlapping tables are independent observations;
- infer absence of a record merely because Gales and Seaton did not select it.

## Census states

- `header_verified`: document number, title, start page and communication header were checked in the scan.
- `toc_identified`: candidate was identified in the volume table of contents but its opening header still requires inspection.

These states concern document identity, not validation of every number inside the document.

## Priority routing

### First extraction block

1. Documents 12 and 22: earliest customs evidence.
2. Documents 32 and 61: receipts/expenditures and explicit missing-return warnings.
3. Documents 102, 124, 146, 159 and 167: overlapping customs duty/drawback vintages.
4. Documents 93, 129, 137, 145, 154 and 166: internal-revenue comparator series.
5. Documents 44, 46, 59 and 147: cash balances, deposits, loans and surplus.
6. Documents 106 and 152: debt payments, redemption and stock-flow reconciliation.

### Supporting interpretation

Documents 6, 87, 99 and 151 establish contemporaneous plans, constraints and risk assessments. They cannot substitute for realized fiscal observations.

## Required extraction rule

Every extracted amount must carry:

- the document number and printed page;
- the original observation period;
- its accounting state;
- whether it was reported, estimated or reconstructed;
- its relationship to any overlapping vintage;
- whether it belongs in operating receipts, financing inflows, liquidity, debt uses or none of those.

The first analytical table should not be calculated until the customs, internal-revenue and financing blocks can be reconciled for the same periods.
