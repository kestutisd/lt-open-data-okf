---
type: Table
title: "PkItraukimas"
description: "Spinta table datasets/gov/vsdfv/pkdalyviai/PkItraukimas (3 columns)."
tags: [gov, vsdfv, pkitraukimas, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# PkItraukimas

- **Model:** `datasets/gov/vsdfv/pkdalyviai/PkItraukimas`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/pkdalyviai](../pkdalyviai.md) (`datasets/gov/vsdfv/pkdalyviai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/pkdalyviai.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `metai`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L18)
