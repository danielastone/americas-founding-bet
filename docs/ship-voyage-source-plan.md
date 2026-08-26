# Ship-voyage source plan

## Research purpose

Link merchant decisions to customs administration through identifiable voyages. The unit is a voyage or port call—not a ship name alone. The same vessel can change owner, master, flag, rig, route, and function.

## Evidence layers

| Layer | Records | What they can establish |
|---|---|---|
| Customs administration | Inward and outward manifests, entrance and clearance registers, vessel documentation | Reported arrival or departure, port, date, master, tonnage, cargo, fees, and legal processing where preserved |
| Merchant operations | Ledgers, orders, invoices, bills of lading, correspondence, insurance | Commercial purpose, counterparties, cargo, financing, routing decisions, and risk allocation |
| Voyage dataset | SlaveVoyages records | Structured evidence on transatlantic slave-trading voyages, with documented and imputed variables |
| Fiscal aggregates | Treasury reports | National or district totals against which voyage evidence can be checked |

## Voyage table

Create one row per voyage leg or customs port call. Use a stable project ID while retaining every archival or database identifier.

- `voyage_id`
- `voyage_leg_id`
- `source_id`
- `source_record_id`
- `vessel_name_original`
- `vessel_name_normalized`
- `vessel_type_or_rig`
- `registry_or_flag`
- `tonnage_original`
- `master_name`
- `owner_or_merchant`
- `departure_port_original`
- `departure_port_normalized`
- `departure_date`
- `arrival_port_original`
- `arrival_port_normalized`
- `arrival_date`
- `intermediate_port`
- `cargo_original`
- `cargo_normalized`
- `enslaved_people_embarked`
- `enslaved_people_disembarked`
- `crew_count`
- `passenger_count`
- `duties_or_fees`
- `currency_original`
- `manifest_direction`
- `document_type`
- `archive_container`
- `page_or_folio`
- `observed_or_imputed`
- `confidence`
- `notes`

## Linkage rules

1. Do not match voyages on vessel name alone.
2. Require at least two additional anchors, preferably master, date window, tonnage, owner, or port pair.
3. Preserve uncertain and conflicting matches instead of forcing a single identity.
4. Treat each port call as a leg; do not collapse multi-stop voyages.
5. Keep outward and inward manifests distinct even when they appear to describe the same movement.
6. Separate cargo from people and crew fields while recognizing that enslaved people were recorded as property in many historical documents.
7. Flag every imputed SlaveVoyages field and retain the database voyage ID and version or access date.

## First controlled sample

Build a 1797–1799 New York pilot by linking Morris & Ludlum orders to RG 36 entrance and clearance records where available. Add comparison voyages from Philadelphia or Baltimore and all identifiable United States-connected slave-trading voyages in the same window. The result remains a case-linked sample unless coverage and missingness are quantified.
