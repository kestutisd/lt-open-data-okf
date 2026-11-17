---
type: Table
title: "PasienioRuozas — Pasienio ruožo leidimų duomenys"
description: "Šiame sluoksnyje pateikiami pasienio ruožo leidimų duomenys Kuršių mariose Lietuva – Rusija pasienyje."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/PasienioRuozas"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L96"
    last_modified: "2026-11-11T14:39:20Z"
---

# PasienioRuozas — Pasienio ruožo leidimų duomenys

Šiame sluoksnyje pateikiami pasienio ruožo leidimų duomenys Kuršių mariose Lietuva – Rusija pasienyje.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/PasienioRuozas`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L96](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L96)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/PasienioRuozas`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `pav` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `info` | `string` | — | `4` | `open` | — | Informacija | — |
| `leidimai` | `string` | — | `4` | `open` | — | Leidimų duomenys | — |
| `leidimas` | `string` | — | `4` | `open` | — | Leidimų duomenys | — |
| `shape_area` | `number` | `m^2` | `4` | `open` | — | Objekto plotas | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto ilgis | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
