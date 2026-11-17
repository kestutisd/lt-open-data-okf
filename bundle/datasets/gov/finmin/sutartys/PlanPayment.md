---
type: Table
title: "PlanPayment — Projekto mokėjimo prašymo teikimo grafiko planuojamas mokėjimo prašymas"
description: "Spinta table datasets/gov/finmin/sutartys/PlanPayment (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PlanPayment"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L354"
    last_modified: "2026-11-11T14:39:20Z"
---

# PlanPayment — Projekto mokėjimo prašymo teikimo grafiko planuojamas mokėjimo prašymas

- **Model:** `datasets/gov/finmin/sutartys/PlanPayment`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L354](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L354)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PlanPayment`
- **Primary Key (`ref`):** `plan_payment_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `plan_payment_id` | `string` | — | `4` | `open` | — | Planuojamo mokėjimo prašymo identifikatorius | — |
| `pay_schedule` | `ref` | [PaySchedule](PaySchedule.md) | `4` | `open` | — | Mokėjimo grafiko identifikatorius | — |
| `created` | `date` | `D` | `4` | `open` | — | Planuojamo mokėjimo prašymo teikimo data | — |
| `amount` | `number` | — | `2` | `open` | — | Planuojamo mokėjimo prašymo suma | — |
| `advance_amount` | `number` | — | `2` | `open` | — | Planuojamo mokėjimo prašymo avanso užskaitos suma | — |
| `type` | `string` | — | `2` | `open` | — | Planuojamo mokėjimo prašymo tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `advance_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
