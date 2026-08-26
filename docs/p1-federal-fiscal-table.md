# P1 federal fiscal falsification table

## Objective

Test whether realized customs cash was the dominant usable federal receipt and whether its timing was consistent with the debt-service role assigned to it.

The current files are:

- `data/federal_fiscal_p1.csv`: observation table;
- `sources/p1-federal-source-inventory.csv`: bounded source and audit queue;
- `sources/p1-verification-log.csv`: correction and residual-risk record;
- `sources/p1-asp-finance-1789-1800-census.csv`: assertion-specific census of early Finance papers;
- `docs/p1-asp-finance-census.md`: census scope and extraction rules;
- `sources/nara-federal-record-groups.csv`: originating-record route map;
- `docs/nara-archival-strategy.md`: NARA priorities and bounded request.

The seeded observations are not a conclusion. They demonstrate the accounting distinctions and provide an endpoint-period starting point while the 1789–1800 series is inventoried.

## Primary test

For a consistently defined period:

[
\text{customs share} =
\frac{\text{customs cash received by Treasury}}
{\text{operating cash receipts excluding loan proceeds and opening balances}}
]

Report a second financing measure:

[
\text{customs share of all inflows} =
\frac{\text{customs cash received by Treasury}}
{\text{operating receipts + loan proceeds + asset-sale proceeds}}
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

## Endpoint audit corrections

The first statement reconciliation produced two material corrections:

- the 1803 report date is October 25, 1803, not October 17;
- the annual $3,096,700.69 observation is principal redeemed, not a combined principal-and-interest cash-payment measure.

The 1803 customs observation remains a lower bound because the narrative says receipts “exceeded” $10.6 million. The $5.86 million Treasury balance also remains rounded. Neither may be promoted to an exact observation without its supporting statement.

The 1802 scan confirms that $12.28 million was received into Treasury from merchandise and tonnage duties during the year ending September 30, 1802. It remains rounded to the nearest stated ten thousand dollars. The same page confirms that the $326,052.08 public-land total is not Treasury cash: $17,162.50 was paid into Treasury in debt certificates, $179,575.52 in specie, and $129,314.06 remained with land-office receivers. Only the specie component belongs in an operating-cash denominator.

The 1801 scan confirms customs cash of $10,126,213.92 and corrects internal-revenue cash from the OCR-derived $910,219.16 to $919,719.16. It also confirms that $576,888.80 of permanent internal duties and $209,853.32 of stamp duties are calendar-1800 net-revenue measures, not year-ending-September-1801 cash receipts. They remain excluded from the period denominator. Gallatin further estimated that $65,000 of drawbacks chargeable to internal revenue had been paid by customs collectors from external-revenue proceeds. This is a source-attribution adjustment, not an additional cash outflow to subtract from total Treasury receipts.

## Validation sequence

1. Resolve NARA RG 217 Receipts and Expenditures Division series identifiers and reproduction feasibility for 1789–1803.
2. Finish image-checking seeded amounts, complete the remaining ASP header checks, and extend that census through 1803.
3. Populate operating receipts for every consistent annual period.
4. Populate borrowing and asset-sale proceeds separately.
5. Populate interest and principal payments separately.
6. Reconcile changes in Treasury specie:

[
\text{opening cash + cash inflows - cash outflows = closing cash + explained reconciling items}
]

7. Calculate customs shares only after denominator completeness and period consistency pass.
8. Treat P1 as failed, mixed, or passed under the precommitted conditions in `docs/falsification-priorities.md`.

## Current status

The table is **partly statement-reconciled but not validated as a series**. It contains rounded endpoint observations and no complete 1789–1803 denominator. Computing a customs-dominance ratio now would be misleading.
