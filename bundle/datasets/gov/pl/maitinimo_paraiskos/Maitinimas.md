---
type: Table
title: "Maitinimas — Prienų ligoninės maitinimo paraiškos"
description: "Šiame rinkinyje pateikiamas Prienų ligoninės maitinimo paraiškos: dienos patiekalų sąrašas, dietos, dienos maistinė vertė, valgančiųjų kiekis."
resource: "https://get.data.gov.lt/datasets/gov/pl/maitinimo_paraiskos/Maitinimas"
tags: [gov, pl, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pl/pl_maitinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pl/pl_maitinimas.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Maitinimas — Prienų ligoninės maitinimo paraiškos

Šiame rinkinyje pateikiamas Prienų ligoninės maitinimo paraiškos: dienos patiekalų sąrašas, dietos, dienos maistinė vertė, valgančiųjų kiekis. Duomenys pateikiami nuo 2019 metų pabaigos iki dabar.

- **Model:** `datasets/gov/pl/maitinimo_paraiskos/Maitinimas`[^manifest]
- **Dataset:** [Prienų ligoninės maitinimo paraiškos](../maitinimo_paraiskos.md) (`datasets/gov/pl/maitinimo_paraiskos`)
- **Manifest CSV:** [datasets/gov/pl/pl_maitinimas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pl/pl_maitinimas.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pl/maitinimo_paraiskos/Maitinimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `diena` | `date` | `D` | `4` | `open` | — | Maitinimo data | — |
| `porciju_kiekis` | `integer` | — | `4` | `open` | — | Porcijų kiekis | — |
| `valgymas` | `string` | — | `4` | `open` | — | Valgymo pavadinimas | — |
| `norma` | `number` | — | `2` | `open` | — | Norma | Įsakymu nustatyta ligonių visos dienos maitinimo piniginė norma. |
| `valgantis_padalinys` | `string` | — | `4` | `open` | — | Valgančio padalinio pavadinimas | — |
| `patiekalas` | `string` | — | `4` | `open` | — | Atsargos pavadinimas | — |
| `patiekalo_grupe` | `string` | — | `4` | `open` | — | Grupės pavadinimas | — |
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
| `valgymas` | `"Nakčiai"` | — | — | Naktipiečiai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pl/pl_maitinimas.csv
