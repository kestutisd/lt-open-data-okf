---
type: Table
title: "MarkImageCategory — Mark image category"
description: "Spinta table datasets/gov/pb/prekiuzenklai/MarkImageCategory (2 columns)."
tags: [gov, pb, markimagecategory, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MarkImageCategory — Mark image category

- **Model:** `datasets/gov/pb/prekiuzenklai/MarkImageCategory`[^manifest]
- **Dataset:** [Prekių ženklai](../prekiuzenklai.md) (`datasets/gov/pb/prekiuzenklai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/prekiuzenklai.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `category_code`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mark_image` | `ref` | [MarkImage](MarkImage.md) (`level=4 UUID`: `mark_image._id`) | `4` | `open` | — | — | — |
| `category_code` | `string` | — | `4` | `open` | — | Category code | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L30)
