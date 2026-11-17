---
type: Table
title: "NtrNaudojimoBudas — NTR naudojimo būdai"
description: "Spinta table datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoBudas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoBudas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_naudojimo_budai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrNaudojimoBudas — NTR naudojimo būdai

- **Model:** `datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoBudas`[^manifest]
- **Dataset:** [NTR paskirčių klasifikatoriai](../ntr_naudojimo_budai.md) (`datasets/gov/rc/ntr/ntr_naudojimo_budai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoBudas`
- **Primary Key (`ref`):** `naub_budas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `naub_budas` | `integer` | — | `4` | `open` | — | Naudojimo būdo kodas | — |
| `naub_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `naub_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `naub_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `naub_vert_grupe` | `integer` | — | `3` | `open` | — | Vertinimo grupė (neklasifikuota) | — |
| `naub_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `naub_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_naudojimo_budai.csv
