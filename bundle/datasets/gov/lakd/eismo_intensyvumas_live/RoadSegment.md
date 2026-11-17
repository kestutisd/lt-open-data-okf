---
type: Table
title: "RoadSegment"
description: "Spinta table datasets/gov/lakd/eismo_intensyvumas_live/RoadSegment (13 columns)."
tags: [gov, lakd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/eismo_intensyvumas_live.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L23"
    last_modified: "2026-11-11T14:39:20Z"
---

# RoadSegment

- **Model:** `datasets/gov/lakd/eismo_intensyvumas_live/RoadSegment`[^manifest]
- **Dataset:** [Eismo intensyvumo duomenų katalogas](../eismo_intensyvumas_live.md) (`datasets/gov/lakd/eismo_intensyvumas_live`)
- **Manifest CSV:** [datasets/gov/lakd/eismo_intensyvumas_live.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L23)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `start_x`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `device` | `ref` | [Device](Device.md) | `4` | `open` | — | — | — |
| `direction` | `string` | — | `4` | `open` | — | Kryptis | — |
| `start_x` | `number` | — | `2` | `private` | — | Ruožo pradžios X taškas, LKS-94 | — |
| `start_y` | `number` | — | `2` | `private` | — | Ruožo pradžios Y taškas, LKS-94 | — |
| `pradzios_koordinates_lks94` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Pradžios koordinatės LKS-94 | — |
| `end_x` | `number` | — | `2` | `private` | — | Ruožo pabaigos X taškas, LKS-94 | — |
| `end_y` | `number` | — | `2` | `private` | — | Ruožo pabaigos Y taškas, LKS-94 | — |
| `pabaigos_koordinates_lks94` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Pabaigos koordinatės LKS-94 | — |
| `winter_speed` | `integer` | `km/h` | `4` | `open` | — | Greičio režimas žiemą | — |
| `summer_speed` | `integer` | `km/h` | `4` | `open` | — | Greičio režimas vasarą | — |
| `number_of_vehicles` | `integer` | — | `3` | `open` | — | Užfiksuotų automobilių kiekis per laiko intervalą | — |
| `average_speed` | `number` | `km/h` | `4` | `open` | — | Užfiksuotas vidutinis greitis | — |
| `traffic_type` | `string` | — | `4` | `open` | — | Eismo įvertinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `direction` | `"positive"` | — | — | Kryptis pirmyn | — |
| `direction` | `"negative"` | — | — | Kryptis atgal | — |
| `traffic_type` | `"normal"` | — | — | Normalus eismas | — |
| `traffic_type` | `"slow"` | — | — | Lėtas eismas | — |
| `traffic_type` | `"high"` | — | — | Intensyvus eismas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/eismo_intensyvumas_live.csv
