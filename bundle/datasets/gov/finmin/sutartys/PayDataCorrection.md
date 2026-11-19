---
type: Table
title: "PayDataCorrection — Projekto mokėjimo prašymo dalies Nr. 1 duomenų koregavimų sąrašas"
description: "Spinta table datasets/gov/finmin/sutartys/PayDataCorrection (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayDataCorrection"
tags: [gov, finmin, paydatacorrection, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L259"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L259"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PayDataCorrection — Projekto mokėjimo prašymo dalies Nr. 1 duomenų koregavimų sąrašas

- **Model:** `datasets/gov/finmin/sutartys/PayDataCorrection`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L259](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L259)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayDataCorrection` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pay_data_correction_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_data_correction_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies duomenų koregavimų identifikatorius | — |
| `fin_measure_name` | `string` | — | `4` | `open` | — | Finansinės priemonės pavadinimas | — |
| `gng_name` | `string` | — | `2` | `open` | — | GNG pavadinimas | Fiziniams ir panašiems asmenims vertės pašalintos |
| `gng_code` | `string` | — | `2` | `open` | — | GNG JAR kodas | Užsienio pareiškėjams nurodyti analogiški kodai. Fiziniams asmenims vertės pašalintos |
| `gng_type` | `string` | — | `3` | `open` | — | GNG tipas | — |
| `signed` | `date` | `D` | `4` | `open` | — | Sutarties data | — |
| `amount_committed` | `number` | — | `2` | `open` | — | Įsipareigota skirti suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `amount_paid` | `number` | — | `2` | `open` | — | Sumokėta suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `amount_disbursed` | `number` | — | `2` | `open` | — | Garantuotų išmokėtų paskolų suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount_committed` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `amount_paid` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `amount_disbursed` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L259 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L259)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
