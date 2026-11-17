---
type: Table
title: "GylisDruskininkaiNevezisVilnius — Gylių duomenys"
description: "Šiame sluoksnyje pateikiami gylių duomenis Nemune Druskininkuose, Neryje Vilniuje ir Nevėžyje."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisDruskininkaiNevezisVilnius"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# GylisDruskininkaiNevezisVilnius — Gylių duomenys

Šiame sluoksnyje pateikiami gylių duomenis Nemune Druskininkuose, Neryje Vilniuje ir Nevėžyje.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/GylisDruskininkaiNevezisVilnius`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisDruskininkaiNevezisVilnius`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `atkarpa` | `string` | — | `3` | `open` | — | Upės ruožo atkarpos pavadinimas | — |
| `eil_nr` | `string` | — | `4` | `open` | — | Taško eilės numeracija | — |
| `gylis_cm` | `number` | `cm` | `4` | `open` | — | Gylis centimetrais | — |
| `data` | `datetime` | `L` | `4` | `open` | — | Data | — |
| `skales_tip` | `string` | — | `4` | `open` | — | Sutartinio ženklo klasifikatoriaus kodas | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto plotas | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
