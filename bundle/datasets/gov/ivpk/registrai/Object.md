---
type: Table
title: "Object — Registras/Informacinė sistema"
description: "Spinta table datasets/gov/ivpk/registrai/Object (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/Object"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L89"
    last_modified: "2026-11-11T14:39:20Z"
---

# Object — Registras/Informacinė sistema

- **Model:** `datasets/gov/ivpk/registrai/Object`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L89](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L89)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/Object`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `1` | `open` | — | — | — |
| `type` | `string` | `object_type` | `3` | `open` | — | Registro tipas | — |
| `name` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `object_no` | `string` | — | `4` | `open` | — | Objekto numeris | — |
| `registration_date` | `date` | `D` | `4` | `open` | — | Registracijos data | — |
| `commencement_date` | `string` | — | `2` | `open` | — | Pradžios data | — |
| `registry_objects` | `string` | — | `2` | `open` | — | — | — |
| `cacelation_date` | `date` | `D` | `4` | `open` | — | Nutraukimo data | — |
| `updated_at` | `datetime` | `S` | `4` | `open` | — | Duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'rs'` | — | — | Registras | — |
| `type` | `'vis'` | — | — | Valstybės informacinės sistema | — |
| `type` | `'both'` | — | — | Registras ir Valstybės informacinė sistema | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
