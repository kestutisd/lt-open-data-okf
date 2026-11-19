---
type: Table
title: "Maitinimas — Gydymo įstaigos pacientų maitinimo paraiškos"
description: "Spinta table datasets/gov/ignalig_progra/maitinimo_paraiskos/Maitinimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ignalig_progra/maitinimo_paraiskos/Maitinimas"
tags: [gov, ignalig_progra, maitinimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2922/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ignalig_progra/maitinimo_paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Maitinimas — Gydymo įstaigos pacientų maitinimo paraiškos

- **Model:** `datasets/gov/ignalig_progra/maitinimo_paraiskos/Maitinimas`[^manifest]
- **Dataset:** [Gydymo įstaigos pacientų maitinimo paraiškos](../maitinimo_paraiskos.md) (`datasets/gov/ignalig_progra/maitinimo_paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ignalig_progra/maitinimo_paraiskos/Maitinimas` (`deployed`)[^manifest]
- **Provider:** `ignalig_progra` — VšĮ Ignalinos rajono savivaldybės sveikatos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `valgymas` | `"Pusryčiai"` | — | — | Pusryčiai | — |
| `valgymas` | `"Priešpiečiai"` | — | — | Priešpiečiai | — |
| `valgymas` | `"Pietūs"` | — | — | Pietūs | — |
| `valgymas` | `"Pavakariai"` | — | — | Pavakariai | — |
| `valgymas` | `"Vakarienė"` | — | — | Vakarienė | — |
| `valgymas` | `"Naktipiečiai"` | — | — | Naktipiečiai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ignalig_progra/maitinimo_paraiskos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ignalig_progra/maitinimo_paraiskos (https://data.gov.lt/datasets/2922/)
