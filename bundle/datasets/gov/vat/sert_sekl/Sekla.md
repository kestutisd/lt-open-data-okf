---
type: Table
title: "Sekla — Pateikiama informacija apie sertifikuotos sėklos augalo rūšį, veislę, kategoriją, kiekį, kg"
description: "Spinta table datasets/gov/vat/sert_sekl/Sekla (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/sert_sekl/Sekla"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r20_sert_sekl.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r20_sert_sekl.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sekla — Pateikiama informacija apie sertifikuotos sėklos augalo rūšį, veislę, kategoriją, kiekį, kg

- **Model:** `datasets/gov/vat/sert_sekl/Sekla`[^manifest]
- **Dataset:** [datasets/gov/vat/sert_sekl](../sert_sekl.md) (`datasets/gov/vat/sert_sekl`)
- **Manifest CSV:** [datasets/gov/vat/r20_sert_sekl.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r20_sert_sekl.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/sert_sekl/Sekla`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `grupe` | `string` | — | `4` | `open` | — | Augalo grupė | — |
| `rusis` | `string` | — | `3` | `open` | — | Augalo rūšies pavadinimas | — |
| `veisle` | `string` | — | `4` | `open` | — | Augalo veislės pavadinimas | — |
| `kategorija` | `string` | — | `3` | `open` | — | Kategorijos kodas | — |
| `kiekis` | `number` | `U` | `4` | `open` | — | Sėklos kiekis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `grupe` | `"Javai"` | — | — | — | — |
| `grupe` | `"Pašariniai augalai"` | — | — | — | — |
| `grupe` | `"Aliejiniai ir pluoštiniai augalai"` | — | — | — | — |
| `grupe` | `"Sėjamieji grikiai"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r20_sert_sekl.csv
