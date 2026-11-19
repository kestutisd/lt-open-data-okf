---
type: Table
title: "RepaymentPart — Projekto grąžintinų lėšų dalys"
description: "Spinta table datasets/gov/finmin/sutartys/RepaymentPart (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/RepaymentPart"
tags: [gov, finmin, repaymentpart, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L328"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L328"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# RepaymentPart — Projekto grąžintinų lėšų dalys

- **Model:** `datasets/gov/finmin/sutartys/RepaymentPart`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L328](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L328)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/RepaymentPart` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `repayment_part_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `repayment_part_id` | `string` | — | `4` | `open` | — | Grąžintinų lėšų dalies identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Grąžintinų lėšų dalies SFMIS numeris | — |
| `pay_part23` | `ref` | [PayPart23](PayPart23.md) (`level=4 UUID`: `pay_part23._id`) | `4` | `open` | — | Mokėjimo prašymo dalies identifikatorius | — |
| `amount` | `number` | — | `2` | `open` | — | Grąžintinų lėšų dalies suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `declare_by` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų dalies deklaruotinumo EK data | — |
| `declared` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų dalies deklaravimo EK data | — |
| `account_submitted` | `date` | `D` | `4` | `open` | — | Grąžintinų lėšų dalies sąskaitų EK teikimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L328 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L328)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
