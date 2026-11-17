---
type: Table
title: "Nusiskundimas — VVTAT vartotojų nusiskundimo pobūdžių klasifikatorius"
description: "Spinta table datasets/gov/vvtat/klasifikatoriai/Nusiskundimas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Nusiskundimas"
tags: [gov, vvtat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L50"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nusiskundimas — VVTAT vartotojų nusiskundimo pobūdžių klasifikatorius

- **Model:** `datasets/gov/vvtat/klasifikatoriai/Nusiskundimas`[^manifest]
- **Dataset:** [Duomenys apie VVTAT klasifikatorius](../klasifikatoriai.md) (`datasets/gov/vvtat/klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/vvtat/klasifikatoriai.csv#L50](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L50)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Nusiskundimas`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Pobūdžio kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Nusiskundimo pobūdis | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv
