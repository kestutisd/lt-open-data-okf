---
type: Table
title: "PublicationReference"
description: "Spinta table datasets/gov/pb/patentai/PublicationReference (4 columns)."
tags: [gov, pb, publicationreference, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L15"
    title: "atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L15"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# PublicationReference

- **Model:** `datasets/gov/pb/patentai/PublicationReference`[^manifest]
- **Dataset:** [Patentai](../patentai.md) (`datasets/gov/pb/patentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/patentai.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L15)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `doc_number`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `country` | `string` | — | `3` | `open` | — | Paskelbimo šalis | — |
| `doc_number` | `string` | — | `4` | `open` | — | Paraiškos numeris | — |
| `kind` | `string` | — | `3` | `open` | — | Dokumento rūšis | — |
| `date` | `date` | — | `4` | `open` | — | Paskelbimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L15 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L15)
