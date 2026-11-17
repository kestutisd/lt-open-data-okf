---
type: Table
title: "CustomsOffice"
description: "Spinta table datasets/gov/muitine/muitines_istaigos/CustomsOffice (16 columns)."
tags: [gov, muitine, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# CustomsOffice

- **Model:** `datasets/gov/muitine/muitines_istaigos/CustomsOffice`[^manifest]
- **Dataset:** [datasets/gov/muitine/muitines_istaigos](../muitines_istaigos.md) (`datasets/gov/muitine/muitines_istaigos`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_istaigos.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **URI:** `foaf:Organization`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Rinkinio identifikacinis numeris | — |
| `metadata` | `ref` | [Metadata](Metadata.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `reference_number` | `string` | — | `3` | `open` | — | Muitinės įstaigos kodas | — |
| `reference_number_main_office` | `string` | — | `3` | `open` | — | — | neprivalomas |
| `reference_number_higher_authority` | `string` | — | `3` | `open` | — | Vadovaujančioji įstaiga | — |
| `reference_number_authority_of_enquiry` | `string` | — | `3` | `open` | — | Muitinės įstaiga tranzito tyrimų vykdymui | — |
| `reference_number_authority_of_recovery` | `string` | — | `3` | `open` | — | Muitinės įstaiga tranzito išieškojimo vykdymui | — |
| `country_code` | `string` | — | `3` | `open` | — | Šalies kodas | — |
| `ncts_entry_date` | `date` | `10D` | `4` | `open` | — | NCTS taikymo pradžios data | — |
| `nearest_office` | `string` | — | `3` | `open` | — | — | neprivalomas |
| `email_address` | `string` | — | `3` | `open` | — | Elektroninio pašto adresas | — |
| `postal_code` | `string` | — | `3` | `open` | — | Pašto kodas | — |
| `geo_info_code` | `string` | — | `3` | `open` | — | Geografinė situacija | — |
| `trader_dedicated` | `boolean` | — | `3` | `open` | — | Supaprastinimų taikymo muitinės įstaigoje požymis | — |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžios data | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaigos data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `geo_info_code` | `"Q"` | — | — | Vidinė įstaiga | — |
| `geo_info_code` | `"CB"` | — | — | Baltijos jūros pakrantė | — |
| `geo_info_code` | `"LT/BY"` | — | — | Siena su Baltarusijos Respublika | — |
| `geo_info_code` | `"LT/RU"` | — | — | Siena su Rusijos Federacija | — |
| `trader_dedicated` | `true` | `1` | — | — | — |
| `trader_dedicated` | `false` | `0` | — | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `foaf` | `http://xmlns.com/foaf/0.1/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv
