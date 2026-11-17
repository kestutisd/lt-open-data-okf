---
type: Table
title: "OrganisationUnitText"
description: "Lietuvos standartizacijos departamento technikos komitetų ir laikinųjų darbo grupių duomenys (pavadinimai, veiklos sritys, veiklos rizikos)"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/OrganisationUnitText"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L231"
    last_modified: "2026-11-11T14:39:20Z"
---

# OrganisationUnitText

Lietuvos standartizacijos departamento technikos komitetų ir laikinųjų darbo grupių duomenys (pavadinimai, veiklos sritys, veiklos rizikos)

- **Model:** `datasets/gov/lst/standards/OrganisationUnitText`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L231](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L231)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/OrganisationUnitText`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `text_type` | `ref` | [TextType](TextType.md) | — | `open` | — | — | — |
| `language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `organisation_unit` | `ref` | [OrganisationUnit](OrganisationUnit.md) | — | `open` | — | — | — |
| `text` | `string` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
