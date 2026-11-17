---
type: Table
title: "ConBudgetParent — Sutarties projekto biudžetas (\"tėviniai\" objektai)"
description: "Spinta table datasets/gov/finmin/sutartys/ConBudgetParent (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConBudgetParent"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L99"
    last_modified: "2026-11-11T14:39:20Z"
---

# ConBudgetParent — Sutarties projekto biudžetas ("tėviniai" objektai)

- **Model:** `datasets/gov/finmin/sutartys/ConBudgetParent`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L99](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L99)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConBudgetParent`
- **Primary Key (`ref`):** `con_budget_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_budget_id` | `string` | — | `4` | `open` | — | Biudžeto identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Biudžeto eilutės numeris | — |
| `amount` | `number` | — | `2` | `open` | — | Biudžeto eilutės tinkamų finansuoti išlaidų suma | — |
| `fin_amount` | `number` | — | `2` | `open` | — | Biudžeto eilutės skiriamos finansavimo lėšos | — |
| `contribution_expense` | `number` | — | `2` | `open` | — | Išlaidos, kurios negali viršyti nuosavo įnašo | — |
| `staff_expense` | `number` | — | `2` | `open` | — | Vykdančiojo personalo išlaidos | — |
| `activity_expense` | `number` | — | `2` | `open` | — | Veiklų rangos išlaidų dalis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `fin_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `contribution_expense` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `staff_expense` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `activity_expense` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
