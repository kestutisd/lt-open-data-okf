---
type: Table
title: "ApplicantAddress"
description: "Spinta table datasets/gov/pb/patentai/ApplicantAddress (2 columns)."
tags: [gov, pb, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/patentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L39"
    last_modified: "2026-11-11T14:39:20Z"
---

# ApplicantAddress

- **Model:** `datasets/gov/pb/patentai/ApplicantAddress`[^manifest]
- **Dataset:** [Patentai](../patentai.md) (`datasets/gov/pb/patentai`)
- **Manifest CSV:** [datasets/gov/pb/patentai.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L39)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `country`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `applicant` | `ref` | [Applicant](Applicant.md) | `4` | `open` | — | — | — |
| `country` | `string` | — | `3` | `open` | — | Pareiškėjo šalis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/patentai.csv
