---
type: Table
title: "ClassDescription — Class description"
description: "Spinta table datasets/gov/pb/prekiuzenklai/ClassDescription (2 columns)."
tags: [gov, pb, classdescription, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ClassDescription — Class description

- **Model:** `datasets/gov/pb/prekiuzenklai/ClassDescription`[^manifest]
- **Dataset:** [Prekių ženklai](../prekiuzenklai.md) (`datasets/gov/pb/prekiuzenklai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/prekiuzenklai.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `class_number`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `class_number` | `integer` | — | `3` | `open` | — | Class number | — |
| `goods_services_description_lt` | `string` | — | `2` | `open` | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `goods_services_description_lt` | `update(property:"goods_services_description@lt, type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L33)
