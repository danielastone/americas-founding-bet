# Tariff and customs-law chronology, 1789–1803

## Purpose

This is the legal specification for testing how cargo produced customs obligations and how those obligations became—or failed to become—Treasury cash. It is not evidence that a law was implemented, a duty was collected, or a drawback was paid.

The machine-readable chronology is in `data/customs_law.csv`.

## What the chronology separates

| Legal mechanism | Why it must remain separate |
|---|---|
| Tariff rate | Determines the nominal obligation by commodity, quantity, or value |
| Tonnage duty or vessel differential | Changes cost by registry, ownership, construction, and voyage status |
| Credit and bonding | Separates assessment from cash timing and default exposure |
| Drawback and retention | Separates gross duty from the amount returned or retained on re-export |
| Collection administration | Defines districts, officers, entry, valuation, security, enforcement, and remittance |
| Revenue appropriation | States a legal use of proceeds but does not prove cash was realized or available |

## Legal periods for empirical coding

### 1789: initial system

The July 4 tariff established specific and ad valorem duties, a qualifying re-export drawback less retention, and vessel-based preferences. The July 20 tonnage law and July 31 collection law supplied separate vessel charges and administrative machinery. These laws must not be represented as one undifferentiated “1789 tariff.”

### 1790–1793: replacement and refinement

The July 20, 1790 tonnage act replaced the initial tonnage regime. The August 4 collection act substantially reworked customs administration, while the August 10 debt-provision act revised duties and connected import revenue to federal finance. The 1791 and 1792 laws changed selected duties and collection provisions. Rate-effective dates, not enactment years alone, must control transaction coding.

### 1794–1797: layered additions

Congress repeatedly imposed additional duties rather than rebuilding a clean schedule. The June 7, 1794 act also specified foreign-vessel additions and re-export drawback treatment. Laws in 1795 and 1797 added or continued commodity-specific burdens, including salt. A transaction-level rate therefore requires a cumulative legal calculation.

### 1799: collection-code baseline

The March 2, 1799 act became the principal collection code for the endpoint period. It governs districts, officers, manifests, entries, valuation, bonds, payment, drawbacks, debentures, and enforcement. It is the main bridge between tariff authority and customhouse observations.

### 1800–1803: endpoint-period modifications

The May 1800 laws continued the salt regime, increased drawback retention, denied drawback of the foreign-vessel addition, changed duties on articles including sugar and molasses, and appropriated specified proceeds to debt. The 1802 laws contain narrower port, vessel, and officer provisions. No transaction should be assigned a generic “1800 tariff rate”; the applicable provision depends on commodity, vessel, entry date, and re-export status.

## Required transaction linkage

For each import or re-export observation, preserve:

1. entry and effective dates;
2. customs district and port;
3. commodity description, quantity, unit, value, and origin;
4. vessel registry, ownership, and relevant status;
5. statutory section and cumulative rate components;
6. duty assessed;
7. credit term, bond, surety, maturity, payment, and default;
8. re-export link, drawback claimed, allowed, retained, and paid;
9. Treasury remittance date and account where evidence survives.

## Known limitations

- This is a governing-act chronology, not yet a complete section-level rate schedule.
- The 1791, 1792, 1795, and 1797 operative sections still require full transcription and double-checking.
- Private relief acts, district-boundary changes, officer-compensation amendments, and commodity-specific exceptions are not yet exhaustive.
- Apparent typographical errors in later Statutes at Large indexes cannot substitute for the act text.
- Absence of an identified 1803 system-wide amendment is not proof that no relevant 1803 provision exists; the session laws still require a closing scan.

## Completion test for this phase

The chronology becomes analysis-ready only when every section affecting the selected commodities and first port pair has:

- exact effective dates;
- original rate and unit;
- cumulative amendment logic;
- credit and bond rules;
- drawback and retention rules;
- repeal or continuation links;
- a checked primary-text citation.

Until then, the file is a legal control table, not a tariff calculator.
