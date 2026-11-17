---
type: Table
title: "CustomsOfficeRoleTraffic"
description: "Spinta table datasets/gov/muitine/muitines_istaigos/CustomsOfficeRoleTraffic (4 columns)."
tags: [gov, muitine, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L74"
    last_modified: "2026-11-11T14:39:20Z"
---

# CustomsOfficeRoleTraffic

- **Model:** `datasets/gov/muitine/muitines_istaigos/CustomsOfficeRoleTraffic`[^manifest]
- **Dataset:** [datasets/gov/muitine/muitines_istaigos](../muitines_istaigos.md) (`datasets/gov/muitine/muitines_istaigos`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_istaigos.csv#L74](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L74)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | — | — |
| `customs_office_timetable_line` | `ref` | [CustomsOfficeTimetableLine](CustomsOfficeTimetableLine.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `role` | `ref` | [/datasets/gov/muitine/muitines_funkcijos/CustomsOfficeNationalRole](../muitines_funkcijos/CustomsOfficeNationalRole.md) | `4` | `open` | — | Muitinės įstaigos atliekamos funkcijos | — |
| `traffic_type` | `string` | — | `3` | `open` | — | Transporto rūšis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `traffic_type` | `"R"` | — | — | Kelių transportas | — |
| `traffic_type` | `"V"` | — | — | Geležinkelių transportas | — |
| `traffic_type` | `"AIR"` | — | — | Oro transportas | — |
| `traffic_type` | `"C"` | — | — | Upių transportas | — |
| `traffic_type` | `"N/A"` | — | — | Nežinomas | — |
| `traffic_type` | `"P"` | — | — | Jūrų transportas | — |
| `traffic_type` | `"PP"` | — | — | Vamzdynai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv
