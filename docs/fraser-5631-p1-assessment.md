# FRASER item 5631 P1 statement assessment

## Decision

Inventory complete; numeric admission is not complete.

FRASER item 5631 is a 93-image compilation published as *Report on Finances*. The item label “1792” does not mean every table is an annual 1792 cash account. The compilation contains multiple congressional communications and Treasury statements prepared in 1793, plus earlier-period and forward-looking material.

The statement inventory is in `sources/fraser-5631-p1-statement-inventory.csv`.

## Primary P1 candidates

### Statement A, PDF ordinal image 17 (extractor index 16)

The *General account of Receipts and Expenditures of Public Moneys* covers January 1–December 31, 1792. Hamilton describes it as receipts into and expenditures from the Treasury corresponding with the Treasurer’s accounts.

This is the primary candidate for the 1792 cash-flow denominator, subject to:

- separating the opening balance from 1792 inflows;
- separating customs cash from internal revenue and miscellaneous receipts;
- separating domestic and foreign loan proceeds from revenue;
- separating the Bank-stock subscription accounting loop;
- verifying every value twice from the page image;
- preserving that the fourth-quarter account was rendered but not yet formally settled when transmitted.

### Appropriation and expenditure statement, PDF images 41–43

This statement separates statutory appropriations, payments during 1792, and unexpended balances. Only the payments column is a candidate for cash uses. Appropriations are legal authority, not disbursements.

## Reconciliation-only statements

Statements B and Ba are not alternate versions of annual cash revenue. They mix:

- actual Treasury receipts;
- estimated revenue products;
- outstanding customs and internal-revenue obligations;
- domestic loans;
- foreign-loan proceeds;
- cash balances;
- cumulative expenditures from the beginning of the government.

They can test the completeness and internal logic of Statement A, but they cannot enter the primary P1 ratio without component-level accounting-state classification.

## Explicit exclusions

- Collector balances in Statement D are local custody, not Treasury receipts.
- Customs bonds in Statement E are bonded obligations, not cash.
- The revenue-on-spirits account in Statement F mixes cash, expenses, accrued duties, estimates, and outstanding credits.
- Statements IV and V are balance snapshots, not receipt flows.
- The revenue-and-appropriations statement on image 40 mixes estimated products with legal appropriations.
- The probable cash statement on image 55 is a forecast and belongs to ex-ante risk and P3 timing analysis.

## Cross-reference problem

The narrative says Statement AB appears elsewhere as document No. 44, printed page 188. It is not reproduced as a separately labeled table within the immediate Statement A–F sequence. Its bank balances may be used only through an exact image citation to the referenced document, not by silently treating the summary in Statement B as the missing table.

## Image-number rule

Repository citations distinguish human-facing PDF ordinal images from zero-based extractor indexes and printed American State Papers pagination. For Statement A, extractor index 16 corresponds to PDF ordinal image 17 and printed ASP page 195. The stable image URL remains mandatory.

## Next extraction order

1. Obtain an attributable independent image verification of Statement A, PDF ordinal image 17 (extractor index 16).
2. Preserve the completed arithmetic reconciliation while keeping analytical admission provisional.
3. Double-transcribe the payments column on images 41–43.
4. Use B/Ba only to explain differences.
5. Transcribe Statement F components only if needed to separate noncustoms cash from accrued internal revenue.

No `C_s`, `C_u`, or `D_c` value is computed at this stage.
