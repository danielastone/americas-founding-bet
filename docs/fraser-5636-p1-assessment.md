# FRASER 5636 P1 assessment

## Decision

FRASER item 5636 expands the stress-and-expansion evidence window, but it does **not** supply a complete, definition-compatible annual P1 ratio by itself.

The item is a compilation of American State Papers documents rather than one annual cash account. Its useful statements report different accounting states: duties received by article, drawbacks paid, revenue payable, estimates for missing returns, cash debt-service applications, asset-sale proceeds, foreign-loan transfers, closing loan balances, debt stocks, and accrued uncollected customs bonds. Combining these without reconciliation would create a result rather than test one.

The statement inventory is in `sources/fraser-5636-p1-statement-inventory.csv`.

## Highest-value evidence

### Customs duties and drawbacks, 1793-1795

Document 102, PDF pages 102-104, reports:

| Year | Duties received | Drawbacks paid in table |
|---|---:|---:|
| 1793 | $6,598,445.31 | $279,809.83 |
| 1794 | $8,588,382.98 | $1,615,574.44 |
| 1795 | $11,163,370.23 | $2,890,034.40 |

The page 104 note adds $8,731.39 of Newburyport drawbacks not included in the article detail, producing the printed 1795 total of **$2,898,765.79**.

These figures cannot yet enter (C_s) or (C_u):

- “duties received” is not explicitly “cash received into Treasury”;
- drawbacks paid in a year can relate to merchandise imported in prior years;
- collection expenses are not reported in this table;
- the table does not report all other federal cash receipts or loan proceeds.

Subtracting annual drawbacks from annual duties would therefore be a cash-period net, not a matched import-cohort net. That may be useful later, but it must be labeled accurately.

### Internal revenue denominator

The internal-revenue report, PDF pages 18-34, is necessary because excluding it would mechanically inflate customs dominance.

Statement K reports:

| Measure | Amount |
|---|---:|
| Internal revenue payable | $528,481.31 |
| Salaries, commissions, compensation, and incidental collection costs | $84,943.21 |
| Net internal revenue | $443,538.10 |

This is not a clean Treasury-cash denominator. The title calls it a “General Statement and Estimate”; underlying statements A-G use different tax periods, include estimates for deficient returns, and contain missing or informal district returns. The source distinguishes duties payable and collected fields. Until those accounting states are reconciled, Statement K is a sensitivity or definition-control source, not primary P1 cash.

### Debt-service and financing evidence

- Document 101, Statement B, PDF page 98, reports **$544,066.54** applied to the first year's reimbursement of six-percent stock. Of this, **$449,804.61** came from proceeds of duties on imports and tonnage **and** domestic distilled spirits. The combined source prevents a customs-only attribution.
- The same document records Bank-stock sale proceeds received into Treasury and their application to bank debts. These asset-sale inflows matter to (C_u), but the full transaction must be reconstructed before admission.
- Document 106, Statement E and Nos. 1-5, PDF pages 118-120, separate annual foreign-loan transfers, foreign-debt interest, selected expenditures, closing foreign-fund balances, and unpaid domestic-loan balances for 1791-1795. Closing loan liabilities are not annual loan proceeds.
- Document 106, Statement H, PDF page 122, estimates **$4,000,000** expected from import-duty bonds accrued through 1795 after drawbacks and collection expenses. It is explicitly accrued, uncollected, and estimated, so it is excluded from primary cash ratios.

## What this source can test

FRASER 5636 can support:

- customs scale and drawback intensity for 1793-1795;
- the noncustoms-revenue denominator as a bounded sensitivity;
- cash debt-service and sinking-fund applications;
- foreign-finance and domestic-loan reconstruction;
- ex ante fiscal risk in 1796;
- identification of accrued customs credit that had not converted to Treasury cash.

It cannot independently establish:

- annual customs cash received into Treasury for 1793-1795;
- all non-loan cash receipts for a compatible annual period;
- all usable cash inflows including annual loan proceeds and asset sales;
- a valid (C_s), (C_u), or (D_c) without cross-statement reconciliation.

## Falsification consequence

The item does not falsify customs dominance, but it blocks a careless pass. The customs totals are large; the denominator and custody definitions are not yet compatible. The next admissible step is a second image transcription of the annual customs/drawback totals and Statement K controls, followed by an explicit accounting-state decision. If the duties cannot be tied to Treasury receipt, they remain outside the primary P1 ratio regardless of magnitude.
