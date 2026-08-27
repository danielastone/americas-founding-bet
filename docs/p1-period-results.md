# P1 admissible period results

## Current result

The repository now contains one admissible annual observation and two admissible quarterly controls. All three exceed the precommitted 50 percent threshold for both strict and usable-inflow customs dominance. This is evidence consistent with P1, but it is not enough to classify the thesis.

| Period | Annual equivalent | C_s | C_u | D_c |
|---|---:|---:|---:|---:|
| 1792 | Yes | 93.70% | 72.07% | 89.08% |
| 1797 Q4 | No | 88.01% | 85.36% | 119.76% |
| 1798 Q1 | No | 88.73% | 88.73% | 46.33% |

The machine-readable calculations are in `data/p1-period-ratios.csv`.

## 1792 construction

Customs cash received into Treasury was $3,443,070.85. All non-loan cash receipts were $3,674,732.36. Usable inflows were $4,777,230.81 after adding $1,102,498.45 of genuine loan proceeds.

The $4 million Bank subscription loop and the opening Treasury balance are excluded from both denominators. Treating the circular Bank transaction as fiscal capacity would materially understate customs dependence.

Debt-service cash was $3,067,104.53:

- public-debt interest: $2,374,054.28;
- reduction of public debt: $257,786.42;
- French-debt principal paid from foreign funds: $435,263.83.

The French payment remains in `D_c` because the numerator measures cash debt service, not only debt service funded from current domestic Treasury receipts.

## Coverage consequence

Only 1792 counts toward the nine-annual-equivalent floor. The quarterly controls establish accounting continuity around 1798 but add zero annual equivalents.

Current admissible annual coverage is therefore:

- 1789-1792: one annual period;
- 1793-1797: zero annual periods;
- 1798-1803: annual report observations remain incomplete for full-ratio construction.

P1 remains `insufficient_coverage`. The observed ratios should not be described as a pass.

## Next evidence gate

The annual denominator gap requires central Treasury records. The active routes are:

1. NARA RG 217 abstracts of receipts and expenditures and T964;
2. LOC MSS83125 shelf 24,495 for 1789-1790;
3. exact supporting annual accounts behind the 1801-1803 Treasury narratives.

The NARA inquiry was sent August 26, 2026; the logged response window begins September 10. Re-contacting NARA before that window would not improve the evidence.
