# Federal debt layer

## Core question

Did federalization and funding of public debt create durable fiscal capacity, credible securities, and lower financing constraints—or merely convert old obligations into a larger centralized balance sheet?

The answer cannot come from the debt balance alone. Assumption increased reported federal debt while potentially improving payment regularity, marketability, and national fiscal control.

## Debt architecture

| Component | Required distinction |
|---|---|
| Inherited foreign debt | Creditor country, currency, interest, arrears, remittance and refinancing |
| Domestic federal debt | Original certificates, accrued interest, subscribed stock and unsubscribed claims |
| Assumed state debt | State of origin, quota, eligible securities, subscription and final settlement |
| New borrowing | Purpose, authorization, lender, currency, proceeds, fees and maturity |
| Debt service | Interest paid, principal redeemed, arrears and payment location |
| Sinking-fund activity | Cash spent, face value purchased, market price and stock type |
| Market performance | Bid/ask or transaction price, yield, liquidity, volatility and holder |

## Instrument table

- `instrument_id`
- `source_id`
- `instrument_name_original`
- `instrument_type`
- `federal_state_or_foreign_origin`
- `original_obligation_date`
- `funding_or_issue_date`
- `subscription_date`
- `creditor_or_holder`
- `principal_face_value`
- `currency_original`
- `interest_rate_current`
- `interest_rate_deferred`
- `interest_start_date`
- `maturity_or_redemption_terms`
- `market_price`
- `market_price_basis`
- `cash_proceeds_or_cost`
- `accrued_interest`
- `payment_status`
- `redemption_date`
- `statutory_authority`
- `archive_series`
- `container_volume_or_page`
- `notes`

## Fiscal-flow table

- `flow_id`
- `date_or_period`
- `flow_type`
- `instrument_id`
- `cash_amount`
- `currency_original`
- `face_value_affected`
- `interest_or_principal`
- `revenue_source`
- `paying_agent`
- `payment_location`
- `domestic_or_foreign`
- `appropriation_or_fund`
- `source_id`
- `page_or_folio`
- `notes`

## Required measures

- debt outstanding by instrument and origin;
- cash interest paid and effective interest cost;
- arrears and deferred interest;
- debt service divided by federal revenue;
- customs revenue pledged to debt service;
- market value versus face value;
- face value retired per dollar spent;
- maturity and currency exposure;
- foreign versus domestic creditor concentration;
- debt service relative to exports and nominal economic scale, with denominator uncertainty disclosed.

## First controlled test

Reconcile 1789 obligations to the funded stocks created under the 1790 act. Then reconstruct 1790–1795 subscriptions, interest payments, sinking-fund purchases, foreign refinancing, and remaining unfunded claims. The annual Historical Debt Outstanding series is only a control total, not the analytical dataset.

## Hypotheses

1. Funding and regular interest payments raised federal security prices and reduced financing constraints.
2. Assumption centralized fiscal authority and linked creditor interests to the federal government.
3. Customs capacity made the funding system credible by supplying a visible revenue stream.
4. Open-market purchases below par retired face value efficiently but could also support security prices.
5. Improved public credit increased wartime and acquisition capacity, including later Louisiana financing.

## Identification limits

- Rising security prices may reflect peace, liquidity, speculation, or European capital conditions—not only policy credibility.
- Debt assumption changed both the federal numerator and state liabilities; consolidated government debt is the relevant comparison.
- Face value is not market value, cash proceeds, or fiscal burden.
- Paying interest reliably is different from reducing principal.
- Federal debt holders were not the public as a whole; distributional incidence requires ownership and tax evidence.
- Revenue pledges rested heavily on customs and therefore on Atlantic trade, slavery-linked commodities, and geopolitical stability.
