# Customs and Treasury source plan

## Research question

How did the new federal government convert constitutional authority into dependable revenue and administrative reach through customs collection?

The source base must keep three layers distinct:

1. **Law:** what Congress authorized and required.
2. **National accounts:** what Treasury reported as receipts, expenditures, debt, and collection costs.
3. **Port operations:** what collectors and customs districts recorded in practice.

The 1799 statute belongs primarily to the first layer. It reorganized and codified collection machinery; it should not be used as a substitute for the tariff schedules that set particular rates.

## Initial canonical sources

| Layer | Source | Repository | Use |
|---|---|---|---|
| Law | *An Act to regulate the collection of duties on imports and tonnage* (March 2, 1799), 1 Stat. 627 | GovInfo | Districts, ports, officers, entry procedures, enforcement, bonds, penalties |
| National accounts | *Annual Report of the Secretary of the Treasury on the State of the Finances* | FRASER | Annual receipts, expenditures, debt, forecasts, and supporting tables |
| National accounts | *Excerpts from the American State Papers: 1792* | FRASER | Early revenue tables, including import-duty proceeds |
| Port operations | Records of the U.S. Customs Service, Record Group 36 | National Archives | Collector correspondence, vessel and cargo documentation, district administration |

## Extraction schema

Create one row per reported observation. Preserve the source's language and add normalized fields separately.

- `observation_id`
- `year_start`
- `year_end`
- `reporting_period_label`
- `port`
- `customs_district`
- `state_or_territory`
- `measure_original`
- `measure_normalized`
- `amount_nominal_usd`
- `unit_original`
- `gross_or_net`
- `imports_exports_or_tonnage`
- `source_id`
- `item_identifier`
- `table_title`
- `page_image`
- `transcription_method`
- `verification_status`
- `notes`

## First extraction pass

1. Transcribe the 1792 revenue table from page images and reconcile totals.
2. Identify comparable Treasury tables for 1793–1799.
3. Index the 1799 act by section: districts and ports, officer roles, entry and clearance, warehousing/bonds, drawbacks, enforcement, and penalties.
4. Select three pilot customs districts—New York, Philadelphia, and Baltimore—and locate series-level RG 36 descriptions.
5. Record missing years and changes in definitions before building a time series.

## Quality rules

- Never copy OCR numbers without checking the page image.
- Do not combine gross and net receipts.
- Do not infer a port value from a national total.
- Keep fiscal year, calendar year, and reporting-period labels separate.
- Preserve historical district and port names; normalization belongs in additional fields.
- Treat finding aids as discovery tools, not substantive evidence.
