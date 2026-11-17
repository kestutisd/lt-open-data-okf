---
type: Table
title: "TaksacRodiklis — Visų miškų medynų taksaciniai rodikliai"
description: "Spinta table datasets/gov/miskai/apskaita/TaksacRodiklis (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/apskaita/TaksacRodiklis"
tags: [gov, miskai, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L44"
    last_modified: "2026-11-11T14:39:20Z"
---

# TaksacRodiklis — Visų miškų medynų taksaciniai rodikliai

- **Model:** `datasets/gov/miskai/apskaita/TaksacRodiklis`[^manifest]
- **Dataset:** [datasets/gov/miskai/apskaita](../apskaita.md) (`datasets/gov/miskai/apskaita`)
- **Manifest CSV:** [datasets/gov/miskai/apskaita.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L44)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/apskaita/TaksacRodiklis`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `medynai` | `string` | — | `2` | `open` | — | Medynai | — |
| `plotas_visu_med` | `number` | `ha` | `4` | `open` | — | Visų medynų plotas | — |
| `turis_visu_med` | `number` | — | `3` | `open` | — | Visų medynų tūris, tūkst. m3 | — |
| `plotas_brandziu_med` | `number` | `ha` | `4` | `open` | — | Brandžių medynų plotas | — |
| `turis_brandziu_med` | `number` | — | `3` | `open` | — | Brandžių medynų tūris, tūkst. m3 | — |
| `prieaugis_turio_pok` | `number` | — | `3` | `open` | — | Prieaugis. Tūrio pokytis | — |
| `prieaugis_bendras` | `number` | — | `3` | `open` | — | Prieaugis. Bendras einamasis | — |
| `amzius` | `integer` | — | `3` | `open` | — | Vidutiniai taksaciniai rodikliai. Amžius | — |
| `bonitetas` | `number` | — | `3` | `open` | — | Vidutiniai taksaciniai rodikliai. Bonitetas | — |
| `skalsumas` | `number` | — | `3` | `open` | — | Vidutiniai taksaciniai rodikliai. Skalsumas | — |
| `vidut_turis_visu` | `integer` | — | `3` | `open` | — | Vidutinis visų medynų tūris | — |
| `vidut_turis_brandziu` | `integer` | — | `3` | `open` | — | Vidutinis brandžių medynų tūris | — |
| `vidut_turio_pokytis` | `number` | — | `3` | `open` | — | Prieaugis. Vidutinis tūrio pokytis | — |
| `vidut_prieaugis_bendras` | `number` | — | `3` | `open` | — | Prieaugis. Vidutinis bendras einamasis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv
