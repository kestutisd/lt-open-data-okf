---
type: Table
title: "ForeignTC"
description: "Tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų technikos komitetai ir jų darbo grupės"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/ForeignTC"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L187"
    last_modified: "2026-11-11T14:39:20Z"
---

# ForeignTC

Tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų technikos komitetai ir jų darbo grupės

- **Model:** `datasets/gov/lst/standards/ForeignTC`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L187](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L187)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/ForeignTC`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `organisation` | `ref` | [Organisation](Organisation.md) | — | `open` | — | — | — |
| `status` | `ref` | [OrganisationUnitStatus](OrganisationUnitStatus.md) | — | `open` | — | — | — |
| `name` | `string` | — | — | `open` | — | — | — |
| `description` | `string` | — | — | `open` | — | — | — |
| `secretary_name` | `string` | — | — | `open` | — | — | — |
| `description_lt` | `string` | — | — | `open` | — | — | — |
| `membership_status` | `ref` | [ForeignTcMembershipStatus](ForeignTcMembershipStatus.md) | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
