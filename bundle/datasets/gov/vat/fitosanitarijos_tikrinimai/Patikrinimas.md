---
type: Table
title: "Patikrinimas — Pateikiama informacija apie atliktus fitosanitarinius tikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo data; žyma, kad tikrinami ne LR ūkio subjektai; metodinė sritis..."
description: "Spinta table datasets/gov/vat/fitosanitarijos_tikrinimai/Patikrinimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_tikrinimai/Patikrinimas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patikrinimas — Pateikiama informacija apie atliktus fitosanitarinius tikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo data; žyma, kad tikrinami ne LR ūkio subjektai; metodinė sritis...

- **Model:** `datasets/gov/vat/fitosanitarijos_tikrinimai/Patikrinimas`[^manifest]
- **Dataset:** [datasets/gov/vat/fitosanitarijos_tikrinimai](../fitosanitarijos_tikrinimai.md) (`datasets/gov/vat/fitosanitarijos_tikrinimai`)
- **Manifest CSV:** [datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_tikrinimai/Patikrinimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis stulpelis | — |
| `tikrinimo_pradzia` | `date` | `D` | `4` | `open` | — | Tikrinimo pradžios data | — |
| `tikrinimo_pabaiga` | `date` | `D` | `4` | `open` | — | Tikrinimo pabaigos data | — |
| `pobudis` | `string` | — | `4` | `open` | — | Tikrinimo pobūdis | — |
| `rusis` | `string` | — | `4` | `open` | — | Tikrinimo rūšis | — |
| `paimtas_meginys` | `boolean` | — | `4` | `open` | — | Paimtas mėginys | — |
| `tikrinamas_objektas` | `string` | — | `4` | `open` | — | Tikrinamo objekto rūšis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rusis` | `"neplaninis"` | — | — | — | — |
| `rusis` | `"planinis"` | — | — | — | — |
| `rusis` | `"planinis+neplaninis"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv
