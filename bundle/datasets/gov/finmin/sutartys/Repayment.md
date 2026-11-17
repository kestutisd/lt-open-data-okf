---
type: Table
title: "Repayment — Projekto grąžintinos lėšos"
description: "Spinta table datasets/gov/finmin/sutartys/Repayment (23 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/Repayment"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L273"
    last_modified: "2026-11-11T14:39:20Z"
---

# Repayment — Projekto grąžintinos lėšos

- **Model:** `datasets/gov/finmin/sutartys/Repayment`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L273](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L273)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/Repayment`
- **Primary Key (`ref`):** `repayment_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `repayment_id` | `string` | — | `4` | `open` | — | Grąžintinų lėšų identifikatorius | — |
| `project` | `ref` | [Payment[project_hash]](Payment.md) | `3` | `open` | — | Šifruotas projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | SFMIS grąžintinų lėšų numeris | — |
| `registered` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų registravimo data | — |
| `method` | `string` | — | `3` | `open` | — | Grąžintinų lėšų grąžinimo būdas | — |
| `type` | `string` | — | `3` | `open` | — | Grąžintinų lėšų tipas | — |
| `return_till` | `date` | `D` | `4` | `open` | — | Grąžinimo termino data | — |
| `state` | `string` | — | `3` | `open` | — | Grąžintinų lėšų būsena | — |
| `state_updated` | `datetime` | `L` | `4` | `open` | — | Grąžintinų lėšų būsenos data | — |
| `state_decided` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų būsenos sprendimo data | — |
| `violation` | `boolean` | — | `4` | `open` | — | Grąžintinos lėšos yra susijusios su pažeidimu | — |
| `violation_code` | `string` | — | `4` | `open` | — | Grąžintinų lėšų pažeidimo kodas | — |
| `declare_by` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų deklaruotinumo EK data | — |
| `amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų grąžintina suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `fin_amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų grąžintinas finansavimas | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `paid_amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų apmokėta suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `paid_fin_amount` | `number` | — | `2` | `open` | — | Apmokėta grąžinintų lėšų finansavimo suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `treasury_amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų pervestas iždui finansavimas | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `cancel_amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų nurašyta suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `doubtful_amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų abejotina suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `remain_amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų likusi grąžinti suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `remain_fin_amount` | `number` | — | `2` | `open` | — | Likusi grąžinti finansavimo suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `declare_amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų deklaruotina EK suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `fin_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `paid_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `paid_fin_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `treasury_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `cancel_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `doubtful_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `remain_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `remain_fin_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `declare_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
