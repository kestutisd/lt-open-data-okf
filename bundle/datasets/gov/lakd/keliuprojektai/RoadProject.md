---
type: Table
title: "RoadProject — Kelio projektas"
description: "Spinta table datasets/gov/lakd/keliuprojektai/RoadProject (15 columns)."
tags: [gov, lakd, roadproject, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuprojektai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliuprojektai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# RoadProject — Kelio projektas

- **Model:** `datasets/gov/lakd/keliuprojektai/RoadProject`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliuprojektai](../keliuprojektai.md) (`datasets/gov/lakd/keliuprojektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/keliuprojektai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuprojektai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `geometry` | `geometry(multilinestring,4326)` | `m` | `4` | `open` | — | Geometrija | — |
| `objectid` | `integer` | — | `4` | `open` | — | Identifikatorius | — |
| `kelionr` | `string` | — | `2` | `open` | — | Kelio numeris | — |
| `pradziakm` | `number` | `km` | `4` | `open` | — | Ruožo pradžia | — |
| `pabaigakm` | `number` | `km` | `4` | `open` | — | Ruožo pabaiga | — |
| `objektas_pavad` | `string` | — | `3` | `open` | — | Objekto pavadinimas | — |
| `sutartiesnr` | `string` | — | `4` | `open` | — | Sutarties Nr. | — |
| `sutartiespradzia` | `date` | — | `2` | `open` | — | Sutarties pradžia | — |
| `sutartiespabaiga` | `date` | — | `2` | `open` | — | Sutarties pabaiga | — |
| `genrangovas_pavad` | `string` | — | `2` | `open` | — | Rangovas | — |
| `importodata` | `date` | — | `2` | `open` | — | Duomenų įkėlimo data | — |
| `darbotipas` | `string` | — | `3` | `open` | — | Darbo tipas | — |
| `kaina` | `number` | — | `3` | `open` | — | Kaina | — |
| `suma` | `number` | — | `3` | `open` | — | Suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kelionr` | `create(property: "kelias", type: "ref", ref: "/datasets/gov/lakd/keliai/StateRoad[kelionr]")` | `property` | `4` | `open` | — | — | — |
| `kelionr` | `update(property: "kelias.kelionr", type: "")` | `property` | `4` | — | — | — | — |
| `genrangovas_pavad` | `create(property: "rangovas", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]")` | `property` | `2` | `open` | — | — | — |
| `genrangovas_pavad` | `update(property: "rangovas.ja_pavadinimas", type: "")` | `property` | `2` | — | — | — | — |
| `kaina` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliuprojektai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuprojektai.csv#L7)
