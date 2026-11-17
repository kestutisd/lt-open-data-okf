---
type: Table
title: "PkDalyvis"
description: "Spinta table datasets/gov/vsdfv/pkdalyviai/PkDalyvis (5 columns)."
tags: [gov, vsdfv, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PkDalyvis

- **Model:** `datasets/gov/vsdfv/pkdalyviai/PkDalyvis`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/pkdalyviai](../pkdalyviai.md) (`datasets/gov/vsdfv/pkdalyviai`)
- **Manifest CSV:** [datasets/gov/vsdfv/pkdalyviai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `metai, menuo`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amzius` | `string` | — | `3` | `open` | — | Amžiaus grupė | — |
| `dalyviu_skaicius` | `integer` | — | `4` | `open` | — | Dalyvių skaičius, vnt. | Iš viso pensijų kaupimo dalyvių skaičius |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"vyrai"` | — | — | Vyrai | — |
| `lytis` | `"moterys"` | — | — | Moterys | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv
