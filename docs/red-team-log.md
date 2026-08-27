# Red-team log — America's Founding Bet

**Repository:** `danielastone/americas-founding-bet`  
**Assessment started:** 2026-08-27  
**Last updated:** 2026-08-27

## Scope

This project is a **pre-conclusion research design**, not a finished argument. The claim register currently contains six `specified` claims and one `deferred` claim. None is marked tested, passed, or failed.

The red-team target is therefore the testing apparatus and its early execution—not a thesis that the repository has not yet earned.

## Phase 0 — Orientation (complete)

Reviewed:

- `README.md`
- `claims/claim-register.csv`
- `docs/falsification-priorities.md`
- `docs/audit-remediation-2026-08-26.md`
- `docs/p1-federal-fiscal-table.md`
- `docs/p1-period-results.md`
- `data/p1-period-ratios.csv`

### Strengths observed

- The falsification priorities specify failure conditions and research priority before a complete result exists.
- The P1 results are not presented as a thesis-level pass despite all three calculated ratios exceeding the 50 percent numerical threshold.
- The remediation log records unresolved source, transcription, and thematic coverage gaps.

### Current governance status

Subsequent repository repair materially narrowed the early-result claims:

- no P1 observation is currently `analysis_ready`;
- 71 canonical observations are `normalized`;
- nine quarterly component observations are `validated` but not analytically admitted;
- all six period-level threshold labels are `provisional_pass`;
- total machine-readable coverage credit is 0 of the required 9 annual-equivalent periods;
- coverage credit is zero in all three required windows;
- the 1797 Q4 and 1798 Q1 controls were demoted because the purported independent image checks do not identify an attributable verifier.

### Open questions

1. **Period-selection risk.** The three calculated periods appear driven by source availability rather than a designed panel. Availability bias can resemble favorable selection even without intentional cherry-picking.
2. **1797 Q4 liquidity signal.** `D_c = 119.76%` means recorded quarterly debt service exceeded customs cash. This belongs in the separate P3 timing and liquidity test; it is not evidence against P1 by itself.
3. **Independent verification.** The repository now correctly blocks analytical admission, but an attributable second check remains outstanding.
4. **Source transcription.** Reproducible arithmetic does not prove that the underlying image transcriptions are correct.

## Phase 1 — Verify 1792 P1 arithmetic (complete)

### Procedure

Recomputed the 1792 aggregates from:

- `data/p1-federal-fiscal-observations.csv`;
- `data/p1-ratio-component-map.csv`;
- `data/p1-period-ratios.csv`.

All amounts were converted to integer cents before summation. No binary floating-point values were used for the dollar controls.

### Component reconstruction

| Measure | Reconstructed | Reported | Variance |
|---|---:|---:|---:|
| Customs cash | $3,443,070.85 | $3,443,070.85 | $0.00 |
| Strict non-loan cash receipts | $3,670,492.36 | $3,670,492.36 | $0.00 |
| Usable cash inflows | $4,777,230.81 | $4,777,230.81 | $0.00 |
| Debt-service cash | $3,067,104.53 | $3,067,104.53 | $0.00 |

### Ratio reconstruction

| Ratio | Reconstructed | Stored |
|---|---:|---:|
| `C_s` | 0.9380405985 | 0.93804061 |
| `C_u` | 0.7207252458 | 0.72072525 |
| `D_c` | 0.8908049423 | 0.89080494 |

The differences are limited to rounding at the eighth decimal place.

### Statement A control

The broader Statement A control also reconciles exactly:

| Side | Reconstructed | Printed control | Variance |
|---|---:|---:|---:|
| Opening balance plus recorded receipt-side components | $9,751,136.56 | $9,751,136.56 | $0.00 |
| Quarterly expenditure totals plus closing balance | $9,751,136.56 | $9,751,136.56 | $0.00 |

The component map deliberately excludes the opening balance and the $4 million Bank-subscription accounting loop. It includes the $4,240 arms sale only in usable inflows, not in the strict non-loan denominator.

### Red-team conclusion

**Arithmetic result: pass.** The stored 1792 aggregates and ratios are reproducible from the declared component map.

**Evidence result: still provisional.** This phase does not establish:

- correctness of the underlying image transcription;
- attributable independent verification;
- denominator completeness beyond the mapped statement;
- representativeness of 1792;
- that customs financed each debt-service payment.

The last limitation matters because `D_c` includes $435,263.83 of French-debt principal paid from foreign funds. The ratio is a burden comparison, not a tracing claim.

No P1 coverage credit is created by this arithmetic check.

## Remaining plan

- [x] Phase 0: Orientation
- [x] Phase 1: Verify 1792 P1 arithmetic
- [ ] Phase 2: Test source-register integrity claims against `sources/source-register.csv`
- [ ] Phase 3: Spot-check FRASER 5631, 5636, and 5637 reconciliation claims
- [ ] Phase 4: Trace one registered claim through required evidence, sources, data, and admission
- [ ] Phase 5: Synthesize a balanced overall assessment
