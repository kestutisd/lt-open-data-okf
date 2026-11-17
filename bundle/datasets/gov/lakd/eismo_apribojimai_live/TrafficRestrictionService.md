---
type: Table
title: "TrafficRestrictionService"
description: "Spinta table datasets/gov/lakd/eismo_apribojimai_live/TrafficRestrictionService (19 columns)."
tags: [gov, lakd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/eismo_apribojimai_live.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_apribojimai_live.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# TrafficRestrictionService

- **Model:** `datasets/gov/lakd/eismo_apribojimai_live/TrafficRestrictionService`[^manifest]
- **Dataset:** [Eismo ribojimų duomenų katalogas](../eismo_apribojimai_live.md) (`datasets/gov/lakd/eismo_apribojimai_live`)
- **Manifest CSV:** [datasets/gov/lakd/eismo_apribojimai_live.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_apribojimai_live.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikacinis numeris | — |
| `type` | `string` | — | `4` | `open` | — | Apribojimo tipas | — |
| `creationtime` | `temporal` | `T` | `5` | `open` | `dct:temporal` | Įrašo sukūrimo data | — |
| `updatetime` | `datetime` | `S` | `4` | `open` | — | Įrašo atnaujinimo data | — |
| `starttime` | `datetime` | `S` | `4` | `open` | — | Apribojimo pradžia | — |
| `endtime` | `datetime` | `S` | `4` | `open` | — | Apribojimo pabaiga | — |
| `description` | `string` | — | `3` | `open` | — | Ilgas aprašas | — |
| `short_description` | `string` | — | `3` | `open` | — | Trumpas aprašas | — |
| `schedule` | `string` | — | `3` | `open` | — | Datų sąrašas | — |
| `location_polyline` | `geometry(linestring,4326)` | `m` | `4` | `open` | — | Vieta kelyje – linijos koordinatės | — |
| `location_direction` | `string` | — | `4` | `open` | — | Vieta kelyje – kelio kryptis | — |
| `location_street` | `string` | — | `3` | `open` | — | Vieta kelyje – kelio ar gatvės pavadinimas | — |
| `location_location_description` | `string` | — | `3` | `open` | — | Vieta kelyje – vietos aprašas | — |
| `source_reference` | `string` | — | `3` | `open` | — | Informacijos šaltinis – trumpas pavadinimas | — |
| `source_name` | `string` | — | `3` | `open` | — | Informacijos šaltinis – pilnas pavadinimas | — |
| `source_url` | `string` | — | `3` | `open` | — | Informacijos šaltinis - internetinis adresas | — |
| `parent_event` | `string` | — | `3` | `open` | — | Pagrindinio renginio pavadinimas | — |
| `subtype` | `string` | — | `4` | `open` | — | Renginio tipas | — |
| `restrictions` | `ref` | [Restriction](Restriction.md) | `4` | `open` | — | Apribojimo duomenys | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `"HAZARD"` | — | — | Pavojus | — |
| `type` | `"CONSTRUCTION"` | — | — | Remontas | — |
| `type` | `"ACCIDENT"` | — | — | Nelaimingas įvykis | — |
| `location_direction` | `"BOTH_DIRECTIONS"` | — | — | Abi kryptys | — |
| `location_direction` | `"ONE_DIRECTION"` | — | — | Viena kryptis | — |
| `subtype` | `"weakBridge"` | — | — | Silpnas tiltas | — |
| `subtype` | `"flooding"` | — | — | Potvyniai | — |
| `subtype` | `"roadworks"` | — | — | Kelio darbai | — |
| `subtype` | `"repairWork"` | — | — | Kelio remontas | — |
| `subtype` | `"damagedRoadSurface"` | — | — | Pažeista kelio danga | — |
| `subtype` | `"motorSportRaceMeeting"` | — | — | Automobilių lenktynės | — |
| `subtype` | `"sportsMeeting"` | — | — | Sporto renginys | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/eismo_apribojimai_live.csv
