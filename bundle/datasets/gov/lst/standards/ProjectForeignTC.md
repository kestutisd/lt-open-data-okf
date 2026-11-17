---
type: Table
title: "ProjectForeignTC"
description: "Standarto projektą parengęs tarptautinės standartizacijos institucijos arba Europos standartizacijos organizacijos technikos komitetas"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/ProjectForeignTC"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L238"
    last_modified: "2026-11-11T14:39:20Z"
---

# ProjectForeignTC

Standarto projektą parengęs tarptautinės standartizacijos institucijos arba Europos standartizacijos organizacijos technikos komitetas

- **Model:** `datasets/gov/lst/standards/ProjectForeignTC`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L238](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L238)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/ProjectForeignTC`
- **Primary Key (`ref`):** `project, foreign_tc`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `project` | `ref` | [Project](Project.md) | — | `open` | — | — | — |
| `foreign_tc` | `ref` | [ForeignTC](ForeignTC.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
