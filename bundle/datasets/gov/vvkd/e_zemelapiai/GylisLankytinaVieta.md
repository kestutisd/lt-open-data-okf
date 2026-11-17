---
type: Table
title: "GylisLankytinaVieta — Lankytinų vietų geoerdviniai duomenys"
description: "Šiame sluoksnyje pateikiamos vidaus vandenų keliuose esančios lankytinos vietos (uostai, prieplaukos ir pan."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisLankytinaVieta"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L42"
    last_modified: "2026-11-11T14:39:20Z"
---

# GylisLankytinaVieta — Lankytinų vietų geoerdviniai duomenys

Šiame sluoksnyje pateikiamos vidaus vandenų keliuose esančios lankytinos vietos (uostai, prieplaukos ir pan.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/GylisLankytinaVieta`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L42)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisLankytinaVieta`
- **Primary Key (`ref`):** `objectid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objectid` | `string` | — | `4` | `open` | — | Atributinės lentelės objekto numeris | — |
| `pav_lt` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pav_lt` | `update(property: "pav_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
