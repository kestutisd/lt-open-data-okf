---
type: Table
title: "ProjectStage"
description: "Standarto projekto rengimo etapai"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/ProjectStage"
tags: [gov, lst, projectstage, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L142"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L142"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# ProjectStage

Standarto projekto rengimo etapai[^manifest]

- **Model:** `datasets/gov/lst/standards/ProjectStage`[^manifest]
- **Dataset:** [Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė](../standards.md) (`datasets/gov/lst/standards`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L142](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L142)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/ProjectStage` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L142 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L142)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
