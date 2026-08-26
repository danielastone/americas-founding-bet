# Alternate source strategy for early customs cash

## Finding

No identified online dataset independently supplies verified customs cash received by the Treasury for 1789–1790. Most easily found figures are either duties accrued, duties arising from collector returns, or later retrospective tables. Treating any of them as cash would reproduce the exact error the audit is designed to prevent.

The viable replacement is a three-sided reconciliation:

1. central Treasury postings;
2. collector-side receipts and remittances;
3. independent institutional or retrospective checks.

## Ranked source routes

### 1. Register's daybook and central abstracts

The strongest alternate access point is NARA microfilm T964, *Day Book of the Register's Office of the Treasury, 1789–1791*. It may reveal dated posting logic at the start of the federal government. The broader RG 217 abstracts of receipts and expenditures remain the best denominator candidate.

These are not two independent datasets if the abstracts were compiled from the daybook. Their value is different granularity, not independent confirmation.

### 2. Collector-side financial records

RG 36 customhouse records can test whether a central posting represents cash collected, bonds accepted, drawbacks, expenses, or a remittance. The trap is survival bias: available records differ sharply by port. No port sample should be selected until the repository has a district-series survival matrix.

### 3. Treasury-collector correspondence

RG 56 and microfilm M178 can explain missing returns, delayed remittances, defaults, bonding, and accounting instructions. Correspondence is mechanism evidence, not a denominator. A letter saying collectors were ordered to remit does not prove that they did.

### 4. Library of Congress Treasury records

The container list identifies one critical candidate: *U.S. Finance, tabular extracts of receipts and expenditures of the United States Treasury, 1784–1790*, available only on microfilm, shelf 24,495. It directly overlaps the unresolved opening years, but its provenance and accounting basis remain unknown. It may be an independent survival, a fair-copy extract, or another derivative of the central Treasury books.

The rest of MSS83125 is not a coherent fiscal series. Relevant supporting items are Box 1 appropriations and circulars, Box 3 general correspondence for 1789–1802, and the Box 4 letterbook. The 1790 loan certificates and 1799–1803 Virginia loan-office stock abstract are financing evidence, not operating receipts. See `sources/loc-treasury-container-map.csv`.

Hamilton collections at LOC and NYPL are searchable complements for specific collectors and reporting problems, but their selective correspondence cannot establish national totals.

### 5. Bank records

First Bank of the United States statements can constrain aggregate Treasury deposits and liquidity after 1791. They cannot normally identify the customs share of a deposit balance, and they do not solve the opening 1789–1790 gap.

### 6. Later Treasury tables

The 1897 Treasury Table K series is useful for anomaly detection and completeness checks. It is not an independent primary series until its accounting basis and source lineage are established.

## Minimum admission test

A candidate amount enters the federal cash dataset only if the source establishes:

- the posting or receipt date;
- the receiving entity or account;
- the revenue classification;
- whether the amount is cash rather than a bond or accrued duty;
- the period and geographic coverage;
- treatment of drawbacks, refunds, expenses, loans, and opening balances.

Failure on any field keeps the amount in staging.

## Next action

Wait for NARA's response on RG 217 identifiers while pursuing two microfilm routes: LOC shelf 24,495 for the 1784–1790 tabular extracts and NARA T964 for the 1789–1791 Register daybook. First determine whether LOC microfilm can be borrowed through interlibrary loan or reproduced. Do not start broad transcription of Boxes 1–4 or Hamilton papers; inspect those only when the central tables reveal a specific accounting ambiguity.
