---
type: Table
title: "VietovesBlokas — Blokas"
description: "Vietovė / Blokas : Sklypas = kadastro numeris"
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp/VietovesBlokas"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L42"
    last_modified: "2026-11-11T14:39:20Z"
---

# VietovesBlokas — Blokas

Vietovė / Blokas : Sklypas = kadastro numeris

- **Model:** `datasets/gov/miskai/pvp/VietovesBlokas`[^manifest]
- **Dataset:** [datasets/gov/miskai/pvp](../pvp.md) (`datasets/gov/miskai/pvp`)
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L42)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp/VietovesBlokas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vietove` | `ref` | [Vietove](Vietove.md) | `4` | `open` | — | Vietovė | — |
| `kadblokas_id` | `integer` | — | `3` | `open` | — | Sąsaja su kadastriniu bloku | — |
| `blokas` | `string` | — | `3` | `open` | — | Blokas | Bloko kodas |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv
