---
type: Table
title: "RelatedProject"
description: "Projekto ryšys su pagrindiniu standartu (keičiantis, keitinys, pataisa)"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/RelatedProject"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L210"
    last_modified: "2026-11-11T14:39:20Z"
---

# RelatedProject

Projekto ryšys su pagrindiniu standartu (keičiantis, keitinys, pataisa)

- **Model:** `datasets/gov/lst/standards/RelatedProject`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L210](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L210)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/RelatedProject`
- **Primary Key (`ref`):** `parent_project, child_project`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `parent_project` | `ref` | [Project](Project.md) | — | `open` | — | — | — |
| `child_project` | `ref` | [Project](Project.md) | — | `open` | — | — | — |
| `relation_type` | `ref` | [ProjectRelationType](ProjectRelationType.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
