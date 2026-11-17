---
type: Table
title: "ObjectsFiles — Objektų failai"
description: "Spinta table datasets/gov/ivpk/registrai/ObjectsFiles (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectsFiles"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L115"
    last_modified: "2026-11-11T14:39:20Z"
---

# ObjectsFiles — Objektų failai

- **Model:** `datasets/gov/ivpk/registrai/ObjectsFiles`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L115](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L115)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectsFiles`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `type` | `string` | — | `2` | `open` | — | Tipas | — |
| `document_id` | `integer` | — | `2` | `open` | — | Dokumento ID | — |
| `file_name` | `string` | — | `3` | `open` | — | Failo pavadinimas | — |
| `file_type` | `string` | — | `4` | `open` | — | Failo tipas | — |
| `file_ext` | `string` | — | `4` | `open` | — | Failo plėtinys | — |
| `file_size` | `number` | — | `3` | `open` | — | Failo dydis | — |
| `update_time` | `datetime` | `S` | `4` | `open` | — | Atnaujinimo data | — |
| `add_time` | `datetime` | `S` | `4` | `open` | — | Pridėjimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'RegulationDocument'` | — | — | — | — |
| `type` | `'AcceptanceDocument'` | — | — | — | — |
| `type` | `'SpecificationDocument'` | — | — | — | — |
| `type` | `'LiquidationDocument'` | — | — | — | — |
| `type` | `'6'` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
