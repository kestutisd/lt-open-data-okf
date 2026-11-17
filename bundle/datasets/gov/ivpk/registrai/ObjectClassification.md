---
type: Table
title: "ObjectClassification — Objekto klasifikacija"
description: "Spinta table datasets/gov/ivpk/registrai/ObjectClassification (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectClassification"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L108"
    last_modified: "2026-11-11T14:39:20Z"
---

# ObjectClassification — Objekto klasifikacija

- **Model:** `datasets/gov/ivpk/registrai/ObjectClassification`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L108](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L108)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectClassification`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `object` | `ref` | [Object](Object.md) | `4` | `open` | — | Objektas | — |
| `objects_interaction` | `integer` | — | `1` | `open` | — | Objekto sąveika | — |
| `name` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `type` | `integer` | — | `1` | `open` | — | Klasifikacijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
