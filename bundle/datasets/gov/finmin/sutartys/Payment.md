---
type: Table
title: "Payment — Projekto mokėjimo prašymas"
description: "Spinta table datasets/gov/finmin/sutartys/Payment (26 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/Payment"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L145"
    last_modified: "2026-11-11T14:39:20Z"
---

# Payment — Projekto mokėjimo prašymas

- **Model:** `datasets/gov/finmin/sutartys/Payment`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L145](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L145)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/Payment`
- **Primary Key (`ref`):** `payment_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `payment_id` | `string` | — | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `project_hash` | `string` | — | `4` | `open` | — | Šifruotas projekto identifikatorius | Skirtas tik jungimui su kitomis Payment ir Repayment lentelėmis |
| `sfmis_no` | `string` | — | `4` | `open` | — | SFMIS mokėjimo prašymo numeris | — |
| `received` | `datetime` | `L` | `4` | `open` | — | Mokėjimo prašymo gavimo data | — |
| `executor_given` | `date` | `D` | `4` | `open` | — | Vykdytojo nurodyta mokėjimo prašymo data | — |
| `revised` | `date` | `D` | `4` | `open` | — | Mokėjimo prašymo patikslinimo data | — |
| `type` | `string` | — | `3` | `open` | — | Mokėjimo prašymo tipas | — |
| `advance_insurance` | `boolean` | — | `4` | `open` | — | Taikomas avanso draudimas | — |
| `is_paid` | `boolean` | — | `4` | `open` | — | Apmokėtas mokėjimo prašymas | — |
| `report_from` | `date` | `D` | `4` | `open` | — | Mokėjimo prašymo ataskaitinio laikotarpio pradžia | — |
| `report_till` | `date` | `D` | `4` | `open` | — | Mokėjimo prašymo ataskaitinio laikotarpio pabaiga | — |
| `state` | `string` | — | `3` | `open` | — | Mokėjimo prašymo būsena | — |
| `state_updated` | `datetime` | `L` | `4` | `open` | — | Mokėjimo prašymo būsenos data | — |
| `request_amount` | `number` | — | `2` | `open` | — | Prašoma suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `advance_set` | `number` | — | `2` | `open` | — | Prašoma užskaityti avanso suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `advance_set_eu` | `number` | — | `2` | `open` | — | Prašoma užskaityti avanso suma (ES) | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `advance_set_gf` | `number` | — | `2` | `open` | — | Prašoma užskaityti avanso suma (BF) | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `part1_state` | `string` | — | `3` | `open` | — | Mokėjimo prašymo 1-os dalies būsena | — |
| `part1_state_updated` | `datetime` | `L` | `4` | `open` | — | MPD1 būsenos data | — |
| `part1_state_decided` | `date` | `D` | `4` | `open` | — | MPD1 būsenos sprendimo data | — |
| `part4_state` | `string` | — | `3` | `open` | — | Mokėjimo prašymo 4-os dalies būsena | — |
| `part4_state_updated` | `datetime` | `L` | `4` | `open` | — | MPD4 būsenos data | — |
| `part4_state_decided` | `date` | `D` | `4` | `open` | — | MPD4 būsenos sprendimo data | — |
| `principles` | `boolean` | — | `4` | `open` | — | Projekto įgyvendinimo metu buvo užtikrintas horizontaliųjų principų laikymasis | — |
| `progress` | `boolean` | — | `4` | `open` | — | Darnus vystymasis | — |
| `gender_equality` | `boolean` | — | `4` | `open` | — | Moterų ir vyrų lygybė ir (arba) nediskriminavimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `request_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `advance_set` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `advance_set_eu` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `advance_set_gf` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
