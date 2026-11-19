---
type: Table
title: "ApplicantResidence"
description: "Spinta table datasets/gov/pb/patentai/ApplicantResidence (2 columns)."
tags: [gov, pb, applicantresidence, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L45"
    title: "atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L45"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ApplicantResidence

- **Model:** `datasets/gov/pb/patentai/ApplicantResidence`[^manifest]
- **Dataset:** [Patentai](../patentai.md) (`datasets/gov/pb/patentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/patentai.csv#L45](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L45)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `country`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `applicant` | `ref` | [Applicant](Applicant.md) (`level=4 UUID`: `applicant._id`) | `4` | `open` | — | — | — |
| `country` | `string` | — | `3` | `open` | — | Pareiškėjo gyvenamoji vieta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L45 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L45)
