# Consumer welfare and household demand context, 1789–1803

## Purpose

The finance–commodity system matters only partly because it increased state capacity or merchant opportunity. A separate question is whether households gained affordable access to food, fuel, clothing, imported goods, and useful household objects—and which households bore taxes, price shocks, debt, dispossession, and coercion.

This layer asks:

> How did changing commodity supply, tariffs, trade routes, prices, wages, credit, and household production affect material welfare and household demand between 1789 and 1803?

It is a demand-side and distributional test. It is not a claim that aggregate trade growth automatically improved welfare.

## Why trade aggregates are inadequate

Imports are not household consumption because they include:

- Re-exports
- Government and business purchases
- Merchant inventories
- Inputs to refining or manufacturing
- Spoilage, seizure, and unsold goods
- Wholesale values excluding retail margins
- Goods consumed by institutions, vessels, armies, and enslaving enterprises

Exports are not household income because gross value must be divided among producers, enslavers, wage workers, merchants, carriers, insurers, creditors, governments, and foreign counterparties.

Customs revenue can indicate federal capacity while simultaneously raising domestic prices. The incidence depends on pass-through, substitution, evasion, market power, location, and household budget shares.

## Welfare concepts

### Market purchasing power

What could cash or monetized income purchase at local retail prices?

A basic measure is:

real purchasing power = household cash and market income / cost of a locally relevant consumer bundle.

This cannot be reduced to a national wage divided by a national CPI. Wages, prices, employment days, household earners, and consumption baskets varied by place and status.

### Full household resources

Household resources may include:

- Men's, women's, and children's earnings
- Farm and craft production consumed at home
- Gleaning, gardens, livestock, hunting, and fishing
- Board, fuel, clothing, or housing received in kind
- Rents, interest, remittances, and business income
- Credit purchases and deferred payment
- Poor relief, kin transfers, and charitable support
- Goods produced through enslaved labor
- The uncompensated labor and deprivation imposed on enslaved households

Market income alone can understate resources for self-provisioning households while badly misrepresenting the welfare of people whose labor and consumption were controlled by enslavers.

### Material access

Ownership or presence of goods—beds, tables, cookware, ceramics, clocks, books, tea wares, textiles, tools, livestock—can show market penetration and material conditions. It does not show equal use within a household, purchase date, satisfaction, or consumption flow.

### Biological and nutritional welfare

Food availability, diet diversity, calories, mortality, morbidity, stature, and work intensity address dimensions missed by goods ownership. The project should use them only where direct evidence and population definitions are adequate.

### Security and risk

A household with higher average consumption but extreme exposure to harvest failure, unemployment, debt enforcement, seizure, war, or displacement may not be unambiguously better off. Welfare analysis should include volatility and downside risk.

## Population structure

Every welfare result should identify the population represented.

| Dimension | Required categories where evidence permits |
|---|---|
| Legal status | Free, indentured, enslaved, emancipated, Indigenous jurisdiction or other recorded status |
| Geography | Urban, port, rural hinterland, western settlement |
| Region | State, county, city, or market |
| Household structure | Single, married, extended, widow-headed, female-headed, absent spouse, institutional |
| Income position | Wealth or income group with source-specific definition |
| Occupation | Merchant, artisan, laborer, sailor, farmer, planter, domestic worker, other |
| Age and sex | Adults and children; household-member contributions |
| Race | Historical recorded categories retained and critically documented |

Averages across these groups would conceal the project's central distributional question.

## Household demand mechanism

1. Global production and shocks affect landed prices.
2. Shipping, insurance, exchange, duties, wholesale margins, and local transport create the port price.
3. Retail margins, quality, package size, and local competition create the household price.
4. Wages, employment, household production, credit, and transfers determine purchasing power.
5. Households substitute across goods, qualities, home production, and timing.
6. Demand affects merchant orders, inventories, imports, re-exports, and customs revenue.
7. Access and welfare vary across households even when aggregate consumption rises.

This creates feedback from households to the federal revenue system rather than a one-way flow from trade to consumers.

## Commodity-demand context

### Sugar, coffee, tea, and molasses

These goods test the spread of formerly elite or colonial imports into broader consumption. Relevant outcomes include retail price, package size, frequency of probate appearance, tea and coffee equipment, sweetener substitution, and household credit.

A tea set in an estate inventory is evidence of possession and social practice, not the annual quantity of tea consumed. Sugar availability also remained tied to slave-based plantation production.

### Flour, grain, corn, and bread

These were central to subsistence and welfare. Relevant measures include retail and wholesale prices, grain-to-flour conversion, household baking, regional staple substitution, harvest conditions, wages, and transport costs.

A shift from home-produced corn to purchased flour may indicate commercialization, changing preferences, or vulnerability—not automatically improved welfare.

### Meat, pork, fish, dairy, and fats

These goods add diet diversity and connect western and rural production to city demand. Preservation, seasonality, local production, and household processing complicate market-price comparisons.

### Rum and other alcohol

Molasses and grain connected trade to household demand, taverns, wages paid partly in drink, taxation, and social costs. Aggregate gallons cannot be interpreted as welfare without considering harm, household allocation, and institutional consumption.

### Textiles and clothing

Imported and domestic textiles connect Asian and European trade, merchant inventories, household production, women's labor, quality change, and durable use. A single price series cannot represent the large variation in fibers, grades, finished cloth, secondhand goods, and home manufacture.

### Fuel and housing

Firewood, rent, and household space are necessary components of welfare even though they do not fit the export-commodity narrative. Excluding them would bias the consumer basket toward the project's traded goods.

## Data sources

### Global Price and Income History Group — AFB-S080

Provides a research portal for historical prices, wages, income distributions, consumer bundles, exchange rates, and American incomes. It is the preferred starting point for series discovery.

Use underlying city, occupation, commodity, unit, and source metadata. A quoted building wage is not household annual income; observed workdays and other household earners matter.

### Probing the Past — AFB-S081

Contains searchable transcripts of 325 Chesapeake probate inventories from 1740–1810. It connects Maryland and Virginia households to goods, valuations, rooms, slavery, and regional markets.

Its selection is not representative: the project states that most inventories came from wealthy estates and its collection rules favored households with detailed dining or room information. Use it for diffusion patterns, item associations, and case studies, not population ownership rates without correction.

### Reconstructed U.S. CPI — AFB-S082

Use only as a sensitivity benchmark. The official CPI did not exist in this period, and early price and expenditure weights are reconstructed.

The project should construct local commodity-specific indexes first, then compare their direction with the long-run reconstruction.

### British household budgets — AFB-S083

These budgets provide comparative evidence about British demand and a methodological model: household composition, multiple earners, cash and in-kind income, expenditures, occupation, region, and self-provisioning.

They cannot be transferred to American households. Their relevance is design and foreign-demand context.

### Existing project sources

- Merchant ledgers and letters: retail orders, customer credit, inventories, and prices
- Customs records: import supply after subtracting re-export
- State and local records: taxes, wages, poor relief, inspection, probate, and market regulation
- Newspapers and price currents: local quotations and advertisements
- Port and voyage records: supply timing and disruption
- Global commodity layer: external prices, freight, war, and harvest controls

## Core household tables

### Household observation

| Field | Definition |
|---|---|
| household_id | Stable identifier |
| place | City, county, state |
| observation_date | Date and source-event type |
| household_head | Recorded name without assuming sole earner |
| members | Adults, children, kin, servants, boarders where recorded |
| legal_status | Status categories with provenance |
| occupation | Each working member where available |
| cash_income | By source and household member |
| in_kind_income | Original item and imputed value separately |
| self_production | Goods produced and retained |
| debt_receivable / payable | Household credit positions |
| rent / housing | Cash, imputed, owned, or unknown |
| source_id | Provenance |
| selection_frame | Probate, budget, tax, merchant account, poor relief, or other |

### Household goods observation

| Field | Definition |
|---|---|
| household_id | Linked household |
| item_description | Exact source wording |
| harmonized_item | Controlled commodity or durable category |
| quantity | Count or original unit |
| appraised_value | Original valuation |
| room_or_location | Where recorded |
| condition_quality | New, old, broken, grade, or unknown |
| ownership_status | Owned, leased, pledged, assigned, or uncertain |
| production_origin | Domestic, foreign, or unknown |
| enslaved_person_flag | Keeps persons out of the commodity table |
| source_reference | Item-level citation |

### Local retail price and wage

| Field | Definition |
|---|---|
| place_date | Market and observation date |
| item_or_occupation | Exact description |
| quality | Grade, skill, sex, age, or other category |
| price_or_wage | Original quotation |
| unit | Original quantity or time basis |
| retail_wholesale_flag | Market level |
| cash_in_kind_flag | Payment form |
| employment_days | Observed or assumption, labeled |
| source_id | Provenance |

### Household demand transaction

Link merchant customer accounts where available: buyer, date, item, quantity, price, credit terms, payment, default, and household attributes. Merchant customers are selected and may not represent the surrounding population.

## Welfare dashboard

Do not collapse the evidence immediately into one index. Report:

1. Local retail price indexes by port and commodity group.
2. Nominal wages and estimated annual earnings by occupation.
3. Subsistence-basket or respectability-basket affordability.
4. Import availability net of re-export per relevant population.
5. Household-goods prevalence within explicitly defined probate samples.
6. Diet and staple substitution where supported.
7. Household debt and payment delay.
8. Price and income volatility.
9. Distribution by status, sex, occupation, geography, and wealth.
10. Fiscal incidence of tariffs and excises where pass-through can be bounded.

## Hypotheses

1. Expanded imports increased the variety and availability of selected household goods in major ports.
2. Customs duties increased federal capacity but imposed heterogeneous consumer costs depending on pass-through and budget share.
3. Re-export booms raised customs and merchant activity without proportionate domestic consumption.
4. Port households gained earlier access to imported goods, while inland transport preserved price wedges.
5. Merchant credit expanded access but increased household exposure to debt and enforcement.
6. Wartime neutral-carrier gains benefited commercial households more than wage-dependent consumers facing food and fuel volatility.
7. Household demand helped sustain customs revenue, creating dependence of federal finance on consumption of imported goods.
8. Aggregate material-goods diffusion coexisted with extreme deprivation and coercion among enslaved households.

## Identification and bias

### Probate selection

People enter probate data through death, property ownership, legal practice, record survival, and archive selection. Correct where possible using age, wealth, jurisdiction, and probate incidence. Otherwise report conditional prevalence, not population prevalence.

### Price selection

Wholesale, institutional, and auction prices may not equal household retail prices. Quality and package size matter. Never combine observations solely because the commodity name matches.

### Wage selection

A daily wage does not establish annual earnings. Employment days, seasonality, payment in kind, unemployment, and household-member earnings matter.

### Tariff incidence

The statutory duty does not identify the consumer burden. Estimate bounds using price changes across affected and unaffected goods, ports, and periods while controlling for global prices, freight, and war.

### Intra-household distribution

Household totals do not establish who consumed the food, used the goods, controlled income, or performed unpaid labor.

### Enslaved households

Market expenditure and probate ownership frameworks are structurally inadequate for measuring enslaved people's welfare. Use rations, clothing issues, housing, health, mortality, family separation, work demands, resistance, independent production or trade, and testimony where available. People listed in estates are evidence of enslavement and wealth extraction by enslavers, never household durable goods.

## Falsification tests

The consumer-benefit claim weakens if import availability rose but retail prices, real purchasing power, or ownership outside wealthy estates did not improve. The tariff-cost claim weakens if pass-through was low or substitution offset the burden. The market-integration claim weakens if inland price wedges and availability gaps persisted. The credit-access claim weakens if customer accounts show credit concentrated among established or affluent buyers.

## Minimum viable welfare layer

1. Construct local retail-price and wage pilots for Philadelphia and Baltimore.
2. Code a 1789–1803 subset of Chesapeake probate inventories with explicit selection flags.
3. Estimate domestic availability of sugar, coffee, tea, molasses, and textiles after re-export.
4. Build one subsistence basket and one broader household-goods dashboard.
5. Compare results by place, wealth or occupation, and legal status where evidence permits.
6. Estimate tariff pass-through only after global price, freight, and war controls exist.

The project should not claim national consumer welfare if these local pilots cannot support it.
