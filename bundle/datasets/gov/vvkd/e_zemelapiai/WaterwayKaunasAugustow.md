---
type: Table
title: "WaterwayKaunasAugustow — Vandens kelio Kaunas - Augustavas geoerdviniai duomenys"
description: "Šiame sluoksnyje pateikiami vandens kelio Kaunas - Augustavas geoerdviniai duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/WaterwayKaunasAugustow"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L147"
    last_modified: "2026-11-11T14:39:20Z"
---

# WaterwayKaunasAugustow — Vandens kelio Kaunas - Augustavas geoerdviniai duomenys

Šiame sluoksnyje pateikiami vandens kelio Kaunas - Augustavas geoerdviniai duomenys. Sluoksnyje nurodomi ne tik geoerdviniai duomenys, bet ir gyliai, objektu pavadinimai ir pan.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/WaterwayKaunasAugustow`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L147](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L147)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/WaterwayKaunasAugustow`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `objectid` | `string` | — | `4` | `open` | — | Atributinės lentelės objekto numeris | — |
| `name` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `reach` | `string` | — | `4` | `open` | — | Ruožas | — |
| `depth` | `number` | `m` | `4` | `open` | — | Gylis | — |
| `length_km` | `number` | `km` | `4` | `open` | — | Atstumas kilometrais | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto ilgis | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
