---
type: Table
title: "TurtoVerte"
description: "Spinta table datasets/gov/lakd/keliuturtoverte/TurtoVerte (2 columns)."
tags: [gov, lakd, turtoverte, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuturtoverte.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliuturtoverte.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# TurtoVerte

- **Model:** `datasets/gov/lakd/keliuturtoverte/TurtoVerte`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliuturtoverte](../keliuturtoverte.md) (`datasets/gov/lakd/keliuturtoverte`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/keliuturtoverte.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuturtoverte.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kelias_tipas`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kelias_tipas` | `string` | — | `3` | `open` | — | Kelių reikšmė | — |
| `likutine_verte` | `integer` | — | `2` | `open` | — | Likutinė vertė 2021m mln. Eur | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `likutine_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliuturtoverte.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuturtoverte.csv#L6)
