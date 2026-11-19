---
type: Table
title: "Priority"
description: "Spinta table datasets/gov/pb/dizainai/Priority (3 columns)."
tags: [gov, pb, priority, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L34"
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv#L34"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priority

- **Model:** `datasets/gov/pb/dizainai/Priority`[^manifest]
- **Dataset:** [Dizainai](../dizainai.md) (`datasets/gov/pb/dizainai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L34)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `priority_number`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priority_country_code` | `string` | — | `3` | `open` | — | Prioriteto šalies kodas | — |
| `priority_number` | `integer` | — | `4` | `open` | — | Prioriteto numeris | — |
| `priority_date` | `date` | `D` | `4` | `open` | — | Prioriteto data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv#L34 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L34)
