---
type: Table
title: "PayAppAm — Projekto mokėjimo prašymo dalies Nr. 2 / Nr. 3 paraiškos asignavimo valdytojui informacija"
description: "Spinta table datasets/gov/finmin/sutartys/PayAppAm (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayAppAm"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L202"
    last_modified: "2026-11-11T14:39:20Z"
---

# PayAppAm — Projekto mokėjimo prašymo dalies Nr. 2 / Nr. 3 paraiškos asignavimo valdytojui informacija

- **Model:** `datasets/gov/finmin/sutartys/PayAppAm`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L202](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L202)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayAppAm`
- **Primary Key (`ref`):** `pay_app_am_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_app_am_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies paraiškos asignavimo valdytojui identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Paraiškos AV numeris | — |
| `assigned` | `date` | `D` | `4` | `open` | — | Paraiškos AV data | — |
| `measure` | `ref` | [/datasets/gov/finmin/kvietimai/Measure](../kvietimai/Measure.md) | `4` | `open` | — | Priemonės identifikatorius | — |
| `paid_amount` | `number` | — | `2` | `open` | — | Paraiškos AV išmokama suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `advance_amount` | `number` | — | `2` | `open` | — | Paraiškos AV įvertinta avanso | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `repayment_amount` | `number` | — | `2` | `open` | — | Paraiškos AV įvertinta gražintinų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paid_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `advance_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `repayment_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
