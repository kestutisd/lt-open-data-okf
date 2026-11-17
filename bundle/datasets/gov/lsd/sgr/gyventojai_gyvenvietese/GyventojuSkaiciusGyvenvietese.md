---
type: Table
title: "GyventojuSkaiciusGyvenvietese"
description: "Gyventojų skaičius gyvenvietėse ir gyvenviečių koordinates."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sgr/gyventojai_gyvenvietese/GyventojuSkaiciusGyvenvietese"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyventojuSkaiciusGyvenvietese

Gyventojų skaičius gyvenvietėse ir gyvenviečių koordinates.

- **Model:** `datasets/gov/lsd/sgr/gyventojai_gyvenvietese/GyventojuSkaiciusGyvenvietese`[^manifest]
- **Dataset:** [gyventojų skaičius gyvenvietėse](../gyventojai_gyvenvietese.md) (`datasets/gov/lsd/sgr/gyventojai_gyvenvietese`)
- **Manifest CSV:** [datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sgr/gyventojai_gyvenvietese/GyventojuSkaiciusGyvenvietese`
- **Primary Key (`ref`):** `gr_gyv_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gr_gyv_id` | `string` | — | `4` | `open` | — | Gyvenvietės identifikacinis kodas | — |
| `gyv_pav` | `string` | — | `4` | `open` | — | Gyvenvietės pavadinimas | — |
| `gyventoju_sk` | `number` | — | `4` | `open` | — | Gyventojų skaičius | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | Koordinate wgs 84 formatu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv
