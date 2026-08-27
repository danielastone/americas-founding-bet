# P1 ratio reproducibility audit

**Audit date:** 2026-08-27  
**Observation table:** `data/p1-federal-fiscal-observations.csv`  
**Component map:** `data/p1-ratio-component-map.csv`  
**Result table:** `data/p1-period-ratios.csv`

## Finding

The three stored period results are reproducible from 22 explicitly selected observation rows. `C_s` and `C_u` reproduced immediately. An apparent `D_c` inversion was traced to an ambiguous shorthand description outside the governing specification: the precommitted formula and stored values both define `D_c` as debt-service cash divided by customs cash.

The ratio table now carries the literal definition `debt_service_cash/customs_cash`, the component-map path, and an exact-reproduction status.

## Reproduction results

| Period | Customs cash | Non-loan cash | Usable cash | Debt-service cash | C_s | C_u | D_c |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1792 | $3,443,070.85 | $3,674,732.36 | $4,777,230.81 | $3,067,104.53 | 0.93695826 | 0.72072525 | 0.89080494 |
| 1797 Q4 | $1,982,927.54 | $2,253,130.65 | $2,323,130.65 | $2,374,712.46 | 0.88007659 | 0.85355834 | 1.19757904 |
| 1798 Q1 | $1,901,789.82 | $2,143,345.67 | $2,143,345.67 | $881,141.30 | 0.88729963 | 0.88729963 | 0.46332212 |

Differences between recomputed and stored monetary totals are zero to the cent. Ratio differences are zero at the eight-decimal storage precision.

## Inclusion controls

- Opening Treasury balances are excluded.
- The $4 million circular Bank-subscription transaction is excluded.
- Genuine loan proceeds enter usable cash but not non-loan cash.
- Assessed, accrued, estimated, mixed-period, and collector-level values are excluded.
- Quarterly controls remain nonannual and receive no annual-coverage credit.
- `D_c` is descriptive; it does not determine the customs-dominance classification.

## Conclusion

The published P1 ratios are computationally reproducible, but the evidence panel remains inadequate for thesis classification. Exact arithmetic on three periods cannot substitute for the missing annual observations. P1 remains `insufficient_coverage`.
