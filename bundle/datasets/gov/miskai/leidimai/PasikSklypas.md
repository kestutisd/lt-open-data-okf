---
type: Table
title: "PasikSklypas — Išduotų leidimų sklypai"
description: "Spinta table datasets/gov/miskai/leidimai/PasikSklypas (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/leidimai/PasikSklypas"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L52"
    last_modified: "2026-11-11T14:39:20Z"
---

# PasikSklypas — Išduotų leidimų sklypai

- **Model:** `datasets/gov/miskai/leidimai/PasikSklypas`[^manifest]
- **Dataset:** [datasets/gov/miskai/leidimai](../leidimai.md) (`datasets/gov/miskai/leidimai`)
- **Manifest CSV:** [datasets/gov/miskai/leidimai.csv#L52](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L52)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/leidimai/PasikSklypas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `l_sklypas` | `ref` | [LeidSklypas](LeidSklypas.md) | `4` | `open` | — | — | — |
| `skl_plotas` | `number` | `ha` | `4` | `open` | — | Plotas | Miško plotas (ha) |
| `up` | `ref` | [UkinePriemone](UkinePriemone.md) | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv
