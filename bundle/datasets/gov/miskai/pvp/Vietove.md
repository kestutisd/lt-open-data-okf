---
type: Table
title: "Vietove — Vietovė"
description: "Vietovė / Blokas : Sklypas = kadastro numeris"
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp/Vietove"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L29"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vietove — Vietovė

Vietovė / Blokas : Sklypas = kadastro numeris

- **Model:** `datasets/gov/miskai/pvp/Vietove`[^manifest]
- **Dataset:** [datasets/gov/miskai/pvp](../pvp.md) (`datasets/gov/miskai/pvp`)
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L29)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp/Vietove`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vietove` | `string` | — | `3` | `open` | — | Vietovė | Vietovės kodas |
| `rajonas` | `ref` | [Rajonas](Rajonas.md) | `4` | `open` | — | Rajonas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv
