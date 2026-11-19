---
type: Table
title: "Versija — DRG versijos"
description: "AR-DRG klasifikacijos versija"
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg/Versija"
tags: [gov, vlk, versija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L45"
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg.csv#L45"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1384/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/drg"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Versija — DRG versijos

AR-DRG klasifikacijos versija[^manifest]

- **Model:** `datasets/gov/vlk/drg/Versija`[^manifest]
- **Dataset:** [DRG sąrašas](../drg.md) (`datasets/gov/vlk/drg`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/drg.csv#L45](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L45)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg/Versija` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `versija` | `string` | — | `4` | `open` | — | Versija | AR-DRG klasifikacijos versija |
| `nuo` | `date` | `D` | `4` | `open` | — | Versija galioja nuo | AR-DRG klasifikacijos versijos galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Versija galioja iki | AR-DRG klasifikacijos versijos galiojimo pabaigos data |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg.csv#L45 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L45)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/drg (https://data.gov.lt/datasets/1384/)
