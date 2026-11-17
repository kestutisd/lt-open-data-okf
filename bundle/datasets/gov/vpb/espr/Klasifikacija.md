---
type: Table
title: "Klasifikacija — Lietuvoje įsigaliojusių Europos patentų klasifikacija"
description: "Lentelė „Lietuvoje įsigaliojusių Europos patentų klasifikacija“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/espr/Klasifikacija"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L27"
    last_modified: "2026-11-11T14:39:20Z"
---

# Klasifikacija — Lietuvoje įsigaliojusių Europos patentų klasifikacija

Lentelė „Lietuvoje įsigaliojusių Europos patentų klasifikacija“. Lentelę sudaro: patento ir paraiškos numeris, IPC klasifikacija ir jos versija mėnesio tikslumu. Vienas įrašas atitinka vieną unikalią patento numerio, IPC klasifikacijos ir jos versijos kombinaciją.

- **Model:** `datasets/gov/vpb/espr/Klasifikacija`[^manifest]
- **Dataset:** [Lietuvoje įsigalioję Europos patentai](../espr.md) (`datasets/gov/vpb/espr`)
- **Manifest CSV:** [datasets/gov/vpb/es_pr.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L27)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/espr/Klasifikacija`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `patento_numeris` | `string` | — | `4` | `open` | — | Patento numeris | — |
| `paraiskos_numeris` | `string` | — | `4` | `open` | — | Patento paraiškos numeris | — |
| `ipc_klase` | `string` | — | `4` | `open` | — | Patento IPC klasė | — |
| `ipc_versija` | `date` | `M` | `4` | `open` | — | Patento IPC klasės versija mėnesio tikslumu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv
