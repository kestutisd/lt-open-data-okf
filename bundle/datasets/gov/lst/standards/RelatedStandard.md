---
type: Table
title: "RelatedStandard"
description: "Standarto ryšys su kitais standartais (pakeičia, keitinys, pataisa)"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/RelatedStandard"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L297"
    last_modified: "2026-11-11T14:39:20Z"
---

# RelatedStandard

Standarto ryšys su kitais standartais (pakeičia, keitinys, pataisa)

- **Model:** `datasets/gov/lst/standards/RelatedStandard`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L297](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L297)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/RelatedStandard`
- **Primary Key (`ref`):** `parent_standard, child_standard`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `parent_standard` | `ref` | [Standard](Standard.md) | — | `open` | — | — | — |
| `child_standard` | `ref` | [Standard](Standard.md) | — | `open` | — | — | — |
| `standard_relation_type` | `ref` | [StandardRelationType](StandardRelationType.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
