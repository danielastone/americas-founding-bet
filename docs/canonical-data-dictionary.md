# Canonical data dictionary and evidence states

## Purpose

Layer-specific schemas are proposals. This file controls shared identifiers, provenance, measurement states, and transformations. The procedures and claim gates in `docs/audit-evidence-hierarchy.md` govern advancement between evidence states.

## Evidence states

| State | Meaning |
|---|---|
| discovery_only | Guide, portal, collection, contextual source, or unresolved item |
| item_identified | Specific primary item, law, treaty, or archival object |
| source_identified | Bounded report, dataset, or secondary study |
| transcribed | Relevant observations extracted from the source image and checked |
| normalized | Originals mapped to controlled entities, units, dates, or currencies |
| validated | Provenance, totals, duplicates, cutoff, classification, and applicable reconciliations passed |
| analysis_ready | Observation meets a specified claim and its accounting, mechanism, or causal gate |

Metadata verification is separate from evidence state.

## Universal provenance fields

Every analytical table must contain record_id, source_id, repository, repository_identifier, series_or_collection, container_volume_or_roll, folder_or_item, page_folio_or_image, document_date, observation_date, transcription_method, transcribed_by, verified_by, verification_date, evidence_state, observed_inferred_or_imputed, confidence, and notes.

Unknown values remain null with a reason; they are not silently inferred.

## Shared entity identifiers

Use person_id, organization_id, office_id, jurisdiction_id, place_id, customs_district_id, vessel_id, voyage_id, voyage_leg_id, commodity_id, cargo_line_id, instrument_id, household_id, and claim_id. Entity links require provenance and matching confidence. Names alone do not establish identity.

## Measurement rules

Never overwrite original values. Preserve value_original, unit_original, currency_original, date_original, place_original, commodity_original, and account_title_original. Normalized companions identify the rule and version used.

Currency conversion requires amount_original, currency_original, accounting_unit, exchange_rate, quotation direction, rate date, rate source, amount_usd_nominal, method, and uncertainty. An accounting conversion is not an observed market rate.

Every commodity observation preserves processing stage, grade, package, original quantity and unit, normalized quantity and unit, conversion rule, origin confidence, and trade type: import, domestic_export, foreign_reexport, transit, coastwise, or unknown. Persons never enter the commodity table.

Finance states remain separate: authorized, assessed, subscribed, face value, market value, cash proceeds, cash received, cash paid, accrued interest, interest paid, principal redeemed, drawback claimed, drawback allowed, drawback paid, and disposition.

## Time and geography

Core period: 1789–1803. Pre-1789 observations are background. Narrow 1804 observations may be endpoint_execution only when needed to complete the 1803 Louisiana transfer, claims, stock, or payment transaction. Later observations are validation or consequence.

New Orleans is a foreign-colonial port before transfer and an endpoint case afterward. It is not pooled mechanically with continuously United States-administered customs districts. Port exports do not establish the producing state.

## Claim readiness

A testable claim specifies claim_id, unit, outcome, mechanism, comparison, evidence requirements, supporting and contradicting observations, missingness, selection, robustness tests, and publication status. A narrative layer is not evidence-ready merely because its mechanism is plausible.

Evidence ranking is assertion-specific. Statutes prove legal authority, not implementation. Published aggregates do not prove transactions. Reproductions of the same underlying report are one evidentiary origin, not independent corroboration.
