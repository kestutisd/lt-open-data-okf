---
type: Table
title: "Dokumentas — Lošimo punktų leidimo dokumentai"
description: "Lošimo punktų leidimų dokumentų ir jų istorijos sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/lpt/leidimai_punktams/Dokumentas"
tags: [gov, lpt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lpt/leidimai_punktams.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/leidimai_punktams.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dokumentas — Lošimo punktų leidimo dokumentai

Lošimo punktų leidimų dokumentų ir jų istorijos sąrašas

- **Model:** `datasets/gov/lpt/leidimai_punktams/Dokumentas`[^manifest]
- **Dataset:** [Lošimo punktų leidimo dokumentai](../leidimai_punktams.md) (`datasets/gov/lpt/leidimai_punktams`)
- **Manifest CSV:** [datasets/gov/lpt/leidimai_punktams.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/leidimai_punktams.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lpt/leidimai_punktams/Dokumentas`
- **Primary Key (`ref`):** `leidimo_dokumento_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leidimo_dokumento_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `licencijos_id` | `string` | — | `4` | `open` | — | Licencijos unikalus identifikatorius | — |
| `leidimo_id` | `string` | — | `4` | `open` | — | Unikalus leidimo id | Licencijų, priskirtų šiems tipams, informacija yra teisinga: Lažybas, Stalo lošimus ir A kategorijos automatais, Lošimus B kategorijos automatais |
| `leidimo_isdavimo_data` | `date` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `leidimo_isdavimo_pagrindas` | `string` | — | `4` | `open` | — | Leidimo išdavimo pagrindas | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |
| `losimu_vieta` | `string` | — | `3` | `open` | — | Lošimo vieta | — |
| `x_koord` | `integer` | — | `4` | `open` | — | Lošimo punkto x koordinatė | — |
| `y_koord` | `integer` | — | `4` | `open` | — | Lošimo punkto y koordinatė | — |
| `leidimo_panaikinimo_pagrindas` | `string` | — | `4` | `open` | — | Leidimo panaikinimo pagrindas | — |
| `leidimo_panaikinimo_data` | `date` | `D` | `4` | `open` | — | Leidimo panaikinimo data | — |
| `dokumento_keitimo_pagrindas` | `string` | — | `4` | `open` | — | Dokumento keitimo pagrindas | — |
| `dokumento_numeris` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `dokumentas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Leidimo dokumentas galioja nuo | — |
| `dokumentas_galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimo dokumentas galioja iki | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `leidimo_tipas` | `"Lošimų automatų salonas"` | — | — | Lošimų automatų salonas | — |
| `leidimo_tipas` | `"Lažybų punktas"` | — | — | Lažybų punktas | — |
| `leidimo_tipas` | `"Lošimo namai (kazino)"` | — | — | Lošimo namai (kazino) | — |
| `leidimo_tipas` | `"Bingo salonas"` | — | — | Bingo salonas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lpt/leidimai_punktams.csv
