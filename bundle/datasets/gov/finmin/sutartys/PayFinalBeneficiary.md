---
type: Table
title: "PayFinalBeneficiary — Projekto mokėjimo prašymo dalies Nr. 1 galutinių naudos gavėjų sąrašas"
description: "Spinta table datasets/gov/finmin/sutartys/PayFinalBeneficiary (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayFinalBeneficiary"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L245"
    last_modified: "2026-11-11T14:39:20Z"
---

# PayFinalBeneficiary — Projekto mokėjimo prašymo dalies Nr. 1 galutinių naudos gavėjų sąrašas

- **Model:** `datasets/gov/finmin/sutartys/PayFinalBeneficiary`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L245](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L245)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayFinalBeneficiary`
- **Primary Key (`ref`):** `pay_final_beneficiary_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_final_beneficiary_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies GNG identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `name` | `string` | — | `2` | `open` | — | GNG pavadinimas | Fiziniams ir panašiems asmenims vertės pašalintos |
| `code` | `string` | — | `2` | `open` | — | GNG JAR kodas | Užsienio pareiškėjams nurodyti analogiški kodai. Fiziniams asmenims vertės pašalintos |
| `type` | `string` | — | `3` | `open` | — | GNG tipas | — |
| `amount_committed` | `number` | — | `2` | `open` | — | Įsipareigota skirti suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `amount_paid` | `number` | — | `2` | `open` | — | Sumokėta suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `amount_disbursed` | `number` | — | `2` | `open` | — | Garantuotų išmokėtų paskolų suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `territory` | `string` | — | `3` | `open` | — | Įgyvendinimo teritorija (LT / ES) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount_committed` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `amount_paid` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `amount_disbursed` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
