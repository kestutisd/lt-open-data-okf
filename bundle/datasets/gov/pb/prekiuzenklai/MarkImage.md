---
type: Table
title: "MarkImage — Mark image"
description: "Spinta table datasets/gov/pb/prekiuzenklai/MarkImage (3 columns)."
tags: [gov, pb, markimage, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L26"
    title: "atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L26"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MarkImage — Mark image

- **Model:** `datasets/gov/pb/prekiuzenklai/MarkImage`[^manifest]
- **Dataset:** [Prekių ženklai](../prekiuzenklai.md) (`datasets/gov/pb/prekiuzenklai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/prekiuzenklai.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L26)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `trade_mark, mark_image_uri`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `trade_mark` | `ref` | [TradeMark](TradeMark.md) (`level=4 UUID`: `trade_mark._id`) | `4` | `open` | — | — | — |
| `mark_image_uri` | `string` | — | `3` | `open` | — | Mark image URI | — |
| `mark_image_colour` | `string` | — | — | `open` (inherited) | — | Mark image colour | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L26 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L26)
