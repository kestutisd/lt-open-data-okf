---
type: Table
title: "Prasymas — Prašymai dėl Lietuvos Respublikos pilietybės"
description: "Spinta table datasets/gov/migracija/lt_pilietybe/Prasymas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe/Prasymas"
tags: [gov, migracija, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Prašymai dėl Lietuvos Respublikos pilietybės

- **Model:** `datasets/gov/migracija/lt_pilietybe/Prasymas`[^manifest]
- **Dataset:** [datasets/gov/migracija/lt_pilietybe](../lt_pilietybe.md) (`datasets/gov/migracija/lt_pilietybe`)
- **Manifest CSV:** [datasets/gov/migracija/lt_pilietybe.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe/Prasymas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `prasymo_registracija` | `date` | `D` | `4` | `open` | — | Prašymo registracijos data | — |
| `pateikimas` | `date` | `D` | `4` | `open` | — | Prašymo pateikimo data | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Asmens amžiaus grupė pagal gimimo datą | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Asmens pilietybė | — |
| `skubos_tvarka` | `boolean` | — | `4` | `open` | — | Prašymo nagrinėjimo tvarka | — |
| `skyrius` | `string` | — | `4` | `open` | — | Prašymo būsenos sukūrimo vieta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv
