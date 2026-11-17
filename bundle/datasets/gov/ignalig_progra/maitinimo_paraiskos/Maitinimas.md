---
type: Table
title: "Maitinimas — Gydymo įstaigos pacientų maitinimo paraiškos"
description: "Spinta table datasets/gov/ignalig_progra/maitinimo_paraiskos/Maitinimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ignalig_progra/maitinimo_paraiskos/Maitinimas"
tags: [gov, ignalig_progra, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ignalig_progra/maitinimo_paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Maitinimas — Gydymo įstaigos pacientų maitinimo paraiškos

- **Model:** `datasets/gov/ignalig_progra/maitinimo_paraiskos/Maitinimas`[^manifest]
- **Dataset:** [datasets/gov/ignalig_progra/maitinimo_paraiskos](../maitinimo_paraiskos.md) (`datasets/gov/ignalig_progra/maitinimo_paraiskos`)
- **Manifest CSV:** [datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ignalig_progra/maitinimo_paraiskos/Maitinimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `diena` | `date` | `D` | `4` | `open` | — | Maitinimo data | — |
| `porciju_kiekis` | `integer` | — | `4` | `open` | — | Porcijų kiekis | — |
| `valgymas` | `string` | — | `4` | `open` | — | Valgymo pavadinimas | — |
| `norma` | `number` | — | `4` | `open` | — | Norma | — |
| `valgantis_padalinys` | `string` | — | `4` | `open` | — | Valgančio padalinio pavadinimas | — |
| `patiekalas` | `string` | — | `4` | `open` | — | Atsargos pavadinimas | — |
| `patiekalo_savikaina` | `number` | — | `4` | `open` | — | Atsargos savikaina | — |
| `dietos_pavadinimas` | `string` | — | `2` | `open` | — | Dietos pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `valgymas` | `"Pusryčiai"` | — | — | Pusryčiai | — |
| `valgymas` | `"Priešpiečiai"` | — | — | Priešpiečiai | — |
| `valgymas` | `"Pietūs"` | — | — | Pietūs | — |
| `valgymas` | `"Pavakariai"` | — | — | Pavakariai | — |
| `valgymas` | `"Vakarienė"` | — | — | Vakarienė | — |
| `valgymas` | `"Naktipiečiai"` | — | — | Naktipiečiai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ignalig_progra/maitinimo_paraiskos.csv
