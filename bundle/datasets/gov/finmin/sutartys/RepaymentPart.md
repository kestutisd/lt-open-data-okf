---
type: Table
title: "RepaymentPart — Projekto grąžintinų lėšų dalys"
description: "Spinta table datasets/gov/finmin/sutartys/RepaymentPart (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/RepaymentPart"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L328"
    last_modified: "2026-11-11T14:39:20Z"
---

# RepaymentPart — Projekto grąžintinų lėšų dalys

- **Model:** `datasets/gov/finmin/sutartys/RepaymentPart`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L328](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L328)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/RepaymentPart`
- **Primary Key (`ref`):** `repayment_part_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `repayment_part_id` | `string` | — | `4` | `open` | — | Grąžintinų lėšų dalies identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Grąžintinų lėšų dalies SFMIS numeris | — |
| `pay_part23` | `ref` | [PayPart23](PayPart23.md) | `4` | `open` | — | Mokėjimo prašymo dalies identifikatorius | — |
| `amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų dalies suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `declare_by` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų dalies deklaruotinumo EK data | — |
| `declared` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų dalies deklaravimo EK data | — |
| `account_submitted` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų dalies sąskaitų EK teikimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
