---
type: Table
title: "NoiseReductionPanel — Akustinė sienelė"
description: "Spinta table datasets/gov/lakd/aplinkosauga/NoiseReductionPanel (11 columns)."
tags: [gov, lakd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/aplinkosauga.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/aplinkosauga.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# NoiseReductionPanel — Akustinė sienelė

- **Model:** `datasets/gov/lakd/aplinkosauga/NoiseReductionPanel`[^manifest]
- **Dataset:** [datasets/gov/lakd/aplinkosauga](../aplinkosauga.md) (`datasets/gov/lakd/aplinkosauga`)
- **Manifest CSV:** [datasets/gov/lakd/aplinkosauga.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/aplinkosauga.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `objectid`
- **Level:** `4`
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto identifikatorius | — |
| `eo_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės erdvinių duomenų rinkinio specifikacijos kodas | — |
| `kelionr` | `string` | — | `2` | `open` | — | Kelio numeris | — |
| `pr_km` | `number` | `km` | `4` | `open` | — | Akustinės sienelės pradžios taškas nustatomas projekcijoje į kelią | — |
| `pab_km` | `number` | `km` | `4` | `open` | — | Akustinės sienelės pabaigos taškas nustatomas projekcijoje į kelią | — |
| `vaz_dal` | `integer` | — | `4` | `open` | — | Važiuojamoji dalis | — |
| `kelio_puse` | `integer` | — | `4` | `open` | — | Kelio pusė | — |
| `akustsientipas` | `integer` | — | `4` | `open` | — | Akustinės sienelės tipas | — |
| `aukstis` | `number` | `m` | `4` | `open` | — | Aukštis | — |
| `ilgis` | `number` | `m` | `4` | `open` | — | Ilgis | — |
| `shape` | `geometry(linestring, 4326)` | `m` | `4` | `open` | — | Geometrija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vaz_dal` | `0` | — | — | Viena važiuojamoji dalis | — |
| `vaz_dal` | `1` | — | — | Pirma važiuojamoji dalis | — |
| `vaz_dal` | `2` | — | — | Antra važiuojamoji dalis | — |
| `kelio_puse` | `1` | — | — | Kairėje šalia kelio | — |
| `kelio_puse` | `2` | — | — | Dešinėje šalia kelio | — |
| `kelio_puse` | `25` | — | — | Kairėje | — |
| `kelio_puse` | `26` | — | — | Dešinėje | — |
| `akustsientipas` | `1` | — | — | Absorbuojanti | — |
| `akustsientipas` | `2` | — | — | Garsą atspindinti | — |
| `akustsientipas` | `3` | — | — | Mišri | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kelionr` | `create(property: "kelias", type: "ref", ref: "/datasets/gov/lakd/keliai/StateRoad[kelionr]")` | `property` | `4` | `open` | — | — | — |
| `kelionr` | `update(property: "kelias.kelionr", type: "")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/aplinkosauga.csv
