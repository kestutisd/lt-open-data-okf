---
type: Table
title: "RepaymentExpend — Projekto grąžintinų lėšų netinkamos išlaidos"
description: "Spinta table datasets/gov/finmin/sutartys/RepaymentExpend (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/RepaymentExpend"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L308"
    last_modified: "2026-11-11T14:39:20Z"
---

# RepaymentExpend — Projekto grąžintinų lėšų netinkamos išlaidos

- **Model:** `datasets/gov/finmin/sutartys/RepaymentExpend`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L308](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L308)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/RepaymentExpend`
- **Primary Key (`ref`):** `repayment_expend_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `repayment_expend_id` | `string` | — | `4` | `open` | — | Grąžintinų lėšų netinkamų išlaidų identifikatorius | — |
| `repayment` | `ref` | [Repayment](Repayment.md) | `4` | `open` | — | Grąžintinų lėšų identifikatorius | — |
| `total` | `number` | — | `2` | `open` | — | Bendra netinkamų finansuoti išlaidų suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `eu` | `number` | — | `2` | `open` | — | Grąžintinų lėšų suma iš projektui skirtų ES fondo finansuojamų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `gf` | `number` | — | `2` | `open` | — | Grąžintinų lėšų suma iš projektui skirtų BF (bendrojo finansavimo) finansuojamų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `state` | `number` | — | `2` | `open` | — | Grąžintinų lėšų suma iš projektui skirtų valstybės biudžeto finansuojamų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `munic` | `number` | — | `2` | `open` | — | Grąžintinų lėšų suma iš projektui skirtų savivaldybės biudžeto finansuojamų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `state_other` | `number` | — | `2` | `open` | — | Grąžintinų lėšų suma iš projektui skirtų kitų valstybės lėšų šaltinių finansuojamų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `own` | `number` | — | `2` | `open` | — | Grąžintinų lėšų suma iš projektui skirtų nuosavų finansuojamų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `other` | `number` | — | `2` | `open` | — | Grąžintinų lėšų suma iš projektui skirtų kitų lėšų šaltinių finansuojamų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `total` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `eu` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `gf` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `state` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `munic` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `state_other` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `own` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `other` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
