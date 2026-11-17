---
type: Table
title: "Project — Projektas ir jo vertinimai"
description: "Spinta table datasets/gov/finmin/paraiskos/Project (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/Project"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Project — Projektas ir jo vertinimai

- **Model:** `datasets/gov/finmin/paraiskos/Project`[^manifest]
- **Dataset:** [datasets/gov/finmin/paraiskos](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/Project`
- **Primary Key (`ref`):** `project_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `project_id` | `string` | — | `4` | `open` | — | Projekto identifikatorius | — |
| `call` | `ref` | [/datasets/gov/finmin/kvietimai/Call](../kvietimai/Call.md) | `4` | `open` | — | Projekto kvietimo/patvirtinto sąrašo identifikatorius | — |
| `code` | `string` | — | `4` | `open` | — | Projekto kodas | — |
| `state` | `string` | — | `3` | `open` | — | Projekto būsena | — |
| `state_date` | `date` | `D` | `4` | `open` | — | Projekto būsenos įgijimo data | — |
| `status` | `string` | — | `3` | `open` | — | Projekto etapas | — |
| `eligibility_result` | `boolean` | — | `4` | `open` | — | Tinkamumo vertinimo rezultatas | — |
| `eligibility_result_date` | `date` | `D` | `4` | `open` | — | Tinkamumo vertinimo rezultato data | — |
| `eligibility_request_amount` | `number` | — | `2` | `open` | — | Tinkamumo vertinimo prašomų lėšų suma | — |
| `eligibility_expense_amount` | `number` | — | `2` | `open` | — | Tinkamumo vertinimo netinkamų išlaidų suma | — |
| `benefit_result` | `boolean` | — | `4` | `open` | — | Naudos ir kokybės vertinimo rezultatas | — |
| `benefit_result_date` | `date` | `D` | `4` | `open` | — | Naudos ir kokybės vertinimo rezultato data | — |
| `benefit_score` | `number` | — | `3` | `open` | — | Vertinimo metu suteiktų balų skaičius | — |
| `decision_result` | `boolean` | — | `4` | `open` | — | Sprendimo dėl finansavimo rezultatas | — |
| `decision_result_date` | `date` | `D` | `4` | `open` | — | Sprendimo dėl finansavimo rezultato data | — |
| `decision_eu_amount` | `number` | — | `2` | `open` | — | Sprendimo dėl finansavimo ES fondų lėšų suma | — |
| `decision_gf_amount` | `number` | — | `2` | `open` | — | Sprendimo dėl finansavimo valstybės biudžeto lėšų suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eligibility_request_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `eligibility_expense_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `decision_eu_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `decision_gf_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv
