---
type: Table
title: "KaunasAugustowWFL1WaterwayKaunasAugustow — Vandens kelio Kaunas Augustavas geoerdviniai duomenys"
description: "Šiame sluoksnyje pateikiami Vandens kelio Kaunas Augustavas geoerdviniai duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1WaterwayKaunasAugustow"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L72"
    last_modified: "2026-11-11T14:39:20Z"
---

# KaunasAugustowWFL1WaterwayKaunasAugustow — Vandens kelio Kaunas Augustavas geoerdviniai duomenys

Šiame sluoksnyje pateikiami Vandens kelio Kaunas Augustavas geoerdviniai duomenys. Nurodomi atkarpų pavadinimai, gyliai, ilgiai ir pan.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1WaterwayKaunasAugustow`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L72](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L72)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/KaunasAugustowWFL1WaterwayKaunasAugustow`
- **Primary Key (`ref`):** `objectid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objectid` | `string` | — | `4` | `open` | — | Atributinės lentelės objekto numeris | — |
| `name` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `reach` | `string` | — | `4` | `open` | — | Ruožas | — |
| `depth` | `number` | `m` | `4` | `open` | — | Gylis | — |
| `length_km` | `number` | `km` | `4` | `open` | — | Ilgis kilometrais | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
