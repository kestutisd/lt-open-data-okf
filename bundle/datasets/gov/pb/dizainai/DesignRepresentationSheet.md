---
type: Table
title: "DesignRepresentationSheet"
description: "Spinta table datasets/gov/pb/dizainai/DesignRepresentationSheet (2 columns)."
tags: [gov, pb, designrepresentationsheet, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# DesignRepresentationSheet

- **Model:** `datasets/gov/pb/dizainai/DesignRepresentationSheet`[^manifest]
- **Dataset:** [Dizainai](../dizainai.md) (`datasets/gov/pb/dizainai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `view_uri`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `design` | `ref` | [Design](Design.md) (`level=4 UUID`: `design._id`) | `4` | `open` | — | — | — |
| `view_uri` | `uri` | — | `3` | `open` | — | Dizaino vaizdo išklotinė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L27)
