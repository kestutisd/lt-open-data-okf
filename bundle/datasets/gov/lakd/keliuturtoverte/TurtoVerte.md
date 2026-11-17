---
type: Table
title: "TurtoVerte"
description: "Spinta table datasets/gov/lakd/keliuturtoverte/TurtoVerte (2 columns)."
tags: [gov, lakd, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliuturtoverte.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuturtoverte.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TurtoVerte

- **Model:** `datasets/gov/lakd/keliuturtoverte/TurtoVerte`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliuturtoverte](../keliuturtoverte.md) (`datasets/gov/lakd/keliuturtoverte`)
- **Manifest CSV:** [datasets/gov/lakd/keliuturtoverte.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuturtoverte.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `kelias_tipas`
- **Level:** `3`
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kelias_tipas` | `string` | — | `3` | `open` | — | Kelių reikšmė | — |
| `likutine_verte` | `integer` | — | `2` | `open` | — | Likutinė vertė 2021m mln. Eur | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `likutine_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliuturtoverte.csv
