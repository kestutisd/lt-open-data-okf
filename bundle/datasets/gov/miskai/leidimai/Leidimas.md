---
type: Table
title: "Leidimas — Leidimai kirsti mišką"
description: "Spinta table datasets/gov/miskai/leidimai/Leidimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/leidimai/Leidimas"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Leidimai kirsti mišką

- **Model:** `datasets/gov/miskai/leidimai/Leidimas`[^manifest]
- **Dataset:** [datasets/gov/miskai/leidimai](../leidimai.md) (`datasets/gov/miskai/leidimai`)
- **Manifest CSV:** [datasets/gov/miskai/leidimai.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/leidimai/Leidimas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `numeris` | `number` | — | `3` | `open` | — | Leidimo numeris | Suteikto leidimo numeris |
| `serija` | `string` | — | `3` | `open` | — | Leidimo serija | Suteikto leidimo serija |
| `tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | Suteikto leidimo tipas |
| `kad_sklypo_nr` | `number` | — | `3` | `open` | — | Kadastrinio sklypo nr. | — |
| `mu` | `ref` | [Uredija](Uredija.md) | `4` | `open` | — | — | — |
| `ur_gir` | `ref` | [UrGir](UrGir.md) | `4` | `open` | — | — | — |
| `strukp` | `ref` | [STRUKPadalinys](STRUKPadalinys.md) | `4` | `open` | — | — | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Leidimas"` | — | — | Leidimas kirsti mišką | — |
| `tipas` | `"Pranešimas"` | — | — | Pranešimas apie ketinimą kirsti mišką | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv
