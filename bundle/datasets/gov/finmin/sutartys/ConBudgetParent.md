---
type: Table
title: "ConBudgetParent — Sutarties projekto biudžetas (\"tėviniai\" objektai)"
description: "Spinta table datasets/gov/finmin/sutartys/ConBudgetParent (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConBudgetParent"
tags: [gov, finmin, conbudgetparent, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L99"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L99"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ConBudgetParent — Sutarties projekto biudžetas ("tėviniai" objektai)

- **Model:** `datasets/gov/finmin/sutartys/ConBudgetParent`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L99](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L99)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConBudgetParent` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `con_budget_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_budget_id` | `string` | — | `4` | `open` | — | Biudžeto identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) (`level=4 UUID`: `project._id`) | `4` | `open` | — | Projekto identifikatorius | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L99 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L99)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
