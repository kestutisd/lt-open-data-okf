---
type: Table
title: "TollRoad — Mokamas kelias"
description: "Spinta table datasets/gov/lakd/mokamikeliai/TollRoad (5 columns)."
tags: [gov, lakd, tollroad, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/mokamikeliai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lakd/mokamikeliai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# TollRoad — Mokamas kelias

- **Model:** `datasets/gov/lakd/mokamikeliai/TollRoad`[^manifest]
- **Dataset:** [datasets/gov/lakd/mokamikeliai](../mokamikeliai.md) (`datasets/gov/lakd/mokamikeliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/mokamikeliai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/mokamikeliai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `objectid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geometry` | `geometry(multilinestring, 4326)` | `m` | `4` | `open` | — | Geometrija | — |
| `objectid` | `integer` | — | `4` | `open` | — | Identifikatorius | — |
| `kelionr` | `string` | — | `2` | `open` | — | Kelio numeris | — |
| `nuo` | `number` | `km` | `4` | `open` | — | Ruožo pradžia | — |
| `iki` | `number` | `km` | `4` | `open` | — | Ruožo pabaiga | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kelionr` | `create(property: "kelias", type: "ref", ref: "/datasets/gov/lakd/keliai/StateRoad[kelionr]")` | `type` | `4` | — | — | — | — |
| `kelionr` | `update(property: "kelias.kelionr", type: "")` | `property` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/mokamikeliai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/mokamikeliai.csv#L7)
