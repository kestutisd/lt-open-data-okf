---
type: Table
title: "PkItraukimas"
description: "Spinta table datasets/gov/vsdfv/pkdalyviai/PkItraukimas (3 columns)."
tags: [gov, vsdfv, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# PkItraukimas

- **Model:** `datasets/gov/vsdfv/pkdalyviai/PkItraukimas`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/pkdalyviai](../pkdalyviai.md) (`datasets/gov/vsdfv/pkdalyviai`)
- **Manifest CSV:** [datasets/gov/vsdfv/pkdalyviai.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `metai`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Įtraukimo Metai | Dalyvavimo pensijų kaupime įtraukimo metai |
| `itraukti_dalyviai_sk` | `integer` | — | `4` | `open` | — | Įtrauktų dalyvių skaičius, vnt. | — |
| `dalyviu_likutis_sk` | `integer` | — | `4` | `open` | — | Įtrauktų dalyvių likutis, vnt. | Įtrauktų dalyvių likutis (neatsisakę dalyvauti pensijų kaupime) |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv
