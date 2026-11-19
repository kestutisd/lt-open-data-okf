---
type: Table
title: "RoadLicence — Kelių transporto veiklos licencijos"
description: "Spinta table datasets/gov/ltsa/keliu_licencijos/RoadLicence (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/keliu_licencijos/RoadLicence"
tags: [gov, ltsa, roadlicence, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_licencijos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/keliu_licencijos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2335/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/keliu_licencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# RoadLicence — Kelių transporto veiklos licencijos

- **Model:** `datasets/gov/ltsa/keliu_licencijos/RoadLicence`[^manifest]
- **Dataset:** [Kelių transporto veiklos licencijos](../keliu_licencijos.md) (`datasets/gov/ltsa/keliu_licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/keliu_licencijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_licencijos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/keliu_licencijos/RoadLicence` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/keliu_licencijos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_licencijos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/keliu_licencijos (https://data.gov.lt/datasets/2335/)
