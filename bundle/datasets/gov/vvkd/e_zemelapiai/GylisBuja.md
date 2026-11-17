---
type: Table
title: "GylisBuja — Bujų geoerdviniai duomenys"
description: "Šiame sluoksnyje pateikiami Bujų duomenys Nemune."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisBuja"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# GylisBuja — Bujų geoerdviniai duomenys

Šiame sluoksnyje pateikiami Bujų duomenys Nemune.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/GylisBuja`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisBuja`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `nr` | `string` | — | `4` | `open` | — | Numeris | — |
| `spalva` | `string` | — | `3` | `open` | — | Spalva | — |
| `sv_signal` | `string` | — | `4` | `open` | — | Bujaus šviesos signalo kodas | — |
| `seka` | `string` | — | `4` | `open` | — | Seka | — |
| `data` | `datetime` | `L` | `4` | `open` | — | Data | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
