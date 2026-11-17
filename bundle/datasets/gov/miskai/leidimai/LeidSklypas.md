---
type: Table
title: "LeidSklypas — Sklypai, kuriems išduotas leidimas"
description: "Spinta table datasets/gov/miskai/leidimai/LeidSklypas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/leidimai/LeidSklypas"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L42"
    last_modified: "2026-11-11T14:39:20Z"
---

# LeidSklypas — Sklypai, kuriems išduotas leidimas

- **Model:** `datasets/gov/miskai/leidimai/LeidSklypas`[^manifest]
- **Dataset:** [datasets/gov/miskai/leidimai](../leidimai.md) (`datasets/gov/miskai/leidimai`)
- **Manifest CSV:** [datasets/gov/miskai/leidimai.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L42)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/leidimai/LeidSklypas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leidimas` | `ref` | [Leidimas](Leidimas.md) | `4` | `open` | — | — | — |
| `kvartalo_nr` | `integer` | — | `3` | `open` | — | Kvartalas | Miško kvartalo numeris(-iai) |
| `sklypo_nr` | `string` | — | `3` | `open` | — | Sklypas | Sklypo numeris(-iai) |
| `sklypo_dal` | `string` | — | `3` | `open` | — | Sklypo dalis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv
