---
type: Table
title: "ConBudget — Sutarties projekto biudžetas"
description: "Spinta table datasets/gov/finmin/sutartys/ConBudget (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConBudget"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L81"
    last_modified: "2026-11-11T14:39:20Z"
---

# ConBudget — Sutarties projekto biudžetas

- **Model:** `datasets/gov/finmin/sutartys/ConBudget`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L81](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L81)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConBudget`
- **Primary Key (`ref`):** `con_budget_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_budget_id` | `string` | — | `4` | `open` | — | Biudžeto identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Biudžeto eilutės / fizinio rodiklio numeris | — |
| `ph_indicator_unit` | `string` | — | `4` | `open` | — | Fizinio rodiklio matavimo vienetas | — |
| `ph_indicator_aim` | `number` | — | `4` | `open` | — | Fizinio rodiklio vnt. skaičius | — |
| `amount` | `number` | — | `2` | `open` | — | Biudžeto eilutės / fizinio rodiklio tinkamų finansuoti išlaidų suma | — |
| `fin_amount` | `number` | — | `2` | `open` | — | Biudžeto eilutės / fizinio rodiklio skiriamos finansavimo lėšos | — |
| `contribution_expense` | `number` | — | `2` | `open` | — | Išlaidos, kurios negali viršyti nuosavo įnašo | — |
| `staff_expense` | `number` | — | `2` | `open` | — | Vykdančiojo personalo išlaidos | — |
| `activity_expense` | `number` | — | `2` | `open` | — | Veiklų rangos išlaidų dalis | — |
| `parent_con_budget` | `ref` | [ConBudgetParent](ConBudgetParent.md) | `3` | `open` | — | Biudžeto "tėvinio" objekto identifikatorius (fiziniam rodikliui nurodytas biudžeto identifikatorius, kuriam jis priklauso) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `fin_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `contribution_expense` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `staff_expense` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `activity_expense` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
