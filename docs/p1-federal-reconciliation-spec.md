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

## Classification rule

- **Pass:** customs is dominant under both the non-loan and usable-inflow denominators for most comparable periods, reconciles within the declared tolerance, and is not defeated by timing.
- **Mixed:** dominance depends on years, accounting state, or the exclusion of material loan/asset inflows.
- **Fail:** customs is not dominant after consistent treatment, or the figures cannot be reconciled well enough to support the claim.

The numeric dominance threshold and reconciliation tolerance must be set before the first complete annual panel is inspected. Until then, no pass/mixed/fail label is allowed.

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
