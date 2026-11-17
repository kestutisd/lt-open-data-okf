---
type: Table
title: "StandardICS"
description: "Standartui priskirtos tarptautinės standartų klasifikacijos sritys, grupės ir pogrupiai"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/StandardICS"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L319"
    last_modified: "2026-11-11T14:39:20Z"
---

# StandardICS

Standartui priskirtos tarptautinės standartų klasifikacijos sritys, grupės ir pogrupiai

- **Model:** `datasets/gov/lst/standards/StandardICS`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L319](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L319)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/StandardICS`
- **Primary Key (`ref`):** `standard, ics`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `standard` | `ref` | [Standard](Standard.md) | — | `open` | — | — | — |
| `ics` | `ref` | [ICS](ICS.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
