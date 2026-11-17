---
type: Table
title: "RoadSpecialist — Kelių specialistų sąrašas"
description: "Spinta table datasets/gov/ltsa/keliu_specialistai/RoadSpecialist (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/keliu_specialistai/RoadSpecialist"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/keliu_specialistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_specialistai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# RoadSpecialist — Kelių specialistų sąrašas

- **Model:** `datasets/gov/ltsa/keliu_specialistai/RoadSpecialist`[^manifest]
- **Dataset:** [Kelių specialistų sąrašas](../keliu_specialistai.md) (`datasets/gov/ltsa/keliu_specialistai`)
- **Manifest CSV:** [datasets/gov/ltsa/keliu_specialistai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_specialistai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/keliu_specialistai/RoadSpecialist`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `valid` | `string` | — | `2` | `open` | — | Galiojimo būklė | — |
| `type` | `string` | — | `3` | `open` | — | Tipas | — |
| `valid_to` | `datetime` | `D` | `4` | `open` | — | Galioja iki | — |
| `id` | `integer` | — | `4` | `open` | — | Pažymėjimo ID | — |
| `valid_from` | `datetime` | `D` | `4` | `open` | — | Galioja iki | — |
| `number` | `string` | — | `4` | `open` | — | Pažymėjimo numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/keliu_specialistai.csv
