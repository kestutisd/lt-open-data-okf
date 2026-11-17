---
type: Table
title: "TyrimoSudedamoji — Tyrimų sudedamosios"
description: "Spinta table datasets/gov/aaa/integruotas_monitoringas/TyrimoSudedamoji (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/TyrimoSudedamoji"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# TyrimoSudedamoji — Tyrimų sudedamosios

- **Model:** `datasets/gov/aaa/integruotas_monitoringas/TyrimoSudedamoji`[^manifest]
- **Dataset:** [datasets/gov/aaa/integruotas_monitoringas](../integruotas_monitoringas.md) (`datasets/gov/aaa/integruotas_monitoringas`)
- **Manifest CSV:** [datasets/gov/aaa/integruotas_monitoringas.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/TyrimoSudedamoji`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tsd_tad_id` | `string` | — | `4` | `open` | — | Tyrimo sudedamosios id | — |
| `tsd_tyrimo_tipas` | `string` | — | `4` | `open` | — | Tyrimo sudedamosios tyrimo tipas | — |
| `tad_laikotarpis_nuo` | `date` | `D` | `4` | `open` | — | Tyrimo laikotarpis nuo | — |
| `tad_laikotarpis_iki` | `date` | `D` | `4` | `open` | — | Tyrimo laikotarpis iki | — |
| `tad_gis_taskas` | `geometry(point, 3346)` | — | `3` | `open` | — | Tyrimo vieta | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tsd_tyrimo_tipas` | `"CHE"` | — | — | Cheminiai tyrimai | — |
| `tsd_tyrimo_tipas` | `"FIZ"` | — | — | Fizikiniai tyrimai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv
