---
type: Table
title: "Produktas — Produktai"
description: "Lentelė „Produktai“."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/Produktas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Produktas — Produktai

Lentelė „Produktai“. Lentelę sudaro: negrįžtamai šifruotas produkto identifikatorius, pavadinimas, gamintojas, autorizacijos liudijimo sąlygos ir pastabos. Produktų pastabos aktualios tik produktams su galiojančiais autorizacijos liudijimais. Vienas įrašas atitinka vieną produktą.

- **Model:** `datasets/gov/lsd/nvsc/bpdb/Produktas`[^manifest]
- **Dataset:** [Biocidinių produktų duomenys](../bpdb.md) (`datasets/gov/lsd/nvsc/bpdb`)
- **Manifest CSV:** [datasets/gov/lsd/nvsc/bpdb.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/Produktas`
- **Primary Key (`ref`):** `produkto_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `produkto_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `produkto_pav` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `produkto_gamintojas` | `string` | — | `2` | `open` | — | Gamintojas | — |
| `autorizacijos_liudijimo_salygos` | `string` | — | `2` | `open` | — | Sąlygos, pagal kurias suteiktas autorizacijos liudijimas produktui | — |
| `pastaba` | `string` | — | `2` | `open` | — | Pastabos, aktualios tik produktams su galiojančiais autorizacijos liudijimais | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv
