---
type: Table
title: "TrafficRestrictionService"
description: "Spinta table datasets/gov/lakd/eismo_apribojimai_live/TrafficRestrictionService (19 columns)."
tags: [gov, lakd, trafficrestrictionservice, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_apribojimai_live.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lakd/eismo_apribojimai_live.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# TrafficRestrictionService

- **Model:** `datasets/gov/lakd/eismo_apribojimai_live/TrafficRestrictionService`[^manifest]
- **Dataset:** [Eismo ribojimų duomenų katalogas](../eismo_apribojimai_live.md) (`datasets/gov/lakd/eismo_apribojimai_live`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/eismo_apribojimai_live.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_apribojimai_live.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`[^manifest]

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
| `restrictions` | `ref` | [Restriction](Restriction.md) (`level=4 UUID`: `restrictions._id`) | `4` | `open` | — | Apribojimo duomenys | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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
| `dct` | `http://purl.org/dc/terms/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/eismo_apribojimai_live.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_apribojimai_live.csv#L7)
