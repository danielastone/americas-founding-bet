# P1 period results

## Current result

The repository contains one provisional annual control and two provisional quarterly controls. All three calculated ratios exceed the precommitted 50 percent threshold for both strict and usable-inflow customs dominance, but none is analytically admitted because the required independent verification is not attributable.

| Period | Annual-equivalent credit | C_s | C_u | D_c | Status |
|---|---:|---:|---:|---:|---|
| 1792 | 0 pending verification | 93.80% | 72.07% | 89.08% | provisional annual control |
| 1797 Q4 | 0 | 88.01% | 85.36% | 119.76% | provisional; second-check verifier unrecorded |
| 1798 Q1 | 0 | 88.73% | 88.73% | 46.33% | provisional; second-check verifier unrecorded |

The machine-readable calculations are in `data/p1-period-ratios.csv`.

`D_c` is debt-service cash divided by customs cash—not its inverse. It measures debt-service burden relative to customs receipts and is not a customs-dominance threshold. Each result is reproducible from `data/p1-ratio-component-map.csv`.

## 1792 construction

Customs cash received into Treasury was $3,443,070.85. Strict non-loan cash receipts were $3,670,492.36. The $4,240 sale of arms and accoutrements is an asset-sale inflow and therefore enters the usable-inflow denominator but not the strict non-loan denominator. Usable inflows were $4,777,230.81 after adding $1,102,498.45 of genuine loan proceeds and the $4,240 asset sale.

The $4 million Bank subscription loop and the opening Treasury balance are excluded from both denominators.

Debt-service cash was $3,067,104.53:

- public-debt interest: $2,374,054.28;
- reduction of public debt: $257,786.42;
- French-debt principal paid from foreign funds: $435,263.83.

The French payment remains in `D_c` because the ratio measures total recorded cash debt service relative to customs cash. It does not prove that domestic customs receipts financed that foreign-funded payment.

## Admission limitation

The 1792 transcriptions were checked visually and against OCR and reconcile arithmetically. OCR is not an independent image reading. Under the precommitted admission rule, the period remains provisional until a second independent image verification confirms every included component and records the result in `sources/p1-verification-log.csv`.

## Coverage consequence

Current admissible annual-equivalent coverage is zero in every window. The quarterly controls receive no annual-equivalent credit and are not analytically admitted until an attributable independent check is retained.

P1 remains `insufficient_coverage`. None of the observed ratios should be described as a P1 pass.

## Next evidence gate

1. Obtain an attributable independent re-read of the 1792, 1797 Q4, and 1798 Q1 included components; record verifier identity and date.
2. Inspect NARA RG 217 abstracts and T964 when available.
3. Inspect LOC MSS83125 shelf 24,495 for 1789–1790.
4. Locate exact supporting annual accounts behind the 1801–1803 Treasury narratives.
