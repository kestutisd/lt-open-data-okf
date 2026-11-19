---
type: Table
title: "TradeMark — Trademark"
description: "Spinta table datasets/gov/pb/prekiuzenklai/TradeMark (12 columns)."
tags: [gov, pb, trademark, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# TradeMark — Trademark

- **Model:** `datasets/gov/pb/prekiuzenklai/TradeMark`[^manifest]
- **Dataset:** [Prekių ženklai](../prekiuzenklai.md) (`datasets/gov/pb/prekiuzenklai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/prekiuzenklai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `application_number`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `application_number` | `string` | — | `4` | `open` | — | Application number | — |
| `application_date` | `date` | `D` | `4` | `open` | — | Application date | — |
| `application_language_code` | `string` | — | `3` | `open` | — | Application language code | — |
| `registration_number` | `integer` | — | `4` | `open` | — | Registration number | — |
| `registration_date` | `date` | `D` | `4` | `open` | — | Registration date | — |
| `expiry_date` | `date` | `D` | `4` | `open` | — | Expiry date | — |
| `mark_current_status_code` | `string` | — | `3` | `open` | — | Mark current status code | — |
| `mark_current_status_date` | `date` | `D` | `4` | `open` | — | Mark current status date | — |
| `kind_mark` | `string` | — | `3` | `open` | — | Kinda mark | — |
| `mark_feature` | `string` | — | `3` | `open` | — | Mark feature | — |
| `opposition_period_start_date` | `date` | `D` | `4` | `open` | — | Opposition period start date | — |
| `opposition_period_end_date` | `date` | `D` | `4` | `open` | — | Opposition period end date | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L13)
