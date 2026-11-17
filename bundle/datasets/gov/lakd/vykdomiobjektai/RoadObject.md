---
type: Table
title: "RoadObject — Vykdomi objektai"
description: "Spinta table datasets/gov/lakd/vykdomiobjektai/RoadObject (13 columns)."
tags: [gov, lakd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/vykdomiobjektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/vykdomiobjektai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# RoadObject — Vykdomi objektai

- **Model:** `datasets/gov/lakd/vykdomiobjektai/RoadObject`[^manifest]
- **Dataset:** [datasets/gov/lakd/vykdomiobjektai](../vykdomiobjektai.md) (`datasets/gov/lakd/vykdomiobjektai`)
- **Manifest CSV:** [datasets/gov/lakd/vykdomiobjektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/vykdomiobjektai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `objectid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geometry` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Geometrija | — |
| `objectid` | `integer` | — | `4` | `open` | — | Identifikatorius | — |
| `kelionr` | `ref` | [/datasets/gov/lakd/keliai/StateRoad[kelionr]](../keliai/StateRoad.md) | `4` | `open` | — | Kelio numeris | — |
| `keliasvieta` | `number` | `km` | `4` | `open` | — | Vieta kelyje | — |
| `objektas_pavad` | `string` | — | `3` | `open` | — | Objekto pavadinimas | — |
| `sutartiesnr` | `string` | — | `4` | `open` | — | Sutarties Nr. | — |
| `sutartiespradzia` | `date` | — | `2` | `open` | — | Sutarties pradžia | — |
| `sutartiespabaiga` | `date` | — | `2` | `open` | — | Sutarties pabaiga | — |
| `rangovas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Rangovas | — |
| `importodata` | `date` | — | `2` | `open` | — | Duomenų įkėlimo data | — |
| `darbotipas` | `string` | — | `3` | `open` | — | Darbo tipas | — |
| `kaina` | `number` | — | `3` | `open` | — | Kaina | — |
| `suma` | `number` | — | `3` | `open` | — | Suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kaina` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/vykdomiobjektai.csv
