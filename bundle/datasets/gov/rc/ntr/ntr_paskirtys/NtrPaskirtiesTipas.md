---
type: Table
title: "NtrPaskirtiesTipas — NTR paskirčių tipai"
description: "Spinta table datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesTipas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesTipas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrPaskirtiesTipas — NTR paskirčių tipai

- **Model:** `datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesTipas`[^manifest]
- **Dataset:** [NTR paskirčių klasifikatoriai](../ntr_paskirtys.md) (`datasets/gov/rc/ntr/ntr_paskirtys`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_paskirtys.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesTipas`
- **Primary Key (`ref`):** `pask_tipas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pask_tipas` | `integer` | — | `4` | `open` | — | Turto paskirtis | — |
| `pasg_grupe` | `ref` | [NtrPaskirtiesGrupe](NtrPaskirtiesGrupe.md) | `4` | `open` | — | Paskirties grupė | — |
| `pask_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `pask_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `pask_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `pask_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv
