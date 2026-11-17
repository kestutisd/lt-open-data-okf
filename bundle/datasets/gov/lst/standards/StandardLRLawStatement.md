---
type: Table
title: "StandardLRLawStatement"
description: "Standartų nuorodinių žymenų ryšys su nacionaliniais teisės aktais"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/StandardLRLawStatement"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L323"
    last_modified: "2026-11-11T14:39:20Z"
---

# StandardLRLawStatement

Standartų nuorodinių žymenų ryšys su nacionaliniais teisės aktais

- **Model:** `datasets/gov/lst/standards/StandardLRLawStatement`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L323](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L323)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/StandardLRLawStatement`
- **Primary Key (`ref`):** `standard, lr_law_statement`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `standard` | `ref` | [Standard](Standard.md) | — | `open` | — | — | — |
| `lr_law_statement` | `ref` | [LRLawStatement](LRLawStatement.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
