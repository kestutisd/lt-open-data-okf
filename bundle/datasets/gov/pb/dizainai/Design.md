---
type: Table
title: "Design"
description: "Spinta table datasets/gov/pb/dizainai/Design (13 columns)."
tags: [gov, pb, design, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Design

- **Model:** `datasets/gov/pb/dizainai/Design`[^manifest]
- **Dataset:** [Dizainai](../dizainai.md) (`datasets/gov/pb/dizainai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `application_number`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `application_language_code` | `string` | — | `3` | `open` | — | Paraiškos kalbos kodas | — |
| `application_publication_date` | `date` | `D` | `4` | `open` | — | Paraiškos paskelbimo data | — |
| `design_current_status_date` | `date` | `D` | `4` | `open` | — | Esamos paraiškos statuso data | — |
| `registration_office_code` | `string` | — | `3` | `open` | — | Registracijos šalies kodas | — |
| `design_identifier` | `string` | — | `4` | `open` | — | Dizaino idenfitikacinis numeris | — |
| `application_number` | `string` | — | `4` | `open` | — | Paraiškos numeris | — |
| `application_date` | `date` | `D` | `4` | `open` | — | Paraiškos data | — |
| `registration_number` | `string` | — | `4` | `open` | — | Registracijos numeris | — |
| `registration_date` | `date` | `D` | `4` | `open` | — | Registracijos data | — |
| `publication_date` | `date` | `D` | `4` | `open` | — | Publikacijos data | — |
| `design_uri` | `uri` | — | `3` | `open` | — | Dizaino nuoroda | — |
| `expiry_date` | `date` | `D` | `4` | `open` | — | Registracijos galiojimo data | — |
| `design_current_status_code` | `string` | — | `3` | `open` | — | Esamos paraiškos statuso kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L10)
