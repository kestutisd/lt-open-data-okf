---
type: Table
title: "ZenklasVilnius — Vandens kelių ženklų informaciniai duomenys"
description: "Šiame sluoksnyje pateikiami vidaus vandenų kelių ženklų geoerdviniai duomenys, pavadinimai, tipai ir pan. Sluoksnyje pateikiami ženklai išsidėstę Neryje Vilniuje."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/ZenklasVilnius"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L167"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZenklasVilnius — Vandens kelių ženklų informaciniai duomenys

Šiame sluoksnyje pateikiami vidaus vandenų kelių ženklų geoerdviniai duomenys, pavadinimai, tipai ir pan. Sluoksnyje pateikiami ženklai išsidėstę Neryje Vilniuje.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/ZenklasVilnius`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L167](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L167)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/ZenklasVilnius`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `pavadinim` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Tipas | — |
| `kodas` | `string` | — | `4` | `open` | — | Kodas | — |
| `info` | `string` | — | `4` | `open` | — | Informacija | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
