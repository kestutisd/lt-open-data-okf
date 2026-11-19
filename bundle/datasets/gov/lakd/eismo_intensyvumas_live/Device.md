---
type: Table
title: "Device"
description: "Spinta table datasets/gov/lakd/eismo_intensyvumas_live/Device (11 columns)."
tags: [gov, lakd, device, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lakd/eismo_intensyvumas_live.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Device

- **Model:** `datasets/gov/lakd/eismo_intensyvumas_live/Device`[^manifest]
- **Dataset:** [Eismo intensyvumo duomenų katalogas](../eismo_intensyvumas_live.md) (`datasets/gov/lakd/eismo_intensyvumas_live`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/eismo_intensyvumas_live.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`[^manifest]

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
| `road_segment` | `ref` | [RoadSegment](RoadSegment.md) (`level=4 UUID`: `road_segment._id`) | `4` | `open` | — | Skaitiklio homogeninis ruožas | — |
| `time_interval` | `integer` | `min` | `4` | `open` | — | Duomenys per (min) | — |
| `date` | `temporal` | `T` | `5` | `open` | `dct:temporal` | Duomenų surinkimo data ir laikas | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kelionr` | `create(property: "kelias", type: "ref", ref: "/datasets/gov/lakd/keliai/StateRoad[kelionr]")` | `type` | `4` | — | — | — | — |
| `kelionr` | `update(property: "kelias.kelionr", type: "")` | `property` | `4` | — | — | — | — |
| `pavadinim` | `update(property: "kelias.pavadinim", type: "")` | `property` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/eismo_intensyvumas_live.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_intensyvumas_live.csv#L7)
