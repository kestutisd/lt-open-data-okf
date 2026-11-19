---
type: Table
title: "RoadObject — Vykdomi objektai"
description: "Spinta table datasets/gov/lakd/vykdomiobjektai/RoadObject (13 columns)."
tags: [gov, lakd, roadobject, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/vykdomiobjektai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lakd/vykdomiobjektai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# RoadObject — Vykdomi objektai

- **Model:** `datasets/gov/lakd/vykdomiobjektai/RoadObject`[^manifest]
- **Dataset:** [datasets/gov/lakd/vykdomiobjektai](../vykdomiobjektai.md) (`datasets/gov/lakd/vykdomiobjektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/vykdomiobjektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/vykdomiobjektai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `objectid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geometry` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Geometrija | — |
| `objectid` | `integer` | — | `4` | `open` | — | Identifikatorius | — |
| `kelionr` | `ref` | [StateRoad](../keliai/StateRoad.md) (`level=4 UUID` via `StateRoad[kelionr]`: `kelionr._id`) | `4` | `open` | — | Kelio numeris | — |
| `keliasvieta` | `number` | `km` | `4` | `open` | — | Vieta kelyje | — |
| `objektas_pavad` | `string` | — | `3` | `open` | — | Objekto pavadinimas | — |
| `sutartiesnr` | `string` | — | `4` | `open` | — | Sutarties Nr. | — |
| `sutartiespradzia` | `date` | — | `2` | `open` | — | Sutarties pradžia | — |
| `sutartiespabaiga` | `date` | — | `2` | `open` | — | Sutarties pabaiga | — |
| `rangovas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `rangovas._id`) | `4` | `open` | — | Rangovas | — |
| `importodata` | `date` | — | `2` | `open` | — | Duomenų įkėlimo data | — |
| `darbotipas` | `string` | — | `3` | `open` | — | Darbo tipas | — |
| `kaina` | `number` | — | `3` | `open` | — | Kaina | — |
| `suma` | `number` | — | `3` | `open` | — | Suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kaina` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/vykdomiobjektai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/vykdomiobjektai.csv#L6)
