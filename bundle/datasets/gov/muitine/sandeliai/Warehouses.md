---
type: Table
title: "Warehouses"
description: "Spinta table datasets/gov/muitine/sandeliai/Warehouses (10 columns)."
tags: [gov, muitine, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/sandeliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliai.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# Warehouses

- **Model:** `datasets/gov/muitine/sandeliai/Warehouses`[^manifest]
- **Dataset:** [datasets/gov/muitine/sandeliai](../sandeliai.md) (`datasets/gov/muitine/sandeliai`)
- **Manifest CSV:** [datasets/gov/muitine/sandeliai.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliai.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `reference_number, valid_from`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Rinkinio identifikacinis numeris | — |
| `metadata` | `ref` | [Metadata](Metadata.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `reference_number` | `string` | — | `3` | `open` | — | Muitinės sandėlio kodas | — |
| `name` | `string` | — | `3` | `open` | — | Sandėlio pavadinimas | — |
| `street_and_number` | `string` | — | `3` | `open` | — | Adresas ir namo numeris | — |
| `postal_code` | `string` | — | `3` | `open` | — | Pašto kodas | — |
| `city` | `string` | — | `3` | `open` | — | Miestas | — |
| `country_code` | `string` | — | `3` | `open` | — | Šalies kodas | 2 simbolių šalies kodas |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžios data | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/sandeliai.csv
