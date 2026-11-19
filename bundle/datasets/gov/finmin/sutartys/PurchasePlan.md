---
type: Table
title: "PurchasePlan — Projekto pirkimo planas"
description: "Spinta table datasets/gov/finmin/sutartys/PurchasePlan (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchasePlan"
tags: [gov, finmin, purchaseplan, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L374"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L374"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PurchasePlan — Projekto pirkimo planas

- **Model:** `datasets/gov/finmin/sutartys/PurchasePlan`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L374](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L374)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchasePlan` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `purchase_plan_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `purchase_plan_id` | `string` | — | `4` | `open` | — | Projekto pirkimų plano identifikatorius | — |
| `project` | `ref` | [Payment](Payment.md) (`level=3`: `project.project_hash`) | `3` | `open` | — | Šifruotas projekto identifikatorius | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L374 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L374)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
