---
type: Table
title: "CustomsOfficeTimetableLine"
description: "Spinta table datasets/gov/muitine/muitines_istaigos/CustomsOfficeTimetableLine (6 columns)."
tags: [gov, muitine, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L67"
    last_modified: "2026-11-11T14:39:20Z"
---

# CustomsOfficeTimetableLine

- **Model:** `datasets/gov/muitine/muitines_istaigos/CustomsOfficeTimetableLine`[^manifest]
- **Dataset:** [datasets/gov/muitine/muitines_istaigos](../muitines_istaigos.md) (`datasets/gov/muitine/muitines_istaigos`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_istaigos.csv#L67](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L67)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | — | — |
| `customs_office_timetable` | `ref` | [CustomsOfficeTimetable](CustomsOfficeTimetable.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `begin_day` | `string` | — | `3` | `open` | — | Savaitės diena nuo | — |
| `hour_from` | `string` | — | `3` | `open` | — | Darbo dienos pradžia | — |
| `hour_to` | `string` | — | `3` | `open` | — | Darbo dienos pabaiga | — |
| `end_day` | `string` | — | `3` | `open` | — | Savaitės diena iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv
