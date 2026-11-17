---
type: Table
title: "NtrLeistinaPaskirtis — NTR leistinos paskirtys pagal objekto tipus"
description: "Spinta table datasets/gov/rc/ntr/ntr_paskirtys/NtrLeistinaPaskirtis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrLeistinaPaskirtis"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrLeistinaPaskirtis — NTR leistinos paskirtys pagal objekto tipus

- **Model:** `datasets/gov/rc/ntr/ntr_paskirtys/NtrLeistinaPaskirtis`[^manifest]
- **Dataset:** [NTR paskirčių klasifikatoriai](../ntr_paskirtys.md) (`datasets/gov/rc/ntr/ntr_paskirtys`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_paskirtys.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrLeistinaPaskirtis`
- **Primary Key (`ref`):** `obje_tipas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obje_tipas` | `integer` | — | `3` | `open` | — | Turto objekto tipas | — |
| `pask_tipas` | `ref` | [NtrPaskirtiesTipas](NtrPaskirtiesTipas.md) | `4` | `open` | — | Turto paskirties tipas | — |
| `lpas_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv
