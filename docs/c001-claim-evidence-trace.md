# Claim AFB-C001 — end-to-end evidence trace

## Claim under test

> Customs cash was the dominant usable federal revenue supporting debt service during 1789–1803.

This sentence contains two analytically distinct propositions:

1. **P1 dominance:** realized customs cash exceeded the precommitted share threshold in consistently defined federal receipt denominators.
2. **P3 liquidity/support:** customs cash arrived in time, and with sufficient regularity, to support scheduled debt service without chronic emergency bridging.

A high annual customs share does not establish the second proposition. The repository must issue separate P1 and P3 decisions before treating AFB-C001 as supported.

## Trace

| Link | Repository requirement | Evidence currently present | Admission result |
|---|---|---|---|
| Claim | AFB-C001 in `claims/claim-register.csv` | Claim is specified; no pass/fail decision | Not tested |
| Falsification rule | P1 and P3 in `docs/falsification-priorities.md` | Separate dominance and timing failure conditions are precommitted | Design present |
| Source register | Treasury/FRASER/ASP/NARA records | Central Treasury accounts identified for isolated periods; E1 central-account series still unresolved | Partial |
| Customs numerator | Realized customs cash received into Treasury | Exact 1792, Q4 1797, and Q1 1798 controls; exact/rounded endpoint components staged | Provisional only |
| Complete strict denominator | All compatible non-loan federal cash receipts | Complete only for the provisional 1792 control; 1801–1803 denominators remain incomplete | Coverage failure |
| Complete usable-inflow denominator | Strict receipts plus borrowing and asset-sale proceeds | 1792 mapped provisionally; annual loan/asset flows unresolved elsewhere | Coverage failure |
| Debt-service numerator | Compatible interest and principal cash payments | 1792 provisional purpose-side total and two quarterly controls; full annual series absent | Partial |
| Timing bridge | Remittances, balances, bond maturities, due dates, short-term borrowing and delays | No admitted 1789–1803 timing panel | Missing |
| Decision | Required coverage across three windows | 0 of 9 annual-equivalent periods; zero in every required window | Cannot pass or fail |

## First material break

The chain breaks at **temporal and denominator coverage**, not at arithmetic. The repository can reproduce several favorable ratios, but it cannot yet estimate the claim over 1789–1803. Treating the available periods as evidence of persistence would convert source survival into a sampling rule.

The claim's phrase “supporting debt service” is also too compressed. `D_c = debt service/customs cash` is a burden comparison, not a cash-tracing or timely-payment test. Q4 1797, where `D_c = 119.76%`, demonstrates why annual or quarterly shares cannot substitute for a liquidity reconstruction.

## Required evidence assessment

The claim register lists reconciled Treasury receipts, customs assessments, bonds, cash collection, and debt-service accounts. Their present status is:

- **Reconciled Treasury receipts:** partial and period-sparse.
- **Customs assessments:** available as noncash staging evidence for early periods; not interchangeable with Treasury cash.
- **Bonds and maturities:** not assembled into an admitted timing series.
- **Cash collection:** present for isolated periods, not a designed 1789–1803 panel.
- **Debt-service accounts:** partial; period and purpose compatibility remain uneven.
- **Contradicting evidence:** the 1797 Q4 liquidity mismatch is recorded but not yet tested within P3.

## Decision

**AFB-C001 remains untested.** The current evidence supports only this narrower statement:

> In the three source-available provisional controls currently computed, customs comprised more than half of the specified receipt denominators.

That statement is descriptive, availability-conditioned, and insufficient for the registered claim.

No claim-status promotion, evidence-state promotion, or coverage credit is warranted.

## Next decisive action

Do not add another convenient FRASER period. Resolve the central annual-account series or an equivalent designed source frame capable of supplying complete, compatible annual denominators across the precommitted windows. If that fails, record a coverage failure and narrow the claim rather than filling the gap with heterogeneous proxies.
