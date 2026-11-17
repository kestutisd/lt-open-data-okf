---
type: Table
title: "PrieziurosSamata"
description: "Spinta table datasets/gov/lakd/keliuprieziura/PrieziurosSamata (3 columns)."
tags: [gov, lakd, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliuprieziura.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuprieziura.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrieziurosSamata

- **Model:** `datasets/gov/lakd/keliuprieziura/PrieziurosSamata`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliuprieziura](../keliuprieziura.md) (`datasets/gov/lakd/keliuprieziura`)
- **Manifest CSV:** [datasets/gov/lakd/keliuprieziura.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliuprieziura.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `paskirtis`
- **Level:** `2`
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe[pavadinimas]](../../rc/ar/savivaldybe/Savivaldybe.md) | `2` | `open` | — | Savivaldybė | — |
| `paskirtis` | `string` | — | `3` | `open` | — | Finansavimo lėšų paskirtis | — |
| `suma` | `number` | — | `2` | `open` | — | Paskirtų lėšų suma | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliuprieziura.csv
