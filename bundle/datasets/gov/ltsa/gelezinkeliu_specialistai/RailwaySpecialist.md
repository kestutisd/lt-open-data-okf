---
type: Table
title: "RailwaySpecialist — Geležinkelio specialistų pažymėjimai"
description: "Spinta table datasets/gov/ltsa/gelezinkeliu_specialistai/RailwaySpecialist (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_specialistai/RailwaySpecialist"
tags: [gov, ltsa, railwayspecialist, deployed, level-2, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2333/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/gelezinkeliu_specialistai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# RailwaySpecialist — Geležinkelio specialistų pažymėjimai

- **Model:** `datasets/gov/ltsa/gelezinkeliu_specialistai/RailwaySpecialist`[^manifest]
- **Dataset:** [Geležinkelio specialistų pažymėjimai](../gelezinkeliu_specialistai.md) (`datasets/gov/ltsa/gelezinkeliu_specialistai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_specialistai/RailwaySpecialist` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `document_number`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `valid_to` | `datetime` | `D` | `4` | `open` | — | Teisė suteikta iki | — |
| `born` | `integer` | — | `2` | `open` | — | Gimimo metai | metai YY formatu |
| `valid_from` | `datetime` | `T` | `4` | `open` | — | Teisė galioja nuo | — |
| `document_number` | `string` | — | `2` | `open` | — | Dokumento numeris | — |
| `type` | `string` | — | `3` | `open` | — | Tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/gelezinkeliu_specialistai (https://data.gov.lt/datasets/2333/)
