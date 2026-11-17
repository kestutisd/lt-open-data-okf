---
type: Table
title: "Design"
description: "Spinta table datasets/gov/pb/dizainai/Design (13 columns)."
tags: [gov, pb, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Design

- **Model:** `datasets/gov/pb/dizainai/Design`[^manifest]
- **Dataset:** [Dizainai](../dizainai.md) (`datasets/gov/pb/dizainai`)
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `application_number`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv
