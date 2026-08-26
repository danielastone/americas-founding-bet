# London credit-crisis layer

## Scope

Treat two shocks separately:

1. **1792–1793 commercial-credit crisis:** war shock, returned and unmarketable bills, merchant and bank failures, credit contraction, and government support through Exchequer bills.
2. **1796–1797 monetary and credit crisis:** land-credit failures, bullion drain, bank runs, suspension of Bank of England cash payments, and transition into the Restriction Period.

Calling both events one London crisis would obscure timing and mechanism. The 1793 event was a commercial-bill and liquidity crisis with broad British regional effects; the 1797 event changed the monetary regime and interacted with an American land-credit collapse.

## Transmission chain

| Link | Observable evidence |
|---|---|
| Caribbean or American merchant draws bill | Bill, invoice, ledger, shipment, acceptance |
| London house accepts or discounts bill | Acceptance book, correspondence, discount record |
| Commodity shipment or remittance underperforms | Price, cargo loss, seizure, delay, protested bill |
| Acceptance chain loses liquidity | Discount refusal, higher rate, shorter tenor, collateral demand |
| Merchant or bank fails | Bankruptcy, assignment, creditor schedule, directors’ minutes |
| British policy intervenes | Exchequer-bill records, Bank minutes, Privy Council order, statute |
| Shock reaches United States | Merchant letters, exchange rates, bank discounts, defaults, imports and exports |

## Credit-instrument table

- `credit_record_id`
- `source_id`
- `document_date`
- `shock_episode`
- `instrument_type`
- `drawer`
- `drawee`
- `acceptor`
- `endorser`
- `holder`
- `principal_original`
- `currency_original`
- `issue_date`
- `maturity_date`
- `tenor_days`
- `discount_rate`
- `exchange_rate`
- `collateral`
- `commodity_or_voyage_id`
- `payment_status`
- `protest_date`
- `bankruptcy_or_assignment`
- `location`
- `archive_series`
- `container_or_volume`
- `page_or_folio`
- `observed_or_inferred`
- `notes`

## First controlled test

Build two event windows: 1792–1794 and 1796–1798. Trace named London acceptors and American or West Indian counterparties found in Dutilh & Wachsmuth, Backus, sugar-trade, and voyage records. Record whether credit terms, remittance instructions, shipment timing, commodity prices, or defaults changed.

## Empirical outcomes

- bills protested or returned unpaid;
- discount availability and rates;
- bill tenor and collateral requirements;
- sterling-dollar exchange rates;
- merchant failures and assignments;
- shipping, imports, and exports;
- commodity prices and inventories;
- bank discounts and specie conditions in American ports.

## Identification limits

- War, seizures, embargoes, harvest failures, and the Haitian Revolution moved trade and credit simultaneously.
- Merchant failures are selected observations; surviving bankruptcies omit firms that contracted quietly.
- London credit, British regional banking, Amsterdam finance, and American banking are connected but not interchangeable.
- A protested bill may reflect the drawer, acceptor, cargo, exchange market, or legal disruption; cause must be evidenced.
- The American land bubble and London restriction interacted. Treating the 1797 American crisis as wholly imported would be wrong.
- Plantation land and enslaved people functioned as collateral and sources of payment; the financial layer cannot be separated from slavery.
