---
type: Table
title: "Siunta — Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų..."
description: "Spinta table datasets/gov/vat/seklu_mainai/Siunta (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/seklu_mainai/Siunta"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r26_seklu_mainai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r26_seklu_mainai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Siunta — Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų...

- **Model:** `datasets/gov/vat/seklu_mainai/Siunta`[^manifest]
- **Dataset:** [datasets/gov/vat/seklu_mainai](../seklu_mainai.md) (`datasets/gov/vat/seklu_mainai`)
- **Manifest CSV:** [datasets/gov/vat/r26_seklu_mainai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r26_seklu_mainai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/seklu_mainai/Siunta`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `rusis` | `string` | — | `3` | `open` | — | Asmens nurodyta augalo rūšis | — |
| `veisle` | `string` | — | `3` | `open` | — | Asmens nurodyta augalo veislė | — |
| `kiekis` | `number` | `g` | `4` | `open` | — | Sėklos kiekis, g | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "metai", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r26_seklu_mainai.csv
