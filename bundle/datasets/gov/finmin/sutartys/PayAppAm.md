---
type: Table
title: "PayAppAm — Projekto mokėjimo prašymo dalies Nr. 2 / Nr. 3 paraiškos asignavimo valdytojui informacija"
description: "Spinta table datasets/gov/finmin/sutartys/PayAppAm (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayAppAm"
tags: [gov, finmin, payappam, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L202"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L202"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PayAppAm — Projekto mokėjimo prašymo dalies Nr. 2 / Nr. 3 paraiškos asignavimo valdytojui informacija

- **Model:** `datasets/gov/finmin/sutartys/PayAppAm`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L202](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L202)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayAppAm` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pay_app_am_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_app_am_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies paraiškos asignavimo valdytojui identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) (`level=4 UUID`: `payment._id`) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Paraiškos AV numeris | — |
| `assigned` | `date` | `D` | `4` | `open` | — | Paraiškos AV data | — |
| `measure` | `ref` | [Measure](../kvietimai/Measure.md) (`level=4 UUID`: `measure._id`) | `4` | `open` | — | Priemonės identifikatorius | — |
| `paid_amount` | `number` | — | `2` | `open` | — | Paraiškos AV išmokama suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `advance_amount` | `number` | — | `2` | `open` | — | Paraiškos AV įvertinta avanso | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `repayment_amount` | `number` | — | `2` | `open` | — | Paraiškos AV įvertinta gražintinų lėšų | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paid_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `advance_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `repayment_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L202 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L202)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
