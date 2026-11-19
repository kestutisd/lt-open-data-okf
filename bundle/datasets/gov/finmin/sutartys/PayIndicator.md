---
type: Table
title: "PayIndicator — Projekto mokėjimo prašymo dalies Nr. 1 produkto ir rezultato stebėsenos rodikliai"
description: "Spinta table datasets/gov/finmin/sutartys/PayIndicator (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayIndicator"
tags: [gov, finmin, payindicator, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L227"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L227"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PayIndicator — Projekto mokėjimo prašymo dalies Nr. 1 produkto ir rezultato stebėsenos rodikliai

- **Model:** `datasets/gov/finmin/sutartys/PayIndicator`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L227](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L227)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayIndicator` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pay_indicator_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_indicator_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies stebėsenos rodiklio identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) (`level=4 UUID`: `payment._id`) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `measure_indicator` | `ref` | [MeasureIndicator](../kvietimai/MeasureIndicator.md) (`level=4 UUID`: `measure_indicator._id`) | `4` | `open` | — | Priemonės stebėsenos rodiklio identifikatorius | — |
| `name` | `string` | — | `4` | `open` | — | Rodiklio pavadinimas | — |
| `code` | `string` | — | `4` | `open` | — | Rodiklio kodas | — |
| `type` | `string` | — | `3` | `open` | — | Rodiklio tipas | — |
| `unit` | `string` | — | `4` | `open` | — | Siektinos reikšmės matavimo vienetas | — |
| `con_value` | `number` | — | `4` | `open` | — | Rodiklio siektina reikšmė | — |
| `pay_value` | `number` | — | `4` | `open` | — | Rodiklio pasiekta reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L227 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L227)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
