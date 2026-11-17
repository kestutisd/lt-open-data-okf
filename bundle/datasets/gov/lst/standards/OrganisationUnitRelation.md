---
type: Table
title: "OrganisationUnitRelation"
description: "Lietuvos standartizacijos departamento technikos komitetų ryšiai su tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų technikos komitetais"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/OrganisationUnitRelation"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L227"
    last_modified: "2026-11-11T14:39:20Z"
---

# OrganisationUnitRelation

Lietuvos standartizacijos departamento technikos komitetų ryšiai su tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų technikos komitetais

- **Model:** `datasets/gov/lst/standards/OrganisationUnitRelation`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L227](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L227)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/OrganisationUnitRelation`
- **Primary Key (`ref`):** `organisation_unit, foreign_tc`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `organisation_unit` | `ref` | [OrganisationUnit](OrganisationUnit.md) | — | `open` | — | — | — |
| `foreign_tc` | `ref` | [ForeignTC](ForeignTC.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
