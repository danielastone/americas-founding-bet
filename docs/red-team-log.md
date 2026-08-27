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

## Phase 2 — Test source-register integrity claims (complete)

### Structural retest

The current `sources/source-register.csv` reproduces the audit document's stated structural results:

| Test | Retest result |
|---|---:|
| Source rows | 95 |
| Columns | 14 |
| Incorrect-width rows | 0 |
| Empty source IDs | 0 |
| Duplicate source IDs | 0 |
| Sequence gaps, AFB-S001–AFB-S095 | 0 |
| Required-field blanks under the published test | 0 |
| Malformed nonblank HTTP/HTTPS landing pages | 0 |
| Blank landing pages | 0 |
| Blank repository identifiers | 0 |

The controlled-value sets also match the audit:

- verification: `verified`, `needs-item-check`, `needs-series-check`;
- readiness: `discovery_only`, `item_identified`, `source_identified`.

The P1 metadata table accurately describes AFB-S087–AFB-S094. All canonical source IDs in the P1 source inventory and all 80 canonical observations join to the source register; orphan count is zero in both cases.

### Red-team findings

**Published structural claims: pass.** The audit document's numerical claims match the current CSV.

**Verification attribution: fail.** Eighty-nine register rows carry `verified`, but the schema stores no verifier identity, verification date, or verification-record foreign key. The label is not independently auditable and cannot support analytical admission.

**Evidentiary-origin control: incomplete.** Four landing pages are reused across 11 scoped entries:

- RG 36 guide: four entries;
- RG 26 guide: three entries;
- RG 53 guide: two entries;
- RG 217 guide: two entries.

These are legitimate scoped catalog entries rather than duplicate IDs. They are not independent sources, however, and the register has no machine-readable origin-group key preventing double-counting.

### Conclusion

The source-register audits are accurate within their expressly narrow structural scope. They do not validate titles, dates, creators, identifiers, destination content, source independence, or the meaning of `verified`.

The first substantive remediation need is an attributable metadata-verification record and an evidentiary-origin key. Neither gap changes P1 coverage, which remains zero.

## Phase 3 — Spot-check FRASER reconciliation claims (complete)

### Scope and method

A bounded source spot-check compared the repository's decisive claims for FRASER items 5631, 5636, and 5637 with the official FRASER page images/searchable PDFs. This was not a complete retranscription of every table.

| Item | Numerical/source result | Governance result |
|---|---|---|
| 5631 | Statement A's customs, internal-revenue, receipt-control, and expenditure-control figures reconcile to the printed source. | The assessment mixed zero-based extractor index 16 with PDF ordinal image 17, and OCR was described as an independent reading. Page labels and verification language were corrected. |
| 5636 | The 1793–1795 duties and drawback controls, the 1795 adjustment, and the cross-period drawback warning agree with the source. Arithmetic identifies the searchable-text value `2,890,334.40` as OCR corruption; the internally consistent printed component is `2,890,034.40`. | The second-pass record lacked an attributable verifier and was not an independent image check. Its claims and inventory admission labels were demoted. |
| 5637 | The two Treasury accounts support the transcribed Q4 1797 and Q1 1798 receipt controls and debt-service component sums. | The assessment and staging CSV still called the observations admissible/double-verified despite missing verifier attribution. Both were corrected to provisional. |

### Red-team conclusion

**Bounded numerical spot-check: pass.** No material arithmetic discrepancy was found in the decisive figures checked against the three official PDFs.

**Verification governance: fail, repaired at the labeling layer.** OCR/text extraction and unattributed second passes had been treated as independent verification. The affected documentation and staging metadata now state the narrower result: one source reading plus arithmetic/OCR controls, with attributable independent image verification still pending.

This phase creates no analytical admission, evidence-state promotion, or P1 coverage credit. The canonical ratios remain provisional and machine-readable coverage remains zero.

## Remaining plan

- [x] Phase 0: Orientation
- [x] Phase 1: Verify 1792 P1 arithmetic
- [x] Phase 2: Test source-register integrity claims against `sources/source-register.csv`
- [x] Phase 3: Spot-check FRASER 5631, 5636, and 5637 reconciliation claims
- [ ] Phase 4: Trace one registered claim through required evidence, sources, data, and admission
- [ ] Phase 5: Synthesize a balanced overall assessment
