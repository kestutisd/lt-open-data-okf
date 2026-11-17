---
type: Table
title: "Tyrimas — Tyrimai"
description: "Spinta table datasets/gov/aaa/integruotas_monitoringas/Tyrimas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/Tyrimas"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tyrimas — Tyrimai

- **Model:** `datasets/gov/aaa/integruotas_monitoringas/Tyrimas`[^manifest]
- **Dataset:** [datasets/gov/aaa/integruotas_monitoringas](../integruotas_monitoringas.md) (`datasets/gov/aaa/integruotas_monitoringas`)
- **Manifest CSV:** [datasets/gov/aaa/integruotas_monitoringas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/Tyrimas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tad_id` | `string` | — | `4` | `open` | — | Tyrimo id | — |
| `tad_laikotarpis_nuo` | `date` | `D` | `4` | `open` | — | Tyrimo laikotarpis nuo | — |
| `tad_laikotarpis_iki` | `date` | `D` | `4` | `open` | — | Tyrimo laikotarpis iki | — |
| `tad_gis_taskas` | `geometry(point, 3346)` | — | `3` | `open` | — | Tyrimo vieta | — |
| `vkl_pavad` | `string` | — | `3` | `open` | — | Veiklos pavadinimas | — |
| `ttr_pavad` | `string` | — | `4` | `open` | — | Tyrimų terpės pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ttr_pavad` | `"Aplinkos oras"` | — | — | Aplinkos oras | — |
| `ttr_pavad` | `"Biota"` | — | — | Biota | — |
| `ttr_pavad` | `"Paviršinis vanduo"` | — | — | Paviršinis vanduo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv
