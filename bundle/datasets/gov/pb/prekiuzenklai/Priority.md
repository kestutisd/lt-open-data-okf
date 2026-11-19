---
type: Table
title: "Priority — Priority"
description: "Spinta table datasets/gov/pb/prekiuzenklai/Priority (3 columns)."
tags: [gov, pb, priority, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L37"
    title: "atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L37"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priority — Priority

- **Model:** `datasets/gov/pb/prekiuzenklai/Priority`[^manifest]
- **Dataset:** [Prekių ženklai](../prekiuzenklai.md) (`datasets/gov/pb/prekiuzenklai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/prekiuzenklai.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L37)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `priority_number`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priority_country_code` | `string` | — | `3` | `open` | — | Priority country code | — |
| `priority_number` | `integer` | — | `4` | `open` | — | Priority number | — |
| `priority_date` | `date` | `D` | `4` | `open` | — | Priority date | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L37 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L37)
