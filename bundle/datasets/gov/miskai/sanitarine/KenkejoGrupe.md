---
type: Table
title: "KenkejoGrupe"
description: "Spinta table datasets/gov/miskai/sanitarine/KenkejoGrupe (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sanitarine/KenkejoGrupe"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# KenkejoGrupe

- **Model:** `datasets/gov/miskai/sanitarine/KenkejoGrupe`[^manifest]
- **Dataset:** [datasets/gov/miskai/sanitarine](../sanitarine.md) (`datasets/gov/miskai/sanitarine`)
- **Manifest CSV:** [datasets/gov/miskai/sanitarine.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine/KenkejoGrupe`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Kenkėjo grupės pavadinimas | — |
| `kodas` | `string` | — | `3` | `open` | — | Kenkėjo grupės kodas | — |
| `vieta` | `ref` | [Vieta](Vieta.md) | `4` | `open` | — | Vieta (medelynas ar miškas) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv
