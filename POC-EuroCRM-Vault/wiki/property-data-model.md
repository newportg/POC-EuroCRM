---
status: Draft
parent:"[[solution-overview]]"
source: European CRM Architecture Review 2.pdf
---

# Property Data Model — Site, Property, Deal

## Data Schema

![[property-data-model-schema.puml]]

## Core Entities

### kf_Site — The Physical Asset

The canonical building or land parcel that every other record hangs off.

**Key Fields:**
- `kf_uprn` — UK reference
- `kf_cadastralref` — EU registry
- `kf_landregistrytitle` — deed
- `kf_loqateid` — verified address

### Address Storage (Country-Neutral Standard)

Because properties span the globe, addresses cannot be stored biased to one country or formatting issues arise. `kf_Site` stores a single canonical, country-neutral address using a version of the UPU S42a-6 / ISO 19773 standard, split into granular elements:

| Element | Field name | Max length |
| ------- | ---------- | ---------- |
| Organisation | Organisation Name | 60 |
|  | Department Name | 60 |
| Premises | Sub Building Name | 30 |
|  | Building Name | 50 |
|  | Building Number | 4 |
| Thoroughfare | Dependent Thoroughfare Name | 60 |
|  | Dependent Thoroughfare Descriptor | 20 |
|  | Thoroughfare Name | 60 |
|  | Thoroughfare Descriptor | 20 |
| Locality | Double Dependent Locality | 35 |
|  | Dependent Locality | 35 |
|  | Post town | 30 |
| Postcode | Postcode | 7 |
| PO Box | PO Box | 6 |

The correct country-specific display format is then applied via the [Loqate international address formats](https://docs.loqate.com/data-coverage/loqate-international-address-formats#loqate-international-address-formats), so the stored data stays country-neutral while presentation follows each market's conventions.

As with the previous schema, the address is also presented as a single line (`kf_addressfull`), but that line is rendered per the applicable international address format from the country-neutral elements rather than stored as a country-biased free-text field. Identifiers such as `kf_uprn` (UK) and `kf_cadastralref` (EU registry) remain as country/regional-specific reference fields alongside the neutral core.

**Address format caching:** The international address format definitions are cached in a reference table (`kf_AddressFormat`), updated periodically from the Loqate international address formats source. `kf_addressfull` is generated at capture/write time from the country-neutral elements using the cached format, and the persisted single-line value is read thereafter. This avoids a live Loqate call (and its per-lookup cost) on every read.

### kf_Property — The Commercial Record

The shared asset register that every commercial service line reads.

**Key Fields:**
- Identity and address, geocoded
- Sector, type, status, tenure
- Areas, floors, parking, planning
- Asking price, owner, ESG

### kf_ResProperty — The Residential Record

The residential sibling on the same site, with its own saleable attributes.

**Key Fields:**
- `kf_propertytype`, `kf_tenure`
- Bedrooms, bathrooms, receptions
- Weekly rent, guide price
- `kf_epcrating`, `kf_siteid`

### kf_DealProperty — The Junction

Deal-specific measures for one asset inside one deal, single or portfolio.

**Key Fields:**
- `kf_allocationpercent`, `kf_lotstatus`
- `kf_passingrent`, `kf_erv`
- `kf_occupancy`, `kf_wault`
- `kf_capitalvalue_psm`, `kf_tenantid`

**Design Principle:** Stable characteristics live on the property records; deal-specific measures live on the junction, so a deal can never overwrite the master asset.

## Why Two Property Tables?

### kf_Property (Commercial)

**Key Schema Fields:** Use class, Floor area, Lease terms, Occupational data, Investor profiles

**Service Lines Served:**
- Capital Markets — deals, bids, DD, investors
- OSS — engagements, leases, assessments

**Deal Cycle:** 6-18 months for institutional buyers; 3-12 months for corporate occupiers

### kf_ResProperty (Residential)

**Key Schema Fields:** Bedrooms, Bathrooms, Tenure, Furnishing, Council tax

**Service Lines Served:**
- Resi Sales, Lettings and Buying Agency
- Resi Property Management

**Deal Cycle:** Days to weeks for individual buyers and tenants

Merging would create mostly blank columns for two unrelated audiences. What they share is the physical building — which is what `kf_Site` covers.

## Two Real Scenarios

### Scenario 1: Change of Use

An office block converts to residential. The commercial record is orphaned, a new resi record is created, and years of deal history are lost.

### Scenario 2: Living Sectors — BTR

A Build-to-Rent block is sold as a CM asset, then let unit-by-unit. Duplicate records in both datasets keep cross-sell invisible.

## Auto Address Look Up with Loqate

Users do not manually create records for `kf_Site` — matching and creation happen silently in the background.

1. User types address into existing CRM form
2. Loqate type-ahead returns validated address matches in real time
3. User picks a match and all address fields auto-fill
4. Standard save — no extra steps or new forms
5. Power Automate matches or creates `kf_Site` silently

Loqate validates and populates the country-neutral address elements above. The addresses it returns conform to the UPU S42a-6 / ISO 19773 standard. The [Loqate international address formats](https://docs.loqate.com/data-coverage/loqate-international-address-formats#loqate-international-address-formats) are cached in the `kf_AddressFormat` reference table (updated periodically) and used at capture time to render the display layout, including the single-line `kf_addressfull`, for each country.

## Every Service Line Reads the Same Record

One property record answers ownership, deals, valuations, leases and ESG in a single graph.

| Service Line | Entity | Relationship |
| ------------ | ------ | ------------ |
| Capital Markets | kf_DealProperty | Many to many |
| OSS | kf_Engagement | Many to one |
| Valuations | kf_ValuationInstruction | Many to one |
| ESG | kf_ESGAssessment | Many to one |
| Building Consultancy | kf_BuildingSurvey | Many to one |
| Development | kf_DevelopmentProject | Many to one |
| Capital Advisory | kf_DebtMandate | Many to one |
| Property Management | kf_PropertyMandate | Many to one |
| Leasing | kf_Lease | Many to one |
| Residential | kf_ResProperty via kf_Site | Sibling |
