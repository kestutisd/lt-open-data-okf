---
type: Table
title: "NtrObjektoBukle — NTR objektų būklių klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_objektai/NtrObjektoBukle (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoBukle"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L37"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrObjektoBukle — NTR objektų būklių klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_objektai/NtrObjektoBukle`[^manifest]
- **Dataset:** [NTR objektus apibūdinantys klasifikatoriai](../ntr_objektai.md) (`datasets/gov/rc/ntr/ntr_objektai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L37)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoBukle`
- **Primary Key (`ref`):** `obuk_bukle`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obuk_bukle` | `integer` | — | `4` | `open` | — | Turto objekto būklė | — |
| `obuk_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `obuk_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `obuk_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `obuk_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `obuk_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv
