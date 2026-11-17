---
type: Table
title: "NtrAtributoPozymis — NTR atributų požymių (būtinas, galimas) klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_atributai/NtrAtributoPozymis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributoPozymis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L48"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrAtributoPozymis — NTR atributų požymių (būtinas, galimas) klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_atributai/NtrAtributoPozymis`[^manifest]
- **Dataset:** [NTR atributų klasifikatoriai](../ntr_atributai.md) (`datasets/gov/rc/ntr/ntr_atributai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L48)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributoPozymis`
- **Primary Key (`ref`):** `atrp_poz`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atrp_poz` | `integer` | — | `4` | `open` | — | Atributo požymis | — |
| `atrp_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `atrp_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv
