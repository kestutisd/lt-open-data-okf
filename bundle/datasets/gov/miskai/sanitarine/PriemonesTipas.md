---
type: Table
title: "PriemonesTipas"
description: "Spinta table datasets/gov/miskai/sanitarine/PriemonesTipas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sanitarine/PriemonesTipas"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# PriemonesTipas

- **Model:** `datasets/gov/miskai/sanitarine/PriemonesTipas`[^manifest]
- **Dataset:** [datasets/gov/miskai/sanitarine](../sanitarine.md) (`datasets/gov/miskai/sanitarine`)
- **Manifest CSV:** [datasets/gov/miskai/sanitarine.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine/PriemonesTipas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Priemonės tipo pavadinimas | — |
| `vieta` | `ref` | [Vieta](Vieta.md) | `4` | `open` | — | Vieta (medelynas ar miškas) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv
