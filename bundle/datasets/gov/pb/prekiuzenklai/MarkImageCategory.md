---
type: Table
title: "MarkImageCategory — Mark image category"
description: "Spinta table datasets/gov/pb/prekiuzenklai/MarkImageCategory (2 columns)."
tags: [gov, pb, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L30"
    last_modified: "2026-11-11T14:39:20Z"
---

# MarkImageCategory — Mark image category

- **Model:** `datasets/gov/pb/prekiuzenklai/MarkImageCategory`[^manifest]
- **Dataset:** [Prekių ženklai](../prekiuzenklai.md) (`datasets/gov/pb/prekiuzenklai`)
- **Manifest CSV:** [datasets/gov/pb/prekiuzenklai.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L30)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `category_code`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mark_image` | `ref` | [MarkImage](MarkImage.md) | `4` | `open` | — | — | — |
| `category_code` | `string` | — | `4` | `open` | — | Category code | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv
