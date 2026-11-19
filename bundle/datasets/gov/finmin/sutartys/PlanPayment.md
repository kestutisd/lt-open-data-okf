---
type: Table
title: "PlanPayment — Projekto mokėjimo prašymo teikimo grafiko planuojamas mokėjimo prašymas"
description: "Spinta table datasets/gov/finmin/sutartys/PlanPayment (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PlanPayment"
tags: [gov, finmin, planpayment, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L354"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L354"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PlanPayment — Projekto mokėjimo prašymo teikimo grafiko planuojamas mokėjimo prašymas

- **Model:** `datasets/gov/finmin/sutartys/PlanPayment`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L354](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L354)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PlanPayment` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `plan_payment_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `plan_payment_id` | `string` | — | `4` | `open` | — | Planuojamo mokėjimo prašymo identifikatorius | — |
| `pay_schedule` | `ref` | [PaySchedule](PaySchedule.md) (`level=4 UUID`: `pay_schedule._id`) | `4` | `open` | — | Mokėjimo grafiko identifikatorius | — |
| `created` | `date` | `D` | `4` | `open` | — | Planuojamo mokėjimo prašymo teikimo data | — |
| `amount` | `number` | — | `2` | `open` | — | Planuojamo mokėjimo prašymo suma | — |
| `advance_amount` | `number` | — | `2` | `open` | — | Planuojamo mokėjimo prašymo avanso užskaitos suma | — |
| `type` | `string` | — | `2` | `open` | — | Planuojamo mokėjimo prašymo tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `advance_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L354 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L354)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
