---
type: Table
title: "Sekla — Pateikiama informacija apie sertifikuotos bulvių sėklos veislę, kategoriją / klasę, kiekį, kg"
description: "Spinta table datasets/gov/vat/sert_bulv/Sekla (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/sert_bulv/Sekla"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r19_sertif_bulv.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r19_sertif_bulv.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sekla — Pateikiama informacija apie sertifikuotos bulvių sėklos veislę, kategoriją / klasę, kiekį, kg

- **Model:** `datasets/gov/vat/sert_bulv/Sekla`[^manifest]
- **Dataset:** [datasets/gov/vat/sert_bulv](../sert_bulv.md) (`datasets/gov/vat/sert_bulv`)
- **Manifest CSV:** [datasets/gov/vat/r19_sertif_bulv.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r19_sertif_bulv.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/sert_bulv/Sekla`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `veisle` | `string` | — | `4` | `open` | — | Augalo veislės pavadinimas | — |
| `kategorija` | `string` | — | `3` | `open` | — | Kategorijos kodas | — |
| `kiekis` | `number` | `U` | `4` | `open` | — | Sėklos kiekis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r19_sertif_bulv.csv
