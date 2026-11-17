---
type: Table
title: "PurchasePlanCorrectionPurchase — Pataisytas projekto pirkimo plano pirkimas"
description: "Spinta table datasets/gov/finmin/sutartys/PurchasePlanCorrectionPurchase (20 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchasePlanCorrectionPurchase"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L474"
    last_modified: "2026-11-11T14:39:20Z"
---

# PurchasePlanCorrectionPurchase — Pataisytas projekto pirkimo plano pirkimas

- **Model:** `datasets/gov/finmin/sutartys/PurchasePlanCorrectionPurchase`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L474](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L474)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchasePlanCorrectionPurchase`
- **Primary Key (`ref`):** `purchase_corr_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `purchase_corr_id` | `string` | — | `4` | `open` | — | Pataisyto pirkimo identifikatorius | — |
| `purchase_plan_corr` | `ref` | [PurchasePlanCorrection](PurchasePlanCorrection.md) | `4` | `open` | — | Projekto pirkimų plano keitimo identifikatorius | — |
| `purchase` | `ref` | [Purchase](Purchase.md) | `4` | `open` | — | Pirkimo identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Pirkimo eilės numeris | — |
| `subject` | `string` | — | `2` | `open` | — | Pirkimą vykdantis subjektas | Fiziniams ir panašiems asmenims vertės pašalintos |
| `subject_code` | `string` | — | `2` | `open` | — | Pirkimą vykdančio subjekto JAR kodas | Užsienio pareiškėjams nurodyti analogiški kodai. Fiziniams asmenims vertės pašalintos |
| `subject_status` | `string` | — | `3` | `open` | — | Pirkimą vykdančio subjekto statusas | — |
| `link` | `boolean` | — | `4` | `open` | — | Pirkimo sąsaja su kitu projektu | — |
| `object` | `string` | — | `4` | `open` | — | Pirkimo objektas | Retos vertės konfidencialumo tikslais nerodomos. |
| `object_type` | `string` | — | `3` | `open` | — | Pirkimo objekto rūšis | — |
| `method` | `string` | — | `3` | `open` | — | Pirkimo būdas | — |
| `contract_plan_fin_value` | `number` | — | `2` | `open` | — | Planuojamos pirkimo sutarties vertė, finansuojama projekto lėšomis | — |
| `planned` | `date` | `D` | `4` | `open` | — | Planuojamo pirkimo data | — |
| `executed` | `date` | `D` | `4` | `open` | — | Vykdomo pirkimo data | — |
| `implemented` | `date` | `D` | `4` | `open` | — | Įvykdyto pirkimo data | — |
| `status` | `string` | — | `3` | `open` | — | Pirkimo būsena | — |
| `status_updated` | `date` | `D` | `4` | `open` | — | Pirkimo būsenos data | — |
| `contract_amount` | `number` | — | `2` | `open` | — | Pirkimo sutarčių suma, susijusi su projektu | — |
| `split_into_parts` | `string` | — | `2` | `open` | — | Požymis, ar pirkimas skaidomas į dalis | — |
| `concluded_preliminary_contract` | `string` | — | `2` | `open` | — | Požymis, ar sudaroma preliminarioji sutartis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `contract_plan_fin_value` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `contract_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
