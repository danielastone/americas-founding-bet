# First Bank of the United States layer

## Research question

Did the First Bank of the United States convert federal fiscal capacity into a more integrated payments and credit system, and if so, which merchants, ports, and regions gained access?

The layer links federal debt, European financing, customs revenue, merchant finance, and port trade. It treats the Bank as a federally chartered, privately capitalized commercial bank with public functions—not as a modern central bank.

## Claims that require separate tests

| Claim | Evidence required |
|---|---|
| The Bank strengthened Treasury operations | Government deposits, transfers, collections, payments, and correspondence |
| The Bank integrated payments across ports | Branch remittances, inter-branch balances, note acceptance, exchange rates, and transfer costs |
| The Bank expanded merchant credit | Discount ledgers, borrowers, endorsers, maturity, collateral, renewals, and repayment |
| The Bank stabilized markets | Lending or purchases around identifiable shocks, compared with market prices and non-Bank credit |
| The Bank privileged insiders | Subscriber, director, borrower, endorser, and political-network overlap |
| The Bank monetized federal debt | Subscription payment records and the use, valuation, and financing of federal securities |
| Banknotes functioned as national money | Issuance, redemption, geographic circulation, discounts, counterfeits, and acceptance—not charter authority alone |

## Institutional mechanism

1. Congress authorizes a twenty-year corporation and a fixed capital structure.
2. Private subscribers and the United States acquire shares under specified payment terms.
3. The Bank accepts government and private deposits.
4. Its Philadelphia office and branches conduct discounts, payments, remittances, and note redemption.
5. Treasury uses the Bank in collecting, holding, transferring, and disbursing federal funds.
6. Merchants use discounts and Bank liabilities alongside bills of exchange, book credit, specie, and state-bank notes.
7. Governance rules, lending limits, specie constraints, and Treasury oversight shape risk and access.
8. Market shocks reveal whether the institution absorbs liquidity pressure, transmits it, or protects selected counterparties.

## Historical boundary

Do not call the First Bank a central bank unless a specific function is demonstrated. It lacked the later Federal Reserve's statutory mandate, nationwide reserve architecture, and monetary-policy machinery. “Quasi-central bank” is an interpretation, not a source category.

Do not confuse:

- The First Bank of the United States, chartered in 1791, with the Second Bank chartered in 1816.
- The Bank's charter with Hamilton's proposed design.
- Authorized capital with paid-in capital.
- Federal stock used in subscriptions with cash available for lending.
- A Bank note's face value with its observed market value or geographic acceptance.
- Treasury deposits with permanent fiscal resources.
- Discounts with long-term investment loans.
- Branch presence with equal regional access.

## Data model

### Bank institution table

| Field | Definition |
|---|---|
| bank_unit_id | Philadelphia office or identified branch |
| opening_date | Verified start of operations |
| location | City and state |
| directors | Directors with service dates |
| officers | President, cashier, and other officers |
| authorized_capital | Charter authority |
| subscribed_capital | Recorded subscriptions |
| paid_in_cash | Cash component actually paid |
| paid_in_securities | Federal stock component, par and market value separately |
| government_ownership | United States shares and changes |
| source_id | Provenance |

### Discount transaction table

| Field | Definition |
|---|---|
| discount_id | Stable project identifier |
| bank_unit_id | Office or branch |
| transaction_date | Discount date |
| maturity_date | Contractual due date |
| borrower | Named obligor |
| drawer / acceptor | Bill parties where applicable |
| endorsers | Each endorser as a separate linked actor |
| instrument_type | Note, bill of exchange, or other verified instrument |
| face_value | Original currency and unit |
| discount_rate | Stated rate |
| proceeds | Net funds advanced |
| renewal_flag | Whether renewed or rolled |
| purpose | Only when documented |
| collateral | Security where recorded |
| disposition | Paid, renewed, protested, defaulted, litigated, unknown |
| merchant_firm_id | Link to merchant layer |
| customs_obligation_id | Link to customs bond where supported |
| voyage_id | Link to voyage where supported |
| source_id / archive_reference | Item-level provenance |

### Treasury–Bank flow table

| Field | Definition |
|---|---|
| flow_id | Stable identifier |
| transaction_date | Accounting date |
| bank_unit_id | Receiving or paying office |
| treasury_account | Account title as recorded |
| flow_type | Deposit, customs receipt, transfer, disbursement, loan, dividend, stock subscription, or other |
| amount | Original currency and unit |
| origin_district | Customs or revenue source |
| destination | Payee, office, or account |
| settlement_method | Specie, banknote, draft, book transfer, or unknown |
| availability_date | When funds became usable, if recorded |
| source_id / archive_reference | Item-level provenance |

### Note and payment observation table

Record issuer, denomination, issue date, presentation place, redemption outcome, discount or premium, counterparty, counterfeit status, and source. A note-issue total alone cannot establish circulation or geographic integration.

## Key measures

- Government deposits and payments by Bank unit and month.
- Customs receipts transferred through the Bank.
- Time and cost to move public funds between customs districts and payment locations.
- Discounts outstanding, new discounts, maturities, renewals, protests, and losses.
- Borrower and endorser concentration.
- Shareholder–director–borrower overlap.
- Share of merchant customs obligations associated with Bank credit.
- Banknote redemption distance and observed discount from par.
- Branch-level balance flows and regional credit shares.
- Paid-in cash versus federal-security components of capital.
- Treasury dividends and financing costs relative to alternative arrangements.

## Hypotheses

1. The Bank reduced the time and cost of moving customs revenue from major ports to federal uses.
2. Branches and note redemption narrowed geographic payment discounts, but integration remained uneven.
3. Discounts helped established merchants bridge cargo purchase, customs-bond maturity, sale, and re-export proceeds.
4. Surety, endorsement, shareholder, and director networks concentrated credit access.
5. Federal securities used in subscriptions connected the funded-debt program to bank capitalization without creating an equal amount of fresh specie.
6. During the 1792 panic and later Atlantic credit shocks, the Bank's balance-sheet response affected liquidity, but the direction and distribution must be established rather than assumed.
7. Treasury dependence on one privileged bank created counterparty and political-governance risk alongside administrative efficiency.

## Source plan

- **AFB-S063:** code every charter provision governing capital, subscriptions, federal ownership, governance, branches, notes, lending constraints, specie, reporting, and duration.
- **AFB-S064:** extract Hamilton's intended mechanisms and convert each into a falsifiable claim.
- **AFB-S014–S015** and later issue-level Treasury reports: identify government deposits, dividends, loans, transfers, and public-funds balances.
- **AFB-S051–S061:** link the Bank to funding, sinking-fund, and European-financing operations.
- **AFB-S016**, **AFB-S021**, and **AFB-S062:** connect customs receipts and merchant duty obligations to payment timing.
- **AFB-S017–S020** and **AFB-S026–S027:** search merchant books and correspondence for Bank discounts, notes, deposits, endorsements, remittances, and refusals.
- **AFB-S065:** use only as orientation and a route to underlying records and scholarship.

A dedicated archival inventory is still required. The charter and Treasury reports cannot substitute for Bank ledgers, branch records, or merchant evidence.

## Identification strategy

### Before and after is insufficient

The Bank began amid simultaneous changes in debt funding, taxation, trade, European war, securities markets, and state banking. A national pre/post comparison would attribute too much to the Bank.

Prefer:

- Port-pair comparisons before and after branch entry.
- Transaction-level comparisons of Bank-linked and non-Bank merchant credit, with merchant and commodity controls.
- Event windows around branch openings and liquidity shocks.
- Network analysis of directors, subscribers, borrowers, endorsers, customs sureties, and federal contractors.
- Treasury-transfer comparisons across routes and periods with different Bank involvement.
- Banknote discount observations by distance from redemption offices.

### Main confounders

- Selection of branches into already important commercial cities.
- Selection of strong or connected merchants into Bank borrowing.
- Wartime trade shocks and neutral-carrier profits.
- Growth of state-chartered banks.
- Changes in tariff schedules and customs administration.
- Survivorship bias in Bank and merchant records.
- Federal patronage and political affiliation.
- Endogenous Treasury support to the Bank.

## Validation rules

- Preserve authorization, subscription, payment, and balance as different states.
- Preserve par, market, and book values of federal securities separately.
- Record each borrower, drawer, acceptor, and endorser as a distinct role.
- Treat discounts as short-term credit unless the instrument proves otherwise.
- Do not infer loan purpose from a merchant's occupation.
- Do not infer national note circulation from aggregate issuance.
- Do not treat an office-opening date as proof of material operations.
- Reconcile Treasury and Bank records without assuming common accounting periods.
- Label derived network links and assign matching confidence.
- Report archival gaps and politically salient cases that may be overrepresented.

## Falsification tests

The fiscal-integration claim weakens if transfers were not faster or cheaper, or if Treasury balances remained immobilized by geography. The merchant-credit claim weakens if Bank discounts merely displaced state-bank or private credit without reducing total financing costs. The national-money claim weakens if notes traded at material discounts away from redemption offices. The access claim weakens if borrower concentration is no greater than the underlying merchant population after controlling for scale and creditworthiness.

## Outputs

1. Charter-versus-Hamilton crosswalk.
2. Branch chronology with evidence-grade opening and operating dates.
3. Subscriber, director, officer, borrower, and endorser entity tables.
4. Treasury–Bank monthly flow panel.
5. Discount-transaction sample linked to merchants, customs obligations, and voyages.
6. Banknote acceptance and redemption observations.
7. Event studies for the 1792 panic and selected Atlantic credit shocks.
8. A distributional assessment of who obtained liquidity, who bore losses, and which regions remained outside the network.
