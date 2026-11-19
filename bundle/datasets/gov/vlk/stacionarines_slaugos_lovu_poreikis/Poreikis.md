---
type: Table
title: "Poreikis — Stacionarinės slaugos lovų poreikis"
description: "Informacija apie metinį stacionarinių slaugos lovų poreikį pagal savivaldybes"
resource: "https://get.data.gov.lt/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis/Poreikis"
tags: [gov, vlk, poreikis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1588/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Poreikis — Stacionarinės slaugos lovų poreikis

Informacija apie metinį stacionarinių slaugos lovų poreikį pagal savivaldybes[^manifest]

- **Model:** `datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis/Poreikis`[^manifest]
- **Dataset:** [Stacionarinės slaugos lovų poreikis](../stacionarines_slaugos_lovu_poreikis.md) (`datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis/Poreikis` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/stacionarines_slaugos_lovu_poreikis (https://data.gov.lt/datasets/1588/)
