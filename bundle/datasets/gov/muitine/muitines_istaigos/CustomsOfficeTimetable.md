---
type: Table
title: "CustomsOfficeTimetable"
description: "Spinta table datasets/gov/muitine/muitines_istaigos/CustomsOfficeTimetable (6 columns)."
tags: [gov, muitine, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L57"
    last_modified: "2026-11-11T14:39:20Z"
---

# CustomsOfficeTimetable

- **Model:** `datasets/gov/muitine/muitines_istaigos/CustomsOfficeTimetable`[^manifest]
- **Dataset:** [datasets/gov/muitine/muitines_istaigos](../muitines_istaigos.md) (`datasets/gov/muitine/muitines_istaigos`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_istaigos.csv#L57](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L57)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | — | — |
| `customs_office` | `ref` | [CustomsOffice](CustomsOffice.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `season_code` | `integer` | — | `3` | `open` | — | Sezono kodas | — |
| `season_name` | `string` | — | `3` | `open` | — | Sezono pavadinimas | — |
| `season_start_date` | `date` | `10D` | `4` | `open` | — | Sezono pradžios data | — |
| `season_end_date` | `date` | `10D` | `4` | `open` | — | Sezono pabaigos data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `season_code` | `1` | — | — | 1 | — |
| `season_code` | `2` | — | — | 2 | — |
| `season_code` | `3` | — | — | 3 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv
