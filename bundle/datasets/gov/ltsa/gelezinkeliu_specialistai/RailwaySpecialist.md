---
type: Table
title: "RailwaySpecialist — Geležinkelio specialistų pažymėjimai"
description: "Spinta table datasets/gov/ltsa/gelezinkeliu_specialistai/RailwaySpecialist (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_specialistai/RailwaySpecialist"
tags: [gov, ltsa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_specialistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# RailwaySpecialist — Geležinkelio specialistų pažymėjimai

- **Model:** `datasets/gov/ltsa/gelezinkeliu_specialistai/RailwaySpecialist`[^manifest]
- **Dataset:** [Geležinkelio specialistų pažymėjimai](../gelezinkeliu_specialistai.md) (`datasets/gov/ltsa/gelezinkeliu_specialistai`)
- **Manifest CSV:** [datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_specialistai/RailwaySpecialist`
- **Primary Key (`ref`):** `document_number`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `valid_to` | `datetime` | `D` | `4` | `open` | — | Teisė suteikta iki | — |
| `born` | `integer` | — | `2` | `open` | — | Gimimo metai | metai YY formatu |
| `valid_from` | `datetime` | `T` | `4` | `open` | — | Teisė galioja nuo | — |
| `document_number` | `string` | — | `2` | `open` | — | Dokumento numeris | — |
| `type` | `string` | — | `3` | `open` | — | Tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_specialistai.csv
