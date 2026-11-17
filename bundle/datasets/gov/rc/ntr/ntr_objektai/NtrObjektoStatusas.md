---
type: Table
title: "NtrObjektoStatusas — NTR objektų statusų klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_objektai/NtrObjektoStatusas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoStatusas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L45"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrObjektoStatusas — NTR objektų statusų klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_objektai/NtrObjektoStatusas`[^manifest]
- **Dataset:** [NTR objektus apibūdinantys klasifikatoriai](../ntr_objektai.md) (`datasets/gov/rc/ntr/ntr_objektai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L45](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L45)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoStatusas`
- **Primary Key (`ref`):** `osta_statusas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `osta_statusas` | `integer` | — | `4` | `open` | — | Turto objekto statusas | — |
| `osta_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `osta_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `osta_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `osta_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `osta_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv
