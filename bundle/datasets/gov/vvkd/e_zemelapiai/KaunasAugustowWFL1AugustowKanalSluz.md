---
type: Table
title: "KaunasAugustowWFL1AugustowKanalSluz — Augustavo kanalo geoerdviniai duomenys"
description: "Šiame sluoksnyje pateikiami Augustavo kanalo šliuzų geoerdviniai duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1AugustowKanalSluz"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L59"
    last_modified: "2026-11-11T14:39:20Z"
---

# KaunasAugustowWFL1AugustowKanalSluz — Augustavo kanalo geoerdviniai duomenys

Šiame sluoksnyje pateikiami Augustavo kanalo šliuzų geoerdviniai duomenys. Nurodomi šliuzų pavadinimai, kampai ir geoerdvinės lokacijos.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1AugustowKanalSluz`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L59](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L59)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1AugustowKanalSluz`
- **Primary Key (`ref`):** `objectid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objectid` | `string` | — | `4` | `open` | — | Atributinės lentelės objekto numeris | — |
| `name` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `angle` | `number` | `°` | `4` | `open` | — | Sutartinio ženklo pasūkimo kampas | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
