---
type: Table
title: "Poreikis — Stacionarinės slaugos lovų poreikis"
description: "Informacija apie metinį stacionarinių slaugos lovų poreikį pagal savivaldybes"
resource: "https://get.data.gov.lt/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis/Poreikis"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Poreikis — Stacionarinės slaugos lovų poreikis

Informacija apie metinį stacionarinių slaugos lovų poreikį pagal savivaldybes

- **Model:** `datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis/Poreikis`[^manifest]
- **Dataset:** [datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis](../stacionarines_slaugos_lovu_poreikis.md) (`datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis`)
- **Manifest CSV:** [datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis/Poreikis`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Laikotarpis (metai) | Ataskaitinio laikotarpio metai |
| `teritorija` | `string` | — | `3` | `open` | — | Teritorija | Teritorija, kurioje vertinamas lovų poreikis |
| `poreikis_1000` | `number` | `U` | `4` | `open` | — | Lovų poreikis 1000 savivaldybės statistinių gyventojų, atsižvelgiant į jų amžių, kai vidutinis šalies normatyvas 3 lovos / 1000 gyv. | — |
| `fakt_skaicius_1000` | `number` | `U` | `4` | `open` | — | Faktinis finansuojamų lovų skaičius 1000 savivaldybės statistinių gyventojų (ataskaitinių metų pradžios duomenys) | — |
| `poreikis` | `number` | `U` | `4` | `open` | — | Lovų poreikis | — |
| `fakt_skaicius` | `number` | `U` | `4` | `open` | — | Faktinis lovų skaičius | Faktinis finansuojamų lovų skaičius (ataskaitiniais metais) |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv
