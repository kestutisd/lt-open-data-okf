---
type: Table
title: "NekeltiBangu5 — Ženklo \"Nekelti bangų\" galiojimo zonos"
description: "Šiame sluoksnyje pateikiamos ženklo \"Nekelti bangų\" galiojimo zonos Minijoje Mingės kaime ir Sakūčiuose."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/NekeltiBangu5"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L87"
    last_modified: "2026-11-11T14:39:20Z"
---

# NekeltiBangu5 — Ženklo "Nekelti bangų" galiojimo zonos

Šiame sluoksnyje pateikiamos ženklo "Nekelti bangų" galiojimo zonos Minijoje Mingės kaime ir Sakūčiuose.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/NekeltiBangu5`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L87](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L87)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/NekeltiBangu5`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `id` | `string` | — | `4` | `open` | — | Unikalus ID numeris | — |
| `info_lt` | `string` | — | `4` | `open` | — | Informacija | — |
| `shape_area` | `number` | `m^2` | `4` | `open` | — | Objekto plotas | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto ilgis | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `info_lt` | `update(property: "info_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
