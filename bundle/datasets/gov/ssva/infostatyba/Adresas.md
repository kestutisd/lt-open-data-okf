---
type: Table
title: "Adresas — Statinių adresai"
description: "Spinta table datasets/gov/ssva/infostatyba/Adresas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/infostatyba/Adresas"
tags: [gov, ssva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/infostatyba.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/infostatyba.csv#L34"
    last_modified: "2026-11-11T14:39:20Z"
---

# Adresas — Statinių adresai

- **Model:** `datasets/gov/ssva/infostatyba/Adresas`[^manifest]
- **Dataset:** [Valstybinės teritorijų planavimo ir statybos inspekcijos prie aplinkos ministerijos duomenys](../infostatyba.md) (`datasets/gov/ssva/infostatyba`)
- **Manifest CSV:** [datasets/gov/ssva/infostatyba.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/infostatyba.csv#L34)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/infostatyba/Adresas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `projekto_id` | `string` | — | `4` | `open` | — | Projekto identifikatorius | Siejasi su duomenų rinkiniu - https://get.data.gov.lt/datasets/gov/vtpsi/infostatyba/Statinys |
| `statinio_id` | `string` | — | `4` | `open` | — | Statinio identifikatorius | Siejasi su duomenų rinkiniu - https://get.data.gov.lt/datasets/gov/vtpsi/infostatyba/Statinys |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | Siejasi su Savivaldybių duomenų rinkiniu - https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe/Savivaldybe |
| `sen_kodas` | `string` | — | `4` | `open` | — | Seniūnijos kodas | Siejasi su Seniūnijų duomenų rinkiniu - https://get.data.gov.lt/datasets/gov/rc/ar/seniunija/Seniunija |
| `gyv_kodas` | `string` | — | `4` | `open` | — | Gyvenamosios vietovės kodas | Siejasi su Gyvenamosios vietovės duomenų rinkiniu - https://get.data.gov.lt/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove |
| `gat_kodas` | `string` | — | `4` | `open` | — | Gatvės kodas | Siejasi su Gatvių duomenų rinkiniu - https://get.data.gov.lt/datasets/gov/rc/ar/gatve/Gatve |
| `pastatas` | `string` | — | `4` | `open` | — | Pastato numeris | — |
| `korpusas` | `string` | — | `4` | `open` | — | Korpusas | — |
| `pasto_kodas` | `string` | — | `4` | `open` | — | Pašto kodas | — |
| `adresas` | `string` | — | `4` | `open` | — | Adresas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/infostatyba.csv
