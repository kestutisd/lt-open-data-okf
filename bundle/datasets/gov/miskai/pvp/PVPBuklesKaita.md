---
type: Table
title: "PVPBuklesKaita — Projekto būklės data"
description: "Spinta table datasets/gov/miskai/pvp/PVPBuklesKaita (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp/PVPBuklesKaita"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# PVPBuklesKaita — Projekto būklės data

- **Model:** `datasets/gov/miskai/pvp/PVPBuklesKaita`[^manifest]
- **Dataset:** [datasets/gov/miskai/pvp](../pvp.md) (`datasets/gov/miskai/pvp`)
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp/PVPBuklesKaita`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bukle` | `ref` | [PVPBukle](PVPBukle.md) | `4` | `open` | — | Būklė | — |
| `bukles_data` | `datetime` | — | `4` | `open` | — | Būklės data | — |
| `pvproj` | `ref` | [PrivacValduProjektas](PrivacValduProjektas.md) | `4` | `open` | — | Projektas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv
