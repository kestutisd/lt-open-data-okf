---
type: Table
title: "Institution — Institucijų sąrašas"
description: "Spinta table datasets/gov/ivpk/registrai/Institution (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/Institution"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L43"
    last_modified: "2026-11-11T14:39:20Z"
---

# Institution — Institucijų sąrašas

- **Model:** `datasets/gov/ivpk/registrai/Institution`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L43](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L43)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/Institution`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `is_jar_update_needed` | `boolean` | — | `4` | `open` | — | Ar JAR atnaujinimas reikalingas | — |
| `type` | `string` | `object_type` | `3` | `open` | — | Tipas | — |
| `name` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `ordering` | `string` | — | `4` | `open` | — | — | — |
| `code` | `string` | — | `4` | `open` | — | Kodas | — |
| `address` | `string` | — | `2` | `open` | — | Adresas | — |
| `url` | `string` | — | `4` | `open` | — | Svetainės adresas | — |
| `phone` | `string` | — | `2` | `open` | — | Telefonas | — |
| `fax` | `string` | — | `2` | `open` | — | Faksas | — |
| `email` | `string` | — | `4` | `open` | — | El. pašto adresas | — |
| `is_classified` | `boolean` | — | `4` | `open` | — | — | — |
| `group` | `string` | — | `1` | `open` | — | Institucijų grupė | — |
| `updated_at` | `string` | — | `2` | `open` | — | Atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'rs'` | — | — | Registras | — |
| `type` | `'vis'` | — | — | Valstybės informacinės sistema | — |
| `type` | `'both'` | — | — | Registras ir Valstybės informacinė sistema | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
