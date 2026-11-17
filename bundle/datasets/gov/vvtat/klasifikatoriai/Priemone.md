---
type: Table
title: "Priemone — VVTAT patikrintų įmonių savanoriškų priemonių klasifikatorius"
description: "Spinta table datasets/gov/vvtat/klasifikatoriai/Priemone (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Priemone"
tags: [gov, vvtat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priemone — VVTAT patikrintų įmonių savanoriškų priemonių klasifikatorius

- **Model:** `datasets/gov/vvtat/klasifikatoriai/Priemone`[^manifest]
- **Dataset:** [Duomenys apie VVTAT klasifikatorius](../klasifikatoriai.md) (`datasets/gov/vvtat/klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/vvtat/klasifikatoriai.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/Priemone`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Savanoriškos priemonės identifikacinis numeris | — |
| `pavadinimas_lt` | `string` | — | `4` | `open` | — | Savanoriškos priemonės tipas | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Klasifikatoriaus galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv
