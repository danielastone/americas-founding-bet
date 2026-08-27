# FRASER 5637 P1 assessment

## Decision

FRASER item 5637 contains two definition-compatible federal Treasury cash accounts, for **1797 Q4** and **1798 Q1**. They are usable only as provisional quarterly controls. A second-pass check and full statement arithmetic reconciliation are recorded, but the purported independent image verification has no attributable verifier and does not satisfy the admission gate. They do not satisfy the project's annual-equivalent coverage floor and therefore do not change P1 from `insufficient_coverage`.

The statement inventory is in `sources/fraser-5637-p1-statement-inventory.csv`.

## Decisive Treasury accounts

Both statements are titled accounts of United States “receipts and expenditures,” are signed by Treasury Secretary Oliver Wolcott on April 27, 1798, and explicitly classify customs as “receipts into the treasury, from duties on merchandise and tonnage.”

| Period | Customs Treasury cash | Internal duties | Other current/source receipts excluding opening balance |
|---|---:|---:|---:|
| 1797-10-01 to 1797-12-31 | $1,982,927.54 | $137,389.37 | $132,813.74 |
| 1798-01-01 to 1798-03-31 | $1,901,789.82 | $173,158.63 | $68,397.22 |

For 1797 Q4, “other” is postage, public lands, patent fees, Mint coin, and the Willings and Francis repayment. The separate $70,000 six-percent stock sale is financing and belongs only in a usable-inflows calculation.

For 1798 Q1, “other” is postage, land sales, patent fees, Mint coin, Bank dividends, and named agent repayments. No loan proceeds appear in the receipts column.

The provisional classifications imply:

- 1797 Q4 operating-receipt customs share: **88.01%**
- 1797 Q4 usable-inflow customs share including the stock sale: **85.36%**
- 1798 Q1 operating-receipt customs share: **88.73%**

These are quarterly diagnostic results, not annual P1 observations.

## Boundary controls

The opening Treasury balance is a stock carried into the period and is excluded from receipt-share denominators. Closing Treasury balances are also stocks. Stock-sale proceeds, dividends, asset receipts, and agent repayments remain separately typed so the strict and usable denominators can be reconstructed rather than silently blended.

The expenditure side is period-compatible. Debt-service cash totals $2,374,712.46 in 1797 Q4 and $881,141.30 in 1798 Q1, producing quarterly `D_c` controls of **119.76%** and **46.33%**. The Q4 value above 100% is not an error: debt service drew on opening cash and the period's financing as well as current customs receipts. Some domestic-debt lines combine interest and principal, but both components belong in the defined numerator.

## Other evidence in the volume

- The 1794-1796 drawback comparison is collector/customs evidence, not proof of Treasury custody.
- Internal-revenue statements are important denominator controls but mix returns, estimates, payable or collected duties, and differing reporting periods.
- The 1798 revenue and expenditure estimates are ex ante risk evidence, not realized P1 data.
- Appropriation balances and bank-loan balances are stocks, not annual cash flows.
- Sinking-fund statements may support debt-service reconstruction only after separating cash paid from stock face values and balances.

## Falsification consequence

The quarterly accounts provide a provisional accounting-bridge signal: in two adjacent quarters, the transcribed customs cash received into Treasury exceeds the other classified current receipts. This remains a source-reading result, not admitted evidence, until attributable independent image verification is complete. They do not establish persistence across 1789-1803. The priority remains locating compatible annual accounts; the next gate is no longer more work on these quarters. It is locating compatible annual Treasury accounts; further refinement of 5637 would have lower value than closing the coverage gap.
