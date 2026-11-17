---
type: Table
title: "CustomsOfficeNationalRole"
description: "Spinta table datasets/gov/muitine/muitines_funkcijos/CustomsOfficeNationalRole (6 columns)."
tags: [gov, muitine, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_funkcijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_funkcijos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# CustomsOfficeNationalRole

- **Model:** `datasets/gov/muitine/muitines_funkcijos/CustomsOfficeNationalRole`[^manifest]
- **Dataset:** [datasets/gov/muitine/muitines_funkcijos](../muitines_funkcijos.md) (`datasets/gov/muitine/muitines_funkcijos`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_funkcijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_funkcijos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `code`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `3` | `open` | — | Funkcijos kodas | 3 simbolių kodas |
| `national` | `boolean` | — | `3` | `open` | — | Nacionalinis požymis | — |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžios data | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaigos data | — |
| `description_lt` | `string` | — | `2` | `open` | — | Aprašymas (LT) | — |
| `description_en` | `string` | — | `2` | `open` | — | Aprašymas (EN) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `description_lt` | `update(property: "description@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `description_en` | `update(property: "description@en", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_funkcijos.csv
