---
type: Table
title: "Nenustatyta — VVTAT nenustatytų skundų priežasčių klasifikatorius"
description: "Spinta table datasets/gov/vvtat/klasifikatoriai/Nenustatyta (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Nenustatyta"
tags: [gov, vvtat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nenustatyta — VVTAT nenustatytų skundų priežasčių klasifikatorius

- **Model:** `datasets/gov/vvtat/klasifikatoriai/Nenustatyta`[^manifest]
- **Dataset:** [Duomenys apie VVTAT klasifikatorius](../klasifikatoriai.md) (`datasets/gov/vvtat/klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/vvtat/klasifikatoriai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Nenustatyta`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Skundo nenustatymo priežasties identifikacinis numeris | — |
| `pavadinimas_lt` | `string` | — | `4` | `open` | — | Skundo nenustatymo priežastis | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv
