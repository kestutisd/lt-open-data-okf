---
type: Table
title: "Grid1KmSq — Stačiakampės gardelės 1 km (LKS-94)"
description: "Spinta table datasets/gov/lsd/grid/Grid1KmSq (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/grid/Grid1KmSq"
tags: [gov, lsd, grid1kmsq, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/grid.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/lsd/grid.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2047/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/grid"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Grid1KmSq — Stačiakampės gardelės 1 km (LKS-94)

- **Model:** `datasets/gov/lsd/grid/Grid1KmSq`[^manifest]
- **Dataset:** [Tinkleliai sudaryti LKS-94 Lietuvos valstybinėje koordinačių sistemoje](../grid.md) (`datasets/gov/lsd/grid`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/grid.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/grid.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/grid/Grid1KmSq` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `grid_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grid_id` | `string` | — | `4` | `open` | — | Gardelės unikalus kodas | Susideda iš gardelės dydžio (pvz. 1 km) + gardelės centro x koordinatės (pirmieji 6 skaitmenys) + gardelės centro y koordinatės (pirmieji 7 skaitmenys) |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/grid.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/grid.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/grid (https://data.gov.lt/datasets/2047/)
