---
type: Table
title: "NtrTurtoGrupe — NTR turto objektų grupių klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_objektai/NtrTurtoGrupe (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrTurtoGrupe"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrTurtoGrupe — NTR turto objektų grupių klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_objektai/NtrTurtoGrupe`[^manifest]
- **Dataset:** [NTR objektus apibūdinantys klasifikatoriai](../ntr_objektai.md) (`datasets/gov/rc/ntr/ntr_objektai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrTurtoGrupe`
- **Primary Key (`ref`):** `objg_grupe`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objg_grupe` | `integer` | — | `4` | `open` | — | Turto objekto grupė | — |
| `objg_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `objg_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `objg_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv
