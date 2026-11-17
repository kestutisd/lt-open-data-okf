---
type: Table
title: "Prasymas — Duomenys apie Lietuvos Respublikos piliečių prašymus panaikinti Lietuvos Respublikos pilietybę."
description: "Spinta table datasets/gov/migracija/pilietybes_netekimas/Prasymas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/pilietybes_netekimas/Prasymas"
tags: [gov, migracija, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/pilietybes_netekimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/pilietybes_netekimas.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Duomenys apie Lietuvos Respublikos piliečių prašymus panaikinti Lietuvos Respublikos pilietybę.

- **Model:** `datasets/gov/migracija/pilietybes_netekimas/Prasymas`[^manifest]
- **Dataset:** [datasets/gov/migracija/pilietybes_netekimas](../pilietybes_netekimas.md) (`datasets/gov/migracija/pilietybes_netekimas`)
- **Manifest CSV:** [datasets/gov/migracija/pilietybes_netekimas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/pilietybes_netekimas.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/pilietybes_netekimas/Prasymas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `prasymo_registracija` | `date` | `D` | `4` | `open` | — | Prašymo registracijos data | — |
| `prasymas` | `string` | — | `3` | `open` | — | Prašymo pagrindas | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Asmens pilietybė | — |
| `skyrius` | `string` | — | `4` | `open` | — | Prašymo būsenos sukūrimo vieta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/pilietybes_netekimas.csv
