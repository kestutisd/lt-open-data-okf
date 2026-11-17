---
type: Table
title: "OrganisationUnit"
description: "Lietuvos standartizacijos departamento technikos komitetai ir laikinosios darbo grupės"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/OrganisationUnit"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L197"
    last_modified: "2026-11-11T14:39:20Z"
---

# OrganisationUnit

Lietuvos standartizacijos departamento technikos komitetai ir laikinosios darbo grupės

- **Model:** `datasets/gov/lst/standards/OrganisationUnit`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L197](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L197)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/OrganisationUnit`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `organisation` | `ref` | [Organisation](Organisation.md) | — | `open` | — | — | — |
| `type` | `ref` | [OrganisationUnitType](OrganisationUnitType.md) | — | `open` | — | — | — |
| `status` | `ref` | [OrganisationUnitStatus](OrganisationUnitStatus.md) | — | `open` | — | — | — |
| `reporting_ou` | `integer` | — | — | `open` | — | — | — |
| `identifier` | `string` | — | — | `open` | — | — | — |
| `modification_date` | `datetime` | — | — | `open` | — | — | — |
| `creation_date` | `datetime` | — | — | `open` | — | — | — |
| `status_date` | `datetime` | — | — | `open` | — | — | — |
| `address` | `string` | — | — | `open` | — | — | — |
| `operational_risk` | `string` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
