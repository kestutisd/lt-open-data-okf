---
type: Table
title: "ICSRemark"
description: "Tarptautinės standartų klasifikacijos (ICS) sričių, grupių ar pogrupių paaiškinimai"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/ICSRemark"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L159"
    last_modified: "2026-11-11T14:39:20Z"
---

# ICSRemark

Tarptautinės standartų klasifikacijos (ICS) sričių, grupių ar pogrupių paaiškinimai

- **Model:** `datasets/gov/lst/standards/ICSRemark`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L159](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L159)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/ICSRemark`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ics` | `ref` | [ICS](ICS.md) | — | `open` | — | — | — |
| `remark` | `string` | — | — | `open` | — | — | — |
| `remark_en` | `string` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
