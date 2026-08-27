# FRASER 5631 Statement A reconciliation

## Source

- Item: FRASER 5631
- Statement: A, *General account of Receipts and Expenditures of Public Moneys*
- Printed date: January 28, 1793
- Period: January 1–December 31, 1792
- Stable image: PDF image 17 / printed American State Papers page 195
- Repository observations: `AFB-P1OBS-0001` through `AFB-P1OBS-0019`

## Verification

One direct visual transcription was cross-checked against FRASER's searchable text extraction. The searchable text is an OCR-derived aid, not an independent image reading. All thirteen credit-side entries and five debit-side entries agree across the visual transcription and OCR cross-check, but an attributable independent image verification remains pending.

- Credit-side sum: $9,751,136.56
- Debit-side sum including closing balance: $9,751,136.56
- Printed control total: $9,751,136.56
- Arithmetic discrepancy: $0.00

This satisfies the within-statement tolerance. It does not make every component admissible for the P1 ratios.

## Receipt classification

The opening Treasury balance of $973,905.75 is a stock carried from 1791, not a 1792 receipt.

The page reports identifiable 1792 Treasury receipts for:

- recoveries and balances;
- an asset sale;
- fines, penalties, and forfeitures;
- ordinary domestic and foreign loan proceeds;
- Bank dividend excess;
- distilled-spirits revenue;
- customs and tonnage.

## Four-million-dollar accounting loop

Two credit entries total $4,000,000:

- $2,000,000 in Amsterdam bills associated with the federal subscription to Bank stock;
- $2,000,000 described as a matching Bank of the United States loan.

The footnote states that the June and September expenditure quarters include $4,000,000 of warrants drawn to effect the subscription and cover the resulting loan, and that the bills were exchanged and the warrants canceled at the Treasury because the transactions were predicated.

Therefore:

- the two $2,000,000 credit entries remain visible;
- they are classified as `accounting_loop`;
- they are excluded from both `C_s` and `C_u` pending instrument-level reconstruction;
- the June and September aggregate expenditure rows cannot establish cash debt service.

Treating the entries as ordinary loan cash would inflate usable inflows by $4,000,000 and mechanically depress the customs share.

## Provisional receipt controls

After removing only the opening balance and the $4,000,000 accounting loop:

- candidate 1792 cash inflows: $4,777,230.81;
- customs and tonnage received into Treasury: $3,443,070.85;
- provisional customs share of candidate usable inflows: approximately 72.07 percent.

This is an arithmetic control, not an admitted `C_u`. It remains provisional until the other receipt components and the Bank-stock loop are reconciled against Statements B/Ba and the relevant loan documents.

For the non-loan denominator, asset sales and recoveries require the policy fixed in the P1 specification; no `C_s` is admitted here.

## Expenditure limitation

Statement A provides quarterly total expenditures, not purpose-level debt service. The second and third quarters contain the canceled-warrant accounting loop. The fourth quarter had been rendered for settlement but was still under examination when transmitted.

Consequently, Statement A alone cannot produce `D_c`.

## Decision

Statement A reconciles arithmetically and has one direct visual transcription plus an OCR cross-check. It does not yet pass the project's independent-image-verification gate. Thirteen substantive receipt entries, four quarterly expenditure totals, one closing balance, and one control total are preserved in the canonical table, provisionally. P1 classification remains blocked.
