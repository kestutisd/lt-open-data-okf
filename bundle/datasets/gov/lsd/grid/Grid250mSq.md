---
type: Table
title: "Grid250mSq — Šešiakampės gardelės 250 m (LKS-94)"
description: "Spinta table datasets/gov/lsd/grid/Grid250mSq (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/grid/Grid250mSq"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/grid.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/grid.csv#L35"
    last_modified: "2026-11-11T14:39:20Z"
---

# Grid250mSq — Šešiakampės gardelės 250 m (LKS-94)

- **Model:** `datasets/gov/lsd/grid/Grid250mSq`[^manifest]
- **Dataset:** [Tinkleliai sudaryti LKS-94 Lietuvos valstybinėje koordinačių sistemoje](../grid.md) (`datasets/gov/lsd/grid`)
- **Manifest CSV:** [datasets/gov/lsd/grid.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/grid.csv#L35)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/grid/Grid250mSq`
- **Primary Key (`ref`):** `grid_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grid_id` | `string` | — | `4` | `open` | — | Gardelės unikalus kodas | Susideda iš gardelės dydžio (pvz. 250 m) + gardelės centro x koordinatės (pirmieji 6 skaitmenys) + gardelės centro y koordinatės (pirmieji 7 skaitmenys) |
| `x_centroid` | `integer` | — | `2` | `open` | — | Gardelės centro x koordinatė (LKS94) | — |
| `y_centroid` | `integer` | — | `2` | `open` | — | Gardelės centro y koordinatė (LKS94) | — |
| `sav_pav` | `string` | — | `3` | `open` | — | Savivaldybės pavadinimas į kurią patenka gardelės centras | — |
| `sav_kodas` | `string` | — | `2` | `open` | — | Savivaldybės dviženklis kodas į kurią patenka gardelės centras | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Objekto geometrija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/grid.csv
