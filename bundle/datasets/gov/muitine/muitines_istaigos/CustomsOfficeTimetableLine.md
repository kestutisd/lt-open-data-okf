---
type: Table
title: "CustomsOfficeTimetableLine"
description: "Spinta table datasets/gov/muitine/muitines_istaigos/CustomsOfficeTimetableLine (6 columns)."
tags: [gov, muitine, customsofficetimetableline, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L67"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv#L67"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# CustomsOfficeTimetableLine

- **Model:** `datasets/gov/muitine/muitines_istaigos/CustomsOfficeTimetableLine`[^manifest]
- **Dataset:** [datasets/gov/muitine/muitines_istaigos](../muitines_istaigos.md) (`datasets/gov/muitine/muitines_istaigos`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_istaigos.csv#L67](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L67)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | — | — |
| `customs_office_timetable` | `ref` | [CustomsOfficeTimetable](CustomsOfficeTimetable.md) (`level=4 UUID`: `customs_office_timetable._id`) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `begin_day` | `string` | — | `3` | `open` | — | Savaitės diena nuo | — |
| `hour_from` | `string` | — | `3` | `open` | — | Darbo dienos pradžia | — |
| `hour_to` | `string` | — | `3` | `open` | — | Darbo dienos pabaiga | — |
| `end_day` | `string` | — | `3` | `open` | — | Savaitės diena iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv#L67 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L67)
