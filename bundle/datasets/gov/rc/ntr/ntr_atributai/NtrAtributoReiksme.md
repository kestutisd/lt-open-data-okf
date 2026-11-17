---
type: Table
title: "NtrAtributoReiksme — NTR atributų reikšmių klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_atributai/NtrAtributoReiksme (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributoReiksme"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrAtributoReiksme — NTR atributų reikšmių klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_atributai/NtrAtributoReiksme`[^manifest]
- **Dataset:** [NTR atributų klasifikatoriai](../ntr_atributai.md) (`datasets/gov/rc/ntr/ntr_atributai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributoReiksme`
- **Primary Key (`ref`):** `atri_kodas, reik_reiksme`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atri_kodas` | `ref` | [NtrAtributas](NtrAtributas.md) | `4` | `open` | — | Atributo kodas | — |
| `reik_reiksme` | `integer` | — | `3` | `open` | — | Reikšmės kodas | — |
| `reik_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `reik_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `reik_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `reik_naudojama` | `integer` | — | `4` | `open` | — | Požymis, ar atributo reikšmė naudojama | — |
| `reik_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `reik_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `reik_naudojama` | `1` | — | — | Ne | — |
| `reik_naudojama` | `0` | — | — | Taip | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv
