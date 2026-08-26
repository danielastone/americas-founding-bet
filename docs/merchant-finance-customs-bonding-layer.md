# Merchant finance, customs bonding, and re-export layer

## Research question

How did customs credit, surety relationships, and drawback rules change the working capital, risk, and market reach of merchants in the early United States?

This layer joins four existing parts of the project: merchant records, customs administration, ship voyages, and Treasury revenue. Its central observation is that a duty assessed at entry was not necessarily cash collected at entry. A merchant could face a dated obligation supported by sureties, later discharge it, default, or qualify for a drawback after documented re-export.

## Historical boundary

Founding-era customs bonds must not be described as the modern federal bonded-warehouse system. The layer will first reconstruct the credit and re-export provisions actually in force under the collection statutes, especially the 1790 and 1799 acts. Later warehouse records may be useful for institutional comparison, but they cannot establish a 1790s mechanism without contemporaneous authority.

## Mechanism

1. A merchant finances or receives a cargo through cash, consignment, book credit, or bills of exchange.
2. The vessel and merchandise are entered at a customs district.
3. Customs values and classifies the goods and assesses duties.
4. The importer pays cash or executes the legally permitted bond, often with one or more sureties.
5. Goods are sold domestically, retained, or re-exported.
6. A qualifying re-export may generate a drawback or debenture after proof and administrative approval.
7. Customs records payment, discharge, cancellation, default, litigation, penalty, or refund.
8. Treasury cash revenue equals neither gross imports nor gross duties assessed; timing and drawbacks must be reconciled.

## Analytical distinctions

| Concept | Measure separately | Do not substitute |
|---|---|---|
| Import | Original customs entry and foreign value | Domestic production |
| Duty assessment | Legal liability at entry | Cash receipt |
| Customs bond | Principal, sureties, maturity, installments, disposition | Revenue already collected |
| Re-export | Foreign merchandise exported after import | Domestic export |
| Drawback | Amount claimed, allowed, and paid | Automatic recovery of the original duty |
| Net customs revenue | Cash collected less refunds and drawbacks for the chosen accounting period | Statutory rate multiplied by gross trade |
| Merchant credit | Supplier credit, bills, consignment, insurance, and customs credit | A single undifferentiated balance |
| Warehousing | Contemporaneous legal and administrative arrangement | The later federal bonded-warehouse regime |

## Data model

### Customs obligation table

| Field | Definition |
|---|---|
| customs_obligation_id | Stable project identifier |
| source_id | Link to the source register |
| district_port | Customs district and port |
| entry_date | Date merchandise was entered |
| importer | Legally recorded importer |
| consignee | Consignee, if different |
| merchant_firm_id | Link to merchant entity table |
| surety_1 / surety_2 | Named guarantors |
| vessel_voyage_id | Link to voyage layer |
| cargo_line_id | Link to commodity line |
| entered_value | Customs value with original unit |
| duty_rate | Rate and statutory basis |
| duty_assessed | Gross liability |
| cash_paid_at_entry | Cash paid on entry |
| bond_principal | Face amount of bond |
| bond_date | Execution date |
| maturity_date | Contractual due date |
| installments | Dates and amounts if applicable |
| bond_type | Duty, re-export, embargo, or other verified type |
| disposition | Paid, discharged, cancelled, defaulted, litigated, unknown |
| disposition_date | Date of final recorded action |
| penalty_cost | Penalty, legal cost, or forfeiture |
| archive_reference | Series, volume, container, page, image, or item |

### Re-export and drawback table

| Field | Definition |
|---|---|
| reexport_id | Stable project identifier |
| original_entry_id | Link to original import entry |
| original_cargo_line_id | Link to the same merchandise where traceable |
| import_origin | Foreign origin recorded at import |
| arrival_date | Initial United States arrival |
| reexport_date | Export date |
| export_port | Customs district of re-export |
| export_voyage_id | Link to outbound voyage |
| destination | Recorded foreign destination |
| quantity_imported | Original quantity and unit |
| quantity_reexported | Re-exported quantity and unit |
| time_in_us_days | Derived interval |
| drawback_claimed | Amount claimed |
| drawback_allowed | Amount approved |
| drawback_paid | Cash payment and date |
| debenture_id | Identifier for the customs instrument |
| retained_duty | Duty ultimately retained, where reconcilable |
| proof_reference | Export certificate, manifest, oath, inspection, or related proof |
| matching_confidence | Exact, probable, possible, or unmatched |

### Merchant financing link table

Record invoices, bills of exchange, insurance, freight, commissions, supplier credit, sale proceeds, and customs obligations as separate instruments. Link them through merchant, voyage, cargo, date, and counterparty rather than forcing them into one account balance.

## Proposed measures

- Bonded share of assessed duties.
- Median days from entry to duty payment.
- Surety-network concentration by port.
- Bond default and delinquency rates.
- Re-export share of foreign merchandise by commodity and destination.
- Drawback claimed, allowed, paid, and processing time.
- Net duty retained per imported dollar.
- Merchant working-capital exposure: cargo cost plus freight, insurance, and duty cash paid, less supplier credit and unpaid customs bonds.
- Re-export margin after freight, insurance, commissions, storage, duty retained, and drawback delay.

## Hypotheses

1. Customs credit reduced immediate cash requirements and increased merchants' capacity to carry inventories.
2. Access was unequal because acceptable sureties and established customs relationships favored connected firms.
3. Drawbacks supported entrepôt trade by reducing the duty cost on foreign goods subsequently exported.
4. Re-export activity made gross import and export totals overstate domestic absorption and production.
5. Commercial crises increased late payment, default, forced sale, and reliance on sureties.
6. Administrative delay in drawback payment could offset part of the formal benefit by tying up working capital.

## Source plan

- Use **AFB-S036** and **AFB-S013** to index the precise bonding, entry, proof, drawback, penalty, and enforcement provisions of the 1790 and 1799 collection statutes.
- Use **AFB-S016**, **AFB-S021**, and **AFB-S062** to identify port-level bond books, impost accounts, manifests, drawback or debenture records, and related correspondence.
- Use **AFB-S014** and issue-level Treasury reports to reconcile assessments, receipts, drawbacks, and net revenue.
- Use **AFB-S017–S020** and **AFB-S026–S027** for merchant-side invoices, account balances, bills, correspondence, seizures, and liquidity stress.
- Link each customs obligation to the voyage and commodity layers wherever identifiers permit.

The national archival guides are discovery aids. Claims require series-, volume-, container-, page-, image-, or item-level citations.

## Initial sampling design

Start with New York and Philadelphia, 1793–1799, because existing merchant sources and the project's London credit-crisis layer make those ports analytically valuable. Add Baltimore where source survival permits. Treat New Orleans as a later extension following United States control rather than forcing it into the same founding-period panel.

Sample three transaction classes:

1. Goods entered for domestic sale.
2. Foreign goods later re-exported with a drawback claim.
3. Bonds with delinquency, default, litigation, or ambiguous disposition.

The comparison should be within commodity and port-year where possible. Sugar, coffee, molasses, textiles, and hardware connect directly to existing project layers.

## Validation rules

- Never count a bond as cash revenue until payment is documented.
- Never count a drawback as paid merely because it was legally eligible or claimed.
- Never count foreign re-exports as domestic produce.
- Preserve original currencies, units, and accounting dates before conversion.
- Tie a re-export to the original import at the cargo-line level where possible; otherwise state matching uncertainty.
- Preserve principal and sureties as separate actors.
- Record amendments and effective dates; do not treat the 1789, 1790, and 1799 rules as one timeless regime.
- Reconcile merchant books, customhouse records, and Treasury aggregates without assuming they use the same accounting basis.
- Report missing bonds, destroyed volumes, and port-specific survival as data limitations.

## Falsification tests

The working-capital claim weakens if merchants normally paid immediately despite legal credit, if bond maturities were too short to affect inventory finance, or if fees and enforcement costs offset the liquidity benefit. The entrepôt claim weakens if re-export volumes were small, concentrated in exceptional war years, or drawbacks were rarely approved or paid. The access hypothesis weakens if surety networks were broad and bond terms did not vary with merchant standing.

## Outputs

1. Section-by-section legal provision index for the 1790 and 1799 acts.
2. Port-and-series archival inventory for bonds, drawbacks, debentures, and re-export proofs.
3. Normalized customs-obligation and re-export tables with provenance.
4. Merchant–surety network dataset.
5. Port-year reconciliation of duties assessed, cash collected, drawbacks paid, and net retained revenue.
6. A case study linking one merchant ledger, one customs bond, one voyage, and one re-export or domestic sale.
