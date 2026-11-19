---
type: Table
title: "PayInformMeasure — Projekto mokėjimo prašymo dalies Nr. 4. informavimo priemonės"
description: "Spinta table datasets/gov/finmin/sutartys/PayInformMeasure (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayInformMeasure"
tags: [gov, finmin, payinformmeasure, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L215"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L215"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PayInformMeasure — Projekto mokėjimo prašymo dalies Nr. 4. informavimo priemonės

- **Model:** `datasets/gov/finmin/sutartys/PayInformMeasure`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L215](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L215)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayInformMeasure` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pay_inform_measure_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_inform_measure_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies informavimo priemonės identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) (`level=4 UUID`: `payment._id`) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `description` | `string` | — | `4` | `open` | — | Informavimo priemonės aprašymas | — |
| `implementation` | `string` | — | `3` | `open` | — | Informavimo priemonės įgyvendinimo požymis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L215 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L215)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
