# Data directory governance

This directory separates analytical data from staging and control files. A filename's presence does not make it admissible evidence.

## Canonical analytical table

- `p1-federal-fiscal-observations.csv` is the sole canonical P1 federal fiscal observation table.
- Rows used analytically must retain assertion-specific provenance, accounting state, evidence state, verification status, and canonical source identifiers.
- Derived ratios must be reproducible from the canonical table through `p1-ratio-component-map.csv`.

## Derived analytical outputs

- `p1-period-ratios.csv`: governed period results; coverage is the sum of `coverage_credit`, never a count of `annual_equivalent=yes` rows.
- `p1-ratio-component-map.csv`: numerator and denominator membership.
- `p1-proxy-sensitivity.csv`: explicitly labeled proxy sensitivity results.

These files are outputs or mappings, not alternate observation tables.

## Noncanonical staging

- `p1-endpoint-staging.csv`: 1801–1803 endpoint extracts retained for reconciliation.
- `early_customs_1789_1790.csv`: accrued and collector-return customs measures that are not yet Treasury-cash compatible.

Staging rows may not feed ratios directly. They must first be reconciled to the accounting specification, assigned canonical source identifiers, satisfy evidence and verification requirements, and then be migrated into `p1-federal-fiscal-observations.csv`. Duplicate migration is prohibited.

## Control and legal context

- `p1-decision-thresholds.csv`: precommitted decision rules.
- `customs_law.csv`: legal chronology and classifications.

These control interpretation; they are not fiscal observations.
