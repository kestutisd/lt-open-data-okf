---
type: Table
title: "NtrNaudojimoPubudis — NTR naudojimo pobūdžiai"
description: "Spinta table datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoPubudis (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoPubudis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_naudojimo_budai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrNaudojimoPubudis — NTR naudojimo pobūdžiai

- **Model:** `datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoPubudis`[^manifest]
- **Dataset:** [NTR paskirčių klasifikatoriai](../ntr_naudojimo_budai.md) (`datasets/gov/rc/ntr/ntr_naudojimo_budai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoPubudis`
- **Primary Key (`ref`):** `npob_pobudis`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `npob_pobudis` | `integer` | — | `4` | `open` | — | Naudojimo pobūdis | — |
| `naub_budas` | `ref` | [NtrNaudojimoBudas](NtrNaudojimoBudas.md) | `4` | `open` | — | Naudojimo būdas | — |
| `npob_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `npob_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `npob_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `npob_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `npob_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai (ilgas) | — |
| `npob_data_nuo` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja nuo | — |
| `npob_data_iki` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_naudojimo_budai.csv
