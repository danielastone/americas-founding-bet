# Early customs evidence, 1789–1790

## Scope

This audit stages the aggregate tables in American State Papers, Finance, volume 1, Documents 12 and 22. It does not convert them into Treasury cash receipts.

Source scan: https://tile.loc.gov/storage-services/service/ll/llscd/llsp009/llsp009.pdf

## Accounting findings

### Document 12: tonnage, September–December 1789

The table is explicitly an abstract of duties **accrued** on foreign and domestic tonnage. The aggregate components are $50,366.72 and $11,990.05, which reconcile exactly to $62,356.77. A degraded scan or OCR can make the total look like $62,350.77; the component arithmetic resolves the ambiguity.

These observations are accrued liabilities, not demonstrated remittances to Treasury.

### Document 22: imports, August 1789–September 1790

Hamilton’s cover letter describes sums “received,” but both enclosed tables are headed as duties **arising** on imported goods. Their internal structure reports gross duties, a ten-percent discount, drawbacks, collection expense, and net duties. The safest classification is therefore net duties arising from collector returns until a remittance or central Treasury account proves a cash transfer.

The first period reconciles:

445,289.9350 - 24,210.7375 - 3.0000 - 5,917.0250 = 415,159.1725

The second period reconciles:

2,130,224.9125 - 146,983.1750 - 5,311.5850 - 74,220.6650 = 1,903,709.4875

Fractional cents are retained rather than rounded.

## Coverage defect

The October 1, 1789–September 30, 1790 table is incomplete. Its notes identify missing returns from small Massachusetts ports for one quarter and from Charleston for one quarter. The aggregate is therefore an incomplete lower bound even for the table’s own accounting measure.

## Decision rule

No row in `data/early_customs_1789_1790.csv` enters the customs-cash numerator or the operating-receipts denominator. Admission requires a source that identifies collector remittance, Treasury receipt, or a reconciled central account for the same period.

## Next evidence

1. Extract the state and port rows to localize missing coverage.
2. Match collector returns to RG 36 customs records where feasible.
3. Locate RG 217 central receipts, remittance, or warrants evidence.
4. Compare later retrospective ASP customs tables for revisions without treating agreement as proof of cash receipt.
