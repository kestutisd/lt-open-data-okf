---
type: Table
title: "ProjectStage"
description: "Standarto projekto rengimo etapai"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/ProjectStage"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L142"
    last_modified: "2026-11-11T14:39:20Z"
---

# ProjectStage

Standarto projekto rengimo etapai

- **Model:** `datasets/gov/lst/standards/ProjectStage`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L142](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L142)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/ProjectStage`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `project` | `ref` | [Project](Project.md) | — | `open` | — | — | — |
| `stage` | `ref` | [Stage](Stage.md) | — | `open` | — | — | — |
| `int_order` | `integer` | — | — | `open` | — | — | — |
| `action_type` | `ref` | [ActionType](ActionType.md) | — | `open` | — | — | — |
| `version` | `integer` | — | — | `open` | — | — | — |
| `duration` | `integer` | — | — | `open` | — | — | — |
| `plan_date` | `datetime` | — | — | `open` | — | — | — |
| `confirmed_plan_date` | `boolean` | — | — | `open` | — | — | — |
| `realized_date` | `datetime` | — | — | `open` | — | — | — |
| `european_stage` | `boolean` | — | — | `open` | — | — | — |
| `done` | `boolean` | — | — | `open` | — | — | — |
| `review_date` | `datetime` | — | — | `open` | — | — | — |
| `procedure_sequence` | `integer` | — | — | `open` | — | — | — |
| `procedure_name` | `string` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
