---
type: Table
title: "TuristineTrasa — Turistinės trasos duomenys"
description: "Šiame sluoksnyje pateikiami turistinės trasos geoerdviniai duomenys Nemune nuo Druskininkų iki Birštono."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/TuristineTrasa"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L140"
    last_modified: "2026-11-11T14:39:20Z"
---

# TuristineTrasa — Turistinės trasos duomenys

Šiame sluoksnyje pateikiami turistinės trasos geoerdviniai duomenys Nemune nuo Druskininkų iki Birštono.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/TuristineTrasa`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L140](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L140)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/TuristineTrasa`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `id` | `string` | — | `4` | `open` | — | Unikalus ID numeris | — |
| `zdugnas` | `number` | — | `2` | `open` | — | Dugno altitudė | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto ilgis | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
