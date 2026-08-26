# P1 federal receipts and debt-service reconciliation specification

## Decision

The customs-dominance test must be built from reported fiscal observations before it is summarized into annual ratios. No figure enters the P1 test merely because it appears in OCR or in a later historical compilation.

The canonical observation table is `data/p1-federal-fiscal-observations.csv`. Its first commit contains the schema only. Empty data is preferable to prematurely admitted numbers.

## Test

P1 asks whether realized customs cash was the dominant usable federal revenue between 1789 and 1803 after accounting definitions and timing are reconciled.

The test is not:

- customs assessments divided by imports;
- customs receipts divided only by tax receipts while excluding loans;
- gross duties before drawbacks and collection costs treated as Treasury cash;
- debt outstanding compared with annual customs revenue;
- a ratio constructed from mismatched calendar and fiscal periods.

## Required flow classes

### Sources of cash

- customs;
- tonnage duties;
- internal revenue or excise;
- direct taxes;
- land sales;
- postal or other operating receipts;
- loan proceeds;
- asset sales;
- repayments and recoveries;
- opening balances and transfers.

### Uses and offsets

- drawbacks and refunds;
- collection expenses;
- interest paid;
- principal redeemed or reimbursed;
- sinking-fund purchases;
- civil, military, diplomatic, and other expenditures;
- transfers and closing balances.

## Accounting-state vocabulary

Every observation must use one of these states:

- `assessed`: liability calculated but not necessarily paid;
- `bonded`: obligation deferred under customs credit;
- `collected_by_collector`: cash received locally;
- `remitted_or_deposited`: cash transferred toward Treasury custody;
- `received_into_treasury`: Treasury receipt;
- `appropriated`: legally assigned, not proof of payment;
- `warranted`: payment authority issued;
- `paid`: cash disbursed;
- `accrued_uncollected`: recognized but outstanding;
- `stock_or_face_value`: noncash principal measure;
- `unknown`: unresolved and excluded from the primary ratio.

## Reconciliation groups

Do not force differently defined reports into one series. Assign observations to a reconciliation group only when they share:

1. the same reporting interval;
2. the same geographic scope;
3. compatible cash or accrual state;
4. compatible gross or net definition;
5. compatible treatment of transfers and balances.

## Primary calculations

For each admissible period:

[
C_s = rac{	ext{customs cash received into Treasury}}{	ext{all non-loan cash receipts}}
]

[
C_u = rac{	ext{customs cash received into Treasury}}{	ext{all usable cash inflows including loan proceeds and asset sales}}
]

[
D_c = rac{	ext{cash interest + cash principal service}}{	ext{customs cash received into Treasury}}
]

These ratios answer different questions and must not be collapsed into one “customs dependence” statistic.

## Precommitted thresholds

These rules were fixed before the first complete annual panel was transcribed.

### Coverage floor

Do not classify P1 unless the admissible evidence contains at least nine annual-equivalent periods, including at least two periods from each of these windows:

- opening: 1789–1792;
- stress and expansion: 1793–1797;
- mature system and endpoint: 1798–1803.

A partial period counts only in period-level results and does not count as a full annual equivalent. Failure to meet the floor produces `insufficient_coverage`, not `mixed`.

### Dominance

“Dominant” means an absolute majority, not merely the largest named category.

A period satisfies non-loan dominance when `C_s > 0.50`. It satisfies usable-inflow dominance when `C_u > 0.50`. Exactly 0.50 does not pass.

### Reconciliation tolerance

- Arithmetic within one printed statement must reconcile within the larger of $1.00 or 0.01 percent of its reported total.
- Independently reported, definition-compatible totals are primary-test compatible when their absolute difference is no greater than 0.50 percent of the larger total.
- A difference above 0.50 percent and no greater than 2.00 percent is provisional and enters sensitivity analysis only.
- A difference above 2.00 percent is excluded until explained and corrected or explicitly reclassified as definition-incompatible.

A documented rounding convention may explain a difference but does not authorize silent adjustment. The original and reconciled values must both remain visible.

## Classification rule

Apply these rules only after the coverage floor is met:

- **Pass:** pooled `C_s > 0.50`, pooled `C_u > 0.50`, and at least two-thirds of admissible periods independently exceed 0.50 on both ratios.
- **Mixed:** the non-loan test passes but the usable-inflow test fails; pooled and period-level results disagree; or results change when provisional observations are excluded.
- **Fail:** pooled `C_s <= 0.50`; or fewer than one-half of admissible periods have `C_s > 0.50`.
- **Indeterminate:** neither pass, mixed, nor fail conditions are met after the coverage floor, or accounting-state ambiguity remains material.

`D_c` measures debt-service burden relative to customs cash; it does not determine customs dominance by itself. Timing failure is evaluated separately under P3 and may narrow “dependable” even if P1 passes.

The stricter usable-inflow condition prevents loan proceeds and asset sales from disappearing from the fiscal-capacity claim. The non-loan condition prevents those financing flows from being mislabeled as revenue.

## Admission rules

A value is admitted only when it has:

- an exact source and item identifier;
- an exact table or statement and page/frame;
- the original reporting-period label;
- an accounting-state classification supported by the source;
- gross/net treatment;
- image verification by two passes or an equivalent independent check;
- a reconciliation group or an explicit reason it cannot be reconciled.

OCR can locate a table but cannot verify a number.

## Source coverage

See `sources/p1-published-source-coverage.csv`. The current independent tranche covers publicly accessible FRASER items for 1792, 1796, and 1798. T964 and LOC shelf 24,495 remain external dependencies and cannot block construction of this specification.

## Stop rule

Do not proceed to port, merchant, commodity, or welfare generalization to compensate for an unresolved or failed P1 result. Preserve discrepancies and negative results.
