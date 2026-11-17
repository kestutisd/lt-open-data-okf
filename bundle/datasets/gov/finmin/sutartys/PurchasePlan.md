---
type: Table
title: "PurchasePlan — Projekto pirkimo planas"
description: "Spinta table datasets/gov/finmin/sutartys/PurchasePlan (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchasePlan"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L374"
    last_modified: "2026-11-11T14:39:20Z"
---

# PurchasePlan — Projekto pirkimo planas

- **Model:** `datasets/gov/finmin/sutartys/PurchasePlan`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L374](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L374)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchasePlan`
- **Primary Key (`ref`):** `purchase_plan_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `purchase_plan_id` | `string` | — | `4` | `open` | — | Projekto pirkimų plano identifikatorius | — |
| `project` | `ref` | [Payment[project_hash]](Payment.md) | `3` | `open` | — | Šifruotas projekto identifikatorius | — |
| `created` | `date` | `D` | `4` | `open` | — | Projekto pirkimų plano data | — |
| `expense_amount` | `number` | — | `2` | `open` | — | Projekto išlaidų suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `amount` | `number` | — | `2` | `open` | — | Planuojamų projekto pirkimų suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `impl_amount` | `number` | — | `2` | `open` | — | Įvykdytų pirkimų tinkamų finansuoti išlaidų suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `no_purchase_amount` | `number` | — | `2` | `open` | — | Projekto išlaidų suma, kuriai netaikomi pirkimai | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `savings_amount` | `number` | — | `2` | `open` | — | Sutaupymai | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `expense_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `impl_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `no_purchase_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `savings_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
