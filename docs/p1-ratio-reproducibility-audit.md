# P1 ratio reproducibility audit

**Audit date:** 2026-08-27  
**Observation table:** `data/p1-federal-fiscal-observations.csv`  
**Component map:** `data/p1-ratio-component-map.csv`  
**Result table:** `data/p1-period-ratios.csv`

## Finding

All three stored period calculations are reproducible from the component map. A subsequent classification review found that the $4,240 sale of arms and accoutrements had been incorrectly included in the 1792 strict non-loan denominator. It belongs only in usable inflows. The component map and stored ratio have been corrected.

## Reproduction results

| Period | Customs cash | Strict non-loan cash | Usable cash | Debt-service cash | C_s | C_u | D_c |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1792 | $3,443,070.85 | $3,670,492.36 | $4,777,230.81 | $3,067,104.53 | 0.93804061 | 0.72072525 | 0.89080494 |
| 1797 Q4 | $1,982,927.54 | $2,253,130.65 | $2,323,130.65 | $2,374,712.46 | 0.88007659 | 0.85355834 | 1.19757904 |
| 1798 Q1 | $1,901,789.82 | $2,143,345.67 | $2,143,345.67 | $881,141.30 | 0.88729963 | 0.88729963 | 0.46332212 |

Monetary totals reproduce to the cent and ratios reproduce at eight-decimal storage precision.

## Controls and limitations

- Opening balances and the circular $4 million Bank transaction are excluded.
- Loan and asset-sale proceeds enter usable cash but not strict non-loan cash.
- Quarterly controls receive no annual-equivalent credit.
- `D_c = debt_service_cash/customs_cash` and is descriptive.
- Computational reproducibility is separate from evidentiary admission.
- The 1792 result remains provisional until an independent second image verification is logged.

## Conclusion

The arithmetic is reproducible after correction. The annual evidence panel currently contains zero admitted annual equivalents. P1 remains `insufficient_coverage`.
