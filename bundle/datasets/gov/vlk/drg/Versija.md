---
type: Table
title: "Versija — DRG versijos"
description: "AR-DRG klasifikacijos versija"
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg/Versija"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L45"
    last_modified: "2026-11-11T14:39:20Z"
---

# Versija — DRG versijos

AR-DRG klasifikacijos versija

- **Model:** `datasets/gov/vlk/drg/Versija`[^manifest]
- **Dataset:** [datasets/gov/vlk/drg](../drg.md) (`datasets/gov/vlk/drg`)
- **Manifest CSV:** [datasets/gov/vlk/drg.csv#L45](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L45)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg/Versija`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `versija` | `string` | — | `4` | `open` | — | Versija | AR-DRG klasifikacijos versija |
| `nuo` | `date` | `D` | `4` | `open` | — | Versija galioja nuo | AR-DRG klasifikacijos versijos galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Versija galioja iki | AR-DRG klasifikacijos versijos galiojimo pabaigos data |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg.csv
