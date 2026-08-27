# FRASER 5636 second-verification record

## Scope

This record documents an unattributed second-pass check of:

1. Document 102 annual duties-received and drawbacks-paid controls for 1793-1795, PDF pages 102-104.
2. Internal Revenue Statement K, PDF page 34.

The first pass was manual image transcription. The second pass used text extraction, component arithmetic, and the printed control totals. Because no verifier identity is recorded and text extraction is not a second image reading, this record does not satisfy the attributable independent-verification gate. All observations retain exact fractional cents where printed.

## Document 102 controls

| Year | Duties received | Drawbacks in article table | Adjustment | Adjusted drawbacks |
|---|---:|---:|---:|---:|
| 1793 | $6,598,445.31 | $279,809.83 | - | $279,809.83 |
| 1794 | $8,588,382.98 | $1,615,574.44 | - | $1,615,574.44 |
| 1795 | $11,163,370.23 | $2,890,034.40 | $8,731.39 | $2,898,765.79 |

The 1795 adjustment is printed on page 104 for drawbacks paid by the present Newburyport collector on merchandise exported before his appointment. The source states that the particulars had not been received at the Treasury.

### Accounting-state decision

“Duties received” is classified as `collected_by_collector`, not `received_into_treasury`.

This is the narrowest classification consistent with the table:

- the amounts are organized from collector and district returns;
- the Newburyport note distinguishes collector payment details from particulars received at Treasury;
- the statement never says the duties were remitted to or received into Treasury.

The observations are verified federal customs cash at the collection stage, but excluded from the primary P1 ratios until a compatible remittance or Treasury-receipt statement is found.

Drawbacks are classified as `paid`. Annual drawbacks are not treated as a matched deduction from the same year's imports because the source explicitly warns that exports can concern merchandise imported in preceding years.

## Internal Revenue Statement K

### Revenue-payable components

| Component | Exact dollars |
|---|---:|
| Distilled spirits and stills | 357,539.3150 |
| Auction sales | 31,289.9175 |
| Snuff by quantity | 2,399.0850 |
| Snuff mills | 7,112.0000 |
| Refined sugar | 33,988.2825 |
| Carriages | 41,421.1700 |
| Retailer licences | 54,731.5450 |
| **Printed and recomputed revenue payable** | **528,481.3150** |

Arithmetic difference: **$0.0000**.

### Collection charges and reported net

| Control | Exact dollars |
|---|---:|
| Salaries, commissions, compensation, and emoluments | 77,978.595 |
| Incidental and contingent expenses | 6,964.620 |
| **Printed and recomputed collection charges** | **84,943.215** |
| **Revenue payable less collection charges** | **443,538.10** |

Arithmetic difference from the printed net: **$0.00**.

### Definition decision

Statement K is classified as assessed or payable revenue, not cash received into Treasury.

Its “net amount of revenue” means net of collection charges. It does **not** mean net of drawbacks. This follows from the component arithmetic:

- the refined-sugar amount carried to Statement K is gross duties less prompt-payment discount, before the $176.10 drawback;
- Statement A similarly carries domestic-spirit duties before its separate drawback columns;
- the seven carried components sum exactly to the printed revenue-payable control only on this basis.

The table also combines different tax periods, deficient returns, informal returns, and estimates. It is therefore excluded from the primary P1 cash denominator, though retained for sensitivity analysis and for bounding noncustoms revenue.

## Canonical-data result

Twenty observations, `AFB-P1OBS-0043` through `AFB-P1OBS-0062`, were added to `data/p1-federal-fiscal-observations.csv`.

Validation:

- At the time of this batch: 21 columns per row and 62 unique observations;
- Current canonical-table dimensions are maintained and tested elsewhere; these historical batch counts are not current-table assertions;
- no duplicate IDs;
- 1795 drawback detail plus adjustment equals the printed adjusted total exactly;
- Statement K components equal the printed revenue-payable total exactly;
- Statement K charges equal the printed charge total exactly;
- revenue payable less charges equals the printed net exactly.

## P1 consequence

No new annual period is admissible for (C_s) or (C_u). The figures reconcile in this second pass, but independent verification is still pending and the custody and accounting states are incompatible with the primary definitions:

- customs is collector-stage cash;
- internal revenue is payable or estimated;
- annual loan and asset-sale inflows are incomplete;
- no common Treasury-cash denominator exists.

Magnitude cannot cure a definition failure. The correct result remains `insufficient_coverage` rather than a provisional customs-dominance pass.
