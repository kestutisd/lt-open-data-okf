---
type: Table
title: "LKAPunktas — LKA punktai"
description: "Lentelėje pateikiami LKA punktų erdviniai taškai ir jų atributai: gyvenvietės pavadinimas, statusas, LKA punkto numeracija, savivaldybė, seniūnija, tarmės identifikatorius ir pavadinimas bei koordinačių sistema."
resource: "https://get.data.gov.lt/datasets/gov/lki/gyventoju_surasymas_2011/LKAPunktas"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/gyventoju_surasymas_2011.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/gyventoju_surasymas_2011.csv#L140"
    last_modified: "2026-11-11T14:39:20Z"
---

# LKAPunktas — LKA punktai

Lentelėje pateikiami LKA punktų erdviniai taškai ir jų atributai: gyvenvietės pavadinimas, statusas, LKA punkto numeracija, savivaldybė, seniūnija, tarmės identifikatorius ir pavadinimas bei koordinačių sistema.

- **Model:** `datasets/gov/lki/gyventoju_surasymas_2011/LKAPunktas`[^manifest]
- **Dataset:** [datasets/gov/lki/gyventoju_surasymas_2011](../gyventoju_surasymas_2011.md) (`datasets/gov/lki/gyventoju_surasymas_2011`)
- **Manifest CSV:** [datasets/gov/lki/gyventoju_surasymas_2011.csv#L140](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/gyventoju_surasymas_2011.csv#L140)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/gyventoju_surasymas_2011/LKAPunktas`
- **Primary Key (`ref`):** `feature_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `feature_id` | `integer` | — | `4` | `open` | — | Objekto identifikatorius | — |
| `geometry_type` | `string` | — | `4` | `open` | — | Geometrijos tipas | — |
| `x` | `number` | — | `4` | `open` | — | X koordinatė | — |
| `y` | `number` | — | `4` | `open` | — | Y koordinatė | — |
| `gyvenvietes_pavadinimas` | `string` | — | `4` | `open` | — | Gyvenvietės pavadinimas | — |
| `gyvenvietes_statusas` | `string` | — | `4` | `open` | — | Gyvenvietės statusas | — |
| `kodas` | `integer` | — | `4` | `open` | — | Objekto arba gyvenvietės kodas | — |
| `lka_punkt_pav` | `string` | — | `4` | `open` | — | LKA punkto pavadinimas | — |
| `lka_punkto_nr` | `string` | — | `4` | `open` | — | LKA punkto numeris | — |
| `lka_punkto_nr_raide` | `string` | — | `4` | `open` | — | LKA punkto numerio raidinis dėmuo | — |
| `lka_punkto_nr_sk` | `integer` | — | `4` | `open` | — | LKA punkto numerio skaitinis dėmuo | — |
| `objectid` | `integer` | — | `4` | `open` | — | Pirminio šaltinio objekto identifikatorius | — |
| `savivaldybes_pavadinimas` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `seniunijos_pavadinimas` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `tarmes_id` | `integer` | — | `4` | `open` | — | Tarmės identifikatorius | — |
| `tarmes_pav` | `string` | — | `4` | `open` | — | Tarmės pavadinimas | — |
| `crs_name` | `string` | — | `4` | `open` | — | Koordinačių sistemos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/gyventoju_surasymas_2011.csv
