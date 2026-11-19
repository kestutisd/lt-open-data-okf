---
type: Table
title: "RoadSpecialist — Kelių specialistų sąrašas"
description: "Spinta table datasets/gov/ltsa/keliu_specialistai/RoadSpecialist (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/keliu_specialistai/RoadSpecialist"
tags: [gov, ltsa, roadspecialist, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_specialistai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/keliu_specialistai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2334/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/keliu_specialistai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# RoadSpecialist — Kelių specialistų sąrašas

- **Model:** `datasets/gov/ltsa/keliu_specialistai/RoadSpecialist`[^manifest]
- **Dataset:** [Kelių specialistų sąrašas](../keliu_specialistai.md) (`datasets/gov/ltsa/keliu_specialistai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/keliu_specialistai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_specialistai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/keliu_specialistai/RoadSpecialist` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `valid` | `string` | — | `2` | `open` | — | Galiojimo būklė | — |
| `type` | `string` | — | `3` | `open` | — | Tipas | — |
| `valid_to` | `datetime` | `D` | `4` | `open` | — | Galioja iki | — |
| `id` | `integer` | — | `4` | `open` | — | Pažymėjimo ID | — |
| `valid_from` | `datetime` | `D` | `4` | `open` | — | Galioja iki | — |
| `number` | `string` | — | `4` | `open` | — | Pažymėjimo numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/keliu_specialistai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_specialistai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/keliu_specialistai (https://data.gov.lt/datasets/2334/)
