---
type: Table
title: "TransportoPriemone"
description: "Spinta table datasets/gov/pd/eiis/TransportoPriemone (18 columns)."
tags: [gov, pd, transportopriemone, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L187"
    title: "atviriduomenys/manifest — datasets/gov/pd/eiis.csv#L187"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# TransportoPriemone

- **Model:** `datasets/gov/pd/eiis/TransportoPriemone`[^manifest]
- **Dataset:** [datasets/gov/pd/eiis](../eiis.md) (`datasets/gov/pd/eiis`)[^manifest]
- **Manifest CSV:** [datasets/gov/pd/eiis.csv#L187](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L187)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pd` — Policijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `tpid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eismo_ivykis` | `ref` | [EismoIvykis](EismoIvykis.md) (`level=4 UUID`: `eismo_ivykis._id`) | `4` | — | — | — | — |
| `tpid` | `integer` | — | `4` | `open` | — | Transporto priemonės ID | — |
| `reg_valstybe` | `string` | — | `3` | `open` | — | Registracijos valstybė | — |
| `kategorija` | `ref` | [TransportoPriemone](../../regitra/tp/TransportoPriemone.md) (`level=2` scalar) | `2` | `open` | — | Kategorija | — |
| `klase` | `ref` | [TransportoPriemone](../../regitra/tp/TransportoPriemone.md) (`level=2` scalar) | `2` | `open` | — | Klasė | — |
| `marke` | `ref` | [TransportoPriemone](../../regitra/tp/TransportoPriemone.md) (`level=4 UUID` via `TransportoPriemone[marke]`: `marke._id`) | `4` | `open` | — | Markė | — |
| `modelis` | `ref` | [TransportoPriemone](../../regitra/tp/TransportoPriemone.md) (`level=4 UUID` via `TransportoPriemone[komercinis_pav]`: `modelis._id`) | `4` | `open` | — | Modelis | — |
| `pagaminimo_metai` | `ref` | [TransportoPriemone](../../regitra/tp/TransportoPriemone.md) (`level=4 UUID` via `TransportoPriemone[gamybos_metai]`: `pagaminimo_metai._id`) | `4` | `open` | — | Pagaminimo metai | — |
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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `apdraustas_civilines` | `true` | `1` | — | Taip | — |
| `apdraustas_civilines` | `false` | `0` | — | Ne | — |
| `apdraustas_kasko` | `true` | `1` | — | Taip | — |
| `apdraustas_kasko` | `false` | `0` | — | Ne | — |
| `fizinis` | `"Ne"` | — | — | Ne | — |
| `fizinis` | `"Taip"` | — | — | Taip | — |
| `dalyvauti_vt_uzdrausta` | `"Ne"` | — | — | Ne | — |
| `dalyvauti_vt_uzdrausta` | `"Taip"` | — | — | Taip | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/eiis.csv#L187 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L187)
