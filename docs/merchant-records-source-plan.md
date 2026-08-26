# Merchant-records source plan

## Purpose

Use private business records to test how federal customs and fiscal institutions were experienced by firms. Merchant papers are micro-level evidence; they do not establish national totals or typical behavior by themselves.

## Initial sample

| Source | Period used | Analytic value | Access constraint |
|---|---|---|---|
| Gelston and Saltonstall ledger | 1790–1793 | Firm accounts in early federal New York | In-person inspection |
| Stewart and Jones records | Bulk 1784–1796 | Ship-chandler accounts and correspondence across the constitutional transition | Mostly in-person; selected earlier records on microfilm |
| Morris & Ludlum letter and order book | 1797–1799 tranche | Orders, commodities, suppliers, and Atlantic/southern connections immediately before the 1799 collection act | In-person inspection |
| NYPL Mercantile collection | Founding-era components only | Discovery pool for New York and Philadelphia trade, finance, insurance, and shipping | Component identification and in-person inspection |

## Unit of analysis

Extract one row per transaction, order, invoice, letter, voyage reference, or account balance. Do not force unlike record types into one undifferentiated table.

Core fields:

- `merchant_record_id`
- `source_id`
- `creator_or_firm`
- `document_type`
- `document_date`
- `origin_place`
- `destination_place`
- `counterparty`
- `commodity_original`
- `commodity_normalized`
- `quantity_original`
- `unit_original`
- `amount_original`
- `currency_original`
- `amount_usd_nominal`
- `vessel`
- `insurance_reference`
- `customs_or_duty_reference`
- `credit_terms`
- `archive_container`
- `page_or_folio`
- `transcription_status`
- `notes`

## Design limits

- These New York-heavy collections cannot support a claim about all American merchants.
- Surviving papers are selected by preservation, donor, repository, and firm prominence.
- Ledger entries may omit informal exchange, failed firms, enslaved labor, and the full production chain.
- Prices and balances require explicit currency and unit normalization.
- A letter mentioning a law shows perception or response, not the law’s aggregate economic effect.

## First controlled test

Compare merchant-level references from 1797–1799 with the 1799 statute and Treasury aggregates. Test whether the records reveal changes in ordering, routing, paperwork, credit, insurance, or duty-related language. Treat the result as case evidence until replicated across ports and firms.
