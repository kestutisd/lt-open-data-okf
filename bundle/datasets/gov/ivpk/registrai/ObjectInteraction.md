---
type: Table
title: "ObjectInteraction — Sąveika su objektais"
description: "Spinta table datasets/gov/ivpk/registrai/ObjectInteraction (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectInteraction"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L151"
    last_modified: "2026-11-11T14:39:20Z"
---

# ObjectInteraction — Sąveika su objektais

- **Model:** `datasets/gov/ivpk/registrai/ObjectInteraction`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L151](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L151)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectInteraction`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `type` | `string` | — | `4` | `open` | — | Tipas | — |
| `object` | `ref` | [Object](Object.md) | `4` | `open` | — | Objektas | — |
| `interaction_object` | `ref` | [Object](Object.md) | `4` | `open` | — | Sąveika su objektu | — |
| `updated_at` | `datetime` | `S` | `4` | `open` | — | Atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'S'` | — | — | Teikia duomenis | — |
| `type` | `'G'` | — | — | Gauna duomenis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
