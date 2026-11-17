---
type: Table
title: "NtrTeisesTipas — NTR teisių ir suvaržymų tipai"
description: "Spinta table datasets/gov/rc/ntr/ntr_teises/NtrTeisesTipas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises/NtrTeisesTipas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrTeisesTipas — NTR teisių ir suvaržymų tipai

- **Model:** `datasets/gov/rc/ntr/ntr_teises/NtrTeisesTipas`[^manifest]
- **Dataset:** [NTR teisių tipų ir teisių potipių klasifikatoriai](../ntr_teises.md) (`datasets/gov/rc/ntr/ntr_teises`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_teises.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises/NtrTeisesTipas`
- **Primary Key (`ref`):** `teit_tipas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teit_tipas` | `integer` | — | `4` | `open` | — | Teisės (suvaržymo) tipas | — |
| `teit_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `teit_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `teit_eilnr` | `integer` | — | `4` | `open` | — | Eilės numeris aplikacijose | — |
| `teit_poz` | `integer` | — | `3` | `open` | — | Aplikacijos požymis | — |
| `teit_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `teit_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `teit_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai (ilgas) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv
