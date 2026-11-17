---
type: Table
title: "TarsosZidinys — Potencialūs taršos židiniai"
description: "Spinta table datasets/gov/lgt/potencialus_tarsos_zidiniai/TarsosZidinys (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/potencialus_tarsos_zidiniai/TarsosZidinys"
tags: [gov, lgt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/potencialus_tarsos_zidiniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# TarsosZidinys — Potencialūs taršos židiniai

- **Model:** `datasets/gov/lgt/potencialus_tarsos_zidiniai/TarsosZidinys`[^manifest]
- **Dataset:** [Potencialūs taršos židiniai](../potencialus_tarsos_zidiniai.md) (`datasets/gov/lgt/potencialus_tarsos_zidiniai`)
- **Manifest CSV:** [datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/potencialus_tarsos_zidiniai/TarsosZidinys`
- **Primary Key (`ref`):** `objecto_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objecto_nr` | `integer` | — | `4` | `open` | — | Objekto numeris | — |
| `ptz_adresas` | `string` | — | `1` | `open` | — | Adresas | — |
| `ptz_anketos_nr` | `string` | — | `4` | `open` | — | Anketos numeris | — |
| `ptz_anketos_data` | `date` | `D` | `4` | `open` | — | Vertinimo data | — |
| `ptz_objekto_bukle` | `string` | — | `3` | `open` | — | Objekto būklė | — |
| `ptz_objekto_tipas` | `string` | — | `3` | `open` | — | Objekto tipas | — |
| `ptz_pavojingumas_aplinkai` | `string` | — | `3` | `open` | — | Pavojingumo aplinkai įvertinimas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Koordinatės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/potencialus_tarsos_zidiniai.csv
