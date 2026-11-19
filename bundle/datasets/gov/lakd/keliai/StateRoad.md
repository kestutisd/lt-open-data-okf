---
type: Table
title: "StateRoad — Kelias"
description: "Spinta table datasets/gov/lakd/keliai/StateRoad (8 columns)."
tags: [gov, lakd, stateroad, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# StateRoad — Kelias

- **Model:** `datasets/gov/lakd/keliai/StateRoad`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliai](../keliai.md) (`datasets/gov/lakd/keliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/keliai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `objectid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geometry` | `geometry(linestring,4326)` | `m` | `4` | `open` | — | Geometrija | — |
| `objectid` | `integer` | — | `4` | `open` | — | Identifikatorius | — |
| `kelionr` | `string` | — | `4` | `open` | — | Kelio numeris | — |
| `pradziakm` | `number` | `km` | `4` | `open` | — | Ruožo pradžia | — |
| `pabaigakm` | `number` | `km` | `4` | `open` | — | Ruožo pabaiga | — |
| `vazdalis` | `integer` | — | `4` | `open` | — | Važiuojamoji dalis | — |
| `pavadinim` | `string` | — | `4` | `open` | — | Kelio pavadinimas | — |
| `kryptis` | `string` | — | `2` | `open` | — | Kelio kryptis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vazdalis` | `0` | — | — | Viena važiuojamoji dalis | — |
| `vazdalis` | `1` | — | — | Pirma važiuojamoji dalis | — |
| `vazdalis` | `2` | — | — | Antra važiuojamoji dalis | — |
| `kryptis` | `"AB"` | — | — | AB | — |
| `kryptis` | `"AT"` | — | — | AT | — |
| `kryptis` | `"PR"` | — | — | PR | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliai.csv#L4)
