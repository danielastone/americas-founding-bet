# P1 federal fiscal falsification table

## Objective

Test whether realized customs cash was the dominant usable federal receipt and whether its timing was consistent with the debt-service role assigned to it.

The current files are:

- `data/federal_fiscal_p1.csv`: observation table;
- `sources/p1-federal-source-inventory.csv`: bounded source and audit queue.

The seeded observations are not a conclusion. They demonstrate the accounting distinctions and provide an endpoint-period starting point while the 1789–1800 series is inventoried.

## Primary test

For a consistently defined period:

[
	ext{customs share} =
rac{	ext{customs cash received by Treasury}}
{	ext{operating cash receipts excluding loan proceeds and opening balances}}
]

Report a second financing measure:

[
	ext{customs share of all inflows} =
rac{	ext{customs cash received by Treasury}}
{	ext{operating receipts + loan proceeds + asset-sale proceeds}}
]

These ratios answer different questions. Neither may combine accrued revenue, duties secured, land-office receipts not transferred, Treasury opening balances, or statutory appropriations with cash received.

## Minimum required measures

### Operating receipts

- customs merchandise and tonnage cash;
- internal duties and direct taxes;
- public-land specie received by Treasury;
- postage, dividends, fees, fines, penalties, repayments, and other incidental cash.

### Financing and nonoperating inflows

- domestic and foreign borrowing proceeds;
- Treasury sales of Bank shares or other assets;
- debt certificates accepted for land or other obligations;
- repayments of advances.

### Uses and liquidity

- interest paid;
- principal redeemed;
- commissions and exchange losses;
- Treasury opening and closing specie;
- transfers and remittances;
- customs bonds outstanding, due, paid, defaulted, or extended;
- drawbacks and refunds.

## Audit problems already identified

1. Gallatin explicitly distinguished receipts into Treasury from revenue accrued and from duties secured for future payment.
2. Public-land “receipts” included specie, public-debt evidence, and balances still held by receivers.
3. Narrative report figures may be rounded while supporting statements contain exact amounts.
4. Debt payments can combine principal, interest, commissions, exchange differences, and debt extinguished through asset sales.
5. Annual totals cannot establish liquidity sufficiency without bond maturities, remittances, balances, and due dates.
6. FRASER searchable text is OCR and must be checked against the report image.
7. The American State Papers reproduce dated reports but remain a retrospective selected compilation.

## Validation sequence

1. Image-check every seeded amount and replace rounded amounts with exact statement figures where available.
2. Complete a document census for American State Papers Finance covering 1789–1803.
3. Populate operating receipts for every consistent annual period.
4. Populate borrowing and asset-sale proceeds separately.
5. Populate interest and principal payments separately.
6. Reconcile changes in Treasury specie:

[
	ext{opening cash + cash inflows - cash outflows = closing cash + explained reconciling items}
]

7. Calculate customs shares only after denominator completeness and period consistency pass.
8. Treat P1 as failed, mixed, or passed under the precommitted conditions in `docs/falsification-priorities.md`.

## Current status

The table is **transcribed but not validated**. It contains several rounded or OCR-dependent endpoint observations and no complete 1789–1803 denominator. Computing a customs-dominance ratio now would be misleading.
