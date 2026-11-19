---
type: Table
title: "MDMSritis"
description: "Spinta table datasets/gov/miskai/mdm/MDMSritis (2 columns)."
tags: [gov, miskai, mdmsritis, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/mdm.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/miskai/mdm.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MDMSritis

- **Model:** `datasets/gov/miskai/mdm/MDMSritis`[^manifest]
- **Dataset:** [datasets/gov/miskai/mdm](../mdm.md) (`datasets/gov/miskai/mdm`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/mdm.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/mdm.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mdm` | `ref` | [Tiekejas](Tiekejas.md) (`level=4 UUID`: `mdm._id`) | `4` | `open` | — | MDM tiekėjas | — |
| `vs` | `ref` | [VeiklosSritis](VeiklosSritis.md) (`level=4 UUID`: `vs._id`) | `4` | `open` | — | Veiklos sritis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/mdm.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/mdm.csv#L18)
