---
type: Table
title: "RoadLicence — Kelių transporto veiklos licencijos"
description: "Spinta table datasets/gov/ltsa/keliu_licencijos/RoadLicence (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/keliu_licencijos/RoadLicence"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/keliu_licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_licencijos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# RoadLicence — Kelių transporto veiklos licencijos

- **Model:** `datasets/gov/ltsa/keliu_licencijos/RoadLicence`[^manifest]
- **Dataset:** [Kelių transporto veiklos licencijos](../keliu_licencijos.md) (`datasets/gov/ltsa/keliu_licencijos`)
- **Manifest CSV:** [datasets/gov/ltsa/keliu_licencijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_licencijos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/keliu_licencijos/RoadLicence`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `valid` | `string` | — | `2` | `open` | — | Galiojimo būklė | — |
| `valid_to` | `datetime` | `D` | `4` | `open` | — | Galioja iki | — |
| `id` | `integer` | — | `4` | `open` | — | Licencijos ID | — |
| `valid_from` | `datetime` | `D` | `4` | `open` | — | Galioja nuo | — |
| `number` | `string` | — | `2` | `open` | — | Licencijos numeris | — |
| `type` | `string` | — | `2` | `open` | — | Licencijos tipas | — |
| `company` | `string` | — | `2` | `open` | — | Vežėjas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/keliu_licencijos.csv
