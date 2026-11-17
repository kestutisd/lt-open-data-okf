---
type: Table
title: "TransportoPriemone"
description: "Spinta table datasets/gov/pd/eiis/TransportoPriemone (18 columns)."
tags: [gov, pd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pd/eiis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L187"
    last_modified: "2026-11-11T14:39:20Z"
---

# TransportoPriemone

- **Model:** `datasets/gov/pd/eiis/TransportoPriemone`[^manifest]
- **Dataset:** [datasets/gov/pd/eiis](../eiis.md) (`datasets/gov/pd/eiis`)
- **Manifest CSV:** [datasets/gov/pd/eiis.csv#L187](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L187)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `tpid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eismo_ivykis` | `ref` | [EismoIvykis](EismoIvykis.md) | `4` | — | — | — | — |
| `tpid` | `integer` | — | `4` | `open` | — | Transporto priemonės ID | — |
| `reg_valstybe` | `string` | — | `3` | `open` | — | Registracijos valstybė | — |
| `kategorija` | `ref` | [/datasets/gov/regitra/tp/TransportoPriemone[kategorija_pilnai]](../../regitra/tp/TransportoPriemone.md) | `2` | `open` | — | Kategorija | — |
| `klase` | `ref` | [/datasets/gov/regitra/tp/TransportoPriemone[kategorija_klase]](../../regitra/tp/TransportoPriemone.md) | `2` | `open` | — | Klasė | — |
| `marke` | `ref` | [/datasets/gov/regitra/tp/TransportoPriemone[marke]](../../regitra/tp/TransportoPriemone.md) | `4` | `open` | — | Markė | — |
| `modelis` | `ref` | [/datasets/gov/regitra/tp/TransportoPriemone[komercinis_pav]](../../regitra/tp/TransportoPriemone.md) | `4` | `open` | — | Modelis | — |
| `pagaminimo_metai` | `ref` | [/datasets/gov/regitra/tp/TransportoPriemone[gamybos_metai]](../../regitra/tp/TransportoPriemone.md) | `4` | `open` | — | Pagaminimo metai | — |
| `pasisalino` | `string` | — | `3` | `open` | — | Pasišalino | — |
| `ypatumai` | `string` | — | `3` | `open` | — | Ypatumai | — |
| `apgadinimai` | `string` | — | `3` | `open` | — | Apgadinimai | — |
| `apdraustas_civilines` | `integer` | — | `4` | `open` | — | Apdraustas civiliniu draudimu | — |
| `apdraustas_kasko` | `integer` | — | `4` | `open` | — | Apdraustas kasko | — |
| `apgadinimai_kita` | `string` | — | `3` | `open` | — | Kiti apgadinimai | — |
| `fizinis` | `string` | — | `4` | `open` | — | Fizinis asmuo | — |
| `dalyvauti_vt_uzdrausta` | `string` | — | `4` | `open` | — | Dalyvauti eisme uždrausta | — |
| `nuliamiantys_gedimai[]` | `string` | — | `3` | `open` | — | Nuliamentis gedimas | — |
| `pirminiai_smugiai[]` | `string` | — | `3` | `open` | — | Pirminis smūgis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `apdraustas_civilines` | `true` | `1` | — | Taip | — |
| `apdraustas_civilines` | `false` | `0` | — | Ne | — |
| `apdraustas_kasko` | `true` | `1` | — | Taip | — |
| `apdraustas_kasko` | `false` | `0` | — | Ne | — |
| `fizinis` | `"Ne"` | — | — | Ne | — |
| `fizinis` | `"Taip"` | — | — | Taip | — |
| `dalyvauti_vt_uzdrausta` | `"Ne"` | — | — | Ne | — |
| `dalyvauti_vt_uzdrausta` | `"Taip"` | — | — | Taip | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/eiis.csv
