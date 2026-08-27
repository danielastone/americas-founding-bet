# 1802 P1 proxy sensitivity

## Decision

The 1802 report cannot produce a primary annual ratio, but it can support a transparent proxy and a falsification threshold. The proxy receives no annual-coverage credit.

Machine-readable scenarios are in `data/p1-proxy-sensitivity.csv`.

## Known-components proxy

Known Treasury cash and asset inflows are:

- customs: $12,280,000.00;
- postage: $50,500.00;
- land specie: $179,575.52;
- Bank-share sale applied to bank debt: $1,287,600.00.

Using only those components gives:

- `C_s = 98.16%`;
- `C_u = 89.00%`.

These are upper-biased customs shares because acknowledged receipt categories are missing.

## Arrears stress scenario

The report identifies closing stocks of approximately:

- $400,000 in direct-tax arrears;
- $700,000 in internal-duty arrears.

Adding the entire $1.1 million to the annual denominator as if it had been received during the year produces:

- `C_s = 90.23%`;
- `C_u = 82.43%`.

This is an illustrative stress scenario, not a lower bound. Closing arrears are amounts still uncollected, not an upper limit on amounts collected during the preceding year.

## Falsification thresholds

Given the known components:

- additional unreported non-loan cash would need to equal **$12,049,924.48** to reduce `C_s` to 50 percent;
- additional unreported receipts or financing would need to equal **$10,762,324.48** to reduce `C_u` to 50 percent after including the Bank-share sale.

These are break-even requirements, not claims that the missing flows were smaller.

## Interpretation

The proxy makes customs dominance difficult to overturn quantitatively, but it does not solve the evidence problem. The missing categories are not exhaustively bounded, the customs figure is rounded, and the report has a separate $166,612.50 debt-service discrepancy.

The correct conclusion is:

> 1802 strongly supports customs dominance in sensitivity analysis, but remains inadmissible as a primary annual observation.

Using this proxy toward the nine-period coverage floor would violate the precommitted source and completeness rules.
