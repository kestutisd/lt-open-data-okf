---
type: Table
title: "Device"
description: "Spinta table datasets/gov/lakd/eismo_intensyvumas_live/Device (11 columns)."
tags: [gov, lakd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/eismo_intensyvumas_live.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Device

- **Model:** `datasets/gov/lakd/eismo_intensyvumas_live/Device`[^manifest]
- **Dataset:** [Eismo intensyvumo duomenų katalogas](../eismo_intensyvumas_live.md) (`datasets/gov/lakd/eismo_intensyvumas_live`)
- **Manifest CSV:** [datasets/gov/lakd/eismo_intensyvumas_live.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Įrenginio identifikacinis numeris | — |
| `name` | `string` | — | `3` | `open` | — | Įrenginio pavadinimas | — |
| `kelionr` | `string` | — | `2` | `open` | — | Kelio numeris | — |
| `pavadinim` | `string` | — | `2` | `open` | — | Kelio pavadinimas | — |
| `km` | `number` | `km` | `4` | `open` | — | Vieta, kilometras | — |
| `platuma` | `number` | — | `2` | `private` | — | Platuma, WGS-84 | — |
| `ilguma` | `number` | — | `2` | `private` | — | Ilguma, WGS-84 | — |
| `koordinates_wgs84` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Koordinates WGS-84 | — |
| `road_segment` | `ref` | [RoadSegment](RoadSegment.md) | `4` | `open` | — | Skaitiklio homogeninis ruožas | — |
| `time_interval` | `integer` | `min` | `4` | `open` | — | Duomenys per (min) | — |
| `date` | `temporal` | `T` | `5` | `open` | `dct:temporal` | Duomenų surinkimo data ir laikas | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |
| `dct` | `http://purl.org/dc/terms/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kelionr` | `create(property: "kelias", type: "ref", ref: "/datasets/gov/lakd/keliai/StateRoad[kelionr]")` | `type` | `4` | — | — | — | — |
| `kelionr` | `update(property: "kelias.kelionr", type: "")` | `property` | `4` | — | — | — | — |
| `pavadinim` | `update(property: "kelias.pavadinim", type: "")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/eismo_intensyvumas_live.csv
