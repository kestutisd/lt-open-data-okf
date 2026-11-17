---
type: Table
title: "PayInformMeasure — Projekto mokėjimo prašymo dalies Nr. 4. informavimo priemonės"
description: "Spinta table datasets/gov/finmin/sutartys/PayInformMeasure (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayInformMeasure"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L215"
    last_modified: "2026-11-11T14:39:20Z"
---

# PayInformMeasure — Projekto mokėjimo prašymo dalies Nr. 4. informavimo priemonės

- **Model:** `datasets/gov/finmin/sutartys/PayInformMeasure`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L215](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L215)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayInformMeasure`
- **Primary Key (`ref`):** `pay_inform_measure_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_inform_measure_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies informavimo priemonės identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `description` | `string` | — | `4` | `open` | — | Informavimo priemonės aprašymas | — |
| `implementation` | `string` | — | `3` | `open` | — | Informavimo priemonės įgyvendinimo požymis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
