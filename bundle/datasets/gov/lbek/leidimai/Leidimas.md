---
type: Table
title: "Leidimas — Lietuvos bioetikos komiteto duomenys"
description: "Spinta table datasets/gov/lbek/leidimai/Leidimas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lbek/leidimai/Leidimas"
tags: [gov, lbek, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lbek/lbek.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lbek/lbek.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Lietuvos bioetikos komiteto duomenys

- **Model:** `datasets/gov/lbek/leidimai/Leidimas`[^manifest]
- **Dataset:** [Lietuvos bioetikos komitetas](../leidimai.md) (`datasets/gov/lbek/leidimai`)
- **Manifest CSV:** [datasets/gov/lbek/lbek.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lbek/lbek.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lbek/leidimai/Leidimas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tyrimo_pavadinimas` | `string` | — | `4` | `open` | — | Lietuvoje atliekamų biomedicininių tyrimų pavadinimai | — |
| `protokolo_nr` | `string` | — | `4` | `open` | — | Tyrimo protokolo numeris | — |
| `leidimo_nr` | `string` | — | `4` | `open` | — | Tyrimo leidimo numeris | — |
| `isdavimo_data` | `date` | `D` | `4` | `open` | — | Tyrimo leidimo išdavimo data | — |
| `tyrimo_atlikimo_vieta` | `string` | — | `4` | `open` | — | Tyrimų leidimo išdavimo vieta | — |
| `tyrimo_uzsakovas` | `string` | — | `4` | `open` | — | Atliekamo tyrimo užsakovas | — |
| `galiojimo_data` | `date` | `D` | `4` | `open` | — | Numatoma biomedicininio tyrimo trukmė/data iki pabaigos/statusas | — |
| `euract_eudract_nr` | `string` | — | `4` | `open` | — | EURACT numeris/EUDRACT numeris | — |
| `leidima_isdavusi_institucija` | `string` | — | `4` | `open` | — | Leidimą tyrimams atlikti išdavusi institucija | — |
| `tyrimo_rusis` | `string` | — | `4` | `open` | — | Biomedicininio tyrimo rūšis | — |
| `tyrimo_faze` | `string` | — | `4` | `open` | — | Biomedicinio tyrimo fazė | — |
| `saltinis` | `string` | — | `4` | `open` | — | Šaltinis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lbek/lbek.csv
