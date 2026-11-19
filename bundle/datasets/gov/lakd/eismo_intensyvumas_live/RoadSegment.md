---
type: Table
title: "RoadSegment"
description: "Spinta table datasets/gov/lakd/eismo_intensyvumas_live/RoadSegment (13 columns)."
tags: [gov, lakd, roadsegment, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L23"
    title: "atviriduomenys/manifest — datasets/gov/lakd/eismo_intensyvumas_live.csv#L23"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# RoadSegment

- **Model:** `datasets/gov/lakd/eismo_intensyvumas_live/RoadSegment`[^manifest]
- **Dataset:** [Eismo intensyvumo duomenų katalogas](../eismo_intensyvumas_live.md) (`datasets/gov/lakd/eismo_intensyvumas_live`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/eismo_intensyvumas_live.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L23)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `start_x`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `device` | `ref` | [Device](Device.md) (`level=4 UUID`: `device._id`) | `4` | `open` | — | — | — |
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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `direction` | `"positive"` | — | — | Kryptis pirmyn | — |
| `direction` | `"negative"` | — | — | Kryptis atgal | — |
| `traffic_type` | `"normal"` | — | — | Normalus eismas | — |
| `traffic_type` | `"slow"` | — | — | Lėtas eismas | — |
| `traffic_type` | `"high"` | — | — | Intensyvus eismas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/eismo_intensyvumas_live.csv#L23 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L23)
