---
type: Table
title: "RusijosFederacija — Rusijos Federacijos riba"
description: "Šiame sluoksnyje pateikiama pasienio ruožo Lietuva – Rusija zona ties Nemunu."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/RusijosFederacija"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L106"
    last_modified: "2026-11-11T14:39:20Z"
---

# RusijosFederacija — Rusijos Federacijos riba

Šiame sluoksnyje pateikiama pasienio ruožo Lietuva – Rusija zona ties Nemunu.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/RusijosFederacija`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L106](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L106)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/RusijosFederacija`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `id` | `string` | — | `4` | `open` | — | Unikalus ID numeris | — |
| `pav` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `shape_area` | `number` | `m^2` | `4` | `open` | — | Objekto plotas | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto ilgis | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
